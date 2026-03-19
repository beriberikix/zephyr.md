---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ring__buffer__apis.html
original_path: doxygen/html/group__ring__buffer__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ring Buffer APIs

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Simple ring buffer implementation.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ring\_buf](structring__buf.md) |
|  | A structure to represent a ring buffer. [More...](structring__buf.md#details) |

| Macros | |
| --- | --- |
| #define | [RING\_BUF\_INIT](#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)(buf, size8) |
| #define | [RING\_BUF\_DECLARE](#ga803e45abf48ee207fc0ab4028726a82b)(name, size8) |
|  | Define and initialize a ring buffer for byte data. |
| #define | [RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d)(name, size32) |
|  | Define and initialize an "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_DECLARE\_SIZE](#ga205e93b5431112da0d191526906c7e01)(name, size32) |
|  | Define and initialize an "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_DECLARE\_POW2](#gaca98f407b222dff12e2bbfcf3746a9e3)(name, pow) |
|  | Define and initialize a power-of-2 sized "item based" ring buffer. |
| #define | [RING\_BUF\_ITEM\_SIZEOF](#ga60451a56ed9b742abfa8e75ca320b004)(expr) |
|  | Compute the ring buffer size in 32-bit needed to store an element. |

| Functions | |
| --- | --- |
| static void | [ring\_buf\_init](#gac06bc272bf99843c65bf28d851bffd55) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Initialize a ring buffer for byte data. |
| static void | [ring\_buf\_item\_init](#ga9d10210160544af25c9a67680aff578d) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Initialize an "item based" ring buffer. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ring\_buf\_is\_empty](#gabb7006d786b1ddc640b5fd2338d1d01c) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine if a ring buffer is empty. |
| static void | [ring\_buf\_reset](#ga9cc0cd445eeeeba7183c3ac0778c7e18) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Reset ring buffer state. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_space\_get](#ga0db0b939d2be3d3fb0688f55780379bb) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine free space in a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_item\_space\_get](#gab58be76e8d3fc5542fb7b03717b89544) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine free space in an "item based" ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_capacity\_get](#ga9c06a3c6f77584ce8317a236cc2de35c) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Return ring buffer capacity. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_size\_get](#gade647873dd72c04a54f51b8d9d335107) (struct [ring\_buf](structring__buf.md) \*buf) |
|  | Determine used space in a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_put\_claim](#ga0381d9c6413d78b9226d32532ef523eb) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Allocate buffer for writing data to a ring buffer. |
| static int | [ring\_buf\_put\_finish](#gaf910aa666eac329813a55db732a21bd8) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Indicate number of bytes written to allocated buffers. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_put](#ga6c7e76e3ca798e994f738d114cb9a7e3) (struct [ring\_buf](structring__buf.md) \*buf, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Write (copy) data to a ring buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_get\_claim](#gad7cd6e1fe8e47ab7f6d9c42b87581f19) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Get address of a valid data in a ring buffer. |
| static int | [ring\_buf\_get\_finish](#ga8ea8ad9949bffd0d6f9b0785e18a6378) (struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Indicate number of bytes read from claimed buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_get](#ga209bef22c47f3938a36d7eb6c3b3dbc7) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Read data from a ring buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ring\_buf\_peek](#ga8ba75a313b2ad7d55e390fa3f1fcadc1) (struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Peek at data from a ring buffer. |
| int | [ring\_buf\_item\_put](#ga6cb71d7c1a36b6e142b251f08ed40599) (struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size32) |
|  | Write a data item to a ring buffer. |
| int | [ring\_buf\_item\_get](#gae0c62af11cab8a661638e50b312b58f8) (struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size32) |
|  | Read a data item from a ring buffer. |

## Detailed Description

Simple ring buffer implementation.

## Macro Definition Documentation

## [◆ ](#ga803e45abf48ee207fc0ab4028726a82b)RING\_BUF\_DECLARE

| #define RING\_BUF\_DECLARE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *size8* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

BUILD\_ASSERT(size8 < RING\_BUFFER\_MAX\_SIZE,\

RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_\_noinit \_ring\_buffer\_data\_##name[size8]; \

struct [ring\_buf](structring__buf.md) name = [RING\_BUF\_INIT](#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)(\_ring\_buffer\_data\_##name, size8)

[RING\_BUF\_INIT](#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)

#define RING\_BUF\_INIT(buf, size8)

**Definition** ring\_buffer.h:72

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:43

Define and initialize a ring buffer for byte data.

This macro establishes a ring buffer of an arbitrary size. The basic storage unit is a byte.

The ring buffer can be accessed outside the module where it is defined using:

extern struct [ring\_buf](structring__buf.md) <name>;

Parameters
:   | name | Name of the ring buffer. |
    | --- | --- |
    | size8 | Size of ring buffer (in bytes). |

## [◆ ](#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)RING\_BUF\_INIT

| #define RING\_BUF\_INIT | ( |  | *buf*, |
| --- | --- | --- | --- |
|  |  |  | *size8* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

{ \

.buffer = buf, \

.size = size8, \

}

## [◆ ](#ga2fc2f4515121ac6bbf6aebf3e029bb5d)RING\_BUF\_ITEM\_DECLARE

| #define RING\_BUF\_ITEM\_DECLARE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *size32* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

BUILD\_ASSERT((size32) < RING\_BUFFER\_MAX\_SIZE / 4,\

RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_\_noinit \_ring\_buffer\_data\_##name[size32]; \

struct [ring\_buf](structring__buf.md) name = { \

.buffer = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) \_ring\_buffer\_data\_##name, \

.size = 4 \* (size32) \

}

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Define and initialize an "item based" ring buffer.

This macro establishes an "item based" ring buffer. Each data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

The ring buffer can be accessed outside the module where it is defined using:

extern struct [ring\_buf](structring__buf.md) <name>;

Parameters
:   | name | Name of the ring buffer. |
    | --- | --- |
    | size32 | Size of ring buffer (in 32-bit words). |

## [◆ ](#gaca98f407b222dff12e2bbfcf3746a9e3)RING\_BUF\_ITEM\_DECLARE\_POW2

| #define RING\_BUF\_ITEM\_DECLARE\_POW2 | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *pow* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

[RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d)(name, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pow))

[RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d)

#define RING\_BUF\_ITEM\_DECLARE(name, size32)

Define and initialize an "item based" ring buffer.

**Definition** ring\_buffer.h:113

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Define and initialize a power-of-2 sized "item based" ring buffer.

This macro establishes an "item based" ring buffer by specifying its size using a power of 2. This exists mainly for backward compatibility reasons. [RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d) should be used instead.

Parameters
:   | name | Name of the ring buffer. |
    | --- | --- |
    | pow | Ring buffer size exponent. |

## [◆ ](#ga205e93b5431112da0d191526906c7e01)RING\_BUF\_ITEM\_DECLARE\_SIZE

| #define RING\_BUF\_ITEM\_DECLARE\_SIZE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *size32* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

[RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d)(name, size32)

Define and initialize an "item based" ring buffer.

This exists for backward compatibility reasons. [RING\_BUF\_ITEM\_DECLARE](#ga2fc2f4515121ac6bbf6aebf3e029bb5d) should be used instead.

Parameters
:   | name | Name of the ring buffer. |
    | --- | --- |
    | size32 | Size of ring buffer (in 32-bit words). |

## [◆ ](#ga60451a56ed9b742abfa8e75ca320b004)RING\_BUF\_ITEM\_SIZEOF

| #define RING\_BUF\_ITEM\_SIZEOF | ( |  | *expr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

**Value:**

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(sizeof(expr), sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

Compute the ring buffer size in 32-bit needed to store an element.

The argument can be a type or an expression. Note: rounds up if the size is not a multiple of 32 bits.

Parameters
:   | expr | Expression or type to compute the size of |
    | --- | --- |

## Function Documentation

## [◆ ](#ga9c06a3c6f77584ce8317a236cc2de35c)ring\_buf\_capacity\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_capacity\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Return ring buffer capacity.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

Returns
:   Ring buffer capacity (in bytes).

## [◆ ](#ga209bef22c47f3938a36d7eb6c3b3dbc7)ring\_buf\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Read data from a ring buffer.

This routine reads data from a ring buffer *buf*.

Warning
:   Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.
:   Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | data | Address of the output buffer. Can be NULL to discard data. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written to the output buffer. |
    | --- | --- |

## [◆ ](#gad7cd6e1fe8e47ab7f6d9c42b87581f19)ring\_buf\_get\_claim()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_get\_claim | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Get address of a valid data in a ring buffer.

With this routine, memory copying can be reduced since internal ring buffer can be used directly by the user. Once data is processed it must be freed using [ring\_buf\_get\_finish](#ga8ea8ad9949bffd0d6f9b0785e18a6378).

Warning
:   Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.
:   Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

Parameters
:   | [in] | buf | Address of ring buffer. |
    | --- | --- | --- |
    | [out] | data | Pointer to the address. It is set to a location within ring buffer. |
    | [in] | size | Requested size (in bytes). |

Returns
:   Number of valid bytes in the provided buffer which can be smaller than requested if there is not enough free space or buffer wraps.

## [◆ ](#ga8ea8ad9949bffd0d6f9b0785e18a6378)ring\_buf\_get\_finish()

| | int ring\_buf\_get\_finish | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Indicate number of bytes read from claimed buffer.

The number of bytes must be equal or lower than the sum corresponding to all preceding [ring\_buf\_get\_claim](#gad7cd6e1fe8e47ab7f6d9c42b87581f19) invocations (or even 0). Surplus bytes will remain available in the buffer.

Warning
:   Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.
:   Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | size | Number of bytes that can be freed. |

Return values
:   | 0 | Successful operation. |
    | --- | --- |
    | -EINVAL | Provided *size* exceeds valid bytes in the ring buffer. |

## [◆ ](#gac06bc272bf99843c65bf28d851bffd55)ring\_buf\_init()

| | void ring\_buf\_init | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Initialize a ring buffer for byte data.

This routine initializes a ring buffer, prior to its first use. It is only used for ring buffers not defined using RING\_BUF\_DECLARE.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | size | Ring buffer size (in bytes). |
    | data | Ring buffer data area ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[size]). |

## [◆ ](#gabb7006d786b1ddc640b5fd2338d1d01c)ring\_buf\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ring\_buf\_is\_empty | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Determine if a ring buffer is empty.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

Returns
:   true if the ring buffer is empty, or false if not.

## [◆ ](#gae0c62af11cab8a661638e50b312b58f8)ring\_buf\_item\_get()

| int ring\_buf\_item\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *size32* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Read a data item from a ring buffer.

This routine reads a data item from ring buffer *buf*. The data item is an array of 32-bit words (up to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

Warning
:   Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | type | Area to store the data item's type identifier. |
    | value | Area to store the data item's integer value. |
    | data | Area to store the data item. Can be NULL to discard data. |
    | size32 | Size of the data item storage area (number of 32-bit chunks). |

Return values
:   | 0 | Data item was fetched; *size32* now contains the number of 32-bit words read into data area *data*. |
    | --- | --- |
    | -EAGAIN | Ring buffer is empty. |
    | -EMSGSIZE | Data area *data* is too small; *size32* now contains the number of 32-bit words needed. |

## [◆ ](#ga9d10210160544af25c9a67680aff578d)ring\_buf\_item\_init()

| | void ring\_buf\_item\_init | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Initialize an "item based" ring buffer.

This routine initializes a ring buffer, prior to its first use. It is only used for ring buffers not defined using RING\_BUF\_ITEM\_DECLARE.

Each data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | size | Ring buffer size (in 32-bit words) |
    | data | Ring buffer data area ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data[size]). |

## [◆ ](#ga6cb71d7c1a36b6e142b251f08ed40599)ring\_buf\_item\_put()

| int ring\_buf\_item\_put | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size32* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Write a data item to a ring buffer.

This routine writes a data item to ring buffer *buf*. The data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

Warning
:   Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | type | Data item's type identifier (application specific). |
    | value | Data item's integer value (application specific). |
    | data | Address of data item. |
    | size32 | Data item size (number of 32-bit words). |

Return values
:   | 0 | Data item was written. |
    | --- | --- |
    | -EMSGSIZE | Ring buffer has insufficient free space. |

## [◆ ](#gab58be76e8d3fc5542fb7b03717b89544)ring\_buf\_item\_space\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_item\_space\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Determine free space in an "item based" ring buffer.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

Returns
:   Ring buffer free space (in 32-bit words).

## [◆ ](#ga8ba75a313b2ad7d55e390fa3f1fcadc1)ring\_buf\_peek()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_peek | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Peek at data from a ring buffer.

This routine reads data from a ring buffer *buf* without removal.

Warning
:   Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.
:   Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).
:   Multiple calls to peek will result in the same data being 'peeked' multiple times. To remove data, use either [ring\_buf\_get](#ga209bef22c47f3938a36d7eb6c3b3dbc7) or [ring\_buf\_get\_claim](#gad7cd6e1fe8e47ab7f6d9c42b87581f19) followed by [ring\_buf\_get\_finish](#ga8ea8ad9949bffd0d6f9b0785e18a6378) with a non-zero size.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | data | Address of the output buffer. Cannot be NULL. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written to the output buffer. |
    | --- | --- |

## [◆ ](#ga6c7e76e3ca798e994f738d114cb9a7e3)ring\_buf\_put()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_put | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Write (copy) data to a ring buffer.

This routine writes data to a ring buffer *buf*.

Warning
:   Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.
:   Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | data | Address of data. |
    | size | Data size (in bytes). |

Return values
:   | Number | of bytes written. |
    | --- | --- |

## [◆ ](#ga0381d9c6413d78b9226d32532ef523eb)ring\_buf\_put\_claim()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_put\_claim | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Allocate buffer for writing data to a ring buffer.

With this routine, memory copying can be reduced since internal ring buffer can be used directly by the user. Once data is written to allocated area number of bytes written must be confirmed (see [ring\_buf\_put\_finish](#gaf910aa666eac329813a55db732a21bd8)).

Warning
:   Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.
:   Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

Parameters
:   | [in] | buf | Address of ring buffer. |
    | --- | --- | --- |
    | [out] | data | Pointer to the address. It is set to a location within ring buffer. |
    | [in] | size | Requested allocation size (in bytes). |

Returns
:   Size of allocated buffer which can be smaller than requested if there is not enough free space or buffer wraps.

## [◆ ](#gaf910aa666eac329813a55db732a21bd8)ring\_buf\_put\_finish()

| | int ring\_buf\_put\_finish | ( | struct [ring\_buf](structring__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Indicate number of bytes written to allocated buffers.

The number of bytes must be equal to or lower than the sum corresponding to all preceding [ring\_buf\_put\_claim](#ga0381d9c6413d78b9226d32532ef523eb) invocations (or even 0). Surplus bytes will be returned to the available free buffer space.

Warning
:   Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.
:   Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |
    | size | Number of valid bytes in the allocated buffers. |

Return values
:   | 0 | Successful operation. |
    | --- | --- |
    | -EINVAL | Provided *size* exceeds free space in the ring buffer. |

## [◆ ](#ga9cc0cd445eeeeba7183c3ac0778c7e18)ring\_buf\_reset()

| | void ring\_buf\_reset | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Reset ring buffer state.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

## [◆ ](#gade647873dd72c04a54f51b8d9d335107)ring\_buf\_size\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_size\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Determine used space in a ring buffer.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

Returns
:   Ring buffer space used (in bytes).

## [◆ ](#ga0db0b939d2be3d3fb0688f55780379bb)ring\_buf\_space\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_space\_get | ( | struct [ring\_buf](structring__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ring_buffer.h](ring__buffer_8h.md)>`

Determine free space in a ring buffer.

Parameters
:   | buf | Address of ring buffer. |
    | --- | --- |

Returns
:   Ring buffer free space (in bytes).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
