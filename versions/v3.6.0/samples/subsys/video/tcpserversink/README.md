---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/video/tcpserversink/README.html
original_path: samples/subsys/video/tcpserversink/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Video TCP server sink

## Description

This sample application gets frames from a video capture device and sends
them over the network to the connected TCP client.

## Requirements

This samples requires a video capture device and network support.

- [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)

## Wiring

On [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), The MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink
interface. Ethernet cable must be connected to RJ45 connector.

## Building and Running

For [NXP MIMXRT1064-EVK](../../../../boards/arm/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), build this sample application with the following commands:

```shell
west build -b mimxrt1064_evk samples/subsys/video/tcpserversink
```

### Sample Output

```shell
Video device detected, format: RGBP 640x480
TCP: Waiting for client...
```

Then from a peer on the same network you can connect and grab frames.

Example with gstreamer:

```shell
gst-launch-1.0 tcpclientsrc host=192.0.2.1 port=5000 \
    ! videoparse format=rgb16 width=640 height=480 \
    ! queue \
    ! videoconvert \
    ! fpsdisplaysink sync=false
```

## References
