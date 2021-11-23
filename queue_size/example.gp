set term postscript eps color
set output 'queue_size_10.eps'
set ylabel 'Queue Size'
set xlabel 'time'
set yrange [0:11]
plot 'output.cwnd' with lines
