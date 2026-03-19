---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mmc_8h.html
original_path: doxygen/html/mmc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmc.h File Reference

Public API for MMC memory card subsystem.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sdhc.h](sdhc_8h_source.md)>`  
`#include <[zephyr/sd/sd.h](sd_8h_source.md)>`

[Go to the source code of this file.](mmc_8h_source.md)

| Functions | |
| --- | --- |
| int | [mmc\_write\_blocks](#acc996d4fba8673401816a7b41707b96f) (struct [sd\_card](structsd__card.md) \*card, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*wbuf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Write blocks to MMC card from buffer. |
| int | [mmc\_read\_blocks](#aa890ebd312875906583d56ddb1a03560) (struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rbuf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Read block from MMC card to buffer. |
| int | [mmc\_ioctl](#a2dd835a0e88299400cd1b4e1533a7b4b) (struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf) |
|  | Get I/O control data from MMC card. |

## Detailed Description

Public API for MMC memory card subsystem.

## Function Documentation

## [◆ ](#a2dd835a0e88299400cd1b4e1533a7b4b)mmc\_ioctl()

| int mmc\_ioctl | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | void \* | *buf* ) |

Get I/O control data from MMC card.

Sends I/O control commands to MMC card.

Parameters
:   | card | MMC card |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | I/O control command Mirrors disk subsystem, see [include/zephyr/drivers/disk.h](disk_8h.md "Disk Driver Interface.") for list of possible commands. |
    | buf | I/O control buf |

Return values
:   | 0 | IOCTL command succeeded |
    | --- | --- |
    | -ENOTSUP | IOCTL command not supported |
    | -EIO | I/O failure |

## [◆ ](#aa890ebd312875906583d56ddb1a03560)mmc\_read\_blocks()

| int mmc\_read\_blocks | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rbuf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_block*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_blocks* ) |

Read block from MMC card to buffer.

Reads blocks into MMC buffer from MMC card. For best performance, this buffer should be aligned to CONFIG\_SDHC\_BUFFER\_ALIGNMENT

Parameters
:   | card | MMC card to read from |
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

## [◆ ](#acc996d4fba8673401816a7b41707b96f)mmc\_write\_blocks()

| int mmc\_write\_blocks | ( | struct [sd\_card](structsd__card.md) \* | *card*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *wbuf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_block*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_blocks* ) |

Write blocks to MMC card from buffer.

Writes blocks from MMC buffer to MMC card. For best performance, this buffer should be aligned to CONFIG\_SDHC\_BUFFER\_ALIGNMENT

Parameters
:   | card | MMC card to write from |
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
- [mmc.h](mmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
