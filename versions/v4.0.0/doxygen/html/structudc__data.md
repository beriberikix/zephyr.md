---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structudc__data.html
original_path: doxygen/html/structudc__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_data Struct Reference

Common UDC driver data structure.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [udc\_ep\_config](structudc__ep__config.md) \* | [ep\_lut](#acc471b34bb24453377b1ae54d33fa415) [32] |
|  | LUT for endpoint management. |
| struct [udc\_device\_caps](structudc__device__caps.md) | [caps](#aae68bfba2e92894851c36dd40c33c0f0) |
|  | Controller capabilities. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#a1ba1b93af26bca4f4554a43a65ab3c2a) |
|  | Driver access mutex. |
| [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) | [event\_cb](#a9bb216d0c87b9ff4e2e99f0c3cfbb381) |
|  | Callback to submit an UDC event to higher layer. |
| const void \* | [event\_ctx](#aaf98e53580a27635a7b02acbcf29ae14) |
|  | Opaque pointer to store higher layer context. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [status](#a9c1ae6e5e204b5a0ed15e92f8b3b384f) |
|  | USB device controller status. |
| int | [stage](#ab957eea73de90379642ed56ddbb84989) |
|  | Internal used Control Sequence Stage. |
| struct [net\_buf](structnet__buf.md) \* | [setup](#a1bbb7a70a14368efc4b933a7d1945fb5) |
|  | Pointer to buffer containing setup packet. |
| void \* | [priv](#ac58682fa2f37bf2034a69cc9b6b10dfb) |
|  | Driver private data. |

## Detailed Description

Common UDC driver data structure.

Mandatory structure for each UDC controller driver. To be implemented as device's private data (device->data).

## Field Documentation

## [◆ ](#aae68bfba2e92894851c36dd40c33c0f0)caps

| struct [udc\_device\_caps](structudc__device__caps.md) udc\_data::caps |
| --- |

Controller capabilities.

## [◆ ](#acc471b34bb24453377b1ae54d33fa415)ep\_lut

| struct [udc\_ep\_config](structudc__ep__config.md)\* udc\_data::ep\_lut[32] |
| --- |

LUT for endpoint management.

## [◆ ](#a9bb216d0c87b9ff4e2e99f0c3cfbb381)event\_cb

| [udc\_event\_cb\_t](udc_8h.md#aa3ff247fd5234f65d91f84ebc38e384a) udc\_data::event\_cb |
| --- |

Callback to submit an UDC event to higher layer.

## [◆ ](#aaf98e53580a27635a7b02acbcf29ae14)event\_ctx

| const void\* udc\_data::event\_ctx |
| --- |

Opaque pointer to store higher layer context.

## [◆ ](#a1ba1b93af26bca4f4554a43a65ab3c2a)mutex

| struct [k\_mutex](structk__mutex.md) udc\_data::mutex |
| --- |

Driver access mutex.

## [◆ ](#ac58682fa2f37bf2034a69cc9b6b10dfb)priv

| void\* udc\_data::priv |
| --- |

Driver private data.

## [◆ ](#a1bbb7a70a14368efc4b933a7d1945fb5)setup

| struct [net\_buf](structnet__buf.md)\* udc\_data::setup |
| --- |

Pointer to buffer containing setup packet.

## [◆ ](#ab957eea73de90379642ed56ddbb84989)stage

| int udc\_data::stage |
| --- |

Internal used Control Sequence Stage.

## [◆ ](#a9c1ae6e5e204b5a0ed15e92f8b3b384f)status

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) udc\_data::status |
| --- |

USB device controller status.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_data](structudc__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
