#!/bin/bash
inputdir='inp'
outputdir='out'
mkdir "$inputdir"
mkdir "$outputdir"
for i in {1..100} 
do
	echo "gen $i"
	python gen.py > "$inputdir/t$i.in" && python skoczek.py < "$inputdir/t$i.in" > "$outputdir/t$i.out"
done
