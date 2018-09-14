<?php
    include "./config.php";
    $id = $_GET['id'];
    $pass = $_POST['pass'];

    $result = mysql_query("SELECT pass FROM board WHERE id=$id", $conn);
    $row = mysql_fetch_array($result);

    if ($pass == $row['pass'])
    {
        $query = "DELETE FROM board WHERE id=$id";
        $result = mysql_query($query, $conn);
    }
    else
    {
        echo("
        <script>
            alert('Wrong Password');
            history.go(-1);
        </script>
        ");
        exit;
    }
?>
<center>
    <meta http-equiv="Refresh" content="1; URL=list.php">
    <font size="2">Delete complete.</font>
</center>
