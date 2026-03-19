---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/video/tcpserversink/README.html
original_path: samples/drivers/video/tcpserversink/README.html
---

# Video TCP server sink

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/video/tcpserversink/README.rst/..)

## Description

This sample application gets frames from a video capture device and sends
them over the network to the connected TCP client.

## Requirements

This samples requires a video capture device and network support.

- [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk)
- [MT9M114 camera module](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114) [[1]](#id1)

## Wiring

On [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk), The MT9M114 camera module should be plugged in the
J35 camera connector. A USB cable should be connected from a host to the micro
USB debug connector (J41) in order to get console output via the freelink
interface. Ethernet cable must be connected to RJ45 connector.

## Building and Running

For [MIMXRT1064-EVK](../../../../boards/nxp/mimxrt1064_evk/doc/index.md#mimxrt1064_evk), the sample can be built with the following command.
If a mt9m114 camera shield is missing, video software generator will be used instead.

```shell
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 samples/drivers/video/tcpserversink
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

[[1](#id2)]

[https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114)

## See also

[Video Interface](../../../../doxygen/html/group__video__interface.md)

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)
