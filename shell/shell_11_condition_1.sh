a=10
b=20
if test $a == $b
then echo "a=b"
elif [ $a -gt $b ]
then echo "a>b"
elif [ $a -lt $b ]
then echo "a<b"
else echo "wrong"
fi
for i in 1 2 3 4 5
do
echo "$i"
done
while [ $b -gt $a ]
do 
echo $b
let "b--"
done
echo "---------------"
b=20
until [ $b -lt $a  ]
do 
echo $b
let "b--"
done

