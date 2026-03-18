---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/video/capture/README.html
original_path: samples/subsys/video/capture/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Video capture

## Description

This sample application uses the [Video](../../../../hardware/peripherals/video.md#video-api) to capture frames from a video capture
device then uses the [Display Interface](../../../../hardware/peripherals/display/index.md#display-api) to display them onto an LCD screen (if any).

## Requirements

This sample needs a video capture device (e.g. a camera) but it is not mandatory.
Supported camera modules on some i.MX RT boards can be found below.

- [Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)
- [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)
- [NXP MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170-evk)
- [OV5640 camera module](https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640_datasheet.pdf)

## Wiring

On [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), the MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink interface.

On [NXP MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170-evk), the OV5640 camera module should be plugged into the
J2 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J11) in order to get console output via the daplink interface.

## Building and Running

For [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), build this sample application with the following commands:

```shell
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 --shield rk043fn66hs_ctg samples/subsys/video/capture
```

For [NXP MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170-evk), build this sample application with the following commands:

```shell
west build -b mimxrt1170_evk/mimxrt1176/cm7 --shield nxp_btb44_ov5640 --shield rk055hdmipi4ma0 samples/subsys/video/capture
```

For testing purpose without the need of any real video capture and/or display hardwares,
a video software pattern generator is supported by the above build commands without
specifying the shields.

### Sample Output

```shell
 Video device: csi@402bc000
 - Capabilities:
   RGBP width [480; 480; 0] height [272; 272; 0]
   YUYV width [480; 480; 0] height [272; 272; 0]
   RGBP width [640; 640; 0] height [480; 480; 0]
   YUYV width [640; 640; 0] height [480; 480; 0]
   RGBP width [1280; 1280; 0] height [720; 720; 0]
   YUYV width [1280; 1280; 0] height [720; 720; 0]
 - Default format: RGBP 480x272

 Display device: display-controller@402b8000
 - Capabilities:
   x_resolution = 480, y_resolution = 272, supported_pixel_formats = 40
   current_pixel_format = 32, current_orientation = 0

 Capture started
 Got frame 0! size: 261120; timestamp 249 ms
 Got frame 1! size: 261120; timestamp 282 ms
 Got frame 2! size: 261120; timestamp 316 ms
 Got frame 3! size: 261120; timestamp 350 ms
 Got frame 4! size: 261120; timestamp 384 ms
 Got frame 5! size: 261120; timestamp 418 ms
 Got frame 6! size: 261120; timestamp 451 ms

<repeats endlessly>
```

## References
