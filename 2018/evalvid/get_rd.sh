. evalvid.conf

test -e rd||mkdir rd


for yuv in $YUVS; do
  ./etmp4 -f -x $TRACEDIR/"sd_"$yuv"_x264_264" $TRACEDIR/"rd_"$yuv"_x264_264" $TRACEDIR/"st_"$yuv"_x264_264" $SDDIR/$MP4DIR/$yuv"_x264_264".mp4 "fx_"$yuv

  ./etmp4 -f -0 $TRACEDIR/"sd_"$yuv"_x264_264" $TRACEDIR/"rd_"$yuv"_x264_264" $TRACEDIR/"st_"$yuv"_x264_264" $SDDIR/$MP4DIR/$yuv"_x264_264".mp4 "f0_"$yuv 
  
  ./etmp4 -p -0 $TRACEDIR/"sd_"$yuv"_x264_264" $TRACEDIR/"rd_"$yuv"_x264_264" $TRACEDIR/"st_"$yuv"_x264_264" $SDDIR/$MP4DIR/$yuv"_x264_264".mp4 "p0_"$yuv

  for code in $CODES; do
    test -e rd/$code||mkdir rd/$code
    test -e rd/$code/mp4||mkdir rd/$code/mp4
    test -e rd/$code/raw||mkdir rd/$code/raw
    test -e rd/$code/lose||mkdir rd/$code/lose
    test -e rd/$code/delay||mkdir rd/$code/delay
    test -e rd/$code/rate||mkdir rd/$code/rate
    test -e rd/$code/yuv||mkdir rd/$code/yuv
    test -e rd/$code/mp4||mkdir rd/$code/mp4
    mv -f $code"_"$yuv.mp4 rd/$code/mp4/$code"_"$yuv.mp4
    mv -f $code"_"$yuv.264 rd/$code/raw/$code"_"$yuv.264
    mv -f  "loss_"$code"_"$yuv.txt rd/$code/lose/"loss_"$code"_"$yuv.txt
    mv -f  "delay_"$code"_"$yuv.txt rd/$code/delay/"delay_"$code"_"$yuv.txt
    mv -f  "rate_s_"$code"_"$yuv.txt rd/$code/rate/"rate_s_"$code"_"$yuv.txt
    mv -f  "rate_r_"$code"_"$yuv.txt rd/$code/rate/"rate_r_"$code"_"$yuv.txt
    ffmpeg -i rd/$code/mp4/$code"_"$yuv.mp4 rd/$code/yuv/$code"_"$yuv"_352x288".yuv
  done 
done


