<?php
    include "./config.php";

    $page_size = 10;
    $list_size = 10;
    $no = $_GET['no'];
    if (!$no || $no < 0)
    {
        $no = 0;
    }

    $query = "SELECT * FROM board ORDER BY id DESC LIMIT $no, $page_size";
    $result = mysql_query($query, $conn);

    $result_count = mysql_query("SELECT count(*) FROM board", $conn);
    $result_row = mysql_fetch_row($result_count);
    $total_row = $result_row[0];

    if ($total_row <= 0) $total_row = 0;
    $total_page = ceil($total_row / $page_size); // ceil => 반올림

    $current_page = ceil(($no + 1) / $page_size);
?>

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
            <font size="2">Simple Board</font>
            <br>
            <br>
            <table width="580" border="0" cellpading="2" cellspacing="1" bgcolor="#999999">
                <tr height="20" bgcolor="#999999">
                    <td width="30" align="center">
                        <font color="white">번호</font>
                    </td>
                    <td width="370" align="center">
                        <font color="white">제 목</font>
                    </td>
                    <td width="50" align="center">
                        <font color="white">글쓴이</font>
                    </td>
                    <td width="60" align="center">
                        <font color="white">날 짜</font>
                    </td>
                    <td width="40" align="center">
                        <font color="white">조회수</font>
                    </td>
                </tr>
                <?
                while($row=mysql_fetch_array($result))
                {
                    ?>
                    <tr>
                        <td height="20" bgcolor="white">
                            <a href="read.php?id=<?= $row['id'] ?>&no=<?= $no ?>" ;>
                                <?=row['id']?></a>
                        </td>
                        <td height="20" bgcolor="white">&nbsp;
                            <a href "read.php?id=<?= row['id'] ?>&no=<?= $no ?>">
                            <?= strip_tags($row['title'], '<b><i>'); ?></a>
                        </td>
                        <td align="center" height="20" bgcolor="white">
                            <font color="black">
                                <a href="mailto:<?= $row['email'] ?>"><?= row['name'] ?></a>
                            </font>
                        </td>
                        <td align="center" height="20" bgcolor="white">
                            <font color="black"><?= $row['wdate'] ?></font>
                        </td>
                        <td align="center" height="20" bgcolor="white">
                            <font color="black"><?= $row['view'] ?></font>
                        </td>
                    </tr>
                    <?
                }

                mysql_close($conn);
                ?>
            </table>
            <table border="0">
                <tr>
                    <td width="600" height="20" align="center" rowspan="4">
                        <font color="gray">&nbsp;
                            <?
                                $start_page = floor(($current_page - 1) / $list_size) * $list_size + 1;
                                // floor => 소수점 버림
                                $end_page = $start_page + $list_size - 1;

                                if ($total_page < $end_page) $end_page = $total_page;
                                if ($start_page >= $list_size)
                                {
                                    $prev_list = ($start_page - 2) * $page_size;
                                    echo "<a href='$PHP_SELF?no=$prev_list'>◀</a>";
                                }

                                for ($i = $start_page; $i <= $end_page; $i++)
                                {
                                    $page = ($i - 1) * $page_size;
                                    if ($no != $page)
                                    {
                                        echo "<a href='$PHP_SELF?no=$page'>";
                                    }

                                    echo " $i ";

                                    if ($no != $page)
                                    {
                                        echo "</a>";
                                    }
                                }

                                if ($total_page > $end_page)
                                {
                                    $next_list = $end_page * $page_size;
                                    echo "<a href='$PHP_SELF?no=$next_list'>▶</a><p>";
                                }
                            ?>
                        </font>
                    </td>
                </tr>
            </table>
            <a href="write.php">[글쓰기]</a>
        </center>
    </body>
</html>