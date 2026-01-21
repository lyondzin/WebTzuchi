<?php

function cek_data($data): mixed{
    if(isset($_GET[$data])){
        if($_GET[$data] == null){
            return 0;
        }else{
            return $_GET[$data];
        }
    }else{
        return 0;
    }
}

$a = cek_data('angka1');
$b = cek_data('angka2');

function hasil($a, $b){
    if (isset($_GET['tambah'])) {
        return $a + $b;
    } elseif (isset($_GET['mines'])) {
        return $a - $b;
    } elseif (isset($_GET['kali'])) {
        return $a * $b;
    } elseif (isset($_GET['bagi'])) {
        if ($b==0){
            return "Tidak Bisa Dibagi 0";
        }
        return $a / $b;
}}

?>

<html>
    <style>
        input {
            margin-left: 2px;
            margin-bottom:10px;
        }
    </style>
    <head>
        <title>Operasi</title>
    </head>
    <body>
        <h2>Angka Pertama : <?php echo $a?></h2>
        <h2>Angka Kedua : <?php echo $b?></h2>
        <h2>hasil : <?php echo hasil($a, $b); ?></h2>

        <hr>

        <form action="" method="get">
            <label>Angka 1</label>
            <input type="number" name="angka1"><br>
            <label>Angka 2</label>
            <input type="number" name="angka2"><br>
            <input type="submit" value="Tambah" name="tambah">
            <input type="submit" value="Mines" name="mines">
            <input type="submit" value="Kali" name="kali">
            <input type="submit" value="Bagi" name="bagi">
        </form>
    </body>
</html>