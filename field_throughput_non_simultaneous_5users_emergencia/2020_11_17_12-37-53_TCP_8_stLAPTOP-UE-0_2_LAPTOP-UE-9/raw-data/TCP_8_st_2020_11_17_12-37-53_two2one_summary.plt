set terminal pngcairo nocrop enhanced size 1024,768 font "Verdana,15"
set output "TCP_8_st_2020_11_17_12-37-53_two2one_summary.png"

set title "{/=20 Bandwidth \\& CPU usage for different packet sizes}\n\n{/=18 (LAPTOP-UE-9 to LAPTOP-UE-0, TCP, 8 st.)}"

set xlabel "Buffer size"
set ylabel "Bandwidth (Mb/s)"
set ytics nomirror
set key bmargin center horizontal box samplen 1 width -1
set bmargin 4.6
set rmargin 4.5
set xtics rotate by -30
printxsizes(x) = x < 1024.0 ? sprintf("%.0fB", x) : (x < 1048576.0 ? sprintf("%.0fKB", x/1024.0) : sprintf("%.0fMB", x/1048576.0))

rf = 1000000.0  # rate factor
stats "TCP_8_st_2020_11_17_12-37-53_two2one_iperf_summary.dat" using ($1 >= 0 ? $3 : 1/0) nooutput
set logscale x 2
set style fill transparent solid 0.2 noborder
set autoscale xfix
plot "TCP_8_st_2020_11_17_12-37-53_two2one_iperf_summary.dat" using ($1 >= 0 ? $2 : 1/0):($3/rf-$4/rf):($3/rf+$4/rf) with filledcurves lc rgb "blue" notitle, \
     "" using 2:($1 == 0 ? $3/rf : 1/0):xtic(printxsizes($2)) with points pt 2 ps 1.5 lw 3 lc rgb "magenta" title "Approx. BW", \
     "" using 2:($1 >= 0 ? $3/rf : 1/0):(sprintf("%.2f Mb/s", $3/rf)) with labels offset 0.9,1.0 rotate by 90 font ",12" notitle, \
     "" using ($1 < 0 ? $2 : 1/0):(STATS_min/rf):(sprintf("Net test failed!")) with labels offset 0.9,2.5 rotate by 90 tc rgb "red" font ",12" notitle, \
