---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/disk__access_8h_source.html
original_path: doxygen/html/disk__access_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk\_access.h

[Go to the documentation of this file.](disk__access_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_STORAGE\_DISK\_ACCESS\_H\_

15#define ZEPHYR\_INCLUDE\_STORAGE\_DISK\_ACCESS\_H\_

16

24

31

32#include <[zephyr/drivers/disk.h](disk_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 48](group__disk__access__interface.md#gaba3fead8c0ce65945b440bf824fd4144)int [disk\_access\_init](group__disk__access__interface.md#gaba3fead8c0ce65945b440bf824fd4144)(const char \*pdrv);

49

[ 59](group__disk__access__interface.md#gac5348a854fe68a607672118c91346133)int [disk\_access\_status](group__disk__access__interface.md#gac5348a854fe68a607672118c91346133)(const char \*pdrv);

60

[ 76](group__disk__access__interface.md#ga5152825bf2a70902e65dbc596a944a1b)int [disk\_access\_read](group__disk__access__interface.md#ga5152825bf2a70902e65dbc596a944a1b)(const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf,

77 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector);

78

[ 94](group__disk__access__interface.md#gaa0495600320a71ea9e861fcf19da7184)int [disk\_access\_write](group__disk__access__interface.md#gaa0495600320a71ea9e861fcf19da7184)(const char \*pdrv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf,

95 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector);

96

[ 108](group__disk__access__interface.md#ga152d85821d73644fea7ffde27b7c953c)int [disk\_access\_ioctl](group__disk__access__interface.md#ga152d85821d73644fea7ffde27b7c953c)(const char \*pdrv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff);

109

110#ifdef \_\_cplusplus

111}

112#endif

113

117

118#endif /\* ZEPHYR\_INCLUDE\_STORAGE\_DISK\_ACCESS\_H\_ \*/

[disk.h](disk_8h.md)

Disk Driver Interface.

[disk\_access\_ioctl](group__disk__access__interface.md#ga152d85821d73644fea7ffde27b7c953c)

int disk\_access\_ioctl(const char \*pdrv, uint8\_t cmd, void \*buff)

Get/Configure disk parameters.

[disk\_access\_read](group__disk__access__interface.md#ga5152825bf2a70902e65dbc596a944a1b)

int disk\_access\_read(const char \*pdrv, uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)

read data from disk

[disk\_access\_write](group__disk__access__interface.md#gaa0495600320a71ea9e861fcf19da7184)

int disk\_access\_write(const char \*pdrv, const uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)

write data to disk

[disk\_access\_init](group__disk__access__interface.md#gaba3fead8c0ce65945b440bf824fd4144)

int disk\_access\_init(const char \*pdrv)

perform any initialization

[disk\_access\_status](group__disk__access__interface.md#gac5348a854fe68a607672118c91346133)

int disk\_access\_status(const char \*pdrv)

Get the status of disk.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [disk\_access.h](disk__access_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
