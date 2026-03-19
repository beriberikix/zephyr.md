---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__pbuf.html
original_path: doxygen/html/group__pbuf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Packed Buffer API

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

Packed buffer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pbuf\_cfg](structpbuf__cfg.md) |
|  | Control block of packet buffer. [More...](structpbuf__cfg.md#details) |
| struct | [pbuf\_data](structpbuf__data.md) |
|  | Data block of the packed buffer. [More...](structpbuf__data.md#details) |
| struct | [pbuf](structpbuf.md) |
|  | Scure packed buffer. [More...](structpbuf.md#details) |

| Macros | |
| --- | --- |
| #define | [PBUF\_PACKET\_LEN\_SZ](#gaa57dc50fdf97af6690ac784f0a4450be)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) |
|  | Size of packet length field. |
| #define | [PBUF\_MAYBE\_CONST](#gaba4cc55b02db047bc2e0ca5c873b1222)   const |
| #define | [PBUF\_CFG\_INIT](#gafc65e8f044930fbd51dd6178302d75e1)(mem\_addr, size, dcache\_align) |
|  | Macro for configuration initialization. |
| #define | [PBUF\_HEADER\_OVERHEAD](#ga00f201bb5e2e139272b2c32f9c3f6efc)(dcache\_align) |
|  | Macro calculates memory overhead taken by the header in shared memory. |
| #define | [PBUF\_DEFINE](#gafc988125a3c06d0ecdc948cab3a3d23a)(name, mem\_addr, size, dcache\_align) |
|  | Statically define and initialize pbuf. |

| Functions | |
| --- | --- |
| int | [pbuf\_tx\_init](#ga05782e212932d84ba1192b4dbe1dfd42) (struct [pbuf](structpbuf.md) \*pb) |
|  | Initialize the Tx packet buffer. |
| int | [pbuf\_rx\_init](#ga9da1179f5fd3e5238244cd2f7664a928) (struct [pbuf](structpbuf.md) \*pb) |
|  | Initialize the Rx packet buffer. |
| int | [pbuf\_write](#ga9df9413dcd6268690a410c33126c081e) (struct [pbuf](structpbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write specified amount of data to the packet buffer. |
| int | [pbuf\_read](#ga44cc22d33d4ec7b7c95459e96ef7d7d0) (struct [pbuf](structpbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Read specified amount of data from the packet buffer. |

## Detailed Description

Packed buffer API.

## Macro Definition Documentation

## [◆ ](#gafc65e8f044930fbd51dd6178302d75e1)PBUF\_CFG\_INIT

| #define PBUF\_CFG\_INIT | ( |  | *mem\_addr*, |
| --- | --- | --- | --- |
|  |  |  | *size*, |
|  |  |  | *dcache\_align* ) |

`#include <[pbuf.h](pbuf_8h.md)>`

**Value:**

{ \

.rd\_idx\_loc = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)(mem\_addr), \

.wr\_idx\_loc = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(mem\_addr) + \

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE)), \

.data\_loc = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(mem\_addr) + \

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE), \

.len = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(size) - [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE) - \

\_PBUF\_IDX\_SIZE), \

.dcache\_alignment = (dcache\_align), \

}

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:385

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Macro for configuration initialization.

It is recommended to use this macro to initialize packed buffer configuration.

Parameters
:   | mem\_addr | Memory address for pbuf. |
    | --- | --- |
    | size | Size of the memory. |
    | dcache\_align | Data cache alignment. |

## [◆ ](#gafc988125a3c06d0ecdc948cab3a3d23a)PBUF\_DEFINE

| #define PBUF\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *mem\_addr*, |
|  |  |  | *size*, |
|  |  |  | *dcache\_align* ) |

`#include <[pbuf.h](pbuf_8h.md)>`

**Value:**

BUILD\_ASSERT(dcache\_align >= 0, \

"Cache line size must be non negative."); \

