<?php
include 'db_connect.php';
?>
<!DOCTYPE html>
<html>
<head>
    <title>Browse Paintings</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Art Gallery</h1>
    <div class="gallery">
        <?php
        $sql = "SELECT ImageID, Title, Path FROM imagedetails";
        $result = pg_query($conn, $sql);

        if ($result && pg_num_rows($result) > 0) {
            while($row = pg_fetch_assoc($result)) {
                echo '<div class="painting">';
                echo '<h3><a href="single-painting.php?ImageID=' . $row["imageid"] . '">' . $row["title"] . '</a></h3>';
                echo '<a href="single-painting.php?ImageID=' . $row["imageid"] . '">';
                echo '<img src="images/' . $row["path"] . '" alt="' . $row["title"] . '" style="width:200px;">'; 
                echo '</a>';
                echo '</div>';
            }
        } else {
            echo "No paintings found.";
        }
        pg_close($conn);
        ?>
    </div>
</body>
</html>
