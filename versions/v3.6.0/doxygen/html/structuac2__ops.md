---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structuac2__ops.html
original_path: doxygen/html/structuac2__ops.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uac2\_ops Struct Reference

USB Audio 2 application event handlers.
[More...](#details)

`#include <[usbd_uac2.h](usbd__uac2_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [sof\_cb](#a76e31b01dc6ce52793735b70301e8470) )(const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Start of Frame callback. |
| void(\* | [terminal\_update\_cb](#ae938633dcf6eb6f120ca458bf8a2142f) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) microframes, void \*user\_data) |
|  | Terminal update callback. |
| void \*(\* | [get\_recv\_buf](#ab41274aadc39d39cbcbfe0047a56f24b) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data) |
|  | Get receive buffer address. |
| void(\* | [data\_recv\_cb](#abb973db8018d09ba34f508c4e8aff573) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data) |
|  | Data received. |
| void(\* | [buf\_release\_cb](#aa934f5ecee8f8e67e2165735a6dd2bca) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*buf, void \*user\_data) |
|  | Transmit buffer release callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [feedback\_cb](#ad427ec3534c8c2b1fe097a7eb83a2e87) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*user\_data) |
|  | Get Explicit Feedback value. |

## Detailed Description

USB Audio 2 application event handlers.

## Field Documentation

## [◆ ](#aa934f5ecee8f8e67e2165735a6dd2bca)buf\_release\_cb

| void(\* uac2\_ops::buf\_release\_cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*buf, void \*user\_data) |
| --- |

Transmit buffer release callback.

This function releases buffer provided in [usbd\_uac2\_send](usbd__uac2_8h.md#ae899d75d786f5b1df86db48de88d1254 "usbd_uac2_send") when the class no longer needs it.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Output Terminal ID linked to AudioStreaming interface |
    | buf | Buffer previously provided via [usbd\_uac2\_send](usbd__uac2_8h.md#ae899d75d786f5b1df86db48de88d1254 "usbd_uac2_send") |
    | user\_data | Opaque user data pointer |

## [◆ ](#abb973db8018d09ba34f508c4e8aff573)data\_recv\_cb

| void(\* uac2\_ops::data\_recv\_cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data) |
| --- |

Data received.

This function releases buffer obtained in [get\_recv\_buf](#ab41274aadc39d39cbcbfe0047a56f24b) after USB has written data to the buffer and/or no longer needs it.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Input Terminal ID linked to AudioStreaming interface |
    | buf | Buffer previously obtained via [get\_recv\_buf](#ab41274aadc39d39cbcbfe0047a56f24b) |
    | size | Number of bytes written to buffer |
    | user\_data | Opaque user data pointer |

## [◆ ](#ad427ec3534c8c2b1fe097a7eb83a2e87)feedback\_cb

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* uac2\_ops::feedback\_cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*user\_data) |
| --- |

Get Explicit Feedback value.

Explicit feedback value format depends terminal connection speed. If device is High-Speed capable, it must use Q16.16 format if and only if the [terminal\_update\_cb](#ae938633dcf6eb6f120ca458bf8a2142f) was called with microframes parameter set to true. On Full-Speed only devices, or if High-Speed capable device is operating at Full-Speed (microframes was false), the format is Q10.14 stored on 24 least significant bits (i.e. 8 most significant bits are ignored).

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Input Terminal ID whose feedback should be returned |
    | user\_data | Opaque user data pointer |

## [◆ ](#ab41274aadc39d39cbcbfe0047a56f24b)get\_recv\_buf

| void \*(\* uac2\_ops::get\_recv\_buf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data) |
| --- |

Get receive buffer address.

USB stack calls this function to obtain receive buffer address for AudioStreaming interface. The buffer is owned by USB stack until [data\_recv\_cb](#abb973db8018d09ba34f508c4e8aff573) callback is called. The buffer must be sufficiently aligned for use by UDC driver.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Input Terminal ID linked to AudioStreaming interface |
    | size | Maximum number of bytes USB stack will write to buffer. |
    | user\_data | Opaque user data pointer |

## [◆ ](#a76e31b01dc6ce52793735b70301e8470)sof\_cb

| void(\* uac2\_ops::sof\_cb) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

Start of Frame callback.

Notifies application about SOF event on the bus.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | user\_data | Opaque user data pointer |

## [◆ ](#ae938633dcf6eb6f120ca458bf8a2142f)terminal\_update\_cb

| void(\* uac2\_ops::terminal\_update\_cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) microframes, void \*user\_data) |
| --- |

Terminal update callback.

Notifies application that host has enabled or disabled a terminal.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Terminal ID linked to AudioStreaming interface |
    | enabled | True if host enabled terminal, False otherwise |
    | microframes | True if USB connection speed uses microframes |
    | user\_data | Opaque user data pointer |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usbd\_uac2.h](usbd__uac2_8h_source.md)

- [uac2\_ops](structuac2__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
