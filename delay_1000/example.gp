set term postscript eps color
set output 'queue_delay_1000.eps'
set ylabel 'delay time'
set xlabel 'time'
plot 'output_delay.cwnd' with lines
