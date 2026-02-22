<?php
session_start();

$favorites = isset($_SESSION['favorites']) ? $_SESSION['favorites'] : [];
$count = count($favorites);
?>
<!DOCTYPE html>
<html>
<head>
    <title>My Favorites</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>My Favorites</h1>
    <p>You have <strong><?php echo $count; ?></strong> favorite(s).</p>
    
    <div class="gallery">
        <?php
        if ($count > 0) {
            foreach ($favorites as $fav) {
                echo '<div class="painting">';
                echo '<h3>' . $fav['Title'] . '</h3>';
                echo '<img src="images/' . $fav['Path'] . '" alt="' . $fav['Title'] . '" style="width:150px;"><br>';
                echo '<a href="remove-favorites.php?ImageID=' . $fav['ImageID'] . '" class="btn remove">Remove</a>';
                echo '</div>';
            }
        } else {
            echo "<p>No favorites yet.</p>";
        }
        ?>
    </div>
    
    <br>
    <?php if ($count > 0): ?>
        <a href="remove-favorites.php?clear=1" class="btn remove">Clear All Favorites</a>
    <?php endif; ?>
    <a href="browse-painting.php" class="btn">Back to Gallery</a>
</body>
</html>
