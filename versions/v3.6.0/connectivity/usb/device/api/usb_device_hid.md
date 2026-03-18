---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/device/api/usb_device_hid.html
original_path: connectivity/usb/device/api/usb_device_hid.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# USB HID Class API

USB device specific part for HID support defined in
[include/zephyr/usb/class/usb\_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usb_hid.h).

## API Reference

Related code samples

[USB HID (Human Interface Device)](../../../../samples/subsys/usb/hid/README.md#usb-hid "Use USB HID driver to enumerate as a raw HID device.")
:   Use USB HID driver to enumerate as a raw HID device.

*group* usb\_hid\_device\_api
:   Typedefs

    typedef int (\*hid\_cb\_t)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct usb\_setup\_packet \*setup, int32\_t \*len, uint8\_t \*\*data)

    typedef void (\*hid\_int\_ready\_callback)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef void (\*hid\_protocol\_cb\_t)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t protocol)

    typedef void (\*hid\_idle\_cb\_t)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t report\_id)

    Functions

    void usb\_hid\_register\_device(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*desc, size\_t size, const struct [hid\_ops](#c.hid_ops) \*op)
    :   Register HID device.

        Parameters:
        :   - **dev** – **[in]** Pointer to USB HID device
            - **desc** – **[in]** Pointer to HID report descriptor
            - **size** – **[in]** Size of HID report descriptor
            - **op** – **[in]** Pointer to USB HID device interrupt struct

    int hid\_int\_ep\_write(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*data, uint32\_t data\_len, uint32\_t \*bytes\_ret)
    :   Write to USB HID interrupt endpoint buffer.

        Parameters:
        :   - **dev** – **[in]** Pointer to USB HID device
            - **data** – **[in]** Pointer to data buffer
            - **data\_len** – **[in]** Length of data to copy
            - **bytes\_ret** – **[out]** Bytes written to the EP buffer.

        Returns:
        :   0 on success, negative errno code on fail.

    int hid\_int\_ep\_read(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*ret\_bytes)
    :   Read from USB HID interrupt endpoint buffer.

        Parameters:
        :   - **dev** – **[in]** Pointer to USB HID device
            - **data** – **[in]** Pointer to data buffer
            - **max\_data\_len** – **[in]** Max length of data to copy
            - **ret\_bytes** – **[out]** Number of bytes to copy. If data is NULL and max\_data\_len is 0 the number of bytes available in the buffer will be returned.

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_hid\_set\_proto\_code(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t proto\_code)
    :   Set USB HID class Protocol Code.

        Should be called before [usb\_hid\_init()](#group__usb__hid__device__api_1ga88c23fc42f45f4ac05d9b2c1f6d7ec9b).

        Parameters:
        :   - **dev** – **[in]** Pointer to USB HID device
            - **proto\_code** – **[in]** Protocol Code to be used for bInterfaceProtocol

        Returns:
        :   0 on success, negative errno code on fail.

    int usb\_hid\_init(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initialize USB HID class support.

        Parameters:
        :   - **dev** – **[in]** Pointer to USB HID device

        Returns:
        :   0 on success, negative errno code on fail.

    struct hid\_ops
    :   *#include <usb\_hid.h>*

        USB HID device interface.
