path1="."
path2="./shell_1_hello_world.sh"
if [ -d $path1 ]
then echo "is directory"
else echo "is not directory"
fi
if [ -f $path2 ]
then echo "is normal file"
else echo "is not normal file"
fi

