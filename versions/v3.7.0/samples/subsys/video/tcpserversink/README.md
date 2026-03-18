---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/video/tcpserversink/README.html
original_path: samples/subsys/video/tcpserversink/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Video TCP server sink

## Description

This sample application gets frames from a video capture device and sends
them over the network to the connected TCP client.

## Requirements

This samples requires a video capture device and network support.

- [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)

## Wiring

On [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), The MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink
interface. Ethernet cable must be connected to RJ45 connector.

## Building and Running

For [NXP MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064-evk), the sample can be built with the following command.
If a mt9m114 camera shield is missing, video software generator will be used instead.

```shell
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 samples/subsys/video/tcpserversink
```

### Sample Output

```shell
Video device detected, format: RGBP 480x272
TCP: Waiting for client...
```

Then from a peer on the same network you can connect and grab frames.

Example with gstreamer:

```shell
gst-launch-1.0 tcpclientsrc host=192.0.2.1 port=5000 \
    ! videoparse format=rgb16 width=480 height=272 \
    ! queue \
    ! videoconvert \
    ! fpsdisplaysink sync=false
```

For video software generator, the default resolution should be width=320 and height=160.

## References
