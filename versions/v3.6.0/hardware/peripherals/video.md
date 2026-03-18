---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/video.html
original_path: hardware/peripherals/video.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

Related code samples

[Video TCP server sink](../../samples/subsys/video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")
:   Capture video frames and send them over the network to a TCP client.

[Video capture](../../samples/subsys/video/capture/README.md#video-capture "Use the video API to retrieve video frames from a capture device.")
:   Use the video API to retrieve video frames from a capture device.

*group* video\_interface
:   Video Interface.

    Defines

    video\_fourcc(a, b, c, d)

    Typedefs

    typedef int (\*video\_api\_set\_format\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_format](#c.video_format) \*fmt)
    :   Set video format.

        See [video\_set\_format()](#group__video__interface_1gae38df95199e41ac197b9754824b2bd29) for argument descriptions.

    typedef int (\*video\_api\_get\_format\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_format](#c.video_format) \*fmt)
    :   Get current video format.

        See [video\_get\_format()](#group__video__interface_1gac0964bd0b57c6be5e773a21af0438edc) for argument descriptions.

    typedef int (\*video\_api\_enqueue\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_buffer](#c.video_buffer) \*buf)
    :   Enqueue a buffer in the driver’s incoming queue.

        See [video\_enqueue()](#group__video__interface_1gac19d14a5875d48c96bd66a8bb65e8a51) for argument descriptions.

    typedef int (\*video\_api\_dequeue\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_buffer](#c.video_buffer) \*\*buf, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Dequeue a buffer from the driver’s outgoing queue.

        See [video\_dequeue()](#group__video__interface_1ga9862024c9b07855609ea2078680c9afd) for argument descriptions.

    typedef int (\*video\_api\_flush\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, bool cancel)
    :   Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

        See [video\_flush()](#group__video__interface_1gae5e6256ab799ca1cbbac4987b82bb145) for argument descriptions.

    typedef int (\*video\_api\_stream\_start\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start the capture or output process.

        See [video\_stream\_start()](#group__video__interface_1ga7145a18ad5e3e5d74398c89c00ea19f0) for argument descriptions.

    typedef int (\*video\_api\_stream\_stop\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Stop the capture or output process.

        See [video\_stream\_stop()](#group__video__interface_1ga6464dede55777c9082e85d6af43a4d48) for argument descriptions.

    typedef int (\*video\_api\_set\_ctrl\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int cid, void \*value)
    :   Set a video control value.

        See [video\_set\_ctrl()](#group__video__interface_1ga87873a4612cfbd2cb62595dec15cb77e) for argument descriptions.

    typedef int (\*video\_api\_get\_ctrl\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int cid, void \*value)
    :   Get a video control value.

        See [video\_get\_ctrl()](#group__video__interface_1ga664122e82da802f1dff8b5c30e158acd) for argument descriptions.

    typedef int (\*video\_api\_get\_caps\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_caps](#c.video_caps) \*caps)
    :   Get capabilities of a video endpoint.

        See [video\_get\_caps()](#group__video__interface_1ga4d5237607c858708380955705a2023bd) for argument descriptions.

    typedef int (\*video\_api\_set\_signal\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*signal)
    :   Register/Unregister poll signal for buffer events.

        See [video\_set\_signal()](#group__video__interface_1gab38a9f956f5d5452fc6e0c0f1bf382be) for argument descriptions.

    Enums

    enum video\_endpoint\_id
    :   [video\_endpoint\_id](#group__video__interface_1gafa3d076a1324ea54b5c5ec7806cb2ef9) enum

        Identify the video device endpoint.

        *Values:*

        enumerator VIDEO\_EP\_NONE

        enumerator VIDEO\_EP\_ANY

        enumerator VIDEO\_EP\_IN

        enumerator VIDEO\_EP\_OUT

    enum video\_signal\_result
    :   video\_event enum

        Identify video event.

        *Values:*

        enumerator VIDEO\_BUF\_DONE

        enumerator VIDEO\_BUF\_ABORTED

        enumerator VIDEO\_BUF\_ERROR

    Functions

    static inline int video\_set\_format(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_format](#c.video_format) \*fmt)
    :   Set video format.

        Configure video device with a specific format.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **fmt** – Pointer to a video format struct.

        Return values:
        :   - **0** – Is successful.
            - **-EINVAL** – If parameters are invalid.
            - **-ENOTSUP** – If format is not supported.
            - **-EIO** – General input / output error.

    static inline int video\_get\_format(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_format](#c.video_format) \*fmt)
    :   Get video format.

        Get video device current video format.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **fmt** – Pointer to video format struct.

        Return values:
        :   **pointer** – to video format

    static inline int video\_enqueue(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_buffer](#c.video_buffer) \*buf)
    :   Enqueue a video buffer.

        Enqueue an empty (capturing) or filled (output) video buffer in the driver’s endpoint incoming queue.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **buf** – Pointer to the video buffer.

        Return values:
        :   - **0** – Is successful.
            - **-EINVAL** – If parameters are invalid.
            - **-EIO** – General input / output error.

    static inline int video\_dequeue(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_buffer](#c.video_buffer) \*\*buf, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Dequeue a video buffer.

        Dequeue a filled (capturing) or displayed (output) buffer from the driver’s endpoint outgoing queue.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **buf** – Pointer a video buffer pointer.
            - **timeout** – Timeout

        Return values:
        :   - **0** – Is successful.
            - **-EINVAL** – If parameters are invalid.
            - **-EIO** – General input / output error.

    static inline int video\_flush(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, bool cancel)
    :   Flush endpoint buffers.

        A call to flush finishes when all endpoint buffers have been moved from incoming queue to outgoing queue. Either because canceled or fully processed through the video function.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **cancel** – If true, cancel buffer processing instead of waiting for completion.

        Return values:
        :   **0** – Is successful, -ERRNO code otherwise.

    static inline int video\_stream\_start(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start the video device function.

        video\_stream\_start is called to enter ‘streaming’ state (capture, output…). The driver may receive buffers with [video\_enqueue()](#group__video__interface_1gac19d14a5875d48c96bd66a8bb65e8a51) before video\_stream\_start is called. If driver/device needs a minimum number of buffers before being able to start streaming, then driver set the min\_vbuf\_count to the related endpoint capabilities.

        Return values:
        :   - **0** – Is successful.
            - **-EIO** – General input / output error.

    static inline int video\_stream\_stop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Stop the video device function.

        On video\_stream\_stop, driver must stop any transactions or wait until they finish.

        Return values:
        :   - **0** – Is successful.
            - **-EIO** – General input / output error.

    static inline int video\_get\_caps(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [video\_caps](#c.video_caps) \*caps)
    :   Get the capabilities of a video endpoint.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **caps** – Pointer to the [video\_caps](#structvideo__caps) struct to fill.

        Return values:
        :   **0** – Is successful, -ERRNO code otherwise.

    static inline int video\_set\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int cid, void \*value)
    :   Set the value of a control.

        This set the value of a video control, value type depends on control ID, and must be interpreted accordingly.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cid** – Control ID.
            - **value** – Pointer to the control value.

        Return values:
        :   - **0** – Is successful.
            - **-EINVAL** – If parameters are invalid.
            - **-ENOTSUP** – If format is not supported.
            - **-EIO** – General input / output error.

    static inline int video\_get\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int cid, void \*value)
    :   Get the current value of a control.

        This retrieve the value of a video control, value type depends on control ID, and must be interpreted accordingly.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cid** – Control ID.
            - **value** – Pointer to the control value.

        Return values:
        :   - **0** – Is successful.
            - **-EINVAL** – If parameters are invalid.
            - **-ENOTSUP** – If format is not supported.
            - **-EIO** – General input / output error.

    static inline int video\_set\_signal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [video\_endpoint\_id](#c.video_endpoint_id) ep, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*signal)
    :   Register/Unregister k\_poll signal for a video endpoint.

        Register a poll signal to the endpoint, which will be signaled on frame completion (done, aborted, error). Registering a NULL poll signal unregisters any previously registered signal.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ep** – Endpoint ID.
            - **signal** – Pointer to [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal)

        Return values:
        :   **0** – Is successful, -ERRNO code otherwise.

    struct [video\_buffer](#c.video_buffer) \*video\_buffer\_alloc(size\_t size)
    :   Allocate video buffer.

        Parameters:
        :   - **size** – Size of the video buffer.

        Return values:
        :   **pointer** – to allocated video buffer

    void video\_buffer\_release(struct [video\_buffer](#c.video_buffer) \*buf)
    :   Release a video buffer.

        Parameters:
        :   - **buf** – Pointer to the video buffer to release.

    struct video\_format
    :   *#include <video.h>*

        Video format structure.

        Used to configure frame format.

        Public Members

        uint32\_t pixelformat
        :   FourCC pixel format value (Video pixel formats).

        uint32\_t width
        :   frame width in pixels.

        uint32\_t height
        :   frame height in pixels.

        uint32\_t pitch
        :   line stride.

            This is the number of bytes that needs to be added to the address in the first pixel of a row in order to go to the address of the first pixel of the next row (>=width).

    struct video\_format\_cap
    :   *#include <video.h>*

        Video format capability.

        Used to describe a video endpoint format capability.

        Public Members

        uint32\_t pixelformat
        :   FourCC pixel format value (Video pixel formats).

        uint32\_t width\_min
        :   minimum supported frame width in pixels.

        uint32\_t width\_max
        :   maximum supported frame width in pixels.

        uint32\_t height\_min
        :   minimum supported frame height in pixels.

        uint32\_t height\_max
        :   maximum supported frame height in pixels.

        uint16\_t width\_step
        :   width step size in pixels.

        uint16\_t height\_step
        :   height step size in pixels.

    struct video\_caps
    :   *#include <video.h>*

        Video format capabilities.

        Used to describe video endpoint capabilities.

        Public Members

        const struct [video\_format\_cap](#c.video_format_cap) \*format\_caps
        :   list of video format capabilities (zero terminated).

        uint8\_t min\_vbuf\_count
        :   minimal count of video buffers to enqueue before being able to start the stream.

    struct video\_buffer
    :   *#include <video.h>*

        Video buffer structure.

        Represent a video frame.

        Public Members

        void \*driver\_data
        :   pointer to driver specific data.

        uint8\_t \*buffer
        :   pointer to the start of the buffer.

        uint32\_t size
        :   size of the buffer in bytes.

        uint32\_t bytesused
        :   number of bytes occupied by the valid data in the buffer.

        uint32\_t timestamp
        :   time reference in milliseconds at which the last data byte was actually received for input endpoints or to be consumed for output endpoints.

    struct video\_driver\_api
    :   *#include <video.h>*

*group* video\_controls
:   Video controls.

    Control classes

    VIDEO\_CTRL\_CLASS\_GENERIC
    :   Generic class controls.

    VIDEO\_CTRL\_CLASS\_CAMERA
    :   Camera class controls.

    VIDEO\_CTRL\_CLASS\_MPEG
    :   MPEG-compression controls.

    VIDEO\_CTRL\_CLASS\_JPEG
    :   JPEG-compression controls.

    VIDEO\_CTRL\_CLASS\_VENDOR
    :   Vendor-specific class controls.

    Generic class control IDs

    VIDEO\_CID\_HFLIP
    :   Mirror the picture horizontally.

    VIDEO\_CID\_VFLIP
    :   Mirror the picture vertically.

    Camera class control IDs

    VIDEO\_CID\_CAMERA\_EXPOSURE

    VIDEO\_CID\_CAMERA\_GAIN

    VIDEO\_CID\_CAMERA\_ZOOM

    VIDEO\_CID\_CAMERA\_BRIGHTNESS

    VIDEO\_CID\_CAMERA\_SATURATION

    VIDEO\_CID\_CAMERA\_WHITE\_BAL

    VIDEO\_CID\_CAMERA\_CONTRAST

    VIDEO\_CID\_CAMERA\_COLORBAR

    VIDEO\_CID\_CAMERA\_QUALITY
