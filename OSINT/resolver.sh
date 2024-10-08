#!/bin/bash

echo "Domain/Subdomain,IP,Provider" > subs_ips_provider.csv

while read subdomain; do
    ip=$(dig +short $subdomain | grep '^[0-9]' | head -n 1)

    if [ -n "$ip" ]; then
        provider=$(whois $ip | grep -i "OrgName\|netname\|Org" | head -n 1 | awk -F': ' '{print $2}' | xargs)

        if [ -n "$provider" ]; then
            echo "$subdomain,$ip,$provider" >> subs_ips_provider.csv
        else
            echo "$subdomain,$ip,/" >> subs_ips_provider.csv
        fi
    else
        echo "$subdomain,/,/" >> subs_ips_provider.csv
    fi
done < subdomains.txt
