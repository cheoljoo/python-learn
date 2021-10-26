$total = 0;
for($i=1;$i<=10000;$i++){
    for ($j=1;$j<=10000;$j++){
        $total += $i + $j;
    }
}

print("The result is $total\n")
