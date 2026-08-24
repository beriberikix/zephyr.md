---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__ethernet__phy.html
original_path: doxygen/html/group__ethernet__phy.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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
| struct | [phy\_plca\_cfg](structphy__plca__cfg.md) |
|  | PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations. [More...](structphy__plca__cfg.md#details) |

| Macros | |
| --- | --- |
| #define | [PHY\_LINK\_IS\_FULL\_DUPLEX](#ga7dcf0d74db291bf0922c8ceb34307558)(x) |
|  | Check if phy link is full duplex. |
| #define | [PHY\_LINK\_IS\_SPEED\_1000M](#ga49f0673ace36bb3bac3e0c820a1f4de0)(x) |
|  | Check if phy link speed is 1 Gbit/sec. |
| #define | [PHY\_LINK\_IS\_SPEED\_100M](#ga35acfd5ebec25784cc1c5b6be7be6a05)(x) |
|  | Check if phy link speed is 100 Mbit/sec. |
| #define | [PHY\_LINK\_IS\_SPEED\_10M](#gabee5b68903eb89190289d88ecff74de7)(x) |
|  | Check if phy link speed is 10 Mbit/sec. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4)) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | Define the callback function signature for [phy\_link\_callback\_set()](#ga0ede85fdd6efd8c3520d7baf18d04a68) function. |

| Enumerations | |
| --- | --- |
| enum | [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) {     [LINK\_HALF\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c) = BIT(0) , [LINK\_FULL\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c) = BIT(1) , [LINK\_HALF\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d) = BIT(2) , [LINK\_FULL\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956) = BIT(3) ,     [LINK\_HALF\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec) = BIT(4) , [LINK\_FULL\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04) = BIT(5) , [LINK\_FULL\_2500BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e) = BIT(6) , [LINK\_FULL\_5000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6) = BIT(7)   } |
|  | Ethernet link speeds. [More...](#ga9b97fff9fcd6823c9b564b3e86b8da68) |
| enum | [phy\_cfg\_link\_flag](#ga6221da76ffca235eafa291b90eab0d93) { [PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED](#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009) = BIT(0) } |
|  | Ethernet configure link flags. [More...](#ga6221da76ffca235eafa291b90eab0d93) |

| Functions | |
| --- | --- |
| int | [genphy\_get\_plca\_cfg](#ga2c723ef30447db60252a86cd9d72e44f) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Write PHY PLCA configuration. |
| int | [genphy\_set\_plca\_cfg](#ga6b00c2872e5c7da17f49ee50089edcca) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Read PHY PLCA configuration. |
| int | [genphy\_get\_plca\_sts](#gaf7d932210a5933479fb3010f28f6d722) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*plca\_status) |
|  | Read PHY PLCA status. |
| static int | [phy\_configure\_link](#gafce454d5da52532e4588324752c5cec3) (const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds, enum [phy\_cfg\_link\_flag](#ga6221da76ffca235eafa291b90eab0d93) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure PHY link. |
| static int | [phy\_get\_link\_state](#ga4d073c152ad4b6f5745db4f6d8477345) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get PHY link state. |
| static int | [phy\_link\_callback\_set](#ga0ede85fdd6efd8c3520d7baf18d04a68) (const struct [device](structdevice.md) \*dev, [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4) callback, void \*user\_data) |
|  | Set link state change callback. |
| static int | [phy\_read](#ga3fcca53d29981e23426b43d5340d8651) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Read PHY registers. |
| static int | [phy\_write](#ga520c049d830051ffa48708bb0dea429f) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Write PHY register. |
| static int | [phy\_read\_c45](#ga4fa30627b96c9a1d02b43c8e799f2796) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read PHY C45 register. |
| static int | [phy\_write\_c45](#ga492c16dd8b5f2708d9e702ce8906ffd3) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write PHY C45 register. |
| static int | [phy\_set\_plca\_cfg](#ga312638eb2d6c515988f783320742fdbc) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Write PHY PLCA configuration. |
| static int | [phy\_get\_plca\_cfg](#ga79f1b9b5a732eddbc2c2ced219e8582f) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Read PHY PLCA configuration. |
| static int | [phy\_get\_plca\_sts](#ga692d77e273fb795091dbdd103ac43312) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*plca\_status) |
|  | Read PHY PLCA status. |

## Detailed Description

Ethernet PHY Interface.

Since
:   2.7

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga7dcf0d74db291bf0922c8ceb34307558)PHY\_LINK\_IS\_FULL\_DUPLEX

| #define PHY\_LINK\_IS\_FULL\_DUPLEX | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

**Value:**

(x & ([LINK\_FULL\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c) | [LINK\_FULL\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956) | [LINK\_FULL\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04) | [LINK\_FULL\_2500BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e) | \

[LINK\_FULL\_5000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)))

[LINK\_FULL\_2500BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)

@ LINK\_FULL\_2500BASE

2.5GBase Full-Duplex

**Definition** phy.h:49

[LINK\_FULL\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)

@ LINK\_FULL\_10BASE

10Base Full-Duplex

**Definition** phy.h:39

[LINK\_FULL\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)

@ LINK\_FULL\_1000BASE

1000Base Full-Duplex

**Definition** phy.h:47

[LINK\_FULL\_5000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)

@ LINK\_FULL\_5000BASE

5GBase Full-Duplex

**Definition** phy.h:51

[LINK\_FULL\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)

@ LINK\_FULL\_100BASE

100Base Full-Duplex

**Definition** phy.h:43

Check if phy link is full duplex.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is full duplex, false if not.

## [◆ ](#ga49f0673ace36bb3bac3e0c820a1f4de0)PHY\_LINK\_IS\_SPEED\_1000M

| #define PHY\_LINK\_IS\_SPEED\_1000M | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

**Value:**

(x & ([LINK\_HALF\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec) | [LINK\_FULL\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)))

[LINK\_HALF\_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)

@ LINK\_HALF\_1000BASE

1000Base Half-Duplex

**Definition** phy.h:45

Check if phy link speed is 1 Gbit/sec.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is 1 Gbit/sec, false if not.

## [◆ ](#ga35acfd5ebec25784cc1c5b6be7be6a05)PHY\_LINK\_IS\_SPEED\_100M

| #define PHY\_LINK\_IS\_SPEED\_100M | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

**Value:**

(x & ([LINK\_HALF\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d) | [LINK\_FULL\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)))

[LINK\_HALF\_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)

@ LINK\_HALF\_100BASE

100Base Half-Duplex

**Definition** phy.h:41

Check if phy link speed is 100 Mbit/sec.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is 100 Mbit/sec, false if not.

## [◆ ](#gabee5b68903eb89190289d88ecff74de7)PHY\_LINK\_IS\_SPEED\_10M

| #define PHY\_LINK\_IS\_SPEED\_10M | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

**Value:**

(x & ([LINK\_HALF\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c) | [LINK\_FULL\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)))

[LINK\_HALF\_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)

@ LINK\_HALF\_10BASE

10Base Half-Duplex

**Definition** phy.h:37

Check if phy link speed is 10 Mbit/sec.

Parameters
:   | x | Link capabilities |
    | --- | --- |

Returns
:   True if link is 10 Mbit/sec, false if not.

## Typedef Documentation

## [◆ ](#ga3ee3db4ac48395f07d0de536b313dfa4)phy\_callback\_t

| typedef void(\* phy\_callback\_t) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
| --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Define the callback function signature for [phy\_link\_callback\_set()](#ga0ede85fdd6efd8c3520d7baf18d04a68) function.

Parameters
:   | dev | PHY device structure |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Pointer to link\_state structure. |
    | user\_data | Pointer to data specified by user |

## Enumeration Type Documentation

## [◆ ](#ga6221da76ffca235eafa291b90eab0d93)phy\_cfg\_link\_flag

| enum [phy\_cfg\_link\_flag](#ga6221da76ffca235eafa291b90eab0d93) |
| --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Ethernet configure link flags.

| Enumerator | |
| --- | --- |
| PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED | Auto-negotiation disable. |

## [◆ ](#ga9b97fff9fcd6823c9b564b3e86b8da68)phy\_link\_speed

| enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) |
| --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Ethernet link speeds.

| Enumerator | |
| --- | --- |
| LINK\_HALF\_10BASE | 10Base Half-Duplex |
| LINK\_FULL\_10BASE | 10Base Full-Duplex |
| LINK\_HALF\_100BASE | 100Base Half-Duplex |
| LINK\_FULL\_100BASE | 100Base Full-Duplex |
| LINK\_HALF\_1000BASE | 1000Base Half-Duplex |
| LINK\_FULL\_1000BASE | 1000Base Full-Duplex |
| LINK\_FULL\_2500BASE | 2.5GBase Full-Duplex |
| LINK\_FULL\_5000BASE | 5GBase Full-Duplex |

## Function Documentation

## [◆ ](#ga2c723ef30447db60252a86cd9d72e44f)genphy\_get\_plca\_cfg()

| int genphy\_get\_plca\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [phy\_plca\_cfg](structphy__plca__cfg.md) \* | *plca\_cfg* ) |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Write PHY PLCA configuration.

This routine provides a generic interface to configure PHY PLCA settings.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | plca\_cfg | Pointer to plca configuration structure |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#gaf7d932210a5933479fb3010f28f6d722)genphy\_get\_plca\_sts()

| int genphy\_get\_plca\_sts | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *plca\_status* ) |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Read PHY PLCA status.

This routine provides a generic interface to get PHY PLCA status.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | plca\_status | Pointer to plca status |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga6b00c2872e5c7da17f49ee50089edcca)genphy\_set\_plca\_cfg()

| int genphy\_set\_plca\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [phy\_plca\_cfg](structphy__plca__cfg.md) \* | *plca\_cfg* ) |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Read PHY PLCA configuration.

This routine provides a generic interface to get PHY PLCA settings.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | plca\_cfg | Pointer to plca configuration structure |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#gafce454d5da52532e4588324752c5cec3)phy\_configure\_link()

| | int phy\_configure\_link | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [phy\_link\_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68) | *speeds*, | |  |  | enum [phy\_cfg\_link\_flag](#ga6221da76ffca235eafa291b90eab0d93) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Configure PHY link.

This route configures the advertised link speeds.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | speeds | OR'd link speeds to be advertised by the PHY |
    |  | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | OR'd flags to control the link configuration or 0. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |
    | -ENOTSUP | If not supported. |
    | -EALREADY | If already configured with the same speeds and flags. |

## [◆ ](#ga4d073c152ad4b6f5745db4f6d8477345)phy\_get\_link\_state()

| | int phy\_get\_link\_state | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [phy\_link\_state](structphy__link__state.md) \* | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

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

## [◆ ](#ga79f1b9b5a732eddbc2c2ced219e8582f)phy\_get\_plca\_cfg()

| | int phy\_get\_plca\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [phy\_plca\_cfg](structphy__plca__cfg.md) \* | *plca\_cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Read PHY PLCA configuration.

This routine provides a generic interface to get PHY PLCA settings.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | plca\_cfg | Pointer to plca configuration structure |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga692d77e273fb795091dbdd103ac43312)phy\_get\_plca\_sts()

| | int phy\_get\_plca\_sts | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *plca\_status* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Read PHY PLCA status.

This routine provides a generic interface to get PHY PLCA status.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    |  | plca\_status | Pointer to plca status |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga0ede85fdd6efd8c3520d7baf18d04a68)phy\_link\_callback\_set()

| | int phy\_link\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [phy\_callback\_t](#ga3ee3db4ac48395f07d0de536b313dfa4) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Set link state change callback.

Sets a callback that is invoked when link state changes. This is the preferred method for ethernet drivers to be notified of the PHY link state change. The callback will be invoked once after setting it, even if link state has not changed. There can only one callback function set and active at a time. This function is mainly used by ethernet drivers to register a callback to be notified of link state changes and should therefore not be used by applications.

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

`#include <[zephyr/net/phy.h](phy_8h.md)>`

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

## [◆ ](#ga4fa30627b96c9a1d02b43c8e799f2796)phy\_read\_c45()

| | int phy\_read\_c45 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Read PHY C45 register.

This routine provides a generic interface to read to a PHY C45 register.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | devad | Device address |
    | [in] | regad | Register address |
    |  | data | Pointer to receive read data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga312638eb2d6c515988f783320742fdbc)phy\_set\_plca\_cfg()

| | int phy\_set\_plca\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [phy\_plca\_cfg](structphy__plca__cfg.md) \* | *plca\_cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Write PHY PLCA configuration.

This routine provides a generic interface to configure PHY PLCA settings.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | plca\_cfg | Pointer to plca configuration structure |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

## [◆ ](#ga520c049d830051ffa48708bb0dea429f)phy\_write()

| | int phy\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_addr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

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

## [◆ ](#ga492c16dd8b5f2708d9e702ce8906ffd3)phy\_write\_c45()

| | int phy\_write\_c45 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/phy.h](phy_8h.md)>`

Write PHY C45 register.

This routine provides a generic interface to write to a PHY C45 register.

Parameters
:   | [in] | dev | PHY device structure |
    | --- | --- | --- |
    | [in] | devad | Device address |
    | [in] | regad | Register address |
    | [in] | data | Data to write |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | If communication with PHY failed. |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
