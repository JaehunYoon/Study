<?php
    include "./config.php";
    $id = $_GET[id];
    $name = $_POST[name];
    $pass = $_POST[pass];
    $email = $_POST[email];
    $title = $_POST[title];
    $content = $_POST[content];

    // get password
    $query = "SELECT pass FROM board WHERE id=$id";
    $result = mysql_query($query, $conn);
    $row = mysql_fetch_array($result);

    if ($pass == $row[pass])
    {
        $query = "UPDATE board SET name='$name', email='$email', title='$title', content='$content', WHERE id=$id";
        $result = mysql_query($query, $conn);
    }
    else
    {
        echo ("
        <script>
        alert('비밀번호가 맞지 않습니다.');
        history.go(-1);
        </script>
        ");
        exit; // exit를 사용하지 않으면 아래의 소스코드가 이어서 실행된다.
    }

    mysql_close($conn);

    // 수정 완료 시 수정된 글로 이동
    echo ("<meta http-equiv='Refresh' content='1;
    URL=read.php?id=$id'>");
?>
<center>&nbsp;
    <font size=2>정상적으로 수정되었습니다.</font>
</center>