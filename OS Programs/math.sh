#!/bin/bash

# Initialize variables
sum=0
i="y"

# Input the first value
echo "Enter the first value:"
read a

# Input the second value
echo "Enter the second value:"
read b

# Loop until the user chooses to exit
while [ "$i" = "y" ]; do
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "Enter your choice:"
    read ch

    # Perform the selected operation using a case statement
    case $ch in
        1)
            sum=$((a + b))
            echo "Summation: $sum"
            ;;
        2)
            sub=$((a - b))
            echo "Subtraction: $sub"
            ;;
        3)
            mul=$((a * b))
            echo "Multiplication: $mul"
            ;;
        4)
            # Use bc for division to support decimal fractions
            div=$(echo "scale=2; $a / $b" | bc)
            echo "Division: $div"
            ;;
        *)
            echo "Invalid Choice"
            ;;
    esac

    # Ask if the user wants to continue
    echo "Do you want to continue? (y/n)"
    read i

    if [ "$i" != "y" ]; then
        echo "Bye"
        exit 0
    fi
done
