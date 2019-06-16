. evalvid.conf

test -e psnr_dir||mkdir psnr_dir
test -e psnr_dir/rd||mkdir psnr_dir/rd
test -e psnr_dir/ref||mkdir psnr_dir/ref
test -e psnr_dir/rd/f0||mkdir psnr_dir/rd/f0
test -e psnr_dir/rd/fx||mkdir psnr_dir/rd/fx
test -e psnr_dir/rd/p0||mkdir psnr_dir/rd/p0

for yuv in $YUVS; do
  ./psnr 352 288 420 $REFDIR/$YUVDIR/$yuv"_352x288".yuv $SDDIR/$YUVDIR/$yuv"_x264_264_352x288".yuv > psnr_dir/ref/"psnr_"$yuv.txt 
  for code in $CODES; do
  ./psnr 352 288 420 $REFDIR/$YUVDIR/$yuv"_352x288".yuv $RDDIR/$code/$YUVDIR/$code"_"$yuv"_352x288".yuv > psnr_dir/rd/$code/$code"_psnr_"$yuv.txt 
  done
done
  
