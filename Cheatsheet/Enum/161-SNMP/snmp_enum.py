#!/usr/bin/env python3

from pysnmp.hlapi import *
import sys
import re
import argparse
import csv
from datetime import datetime

SENSITIVE_REGEX = re.compile(
    r'user|username|login|pass|password|admin|root|enable|auth|secret|community|credential|'
    r'ssh|telnet|rdp|smb|snmp|ftp|tftp|vpn|ike|radius|kerberos|key|hash|history|'
    r'shell|bash|zsh|powershell|cmd|script|session|home|\.bash_history|\.ssh|\.profile|'
    r'netbios|sam|registry|sid|token',
    re.IGNORECASE
)

GENERIC_OID = ObjectIdentity('1.3.6.1.2.1')
SYSNAME_OID = '1.3.6.1.2.1.1.5.0'

ENTERPRISE_OIDS = {
    "Cisco": '1.3.6.1.4.1.9',
    "HP": '1.3.6.1.4.1.11',
    "Netgear": '1.3.6.1.4.1.4526'
}

results = []

def get_sysname(target, community):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=1),
            UdpTransportTarget((target, 161), timeout=1.0, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(SYSNAME_OID))
        )
    )
    if errorIndication or errorStatus:
        print(f"[-] Failed to retrieve sysName. SNMP may not be accessible.")
        return None
    for varBind in varBinds:
        return str(varBind[1])

def snmp_enum(target, community, oid_str, label=""):
    print(f"\n[*] Enumerating {label} ({oid_str})")
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((target, 161), timeout=1.0, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity(oid_str)),
        lexicographicMode=False
    ):
        if errorIndication or errorStatus:
            break
        for varBind in varBinds:
            value = str(varBind)
            if SENSITIVE_REGEX.search(value):
                print(f"  [+] {value}")
                results.append((label, oid_str, value))

def snmp_full_enum(target, community, oid_str):
    """Scan the entire subtree under 1.3.6.1.4.1."""
    print(f"\n[*] Scanning full OID subtree starting from {oid_str}")
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((target, 161), timeout=1.0, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity(oid_str)),
        lexicographicMode=False
    ):
        if errorIndication or errorStatus:
            break
        for varBind in varBinds:
            value = str(varBind)
            if SENSITIVE_REGEX.search(value):
                print(f"  [+] {value}")
                results.append(("Full Scan", oid_str, value))

def export_results(output_format, target):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"snmp_enum_{target}_{timestamp}.{output_format}"

    if output_format == "txt":
        with open(filename, "w") as f:
            for label, oid, value in results:
                f.write(f"[{label}] ({oid}) {value}\n")
    elif output_format == "csv":
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Label", "OID", "Result"])
            writer.writerows(results)

    print(f"\n[✔] Results saved to: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SNMP Sensitive Enum")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("community", nargs="?", default="public", help="SNMP community string (default: public)")
    parser.add_argument("--output", choices=["txt", "csv"], default="txt", help="Output format (txt or csv)")
    parser.add_argument("--full", action="store_true", help="Scan the full .1.3.6.1.4.1 OID subtree for sensitive info")

    args = parser.parse_args()

    sysname = get_sysname(args.target, args.community)
    if sysname:
        print(f"\n[+] sysName: {sysname}")
    else:
        sys.exit(1)

    snmp_enum(args.target, args.community, str(GENERIC_OID), "Generic")

    for vendor, oid in ENTERPRISE_OIDS.items():
        snmp_enum(args.target, args.community, oid, vendor)

    if args.full:
        snmp_full_enum(args.target, args.community, '1.3.6.1.4.1')

    if results:
        export_results(args.output, args.target)
    else:
        print("\n[-] No sensitive info found.")
