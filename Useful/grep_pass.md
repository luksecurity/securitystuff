# Récupérer des mots de passe dans un dossier

```
clear && LANG=C \grep -siroPah --include="*.*" --exclude-dir={lib,python,pip,.venv,share,include,objects} --exclude=*.{js,css,iso,zip,tgz,gz,bz2,mkv,avi,mp3,mp4,doc,docx,xls,xlsx,pdf,dll,exe,png,jpg,jpeg,gif} '(password|pass|passwd|secret|priv|private|passphrase|endpoint|oauth2?)\s{0,3}={1,3}\s{0,3}[^"|^\x27|^\x60]?.[^"|\n|\r|\s|\x60|\x27|;]{5,32}' 2>/dev/null | awk '!x[$0]++'  | sort
```
