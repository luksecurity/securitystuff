### Find files/folders of interest to users/groups and display them, except dir between / \

```text
# User
find / -user luks -ls 2>/dev/null | grep -v '/proc\|/sys\|/home\|/run'

# Group
find / -group adm -ls 2>/dev/null | grep -v '/proc\|/sys\|/home\|/run'
```
