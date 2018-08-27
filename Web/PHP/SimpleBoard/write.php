<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>글쓰기</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body topmargin=0 leftmargin=0 text=#464646>
    <center>
        <br>
        <!-- 글 작성 후 insert.php에 값을 POST 방식으로 전달 -->
        <form action="insert.php" method="post">
        <table width=580 border=0 cellpadding=2 cellspacing=1 bgcolor=#777777>
            <tr>
                <td height=20 align=center bgcolor=#9999>
                    <font color=white><b>글 쓰 기</b></font>
                </td>
            </tr>
            <!-- 입력 -->
            <tr>
                <td bgcolor=white>&nbsp;
                <table>
                    <tr>
                        <td width=60 align=left>이름</td>
                        <td align=left>
                            <input type="text" name="name" size="20" maxlength="10">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left>이메일</td>
                        <td align=left>
                            <input type="text" name="email" size="20" maxlength="25">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left>비밀번호</td>
                        <td align=left>
                            <input type="password" name="pass" size=8 maxlength="8">
                            <!-- password는 글 수정, 삭제 시에 반드시 필요함. -->
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left>제목</td>
                        <td align=left>
                            <input type="text" name="title" size=60 maxlength="35">
                        </td>
                    </tr>
                    <tr>
                        <td width=60 align=left>내용</td>
                        <td align=left>
                            <textarea name="content" cols="65" rows="15"></textarea>
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