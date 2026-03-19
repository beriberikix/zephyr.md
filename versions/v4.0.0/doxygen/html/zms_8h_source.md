---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/zms_8h_source.html
original_path: doxygen/html/zms_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms.h

[Go to the documentation of this file.](zms_8h.md)

1/\* Copyright (c) 2024 BayLibre SAS

2 \*

3 \* SPDX-License-Identifier: Apache-2.0

4 \*

5 \* ZMS: Zephyr Memory Storage

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_FS\_ZMS\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_ZMS\_H\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11#include <[zephyr/drivers/flash.h](flash_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13#include <[zephyr/device.h](device_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

26

32

[ 34](structzms__fs.md)struct [zms\_fs](structzms__fs.md) {

[ 36](structzms__fs.md#af2dfcc5d0e8eabc5f116e2964668b05f) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structzms__fs.md#af2dfcc5d0e8eabc5f116e2964668b05f);

[ 42](structzms__fs.md#a6c28786531454a050f81981d32ca3640) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ate\_wra](structzms__fs.md#a6c28786531454a050f81981d32ca3640);

[ 44](structzms__fs.md#a25f2b002e4189ee29432198991061b7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [data\_wra](structzms__fs.md#a25f2b002e4189ee29432198991061b7a);

[ 48](structzms__fs.md#aae1ffd5eebd0bfb4c898719c221a239f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sector\_size](structzms__fs.md#aae1ffd5eebd0bfb4c898719c221a239f);

[ 50](structzms__fs.md#ad8960c2cee8e03446aca96697c0c9e4a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sector\_count](structzms__fs.md#ad8960c2cee8e03446aca96697c0c9e4a);

[ 52](structzms__fs.md#ab3b4551a3007e4b36bfd8a2fc209b543) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sector\_cycle](structzms__fs.md#ab3b4551a3007e4b36bfd8a2fc209b543);

[ 54](structzms__fs.md#af46a398f15fbb933d46c0b16283dae16) bool [ready](structzms__fs.md#af46a398f15fbb933d46c0b16283dae16);

[ 56](structzms__fs.md#af524e7a105749a3dbff41a229c20443b) struct [k\_mutex](structk__mutex.md) [zms\_lock](structzms__fs.md#af524e7a105749a3dbff41a229c20443b);

[ 58](structzms__fs.md#a2628eaff292518933e037b871179b8ea) const struct [device](structdevice.md) \*[flash\_device](structzms__fs.md#a2628eaff292518933e037b871179b8ea);

[ 60](structzms__fs.md#a19baa487b73542d4075eeb4ea24c303f) const struct [flash\_parameters](structzms__fs.md#a19baa487b73542d4075eeb4ea24c303f) \*[flash\_parameters](structzms__fs.md#a19baa487b73542d4075eeb4ea24c303f);

[ 62](structzms__fs.md#a939f1c9100dc9d2efdc163aea61e38a3) size\_t [ate\_size](structzms__fs.md#a939f1c9100dc9d2efdc163aea61e38a3);

63#if CONFIG\_ZMS\_LOOKUP\_CACHE

65 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) lookup\_cache[CONFIG\_ZMS\_LOOKUP\_CACHE\_SIZE];

66#endif

67};

68

72

78

[ 86](group__zms__high__level__api.md#ga962625b12f21cf030a35c944a2de380e)int [zms\_mount](group__zms__high__level__api.md#ga962625b12f21cf030a35c944a2de380e)(struct [zms\_fs](structzms__fs.md) \*fs);

87

[ 95](group__zms__high__level__api.md#gafe06d28af34fbecf2bd666ef11095ed1)int [zms\_clear](group__zms__high__level__api.md#gafe06d28af34fbecf2bd666ef11095ed1)(struct [zms\_fs](structzms__fs.md) \*fs);

96

[ 114](group__zms__high__level__api.md#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zms\_write](group__zms__high__level__api.md#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8)(struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, size\_t len);

115

[ 124](group__zms__high__level__api.md#gacc98554728353b2d3a2e55c23a8f4746)int [zms\_delete](group__zms__high__level__api.md#gacc98554728353b2d3a2e55c23a8f4746)(struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

125

[ 138](group__zms__high__level__api.md#ga99d451d07e5603a22996ac7960fed196)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zms\_read](group__zms__high__level__api.md#ga99d451d07e5603a22996ac7960fed196)(struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, size\_t len);

139

[ 154](group__zms__high__level__api.md#ga1b899562d98bf088c05d9fd8b5904d81)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zms\_read\_hist](group__zms__high__level__api.md#ga1b899562d98bf088c05d9fd8b5904d81)(struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, size\_t len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt);

155

[ 165](group__zms__high__level__api.md#gafcc5b2f75f19c042b0f08192fac16b4a)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zms\_get\_data\_length](group__zms__high__level__api.md#gafcc5b2f75f19c042b0f08192fac16b4a)(struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

166

[ 177](group__zms__high__level__api.md#ga02be33c18632687133f53557b5ee8bc2)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zms\_calc\_free\_space](group__zms__high__level__api.md#ga02be33c18632687133f53557b5ee8bc2)(struct [zms\_fs](structzms__fs.md) \*fs);

178

[ 186](group__zms__high__level__api.md#gab9ace837cff289d4ec492541dba298fa)size\_t [zms\_active\_sector\_free\_space](group__zms__high__level__api.md#gab9ace837cff289d4ec492541dba298fa)(struct [zms\_fs](structzms__fs.md) \*fs);

187

[ 201](group__zms__high__level__api.md#ga90a6f8c47f02641ca33ee42a7c709750)int [zms\_sector\_use\_next](group__zms__high__level__api.md#ga90a6f8c47f02641ca33ee42a7c709750)(struct [zms\_fs](structzms__fs.md) \*fs);

202

206

207#ifdef \_\_cplusplus

208}

209#endif

210

211#endif /\* ZEPHYR\_INCLUDE\_FS\_ZMS\_H\_ \*/

[device.h](device_8h.md)

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[zms\_calc\_free\_space](group__zms__high__level__api.md#ga02be33c18632687133f53557b5ee8bc2)

ssize\_t zms\_calc\_free\_space(struct zms\_fs \*fs)

Calculate the available free space in the file system.

[zms\_read\_hist](group__zms__high__level__api.md#ga1b899562d98bf088c05d9fd8b5904d81)

ssize\_t zms\_read\_hist(struct zms\_fs \*fs, uint32\_t id, void \*data, size\_t len, uint32\_t cnt)

Read a history entry from the file system.

[zms\_write](group__zms__high__level__api.md#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8)

ssize\_t zms\_write(struct zms\_fs \*fs, uint32\_t id, const void \*data, size\_t len)

Write an entry to the file system.

[zms\_sector\_use\_next](group__zms__high__level__api.md#ga90a6f8c47f02641ca33ee42a7c709750)

int zms\_sector\_use\_next(struct zms\_fs \*fs)

Close the currently active sector and switch to the next one.

[zms\_mount](group__zms__high__level__api.md#ga962625b12f21cf030a35c944a2de380e)

int zms\_mount(struct zms\_fs \*fs)

Mount a ZMS file system onto the device specified in fs.

[zms\_read](group__zms__high__level__api.md#ga99d451d07e5603a22996ac7960fed196)

ssize\_t zms\_read(struct zms\_fs \*fs, uint32\_t id, void \*data, size\_t len)

Read an entry from the file system.

[zms\_active\_sector\_free\_space](group__zms__high__level__api.md#gab9ace837cff289d4ec492541dba298fa)

size\_t zms\_active\_sector\_free\_space(struct zms\_fs \*fs)

Tell how much contiguous free space remains in the currently active ZMS sector.

[zms\_delete](group__zms__high__level__api.md#gacc98554728353b2d3a2e55c23a8f4746)

int zms\_delete(struct zms\_fs \*fs, uint32\_t id)

Delete an entry from the file system.

[zms\_get\_data\_length](group__zms__high__level__api.md#gafcc5b2f75f19c042b0f08192fac16b4a)

ssize\_t zms\_get\_data\_length(struct zms\_fs \*fs, uint32\_t id)

Gets the length of the data that is stored in an entry with a given ID.

[zms\_clear](group__zms__high__level__api.md#gafe06d28af34fbecf2bd666ef11095ed1)

int zms\_clear(struct zms\_fs \*fs)

Clear the ZMS file system from device.

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

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[zms\_fs](structzms__fs.md)

Zephyr Memory Storage file system structure.

**Definition** zms.h:34

[zms\_fs::flash\_parameters](structzms__fs.md#a19baa487b73542d4075eeb4ea24c303f)

const struct flash\_parameters \* flash\_parameters

Flash memory parameters structure.

**Definition** zms.h:60

[zms\_fs::data\_wra](structzms__fs.md#a25f2b002e4189ee29432198991061b7a)

uint64\_t data\_wra

Data write address.

**Definition** zms.h:44

[zms\_fs::flash\_device](structzms__fs.md#a2628eaff292518933e037b871179b8ea)

const struct device \* flash\_device

Flash device runtime structure.

**Definition** zms.h:58

[zms\_fs::ate\_wra](structzms__fs.md#a6c28786531454a050f81981d32ca3640)

uint64\_t ate\_wra

Allocation Table Entry (ATE) write address.

**Definition** zms.h:42

[zms\_fs::ate\_size](structzms__fs.md#a939f1c9100dc9d2efdc163aea61e38a3)

size\_t ate\_size

Size of an Allocation Table Entry.

**Definition** zms.h:62

[zms\_fs::sector\_size](structzms__fs.md#aae1ffd5eebd0bfb4c898719c221a239f)

uint32\_t sector\_size

Storage system is split into sectors.

**Definition** zms.h:48

[zms\_fs::sector\_cycle](structzms__fs.md#ab3b4551a3007e4b36bfd8a2fc209b543)

uint8\_t sector\_cycle

Current cycle counter of the active sector (pointed to by ate\_wra).

**Definition** zms.h:52

[zms\_fs::sector\_count](structzms__fs.md#ad8960c2cee8e03446aca96697c0c9e4a)

uint32\_t sector\_count

Number of sectors in the file system.

**Definition** zms.h:50

[zms\_fs::offset](structzms__fs.md#af2dfcc5d0e8eabc5f116e2964668b05f)

off\_t offset

File system offset in flash.

**Definition** zms.h:36

[zms\_fs::ready](structzms__fs.md#af46a398f15fbb933d46c0b16283dae16)

bool ready

Flag indicating if the file system is initialized.

**Definition** zms.h:54

[zms\_fs::zms\_lock](structzms__fs.md#af524e7a105749a3dbff41a229c20443b)

struct k\_mutex zms\_lock

Mutex used to lock flash writes.

**Definition** zms.h:56

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [zms.h](zms_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
