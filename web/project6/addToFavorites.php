<?php
session_start();

if (isset($_GET['ImageID']) && isset($_GET['Title']) && isset($_GET['Path'])) {
    $item = [
        'ImageID' => $_GET['ImageID'],
        'Title' => $_GET['Title'],
        'Path' => $_GET['Path']
    ];

    if (!isset($_SESSION['favorites'])) {
        $_SESSION['favorites'] = [];
    }

    // Check if duplicate
    $exists = false;
    foreach ($_SESSION['favorites'] as $fav) {
        if ($fav['ImageID'] == $item['ImageID']) {
            $exists = true;
            break;
        }
    }

    if (!$exists) {
        $_SESSION['favorites'][] = $item;
    }
}

header("Location: view-favorites.php");
exit();
?>
