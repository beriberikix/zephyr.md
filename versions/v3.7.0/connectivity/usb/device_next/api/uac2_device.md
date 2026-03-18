---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/api/uac2_device.html
original_path: connectivity/usb/device_next/api/uac2_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Audio Class 2 device API

USB Audio Class 2 device specific API defined in [include/zephyr/usb/class/usbd\_uac2.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_uac2.h).

## API Reference

Related code samples

[USB Audio asynchronous explicit feedback sample](../../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")
:   USB Audio 2 explicit feedback sample playing audio on I2S.

*group* USB Audio Class 2 device API
:   USB Audio Class 2 device API.

    Defines

    UAC2\_ENTITY\_ID(node)
    :   Get entity ID.

        Parameters:
        :   - **node** – node identifier

    Functions

    void usbd\_uac2\_set\_ops(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [uac2\_ops](#c.uac2_ops) \*ops, void \*user\_data)
    :   Register USB Audio 2 application callbacks.

        Parameters:
        :   - **dev** – USB Audio 2 device instance
            - **ops** – USB Audio 2 callback structure
            - **user\_data** – Opaque user data to pass to ops callbacks

    int usbd\_uac2\_send(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, void \*data, uint16\_t size)
    :   Send audio data to output terminal.

        Data buffer must be sufficiently aligned and otherwise suitable for use by UDC driver.

        Parameters:
        :   - **dev** – USB Audio 2 device
            - **terminal** – Output Terminal ID linked to AudioStreaming interface
            - **data** – Buffer containing outgoing data
            - **size** – Number of bytes to send

        Returns:
        :   0 on success, negative value on error

    struct uac2\_ops
    :   *#include <usbd\_uac2.h>*

        USB Audio 2 application event handlers.

        Public Members

        void (\*sof\_cb)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, void \*user\_data)
        :   Start of Frame callback.

            Notifies application about SOF event on the bus.

            Param dev:
            :   USB Audio 2 device

            Param user\_data:
            :   Opaque user data pointer

        void (\*terminal\_update\_cb)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, bool enabled, bool microframes, void \*user\_data)
        :   Terminal update callback.

            Notifies application that host has enabled or disabled a terminal.

            Param dev:
            :   USB Audio 2 device

            Param terminal:
            :   Terminal ID linked to AudioStreaming interface

            Param enabled:
            :   True if host enabled terminal, False otherwise

            Param microframes:
            :   True if USB connection speed uses microframes

            Param user\_data:
            :   Opaque user data pointer

        void \*(\*get\_recv\_buf)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, uint16\_t size, void \*user\_data)
        :   Get receive buffer address.

            USB stack calls this function to obtain receive buffer address for AudioStreaming interface. The buffer is owned by USB stack until [data\_recv\_cb](#structuac2__ops_1abb973db8018d09ba34f508c4e8aff573) callback is called. The buffer must be sufficiently aligned and otherwise suitable for use by UDC driver.

            Param dev:
            :   USB Audio 2 device

            Param terminal:
            :   Input Terminal ID linked to AudioStreaming interface

            Param size:
            :   Maximum number of bytes USB stack will write to buffer.

            Param user\_data:
            :   Opaque user data pointer

        void (\*data\_recv\_cb)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, void \*buf, uint16\_t size, void \*user\_data)
        :   Data received.

            This function releases buffer obtained in [get\_recv\_buf](#structuac2__ops_1ab41274aadc39d39cbcbfe0047a56f24b) after USB has written data to the buffer and/or no longer needs it.

            Param dev:
            :   USB Audio 2 device

            Param terminal:
            :   Input Terminal ID linked to AudioStreaming interface

            Param buf:
            :   Buffer previously obtained via [get\_recv\_buf](#structuac2__ops_1ab41274aadc39d39cbcbfe0047a56f24b)

            Param size:
            :   Number of bytes written to buffer

            Param user\_data:
            :   Opaque user data pointer

        void (\*buf\_release\_cb)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, void \*buf, void \*user\_data)
        :   Transmit buffer release callback.

            This function releases buffer provided in [usbd\_uac2\_send](#group__uac2__device_1gae899d75d786f5b1df86db48de88d1254) when the class no longer needs it.

            Param dev:
            :   USB Audio 2 device

            Param terminal:
            :   Output Terminal ID linked to AudioStreaming interface

            Param buf:
            :   Buffer previously provided via [usbd\_uac2\_send](#group__uac2__device_1gae899d75d786f5b1df86db48de88d1254)

            Param user\_data:
            :   Opaque user data pointer

        uint32\_t (\*feedback\_cb)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t terminal, void \*user\_data)
        :   Get Explicit Feedback value.

            Explicit feedback value format depends terminal connection speed. If device is High-Speed capable, it must use Q16.16 format if and only if the [terminal\_update\_cb](#structuac2__ops_1ae938633dcf6eb6f120ca458bf8a2142f) was called with microframes parameter set to true. On Full-Speed only devices, or if High-Speed capable device is operating at Full-Speed (microframes was false), the format is Q10.14 stored on 24 least significant bits (i.e. 8 most significant bits are ignored).

            Param dev:
            :   USB Audio 2 device

            Param terminal:
            :   Input Terminal ID whose feedback should be returned

            Param user\_data:
            :   Opaque user data pointer
