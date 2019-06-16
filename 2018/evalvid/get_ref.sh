
. evalvid.conf

test -e $REFDIR || mkdir $REFDIR
test -e $REFDIR/$YUVDIR || mkdir $REFDIR/$YUVDIR


for yuv in $YUVS; do
 ffmpeg -i $REFDIR/$RAWDIR/$yuv.264 $REFDIR/$YUVDIR/$yuv"_352x288".yuv 
done
