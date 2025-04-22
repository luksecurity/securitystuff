#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import csv
import re
import argparse
import ipaddress

def parse_udpz_output(udpz_output):
    pattern = re.compile(
        r'host=(?P<ip>\d+\.\d+\.\d+\.\d+)\s+port=(?P<port>\d+).*?service=(?P<service>\S+)'
    )
    parsed_data = []

    for line in udpz_output:
        match = pattern.search(line)
        if match:
            ip = match.group("ip")
            port = match.group("port")
            status = "open" 
            service = match.group("service")
            parsed_data.append([ip, port, status, service])

    return parsed_data

def write_to_csv(parsed_data, output_file):
    headers = ['IP', 'Port', 'Status', 'Service']
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(parsed_data)

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        udpz_output = file.readlines()

    parsed_data = parse_udpz_output(udpz_output)
    parsed_data.sort(key=lambda x: ipaddress.ip_address(x[0]))

    write_to_csv(parsed_data, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse UDPZ-style output and convert to CSV")
    parser.add_argument('-i', '--input', required=True, help='Input UDPZ scan result file')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file')

    args = parser.parse_args()
    main(args.input, args.output)
