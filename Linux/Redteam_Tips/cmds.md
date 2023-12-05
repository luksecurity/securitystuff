### List the 50 largest packages

```
(echo -e "$(tput bold)$(tput setaf 4)Size (MB)   $(tput setaf 6)Package$(tput sgr0)" && echo && dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -rn | head -n 50 | awk '{printf "%-12.2f%s\n", $1/1024, $2}')
```
