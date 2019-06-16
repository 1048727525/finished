. evalvid.conf
rm -rf mos_dir
test -e mos_dir||mkdir mos_dir

for yuv in $YUVS; do
  test -e mos_dir/$yuv"_work"||mkdir mos_dir/$yuv"_work"
  for code in $CODES; do
     cp -f psnr_dir/rd/$code/$code"_psnr_"$yuv.txt mos_dir/$yuv"_work"/$code"_psnr_"$yuv.txt
  done
  ./mos mos_dir/$yuv"_work" psnr_dir/ref/"psnr_"$yuv.txt 25 >> mos_dir/mos.txt
  ./miv mos_dir/$yuv"_work">> mos_dir/miv.txt
done
  
