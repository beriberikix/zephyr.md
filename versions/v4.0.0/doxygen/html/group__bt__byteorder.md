---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__byteorder.html
original_path: doxygen/html/group__bt__byteorder.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Byteorder

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Byteorder.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_BYTES\_LIST\_LE16](#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_v) |
|  | Encode 16-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_LE24](#ga68d63372c0b7e981d7ae715250c42261)(\_v) |
|  | Encode 24-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_LE32](#ga0bf0275f0eea70eb5ae6002edeb1b812)(\_v) |
|  | Encode 32-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_LE40](#gadd963cf0f7898e5e143b5d2fd79839ef)(\_v) |
|  | Encode 40-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_LE48](#ga6211946252ccd004f8ed35addee462f6)(\_v) |
|  | Encode 48-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_LE64](#ga52500bb74dcf28535cb70823ce8aed18)(\_v) |
|  | Encode 64-bit value into array values in little-endian format. |
| #define | [BT\_BYTES\_LIST\_BE16](#ga50c0737d9c82bd8d86839614e5dc35f7)(\_v) |
|  | Encode 16-bit value into array values in big-endian format. |
| #define | [BT\_BYTES\_LIST\_BE24](#ga0c728bcd2941ef6d5c5b174dcede4f54)(\_v) |
|  | Encode 24-bit value into array values in big-endian format. |
| #define | [BT\_BYTES\_LIST\_BE32](#gab6ccd0fdb5f6d2d5214465037388f470)(\_v) |
|  | Encode 32-bit value into array values in big-endian format. |
| #define | [BT\_BYTES\_LIST\_BE40](#ga346b3e8d3b98fd7d532a191459f51a96)(\_v) |
|  | Encode 40-bit value into array values in big-endian format. |
| #define | [BT\_BYTES\_LIST\_BE48](#gad7af352ecb0f523fbd566adc1f04664a)(\_v) |
|  | Encode 48-bit value into array values in big-endian format. |
| #define | [BT\_BYTES\_LIST\_BE64](#gaec9f6617a3e8b10f381c6fa51a513593)(\_v) |
|  | Encode 64-bit value into array values in big-endian format. |

## Detailed Description

Byteorder.

## Macro Definition Documentation

## [◆ ](#ga50c0737d9c82bd8d86839614e5dc35f7)BT\_BYTES\_LIST\_BE16

| #define BT\_BYTES\_LIST\_BE16 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

(((\_v) >> 8) & 0xFFU), (((\_v) >> 0) & 0xFFU)

Encode 16-bit value into array values in big-endian format.

Helper macro to encode 16-bit values into comma separated values.

Note
:   `_v` is evaluated 2 times.

Parameters
:   | \_v | 16-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 16-bit value.

## [◆ ](#ga0c728bcd2941ef6d5c5b174dcede4f54)BT\_BYTES\_LIST\_BE24

| #define BT\_BYTES\_LIST\_BE24 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

(((\_v) >> 16) & 0xFFU), [BT\_BYTES\_LIST\_BE16](#ga50c0737d9c82bd8d86839614e5dc35f7)(\_v)

[BT\_BYTES\_LIST\_BE16](#ga50c0737d9c82bd8d86839614e5dc35f7)

#define BT\_BYTES\_LIST\_BE16(\_v)

Encode 16-bit value into array values in big-endian format.

**Definition** byteorder.h:120

Encode 24-bit value into array values in big-endian format.

Helper macro to encode 24-bit values into comma separated values.

Note
:   `_v` is evaluated 3 times.

Parameters
:   | \_v | 24-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 24-bit value.

## [◆ ](#gab6ccd0fdb5f6d2d5214465037388f470)BT\_BYTES\_LIST\_BE32

| #define BT\_BYTES\_LIST\_BE32 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

(((\_v) >> 24) & 0xFFU), [BT\_BYTES\_LIST\_BE24](#ga0c728bcd2941ef6d5c5b174dcede4f54)(\_v)

[BT\_BYTES\_LIST\_BE24](#ga0c728bcd2941ef6d5c5b174dcede4f54)

#define BT\_BYTES\_LIST\_BE24(\_v)

Encode 24-bit value into array values in big-endian format.

**Definition** byteorder.h:132

Encode 32-bit value into array values in big-endian format.

Helper macro to encode 32-bit values into comma separated values.

Note
:   `_v` is evaluated 4 times.

Parameters
:   | \_v | 32-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 32-bit value.

## [◆ ](#ga346b3e8d3b98fd7d532a191459f51a96)BT\_BYTES\_LIST\_BE40

| #define BT\_BYTES\_LIST\_BE40 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_BE16](#ga50c0737d9c82bd8d86839614e5dc35f7)((\_v) >> 24), [BT\_BYTES\_LIST\_BE24](#ga0c728bcd2941ef6d5c5b174dcede4f54)(\_v)

Encode 40-bit value into array values in big-endian format.

Helper macro to encode 40-bit values into comma separated values.

Note
:   `_v` is evaluated 5 times.

Parameters
:   | \_v | 40-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 40-bit value.

## [◆ ](#gad7af352ecb0f523fbd566adc1f04664a)BT\_BYTES\_LIST\_BE48

| #define BT\_BYTES\_LIST\_BE48 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_BE16](#ga50c0737d9c82bd8d86839614e5dc35f7)((\_v) >> 32), [BT\_BYTES\_LIST\_BE32](#gab6ccd0fdb5f6d2d5214465037388f470)(\_v)

[BT\_BYTES\_LIST\_BE32](#gab6ccd0fdb5f6d2d5214465037388f470)

#define BT\_BYTES\_LIST\_BE32(\_v)

Encode 32-bit value into array values in big-endian format.

**Definition** byteorder.h:144

Encode 48-bit value into array values in big-endian format.

Helper macro to encode 48-bit values into comma separated values.

Note
:   `_v` is evaluated 6 times.

Parameters
:   | \_v | 48-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 48-bit value.

## [◆ ](#gaec9f6617a3e8b10f381c6fa51a513593)BT\_BYTES\_LIST\_BE64

| #define BT\_BYTES\_LIST\_BE64 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_BE32](#gab6ccd0fdb5f6d2d5214465037388f470)((\_v) >> 32), [BT\_BYTES\_LIST\_BE32](#gab6ccd0fdb5f6d2d5214465037388f470)(\_v)

Encode 64-bit value into array values in big-endian format.

Helper macro to encode 64-bit values into comma separated values.

Note
:   `_v` is evaluated 8 times.

Parameters
:   | \_v | 64-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 64-bit value.

## [◆ ](#ga83b5828023306b4bbf354ca3d6d6c6f2)BT\_BYTES\_LIST\_LE16

| #define BT\_BYTES\_LIST\_LE16 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

(((\_v) >> 0) & 0xFFU), \

(((\_v) >> 8) & 0xFFU) \

Encode 16-bit value into array values in little-endian format.

Helper macro to encode 16-bit values into comma separated values.

Note
:   `_v` is evaluated 2 times.

Parameters
:   | \_v | 16-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 16-bit value.

## [◆ ](#ga68d63372c0b7e981d7ae715250c42261)BT\_BYTES\_LIST\_LE24

| #define BT\_BYTES\_LIST\_LE24 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE16](#ga83b5828023306b4bbf354ca3d6d6c6f2)(\_v), \

(((\_v) >> 16) & 0xFFU) \

[BT\_BYTES\_LIST\_LE16](#ga83b5828023306b4bbf354ca3d6d6c6f2)

#define BT\_BYTES\_LIST\_LE16(\_v)

Encode 16-bit value into array values in little-endian format.

**Definition** byteorder.h:36

Encode 24-bit value into array values in little-endian format.

Helper macro to encode 24-bit values into comma separated values.

Note
:   `_v` is evaluated 3 times.

Parameters
:   | \_v | 24-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 24-bit value.

## [◆ ](#ga0bf0275f0eea70eb5ae6002edeb1b812)BT\_BYTES\_LIST\_LE32

| #define BT\_BYTES\_LIST\_LE32 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE24](#ga68d63372c0b7e981d7ae715250c42261)(\_v), \

(((\_v) >> 24) & 0xFFU) \

[BT\_BYTES\_LIST\_LE24](#ga68d63372c0b7e981d7ae715250c42261)

#define BT\_BYTES\_LIST\_LE24(\_v)

Encode 24-bit value into array values in little-endian format.

**Definition** byteorder.h:50

Encode 32-bit value into array values in little-endian format.

Helper macro to encode 32-bit values into comma separated values.

Note
:   `_v` is evaluated 4 times.

Parameters
:   | \_v | 32-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 32-bit value.

## [◆ ](#gadd963cf0f7898e5e143b5d2fd79839ef)BT\_BYTES\_LIST\_LE40

| #define BT\_BYTES\_LIST\_LE40 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE24](#ga68d63372c0b7e981d7ae715250c42261)(\_v), \

BT\_BYTES\_LIST\_LE16((\_v) >> 24) \

Encode 40-bit value into array values in little-endian format.

Helper macro to encode 40-bit values into comma separated values.

Note
:   `_v` is evaluated 5 times.

Parameters
:   | \_v | 40-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 40-bit value.

## [◆ ](#ga6211946252ccd004f8ed35addee462f6)BT\_BYTES\_LIST\_LE48

| #define BT\_BYTES\_LIST\_LE48 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE32](#ga0bf0275f0eea70eb5ae6002edeb1b812)(\_v), \

BT\_BYTES\_LIST\_LE16((\_v) >> 32) \

[BT\_BYTES\_LIST\_LE32](#ga0bf0275f0eea70eb5ae6002edeb1b812)

#define BT\_BYTES\_LIST\_LE32(\_v)

Encode 32-bit value into array values in little-endian format.

**Definition** byteorder.h:64

Encode 48-bit value into array values in little-endian format.

Helper macro to encode 48-bit values into comma separated values.

Note
:   `_v` is evaluated 6 times.

Parameters
:   | \_v | 48-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 48-bit value.

## [◆ ](#ga52500bb74dcf28535cb70823ce8aed18)BT\_BYTES\_LIST\_LE64

| #define BT\_BYTES\_LIST\_LE64 | ( |  | *\_v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[byteorder.h](bluetooth_2byteorder_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE32](#ga0bf0275f0eea70eb5ae6002edeb1b812)(\_v), \

BT\_BYTES\_LIST\_LE32((\_v) >> 32) \

Encode 64-bit value into array values in little-endian format.

Helper macro to encode 64-bit values into comma separated values.

Note
:   `_v` is evaluated 8 times.

Parameters
:   | \_v | 64-bit integer in host endianness. |
    | --- | --- |

Returns
:   The comma separated values for the 64-bit value.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
