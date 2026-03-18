---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/disk__access_8h.html
original_path: doxygen/html/disk__access_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk\_access.h File Reference

Disk Access layer API.
[More...](#details)

`#include <[zephyr/drivers/disk.h](disk_8h_source.md)>`

[Go to the source code of this file.](disk__access_8h_source.md)

| Functions | |
| --- | --- |
| int | [disk\_access\_init](group__disk__access__interface.md#gaba3fead8c0ce65945b440bf824fd4144) (const char \*pdrv) |
|  | perform any initialization |
| int | [disk\_access\_status](group__disk__access__interface.md#gac5348a854fe68a607672118c91346133) (const char \*pdrv) |
|  | Get the status of disk. |
| int | [disk\_access\_read](group__disk__access__interface.md#ga5152825bf2a70902e65dbc596a944a1b) (const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
|  | read data from disk |
| int | [disk\_access\_write](group__disk__access__interface.md#gaa0495600320a71ea9e861fcf19da7184) (const char \*pdrv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
|  | write data to disk |
| int | [disk\_access\_ioctl](group__disk__access__interface.md#ga152d85821d73644fea7ffde27b7c953c) (const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff) |
|  | Get/Configure disk parameters. |

## Detailed Description

Disk Access layer API.

This file contains APIs for disk access.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [disk\_access.h](disk__access_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
