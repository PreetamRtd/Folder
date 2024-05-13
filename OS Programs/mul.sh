#!/bin/bash
echo "Enter a number to generate its multiplication table:"
read num

i=1

while [ $i -le 10 ]
do 
    result=$((num * i))
    echo "$num * $i = $result"
    i=$((i + 1))
done
