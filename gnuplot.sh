gnuplot -pe <<- EOF
	#set grid
	set terminal png size 1480,640
	set output '.png'
	set title 'Accuracy v length of sentence'
	set yrange [0:0.02]
	set xlabel 'length of sentence'
	#set output "Graph1.png"
	set ylabel 'Context_Switch'
	plot 'graphlength.csv' u 1:2 w lp t 'graphlength.csv'
EOF

exit 0
