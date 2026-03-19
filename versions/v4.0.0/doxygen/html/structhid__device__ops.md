---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhid__device__ops.html
original_path: doxygen/html/structhid__device__ops.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hid\_device\_ops Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USBD HID device API](group__usbd__hid__device.md)

HID device user callbacks.
[More...](#details)

`#include <[usbd_hid.h](usbd__hid_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [iface\_ready](#a8d96a142b963dd257b2dbb64df82181d) )(const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ready) |
|  | The interface ready callback is called with the ready argument set to true when the corresponding interface is part of the active configuration and the device can e.g. |
| int(\* | [get\_report](#aff034989bee801c143384464eb6a5a9d) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
|  | This callback is called for the HID Get Report request to get a feature, input, or output report, which is specified by the argument type. |
| int(\* | [set\_report](#add555b9782b763d5b411909d07d952b8) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
|  | This callback is called for the HID Set Report request to set a feature, input, or output report, which is specified by the argument type. |
| void(\* | [set\_idle](#a48e03408d693d4d9d9dacf6513a36828) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) duration) |
|  | Notification to limit input report frequency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_idle](#afd8c16e1256945bc15c70439051deb26) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | If a report ID is used in the report descriptor, the device must implement this callback and return the duration for the specified report ID. |
| void(\* | [set\_protocol](#ae9290b806b57c9595fad3ec0a65fdca2) )(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto) |
|  | Notification that the host has changed the protocol from Boot Protocol(0) to Report Protocol(1) or vice versa. |
| void(\* | [input\_report\_done](#ae60e82dd991f18d28da1a035ae6b257c) )(const struct [device](structdevice.md) \*dev) |
|  | Notification that input report submitted with [hid\_device\_submit\_report()](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8 "Submit new input report.") has been sent. |
| void(\* | [output\_report](#ac58785fc2a44be7c46e0c950fc09f0ac) )(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
|  | New output report callback. |
| void(\* | [sof](#a0043b6bf005785274de2b65f341cb588) )(const struct [device](structdevice.md) \*dev) |
|  | Optional Start of Frame (SoF) event callback. |

## Detailed Description

HID device user callbacks.

Each device depends on a user part that handles feature, input, and output report processing according to the device functionality described by the report descriptor. Which callbacks must be implemented depends on the device functionality. The USB device part of the HID device, cannot interpret device specific report descriptor and only handles USB specific parts, transfers and validation of requests, all reports are opaque to it. Callbacks are called from the USB device stack thread and must not block.

## Field Documentation

## [◆ ](#afd8c16e1256945bc15c70439051deb26)get\_idle

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* hid\_device\_ops::get\_idle) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
| --- |

If a report ID is used in the report descriptor, the device must implement this callback and return the duration for the specified report ID.

Duration time resolution is in milliseconds.

## [◆ ](#aff034989bee801c143384464eb6a5a9d)get\_report

| int(\* hid\_device\_ops::get\_report) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
| --- |

This callback is called for the HID Get Report request to get a feature, input, or output report, which is specified by the argument type.

If there is no report ID in the report descriptor, the id argument is zero. The callback implementation must check the arguments, such as whether the report type is supported and the report length, and return a negative value to indicate an unsupported type or an error, or return the length of the report written to the buffer.

## [◆ ](#a8d96a142b963dd257b2dbb64df82181d)iface\_ready

| void(\* hid\_device\_ops::iface\_ready) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ready) |
| --- |

The interface ready callback is called with the ready argument set to true when the corresponding interface is part of the active configuration and the device can e.g.

begin submitting input reports, and with the argument set to false when the interface is no longer active. This callback is optional.

## [◆ ](#ae60e82dd991f18d28da1a035ae6b257c)input\_report\_done

| void(\* hid\_device\_ops::input\_report\_done) (const struct [device](structdevice.md) \*dev) |
| --- |

Notification that input report submitted with [hid\_device\_submit\_report()](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8 "Submit new input report.") has been sent.

If the device does not use the callback, [hid\_device\_submit\_report()](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8 "Submit new input report.") will be processed synchronously.

## [◆ ](#ac58785fc2a44be7c46e0c950fc09f0ac)output\_report

| void(\* hid\_device\_ops::output\_report) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
| --- |

New output report callback.

Callback will only be called for reports received through the optional interrupt OUT pipe. If there is no interrupt OUT pipe, output reports will be received using [set\_report()](#add555b9782b763d5b411909d07d952b8). If a report ID is used in the report descriptor, the host places the ID in the buffer first, followed by the report data.

## [◆ ](#a48e03408d693d4d9d9dacf6513a36828)set\_idle

| void(\* hid\_device\_ops::set\_idle) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) duration) |
| --- |

Notification to limit input report frequency.

The device should mute an input report submission until a new event occurs or until the time specified by the duration value has elapsed. If a report ID is used in the report descriptor, the device must store the duration and handle the specified report accordingly. Duration time resolution is in milliseconds.

## [◆ ](#ae9290b806b57c9595fad3ec0a65fdca2)set\_protocol

| void(\* hid\_device\_ops::set\_protocol) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto) |
| --- |

Notification that the host has changed the protocol from Boot Protocol(0) to Report Protocol(1) or vice versa.

## [◆ ](#add555b9782b763d5b411909d07d952b8)set\_report

| int(\* hid\_device\_ops::set\_report) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const buf) |
| --- |

This callback is called for the HID Set Report request to set a feature, input, or output report, which is specified by the argument type.

If there is no report ID in the report descriptor, the id argument is zero. The callback implementation must check the arguments, such as whether the report type is supported, and return a nonzero value to indicate an unsupported type or an error.

## [◆ ](#a0043b6bf005785274de2b65f341cb588)sof

| void(\* hid\_device\_ops::sof) (const struct [device](structdevice.md) \*dev) |
| --- |

Optional Start of Frame (SoF) event callback.

There will always be software and hardware dependent jitter and latency. This should be used very carefully, it should not block and the execution time should be quite short.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usbd\_hid.h](usbd__hid_8h_source.md)

- [hid\_device\_ops](structhid__device__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
