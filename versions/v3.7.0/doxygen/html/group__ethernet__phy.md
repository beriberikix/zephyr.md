---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__ethernet__phy.html
original_path: doxygen/html/group__ethernet__phy.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet PHY Interface

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Ethernet PHY Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [phy\_link\_state](structphy__link__state.md) |
|  | Link state. [More...](structphy__link__state.md#details) |

| Macros | |
| --- | --- |
| #define | [PHY\_LINK\_IS\_FULL\_DUPLEX](#ga7dcf0d74db291bf0922c8ceb34307558)(x) |
|  | Check if phy link is full duplex. |
| #define | [PHY\_LINK\_IS\_SPEED\_1000M](#ga49f0673ace36bb3bac3e0c820a1f4de0)(x) |
|  | Check if phy link speed is 1 Gbit/sec. |
| #define | [PHY\_LINK\_IS\_SPEED\_100M](#ga35acfd5ebec25784cc1c5b6be7be6a05)(x) |
|  | Check if phy link speed is 100 Mbit/sec. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4)) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | Define the callback function signature for [phy\_link\_callback\_set()](#ga0ede85fdd6efd8c3520d7baf18d04a68) function. |

| Enumerations | |
| --- | --- |
| enum | [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) {     [LINK\_HALF\_10BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68a3010bbc6bde6ae12b39393ab34ed6c99) = BIT(0) , [LINK\_FULL\_10BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68a96d36b5ff474b1919288602cc1927842) = BIT(1) , [LINK\_HALF\_100BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68a165dfc46d79c06755d315c2d4033b629) = BIT(2) , [LINK\_FULL\_100BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68aa2b3167b8fb31ccbe3cd314aa82cf213) = BIT(3) ,     [LINK\_HALF\_1000BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68ad2b4a4c3ff8358685316c5f056a73d04) = BIT(4) , [LINK\_FULL\_1000BASE\_T](#gga9b97fff9fcd6823c9b564b3e86b8da68a72eec6d30279ddb51d7e9d6d7dabb611) = BIT(5)   } |
|  | Ethernet link speeds. [More...](#ga9b97fff9fcd6823c9b564b3e86b8da68) |

| Functions | |
| --- | --- |
| static int | [phy\_configure\_link](#gacb1e5d12f51106d481159d4b3e593e80) (const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds) |
|  | Configure PHY link. |
| static int | [phy\_get\_link\_state](#ga4d073c152ad4b6f5745db4f6d8477345) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get PHY link state. |
| static int | [phy\_link\_callback\_set](#ga0ede85fdd6efd8c3520d7baf18d04a68) (const struct [device](structdevice.md) \*dev, [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4) callback, void \*user\_data) |
|  | Set link state change callback. |
| static int | [phy\_read](#ga3fcca53d29981e23426b43d5340d8651) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Read PHY registers. |
| static int | [phy\_write](#ga520c049d830051ffa48708bb0dea429f) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Write PHY register. |

## Detailed Description

Ethernet PHY Interface.

## Macro Definition Documentation

## [◆ ](#ga7dcf0d74db291bf0922c8ceb34307558)PHY\_LINK\_IS\_FULL\_DUPLEX

| #define PHY\_LINK\_IS\_FULL\_DUPLEX | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

**Value:**

(x & ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Check if phy link is full duplex.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is full duplex, false if not.

## [◆ ](#ga49f0673ace36bb3bac3e0c820a1f4de0)PHY\_LINK\_IS\_SPEED\_1000M

| #define PHY\_LINK\_IS\_SPEED\_1000M | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

**Value:**

(x & ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)))

Check if phy link speed is 1 Gbit/sec.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is 1 Gbit/sec, false if not.

## [◆ ](#ga35acfd5ebec25784cc1c5b6be7be6a05)PHY\_LINK\_IS\_SPEED\_100M

| #define PHY\_LINK\_IS\_SPEED\_100M | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

**Value:**

(x & ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)))

Check if phy link speed is 100 Mbit/sec.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is 1 Mbit/sec, false if not.

## Typedef Documentation

## [◆ ](#ga3ee3db4ac48395f07d0de536b313dfa4)phy\_callback\_t

| typedef void(\* phy\_callback\_t) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
| --- |

`#include <[phy.h](phy_8h.md)>`

Define the callback function signature for [phy\_link\_callback\_set()](#ga0ede85fdd6efd8c3520d7baf18d04a68) function.

Parameters
:   | dev | PHY device structure |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Pointer to link\_state structure. |
    | user\_data | Pointer to data specified by user |

## Enumeration Type Documentation

## [◆ ](#ga9b97fff9fcd6823c9b564b3e86b8da68)phy\_link\_speed

| enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) |
| --- |

`#include <[phy.h](phy_8h.md)>`

Ethernet link speeds.

| Enumerator | |
| --- | --- |
| LINK\_HALF\_10BASE\_T | 10Base-T Half-Duplex |
| LINK\_FULL\_10BASE\_T | 10Base-T Full-Duplex |
| LINK\_HALF\_100BASE\_T | 100Base-T Half-Duplex |
| LINK\_FULL\_100BASE\_T | 100Base-T Full-Duplex |
| LINK\_HALF\_1000BASE\_T | 1000Base-T Half-Duplex |
| LINK\_FULL\_1000BASE\_T | 1000Base-T Full-Duplex |

## Function Documentation

## [◆ ](#gacb1e5d12f51106d481159d4b3e593e80)phy\_configure\_link()

| | int phy\_configure\_link | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) | *speeds* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

Configure PHY link.

This route configures the advertised link speeds.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | speeds | OR'd link speeds to be advertised by the PHY |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |
    | -ENOTSUP | If not supported. |

## [◆ ](#ga4d073c152ad4b6f5745db4f6d8477345)phy\_get\_link\_state()

| | int phy\_get\_link\_state | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [phy\_link\_state](structphy__link__state.md) \* | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

Get PHY link state.

Returns the current state of the PHY link. This can be used by to determine when a link is up and the negotiated link speed.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Pointer to receive PHY state |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga0ede85fdd6efd8c3520d7baf18d04a68)phy\_link\_callback\_set()

| | int phy\_link\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

Set link state change callback.

Sets a callback that is invoked when link state changes. This is the preferred method for ethernet drivers to be notified of the PHY link state change.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | callback | Callback handler |
    |  | user\_data | Pointer to data specified by user. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If not supported. |

## [◆ ](#ga3fcca53d29981e23426b43d5340d8651)phy\_read()

| | int phy\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_addr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

Read PHY registers.

This routine provides a generic interface to read from a PHY register.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | reg\_addr | Register address |
    |  | value | Pointer to receive read value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga520c049d830051ffa48708bb0dea429f)phy\_write()

| | int phy\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_addr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[phy.h](phy_8h.md)>`

Write PHY register.

This routine provides a generic interface to write to a PHY register.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | reg\_addr | Register address |
    | [in] | value | Value to write |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
