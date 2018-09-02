<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Simple Board</title>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
    <center>
        <br/>
        <form action=update.php?id=<?=$_GET[id]?> method=post>
        <table width=580 border=0 cellpadding=2 cellspacing=1 bgcolor=#777777>
            <tr>
                <td height=20 align=center bgcolor=#999999>
                    <font color=white><b>글 수 정 하 기</b></font>
                </td>
            </tr>
        <?
            include "config.php";
            $id = $_GET[id];
            $no = $_GET[no];

            $result = mysql_query("SELECT * FROM board WHERE id=$id", $conn);
            $row = mysql_fetch_array($result);
        ?>
            <tr>
                <td bgcolor=white>&nbsp;
                <table>
                    <tr>
                        <td width=60 align=left >이름</td>
                        <td align=left>
                            <input type=text name=name size=20 value="<?=$row[name]?>">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left >이메일</td>
                        <td align=left>
                            <input type=text name=email size=20 value="<?=$row[email]?>">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left >비밀번호</td>
                        <td align=left>
                            <input type=password name=pass size=8>
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left >제 목</td>
                        <td align=left>
                            <input type=text name=title size=60 value="<?=$row[title]?>">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left >내용</td>
                        <td align=left>
                            <textarea name=content cols=65 rows=15><?=$row[content]?></textarea>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="10" align=center>
                            <input type="submit" value="글 저장하기">
                            &nbsp;&nbsp;
                            <input type="reset" value="다시 쓰기">
                            &nbsp;&nbsp;
                            <input type="button" value="되돌아가기" onclick="history.back(-1)">
                            <!-- 버튼 클릭 시 js 이벤트 실행 -->
                        </td>
                    </tr>
                    </table>
                </td>
            </tr>
        </table>
        </form>
    </center>
    </body>
</html>