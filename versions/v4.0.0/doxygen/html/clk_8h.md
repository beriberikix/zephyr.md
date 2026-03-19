---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clk_8h.html
original_path: doxygen/html/clk_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clk.h File Reference

SCMI clock protocol helpers.
[More...](#details)

`#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h_source.md)>`

[Go to the source code of this file.](clk_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_clock\_config](structscmi__clock__config.md) |
|  | Describes the parameters for the CLOCK\_CONFIG\_SET command. [More...](structscmi__clock__config.md#details) |

| Macros | |
| --- | --- |
| #define | [SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK](#a8b14e6d0d7329cb53c57ec21d241c3de)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| #define | [SCMI\_CLK\_CONFIG\_ENABLE\_DISABLE](#af797af4466ae90d17a58527f53d698ce)(x) |
| #define | [SCMI\_CLK\_ATTRIBUTES\_CLK\_NUM](#a9c2b446e167d9d5a903c55e4644d85ed)(x) |

| Enumerations | |
| --- | --- |
| enum | [scmi\_clock\_message](#a1f469b4773ddd8bcf07c9dc5c1319c1e) {     [SCMI\_CLK\_MSG\_PROTOCOL\_VERSION](#a1f469b4773ddd8bcf07c9dc5c1319c1eaca2f0a8361ee5dc916124025f6526607) = 0x0 , [SCMI\_CLK\_MSG\_PROTOCOL\_ATTRIBUTES](#a1f469b4773ddd8bcf07c9dc5c1319c1ea408af2dc0a8c4dca018bbf2631b7a516) = 0x1 , [SCMI\_CLK\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](#a1f469b4773ddd8bcf07c9dc5c1319c1eafbadc52b702794b36a42e033f7ddfc42) = 0x2 , [SCMI\_CLK\_MSG\_CLOCK\_ATTRIBUTES](#a1f469b4773ddd8bcf07c9dc5c1319c1ea4e3d5c2fdf920e72621b9bd20217d1c2) = 0x3 ,     [SCMI\_CLK\_MSG\_CLOCK\_DESCRIBE\_RATES](#a1f469b4773ddd8bcf07c9dc5c1319c1ea6551cd48e112cb0b839be88734865390) = 0x4 , [SCMI\_CLK\_MSG\_CLOCK\_RATE\_SET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea8b57e5ba159084a0f4567ef57666dda6) = 0x5 , [SCMI\_CLK\_MSG\_CLOCK\_RATE\_GET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea8ec4db9ccd6aea715001a41fcef20cd9) = 0x6 , [SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_SET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea97cc819e6d0a8ef184c137c1400ae059) = 0x7 ,     [SCMI\_CLK\_MSG\_CLOCK\_NAME\_GET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea0146f7bab4392d882f7b362976c78488) = 0x8 , [SCMI\_CLK\_MSG\_CLOCK\_RATE\_NOTIFY](#a1f469b4773ddd8bcf07c9dc5c1319c1eaadac9b02cf7136a3de2deb4139f8b891) = 0x9 , [SCMI\_CLK\_MSG\_CLOCK\_RATE\_CHANGE\_REQUESTED\_NOTIFY](#a1f469b4773ddd8bcf07c9dc5c1319c1ea2eaf16c90fcaf03d087ed2226c24f382) = 0xa , [SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_GET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea255aabcc89b96395c6e0db65054c7ee4) = 0xb ,     [SCMI\_CLK\_MSG\_CLOCK\_POSSIBLE\_PARENTS\_GET](#a1f469b4773ddd8bcf07c9dc5c1319c1ea895901f8e1ba97f961107ab21124df22) = 0xc , [SCMI\_CLK\_MSG\_CLOCK\_PARENT\_SET](#a1f469b4773ddd8bcf07c9dc5c1319c1eae5eedf089ea7fc08b49fd6a3086e79a9) = 0xd , [SCMI\_CLK\_MSG\_CLOCK\_PARENT\_GET](#a1f469b4773ddd8bcf07c9dc5c1319c1eaaa3979a8e0ad76b674f1bd02ee6ccfab) = 0xe , [SCMI\_CLK\_MSG\_CLOCK\_GET\_PERMISSIONS](#a1f469b4773ddd8bcf07c9dc5c1319c1eaf1de9a844e0d6ab5e840757d1f069957) = 0xf ,     [SCMI\_CLK\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](#a1f469b4773ddd8bcf07c9dc5c1319c1ea76ddf68387ac3dd18a014b20d5139495) = 0x10   } |
|  | Clock protocol command message IDs. [More...](#a1f469b4773ddd8bcf07c9dc5c1319c1e) |

| Functions | |
| --- | --- |
| int | [scmi\_clock\_protocol\_attributes](#ab4dd6c5aba4beea5e73679bbe96244cc) (struct [scmi\_protocol](structscmi__protocol.md) \*proto, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*attributes) |
|  | Send the PROTOCOL\_ATTRIBUTES command and get its reply. |
| int | [scmi\_clock\_config\_set](#ac9fe7f4275895fd9e6a7eada26012efb) (struct [scmi\_protocol](structscmi__protocol.md) \*proto, struct [scmi\_clock\_config](structscmi__clock__config.md) \*cfg) |
|  | Send the CLOCK\_CONFIG\_SET command and get its reply. |
| int | [scmi\_clock\_rate\_get](#ac69cff69cef158aebf5b40ba2c3c7bb4) (struct [scmi\_protocol](structscmi__protocol.md) \*proto, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clk\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Query the rate of a clock. |

## Detailed Description

SCMI clock protocol helpers.

## Macro Definition Documentation

## [◆ ](#a9c2b446e167d9d5a903c55e4644d85ed)SCMI\_CLK\_ATTRIBUTES\_CLK\_NUM

| #define SCMI\_CLK\_ATTRIBUTES\_CLK\_NUM | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0))

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:79

## [◆ ](#a8b14e6d0d7329cb53c57ec21d241c3de)SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK

| #define SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

## [◆ ](#af797af4466ae90d17a58527f53d698ce)SCMI\_CLK\_CONFIG\_ENABLE\_DISABLE

| #define SCMI\_CLK\_CONFIG\_ENABLE\_DISABLE | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(x) & [SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK](#a8b14e6d0d7329cb53c57ec21d241c3de))

[SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK](#a8b14e6d0d7329cb53c57ec21d241c3de)

#define SCMI\_CLK\_CONFIG\_DISABLE\_ENABLE\_MASK

**Definition** clk.h:17

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## Enumeration Type Documentation

## [◆ ](#a1f469b4773ddd8bcf07c9dc5c1319c1e)scmi\_clock\_message

| enum [scmi\_clock\_message](#a1f469b4773ddd8bcf07c9dc5c1319c1e) |
| --- |

Clock protocol command message IDs.

| Enumerator | |
| --- | --- |
| SCMI\_CLK\_MSG\_PROTOCOL\_VERSION |  |
| SCMI\_CLK\_MSG\_PROTOCOL\_ATTRIBUTES |  |
| SCMI\_CLK\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES |  |
| SCMI\_CLK\_MSG\_CLOCK\_ATTRIBUTES |  |
| SCMI\_CLK\_MSG\_CLOCK\_DESCRIBE\_RATES |  |
| SCMI\_CLK\_MSG\_CLOCK\_RATE\_SET |  |
| SCMI\_CLK\_MSG\_CLOCK\_RATE\_GET |  |
| SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_SET |  |
| SCMI\_CLK\_MSG\_CLOCK\_NAME\_GET |  |
| SCMI\_CLK\_MSG\_CLOCK\_RATE\_NOTIFY |  |
| SCMI\_CLK\_MSG\_CLOCK\_RATE\_CHANGE\_REQUESTED\_NOTIFY |  |
| SCMI\_CLK\_MSG\_CLOCK\_CONFIG\_GET |  |
| SCMI\_CLK\_MSG\_CLOCK\_POSSIBLE\_PARENTS\_GET |  |
| SCMI\_CLK\_MSG\_CLOCK\_PARENT\_SET |  |
| SCMI\_CLK\_MSG\_CLOCK\_PARENT\_GET |  |
| SCMI\_CLK\_MSG\_CLOCK\_GET\_PERMISSIONS |  |
| SCMI\_CLK\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION |  |

## Function Documentation

## [◆ ](#ac9fe7f4275895fd9e6a7eada26012efb)scmi\_clock\_config\_set()

| int scmi\_clock\_config\_set | ( | struct [scmi\_protocol](structscmi__protocol.md) \* | *proto*, |
| --- | --- | --- | --- |
|  |  | struct [scmi\_clock\_config](structscmi__clock__config.md) \* | *cfg* ) |

Send the CLOCK\_CONFIG\_SET command and get its reply.

Parameters
:   | proto | pointer to SCMI clock protocol data |
    | --- | --- |
    | cfg | pointer to structure containing configuration to be set |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ab4dd6c5aba4beea5e73679bbe96244cc)scmi\_clock\_protocol\_attributes()

| int scmi\_clock\_protocol\_attributes | ( | struct [scmi\_protocol](structscmi__protocol.md) \* | *proto*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *attributes* ) |

Send the PROTOCOL\_ATTRIBUTES command and get its reply.

Parameters
:   | proto | pointer to SCMI clock protocol data |
    | --- | --- |
    | attributes | pointer to attributes to be set via this command |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ac69cff69cef158aebf5b40ba2c3c7bb4)scmi\_clock\_rate\_get()

| int scmi\_clock\_rate\_get | ( | struct [scmi\_protocol](structscmi__protocol.md) \* | *proto*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *clk\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *rate* ) |

Query the rate of a clock.

Parameters
:   | proto | pointer to SCMI clock protocol data |
    | --- | --- |
    | clk\_id | ID of the clock for which the query is done |
    | rate | pointer to rate to be set via this command |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [clk.h](clk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
