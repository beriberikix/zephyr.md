---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ring__buffer_8h.html
original_path: doxygen/html/ring__buffer_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ring\_buffer.h File Reference

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](ring__buffer_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ring\_buf](structring__buf.md) |
|  | A structure to represent a ring buffer. [More...](structring__buf.md#details) |

| Macros | |
| --- | --- |
| #define | [RING\_BUF\_INIT](group__ring__buffer__apis.md#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)(buf, size8) |
| #define | [RING\_BUF\_DECLARE](group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b)(name, size8) |
|  | Define and initialize a ring buffer for byte data. |
| #define | [RING\_BUF\_ITEM\_DECLARE](group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d)(name, size32) |
|  | Define and initialize an "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_DECLARE\_SIZE](group__ring__buffer__apis.md#ga205e93b5431112da0d191526906c7e01)(name, size32) |
|  | Define and initialize an "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_DECLARE\_POW2](group__ring__buffer__apis.md#gaca98f407b222dff12e2bbfcf3746a9e3)(name, pow) |
|  | Define and initialize a power-of-2 sized "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_SIZEOF](group__ring__buffer__apis.md#ga60451a56ed9b742abfa8e75ca320b004)(expr) |
|  | Compute the ring buffer size in 32-bit needed to store an element. |

| Functions | |
| --- | --- |
| static void | [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Initialize a ring buffer for byte data. |
| static void | [ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Initialize an "item based" ring buffer. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ring\_buf\_is\_empty](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine if a ring buffer is empty. |
| static void | [ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Reset ring buffer state. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine free space in a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine free space in an "item based" ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Return ring buffer capacity. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine used space in a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_put\_claim](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Allocate buffer for writing data to a ring buffer. |
| static int | [ring\_buf\_put\_finish](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Indicate number of bytes written to allocated buffers. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3) (struct [ring\_buf](structring__buf.md) \*buf, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Write (copy) data to a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_get\_claim](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Get address of a valid data in a ring buffer. |
| static int | [ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Indicate number of bytes read from claimed buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Read data from a ring buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Peek at data from a ring buffer. |
| int | [ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599) (struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size32) |
|  | Write a data item to a ring buffer. |
| int | [ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8) (struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size32) |
|  | Read a data item from a ring buffer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [ring\_buffer.h](ring__buffer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
