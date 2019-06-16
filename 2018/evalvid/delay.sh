
. evalvid.conf

for mode in fx f0 p0; do
  count=0
  echo -n "time_[s]" > delay"_"$mode.txt
  for l in $RDDIR/$mode/delay/delay*.txt; do
    printf "\tPDF_`basename $l .txt` CDF_`basename $l .txt`" >> delay"_"$mode.txt
    [ $count == 0 ] && awk '{print $3}' < $l | ./hist - $T1_DELAY $T2_DELAY $T_STEPS | awk '{print $1}' > time.txt
    awk '{print $3}' < $l | ./hist - $T1_DELAY $T2_DELAY $T_STEPS | awk '{print $2,$3}' > tmp.txt
    [ $count != 0 ] && cp d"_"$mode.txt time.txt
    paste time.txt tmp.txt > d"_"$mode.txt
    count=$((count+1))
    printf "%8d %s\n" $count $l
  done
  echo "" >> delay"_"$mode.txt
  mv delay"_"$mode.txt mos_dir
  cat d"_"$mode.txt >> mos_dir/delay"_"$mode.txt
  rm d"_"$mode.txt time.txt tmp.txt
done
