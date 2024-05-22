#!/usr/bin/env python3

import csv
import re
import sys

def parse_nmap_output(nmap_output):
    ip_pattern = re.compile(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)')
    port_pattern = re.compile(r'(\d+)/tcp\s+(\w+)\s+(\w+)\s+(.*)')

    # Variables to store parsed data
    current_ip = None
    parsed_data = []

    for line in nmap_output:
        ip_match = ip_pattern.search(line)
        if ip_match:
            current_ip = ip_match.group(1)

        port_match = port_pattern.search(line)
        if port_match and current_ip:
            port = port_match.group(1)
            state = port_match.group(2)
            service = port_match.group(3)
            banner = port_match.group(4).strip()
            if state == "open":
                parsed_data.append([current_ip, port, service, state, banner])

    return parsed_data

def write_to_csv(parsed_data, output_file):
    headers = ['IP', 'Port', 'Service', 'Statut', 'Bannière']
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(parsed_data)

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        nmap_output = file.readlines()

    parsed_data = parse_nmap_output(nmap_output)
    write_to_csv(parsed_data, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nmap_to_csv.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
