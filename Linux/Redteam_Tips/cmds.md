### List the 50 largest packages

```
(echo "Size (KB)   Package" && echo && dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -rn | head -n 50 | awk '{printf "%-12s%s\n", $1, $2}')
```
