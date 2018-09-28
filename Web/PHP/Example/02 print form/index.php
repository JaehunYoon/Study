<?php
// 폼이 전송되면 매개변수 출력
if (isset($_POST['user']))
{
    echo "안녕하세요, " . $_POST['user'] . "님!";
}

else
{
    echo <<<_HTML_
<form method="POST" action="$_SERVER[PHP_SELF]">
이름 : <input type="text" name="user"/>
<br>
<button type="submit">인사</button>
</form>
_HTML_;
}

?>