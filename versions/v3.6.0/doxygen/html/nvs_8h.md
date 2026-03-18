---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nvs_8h.html
original_path: doxygen/html/nvs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nvs.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](nvs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nvs\_fs](structnvs__fs.md) |
|  | Non-volatile Storage File system structure. [More...](structnvs__fs.md#details) |

| Functions | |
| --- | --- |
| int | [nvs\_mount](group__nvs__high__level__api.md#gab932ea2d6e933825c2378bef8c30b065) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Mount an NVS file system onto the flash device specified in `fs`. |
| int | [nvs\_clear](group__nvs__high__level__api.md#ga42ee9fd0d98f89dcabc5888f8b4600f0) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Clear the NVS file system from flash. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_write](group__nvs__high__level__api.md#ga34d40e9f63ba514d7915b72c4fef0b82) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write an entry to the file system. |
| int | [nvs\_delete](group__nvs__high__level__api.md#ga5fd4175a4976e6d3ee8621ed95e0ee9e) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Delete an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_read](group__nvs__high__level__api.md#ga341fd2ad029709cbb6eafde1ae88603f) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_read\_hist](group__nvs__high__level__api.md#ga8e525038e353045ad6cd90607e887b0d) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cnt) |
|  | Read a history entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_calc\_free\_space](group__nvs__high__level__api.md#ga37e5a55f0b9209c7c0c95db9e1e84715) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Calculate the available free space in the file system. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [nvs.h](nvs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
