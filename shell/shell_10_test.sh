a=10
b=20
if test $a -eq $b
then echo "a=b"
else echo "a!=b"
fi
str1="abcd"
str2="abcdefgh"
if test $str1 == $str2
then echo "str1=str2"
else echo "str1!=str2"
fi