BUILD\_ASSERT((size) > 0 && [IS\_PTR\_ALIGNED\_BYTES](include_2zephyr_2toolchain_2common_8h.md#accd51a2e6e0aacde1d3c7ad7497e40ec)(size, \_PBUF\_IDX\_SIZE), \

"Incorrect size."); \

BUILD\_ASSERT([IS\_PTR\_ALIGNED\_BYTES](include_2zephyr_2toolchain_2common_8h.md#accd51a2e6e0aacde1d3c7ad7497e40ec)(mem\_addr, [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE)), \

"Misaligned memory."); \

BUILD\_ASSERT(size >= ([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE + \

\_PBUF\_MIN\_DATA\_LEN), "Insufficient size."); \

static [PBUF\_MAYBE\_CONST](#gaba4cc55b02db047bc2e0ca5c873b1222) struct [pbuf\_cfg](structpbuf__cfg.md) cfg\_##name = \

PBUF\_CFG\_INIT(mem\_addr, size, dcache\_align); \

static struct [pbuf](structpbuf.md) name = { \

.cfg = &cfg\_##name, \

}

[PBUF\_MAYBE\_CONST](#gaba4cc55b02db047bc2e0ca5c873b1222)

#define PBUF\_MAYBE\_CONST

**Definition** pbuf.h:42

[IS\_PTR\_ALIGNED\_BYTES](include_2zephyr_2toolchain_2common_8h.md#accd51a2e6e0aacde1d3c7ad7497e40ec)

#define IS\_PTR\_ALIGNED\_BYTES(ptr, bytes)

**Definition** common.h:198

[pbuf\_cfg](structpbuf__cfg.md)

Control block of packet buffer.

**Definition** pbuf.h:49

[pbuf](structpbuf.md)

Scure packed buffer.

**Definition** pbuf.h:96

Statically define and initialize pbuf.

Parameters
:   | name | Name of the pbuf. |
    | --- | --- |
    | mem\_addr | Memory address for pbuf. |
    | size | Size of the memory. |
    | dcache\_align | Data cache line size. |

## [◆ ](#ga00f201bb5e2e139272b2c32f9c3f6efc)PBUF\_HEADER\_OVERHEAD

| #define PBUF\_HEADER\_OVERHEAD | ( |  | *dcache\_align* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pbuf.h](pbuf_8h.md)>`

**Value:**

([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE)

Macro calculates memory overhead taken by the header in shared memory.

It contains the read index, write index and padding.

Parameters
:   | dcache\_align | Data cache alignment. |
    | --- | --- |

## [◆ ](#gaba4cc55b02db047bc2e0ca5c873b1222)PBUF\_MAYBE\_CONST

| #define PBUF\_MAYBE\_CONST   const |
| --- |

`#include <[pbuf.h](pbuf_8h.md)>`

## [◆ ](#gaa57dc50fdf97af6690ac784f0a4450be)PBUF\_PACKET\_LEN\_SZ

| #define PBUF\_PACKET\_LEN\_SZ   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) |
| --- |

`#include <[pbuf.h](pbuf_8h.md)>`

Size of packet length field.

## Function Documentation

## [◆ ](#ga44cc22d33d4ec7b7c95459e96ef7d7d0)pbuf\_read()

| int pbuf\_read | ( | struct [pbuf](structpbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[pbuf.h](pbuf_8h.md)>`

Read specified amount of data from the packet buffer.

Single read allows to read the message send by the single write. The provided p buf must be big enough to store the whole message.

Parameters
:   | pb | A buffer from which data will be read. |
    | --- | --- |
    | buf | Data pointer to which read data will be written. If NULL, len of stored message is returned. |
    | len | Number of bytes to be read from the buffer. |

Return values
:   | int | Bytes read, negative error code on fail. Bytes to be read, if buf == NULL. -EINVAL, if any of input parameter is incorrect. -ENOMEM, if message can not fit in provided buf. -EAGAIN, if not whole message is ready yet. |
    | --- | --- |

## [◆ ](#ga9da1179f5fd3e5238244cd2f7664a928)pbuf\_rx\_init()

| int pbuf\_rx\_init | ( | struct [pbuf](structpbuf.md) \* | *pb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pbuf.h](pbuf_8h.md)>`

Initialize the Rx packet buffer.

This function initializes the Rx packet buffer. If the configuration is incorrect, the function will return error.

It is recommended to use PBUF\_DEFINE macro for build time initialization.

Parameters
:   | pb | Pointer to the packed buffer containing configuration and data. Configuration has to be fixed before the initialization. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | when the input parameter is incorrect. |

## [◆ ](#ga05782e212932d84ba1192b4dbe1dfd42)pbuf\_tx\_init()

| int pbuf\_tx\_init | ( | struct [pbuf](structpbuf.md) \* | *pb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pbuf.h](pbuf_8h.md)>`

Initialize the Tx packet buffer.

This function initializes the Tx packet buffer based on provided configuration. If the configuration is incorrect, the function will return error.

It is recommended to use PBUF\_DEFINE macro for build time initialization.

Parameters
:   | pb | Pointer to the packed buffer containing configuration and data. Configuration has to be fixed before the initialization. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | when the input parameter is incorrect. |

## [◆ ](#ga9df9413dcd6268690a410c33126c081e)pbuf\_write()

| int pbuf\_write | ( | struct [pbuf](structpbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | const char \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[pbuf.h](pbuf_8h.md)>`

Write specified amount of data to the packet buffer.

This function call writes specified amount of data to the packet buffer if the buffer will fit the data.

Parameters
:   | pb | A buffer to which to write. |
    | --- | --- |
    | buf | Pointer to the data to be written to the buffer. |
    | len | Number of bytes to be written to the buffer. Must be positive. |

Return values
:   | int | Number of bytes written, negative error code on fail. -EINVAL, if any of input parameter is incorrect. -ENOMEM, if len is bigger than the buffer can fit. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
