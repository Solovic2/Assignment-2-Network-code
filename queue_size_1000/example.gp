set term postscript eps color
set output 'cwnd.eps'
set ylabel 'Queue Size'
set xlabel 'time'
plot 'output.cwnd' using 1:2 with lines
