<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Simple Board</title>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body topmargin=0 leftmargin=0 text=#464646>
    <center>
    <br>
    <?php
        include "./config.php";
        include "./func.php";

        $id = $_GET[id];
        $no = $_GET[no];

        $result = mysql_query("SELECT * FROM board WHERE id=$id", $conn) or die(is_null($result));
        $row = mysql_fetch_array($result);
    ?>
    <table width=580 border=0 cellpadding=2 cellspacing=1 bgcolor=#777777>
        <tr>
            <td>
                <font color=white><b><?=check_null($row['title'])?></b></font>
            </td>
        </tr>
        <tr>
            <td width=50 height=20 align=center bgcolor=#EEEEEE>글쓴이</td>
            <td width=240 bgcolor=white><?=$row['name']?></td>
            <td width=50 height=20 align=center bgcolor=#EEEEEE>이메일</td>
            <td width=240 bgcolor=white><?=$row['email']?></td>
        </tr>
        <tr>
            <td width=50 height=20 align=center bgcolor=#EEEEEE>날&nbsp;&nbsp;&nbsp;짜</td>
            <td width=240 bgcolor=white><?=$row['wdate']?></td>
            <td width=50 height=20 align=center bgcolor=#EEEEEE>조회수</td>
            <td width=240 bgcolor=white><?=$row['view']?></td>
        </tr>
        <tr>
            <td bgcolor=white colspan=4>
                <font color=black>
                    <pre><?=$row['content']?></pre>
                </font>
            </td>
        </tr>
        <tr>
            <td width=200 height=20 align=left>
                <a href="list.php?no=<?$no?>">
                    <font color=white>[목록보기]</font>
                </a>
                <a href="write.php">
                    <font color=white>[글쓰기]</font>
                </a>
                <a href="edit.php?id=<?$id?>">
                    <font color=white>[수정]</font>
                </a>
                <a href="predel.php?id=<?$id?>">
                    <font color=white>[삭제]</font>
                </a>
            </td>
            <td align=left>
            <?php
                $query = mysql_query("SELECT * FROM board WHERE id > $id LIMIT 1", $conn);
                $prev_id = mysql_fetch_array($query);

                if ($prev_id[id])
                {
                    echo "
                    <a href=read.php?id=$prev_id[id]>
                        <font color=white>[이전]</font>
                    </a>";
                }
                else
                {
                    echo "[이전]";
                }

                $query = mysql_query("SELECT id FROM board WHERE id < $id ORDER BY id DESC LIMIT 1", $conn);
                $next_id = mysql_fetch_array($query);

                if ($next_id[id])
                {
                    echo "
                    <a href=read.php?id=$next_id[id]>
                        <font color=white>[다음]</font>
                    </a>";
                }
                else
                {
                    echo "[다음]";
                }
            ?>
            </td>
        </tr>
    </table>
    </center>
    </body>
</html>

<?php
    $result = mysql_query("UPDATE board SET view=view+1 WHERE id=$id", $conn);

    mysql_close($conn);
?>