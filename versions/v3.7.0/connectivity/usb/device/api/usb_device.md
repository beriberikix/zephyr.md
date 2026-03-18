---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device/api/usb_device.html
original_path: connectivity/usb/device/api/usb_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB device stack API

## API reference

There are two ways to transmit data, using the ‘low’ level read/write API or
the ‘high’ level transfer API.

Low level API
:   To transmit data to the host, the class driver should call usb\_write().
    Upon completion the registered endpoint callback will be called. Before
    sending another packet the class driver should wait for the completion of
    the previous write. When data is received, the registered endpoint callback
    is called. usb\_read() should be used for retrieving the received data.
    For CDC ACM sample driver this happens via the OUT bulk endpoint handler
    (cdc\_acm\_bulk\_out) mentioned in the endpoint array (cdc\_acm\_ep\_data).

High level API
:   The usb\_transfer method can be used to transfer data to/from the host. The
    transfer API will automatically split the data transmission into one or more
    USB transaction(s), depending endpoint max packet size. The class driver does
    not have to implement endpoint callback and should set this callback to the
    generic usb\_transfer\_ep\_callback.

Related code samples

[802.15.4 USB](../../../../samples/net/wpanusb/README.md#wpan-usb "Implement a device that exposes an IEEE 802.15.4 radio over USB.")
:   Implement a device that exposes an IEEE 802.15.4 radio over USB.

[Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
:   Output "Hello World!" to the console over USB CDC ACM.

[USB Audio headset](../../../../samples/subsys/usb/audio/headset/README.md#usb-audio-headset "Implement a USB Audio headset device with audio IN/OUT loopback.")
:   Implement a USB Audio headset device with audio IN/OUT loopback.

[USB Audio microphone & headphones](../../../../samples/subsys/usb/audio/headphones_microphone/README.md#usb-audio-headphones-microphone "Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.")
:   Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.

[USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")
:   Use USB CDC-ACM driver to implement a serial port echo.

[USB CDC-ACM composite](../../../../samples/subsys/usb/cdc_acm_composite/README.md#usb-cdc-acm-composite "Implement a composite USB device exposing two serial ports using USB CDC-ACM driver.")
:   Implement a composite USB device exposing two serial ports using USB CDC-ACM driver.

[USB DFU (Device Firmware Upgrade)](../../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.")
:   Implement device firmware upgrade using the USB DFU class driver.

[USB HID (Human Interface Device)](../../../../samples/subsys/usb/hid/README.md#usb-hid "Use USB HID driver to enumerate as a raw HID device.")
:   Use USB HID driver to enumerate as a raw HID device.

[USB HID mouse](../../../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")
:   Implement a basic HID mouse device.

[USB Mass Storage](../../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
:   Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.

[USB testing application](../../../../samples/subsys/usb/testusb/README.md#testusb-app "Test USB device drivers using a loopback function.")
:   Test USB device drivers using a loopback function.

[WebUSB](../../../../samples/subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.")
:   Receive and echo data from a web page using WebUSB API.

*group* USB Device Core API
:   USB Device Core Layer API.

    Defines

    USB\_TRANS\_READ

    USB\_TRANS\_WRITE

    USB\_TRANS\_NO\_ZLP

    USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP
    :   Helper macro to place the BOS compatibility descriptor in the right memory section.

    Typedefs

    typedef void (\*usb\_ep\_callback)(uint8\_t ep, enum [usb\_dc\_ep\_cb\_status\_code](usb_dc.md#c.usb_dc_ep_cb_status_code "usb_dc_ep_cb_status_code") cb\_status)
    :   Callback function signature for the USB Endpoint status.

    typedef int (\*usb\_request\_handler)(struct usb\_setup\_packet \*setup, int32\_t \*transfer\_len, uint8\_t \*\*payload\_data)
    :   Callback function signature for class specific requests.

        Function which handles Class specific requests corresponding to an interface number specified in the device descriptor table. For host to device direction the ‘len’ and ‘payload\_data’ contain the length of the received data and the pointer to the received data respectively. For device to host class requests, ‘len’ and ‘payload\_data’ should be set by the callback function with the length and the address of the data to be transmitted buffer respectively.

    typedef void (\*usb\_interface\_config)(struct usb\_desc\_header \*head, uint8\_t bInterfaceNumber)
    :   Function for interface runtime configuration.

    typedef void (\*usb\_transfer\_callback)(uint8\_t ep, int tsize, void \*priv)
    :   Callback function signature for transfer completion.

    Functions

    int usb\_set\_config(const uint8\_t \*usb\_descriptor)
    :   Configure USB controller.

        Function to configure USB controller. Configuration parameters must be valid or an error is returned

        Parameters:
        :   - **usb\_descriptor** – **[in]** USB descriptor table

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_deconfig(void)
    :   Deconfigure USB controller.

        This function returns the USB device to it’s initial state

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_enable([usb\_dc\_status\_callback](usb_dc.md#c.usb_dc_status_callback "usb_dc_status_callback") status\_cb)
    :   Enable the USB subsystem and associated hardware.

        This function initializes the USB core subsystem and enables the corresponding hardware so that it can begin transmitting and receiving on the USB bus, as well as generating interrupts.

        Class-specific initialization and registration must be performed by the user before invoking this, so that any data or events on the bus are processed correctly by the associated class handling code.

        Parameters:
        :   - **status\_cb** – **[in]** Callback registered by user to notify about USB device controller state.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_disable(void)
    :   Disable the USB device.

        Function to disable the USB device. Upon success, the specified USB interface is clock gated in hardware, it is no longer capable of generating interrupts.

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_write(uint8\_t ep, const uint8\_t \*data, uint32\_t data\_len, uint32\_t \*bytes\_ret)
    :   Write data to the specified endpoint.

        Function to write data to the specified endpoint. The supplied [usb\_ep\_callback](#group____usb__device__core__api_1ga9a45db26a9be295640ed122533427725) will be called when transmission is done.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data to write
            - **data\_len** – **[in]** Length of data requested to write. This may be zero for a zero length status packet.
            - **bytes\_ret** – **[out]** Bytes written to the EP FIFO. This value may be NULL if the application expects all bytes to be written

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_read(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*ret\_bytes)
    :   Read data from the specified endpoint.

        This function is called by the Endpoint handler function, after an OUT interrupt has been received for that EP. The application must only call this function through the supplied [usb\_ep\_callback](#group____usb__device__core__api_1ga9a45db26a9be295640ed122533427725) function.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data buffer to write to
            - **max\_data\_len** – **[in]** Max length of data to read
            - **ret\_bytes** – **[out]** Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read is returned.

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_ep\_set\_stall(uint8\_t ep)
    :   Set STALL condition on the specified endpoint.

        This function is called by USB device class handler code to set stall condition on endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_ep\_clear\_stall(uint8\_t ep)
    :   Clears STALL condition on the specified endpoint.

        This function is called by USB device class handler code to clear stall condition on endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail

    int usb\_ep\_read\_wait(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*read\_bytes)
    :   Read data from the specified endpoint.

        This is similar to usb\_ep\_read, the difference being that, it doesn’t clear the endpoint NAKs so that the consumer is not bogged down by further upcalls till he is done with the processing of the data. The caller should reactivate ep by invoking [usb\_ep\_read\_continue()](#group____usb__device__core__api_1gaab17b8c523ac211ff308c8dc774ba092) do so.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** pointer to data buffer to write to
            - **max\_data\_len** – **[in]** max length of data to read
            - **read\_bytes** – **[out]** Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_ep\_read\_continue(uint8\_t ep)
    :   Continue reading data from the endpoint.

        Clear the endpoint NAK and enable the endpoint to accept more data from the host. Usually called after [usb\_ep\_read\_wait()](#group____usb__device__core__api_1ga4c919f7e993f80150bdde2d7fab254ee) when the consumer is fine to accept more data. Thus these calls together acts as flow control mechanism.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    void usb\_transfer\_ep\_callback(uint8\_t ep, enum [usb\_dc\_ep\_cb\_status\_code](usb_dc.md#c.usb_dc_ep_cb_status_code "usb_dc_ep_cb_status_code"))
    :   Transfer management endpoint callback.

        If a USB class driver wants to use high-level transfer functions, driver needs to register this callback as usb endpoint callback.

    int usb\_transfer(uint8\_t ep, uint8\_t \*data, size\_t dlen, unsigned int flags, [usb\_transfer\_callback](#c.usb_transfer_callback) cb, void \*priv)
    :   Start a transfer.

        Start a usb transfer to/from the data buffer. This function is asynchronous and can be executed in IRQ context. The provided callback will be called on transfer completion (or error) in thread context.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data buffer to write-to/read-from
            - **dlen** – **[in]** Size of data buffer
            - **flags** – Transfer flags (USB\_TRANS\_READ, USB\_TRANS\_WRITE…)
            - **cb** – **[in]** Function called on transfer completion/failure
            - **priv** – **[in]** Data passed back to the transfer completion callback

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_transfer\_sync(uint8\_t ep, uint8\_t \*data, size\_t dlen, unsigned int flags)
    :   Start a transfer and block-wait for completion.

        Synchronous version of usb\_transfer, wait for transfer completion before returning. A return value of zero can also mean that transfer was cancelled or that the endpoint is not ready. This is due to the design of transfers and usb\_dc API.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data buffer to write-to/read-from
            - **dlen** – **[in]** Size of data buffer
            - **flags** – Transfer flags

        Returns:
        :   number of bytes transferred on success, negative errno code on fail.

    void usb\_cancel\_transfer(uint8\_t ep)
    :   Cancel any ongoing transfer on the specified endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

    void usb\_cancel\_transfers(void)
    :   Cancel all ongoing transfers.

    bool usb\_transfer\_is\_busy(uint8\_t ep)
    :   Check that transfer is ongoing for the endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   true if transfer is ongoing, false otherwise.

    int usb\_wakeup\_request(void)
    :   Start the USB remote wakeup procedure.

        Function to request a remote wakeup. This feature must be enabled in configuration, otherwise it will always return -ENOTSUP error.

        Returns:
        :   0 on success, negative errno code on fail, i.e. when the bus is already active.

    bool usb\_get\_remote\_wakeup\_status(void)
    :   Get status of the USB remote wakeup feature.

        Returns:
        :   true if remote wakeup has been enabled by the host, false otherwise.

    void usb\_bos\_register\_cap(void \*hdr)
    :   Register BOS capability descriptor.

        This function should be used by the application to register BOS capability descriptors before the USB device stack is enabled.

        Parameters:
        :   - **hdr** – **[in]** Pointer to BOS capability descriptor

    struct usb\_ep\_cfg\_data
    :   *#include <usb\_device.h>*

        USB Endpoint Configuration.

        This structure contains configuration for the endpoint.

        Public Members

        [usb\_ep\_callback](#c.usb_ep_callback) ep\_cb
        :   Callback function for notification of data received and available to application or transmit done, NULL if callback not required by application code.

        uint8\_t ep\_addr
        :   The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>.

    struct usb\_interface\_cfg\_data
    :   *#include <usb\_device.h>*

        USB Interface Configuration.

        This structure contains USB interface configuration.

        Public Members

        [usb\_request\_handler](#c.usb_request_handler) class\_handler
        :   Handler for USB Class specific Control (EP 0) communications.

        [usb\_request\_handler](#c.usb_request_handler) vendor\_handler
        :   Handler for USB Vendor specific commands.

        [usb\_request\_handler](#c.usb_request_handler) custom\_handler
        :   The custom request handler gets a first chance at handling the request before it is handed over to the ‘chapter 9’ request handler.

            return 0 on success, -EINVAL if the request has not been handled by the custom handler and instead needs to be handled by the core USB stack. Any other error code to denote failure within the custom handler.

    struct usb\_cfg\_data
    :   *#include <usb\_device.h>*

        USB device configuration.

        The Application instantiates this with given parameters added using the “usb\_set\_config” function. Once this function is called changes to this structure will result in undefined behavior. This structure may only be updated after calls to usb\_deconfig

        Public Members

        const uint8\_t \*usb\_device\_description
        :   USB device description, see [http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors](http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors).

        void \*interface\_descriptor
        :   Pointer to interface descriptor.

        [usb\_interface\_config](#c.usb_interface_config) interface\_config
        :   Function for interface runtime configuration.

        void (\*cb\_usb\_status)(struct [usb\_cfg\_data](#c.usb_cfg_data) \*cfg, enum [usb\_dc\_status\_code](usb_dc.md#c.usb_dc_status_code "usb_dc_status_code") cb\_status, const uint8\_t \*param)
        :   Callback to be notified on USB connection status change.

        struct [usb\_interface\_cfg\_data](#c.usb_interface_cfg_data) interface
        :   USB interface (Class) handler and storage space.

        uint8\_t num\_endpoints
        :   Number of individual endpoints in the device configuration.

        struct [usb\_ep\_cfg\_data](#c.usb_ep_cfg_data) \*endpoint
        :   Pointer to an array of endpoint structs of length equal to the number of EP associated with the device description, not including control endpoints.
