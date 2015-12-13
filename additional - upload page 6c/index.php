<?php



if( is_uploaded_file($_FILES['filex']['tmp_name'])){
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["filex"]["name"]);
if (move_uploaded_file($_FILES['filex']['tmp_name'], $target_file)) {
    echo 'Plik wrzucony poprawnie';
} else {
    echo "Błąd wrzycania pliku";
}

}
else{
echo '
<!DOCTYPE html>
<html>
<body>

<form method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="filex" id="filex">
    <input type="submit" value="Upload Image" name="submit">
</form>

</body>
</html> ';
}
?>