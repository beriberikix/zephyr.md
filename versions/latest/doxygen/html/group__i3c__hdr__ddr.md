---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i3c__hdr__ddr.html
original_path: doxygen/html/group__i3c__hdr__ddr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C HDR DDR API

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C HDR DDR API.
[More...](#details)

| Functions | |
| --- | --- |
| static int | [i3c\_hdr\_ddr\_write](#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I3C target device with HDR DDR. |
| static int | [i3c\_hdr\_ddr\_read](#ga11e788383aeb52184fdd6483cf702d40) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I3C target device with HDR DDR. |
| static int | [i3c\_hdr\_ddr\_write\_read](#gaa752f1095c84ad1b94fb09cc0aeee4fa) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) read\_cmd, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_cmd) |
|  | Write then read data from an I3C target device with HDR DDR. |

## Detailed Description

I3C HDR DDR API.

## Function Documentation

## [◆ ](#ga11e788383aeb52184fdd6483cf702d40)i3c\_hdr\_ddr\_read()

| | int i3c\_hdr\_ddr\_read | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hdr_ddr.h](hdr__ddr_8h.md)>`

Read a set amount of data from an I3C target device with HDR DDR.

This routine reads a set amount of data synchronously.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | 7-bit command code |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes to read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)i3c\_hdr\_ddr\_write()

| | int i3c\_hdr\_ddr\_write | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hdr_ddr.h](hdr__ddr_8h.md)>`

Write a set amount of data to an I3C target device with HDR DDR.

This routine writes a set amount of data synchronously.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | 7-bit command code |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes to write. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#gaa752f1095c84ad1b94fb09cc0aeee4fa)i3c\_hdr\_ddr\_write\_read()

| | int i3c\_hdr\_ddr\_write\_read | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *read\_cmd*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *write\_cmd* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[hdr_ddr.h](hdr__ddr_8h.md)>`

Write then read data from an I3C target device with HDR DDR.

This supports the common operation "this is what I want", "now give
it to me" transaction pair through a combined write-then-read bus transaction.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | write\_cmd | 7-bit command code for write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |
    | read\_cmd | 7-bit command code for read |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
