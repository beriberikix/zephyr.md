---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/video/capture/README.html
original_path: samples/subsys/video/capture/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Video capture

## Description

This sample application uses the [Video API](../../../../hardware/peripherals/video.md#video-api) to retrieve video frames from the
video capture device, writes a frame count message to the console, and then
discards the video frame data.

## Requirements

This sample requires a video capture device (e.g. a camera).

- [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)

## Wiring

On [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), The MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink
interface.

## Building and Running

For [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), build this sample application with the following commands:

```shell
west build -b mimxrt1064_evk samples/subsys/video/capture
```

### Sample Output

```shell
 Found video device: CSI
 width (640,640), height (480,480)
 Supported pixelformats (fourcc):
  - RGBP
 Use default format (640x480)
 Capture started
 Got frame 743! size: 614400; timestamp 100740 ms
 Got frame 744! size: 614400; timestamp 100875 ms
 Got frame 745! size: 614400; timestamp 101010 ms
 Got frame 746! size: 614400; timestamp 101146 ms
 Got frame 747! size: 614400; timestamp 101281 ms
 Got frame 748! size: 614400; timestamp 101416 ms

<repeats endlessly>
```

## References
