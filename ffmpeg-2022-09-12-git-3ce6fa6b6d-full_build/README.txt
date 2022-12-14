FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2022-09-12-git-3ce6fa6b6d-full_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/3ce6fa6b6d

External Assets
frei0r plugins:   https://www.gyan.dev/ffmpeg/builds/ffmpeg-frei0r-plugins
lensfun database: https://www.gyan.dev/ffmpeg/builds/ffmpeg-lensfun-db

git-full build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    yes
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libilbc                 libsvtav1
bzlib                   libjxl                  libtheora
chromaprint             liblensfun              libtwolame
frei0r                  libmodplug              libuavs3d
gmp                     libmp3lame              libvidstab
gnutls                  libmysofa               libvmaf
iconv                   libopencore_amrnb       libvo_amrwbenc
ladspa                  libopencore_amrwb       libvorbis
libaom                  libopenjpeg             libvpx
libass                  libopenmpt              libwebp
libbluray               libopus                 libx264
libbs2b                 libplacebo              libx265
libcaca                 librav1e                libxavs2
libcdio                 librist                 libxml2
libdav1d                librubberband           libxvid
libdavs2                libshaderc              libzimg
libflite                libshine                libzmq
libfontconfig           libsnappy               libzvbi
libfreetype             libsoxr                 lzma
libfribidi              libspeex                mediafoundation
libgme                  libsrt                  sdl2
libgsm                  libssh                  zlib

External libraries providing hardware acceleration:
amf                     d3d11va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               opencl
cuvid                   libmfx                  vulkan

