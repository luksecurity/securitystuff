### Redteam Tips for Linux
by @Alh4zr3d

```sh
"export HISTFILE=/dev/null"                   # Disable history
"(exec -a syslogd $cmd)"                      # Hidden a cmd by masking it as syslogd
"exec -a syslogd $cmd &"                      # Start a background hidden process as syslogd
```
