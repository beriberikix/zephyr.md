---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structudc__ep__config.html
original_path: doxygen/html/structudc__ep__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_ep\_config Struct Reference

USB device controller endpoint configuration.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_fifo](structk__fifo.md) | [fifo](#aa62ff3f308771d51563df88439570918) |
|  | Endpoint requests FIFO. |
| struct [udc\_ep\_caps](structudc__ep__caps.md) | [caps](#a706987205ac971574d1b81bf72d03248) |
|  | Endpoint capabilities. |
| struct [udc\_ep\_stat](structudc__ep__stat.md) | [stat](#ad42f77d1a9d65239cdb142209050e38e) |
|  | Endpoint status. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#ac795b839cbd426d233a1f91d10d5fc7e) |
|  | Endpoint address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [attributes](#acbeab755d1b03da0c58f43aff5bd7d00) |
|  | Endpoint attributes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mps](#ae4f75e52d1c822f5d873095a761c6b48) |
|  | Maximum packet size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [interval](#a1f2afc2d5e512229688764e1b7cd0171) |
|  | Polling interval. |

## Detailed Description

USB device controller endpoint configuration.

This structure is mandatory for configuration and management of endpoints. It is not exposed to higher layer and is used only by internal part of UDC API and driver.

## Field Documentation

## [◆ ](#ac795b839cbd426d233a1f91d10d5fc7e)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) udc\_ep\_config::addr |
| --- |

Endpoint address.

## [◆ ](#acbeab755d1b03da0c58f43aff5bd7d00)attributes

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) udc\_ep\_config::attributes |
| --- |

Endpoint attributes.

## [◆ ](#a706987205ac971574d1b81bf72d03248)caps

| struct [udc\_ep\_caps](structudc__ep__caps.md) udc\_ep\_config::caps |
| --- |

Endpoint capabilities.

## [◆ ](#aa62ff3f308771d51563df88439570918)fifo

| struct [k\_fifo](structk__fifo.md) udc\_ep\_config::fifo |
| --- |

Endpoint requests FIFO.

## [◆ ](#a1f2afc2d5e512229688764e1b7cd0171)interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) udc\_ep\_config::interval |
| --- |

Polling interval.

## [◆ ](#ae4f75e52d1c822f5d873095a761c6b48)mps

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) udc\_ep\_config::mps |
| --- |

Maximum packet size.

## [◆ ](#ad42f77d1a9d65239cdb142209050e38e)stat

| struct [udc\_ep\_stat](structudc__ep__stat.md) udc\_ep\_config::stat |
| --- |

Endpoint status.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_ep\_config](structudc__ep__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
