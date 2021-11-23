set term postscript eps color
set output 'queue_size_1000.eps'
set ylabel 'Queue Size'
set xlabel 'time'
plot 'output.cwnd' with lines
