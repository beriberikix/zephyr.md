---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sdmmc_8h.html
original_path: doxygen/html/sdmmc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdmmc.h File Reference

Public API for SD memory card subsystem.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sdhc.h](sdhc_8h_source.md)>`  
`#include <[zephyr/sd/sd.h](sd_8h_source.md)>`

[Go to the source code of this file.](sdmmc_8h_source.md)

| Functions | |
| --- | --- |
| int | [sdmmc\_write\_blocks](#acd78118815c9f77e0c3c6fe72938eabb) (struct [sd\_card](structsd__card.md) \*card, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*wbuf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Write blocks to SD card from buffer. |
| int | [sdmmc\_read\_blocks](#a7d6ac16b7ebbaefd1667fe7ba3abd910) (struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rbuf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Read block from SD card to buffer. |
| int | [sdmmc\_ioctl](#adba7120fd5b4b1131200a2c7c97f4bf4) (struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf) |
|  | Get I/O control data from SD card. |

## Detailed Description

Public API for SD memory card subsystem.

## Function Documentation

## [◆ ](#adba7120fd5b4b1131200a2c7c97f4bf4)sdmmc\_ioctl()

| int sdmmc\_ioctl | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | void \* | *buf* ) |

Get I/O control data from SD card.

Sends I/O control commands to SD card.

Parameters
:   | card | SD card |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | I/O control command |
    | buf | I/O control buf |

Return values
:   | 0 | IOCTL command succeeded |
    | --- | --- |
    | -ENOTSUP | IOCTL command not supported |
    | -EIO | I/O failure |

## [◆ ](#a7d6ac16b7ebbaefd1667fe7ba3abd910)sdmmc\_read\_blocks()

| int sdmmc\_read\_blocks | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rbuf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_block*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_blocks* ) |

Read block from SD card to buffer.

Reads blocks into SD buffer from SD card. For best performance, this buffer should be aligned to CONFIG\_SDHC\_BUFFER\_ALIGNMENT

Parameters
:   | card | SD card to read from |
    | --- | --- |
    | rbuf | read buffer |
    | start\_block | first block to read from |
    | num\_blocks | number of blocks to read |

Return values
:   | 0 | read succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card read timed out |
    | -EIO | I/O error |

## [◆ ](#acd78118815c9f77e0c3c6fe72938eabb)sdmmc\_write\_blocks()

| int sdmmc\_write\_blocks | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *wbuf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_block*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_blocks* ) |

Write blocks to SD card from buffer.

Writes blocks from SD buffer to SD card. For best performance, this buffer should be aligned to CONFIG\_SDHC\_BUFFER\_ALIGNMENT

Parameters
:   | card | SD card to write from |
    | --- | --- |
    | wbuf | write buffer |
    | start\_block | first block to write to |
    | num\_blocks | number of blocks to write |

Return values
:   | 0 | write succeeded |
    | --- | --- |
    | -EBUSY | card is busy with another request |
    | -ETIMEDOUT | card write timed out |
    | -EIO | I/O error |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sdmmc.h](sdmmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
