. evalvid.conf

test -e $TRACEDIR || mkdir $TRACEDIR

for mp4 in $SDDIR/$MP4DIR/*.mp4; do
  tcpdump -n -tt -v udp port 12346 > $TRACEDIR/sd"_"`basename $mp4 .mp4` &
  sleep 3
  ./mp4trace -f -s 192.168.0.2 12346 $mp4 > $TRACEDIR/st"_"`basename $mp4 .mp4`

  sleep 3
  killall tcpdump
  sleep 3
done

#nsa.gov
