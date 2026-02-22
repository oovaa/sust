<?php
include 'db_connect.php';

if (!isset($_GET['ImageID'])) {
    die("No image selected.");
}

$imageID = $_GET['ImageID'];
// Validate integer to prevent SQL injection (basic protection since we aren't using prepared statements for simplicity in this example)
$imageID = intval($imageID);

$sql = "SELECT * FROM imagedetails WHERE ImageID = $imageID";
$result = pg_query($conn, $sql);

if (!$result) {
	die("Query failed.");
}

$row = pg_fetch_assoc($result);

if (!$row) {
    die("Image not found.");
}

// PostgreSQL keys are lowercase by default in assoc array
$exif = json_decode($row['exif'], true);
$colors = json_decode($row['colors'], true);
?>
<!DOCTYPE html>
<html>
<head>
    <title><?php echo $row['title']; ?></title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1><?php echo $row['title']; ?></h1>
    <img src="images/<?php echo $row['path']; ?>" alt="<?php echo $row['title']; ?>" style="max-width: 500px;">
    
    <h3>Camera Details</h3>
    <ul>
        <?php
        if ($exif) {
            foreach ($exif as $key => $value) {
                echo "<li><strong>" . ucfirst($key) . ":</strong> $value</li>";
            }
        } else {
             echo "<li>No camera details available.</li>";
        }
        ?>
    </ul>

    <h3>Main Colors</h3>
    <div class="colors">
        <?php
        if ($colors) {
            foreach ($colors as $color) {
                echo '<div class="color-box" style="background-color: ' . $color . ';"></div>';
            }
        }
        ?>
    </div>

    <br>
    <a href="addToFavorites.php?ImageID=<?php echo $row['imageid']; ?>&Title=<?php echo urlencode($row['title']); ?>&Path=<?php echo urlencode($row['path']); ?>" class="btn">Add to Favorites</a>
    <a href="browse-painting.php" class="btn">Back to Gallery</a>
</body>
</html>
