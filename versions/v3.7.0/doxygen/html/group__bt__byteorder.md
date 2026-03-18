---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__byteorder.html
original_path: doxygen/html/group__bt__byteorder.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

## Detailed Description

Byteorder.

## Macro Definition Documentation

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
