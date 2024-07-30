About the FFmpeg library
---------------------------------------------------------------------------------------------------------
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, 
filter and play pretty much anything that humans and machines have created. It supports the most 
obscure ancient formats up to the cutting edge. No matter if they were designed by some standards 
committee, the community or a corporation. It is also highly portable: FFmpeg compiles, runs, and 
passes our testing infrastructure FATE across Linux, Mac OS X, Microsoft Windows, the BSDs, Solaris, 
etc. under a wide variety of build environments, machine architectures, and configurations.

It contains libavcodec, libavutil, libavformat, libavfilter, libavdevice, libswscale and libswresample 
which can be used by applications. As well as ffmpeg, ffserver, ffplay and ffprobe which can be 
used by end users for transcoding, streaming and playing.

The FFmpeg project tries to provide the best technically possible solution for developers of applications 
and end users alike. To achieve this we combine the best free software options available. We slightly 
favor our own code to keep the dependencies on other libs low and to maximize code sharing between parts 
of FFmpeg. Wherever the question of "best" cannot be answered we support both options so the end user 
can choose.

https://ffmpeg.org/


About the plugin
---------------------------------------------------------------------------------------------------------
The aimp_inputFFmpeg plugin is designed to play following formats using the FFmpeg library:
+ Sony OpenMG
+ TrueHD
+ ATRAC3
+ Matroska Audio
+ WebM Audio


How to build
---------------------------------------------------------------------------------------------------------
The plugin uses original FFmpeg v4.3.3 library that can be found here:
  https://ffmpeg.org/releases/ffmpeg-4.3.3.tar.xz
  https://www.aimp.ru/files/windows/sources/FFmpeg-4.3.3-aimp.zip

Apply following patch to common.mak:
  https://github.com/rdp/ffmpeg-windows-build-helpers/pull/558/files


The Zeranoe's MingGW-w64 Build Script have been used to setup required environment in Ubuntu 21:
https://github.com/Zeranoe/mingw-w64-build
Command line is:
  sudo apt-get update
  sudo apt-get install g++
  sudo apt-get install flex
  sudo apt-get install bison
  sudo apt-get install git
  sudo apt-get install curl
  sudo apt-get install make
  sudo apt-get install texinfo
  sudo apt-get install yasm
  ./mingw-w64-build i686 x86_64
  

FFmpeg build command line is (32-bit):
  PATH=$PATH:/home/artem/.zeranoe/mingw-w64/i686/bin
  cd /home/artem/FFmpeg/sources/
  PKG_CONFIG_PATH="/home/artem/FFmpeg/x86/lib/pkgconfig" LDFLAGS="-L/home/artem/FFmpeg/x86/lib" CFLAGS="-I/home/artem/FFmpeg/x86/include" /home/artem/FFmpeg/sources/configure --pkg-config=pkg-config --prefix="/home/artem/FFmpeg/x86" --arch=x86 --target-os=mingw32 --cross-prefix=i686-w64-mingw32- --enable-shared --disable-w32threads --disable-programs --disable-doc --disable-everything --disable-avdevice --enable-swresample --enable-swscale  --build_suffix=-aimp --enable-demuxer=aac --enable-demuxer=ogg --enable-demuxer=webm_dash_manifest --enable-decoder=aac --enable-decoder=vorbis --enable-decoder=opus --enable-demuxer=mov --enable-decoder=mp3* --enable-decoder=flac --enable-decoder=atrac3 --enable-decoder=atrac3al --enable-decoder=atrac3p  --enable-demuxer=oma --enable-decoder=pcm_* --enable-decoder=truehd --enable-decoder=ac3* --enable-demuxer=mp3
  make install
  
FFmpeg build command line is (64-bit):
  PATH=$PATH:/home/artem/.zeranoe/mingw-w64/x86_64/bin
  cd /home/artem/FFmpeg/sources/
  PKG_CONFIG_PATH="/home/artem/FFmpeg/x64/lib/pkgconfig" LDFLAGS="-L/home/artem/FFmpeg/x64/lib" CFLAGS="-I/home/artem/FFmpeg/x64/include" /home/artem/FFmpeg/sources/configure --pkg-config=pkg-config --prefix="/home/artem/FFmpeg/x64" --arch=x86_64 --target-os=mingw32 --cross-prefix=x86_64-w64-mingw32- --enable-shared --disable-w32threads --disable-programs --disable-doc --disable-everything --disable-avdevice --enable-swresample --enable-swscale  --build_suffix=-aimp --enable-demuxer=aac --enable-demuxer=ogg --enable-demuxer=webm_dash_manifest --enable-decoder=aac --enable-decoder=vorbis --enable-decoder=opus --enable-demuxer=mov --enable-decoder=mp3* --enable-decoder=flac --enable-decoder=atrac3 --enable-decoder=atrac3al --enable-decoder=atrac3p  --enable-demuxer=oma --enable-decoder=pcm_* --enable-decoder=truehd --enable-decoder=ac3* --enable-demuxer=mp3
  make install
