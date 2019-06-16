rm -rf mos_dir
rm -rf psnr_dir
rm -rf rd
rm -rf sd
rm -rf traces
rm -rf ref/yuv
./get_ref.sh  # encode all videos 
./get_sd.sh  # pack in mp4-container and hint
./send.sh    # send and generate sender traces
./eg.sh      # generate receiver traces
./get_rd.sh     # calculate reference PSNR
./get_psnr.sh   # calculate loss, delay, rate; generate received videos
./get_mos.sh
./loss.sh
./delay.sh

