---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/disk_8h_source.html
original_path: doxygen/html/disk_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk.h

[Go to the documentation of this file.](disk_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \* Copyright (c) 2021 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

17

18#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DISK\_H\_

19#define ZEPHYR\_INCLUDE\_DRIVERS\_DISK\_H\_

20

27

28#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

29#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

30#include <[zephyr/sys/dlist.h](dlist_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

39

[ 41](group__disk__driver__interface.md#ga7e75d3121989e64a8c6e218409e8fe95)#define DISK\_IOCTL\_GET\_SECTOR\_COUNT 1

[ 43](group__disk__driver__interface.md#ga03dcb39dd5be7144d8f6ae76b7415e9a)#define DISK\_IOCTL\_GET\_SECTOR\_SIZE 2

[ 45](group__disk__driver__interface.md#ga7ffc5d075a4e8d6eb659ee4ea73e62a0)#define DISK\_IOCTL\_RESERVED 3

[ 47](group__disk__driver__interface.md#ga2444e2a2884f9e0d6dd93aedc5d654ac)#define DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ 4

[ 49](group__disk__driver__interface.md#ga656aaa245cc142f3ff82a003bb307d62)#define DISK\_IOCTL\_CTRL\_SYNC 5

50

54

[ 56](group__disk__driver__interface.md#gae1730a7bf4ca0210bc8eefe3b590623a)#define DISK\_STATUS\_OK 0x00

[ 58](group__disk__driver__interface.md#ga533eb718a946ba60e0ad6e0e4fd4f75a)#define DISK\_STATUS\_UNINIT 0x01

[ 60](group__disk__driver__interface.md#ga1c70c8182b3497f606091f19c142be59)#define DISK\_STATUS\_NOMEDIA 0x02

[ 62](group__disk__driver__interface.md#ga0a5ba8f4be6241f62a969ea56c26f7e3)#define DISK\_STATUS\_WR\_PROTECT 0x04

63

64struct [disk\_operations](structdisk__operations.md);

65

[ 69](structdisk__info.md)struct [disk\_info](structdisk__info.md) {

[ 71](structdisk__info.md#ab3413d8809d5181c671e1890a4662ba2) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structdisk__info.md#ab3413d8809d5181c671e1890a4662ba2);

[ 73](structdisk__info.md#a817b13306aa7deab4d366482b77e4dfc) char \*[name](structdisk__info.md#a817b13306aa7deab4d366482b77e4dfc);

[ 75](structdisk__info.md#a329a571f988718fd4737b8974d4f7ada) const struct [disk\_operations](structdisk__operations.md) \*[ops](structdisk__info.md#a329a571f988718fd4737b8974d4f7ada);

[ 77](structdisk__info.md#ae316915bd577f22dc9d353fc4b2f04bb) const struct [device](structdevice.md) \*[dev](structdisk__info.md#ae316915bd577f22dc9d353fc4b2f04bb);

78};

79

[ 83](structdisk__operations.md)struct [disk\_operations](structdisk__operations.md) {

[ 84](structdisk__operations.md#ad944962a397c3427b4b6331518d6eb8b) int (\*[init](structdisk__operations.md#ad944962a397c3427b4b6331518d6eb8b))(struct [disk\_info](structdisk__info.md) \*disk);

[ 85](structdisk__operations.md#acd7d82f4d65ae8badd5005ae3a21bf44) int (\*[status](structdisk__operations.md#acd7d82f4d65ae8badd5005ae3a21bf44))(struct [disk\_info](structdisk__info.md) \*disk);

[ 86](structdisk__operations.md#a2899499e982a861f41d02fa2e856b753) int (\*[read](structdisk__operations.md#a2899499e982a861f41d02fa2e856b753))(struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf,

87 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector);

[ 88](structdisk__operations.md#ad74bec53a1ef7dc159b1ca90dd3c5a91) int (\*[write](structdisk__operations.md#ad74bec53a1ef7dc159b1ca90dd3c5a91))(struct [disk\_info](structdisk__info.md) \*disk, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf,

89 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector);

[ 90](structdisk__operations.md#a890f3f9e912b7e0b56fa105f82608f97) int (\*[ioctl](structdisk__operations.md#a890f3f9e912b7e0b56fa105f82608f97))(struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff);

91};

92

[ 100](group__disk__driver__interface.md#gaa11586a0b8ae6f2f0c142cec0df0c5fa)int [disk\_access\_register](group__disk__driver__interface.md#gaa11586a0b8ae6f2f0c142cec0df0c5fa)(struct [disk\_info](structdisk__info.md) \*disk);

101

[ 109](group__disk__driver__interface.md#gada802c6be65186009162a25f391dfb71)int [disk\_access\_unregister](group__disk__driver__interface.md#gada802c6be65186009162a25f391dfb71)(struct [disk\_info](structdisk__info.md) \*disk);

110

111#ifdef \_\_cplusplus

112}

113#endif

114

118

119#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DISK\_H\_ \*/

[dlist.h](dlist_8h.md)

[disk\_access\_register](group__disk__driver__interface.md#gaa11586a0b8ae6f2f0c142cec0df0c5fa)

int disk\_access\_register(struct disk\_info \*disk)

Register disk.

[disk\_access\_unregister](group__disk__driver__interface.md#gada802c6be65186009162a25f391dfb71)

int disk\_access\_unregister(struct disk\_info \*disk)

Unregister disk.

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[disk\_info](structdisk__info.md)

Disk info.

**Definition** disk.h:69

[disk\_info::ops](structdisk__info.md#a329a571f988718fd4737b8974d4f7ada)

const struct disk\_operations \* ops

Disk operations.

**Definition** disk.h:75

[disk\_info::name](structdisk__info.md#a817b13306aa7deab4d366482b77e4dfc)

char \* name

Disk name.

**Definition** disk.h:73

[disk\_info::node](structdisk__info.md#ab3413d8809d5181c671e1890a4662ba2)

sys\_dnode\_t node

Internally used list node.

**Definition** disk.h:71

[disk\_info::dev](structdisk__info.md#ae316915bd577f22dc9d353fc4b2f04bb)

const struct device \* dev

Device associated to this disk.

**Definition** disk.h:77

[disk\_operations](structdisk__operations.md)

Disk operations.

**Definition** disk.h:83

[disk\_operations::read](structdisk__operations.md#a2899499e982a861f41d02fa2e856b753)

int(\* read)(struct disk\_info \*disk, uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)

**Definition** disk.h:86

[disk\_operations::ioctl](structdisk__operations.md#a890f3f9e912b7e0b56fa105f82608f97)

int(\* ioctl)(struct disk\_info \*disk, uint8\_t cmd, void \*buff)

**Definition** disk.h:90

[disk\_operations::status](structdisk__operations.md#acd7d82f4d65ae8badd5005ae3a21bf44)

int(\* status)(struct disk\_info \*disk)

**Definition** disk.h:85

[disk\_operations::write](structdisk__operations.md#ad74bec53a1ef7dc159b1ca90dd3c5a91)

int(\* write)(struct disk\_info \*disk, const uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)

**Definition** disk.h:88

[disk\_operations::init](structdisk__operations.md#ad944962a397c3427b4b6331518d6eb8b)

int(\* init)(struct disk\_info \*disk)

**Definition** disk.h:84

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [disk.h](disk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