Libraries:
avcodec                 avformat                swresample
avdevice                avutil                  swscale
avfilter                postproc

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     fourxm                  pcm_u32be
aac_fixed               fraps                   pcm_u32le
aac_latm                frwu                    pcm_u8
aasc                    g2m                     pcm_vidc
ac3                     g723_1                  pcx
ac3_fixed               g729                    pfm
acelp_kelvin            gdv                     pgm
adpcm_4xm               gem                     pgmyuv
adpcm_adx               gif                     pgssub
adpcm_afc               gremlin_dpcm            pgx
adpcm_agm               gsm                     phm
adpcm_aica              gsm_ms                  photocd
adpcm_argo              h261                    pictor
adpcm_ct                h263                    pixlet
adpcm_dtk               h263i                   pjs
adpcm_ea                h263p                   png
adpcm_ea_maxis_xa       h264                    ppm
adpcm_ea_r1             h264_cuvid              prores
adpcm_ea_r2             h264_qsv                prosumer
adpcm_ea_r3             hap                     psd
adpcm_ea_xas            hca                     ptx
adpcm_g722              hcom                    qcelp
adpcm_g726              hdr                     qdm2
adpcm_g726le            hevc                    qdmc
adpcm_ima_acorn         hevc_cuvid              qdraw
adpcm_ima_alp           hevc_qsv                qoi
adpcm_ima_amv           hnm4_video              qpeg
adpcm_ima_apc           hq_hqa                  qtrle
adpcm_ima_apm           hqx                     r10k
adpcm_ima_cunning       huffyuv                 r210
adpcm_ima_dat4          hymt                    ra_144
adpcm_ima_dk3           iac                     ra_288
adpcm_ima_dk4           idcin                   ralf
adpcm_ima_ea_eacs       idf                     rasc
adpcm_ima_ea_sead       iff_ilbm                rawvideo
adpcm_ima_iss           ilbc                    realtext
adpcm_ima_moflex        imc                     rl2
adpcm_ima_mtf           imm4                    roq
adpcm_ima_oki           imm5                    roq_dpcm
adpcm_ima_qt            indeo2                  rpza
adpcm_ima_rad           indeo3                  rscc
adpcm_ima_smjpeg        indeo4                  rv10
adpcm_ima_ssi           indeo5                  rv20
adpcm_ima_wav           interplay_acm           rv30
adpcm_ima_ws            interplay_dpcm          rv40
adpcm_ms                interplay_video         s302m
adpcm_mtaf              ipu                     sami
adpcm_psx               jacosub                 sanm
adpcm_sbpro_2           jpeg2000                sbc
adpcm_sbpro_3           jpegls                  scpr
adpcm_sbpro_4           jv                      screenpresso
adpcm_swf               kgv1                    sdx2_dpcm
adpcm_thp               kmvc                    sga
adpcm_thp_le            lagarith                sgi
adpcm_vima              libaom_av1              sgirle
adpcm_xa                libdav1d                sheervideo
adpcm_yamaha            libdavs2                shorten
adpcm_zork              libgsm                  simbiosis_imx
agm                     libgsm_ms               sipr
aic                     libilbc                 siren
alac                    libjxl                  smackaud
alias_pix               libopencore_amrnb       smacker
als                     libopencore_amrwb       smc
amrnb                   libopenjpeg             smvjpeg
amrwb                   libopus                 snow
amv                     libspeex                sol_dpcm
anm                     libuavs3d               sonic
ansi                    libvorbis               sp5x
ape                     libvpx_vp8              speedhq
apng                    libvpx_vp9              speex
aptx                    libzvbi_teletext        srgc
aptx_hd                 loco                    srt
arbc                    lscr                    ssa
argo                    m101                    stl
ass                     mace3                   subrip
asv1                    mace6                   subviewer
asv2                    magicyuv                subviewer1
atrac1                  mdec                    sunrast
atrac3                  metasound               svq1
atrac3al                microdvd                svq3
atrac3p                 mimic                   tak
atrac3pal               mjpeg                   targa
atrac9                  mjpeg_cuvid             targa_y216
aura                    mjpeg_qsv               tdsc
aura2                   mjpegb                  text
av1                     mlp                     theora
av1_cuvid               mmvideo                 thp
av1_qsv                 mobiclip                tiertexseqvideo
avrn                    motionpixels            tiff
avrp                    movtext                 tmv
avs                     mp1                     truehd
avui                    mp1float                truemotion1
ayuv                    mp2                     truemotion2
bethsoftvid             mp2float                truemotion2rt
bfi                     mp3                     truespeech
bink                    mp3adu                  tscc
binkaudio_dct           mp3adufloat             tscc2
binkaudio_rdft          mp3float                tta
bintext                 mp3on4                  twinvq
bitpacked               mp3on4float             txd
bmp                     mpc7                    ulti
bmv_audio               mpc8                    utvideo
bmv_video               mpeg1_cuvid             v210
bonk                    mpeg1video              v210x
brender_pix             mpeg2_cuvid             v308
c93                     mpeg2_qsv               v408
cavs                    mpeg2video              v410
ccaption                mpeg4                   vb
cdgraphics              mpeg4_cuvid             vble
cdtoons                 mpegvideo               vbn
cdxl                    mpl2                    vc1
cfhd                    msa1                    vc1_cuvid
cinepak                 mscc                    vc1_qsv
clearvideo              msmpeg4v1               vc1image
cljr                    msmpeg4v2               vcr1
cllc                    msmpeg4v3               vmdaudio
comfortnoise            msnsiren                vmdvideo
cook                    msp2                    vmnc
cpia                    msrle                   vorbis
cri                     mss1                    vp3
cscd                    mss2                    vp4
cyuv                    msvideo1                vp5
dca                     mszh                    vp6
dds                     mts2                    vp6a
derf_dpcm               mv30                    vp6f
dfa                     mvc1                    vp7
dfpwm                   mvc2                    vp8
dirac                   mvdv                    vp8_cuvid
dnxhd                   mvha                    vp8_qsv
dolby_e                 mwsc                    vp9
dpx                     mxpeg                   vp9_cuvid
dsd_lsbf                nellymoser              vp9_qsv
dsd_lsbf_planar         notchlc                 vplayer
dsd_msbf                nuv                     vqa
dsd_msbf_planar         on2avc                  wavpack
dsicinaudio             opus                    wbmp
dsicinvideo             paf_audio               wcmv
dss_sp                  paf_video               webp
dst                     pam                     webvtt
dvaudio                 pbm                     wmalossless
dvbsub                  pcm_alaw                wmapro
dvdsub                  pcm_bluray              wmav1
dvvideo                 pcm_dvd                 wmav2
dxa                     pcm_f16le               wmavoice
dxtory                  pcm_f24le               wmv1
dxv                     pcm_f32be               wmv2
eac3                    pcm_f32le               wmv3
eacmv                   pcm_f64be               wmv3image
eamad                   pcm_f64le               wnv1
eatgq                   pcm_lxf                 wrapped_avframe
eatgv                   pcm_mulaw               ws_snd1
eatqi                   pcm_s16be               xan_dpcm
eightbps                pcm_s16be_planar        xan_wc3
eightsvx_exp            pcm_s16le               xan_wc4
eightsvx_fib            pcm_s16le_planar        xbin
escape124               pcm_s24be               xbm
escape130               pcm_s24daud             xface
evrc                    pcm_s24le               xl
exr                     pcm_s24le_planar        xma1
fastaudio               pcm_s32be               xma2
ffv1                    pcm_s32le               xpm
ffvhuff                 pcm_s32le_planar        xsub
ffwavesynth             pcm_s64be               xwd
fic                     pcm_s64le               y41p
fits                    pcm_s8                  ylc
flac                    pcm_s8_planar           yop
flashsv                 pcm_sga                 yuv4
flashsv2                pcm_u16be               zero12v
flic                    pcm_u16le               zerocodec
flv                     pcm_u24be               zlib
fmvc                    pcm_u24le               zmbv

