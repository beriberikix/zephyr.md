---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/api/udc.html
original_path: connectivity/usb/device_next/api/udc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB device controller (UDC) driver API

The USB device controller driver API is described in
[include/zephyr/drivers/usb/udc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/udc.h) and referred to
as the `UDC driver` API.

UDC driver API is experimental and is subject to change without notice.
It is a replacement for [USB device controller driver API](../../device/api/usb_dc.md#usb-dc-api). If you wish to port an existing
driver to UDC driver API, or add a new driver, please use
[drivers/usb/udc/udc\_skeleton.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/udc_skeleton.c) as a starting point.

## API reference

*group* USB device controller driver API
:   New USB device controller (UDC) driver API.

    Functions

    static inline bool udc\_is\_initialized(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Checks whether the controller is initialized.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   true if controller is initialized, false otherwise

    static inline bool udc\_is\_enabled(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Checks whether the controller is enabled.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   true if controller is enabled, false otherwise

    static inline bool udc\_is\_suspended(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Checks whether the controller is suspended.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   true if controller is suspended, false otherwise

    int udc\_init(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, udc\_event\_cb\_t event\_cb)
    :   Initialize USB device controller.

        Initialize USB device controller and control IN/OUT endpoint. After initialization controller driver should be able to detect power state of the bus and signal power state changes.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **event\_cb** – **[in]** Event callback from the higher layer (USB device stack)

        Return values:
        :   - **-EINVAL** – on parameter error (no callback is passed)
            - **-EALREADY** – already initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_enable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable USB device controller.

        Enable powered USB device controller and allow host to recognize and enumerate the device.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   - **-EPERM** – controller is not initialized
            - **-EALREADY** – already enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_disable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable USB device controller.

        Disable enabled USB device controller. The driver should continue to detect power state changes.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – already disabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_shutdown(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Poweroff USB device controller.

        Shut down the controller completely to reduce energy consumption or to change the role of the controller.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline struct udc\_device\_caps udc\_caps(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get USB device controller capabilities.

        Obtain the capabilities of the controller such as full speed (FS), high speed (HS), and more.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   USB device controller capabilities.

    enum udc\_bus\_speed udc\_device\_speed(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get actual USB device speed.

        The function should be called after the reset event to determine the actual bus speed.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   USB device controller capabilities.

    static inline int udc\_set\_address(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t addr)
    :   Set USB device address.

        Set address of enabled USB device.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **addr** – **[in]** USB device address

        Return values:
        :   **-EPERM** – controller is not enabled (or not initialized)

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline int udc\_test\_mode(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t mode, const bool dryrun)
    :   Enable Test Mode.

        For compliance testing, high-speed controllers must support test modes. A particular test is enabled by a SetFeature(TEST\_MODE) request. To disable a test mode, device needs to be power cycled.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **mode** – **[in]** Test mode
            - **dryrun** – **[in]** Verify that a particular mode can be enabled, but do not enable test mode

        Return values:
        :   **-ENOTSUP** – Test mode is not supported

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline int udc\_host\_wakeup(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initiate host wakeup procedure.

        Initiate host wakeup. Only possible when the bus is suspended.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EPERM** – controller is not enabled (or not initialized)

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_try\_config(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep, const uint8\_t attributes, uint16\_t \*const mps, const uint8\_t interval)
    :   Try an endpoint configuration.

        Try an endpoint configuration based on endpoint descriptor. This function may modify wMaxPacketSize descriptor fields of the endpoint. All properties of the descriptor, such as direction, and transfer type, should be set correctly. If wMaxPacketSize value is zero, it will be updated to maximum buffer size of the endpoint.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address (same as bEndpointAddress)
            - **attributes** – **[in]** Endpoint attributes (same as bmAttributes)
            - **mps** – **[in]** Maximum packet size (same as wMaxPacketSize)
            - **interval** – **[in]** Polling interval (same as bInterval)

        Return values:
        :   - **-EINVAL** – on wrong parameter
            - **-ENOTSUP** – endpoint configuration not supported
            - **-ENODEV** – no endpoints available

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_enable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep, const uint8\_t attributes, const uint16\_t mps, const uint8\_t interval)
    :   Configure and enable endpoint.

        Configure and make an endpoint ready for use. Valid for all endpoints except control IN/OUT.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address (same as bEndpointAddress)
            - **attributes** – **[in]** Endpoint attributes (same as bmAttributes)
            - **mps** – **[in]** Maximum packet size (same as wMaxPacketSize)
            - **interval** – **[in]** Polling interval (same as bInterval)

        Return values:
        :   - **-EINVAL** – on wrong parameter (control IN/OUT endpoint)
            - **-EPERM** – controller is not initialized
            - **-ENODEV** – endpoint configuration not found
            - **-EALREADY** – endpoint is already enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_disable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep)
    :   Disable endpoint.

        Valid for all endpoints except control IN/OUT.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address

        Return values:
        :   - **-EINVAL** – on wrong parameter (control IN/OUT endpoint)
            - **-ENODEV** – endpoint configuration not found
            - **-EALREADY** – endpoint is already disabled
            - **-EPERM** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_set\_halt(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep)
    :   Halt endpoint.

        Valid for all endpoints.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address

        Return values:
        :   - **-ENODEV** – endpoint configuration not found
            - **-ENOTSUP** – not supported (e.g. isochronous endpoint)
            - **-EPERM** – controller is not enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_clear\_halt(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep)
    :   Clear endpoint halt.

        Valid for all endpoints.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address

        Return values:
        :   - **-ENODEV** – endpoint configuration not found
            - **-ENOTSUP** – not supported (e.g. isochronous endpoint)
            - **-EPERM** – controller is not enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_enqueue(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Queue USB device controller request.

        Add request to the queue. If the queue is empty, the request buffer can be claimed by the controller immediately.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **buf** – **[in]** Pointer to UDC request buffer

        Return values:
        :   - **-ENODEV** – endpoint configuration not found
            - **-EACCES** – endpoint is not enabled (TBD)
            - **-EBUSY** – request can not be queued
            - **-EPERM** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int udc\_ep\_dequeue(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep)
    :   Remove all USB device controller requests from endpoint queue.

        UDC\_EVT\_EP\_REQUEST event will be generated when the driver releases claimed buffer, no new requests will be claimed, all requests in the queue will passed as chained list of the event variable buf. The endpoint queue is empty after that.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address

        Return values:
        :   - **-ENODEV** – endpoint configuration not found
            - **-EACCES** – endpoint is not disabled
            - **-EPERM** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*udc\_ep\_buf\_alloc(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t ep, const size\_t size)
    :   Allocate UDC request buffer.

        Allocate a new buffer from common request buffer pool.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **ep** – **[in]** Endpoint address
            - **size** – **[in]** Size of the request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    int udc\_ep\_buf\_free(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Free UDC request buffer.

        Put the buffer back into the request buffer pool.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline void udc\_ep\_buf\_set\_zlp(struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Set ZLP flag in requests metadata.

        The controller should send a ZLP at the end of the transfer.

        Parameters:
        :   - **buf** – **[in]** Pointer to UDC request buffer

    static inline struct udc\_buf\_info \*udc\_get\_buf\_info(const struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Get requests metadata.

        Parameters:
        :   - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   pointer to metadata structure.
