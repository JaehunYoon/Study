<?php
    include "./config.php";

    $result = mysqli_query($conn, "SELECT * FROM table_name");
//  $row = mysqli_fetch_array($result, MYSQLI_ASSOC)
//  OR
    $row = mysqli_fetch_assoc($result);
    echo row['id'];

    mysqli_free_result($result);
    mysqli_close($conn);
?>