#!/bin/bash
inputdir='inp'
outputdir='out'
progname='skoczek.py'
for i in {1..100} 
do
	python skoczek.py < "$inputdir/t$i.in" > tak
	di=$(diff -w tak "$outputdir/t$i.out")
	if [ "$di" != "" ]
	then
		echo "test $i WRONG"
		echo
		echo
		echo "| ~/$inputdir/$i.in |--------------"
		cat "$inputdir/t$i.in"
		echo
		echo
		echo "| diff |--------------"
		echo "$di"
		break
	else
		echo "test $i OK"
	fi
done
