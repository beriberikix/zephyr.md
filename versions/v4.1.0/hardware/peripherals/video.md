---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/video.html
original_path: hardware/peripherals/video.html
---

# Video

The video driver API offers a generic interface to video devices.

## Basic Operation

### Video Device

A video device is the abstraction of a hardware or software video function,
which can produce, process, consume or transform video data. The video API is
designed to offer flexible way to create, handle and combine various video
devices.

### Endpoint

Each video device can have one or more endpoints. Output endpoints configure
video output function and generate data. Input endpoints configure video input
function and consume data.

### Video Buffer

A video buffer provides the transport mechanism for the data. There is no
particular requirement on the content. The requirement for the content is
defined by the endpoint format. A video buffer can be queued to a device
endpoint for filling (input ep) or consuming (output ep) operation, once
the operation is achieved, buffer can be dequeued for post-processing,
release or reuse.

### Controls

A video control is accessed and identified by a CID (control identifier). It
represents a video control property. Different devices will have different
controls available which can be generic, related to a device class or vendor
specific. The set/get control functions provide a generic scalable interface
to handle and create controls.

## Configuration Options

Related configuration options:

- [`CONFIG_VIDEO`](../../kconfig.md#CONFIG_VIDEO "CONFIG_VIDEO")

## API Reference

[Video Interface](../../doxygen/html/group__video__interface.md)

Related code samples

- [Video capture](../../samples/drivers/video/capture/README.md#video-capture "Use the video API to retrieve video frames from a capture device.")Use the video API to retrieve video frames from a capture device.
- [Video capture to LVGL](../../samples/drivers/video/capture_to_lvgl/README.md#video-capture-to-lvgl "Capture video frames and display them on an LCD using LVGL.")Capture video frames and display them on an LCD using LVGL.
- [Video TCP server sink](../../samples/drivers/video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")Capture video frames and send them over the network to a TCP client.

[Video Controls](../../doxygen/html/group__video__controls.md)
