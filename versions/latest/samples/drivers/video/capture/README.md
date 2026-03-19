---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/video/capture/README.html
original_path: samples/drivers/video/capture/README.html
---

# Video capture

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/video/capture/README.rst/..)

## Description

This sample application uses the [Video](../../../../hardware/peripherals/video.md#video-api) to capture frames from a video capture
device then uses the [Display Interface](../../../../hardware/peripherals/display/index.md#display-api) to display them onto an LCD screen (if any).

## Requirements

This sample needs a video capture device (e.g. a camera) but it is not mandatory.
Supported camera modules on some i.MX RT boards can be found below.

- [Camera iMXRT](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183) [[1]](#id1)
- [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114) [[2]](#id3)
- [MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170_evk)
- [OV5640 camera module](https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640_datasheet.pdf) [[3]](#id5)

Also [Arduino Nicla Vision](../../../../boards/arduino/nicla_vision/doc/index.md#arduino-nicla-vision-board) can be used in this sample as capture device, in that case
The user can transfer the captured frames through on board USB.

## Wiring

On [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk), the MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink interface.

On [MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170_evk), the OV5640 camera module should be plugged into the
J2 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J11) in order to get console output via the daplink interface.

For [Arduino Nicla Vision](../../../../boards/arduino/nicla_vision/doc/index.md#arduino-nicla-vision-board) there is no extra wiring required.

## Building and Running

For [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk), build this sample application with the following commands:

```shell
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 --shield rk043fn66hs_ctg samples/drivers/video/capture
```

For [MIMXRT1170-EVK/EVKB](../../../../boards/nxp/mimxrt1170_evk/doc/index.md#mimxrt1170_evk), build this sample application with the following commands:

```shell
west build -b mimxrt1170_evk/mimxrt1176/cm7 --shield nxp_btb44_ov5640 --shield rk055hdmipi4ma0 samples/drivers/video/capture
```

For [Arduino Nicla Vision](../../../../boards/arduino/nicla_vision/doc/index.md#arduino-nicla-vision-board), build this sample application with the following commands:

```shell
west build -b arduino_nicla_vision/stm32h747xx/m7 samples/drivers/video/capture
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

[[1](#id2)]

[https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Connecting-camera-and-LCD-to-i-MX-RT-EVKs/ta-p/1122183)

[[2](#id4)]

[https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)

[[3](#id6)]

[https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640\_datasheet.pdf](https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640_datasheet.pdf)

## See also

[Video Interface](../../../../doxygen/html/group__video__interface.md)
