---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__ccc__target__payload.html
original_path: doxygen/html/structi3c__ccc__target__payload.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_target\_payload Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload structure for Direct CCC to one target.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#a2669978506b20ef01569357fbd3a9eef) |
|  | Target address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rnw](#aa09ebbfdff5d9d97be1558a63bb3535e):1 |
|  | `0` for Write, `1` for Read |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#abc655b08df77701275038e80bfb5ba85) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#a5ddda39b2aeb2818b389d4df1e25ba0a) |
|  | Length in bytes for `data`. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_xfer](#ae6091f0b1cc804f9658d941f6ab493ef) |
|  | Total number of bytes transferred. |
| enum [i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0) | [err](#af061d387258ee3e2454ceae0b7c0dcf7) |
|  | SDR Error Type. |

## Detailed Description

Payload structure for Direct CCC to one target.

## Field Documentation

## [◆ ](#a2669978506b20ef01569357fbd3a9eef)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_target\_payload::addr |
| --- |

Target address.

## [◆ ](#abc655b08df77701275038e80bfb5ba85)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* i3c\_ccc\_target\_payload::data |
| --- |

- For Write CCC, pointer to the byte array of data to be sent, which may contain the Sub-Command Byte and additional data.
- For Read CCC, pointer to the byte buffer for data to be read into.

## [◆ ](#a5ddda39b2aeb2818b389d4df1e25ba0a)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i3c\_ccc\_target\_payload::data\_len |
| --- |

Length in bytes for `data`.

## [◆ ](#af061d387258ee3e2454ceae0b7c0dcf7)err

| enum [i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0) i3c\_ccc\_target\_payload::err |
| --- |

SDR Error Type.

Error from I3C Specification v1.1.1 section 5.1.10.2. It is expected for the driver to write to this.

## [◆ ](#ae6091f0b1cc804f9658d941f6ab493ef)num\_xfer

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i3c\_ccc\_target\_payload::num\_xfer |
| --- |

Total number of bytes transferred.

A Target can issue an EoD or the Controller can abort a transfer before the length of the buffer. It is expected for the driver to write to this after the transfer.

## [◆ ](#aa09ebbfdff5d9d97be1558a63bb3535e)rnw

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_target\_payload::rnw |
| --- |

`0` for Write, `1` for Read

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
