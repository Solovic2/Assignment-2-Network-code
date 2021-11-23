set term postscript eps color
set output 'queue_delay.eps'
set ylabel 'delay_time'
set xlabel 'time'
plot 'output_delay.cwnd' with lines
