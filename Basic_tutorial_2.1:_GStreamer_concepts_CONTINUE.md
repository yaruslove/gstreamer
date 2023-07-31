## Understanding matching fitting Gst.Elements

Задача понять по каким параметрам можно сопоставлять (соединять-линковать) Gst.Elements, какие элементы нельзя стыковать междусобой.

Вспомним как в предыдущей задаче мы создали элементы  
###  Create the elements
```
source = Gst.ElementFactory.make("videotestsrc", "source")
filter_vertigo = Gst.ElementFactory.make("vertigotv", "vertigo-filter")
videoconvert = Gst.ElementFactory.make("videoconvert", "video-convert")
sink = Gst.ElementFactory.make("autovideosink", "sink")
``` 


Имя plugin "**videotestsrc**"

Впишем команду terminal command для того чтоб узнать о плагине
```
gst-inspect-1.0 videotestsrc
```

#### Output:
```
Factory Details:
  Rank                     none (0)
  Long-name                Video test source
  Klass                    Source/Video
  Description              Creates a test video stream
  Author                   David A. Schleef <ds@schleef.org>

Plugin Details:
  Name                     videotestsrc
  Description              Creates a test video stream
  Filename                 /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstvideotestsrc.so
  Version                  1.16.2
  License                  LGPL
  Source module            gst-plugins-base
  Source release date      2019-12-03
  Binary package           GStreamer Base Plugins (Ubuntu)
  Origin URL               https://launchpad.net/distros/ubuntu/+source/gst-plugins-base1.0

GObject
 +----GInitiallyUnowned
       +----GstObject
             +----GstElement
                   +----GstBaseSrc
                         +----GstPushSrc
                               +----GstVideoTestSrc

Pad Templates:
  SRC template: 'src'
    Availability: Always
    Capabilities:
      video/x-raw
                 format: { (string)I420, (string)YV12, (string)YUY2, (string)UYVY, (string)AYUV, (string)VUYA, (string)
                 RGBx, (string)BGRx, (string)xRGB, (string)xBGR, (string)RGBA, (string)BGRA, (string)ARGB, (string)ABGR,
                (string)RGB, (string)BGR, (string)Y41B, (string)Y42B, (string)YVYU, (string)Y444, (string)v210, 
                (string)v216, (string)Y210, (string)Y410, (string)NV12, (string)NV21, (string)GRAY8, (string)
                GRAY16_BE, (string)GRAY16_LE, (string)v308, (string)RGB16, (string)BGR16, (string)RGB15, (string)
                BGR15, (string)UYVP, (string)A420, (string)RGB8P, (string)YUV9, (string)YVU9, (string)IYU1, (string)
                ARGB64, (string)AYUV64, (string)r210, (string)I420_10BE, (string)I420_10LE, (string)I422_10BE, (string)
                I422_10LE, (string)Y444_10BE, (string)Y444_10LE, (string)GBR, (string)GBR_10BE, (string)GBR_10LE,
                (string)NV16, (string)NV24, (string)NV12_64Z32, (string)A420_10BE, (string)A420_10LE, (string)
                A422_10BE, (string)A422_10LE, (string)A444_10BE, (string)A444_10LE, (string)NV61, (string)P010_10BE,
                (string)P010_10LE, (string)IYU2, (string)VYUY, (string)GBRA, (string)GBRA_10BE, (string)GBRA_10LE,
                (string)BGR10A2_LE, (string)GBR_12BE, (string)GBR_12LE, (string)GBRA_12BE, (string)GBRA_12LE,
                (string)I420_12BE, (string)I420_12LE, (string)I422_12BE, (string)I422_12LE, (string)Y444_12BE,
                (string)Y444_12LE, (string)GRAY10_LE32, (string)NV12_10LE32, (string)NV16_10LE32, (string)
                NV12_10LE40 }
                  width: [ 1, 2147483647 ]
                 height: [ 1, 2147483647 ]
              framerate: [ 0/1, 2147483647/1 ]
         multiview-mode: { (string)mono, (string)left, (string)right }
      video/x-bayer
                 format: { (string)bggr, (string)rggb, (string)grbg, (string)gbrg }
                  width: [ 1, 2147483647 ]
                 height: [ 1, 2147483647 ]
              framerate: [ 0/1, 2147483647/1 ]
         multiview-mode: { (string)mono, (string)left, (string)right }

Element has no clocking capabilities.
Element has no URI handling capabilities.

Pads:
  SRC: 'src'
    Pad Template: 'src'

```
<br/>  
Подметим что в plugin "videotestsrc" в 'src' (т.е выход) output в форматах (format) есть форматы: (string)RGBx, (string)BGRx   
<br/>  
<br/>  
<br/>  
Посмотрим на другой плагин.
put in terminal another command  

```
gst-inspect-1.0 vertigotv
```  

#### Output:

```
Factory Details:
  Rank                     none (0)
  Long-name                VertigoTV effect
  Klass                    Filter/Effect/Video
  Description              A loopback alpha blending effector with rotating and scaling
  Author                   Wim Taymans <wim.taymans@gmail.be>

Plugin Details:
  Name                     effectv
  Description              effect plugins from the effectv project
  Filename                 /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgsteffectv.so
  Version                  1.16.2
  License                  LGPL
  Source module            gst-plugins-good
  Source release date      2019-12-03
  Binary package           GStreamer Good Plugins (Ubuntu)
  Origin URL               https://launchpad.net/distros/ubuntu/+source/gst-plugins-good1.0

GObject
 +----GInitiallyUnowned
       +----GstObject
             +----GstElement
                   +----GstBaseTransform
                         +----GstVideoFilter
                               +----GstVertigoTV

Pad Templates:
  SINK template: 'sink'
    Availability: Always
    Capabilities:
      video/x-raw
                 format: { (string)RGBx, (string)BGRx }
                  width: [ 1, 2147483647 ]
                 height: [ 1, 2147483647 ]
              framerate: [ 0/1, 2147483647/1 ]

  SRC template: 'src'
    Availability: Always
    Capabilities:
      video/x-raw
                 format: { (string)RGBx, (string)BGRx }
                  width: [ 1, 2147483647 ]
                 height: [ 1, 2147483647 ]
              framerate: [ 0/1, 2147483647/1 ]

Element has no clocking capabilities.
Element has no URI handling capabilities.

Pads:
  SINK: 'sink'
    Pad Template: 'sink'
  SRC: 'src'
    Pad Template: 'src'
```
<br/>  
<br/>  

Подметим что в plugin "vertigotv" в 'src' (т.е выход) output в форматах (format) есть форматы: (string)RGBx, (string)BGRx  
  

Т.к. в  
plugin(videotestsrc)  "src"(выход)=> иммеет формат (string)RGBx, (string)BGRx  
plugin(vertigotv)     =>"src"(вход) иммеет формат (string)RGBx, (string)BGRx  
**ОНИ ОДИНАКОВЫЕ => соотвественно мы имеем право их линковать**
