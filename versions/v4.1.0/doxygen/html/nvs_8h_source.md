---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nvs_8h_source.html
original_path: doxygen/html/nvs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nvs.h

[Go to the documentation of this file.](nvs_8h.md)

1/\* NVS: non volatile storage in flash

2 \*

3 \* Copyright (c) 2018 Laczen

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_FS\_NVS\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_NVS\_H\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/device.h](device_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

28

35

[ 39](structnvs__fs.md)struct [nvs\_fs](structnvs__fs.md) {

[ 41](structnvs__fs.md#a793b43b069d5e7a42963d84423ab5717) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structnvs__fs.md#a793b43b069d5e7a42963d84423ab5717);

[ 47](structnvs__fs.md#aba5caa7709d58fa018cbb91db085f140) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ate\_wra](structnvs__fs.md#aba5caa7709d58fa018cbb91db085f140);

[ 49](structnvs__fs.md#ac6bc3719e803f27fc20de5ebc63d7707) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_wra](structnvs__fs.md#ac6bc3719e803f27fc20de5ebc63d7707);

[ 51](structnvs__fs.md#a036af291edc8d389b56fcb532e6738df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sector\_size](structnvs__fs.md#a036af291edc8d389b56fcb532e6738df);

[ 53](structnvs__fs.md#abf8ffaea29e3357ca6e897902fd49a63) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sector\_count](structnvs__fs.md#abf8ffaea29e3357ca6e897902fd49a63);

[ 55](structnvs__fs.md#a2a167bd6a1698d2070dbe65b669ba0f4) bool [ready](structnvs__fs.md#a2a167bd6a1698d2070dbe65b669ba0f4);

[ 57](structnvs__fs.md#a6f49bb17819e3b78e0b3c1a1bc578f09) struct [k\_mutex](structk__mutex.md) [nvs\_lock](structnvs__fs.md#a6f49bb17819e3b78e0b3c1a1bc578f09);

[ 59](structnvs__fs.md#a02381974223dfbd22fe50b2cfecb7da2) const struct [device](structdevice.md) \*[flash\_device](structnvs__fs.md#a02381974223dfbd22fe50b2cfecb7da2);

[ 61](structnvs__fs.md#a34f769be6fed7c81254501af207147df) const struct [flash\_parameters](structnvs__fs.md#a34f769be6fed7c81254501af207147df) \*[flash\_parameters](structnvs__fs.md#a34f769be6fed7c81254501af207147df);

62#if CONFIG\_NVS\_LOOKUP\_CACHE

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lookup\_cache[CONFIG\_NVS\_LOOKUP\_CACHE\_SIZE];

64#endif

65};

66

70

77

[ 85](group__nvs__high__level__api.md#gab932ea2d6e933825c2378bef8c30b065)int [nvs\_mount](group__nvs__high__level__api.md#gab932ea2d6e933825c2378bef8c30b065)(struct [nvs\_fs](structnvs__fs.md) \*fs);

86

[ 94](group__nvs__high__level__api.md#ga42ee9fd0d98f89dcabc5888f8b4600f0)int [nvs\_clear](group__nvs__high__level__api.md#ga42ee9fd0d98f89dcabc5888f8b4600f0)(struct [nvs\_fs](structnvs__fs.md) \*fs);

95

[ 113](group__nvs__high__level__api.md#ga34d40e9f63ba514d7915b72c4fef0b82)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [nvs\_write](group__nvs__high__level__api.md#ga34d40e9f63ba514d7915b72c4fef0b82)(struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const void \*data, size\_t len);

114

[ 123](group__nvs__high__level__api.md#ga5fd4175a4976e6d3ee8621ed95e0ee9e)int [nvs\_delete](group__nvs__high__level__api.md#ga5fd4175a4976e6d3ee8621ed95e0ee9e)(struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

124

[ 138](group__nvs__high__level__api.md#ga341fd2ad029709cbb6eafde1ae88603f)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [nvs\_read](group__nvs__high__level__api.md#ga341fd2ad029709cbb6eafde1ae88603f)(struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, size\_t len);

139

[ 154](group__nvs__high__level__api.md#ga8e525038e353045ad6cd90607e887b0d)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [nvs\_read\_hist](group__nvs__high__level__api.md#ga8e525038e353045ad6cd90607e887b0d)(struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, size\_t len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cnt);

155

[ 165](group__nvs__high__level__api.md#ga37e5a55f0b9209c7c0c95db9e1e84715)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [nvs\_calc\_free\_space](group__nvs__high__level__api.md#ga37e5a55f0b9209c7c0c95db9e1e84715)(struct [nvs\_fs](structnvs__fs.md) \*fs);

166

[ 174](group__nvs__high__level__api.md#ga7ce6065cf3ac68544f51d26cabd983b2)size\_t [nvs\_sector\_max\_data\_size](group__nvs__high__level__api.md#ga7ce6065cf3ac68544f51d26cabd983b2)(struct [nvs\_fs](structnvs__fs.md) \*fs);

175

[ 189](group__nvs__high__level__api.md#ga52db47389e9aa2b0de77497f0e60ed5b)int [nvs\_sector\_use\_next](group__nvs__high__level__api.md#ga52db47389e9aa2b0de77497f0e60ed5b)(struct [nvs\_fs](structnvs__fs.md) \*fs);

190

194

195#ifdef \_\_cplusplus

196}

197#endif

198

199#endif /\* ZEPHYR\_INCLUDE\_FS\_NVS\_H\_ \*/

[device.h](device_8h.md)

[nvs\_read](group__nvs__high__level__api.md#ga341fd2ad029709cbb6eafde1ae88603f)

ssize\_t nvs\_read(struct nvs\_fs \*fs, uint16\_t id, void \*data, size\_t len)

Read an entry from the file system.

[nvs\_write](group__nvs__high__level__api.md#ga34d40e9f63ba514d7915b72c4fef0b82)

ssize\_t nvs\_write(struct nvs\_fs \*fs, uint16\_t id, const void \*data, size\_t len)

Write an entry to the file system.

[nvs\_calc\_free\_space](group__nvs__high__level__api.md#ga37e5a55f0b9209c7c0c95db9e1e84715)

ssize\_t nvs\_calc\_free\_space(struct nvs\_fs \*fs)

Calculate the available free space in the file system.

[nvs\_clear](group__nvs__high__level__api.md#ga42ee9fd0d98f89dcabc5888f8b4600f0)

int nvs\_clear(struct nvs\_fs \*fs)

Clear the NVS file system from flash.

[nvs\_sector\_use\_next](group__nvs__high__level__api.md#ga52db47389e9aa2b0de77497f0e60ed5b)

int nvs\_sector\_use\_next(struct nvs\_fs \*fs)

Close the currently active sector and switch to the next one.

[nvs\_delete](group__nvs__high__level__api.md#ga5fd4175a4976e6d3ee8621ed95e0ee9e)

int nvs\_delete(struct nvs\_fs \*fs, uint16\_t id)

Delete an entry from the file system.

[nvs\_sector\_max\_data\_size](group__nvs__high__level__api.md#ga7ce6065cf3ac68544f51d26cabd983b2)

size\_t nvs\_sector\_max\_data\_size(struct nvs\_fs \*fs)

Tell how many contiguous free space remains in the currently active NVS sector.

[nvs\_read\_hist](group__nvs__high__level__api.md#ga8e525038e353045ad6cd90607e887b0d)

ssize\_t nvs\_read\_hist(struct nvs\_fs \*fs, uint16\_t id, void \*data, size\_t len, uint16\_t cnt)

Read a history entry from the file system.

[nvs\_mount](group__nvs__high__level__api.md#gab932ea2d6e933825c2378bef8c30b065)

int nvs\_mount(struct nvs\_fs \*fs)

Mount an NVS file system onto the flash device specified in fs.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[nvs\_fs](structnvs__fs.md)

Non-volatile Storage File system structure.

**Definition** nvs.h:39

[nvs\_fs::flash\_device](structnvs__fs.md#a02381974223dfbd22fe50b2cfecb7da2)

const struct device \* flash\_device

Flash device runtime structure.

**Definition** nvs.h:59

[nvs\_fs::sector\_size](structnvs__fs.md#a036af291edc8d389b56fcb532e6738df)

uint16\_t sector\_size

File system is split into sectors, each sector must be multiple of erase-block-size.

**Definition** nvs.h:51

[nvs\_fs::ready](structnvs__fs.md#a2a167bd6a1698d2070dbe65b669ba0f4)

bool ready

Flag indicating if the file system is initialized.

**Definition** nvs.h:55

[nvs\_fs::flash\_parameters](structnvs__fs.md#a34f769be6fed7c81254501af207147df)

const struct flash\_parameters \* flash\_parameters

Flash memory parameters structure.

**Definition** nvs.h:61

[nvs\_fs::nvs\_lock](structnvs__fs.md#a6f49bb17819e3b78e0b3c1a1bc578f09)

struct k\_mutex nvs\_lock

Mutex.

**Definition** nvs.h:57

[nvs\_fs::offset](structnvs__fs.md#a793b43b069d5e7a42963d84423ab5717)

off\_t offset

File system offset in flash.

**Definition** nvs.h:41

[nvs\_fs::ate\_wra](structnvs__fs.md#aba5caa7709d58fa018cbb91db085f140)

uint32\_t ate\_wra

Allocation table entry write address.

**Definition** nvs.h:47

[nvs\_fs::sector\_count](structnvs__fs.md#abf8ffaea29e3357ca6e897902fd49a63)

uint16\_t sector\_count

Number of sectors in the file system.

**Definition** nvs.h:53

[nvs\_fs::data\_wra](structnvs__fs.md#ac6bc3719e803f27fc20de5ebc63d7707)

uint32\_t data\_wra

Data write address.

**Definition** nvs.h:49

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [nvs.h](nvs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
