set term postscript eps color
set output 'cwnd.eps'
set ylabel 'time'
set xlabel 'delay time'
plot 'output_delay.cwnd' 