Enabled encoders:
a64multi                jpeg2000                pcm_u16le
a64multi5               jpegls                  pcm_u24be
aac                     libaom_av1              pcm_u24le
aac_mf                  libgsm                  pcm_u32be
ac3                     libgsm_ms               pcm_u32le
ac3_fixed               libilbc                 pcm_u8
ac3_mf                  libjxl                  pcm_vidc
adpcm_adx               libmp3lame              pcx
adpcm_argo              libopencore_amrnb       pfm
adpcm_g722              libopenjpeg             pgm
adpcm_g726              libopus                 pgmyuv
adpcm_g726le            librav1e                phm
adpcm_ima_alp           libshine                png
adpcm_ima_amv           libspeex                ppm
adpcm_ima_apm           libsvtav1               prores
adpcm_ima_qt            libtheora               prores_aw
adpcm_ima_ssi           libtwolame              prores_ks
adpcm_ima_wav           libvo_amrwbenc          qoi
adpcm_ima_ws            libvorbis               qtrle
adpcm_ms                libvpx_vp8              r10k
adpcm_swf               libvpx_vp9              r210
adpcm_yamaha            libwebp                 ra_144
alac                    libwebp_anim            rawvideo
alias_pix               libx264                 roq
amv                     libx264rgb              roq_dpcm
apng                    libx265                 rpza
aptx                    libxavs2                rv10
aptx_hd                 libxvid                 rv20
ass                     ljpeg                   s302m
asv1                    magicyuv                sbc
asv2                    mjpeg                   sgi
avrp                    mjpeg_qsv               smc
avui                    mlp                     snow
ayuv                    movtext                 sonic
bitpacked               mp2                     sonic_ls
bmp                     mp2fixed                speedhq
cfhd                    mp3_mf                  srt
cinepak                 mpeg1video              ssa
cljr                    mpeg2_qsv               subrip
comfortnoise            mpeg2video              sunrast
dca                     mpeg4                   svq1
dfpwm                   msmpeg4v2               targa
dnxhd                   msmpeg4v3               text
dpx                     msvideo1                tiff
dvbsub                  nellymoser              truehd
dvdsub                  opus                    tta
dvvideo                 pam                     ttml
eac3                    pbm                     utvideo
exr                     pcm_alaw                v210
ffv1                    pcm_bluray              v308
ffvhuff                 pcm_dvd                 v408
fits                    pcm_f32be               v410
flac                    pcm_f32le               vbn
flashsv                 pcm_f64be               vc2
flashsv2                pcm_f64le               vorbis
flv                     pcm_mulaw               vp9_qsv
g723_1                  pcm_s16be               wavpack
gif                     pcm_s16be_planar        wbmp
h261                    pcm_s16le               webvtt
h263                    pcm_s16le_planar        wmav1
h263p                   pcm_s24be               wmav2
h264_amf                pcm_s24daud             wmv1
h264_mf                 pcm_s24le               wmv2
h264_nvenc              pcm_s24le_planar        wrapped_avframe
h264_qsv                pcm_s32be               xbm
hap                     pcm_s32le               xface
hdr                     pcm_s32le_planar        xsub
hevc_amf                pcm_s64be               xwd
hevc_mf                 pcm_s64le               y41p
hevc_nvenc              pcm_s8                  yuv4
hevc_qsv                pcm_s8_planar           zlib
huffyuv                 pcm_u16be               zmbv

