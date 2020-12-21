set terminal pngcairo nocrop enhanced size 1024,768 font "Verdana,15"
set output "TCP_8_st_2020_12_05_00-21-22_two2one_00032B.png"

set title "{/=20 Buffer size: 32 B, Av. rate: 4.72 Mb/s}\n\n{/=18 (LAPTOP-UE-7 to LAPTOP-UE-0, TCP, 8 st.)}"

set xlabel "Time (s)"
set ylabel "Bandwidth (Mb/s)"
set ytics nomirror
set key bmargin center horizontal box samplen 1 width -1
set bmargin 4.6
set rmargin 4.5

rf = 1000000.0  # rate factor
set style fill transparent solid 0.2 noborder
set autoscale xfix
plot "TCP_8_st_2020_12_05_00-21-22_two2one_00032B_iperf_processed.dat" using 1:($2/rf-$3/rf):($2/rf+$3/rf) with filledcurves lc rgb "blue" notitle, \
     "" using 1:($2/rf) with points pt 2 ps 1.5 lw 3 lc rgb "blue" title "Mean tot. BW", \
