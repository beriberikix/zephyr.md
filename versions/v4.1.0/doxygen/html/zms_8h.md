---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zms_8h.html
original_path: doxygen/html/zms_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/drivers/flash.h](flash_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](zms_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [zms\_fs](structzms__fs.md) |
|  | Zephyr Memory Storage file system structure. [More...](structzms__fs.md#details) |

| Functions | |
| --- | --- |
| int | [zms\_mount](group__zms__high__level__api.md#ga962625b12f21cf030a35c944a2de380e) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Mount a ZMS file system onto the device specified in fs. |
| int | [zms\_clear](group__zms__high__level__api.md#gafe06d28af34fbecf2bd666ef11095ed1) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Clear the ZMS file system from device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_write](group__zms__high__level__api.md#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write an entry to the file system. |
| int | [zms\_delete](group__zms__high__level__api.md#gacc98554728353b2d3a2e55c23a8f4746) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Delete an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_read](group__zms__high__level__api.md#ga99d451d07e5603a22996ac7960fed196) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_read\_hist](group__zms__high__level__api.md#ga1b899562d98bf088c05d9fd8b5904d81) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Read a history entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_get\_data\_length](group__zms__high__level__api.md#gafcc5b2f75f19c042b0f08192fac16b4a) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Gets the length of the data that is stored in an entry with a given id. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_calc\_free\_space](group__zms__high__level__api.md#ga02be33c18632687133f53557b5ee8bc2) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Calculate the available free space in the file system. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [zms\_active\_sector\_free\_space](group__zms__high__level__api.md#gab9ace837cff289d4ec492541dba298fa) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Tell how much contiguous free space remains in the currently active ZMS sector. |
| int | [zms\_sector\_use\_next](group__zms__high__level__api.md#ga90a6f8c47f02641ca33ee42a7c709750) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Close the currently active sector and switch to the next one. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [zms.h](zms_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
