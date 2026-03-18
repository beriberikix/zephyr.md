---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/device/api/usb_dc.html
original_path: connectivity/usb/device/api/usb_dc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# USB device controller driver API

The USB device controller driver API is described in
[include/zephyr/drivers/usb/usb\_dc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/usb_dc.h) and sometimes referred to
as the `usb_dc` API.

This API has some limitations by design, it does not follow [Device Driver Model](../../../../kernel/drivers/index.md#device-model-api)
and is being replaced by a new UDC driver API.

## API reference

*group* \_usb\_device\_controller\_api
:   USB Device Controller API.

    Typedefs

    typedef void (\*usb\_dc\_ep\_callback)(uint8\_t ep, enum [usb\_dc\_ep\_cb\_status\_code](#c.usb_dc_ep_cb_status_code) cb\_status)
    :   Callback function signature for the USB Endpoint status.

    typedef void (\*usb\_dc\_status\_callback)(enum [usb\_dc\_status\_code](#c.usb_dc_status_code) cb\_status, const uint8\_t \*param)
    :   Callback function signature for the device.

    Enums

    enum usb\_dc\_status\_code
    :   USB Driver Status Codes.

        Status codes reported by the registered device status callback.

        *Values:*

        enumerator USB\_DC\_ERROR
        :   USB error reported by the controller.

        enumerator USB\_DC\_RESET
        :   USB reset.

        enumerator USB\_DC\_CONNECTED
        :   USB connection established, hardware enumeration is completed.

        enumerator USB\_DC\_CONFIGURED
        :   USB configuration done.

        enumerator USB\_DC\_DISCONNECTED
        :   USB connection lost.

        enumerator USB\_DC\_SUSPEND
        :   USB connection suspended by the HOST.

        enumerator USB\_DC\_RESUME
        :   USB connection resumed by the HOST.

        enumerator USB\_DC\_INTERFACE
        :   USB interface selected.

        enumerator USB\_DC\_SET\_HALT
        :   Set Feature ENDPOINT\_HALT received.

        enumerator USB\_DC\_CLEAR\_HALT
        :   Clear Feature ENDPOINT\_HALT received.

        enumerator USB\_DC\_SOF
        :   Start of Frame received.

        enumerator USB\_DC\_UNKNOWN
        :   Initial USB connection status.

    enum usb\_dc\_ep\_cb\_status\_code
    :   USB Endpoint Callback Status Codes.

        Status Codes reported by the registered endpoint callback.

        *Values:*

        enumerator USB\_DC\_EP\_SETUP
        :   SETUP received.

        enumerator USB\_DC\_EP\_DATA\_OUT
        :   Out transaction on this EP, data is available for read.

        enumerator USB\_DC\_EP\_DATA\_IN
        :   In transaction done on this EP.

    enum usb\_dc\_ep\_transfer\_type
    :   USB Endpoint Transfer Type.

        *Values:*

        enumerator USB\_DC\_EP\_CONTROL = 0
        :   Control type endpoint.

        enumerator USB\_DC\_EP\_ISOCHRONOUS
        :   Isochronous type endpoint.

        enumerator USB\_DC\_EP\_BULK
        :   Bulk type endpoint.

        enumerator USB\_DC\_EP\_INTERRUPT
        :   Interrupt type endpoint.

    enum usb\_dc\_ep\_synchronozation\_type
    :   USB Endpoint Synchronization Type.

        Note

        Valid only for Isochronous Endpoints

        *Values:*

        enumerator USB\_DC\_EP\_NO\_SYNCHRONIZATION = (0U << 2U)
        :   No Synchronization.

        enumerator USB\_DC\_EP\_ASYNCHRONOUS = (1U << 2U)
        :   Asynchronous.

        enumerator USB\_DC\_EP\_ADAPTIVE = (2U << 2U)
        :   Adaptive.

        enumerator USB\_DC\_EP\_SYNCHRONOUS = (3U << 2U)
        :   Synchronous.

    Functions

    int usb\_dc\_attach(void)
    :   Attach USB for device connection.

        Function to attach USB for device connection. Upon success, the USB PLL is enabled, and the USB device is now capable of transmitting and receiving on the USB bus and of generating interrupts.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_detach(void)
    :   Detach the USB device.

        Function to detach the USB device. Upon success, the USB hardware PLL is powered down and USB communication is disabled.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_reset(void)
    :   Reset the USB device.

        This function returns the USB device and firmware back to it’s initial state. N.B. the USB PLL is handled by the usb\_detach function

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_set\_address(const uint8\_t addr)
    :   Set USB device address.

        Parameters:
        :   - **addr** – **[in]** Device address

        Returns:
        :   0 on success, negative errno code on fail.

    void usb\_dc\_set\_status\_callback(const [usb\_dc\_status\_callback](#c.usb_dc_status_callback) cb)
    :   Set USB device controller status callback.

        Function to set USB device controller status callback. The registered callback is used to report changes in the status of the device controller. The status code are described by the [usb\_dc\_status\_code](#group____usb__device__controller__api_1gac09e3e0af1a2b41a5bfbad91f900baf7) enumeration.

        Parameters:
        :   - **cb** – **[in]** Callback function

    int usb\_dc\_ep\_check\_cap(const struct [usb\_dc\_ep\_cfg\_data](#c.usb_dc_ep_cfg_data) \*const cfg)
    :   check endpoint capabilities

        Function to check capabilities of an endpoint. [usb\_dc\_ep\_cfg\_data](#structusb__dc__ep__cfg__data) structure provides the endpoint configuration parameters: endpoint address, endpoint maximum packet size and endpoint type. The driver should check endpoint capabilities and return 0 if the endpoint configuration is possible.

        Parameters:
        :   - **cfg** – **[in]** Endpoint config

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_configure(const struct [usb\_dc\_ep\_cfg\_data](#c.usb_dc_ep_cfg_data) \*const cfg)
    :   Configure endpoint.

        Function to configure an endpoint. [usb\_dc\_ep\_cfg\_data](#structusb__dc__ep__cfg__data) structure provides the endpoint configuration parameters: endpoint address, endpoint maximum packet size and endpoint type.

        Parameters:
        :   - **cfg** – **[in]** Endpoint config

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_set\_stall(const uint8\_t ep)
    :   Set stall condition for the selected endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_clear\_stall(const uint8\_t ep)
    :   Clear stall condition for the selected endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_is\_stalled(const uint8\_t ep, uint8\_t \*const stalled)
    :   Check if the selected endpoint is stalled.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **stalled** – **[out]** Endpoint stall status

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_halt(const uint8\_t ep)
    :   Halt the selected endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_enable(const uint8\_t ep)
    :   Enable the selected endpoint.

        Function to enable the selected endpoint. Upon success interrupts are enabled for the corresponding endpoint and the endpoint is ready for transmitting/receiving data.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_disable(const uint8\_t ep)
    :   Disable the selected endpoint.

        Function to disable the selected endpoint. Upon success interrupts are disabled for the corresponding endpoint and the endpoint is no longer able for transmitting/receiving data.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_flush(const uint8\_t ep)
    :   Flush the selected endpoint.

        This function flushes the FIFOs for the selected endpoint.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_write(const uint8\_t ep, const uint8\_t \*const data, const uint32\_t data\_len, uint32\_t \*const ret\_bytes)
    :   Write data to the specified endpoint.

        This function is called to write data to the specified endpoint. The supplied [usb\_ep\_callback](usb_device.md#group____usb__device__core__api_1ga9a45db26a9be295640ed122533427725) function will be called when data is transmitted out.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data to write
            - **data\_len** – **[in]** Length of the data requested to write. This may be zero for a zero length status packet.
            - **ret\_bytes** – **[out]** Bytes scheduled for transmission. This value may be NULL if the application expects all bytes to be written

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_read(const uint8\_t ep, uint8\_t \*const data, const uint32\_t max\_data\_len, uint32\_t \*const read\_bytes)
    :   Read data from the specified endpoint.

        This function is called by the endpoint handler function, after an OUT interrupt has been received for that EP. The application must only call this function through the supplied [usb\_ep\_callback](usb_device.md#group____usb__device__core__api_1ga9a45db26a9be295640ed122533427725) function. This function clears the ENDPOINT NAK, if all data in the endpoint FIFO has been read, so as to accept more data from host.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data buffer to write to
            - **max\_data\_len** – **[in]** Max length of data to read
            - **read\_bytes** – **[out]** Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_set\_callback(const uint8\_t ep, const [usb\_dc\_ep\_callback](#c.usb_dc_ep_callback) cb)
    :   Set callback function for the specified endpoint.

        Function to set callback function for notification of data received and available to application or transmit done on the selected endpoint, NULL if callback not required by application code. The callback status code is described by [usb\_dc\_ep\_cb\_status\_code](#group____usb__device__controller__api_1gaf7f083f61e1406e7d41513113dccd3bd).

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **cb** – **[in]** Callback function

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_read\_wait(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*read\_bytes)
    :   Read data from the specified endpoint.

        This is similar to usb\_dc\_ep\_read, the difference being that, it doesn’t clear the endpoint NAKs so that the consumer is not bogged down by further upcalls till he is done with the processing of the data. The caller should reactivate ep by invoking [usb\_dc\_ep\_read\_continue()](#group____usb__device__controller__api_1ga9694ad0cc1ee84a4ed9de4f2860d4ae6) do so.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table
            - **data** – **[in]** Pointer to data buffer to write to
            - **max\_data\_len** – **[in]** Max length of data to read
            - **read\_bytes** – **[out]** Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_read\_continue(uint8\_t ep)
    :   Continue reading data from the endpoint.

        Clear the endpoint NAK and enable the endpoint to accept more data from the host. Usually called after [usb\_dc\_ep\_read\_wait()](#group____usb__device__controller__api_1ga012fb4d99870e1e30e0ecd4ac2b22312) when the consumer is fine to accept more data. Thus these calls together act as a flow control mechanism.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_dc\_ep\_mps(uint8\_t ep)
    :   Get endpoint max packet size.

        Parameters:
        :   - **ep** – **[in]** Endpoint address corresponding to the one listed in the device configuration table

        Returns:
        :   Endpoint max packet size (mps)

    int usb\_dc\_wakeup\_request(void)
    :   Start the host wake up procedure.

        Function to wake up the host if it’s currently in sleep mode.

        Returns:
        :   0 on success, negative errno code on fail.

    struct usb\_dc\_ep\_cfg\_data
    :   *#include <usb\_dc.h>*

        USB Endpoint Configuration.

        Structure containing the USB endpoint configuration.

        Public Members

        uint8\_t ep\_addr
        :   The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>.

        uint16\_t ep\_mps
        :   Endpoint max packet size.

        enum [usb\_dc\_ep\_transfer\_type](#c.usb_dc_ep_transfer_type) ep\_type
        :   Endpoint Transfer Type.

            May be Bulk, Interrupt, Control or Isochronous
