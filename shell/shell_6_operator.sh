a=10
b=20
val1=`expr $a + $b`
echo $val1
val2=`expr $a - $b`
echo $val2
val3=`expr $a \* $b`
echo $val3
if [ $a == $b ]
then echo "a=b"
else echo "a!=b"
fi
if [ $a -gt $b ]
then echo "a is bigger than b"
fi
if [ $a -lt $b ]
then echo "a is smaller than b"
fi
if [[ $a -lt 100 && $b -gt 100 ]]
then echo "true"
else echo "flase"
fi
str1="abcd"
str2="abcdf"
if [ $str1 == $str2 ]
then echo "true"
else echo "false"
fi

