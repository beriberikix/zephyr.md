---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device/api/usb_device_bos.html
original_path: connectivity/usb/device/api/usb_device_bos.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Binary Device Object Store (BOS) support API

## API reference

*group* USB BOS support
:   USB Binary Device Object Store support.

    Enums

    enum usb\_bos\_capability\_types
    :   Device capability type codes.

        *Values:*

        enumerator USB\_BOS\_CAPABILITY\_EXTENSION = 0x02

        enumerator USB\_BOS\_CAPABILITY\_PLATFORM = 0x05

    struct usb\_bos\_descriptor
    :   *#include <bos.h>*

        Root BOS Descriptor.

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