Enabled hwaccels:
av1_d3d11va             hevc_nvdec              vc1_nvdec
av1_d3d11va2            mjpeg_nvdec             vp8_nvdec
av1_dxva2               mpeg1_nvdec             vp9_d3d11va
av1_nvdec               mpeg2_d3d11va           vp9_d3d11va2
h264_d3d11va            mpeg2_d3d11va2          vp9_dxva2
h264_d3d11va2           mpeg2_dxva2             vp9_nvdec
h264_dxva2              mpeg2_nvdec             wmv3_d3d11va
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va2
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_dxva2              vc1_dxva2

Enabled parsers:
aac                     dvd_nav                 opus
aac_latm                dvdsub                  png
ac3                     flac                    pnm
adx                     g723_1                  qoi
amr                     g729                    rv30
av1                     gif                     rv40
avs2                    gsm                     sbc
avs3                    h261                    sipr
bmp                     h263                    tak
cavsvideo               h264                    vc1
cook                    hdr                     vorbis
cri                     hevc                    vp3
dca                     ipu                     vp8
dirac                   jpeg2000                vp9
dnxhd                   mjpeg                   webp
dolby_e                 mlp                     xbm
dpx                     mpeg4video              xma
dvaudio                 mpegaudio
dvbsub                  mpegvideo

Enabled demuxers:
aa                      ico                     pcm_alaw
aac                     idcin                   pcm_f32be
aax                     idf                     pcm_f32le
ac3                     iff                     pcm_f64be
ace                     ifv                     pcm_f64le
acm                     ilbc                    pcm_mulaw
act                     image2                  pcm_s16be
adf                     image2_alias_pix        pcm_s16le
adp                     image2_brender_pix      pcm_s24be
ads                     image2pipe              pcm_s24le
adx                     image_bmp_pipe          pcm_s32be
aea                     image_cri_pipe          pcm_s32le
afc                     image_dds_pipe          pcm_s8
aiff                    image_dpx_pipe          pcm_u16be
aix                     image_exr_pipe          pcm_u16le
alp                     image_gem_pipe          pcm_u24be
amr                     image_gif_pipe          pcm_u24le
amrnb                   image_hdr_pipe          pcm_u32be
amrwb                   image_j2k_pipe          pcm_u32le
anm                     image_jpeg_pipe         pcm_u8
apc                     image_jpegls_pipe       pcm_vidc
ape                     image_jpegxl_pipe       pjs
apm                     image_pam_pipe          pmp
apng                    image_pbm_pipe          pp_bnk
aptx                    image_pcx_pipe          pva
aptx_hd                 image_pfm_pipe          pvf
aqtitle                 image_pgm_pipe          qcp
argo_asf                image_pgmyuv_pipe       r3d
argo_brp                image_pgx_pipe          rawvideo
argo_cvg                image_phm_pipe          realtext
asf                     image_photocd_pipe      redspark
asf_o                   image_pictor_pipe       rl2
ass                     image_png_pipe          rm
ast                     image_ppm_pipe          roq
au                      image_psd_pipe          rpl
av1                     image_qdraw_pipe        rsd
avi                     image_qoi_pipe          rso
avisynth                image_sgi_pipe          rtp
avr                     image_sunrast_pipe      rtsp
avs                     image_svg_pipe          s337m
avs2                    image_tiff_pipe         sami
avs3                    image_vbn_pipe          sap
bethsoftvid             image_webp_pipe         sbc
bfi                     image_xbm_pipe          sbg
bfstm                   image_xpm_pipe          scc
bink                    image_xwd_pipe          scd
binka                   imf                     sdp
bintext                 ingenient               sdr2
bit                     ipmovie                 sds
bitpacked               ipu                     sdx
bmv                     ircam                   segafilm
boa                     iss                     ser
bonk                    iv8                     sga
brstm                   ivf                     shorten
c93                     ivr                     siff
caf                     jacosub                 simbiosis_imx
cavsvideo               jv                      sln
cdg                     kux                     smacker
cdxl                    kvag                    smjpeg
cine                    libgme                  smush
codec2                  libmodplug              sol
codec2raw               libopenmpt              sox
concat                  live_flv                spdif
dash                    lmlm4                   srt
data                    loas                    stl
daud                    lrc                     str
dcstr                   luodat                  subviewer
derf                    lvf                     subviewer1
dfa                     lxf                     sup
dfpwm                   m4v                     svag
dhav                    matroska                svs
dirac                   mca                     swf
dnxhd                   mcc                     tak
dsf                     mgsts                   tedcaptions
dsicin                  microdvd                thp
dss                     mjpeg                   threedostr
dts                     mjpeg_2000              tiertexseq
dtshd                   mlp                     tmv
dv                      mlv                     truehd
dvbsub                  mm                      tta
dvbtxt                  mmf                     tty
dxa                     mods                    txd
ea                      moflex                  ty
ea_cdata                mov                     v210
eac3                    mp3                     v210x
epaf                    mpc                     vag
ffmetadata              mpc8                    vc1
filmstrip               mpegps                  vc1t
fits                    mpegts                  vividas
flac                    mpegtsraw               vivo
flic                    mpegvideo               vmd
flv                     mpjpeg                  vobsub
fourxm                  mpl2                    voc
frm                     mpsub                   vpk
fsb                     msf                     vplayer
fwse                    msnwc_tcp               vqf
g722                    msp                     w64
g723_1                  mtaf                    wav
g726                    mtv                     wc3
g726le                  musx                    webm_dash_manifest
g729                    mv                      webvtt
gdv                     mvi                     wsaud
genh                    mxf                     wsd
gif                     mxg                     wsvqa
gsm                     nc                      wtv
gxf                     nistsphere              wv
h261                    nsp                     wve
h263                    nsv                     xa
h264                    nut                     xbin
hca                     nuv                     xmv
hcom                    obu                     xvag
hevc                    ogg                     xwma
hls                     oma                     yop
hnm                     paf                     yuv4mpegpipe

