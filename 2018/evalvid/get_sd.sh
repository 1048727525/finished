
. evalvid.conf

test -e $SDDIR || mkdir $SDDIR
test -e $SDDIR/$YUVDIR || mkdir $SDDIR/$YUVDIR
test -e $SDDIR/$MP4DIR || mkdir $SDDIR/$MP4DIR
test -e $SDDIR/$RAWDIR || mkdir $SDDIR/$RAWDIR

for yuv in $YUVS; do
  x264 -I $GOP -B $KBPS --fps $FPS -o $SDDIR/$RAWDIR/$yuv"_"x264.264 --input-res 352x288 $REFDIR/$YUVDIR/$yuv"_352x288".yuv 
done

for raw in $SDDIR/$RAWDIR/*.*; do
  mp4=`echo $raw | cut -d. -f1`"_"`echo $raw | cut -d. -f2`
  mp4=$SDDIR/$MP4DIR/`echo $mp4 | cut -d/ -f3`.mp4
  MP4Box -hint -mtu $MTU -fps $FPS -add $raw $mp4
done

for mp4 in $SDDIR/$MP4DIR/*.*;do
  yuv=`echo $mp4 | cut -d. -f1`
  yuv=$SDDIR/$YUVDIR/`echo $yuv | cut -d/ -f3`"_352x288".yuv
  ffmpeg -i $mp4 $yuv
done
