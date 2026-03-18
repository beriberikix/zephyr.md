---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__rtio__cqe__flags.html
original_path: doxygen/html/group__rtio__cqe__flags.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTIO CQE Flags

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

RTIO CQE Flags.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](#ga0f212500447a5e37e225a6997953b609)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | The entry's buffer was allocated from the RTIO's mempool. |
| #define | [RTIO\_CQE\_FLAG\_GET](#gaef64ea020a20ac22a0edcb6eca032efc)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](#ga0b5f3f7e7be472ecf87bd2b08c1888da)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get the block index of a mempool flags. |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](#ga087465f866d417d5332602bb582cc1a7)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get the block count of a mempool flags. |
| #define | [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](#ga28b3a5661248b6b3763aab47417114d6)(blk\_idx, blk\_cnt) |
|  | Prepare CQE flags for a mempool read. |

## Detailed Description

RTIO CQE Flags.

## Macro Definition Documentation

## [◆ ](#gaef64ea020a20ac22a0edcb6eca032efc)RTIO\_CQE\_FLAG\_GET

| #define RTIO\_CQE\_FLAG\_GET | ( |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:70

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

Extract a bitfield element from value corresponding to the field mask mask.

**Definition** util.h:87

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

## [◆ ](#ga0f212500447a5e37e225a6997953b609)RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER

| #define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The entry's buffer was allocated from the RTIO's mempool.

If this bit is set, the buffer was allocated from the memory pool and should be recycled as soon as the application is done with it.

## [◆ ](#ga087465f866d417d5332602bb582cc1a7)RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT

| #define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT | ( |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 20), ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

Get the block count of a mempool flags.

Parameters
:   | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | The CQE flags value |
    | --- | --- |

Returns
:   The block count portion of the flags field.

## [◆ ](#ga0b5f3f7e7be472ecf87bd2b08c1888da)RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX

| #define RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX | ( |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

[FIELD\_GET](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 8), ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

Get the block index of a mempool flags.

Parameters
:   | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | The CQE flags value |
    | --- | --- |

Returns
:   The block index portion of the flags field.

## [◆ ](#ga28b3a5661248b6b3763aab47417114d6)RTIO\_CQE\_FLAG\_PREP\_MEMPOOL

| #define RTIO\_CQE\_FLAG\_PREP\_MEMPOOL | ( |  | *blk\_idx*, |
| --- | --- | --- | --- |
|  |  |  | *blk\_cnt* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

([FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](#ga0f212500447a5e37e225a6997953b609)) | \

FIELD\_PREP([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 8), blk\_idx) | [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 20), blk\_cnt))

[RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](#ga0f212500447a5e37e225a6997953b609)

#define RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER

The entry's buffer was allocated from the RTIO's mempool.

**Definition** rtio.h:160

[FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

Prepare a bitfield element using value with mask representing its field position and width.

**Definition** util.h:94

Prepare CQE flags for a mempool read.

Parameters
:   | blk\_idx | The mempool block index |
    | --- | --- |
    | blk\_cnt | The mempool block count |

Returns
:   A shifted and masked value that can be added to the flags field with an OR operator.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
