#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import csv
import re
import argparse

def parse_nmap_output(nmap_output):
    ip_pattern = re.compile(r'Nmap scan report for (?:[^\s]+ )?\(?(\d+\.\d+\.\d+\.\d+)\)?')
    port_pattern = re.compile(r'(\d+)/(tcp|udp)\s+(\w+)\s+(\w+)?\s*(.*)')

    current_ip = None
    parsed_data = []

    for line in nmap_output:
        ip_match = ip_pattern.search(line)
        if ip_match:
            current_ip = ip_match.group(1)

        port_match = port_pattern.search(line)
        if port_match and current_ip:
            port = port_match.group(1)
            protocol = port_match.group(2)
            state = port_match.group(3)
            service = port_match.group(4) if port_match.group(4) else "unknown"
            banner = port_match.group(5).strip()
            if state == "open":
                parsed_data.append([current_ip, port, protocol, service, state, banner])

    return parsed_data

def write_to_csv(parsed_data, output_file):
    headers = ['IP', 'Port', 'Protocol', 'Service', 'Statut', 'Bannière']
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
    parser = argparse.ArgumentParser(description="Parse Nmap output and convert to CSV")
    parser.add_argument('-i', '--input', required=True, help='Input Nmap file')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    main(input_file, output_file)
