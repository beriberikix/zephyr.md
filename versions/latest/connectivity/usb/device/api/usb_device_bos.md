---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/device/api/usb_device_bos.html
original_path: connectivity/usb/device/api/usb_device_bos.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Binary Device Object Store (BOS) support API

## API reference

*group* usb\_bos
:   USB Binary Device Object Store support.

    Defines

    USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP
    :   Helper macro to place the BOS compatibility descriptor in the right memory section.

    Enums

    enum usb\_bos\_capability\_types
    :   Device capability type codes.

        *Values:*

        enumerator USB\_BOS\_CAPABILITY\_EXTENSION = 0x02

        enumerator USB\_BOS\_CAPABILITY\_PLATFORM = 0x05

    Functions

    void usb\_bos\_register\_cap(struct [usb\_bos\_platform\_descriptor](#c.usb_bos_platform_descriptor) \*hdr)
    :   Register BOS capability descriptor.

        This function should be used by the application to register BOS capability descriptors before the USB device stack is enabled.

        Parameters:
        :   - **hdr** – **[in]** Pointer to BOS capability descriptor

    struct usb\_bos\_capability\_lpm
    :   *#include <bos.h>*

        BOS USB 2.0 extension capability descriptor.

    struct usb\_bos\_platform\_descriptor
    :   *#include <bos.h>*

        BOS platform capability descriptor.

    struct usb\_bos\_capability\_webusb
    :   *#include <bos.h>*

        WebUSB specific part of platform capability descriptor.

    struct usb\_bos\_capability\_msos
    :   *#include <bos.h>*

        Microsoft OS 2.0 descriptor specific part of platform capability descriptor.
