#!/bin/bash 

echo "Expr aritmetico"
echo -n "Introduce un valor:"
read var1
echo -n "Introduce un valor:"
read var2
resultado=`expr $var1 \* $var2`
echo "El resultado de la multiplicación es "$resultado

echo "Expr logico"
echo -n "Introduce un valor"
read var3
echo -n "Introduce un valor"
read var4
resultado2=`expr $var3 = $var4`
echo "El resultado es "$resultado2

echo "Numeros aleatorios"
numero=`expr $RANDOM % 5`
echo "$numero"

echo "test"
echo -n "Introduce un valor: "
read var5
echo -n "Introduce un valor: "
read var6

if [ "$var5" -lt "$var6" ]; then
  resultado3="true"
else
  resultado3="false"
fi

echo "El resultado es $resultado3"

