set terminal pngcairo nocrop enhanced size 1024,768 font "Verdana,15"
set output "UDP_2_st_2020_10_12_09-09-53_one2two_00032B.png"

set title "{/=20 Datagram size: 32 B, Av. rate: 9.07 Mb/s}\n\n{/=18 (LAPTOP-UE-0 to LAPTOP-UE-3, UDP, 2 st.)}"
set label "Warning:\nToo few connections!\nResults may not be accurate!" at screen 0.01, screen 0.96 tc rgb "red"

set xlabel "Time (s)"
set ylabel "Bandwidth (Mb/s)"
set ytics nomirror
set key bmargin center horizontal box samplen 1 width -1
set bmargin 4.6
set rmargin 4.5

rf = 1000000.0  # rate factor
set style fill transparent solid 0.2 noborder
set autoscale xfix
plot "UDP_2_st_2020_10_12_09-09-53_one2two_00032B_iperf_processed.dat" using 1:($2/rf-$3/rf):($2/rf+$3/rf) with filledcurves lc rgb "blue" notitle, \
     "" using 1:($2/rf) with points pt 2 ps 1.5 lw 3 lc rgb "blue" title "Mean tot. BW", \
