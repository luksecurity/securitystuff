#!/bin/bash

output="pulselog.txt"
> $output

for year in {2013..2024}; do
  for month in {01..12}; do
    for day in {01..31}; do
      if date -d "$year-$month-$day" &>/dev/null; then
        echo "pulse_${year}${month}${day}.txt" >> $output
      fi
    done
  done
done

echo "Wordlist generated in $output"
