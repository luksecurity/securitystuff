#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import os
import subprocess
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tabulate import tabulate

def add_scheme_if_missing(domain):
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain
    return domain

def find_files_on_site(domain, file_type):
    domain = add_scheme_if_missing(domain)
    print(f"\033[92m[+] Searching for {file_type} files on {domain}\033[0m")
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(domain, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        file_urls = []
        for link in soup.find_all('a', href=True):
            url = urljoin(domain, link['href'])
            if url.endswith(file_type):
                file_urls.append(url)

        if file_urls:
            print(f"\033[92m[+] Found {len(file_urls)} {file_type} files on the website\033[0m")
        else:
            print(f"\033[93m[-] No {file_type} files found on the website\033[0m")
        return file_urls
    except requests.RequestException as e:
        print(f"\033[91m[-] Error accessing {domain}: {e}\033[0m")
        return []

def find_files_in_archive(domain, file_type):
    print(f"\033[92m[+] Searching for {file_type} files in archive\033[0m")
    try:
        command = f"echo {domain} | gau | grep '{file_type}'"
        urls = subprocess.run(command, shell=True, capture_output=True, text=True).stdout.splitlines()
        if urls:
            print(f"\033[92m[+] Found {len(urls)} {file_type} files in archive\033[0m")
        return urls
    except Exception as e:
        print(f"\033[91m[-] Error running gau: {e}\033[0m")
        return []

def download_files(domain, urls, file_type_dir):
    domain_name = domain.split("//")[-1].split("/")[0]
    parent_dir = os.path.join(domain_name, file_type_dir)
    os.makedirs(parent_dir, exist_ok=True)

    for url in urls:
        file_name = os.path.join(parent_dir, os.path.basename(url))
        try:
            print(f"Downloading {url} to {file_name}")
            response = requests.get(url)
            response.raise_for_status()
            with open(file_name, 'wb') as f:
                f.write(response.content)
        except requests.RequestException as e:
            print(f"\033[91m[-] Error downloading {url}: {e}\033[0m")

def extract_metadata(domain, file_type_dir):
    print("\033[92m[+] Extracting metadata from downloaded files\033[0m")
    domain_name = domain.split("//")[-1].split("/")[0]
    file_pattern = os.path.join(domain_name, file_type_dir, '*')
    cmd = f"exiftool {file_pattern} | grep -E '^(Creator|Author|File Name)\\s*:'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    metadata = []
    emails = []
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
            if author:
                email = author.lower().replace(' ', '.').replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('ë', 'e').replace('ç', 'c')
                email = f"{email}@{domain_name}"
                emails.append(email)

    if current_file:
        metadata.append([current_file, creator or "", author or ""])

    headers = ["File name", "Creator", "Author"]
    table = tabulate(metadata, headers, tablefmt="fancy_grid")

    output_file = os.path.join(domain_name, "metadata.txt")
    with open(output_file, "w") as f:
        f.write(table)

    print(table)

    if emails:
        wordlist_file = os.path.join(domain_name, "wordlist.txt")
        with open(wordlist_file, "w") as f:
            for email in set(emails):
                f.write(f"{email}\n")
        print(f"\033[92m[+] Email wordlist created: {wordlist_file}\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Download files from a domain and extract metadata")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-t", "--file_type", required=True, help="File types to download (e.g., pdf,docx,xlsx)", type=str)

    args = parser.parse_args()
    file_type = args.file_type

    web_files = find_files_on_site(args.domain, file_type)
    archive_files = find_files_in_archive(args.domain, file_type)

    all_urls = set(web_files + archive_files)

    if all_urls:
        download_files(args.domain, all_urls, file_type)

    extract_metadata(args.domain, file_type)

if __name__ == "__main__":
    main()
