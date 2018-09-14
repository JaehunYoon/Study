<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Simple Board</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="./style.css" />
    </head>
    <body topmargin="0" leftmargin="0" text="#464646">
        <center>
            <br>
            <form action="del.php?id=<?=$_GET['id']?>" method="post">
                <table width="300" border="0" cellpadding="2" cellspacing="1" bgcolor="#777777">
                    <tr>
                        <td height="20" align="center" bgcolor="#999999">
                            <font color="white"><b>비 밀 번 호 확 인</b></font>
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            <font color="white"><b>비밀번호 : </b></font>
                            <input type="password" name="pass" size="8">
                            <input type="submit" value="확 인">
                            <input type="button" value="취 소" onclick="history.back(-1)">
                        </td>
                    </tr>
                </table>
            </form>
        </center>
    </body>
</html>