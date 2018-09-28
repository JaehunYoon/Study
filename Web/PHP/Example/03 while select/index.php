<?php
    $i = 1;
    echo '<select name="people">';
    while ($i <= 10)
    {
        echo "<option>$i</option>\n";
        $i++;
    }

    echo "</select>";

    // 
    echo '<select name="people">';
    for ($j = 1; $j <= 10; $j++)
        echo "<option>$j</option>\n";
    
    echo "</select>";
?>