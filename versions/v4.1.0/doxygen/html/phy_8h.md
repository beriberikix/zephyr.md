---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/phy_8h.html
original_path: doxygen/html/phy_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

phy.h File Reference

Public APIs for Ethernet PHY drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](phy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [phy\_link\_state](structphy__link__state.md) |
|  | Link state. [More...](structphy__link__state.md#details) |
| struct | [phy\_plca\_cfg](structphy__plca__cfg.md) |
|  | PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations. [More...](structphy__plca__cfg.md#details) |

| Macros | |
| --- | --- |
| #define | [PHY\_LINK\_IS\_FULL\_DUPLEX](group__ethernet__phy.md#ga7dcf0d74db291bf0922c8ceb34307558)(x) |
|  | Check if phy link is full duplex. |
| #define | [PHY\_LINK\_IS\_SPEED\_1000M](group__ethernet__phy.md#ga49f0673ace36bb3bac3e0c820a1f4de0)(x) |
|  | Check if phy link speed is 1 Gbit/sec. |
| #define | [PHY\_LINK\_IS\_SPEED\_100M](group__ethernet__phy.md#ga35acfd5ebec25784cc1c5b6be7be6a05)(x) |
|  | Check if phy link speed is 100 Mbit/sec. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | Define the callback function signature for [phy\_link\_callback\_set()](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68 "Set link state change callback.") function. |

| Enumerations | |
| --- | --- |
| enum | [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) {     [LINK\_HALF\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a3010bbc6bde6ae12b39393ab34ed6c99) = BIT(0) , [LINK\_FULL\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a96d36b5ff474b1919288602cc1927842) = BIT(1) , [LINK\_HALF\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a165dfc46d79c06755d315c2d4033b629) = BIT(2) , [LINK\_FULL\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa2b3167b8fb31ccbe3cd314aa82cf213) = BIT(3) ,     [LINK\_HALF\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ad2b4a4c3ff8358685316c5f056a73d04) = BIT(4) , [LINK\_FULL\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a72eec6d30279ddb51d7e9d6d7dabb611) = BIT(5) , [LINK\_FULL\_2500BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a2f02a79486c5ee930f74e67e60bde377) = BIT(6) , [LINK\_FULL\_5000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a584f66dc8dde26f1377cc4596038e2c9) = BIT(7)   } |
|  | Ethernet link speeds. [More...](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) |

| Functions | |
| --- | --- |
| int | [genphy\_get\_plca\_cfg](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Write PHY PLCA configuration. |
| int | [genphy\_set\_plca\_cfg](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Read PHY PLCA configuration. |
| int | [genphy\_get\_plca\_sts](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*plca\_status) |
|  | Read PHY PLCA status. |
| static int | [phy\_configure\_link](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80) (const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds) |
|  | Configure PHY link. |
| static int | [phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345) (const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get PHY link state. |
| static int | [phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68) (const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) callback, void \*user\_data) |
|  | Set link state change callback. |
| static int | [phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Read PHY registers. |
| static int | [phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Write PHY register. |
| static int | [phy\_read\_c45](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read PHY C45 register. |
| static int | [phy\_write\_c45](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write PHY C45 register. |
| static int | [phy\_set\_plca\_cfg](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Write PHY PLCA configuration. |
| static int | [phy\_get\_plca\_cfg](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f) (const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg) |
|  | Read PHY PLCA configuration. |
| static int | [phy\_get\_plca\_sts](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*plca\_status) |
|  | Read PHY PLCA status. |

## Detailed Description

Public APIs for Ethernet PHY drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [phy.h](phy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
