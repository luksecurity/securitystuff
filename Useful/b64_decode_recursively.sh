#!/bin/bash

# Script to recursively decode base64 encoded string

state=$(<base64.txt)
for i in {1..13}; do
   state=$(<<<"$state" base64 --decode)
   printf "\n%s\n------------" $state
done
