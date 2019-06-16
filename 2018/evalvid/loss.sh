. evalvid.conf

for mode in fx f0 p0; do
  echo -n "" > loss"_"$mode
  echo -n "" > tmp.txt
  for l in $RDDIR/$mode/lose/loss*.txt; do
    echo $l
    echo `basename $l .txt` >> loss"_"$mode
    cat $l >> tmp.txt
  done
  paste loss"_"$mode tmp.txt > mos_dir/loss"_"$mode.txt
  rm loss"_"$mode tmp.txt
done
