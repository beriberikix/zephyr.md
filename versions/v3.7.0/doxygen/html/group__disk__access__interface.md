---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__disk__access__interface.html
original_path: doxygen/html/group__disk__access__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Disk Access Interface

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md)

Disk Access APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [disk\_access\_init](#gaba3fead8c0ce65945b440bf824fd4144) (const char \*pdrv) |
|  | perform any initialization |
| int | [disk\_access\_status](#gac5348a854fe68a607672118c91346133) (const char \*pdrv) |
|  | Get the status of disk. |
| int | [disk\_access\_read](#ga5152825bf2a70902e65dbc596a944a1b) (const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
|  | read data from disk |
| int | [disk\_access\_write](#gaa0495600320a71ea9e861fcf19da7184) (const char \*pdrv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
|  | write data to disk |
| int | [disk\_access\_ioctl](#ga152d85821d73644fea7ffde27b7c953c) (const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff) |
|  | Get/Configure disk parameters. |

## Detailed Description

Disk Access APIs.

## Function Documentation

## [◆ ](#gaba3fead8c0ce65945b440bf824fd4144)disk\_access\_init()

| int disk\_access\_init | ( | const char \* | *pdrv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[disk_access.h](disk__access_8h.md)>`

perform any initialization

This call is made by the consumer before doing any IO calls so that the disk or the backing device can do any initialization. Although still supported for legacy compatibility, users should instead call [disk\_access\_ioctl](#ga152d85821d73644fea7ffde27b7c953c) with the IOCTL [DISK\_IOCTL\_CTRL\_INIT](group__disk__driver__interface.md#ga9def34b23915a3ce6c9a8a746d3d1372 "DISK_IOCTL_CTRL_INIT").

Disk initialization is reference counted, so only the first successful call to initialize a uninitialized (or previously de-initialized) disk will actually initialize the disk

Parameters
:   | [in] | pdrv | Disk name |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga152d85821d73644fea7ffde27b7c953c)disk\_access\_ioctl()

| int disk\_access\_ioctl | ( | const char \* | *pdrv*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | void \* | *buff* ) |

`#include <[disk_access.h](disk__access_8h.md)>`

Get/Configure disk parameters.

Function to get disk parameters and make any special device requests.

Parameters
:   | [in] | pdrv | Disk name |
    | --- | --- | --- |
    | [in] | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | DISK\_IOCTL\_\* code describing the request |
    | [in] | buff | Command data buffer |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga5152825bf2a70902e65dbc596a944a1b)disk\_access\_read()

| int disk\_access\_read | ( | const char \* | *pdrv*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data\_buf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_sector*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_sector* ) |

`#include <[disk_access.h](disk__access_8h.md)>`

read data from disk

Function to read data from disk to a memory buffer.

Note: if he disk is of NVMe type, user will need to ensure data\_buf pointer is 4-bytes aligned.

Parameters
:   | [in] | pdrv | Disk name |
    | --- | --- | --- |
    | [in] | data\_buf | Pointer to the memory buffer to put data. |
    | [in] | start\_sector | Start disk sector to read from |
    | [in] | num\_sector | Number of disk sectors to read |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gac5348a854fe68a607672118c91346133)disk\_access\_status()

| int disk\_access\_status | ( | const char \* | *pdrv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[disk_access.h](disk__access_8h.md)>`

Get the status of disk.

This call is used to get the status of the disk

Parameters
:   | [in] | pdrv | Disk name |
    | --- | --- | --- |

Returns
:   DISK\_STATUS\_OK or other DISK\_STATUS\_\*s

## [◆ ](#gaa0495600320a71ea9e861fcf19da7184)disk\_access\_write()

| int disk\_access\_write | ( | const char \* | *pdrv*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data\_buf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *start\_sector*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_sector* ) |

`#include <[disk_access.h](disk__access_8h.md)>`

write data to disk

Function write data from memory buffer to disk.

Note: if he disk is of NVMe type, user will need to ensure data\_buf pointer is 4-bytes aligned.

Parameters
:   | [in] | pdrv | Disk name |
    | --- | --- | --- |
    | [in] | data\_buf | Pointer to the memory buffer |
    | [in] | start\_sector | Start disk sector to write to |
    | [in] | num\_sector | Number of disk sectors to write |

Returns
:   0 on success, negative errno code on fail

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
