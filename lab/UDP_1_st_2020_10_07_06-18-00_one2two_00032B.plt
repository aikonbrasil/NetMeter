set terminal pngcairo nocrop enhanced size 1024,768 font "Verdana,15"
set output "UDP_1_st_2020_10_07_06-18-00_one2two_00032B.png"

set title "{/=20 print UNIT size: 100 B, Av. rate: 15.00 ms}\n\n{/=18 (name1 to name2, UDP, 6 st.)}"

set xlabel "Time (s)"
set ylabel "Latency (ms)"
set format y "%.1f"
set key bmargin center horizontal box samplen 1 width -1
set bmargin 4.6
set rmargin 4.5

rf = 1.0  # rate factor
set style fill transparent solid 0.2 noborder
set autoscale xfix
set autoscale yfix
plot "UDP_1_st_2020_10_07_06-18-00_one2two_00032B_iperf_processed.dat" using 1:($2/rf-$3/rf):($2/rf+$3/rf) with filledcurves lc rgb "blue" notitle, \
     "" using 1:($2/rf) with points pt 2 ps 1.5 lw 3 lc rgb "blue" title "Mean tot. BW", \
