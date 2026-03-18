---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2logging_2log__core_8h.html
original_path: doxygen/html/include_2zephyr_2logging_2log__core_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_core.h File Reference

`#include <[zephyr/logging/log_msg.h](include_2zephyr_2logging_2log__msg_8h_source.md)>`  
`#include <[zephyr/logging/log_instance.h](log__instance_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2logging_2log__core_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOG\_LEVEL\_NONE](#a43dece650f96e7cf2a4e535c9bd4804a)   0U |
| #define | [LOG\_LEVEL\_ERR](#ab3a03740685cbdaa375e2bde8247fdc6)   1U |
| #define | [LOG\_LEVEL\_WRN](#a54f5db1327d9fdbaecbb03a6969de97b)   2U |
| #define | [LOG\_LEVEL\_INF](#a281bc2ce5315e6fae369796c0fdf5c1d)   3U |
| #define | [LOG\_LEVEL\_DBG](#ad1f7d41b1af28ba81ea63d24c9b690cc)   4U |
| #define | [CONFIG\_LOG\_DEFAULT\_LEVEL](#ac618493585bc226f18f36b6a2ad7e8d5)   0U |
| #define | [CONFIG\_LOG\_MAX\_LEVEL](#a97df309d4ec6704223193647b6faf819)   0U |
| #define | [LOG\_FUNCTION\_PREFIX\_MASK](#add313a51d2d73b99ad0d00fc5184312f) |
| #define | [LOG\_CURRENT\_MODULE\_ID](#a85c70bfd98bbc66a35806010a206237e)() |
|  | Macro for getting ID of current module. |
| #define | [LOG\_POINTERS\_VALIDATE](#a6d29de8e144ab8e57f42f096b0b47ca0)(string\_ok, ...) |
| #define | [LOG\_STRING\_WARNING](#ad9fb171d1afec420ff46f6e0e4b0481d)(\_mode, \_src, ...) |
| #define | [LOG\_LEVEL\_BITS](#a84474b9b8e31f5ee7040f7e22021c163)   3U |
|  | Number of bits used to encode log level. |
| #define | [LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)   [LOG\_LEVEL\_BITS](#a84474b9b8e31f5ee7040f7e22021c163) |
|  | Filter slot size. |
| #define | [LOG\_FILTERS\_NUM\_OF\_SLOTS](#ad7a2f00a0b9d7961f6f246b828ec8c63)   (32 / [LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)) |
|  | Number of slots in one word. |
| #define | [LOG\_FILTERS\_MAX\_BACKENDS](#a6258cbdcc73befb83fb5e5b5efd29d65)   ([LOG\_FILTERS\_NUM\_OF\_SLOTS](#ad7a2f00a0b9d7961f6f246b828ec8c63) - (1 + [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FRONTEND))) |
|  | Maximum number of backends supported when runtime filtering is enabled. |
| #define | [LOG\_FRONTEND\_SLOT\_ID](#ad3865db594c20dff3d20e02b954d7a51)   ([LOG\_FILTERS\_NUM\_OF\_SLOTS](#ad7a2f00a0b9d7961f6f246b828ec8c63) - 1) |
|  | Slot reserved for the frontend. |
| #define | [LOG\_FILTER\_SLOT\_MASK](#a6d1b6a2b8ac28915ac085d430a952a15)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)) - 1U) |
|  | Slot mask. |
| #define | [LOG\_FILTER\_SLOT\_SHIFT](#a5a21fea47b27e76f7382cf4cf687b4b3)(\_id) |
|  | Bit offset of a slot. |
| #define | [LOG\_FILTER\_SLOT\_GET](#a91e38e2a6e541df4bb8dbb741e393e0e)(\_filters, \_id) |
| #define | [LOG\_FILTER\_SLOT\_SET](#aa95cdf72ca0084ef4deed1cf698192d6)(\_filters, \_id, \_filter) |
| #define | [LOG\_FILTER\_AGGR\_SLOT\_IDX](#a3a875fb65e4f17a0b2d5cbc493084e34)   0 |
| #define | [LOG\_FILTER\_AGGR\_SLOT\_GET](#a4f4120cb018e563dea7005b10d5a6dc8)(\_filters) |
| #define | [LOG\_FILTER\_FIRST\_BACKEND\_SLOT\_IDX](#ab0f4745bf6824181306e2f71b3c9612e)   1 |
| #define | [LOG\_LEVEL\_INTERNAL\_RAW\_STRING](#a8be8b78ac80e9dd6bc8b9d3639942d33)   [LOG\_LEVEL\_NONE](#a43dece650f96e7cf2a4e535c9bd4804a) |
|  | Log level value used to indicate log entry that should not be formatted (raw string). |
| #define | [LOG\_ITEM\_DYNAMIC\_DATA](#a86c2e55bace38c6e71b4d1d0736b1160)(\_name) |
|  | Creates name of variable and section for runtime log data. |
| #define | [LOG\_INSTANCE\_DYNAMIC\_DATA](#a322351c9b30bf3328821c6358ddc6a0b)(\_module\_name, \_inst) |

| Functions | |
| --- | --- |
|  | [TYPE\_SECTION\_START\_EXTERN](#a8bddbf82fcd014a2b65b53d80312237d) (struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const) |
|  | [TYPE\_SECTION\_END\_EXTERN](#a9c76801a0e4d03e64c025f7cd5695d77) (struct [log\_source\_const\_data](structlog__source__const__data.md), log\_const) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_const\_source\_id](#add353f5f883b7edee6428adb7fb7e4d5) (const struct [log\_source\_const\_data](structlog__source__const__data.md) \*data) |
|  | Get index of the log source based on the address of the constant data associated with the source. |
|  | [TYPE\_SECTION\_START\_EXTERN](#aab9e9896eac3c3008df9f191e2dc46eb) (struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic) |
|  | [TYPE\_SECTION\_END\_EXTERN](#aa42f7911fae598d4b602b336cdf269b1) (struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md), log\_dynamic) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_dynamic\_source\_id](#ab2e628ee35c240d79a5e622fa1209008) (struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \*data) |
|  | Get index of the log source based on the address of the dynamic data associated with the source. |
| static void | [log\_generic](#ab81a1401935513819384b85948e3d09c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const char \*fmt, va\_list ap) |
|  | Write a generic log message. |

## Macro Definition Documentation

## [◆ ](#ac618493585bc226f18f36b6a2ad7e8d5)CONFIG\_LOG\_DEFAULT\_LEVEL

| #define CONFIG\_LOG\_DEFAULT\_LEVEL   0U |
| --- |

## [◆ ](#a97df309d4ec6704223193647b6faf819)CONFIG\_LOG\_MAX\_LEVEL

| #define CONFIG\_LOG\_MAX\_LEVEL   0U |
| --- |

## [◆ ](#a85c70bfd98bbc66a35806010a206237e)LOG\_CURRENT\_MODULE\_ID

| #define LOG\_CURRENT\_MODULE\_ID | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

(\_\_log\_level != 0 ? \

log\_const\_source\_id(\_\_log\_current\_const\_data) : 0U)

Macro for getting ID of current module.

## [◆ ](#a4f4120cb018e563dea7005b10d5a6dc8)LOG\_FILTER\_AGGR\_SLOT\_GET

| #define LOG\_FILTER\_AGGR\_SLOT\_GET | ( |  | *\_filters* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[LOG\_FILTER\_SLOT\_GET](#a91e38e2a6e541df4bb8dbb741e393e0e)(\_filters, [LOG\_FILTER\_AGGR\_SLOT\_IDX](#a3a875fb65e4f17a0b2d5cbc493084e34))

[LOG\_FILTER\_AGGR\_SLOT\_IDX](#a3a875fb65e4f17a0b2d5cbc493084e34)

#define LOG\_FILTER\_AGGR\_SLOT\_IDX

**Definition** log\_core.h:408

[LOG\_FILTER\_SLOT\_GET](#a91e38e2a6e541df4bb8dbb741e393e0e)

#define LOG\_FILTER\_SLOT\_GET(\_filters, \_id)

**Definition** log\_core.h:397

## [◆ ](#a3a875fb65e4f17a0b2d5cbc493084e34)LOG\_FILTER\_AGGR\_SLOT\_IDX

| #define LOG\_FILTER\_AGGR\_SLOT\_IDX   0 |
| --- |

## [◆ ](#ab0f4745bf6824181306e2f71b3c9612e)LOG\_FILTER\_FIRST\_BACKEND\_SLOT\_IDX

| #define LOG\_FILTER\_FIRST\_BACKEND\_SLOT\_IDX   1 |
| --- |

## [◆ ](#a91e38e2a6e541df4bb8dbb741e393e0e)LOG\_FILTER\_SLOT\_GET

| #define LOG\_FILTER\_SLOT\_GET | ( |  | *\_filters*, |
| --- | --- | --- | --- |
|  |  |  | *\_id* ) |

**Value:**

((\*(\_filters) >> [LOG\_FILTER\_SLOT\_SHIFT](#a5a21fea47b27e76f7382cf4cf687b4b3)(\_id)) & [LOG\_FILTER\_SLOT\_MASK](#a6d1b6a2b8ac28915ac085d430a952a15))

[LOG\_FILTER\_SLOT\_SHIFT](#a5a21fea47b27e76f7382cf4cf687b4b3)

#define LOG\_FILTER\_SLOT\_SHIFT(\_id)

Bit offset of a slot.

**Definition** log\_core.h:395

[LOG\_FILTER\_SLOT\_MASK](#a6d1b6a2b8ac28915ac085d430a952a15)

#define LOG\_FILTER\_SLOT\_MASK

Slot mask.

**Definition** log\_core.h:389

## [◆ ](#a6d1b6a2b8ac28915ac085d430a952a15)LOG\_FILTER\_SLOT\_MASK

| #define LOG\_FILTER\_SLOT\_MASK   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)) - 1U) |
| --- |

Slot mask.

## [◆ ](#aa95cdf72ca0084ef4deed1cf698192d6)LOG\_FILTER\_SLOT\_SET

| #define LOG\_FILTER\_SLOT\_SET | ( |  | *\_filters*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_filter* ) |

**Value:**

do { \

\*(\_filters) &= ~([LOG\_FILTER\_SLOT\_MASK](#a6d1b6a2b8ac28915ac085d430a952a15) << \

[LOG\_FILTER\_SLOT\_SHIFT](#a5a21fea47b27e76f7382cf4cf687b4b3)(\_id)); \

\*(\_filters) |= ((\_filter) & [LOG\_FILTER\_SLOT\_MASK](#a6d1b6a2b8ac28915ac085d430a952a15)) << \

LOG\_FILTER\_SLOT\_SHIFT(\_id); \

} while (false)

## [◆ ](#a5a21fea47b27e76f7382cf4cf687b4b3)LOG\_FILTER\_SLOT\_SHIFT

| #define LOG\_FILTER\_SLOT\_SHIFT | ( |  | *\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd) \* (\_id))

[LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)

#define LOG\_FILTER\_SLOT\_SIZE

Filter slot size.

**Definition** log\_core.h:376

Bit offset of a slot.

Parameters
:   | \_id | Slot ID. |
    | --- | --- |

## [◆ ](#a31c9e4a93ba2527b3bce4e5461dd65dd)LOG\_FILTER\_SLOT\_SIZE

| #define LOG\_FILTER\_SLOT\_SIZE   [LOG\_LEVEL\_BITS](#a84474b9b8e31f5ee7040f7e22021c163) |
| --- |

Filter slot size.

## [◆ ](#a6258cbdcc73befb83fb5e5b5efd29d65)LOG\_FILTERS\_MAX\_BACKENDS

| #define LOG\_FILTERS\_MAX\_BACKENDS   ([LOG\_FILTERS\_NUM\_OF\_SLOTS](#ad7a2f00a0b9d7961f6f246b828ec8c63) - (1 + [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FRONTEND))) |
| --- |

Maximum number of backends supported when runtime filtering is enabled.

## [◆ ](#ad7a2f00a0b9d7961f6f246b828ec8c63)LOG\_FILTERS\_NUM\_OF\_SLOTS

| #define LOG\_FILTERS\_NUM\_OF\_SLOTS   (32 / [LOG\_FILTER\_SLOT\_SIZE](#a31c9e4a93ba2527b3bce4e5461dd65dd)) |
| --- |

Number of slots in one word.

## [◆ ](#ad3865db594c20dff3d20e02b954d7a51)LOG\_FRONTEND\_SLOT\_ID

| #define LOG\_FRONTEND\_SLOT\_ID   ([LOG\_FILTERS\_NUM\_OF\_SLOTS](#ad7a2f00a0b9d7961f6f246b828ec8c63) - 1) |
| --- |

Slot reserved for the frontend.

Last slot is used.

## [◆ ](#add313a51d2d73b99ad0d00fc5184312f)LOG\_FUNCTION\_PREFIX\_MASK

| #define LOG\_FUNCTION\_PREFIX\_MASK |
| --- |

**Value:**

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_ERR) << \

[LOG\_LEVEL\_ERR](#ab3a03740685cbdaa375e2bde8247fdc6)) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_WRN) << \

[LOG\_LEVEL\_WRN](#a54f5db1327d9fdbaecbb03a6969de97b)) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_INF) << \

[LOG\_LEVEL\_INF](#a281bc2ce5315e6fae369796c0fdf5c1d)) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FUNC\_NAME\_PREFIX\_DBG) << [LOG\_LEVEL\_DBG](#ad1f7d41b1af28ba81ea63d24c9b690cc)))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[LOG\_LEVEL\_INF](#a281bc2ce5315e6fae369796c0fdf5c1d)

#define LOG\_LEVEL\_INF

**Definition** log\_core.h:22

[LOG\_LEVEL\_WRN](#a54f5db1327d9fdbaecbb03a6969de97b)

#define LOG\_LEVEL\_WRN

**Definition** log\_core.h:21

[LOG\_LEVEL\_ERR](#ab3a03740685cbdaa375e2bde8247fdc6)

#define LOG\_LEVEL\_ERR

**Definition** log\_core.h:20

[LOG\_LEVEL\_DBG](#ad1f7d41b1af28ba81ea63d24c9b690cc)

#define LOG\_LEVEL\_DBG

**Definition** log\_core.h:23

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#a322351c9b30bf3328821c6358ddc6a0b)LOG\_INSTANCE\_DYNAMIC\_DATA

| #define LOG\_INSTANCE\_DYNAMIC\_DATA | ( |  | *\_module\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_inst* ) |

**Value:**

[LOG\_ITEM\_DYNAMIC\_DATA](#a86c2e55bace38c6e71b4d1d0736b1160)(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst))

[LOG\_ITEM\_DYNAMIC\_DATA](#a86c2e55bace38c6e71b4d1d0736b1160)

#define LOG\_ITEM\_DYNAMIC\_DATA(\_name)

Creates name of variable and section for runtime log data.

**Definition** log\_core.h:478

## [◆ ](#a86c2e55bace38c6e71b4d1d0736b1160)LOG\_ITEM\_DYNAMIC\_DATA

| #define LOG\_ITEM\_DYNAMIC\_DATA | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(log\_dynamic\_, \_name)

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Creates name of variable and section for runtime log data.

Parameters
:   | \_name | Name. |
    | --- | --- |

## [◆ ](#a84474b9b8e31f5ee7040f7e22021c163)LOG\_LEVEL\_BITS

| #define LOG\_LEVEL\_BITS   3U |
| --- |

Number of bits used to encode log level.

## [◆ ](#ad1f7d41b1af28ba81ea63d24c9b690cc)LOG\_LEVEL\_DBG

| #define LOG\_LEVEL\_DBG   4U |
| --- |

## [◆ ](#ab3a03740685cbdaa375e2bde8247fdc6)LOG\_LEVEL\_ERR

| #define LOG\_LEVEL\_ERR   1U |
| --- |

## [◆ ](#a281bc2ce5315e6fae369796c0fdf5c1d)LOG\_LEVEL\_INF

| #define LOG\_LEVEL\_INF   3U |
| --- |

## [◆ ](#a8be8b78ac80e9dd6bc8b9d3639942d33)LOG\_LEVEL\_INTERNAL\_RAW\_STRING

| #define LOG\_LEVEL\_INTERNAL\_RAW\_STRING   [LOG\_LEVEL\_NONE](#a43dece650f96e7cf2a4e535c9bd4804a) |
| --- |

Log level value used to indicate log entry that should not be formatted (raw string).

## [◆ ](#a43dece650f96e7cf2a4e535c9bd4804a)LOG\_LEVEL\_NONE

| #define LOG\_LEVEL\_NONE   0U |
| --- |

## [◆ ](#a54f5db1327d9fdbaecbb03a6969de97b)LOG\_LEVEL\_WRN

| #define LOG\_LEVEL\_WRN   2U |
| --- |

## [◆ ](#a6d29de8e144ab8e57f42f096b0b47ca0)LOG\_POINTERS\_VALIDATE

| #define LOG\_POINTERS\_VALIDATE | ( |  | *string\_ok*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

string\_ok = true

## [◆ ](#ad9fb171d1afec420ff46f6e0e4b0481d)LOG\_STRING\_WARNING

| #define LOG\_STRING\_WARNING | ( |  | *\_mode*, |
| --- | --- | --- | --- |
|  |  |  | *\_src*, |
|  |  |  | ... ) |

## Function Documentation

## [◆ ](#add353f5f883b7edee6428adb7fb7e4d5)log\_const\_source\_id()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_const\_source\_id | ( | const struct [log\_source\_const\_data](structlog__source__const__data.md) \* | *data* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get index of the log source based on the address of the constant data associated with the source.

Parameters
:   | data | Address of the constant data. |
    | --- | --- |

Returns
:   Source ID.

## [◆ ](#ab2e628ee35c240d79a5e622fa1209008)log\_dynamic\_source\_id()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_dynamic\_source\_id | ( | struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \* | *data* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get index of the log source based on the address of the dynamic data associated with the source.

Parameters
:   | data | Address of the dynamic data. |
    | --- | --- |

Returns
:   Source ID.

## [◆ ](#ab81a1401935513819384b85948e3d09c)log\_generic()

| | void log\_generic | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level*, | | --- | --- | --- | --- | |  |  | const char \* | *fmt*, | |  |  | va\_list | *ap* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write a generic log message.

Note
:   This function is intended to be used when porting other log systems.

Parameters
:   | level | Log level.. |
    | --- | --- |
    | fmt | String to format. |
    | ap | Pointer to arguments list. |

## [◆ ](#a9c76801a0e4d03e64c025f7cd5695d77)TYPE\_SECTION\_END\_EXTERN() [1/2]

| TYPE\_SECTION\_END\_EXTERN | ( | struct [log\_source\_const\_data](structlog__source__const__data.md) | , |
| --- | --- | --- | --- |
|  |  | log\_const | ) |

## [◆ ](#aa42f7911fae598d4b602b336cdf269b1)TYPE\_SECTION\_END\_EXTERN() [2/2]

| TYPE\_SECTION\_END\_EXTERN | ( | struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) | , |
| --- | --- | --- | --- |
|  |  | log\_dynamic | ) |

## [◆ ](#a8bddbf82fcd014a2b65b53d80312237d)TYPE\_SECTION\_START\_EXTERN() [1/2]

| TYPE\_SECTION\_START\_EXTERN | ( | struct [log\_source\_const\_data](structlog__source__const__data.md) | , |
| --- | --- | --- | --- |
|  |  | log\_const | ) |

## [◆ ](#aab9e9896eac3c3008df9f191e2dc46eb)TYPE\_SECTION\_START\_EXTERN() [2/2]

| TYPE\_SECTION\_START\_EXTERN | ( | struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) | , |
| --- | --- | --- | --- |
|  |  | log\_dynamic | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_core.h](include_2zephyr_2logging_2log__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
