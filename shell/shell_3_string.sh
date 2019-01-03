str1='abcd'
str2="1234 \"$str1\" 5678"
echo $str2
str3='ha'
str4="abcdefgh"$str3"  wefg"
echo $str4
echo ${#str4}
str5=${str4:1:4}
echo $str5

