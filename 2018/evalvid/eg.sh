. evalvid.conf

for sd in $TRACEDIR/sd_*; do
  ID=`basename $sd | cut -c3-`
  test -e $TRACEDIR/rd$ID $TRACEDIR/st$ID || touch $TRACEDIR/rd$ID $TRACEDIR/st$ID
  ./eg $sd $TRACEDIR/rd$ID $TRACEDIR/st$ID AWGN $BER
done
