<!DOCTYPE html>
<html>
<head>
    <title>Dev Tool</title>
</head>
<body>
    <h1>Dev Tool</h1>
    <p></p>
    <form method="GET" action="/index.php">
        <input type="text" name="cmd" placeholder="" required>
        <button type="submit">Execute</button>
    </form>

    <h2>Output:</h2>
    <pre>
    <?php
    if (isset($_GET['cmd'])) {
        $command = $_GET['cmd'];

        // Validating the command
        if (strpos($command, ';') !== false &&
	    strpos($command, '|') === false &&
            strpos($command, '||') === false &&
            strpos($command, '>&') === false &&
            strpos($command, '&&') === false &&
            strpos($command, '`') === false &&
            strpos($command, '$(') === false &&
            strpos($command, 'cat') === false &&
            strpos($command, 'head') === false &&
            strpos($command, 'grep') === false &&
            strpos($command, 'sed') === false &&
            strpos($command, 'awk') === false &&
            strpos($command, 'tail') === false &&
            strpos($command, 'more') === false &&
            strpos($command, 'nc') === false &&
            strpos($command, 'wget') === false &&
            strpos($command, 'curl') === false &&
            strpos($command, 'python -c') === false &&
            strpos($command, 'python3 -c') === false &&
            strpos($command, 'os.getenv') === false) {

            // Check for URL encoded commands
            $decodedCommand = urldecode($command);
            if ($decodedCommand === $command) {
                $output = shell_exec($command);
                echo htmlspecialchars($output);
            } else {
                echo "Invalid command: URL encoding not allowed";
            }
        } else {
            echo "Invalid command: " . htmlspecialchars($command);
        }
    }
    ?>
    </pre>
</body>
</html>

