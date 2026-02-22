<?php
session_start();

if (isset($_GET['clear']) && $_GET['clear'] == 1) {
    unset($_SESSION['favorites']);
} elseif (isset($_GET['ImageID'])) {
    $imageID = $_GET['ImageID'];
    
    if (isset($_SESSION['favorites'])) {
        foreach ($_SESSION['favorites'] as $key => $fav) {
            if ($fav['ImageID'] == $imageID) {
                unset($_SESSION['favorites'][$key]);
                // Re-index array
                $_SESSION['favorites'] = array_values($_SESSION['favorites']);
                break;
            }
        }
    }
}

header("Location: view-favorites.php");
exit();
?>