Enabled muxers:
a64                     h263                    pcm_s24be
ac3                     h264                    pcm_s24le
adts                    hash                    pcm_s32be
adx                     hds                     pcm_s32le
aiff                    hevc                    pcm_s8
alp                     hls                     pcm_u16be
amr                     ico                     pcm_u16le
amv                     ilbc                    pcm_u24be
apm                     image2                  pcm_u24le
apng                    image2pipe              pcm_u32be
aptx                    ipod                    pcm_u32le
aptx_hd                 ircam                   pcm_u8
argo_asf                ismv                    pcm_vidc
argo_cvg                ivf                     psp
asf                     jacosub                 rawvideo
asf_stream              kvag                    rm
ass                     latm                    roq
ast                     lrc                     rso
au                      m4v                     rtp
avi                     matroska                rtp_mpegts
avif                    matroska_audio          rtsp
avm2                    md5                     sap
avs2                    microdvd                sbc
avs3                    mjpeg                   scc
bit                     mkvtimestamp_v2         segafilm
caf                     mlp                     segment
cavsvideo               mmf                     smjpeg
chromaprint             mov                     smoothstreaming
codec2                  mp2                     sox
codec2raw               mp3                     spdif
crc                     mp4                     spx
dash                    mpeg1system             srt
data                    mpeg1vcd                stream_segment
daud                    mpeg1video              streamhash
dfpwm                   mpeg2dvd                sup
dirac                   mpeg2svcd               swf
dnxhd                   mpeg2video              tee
dts                     mpeg2vob                tg2
dv                      mpegts                  tgp
eac3                    mpjpeg                  truehd
f4v                     mxf                     tta
ffmetadata              mxf_d10                 ttml
fifo                    mxf_opatom              uncodedframecrc
fifo_test               null                    vc1
filmstrip               nut                     vc1t
fits                    obu                     voc
flac                    oga                     w64
flv                     ogg                     wav
framecrc                ogv                     webm
framehash               oma                     webm_chunk
framemd5                opus                    webm_dash_manifest
g722                    pcm_alaw                webp
g723_1                  pcm_f32be               webvtt
g726                    pcm_f32le               wsaud
g726le                  pcm_f64be               wtv
gif                     pcm_f64le               wv
gsm                     pcm_mulaw               yuv4mpegpipe
gxf                     pcm_s16be
h261                    pcm_s16le

