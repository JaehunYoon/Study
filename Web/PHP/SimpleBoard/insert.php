<!DOCTYPE html>
<html>
    <?php
        // Connect Database
        include "./config.php";

        $id = $_GET[id];
        $name = $_POST[name];
        $email = $_POST[email];
        $pass = $_POST[pass];
        $title = $_POST[title];
        $content = $_POST[content];
        $user_ip = $_SERVER['REMOTE_ADDR'];

        $query = "INSERT INTO board (id, name, email, pass, title, content, wdate, ip, view) VALUES ('', '$name', '$email', '$pass', '$title', '$content', now(), '$user_ip', 0)";
        $result = mysql_query($query, $conn) or die(mysql_error());
        // mysql_error() 출력 시 이를 이용한 Error Based Blind SQL Injection 공격이 가능함. 주의!!

        mysql_close($conn); // Unconnect Database

        echo("<meta http-equiv='Refresh' content='1; URL=list.php'>");
        // 1초 후 list.php 로 리다이렉션
    ?>
    <center>&nbsp;
        <font size=2>정상적으로 저장되었습니다.</font>
    </center>
</html>