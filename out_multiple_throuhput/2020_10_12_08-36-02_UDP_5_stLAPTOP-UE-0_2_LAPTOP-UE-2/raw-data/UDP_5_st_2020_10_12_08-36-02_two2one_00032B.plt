set terminal pngcairo nocrop enhanced size 1024,768 font "Verdana,15"
set output "UDP_5_st_2020_10_12_08-36-02_two2one_00032B.png"

set title "{/=20 Datagram size: 32 B, Av. rate: 630.56 Kb/s}\n\n{/=18 (LAPTOP-UE-2 to LAPTOP-UE-0, UDP, 5 st.)}"
set label "Warning:\nTest failed to finish!\nResults may not be accurate!" at screen 0.01, screen 0.96 tc rgb "red"

set xlabel "Time (s)"
set ylabel "Bandwidth (Kb/s)"
set ytics nomirror
set key bmargin center horizontal box samplen 1 width -1
set bmargin 4.6
set rmargin 4.5

rf = 1000.0  # rate factor
set style fill transparent solid 0.2 noborder
set autoscale xfix
plot "UDP_5_st_2020_10_12_08-36-02_two2one_00032B_iperf_processed.dat" using 1:($2/rf-$3/rf):($2/rf+$3/rf) with filledcurves lc rgb "blue" notitle, \
     "" using 1:($2/rf) with points pt 2 ps 1.5 lw 3 lc rgb "blue" title "Mean tot. BW", \
