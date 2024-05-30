#!/usr/bin/env python3
# Author - Luks (@luksecurity_)

import os
import subprocess
import argparse
import requests
from tabulate import tabulate

def download_files(domain, file_type):
    print(f"\033[92m[+] Starting to download {file_type} files\033[0m")
    urls = subprocess.run(f"echo {domain} | gau | grep {file_type}", shell=True, capture_output=True, text=True).stdout.splitlines()

    domain_name = domain.split("//")[-1].split("/")[0]
    file_type_dir = file_type.lstrip('.')
    parent_dir = os.path.join(domain_name, file_type_dir)
    os.makedirs(parent_dir, exist_ok=True)

    for url in urls:
        file_name = os.path.join(domain_name, os.path.basename(url))
        try:
            print(f"Downloading {url} to {file_name}")
            response = requests.get(url)
            response.raise_for_status()

            with open(file_name, 'wb') as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")

def extract_metadata(domain, file_type):
    print("\033[92m[+] Extracting metadata\033[0m")
    domain_name = domain.split("//")[-1].split("/")[0]
    file_pattern = os.path.join(domain_name, f"*{file_type}")
    cmd = f"exiftool {file_pattern} | grep -E '^(Creator|Author|File Name)\\s*:'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    metadata = []
    lines = result.stdout.splitlines()
    current_file = None
    creator = None
    author = None

    for line in lines:
        if line.startswith("File Name"):
            if current_file:
                metadata.append([current_file, creator or "", author or ""])
            current_file = line.split(": ", 1)[1].strip()
            creator = None
            author = None
        elif line.startswith("Creator"):
            creator = line.split(": ", 1)[1].strip()
        elif line.startswith("Author"):
            author = line.split(": ", 1)[1].strip()

    if current_file:
        metadata.append([current_file, creator or "", author or ""])

    headers = ["PDF name", "Creator", "Author"]
    table = tabulate(metadata, headers, tablefmt="fancy_grid")

    output_file = os.path.join(domain_name, "metadata.txt")
    with open(output_file, "w") as f:
        f.write(table)

    print(table)

def main():
    parser = argparse.ArgumentParser(description="Download files and extract metadata")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-t", "--file_type", required=True, help="File type to download (e.g., .pdf, .doc, .xls)")

    args = parser.parse_args()

    download_files(args.domain, args.file_type)
    extract_metadata(args.domain, args.file_type)

if __name__ == "__main__":
    main()
