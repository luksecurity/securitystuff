# Full tty python

```
which python/python3                                 # vérifier s'il y a python ou python3

python3 -c 'import pty; pty.spawn("/bin/bash")'      # full tty
CTRL+Z

stty raw -echo; fg                                   # tab autocompletion

export TERM=xterm-256color                           # clear screen

stty -a                                              # afficher la configuration actuelle stty
stty rows $value cols $value                         # récupérer les valeurs de rows et cols
```