Enabled protocols:
async                   httpproxy               rtmpe
bluray                  https                   rtmps
cache                   icecast                 rtmpt
concat                  ipfs                    rtmpte
concatf                 ipns                    rtmpts
crypto                  librist                 rtp
data                    libsrt                  srtp
ffrtmpcrypt             libssh                  subfile
ffrtmphttp              libzmq                  tcp
file                    md5                     tee
ftp                     mmsh                    tls
gopher                  mmst                    udp
gophers                 pipe                    udplite
hls                     prompeg
http                    rtmp

Enabled filters:
a3dscope                deband                  pad
abench                  deblock                 pad_opencl
abitscope               decimate                pal100bars
acompressor             deconvolve              pal75bars
acontrast               dedot                   palettegen
acopy                   deesser                 paletteuse
acrossfade              deflate                 pan
acrossover              deflicker               perms
acrusher                deinterlace_qsv         perspective
acue                    dejudder                phase
addroi                  delogo                  photosensitivity
adeclick                derain                  pixdesctest
adeclip                 deshake                 pixelize
adecorrelate            deshake_opencl          pixscope
adelay                  despill                 pp
adenorm                 detelecine              pp7
aderivative             dialoguenhance          premultiply
adrawgraph              dilation                prewitt
adynamicequalizer       dilation_opencl         prewitt_opencl
adynamicsmooth          displace                program_opencl
aecho                   dnn_classify            pseudocolor
aemphasis               dnn_detect              psnr
aeval                   dnn_processing          pullup
aevalsrc                doubleweave             qp
aexciter                drawbox                 random
afade                   drawgraph               readeia608
afftdn                  drawgrid                readvitc
afftfilt                drawtext                realtime
afifo                   drmeter                 remap
afir                    dynaudnorm              remap_opencl
afirsrc                 earwax                  removegrain
aformat                 ebur128                 removelogo
afreqshift              edgedetect              repeatfields
afwtdn                  elbg                    replaygain
agate                   entropy                 reverse
agraphmonitor           epx                     rgbashift
ahistogram              eq                      rgbtestsrc
aiir                    equalizer               roberts
aintegral               erosion                 roberts_opencl
ainterleave             erosion_opencl          rotate
alatency                estdif                  rubberband
alimiter                exposure                sab
allpass                 extractplanes           scale
allrgb                  extrastereo             scale2ref
allyuv                  fade                    scale_cuda
aloop                   feedback                scale_qsv
alphaextract            fftdnoiz                scale_vulkan
alphamerge              fftfilt                 scdet
amerge                  field                   scharr
ametadata               fieldhint               scroll
amix                    fieldmatch              segment
amovie                  fieldorder              select
amplify                 fifo                    selectivecolor
amultiply               fillborders             sendcmd
anequalizer             find_rect               separatefields
anlmdn                  firequalizer            setdar
anlmf                   flanger                 setfield
anlms                   flip_vulkan             setparams
anoisesrc               flite                   setpts
anull                   floodfill               setrange
anullsink               format                  setsar
anullsrc                fps                     settb
apad                    framepack               shear
aperms                  framerate               showcqt
aphasemeter             framestep               showfreqs
aphaser                 freezedetect            showinfo
aphaseshift             freezeframes            showpalette
apsyclip                frei0r                  showspatial
apulsator               frei0r_src              showspectrum
arealtime               fspp                    showspectrumpic
aresample               gblur                   showvolume
areverse                gblur_vulkan            showwaves
arnndn                  geq                     showwavespic
asdr                    gradfun                 shuffleframes
asegment                gradients               shufflepixels
aselect                 graphmonitor            shuffleplanes
asendcmd                grayworld               sidechaincompress
asetnsamples            greyedge                sidechaingate
asetpts                 guided                  sidedata
asetrate                haas                    sierpinski
asettb                  haldclut                signalstats
ashowinfo               haldclutsrc             signature
asidedata               hdcd                    silencedetect
asoftclip               headphone               silenceremove
aspectralstats          hflip                   sinc
asplit                  hflip_vulkan            sine
ass                     highpass                siti
astats                  highshelf               smartblur
astreamselect           hilbert                 smptebars
asubboost               histeq                  smptehdbars
asubcut                 histogram               sobel
asupercut               hqdn3d                  sobel_opencl
asuperpass              hqx                     sofalizer
asuperstop              hstack                  spectrumsynth
atadenoise              hsvhold                 speechnorm
atempo                  hsvkey                  split
atilt                   hue                     spp
atrim                   huesaturation           sr
avectorscope            hwdownload              ssim
avgblur                 hwmap                   stereo3d
avgblur_opencl          hwupload                stereotools
avgblur_vulkan          hwupload_cuda           stereowiden
avsynctest              hysteresis              streamselect
axcorrelate             identity                subtitles
azmq                    idet                    super2xsai
bandpass                il                      superequalizer
bandreject              inflate                 surround
bass                    interlace               swaprect
bbox                    interleave              swapuv
bench                   join                    tblend
bilateral               kerndeint               telecine
bilateral_cuda          kirsch                  testsrc
biquad                  ladspa                  testsrc2
bitplanenoise           lagfun                  thistogram
blackdetect             latency                 threshold
blackframe              lenscorrection          thumbnail
blend                   lensfun                 thumbnail_cuda
blend_vulkan            libplacebo              tile
blockdetect             libvmaf                 tiltshelf
blurdetect              life                    tinterlace
bm3d                    limitdiff               tlut2
boxblur                 limiter                 tmedian
boxblur_opencl          loop                    tmidequalizer
bs2b                    loudnorm                tmix
bwdif                   lowpass                 tonemap
cas                     lowshelf                tonemap_opencl
cellauto                lumakey                 tpad
channelmap              lut                     transpose
channelsplit            lut1d                   transpose_opencl
chorus                  lut2                    transpose_vulkan
chromaber_vulkan        lut3d                   treble
chromahold              lutrgb                  tremolo
chromakey               lutyuv                  trim
chromakey_cuda          mandelbrot              unpremultiply
chromanr                maskedclamp             unsharp
chromashift             maskedmax               unsharp_opencl
ciescope                maskedmerge             untile
codecview               maskedmin               v360
color                   maskedthreshold         vaguedenoiser
colorbalance            maskfun                 varblur
colorchannelmixer       mcompand                vectorscope
colorchart              median                  vflip
colorcontrast           mergeplanes             vflip_vulkan
colorcorrect            mestimate               vfrdet
colorhold               metadata                vibrance
colorize                midequalizer            vibrato
colorkey                minterpolate            vidstabdetect
colorkey_opencl         mix                     vidstabtransform
colorlevels             monochrome              vif
colormap                morpho                  vignette
colormatrix             movie                   virtualbass
colorspace              mpdecimate              vmafmotion
colorspectrum           mptestsrc               volume
colortemperature        msad                    volumedetect
compand                 multiply                vpp_qsv
compensationdelay       negate                  vstack
concat                  nlmeans                 w3fdif
convolution             nlmeans_opencl          waveform
convolution_opencl      nnedi                   weave
convolve                noformat                xbr
copy                    noise                   xcorrelate
cover_rect              normalize               xfade
crop                    null                    xfade_opencl
cropdetect              nullsink                xmedian
crossfeed               nullsrc                 xstack
crystalizer             openclsrc               yadif
cue                     oscilloscope            yadif_cuda
curves                  overlay                 yaepblur
datascope               overlay_cuda            yuvtestsrc
dblur                   overlay_opencl          zmq
dcshift                 overlay_qsv             zoompan
dctdnoiz                overlay_vulkan          zscale
ddagrab                 owdenoise

Enabled bsfs:
aac_adtstoasc           h264_redundant_pps      opus_metadata
av1_frame_merge         hapqa_extract           pcm_rechunk
av1_frame_split         hevc_metadata           pgs_frame_merge
av1_metadata            hevc_mp4toannexb        prores_metadata
chomp                   imx_dump_header         remove_extradata
dca_core                mjpeg2jpeg              setts
dump_extradata          mjpega_dump_header      text2movsub
dv_error_marker         mov2textsub             trace_headers
eac3_core               mp3_header_decompress   truehd_core
extract_extradata       mpeg2_metadata          vp9_metadata
filter_units            mpeg4_unpack_bframes    vp9_raw_reorder
h264_metadata           noise                   vp9_superframe
h264_mp4toannexb        null                    vp9_superframe_split

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 libcdio

Enabled outdevs:
caca                    sdl2
