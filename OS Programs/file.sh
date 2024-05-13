echo "enter file name"
read n

if [ -r "$n" ]; then
    echo "Read permission is granted"
else
    echo "Read permission is not granted"
fi

if [ -w "$n" ]; then
    echo "Write permission is granted "
else
    echo "Write permission is not granted"
fi

if [ -x "$n" ]; then
    echo "Execute permission is granted"
else
    echo "Execute permission is not granted"
fi
