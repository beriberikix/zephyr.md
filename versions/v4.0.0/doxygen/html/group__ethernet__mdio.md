---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ethernet__mdio.html
original_path: doxygen/html/group__ethernet__mdio.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IEEE 802.3 management interface

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Definitions for IEEE 802.3 management interface.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MDIO\_MMD\_PMAPMD](#ga2aa490a7b68e2ad92d01440a240c118e)   0x01U |
|  | Physical Medium Attachment / Physical Medium Dependent. |
| #define | [MDIO\_MMD\_WIS](#ga3e8b5218550de81211db3d78e16b5f7c)   0x02U |
|  | WAN Interface Sublayer. |
| #define | [MDIO\_MMD\_PCS](#gab071c192b965230e107b7111fa901c23)   0x03U |
|  | Physical Coding Sublayer. |
| #define | [MDIO\_MMD\_PHYXS](#ga7e34a58a18740b276e54095bae9b0421)   0x04U |
|  | PHY Extender Sublayer. |
| #define | [MDIO\_MMD\_DTEXS](#gaa8e0fb0cf10bc5584d34eed46d3d21ff)   0x05U |
|  | DTE Extender Sublayer. |
| #define | [MDIO\_MMD\_TC](#gaf6a80fb3d3090cba631aad20026e23c1)   0x06U |
|  | Transmission Convergence. |
| #define | [MDIO\_MMD\_AN](#ga47459e9e120969a7fc3a7ada2abdd440)   0x07U |
|  | Auto-negotiation. |
| #define | [MDIO\_MMD\_SEPARATED\_PMA1](#ga991d5fc38be73371ac3b0bae8a04f63d)   0x08U |
|  | Separated PMA (1). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA2](#gacde2c812689ada4b7006e1ab4262eaf2)   0x09U |
|  | Separated PMA (2). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA3](#gaee49981a836d3b2a2cf12b3e4bb703b5)   0x0AU |
|  | Separated PMA (3). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA4](#gac57c99dcb72884df7e538e2af1804244)   0x0BU |
|  | Separated PMA (4). |
| #define | [MDIO\_MMD\_C22EXT](#gab8a03ec360a743225345dd6bb64882f1)   0x1DU |
|  | Clause 22 extension. |
| #define | [MDIO\_MMD\_VENDOR\_SPECIFIC1](#ga71e8d72d50c484557a2e39c622490956)   0x1EU |
|  | Vendor Specific 1. |
| #define | [MDIO\_MMD\_VENDOR\_SPECIFIC2](#gaac45f28f75bcfeca861d06b99239cc77)   0x1FU |
|  | Vendor Specific 2. |
| #define | [MDIO\_CTRL1](#gaab4d7fa609d78bb982f2e0baae2facc9)   0x0000U |
|  | Control 1. |
| #define | [MDIO\_STAT1](#ga684cd28a49124170c327f279db8ba512)   0x0001U |
|  | Status 1. |
| #define | [MDIO\_DEVID1](#ga8a63e5b18fa478566b230f22172e998f)   0x0002U |
|  | Device identifier (1). |
| #define | [MDIO\_DEVID2](#gaafa088ec5cbe2a4b4023a2c8310b1ae1)   0x0003U |
|  | Device identifier (2). |
| #define | [MDIO\_SPEED](#ga75c8d4845abbcb0d0b283dcf24ea684a)   0x0004U |
|  | Speed ability. |
| #define | [MDIO\_DEVS1](#ga210f57aa1971b2f77765fdc47a2b00f2)   0x0005U |
|  | Devices in package (1). |
| #define | [MDIO\_DEVS2](#ga4d095f2392dd8d94ff014e510e164a16)   0x0006U |
|  | Devices in package (2). |
| #define | [MDIO\_CTRL2](#ga3c3d4c2f16cfdd4f2a4f6781069b2395)   0x0007U |
|  | Control 2. |
| #define | [MDIO\_STAT2](#ga1cc7343ad758f8c070f6b28b568e2a00)   0x0008U |
|  | Status 2. |
| #define | [MDIO\_PKGID1](#gaead8a046d17d07f54cf5cae793cc7392)   0x000EU |
|  | Package identifier (1). |
| #define | [MDIO\_PKGID2](#gadd799e84b3cc7a31f57962fe29a1800f)   0x000FU |
|  | Package identifier (2). |
| #define | [MDIO\_PCS\_EEE\_CAP](#ga12b7f932606a306043434433c6c721ff)   0x0014U |
| #define | [MDIO\_AN\_EEE\_ADV](#gabe093365122e043bbceb08f6c354dda2)   0x003CU |
| #define | [MDIO\_AN\_T1\_CTRL](#ga52b4b4aac146d80fe6581f612878df09)   0x0200U |
|  | BASE-T1 Auto-negotiation control. |
| #define | [MDIO\_AN\_T1\_STAT](#ga698a5175bfa98c727579e0be12204cff)   0x0201U |
|  | BASE-T1 Auto-negotiation status. |
| #define | [MDIO\_AN\_T1\_ADV\_L](#ga69e18d3aafb29972b8746b2ca5e67b3b)   0x0202U |
|  | BASE-T1 Auto-negotiation advertisement register [15:0]. |
| #define | [MDIO\_AN\_T1\_ADV\_M](#gad870783cb015fd3bf7e07a437b429ec6)   0x0203U |
|  | BASE-T1 Auto-negotiation advertisement register [31:16]. |
| #define | [MDIO\_AN\_T1\_ADV\_H](#ga85201e69432f1749c9f29f351565d8f2)   0x0204U |
|  | BASE-T1 Auto-negotiation advertisement register [47:32]. |
| #define | [MDIO\_PMA\_PMD\_BT1\_CTRL](#ga8a2295bc2f17aa0444e302ebadb34f6b)   0x0834U |
|  | BASE-T1 PMA/PMD control register. |
| #define | [MDIO\_AN\_T1\_CTRL\_RESTART](#gabef35b68eb8a6e27c90dc5c5ea2001aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Auto-negotiation Restart. |
| #define | [MDIO\_AN\_T1\_CTRL\_EN](#gac186dd4bb083f29368b2af4750daece7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Auto-negotiation Enable. |
| #define | [MDIO\_AN\_T1\_STAT\_LINK\_STATUS](#gac1f927e0b3fbd99a1f4a85bada0f7a94)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Link Status. |
| #define | [MDIO\_AN\_T1\_STAT\_ABLE](#ga912f2bddd1b8573e6420152e43060bdc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Auto-negotiation Ability. |
| #define | [MDIO\_AN\_T1\_STAT\_REMOTE\_FAULT](#ga7acdb2f35803d1f3e8e5ce2e340a6e30)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Auto-negotiation Remote Fault. |
| #define | [MDIO\_AN\_T1\_STAT\_COMPLETE](#ga5f1496d45ba3404aabd05ae9f574ade7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Auto-negotiation Complete. |
| #define | [MDIO\_AN\_T1\_STAT\_PAGE\_RX](#ga638f63292ab5ddd4e301ddd9e4d70418)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Page Received. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_PAUSE\_CAP](#ga404345912bcad2c6691483910928f85a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Pause Ability. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_PAUSE\_ASYM](#gae19eabc9238eae96ef8055f37fb0882e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Pause Ability. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_FORCE\_MS](#gaa227d9a74c324e64935e77811e7c2dcc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Force Master/Slave Configuration. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_REMOTE\_FAULT](#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Remote Fault. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_ACK](#gaf6f17971533580a89bde8c52bc110363)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Acknowledge (ACK). |
| #define | [MDIO\_AN\_T1\_ADV\_L\_NEXT\_PAGE\_REQ](#gab69a2d9ebd289f792aba878bc831079a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Next Page Request. |
| #define | [MDIO\_AN\_T1\_ADV\_M\_B10L](#ga32e41aa9618bc858f9ca70fabef9bf37)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L Ability |
| #define | [MDIO\_AN\_T1\_ADV\_M\_MST](#ga2ada131bfc4e87d3c8993ce3d0ca2d48)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Master/slave Configuration. |
| #define | [MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI\_REQ](#ga534444217d2388e5d752d60a03ca68b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L High Level Transmit Operating Mode Request |
| #define | [MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI](#ga581d91721dd6f1aab1462c63df48d50a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | 10BASE-T1L High Level Transmit Operating Mode Ability |
| #define | [MDIO\_PMA\_PMD\_BT1\_CTRL\_CFG\_MST](#ga11863eaaeb876c1d3dc83d1ee9e045d2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | BASE-T1 master/slave configuration. |
| #define | [MDIO\_PMA\_B10L\_CTRL](#ga490f3bb0e91ddbe9783864040d2054a8)   0x08F6U |
|  | 10BASE-T1L PMA control |
| #define | [MDIO\_PMA\_B10L\_STAT](#ga17955956be0807edf50f24f3d6b1a175)   0x08F7U |
|  | 10BASE-T1L PMA status |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT](#gad55902f2a79193162459a6b90d508a41)   0x8302U |
|  | 10BASE-T1L PMA link status |
| #define | [MDIO\_PCS\_B10L\_CTRL](#gaafbb9fbd657bf59ee11a1c832ff4d4a0)   0x08E6U |
|  | 10BASE-T1L PCS control |
| #define | [MDIO\_PCS\_B10L\_STAT](#ga66181040f5b5d5301203914700d02dd7)   0x08E7U |
|  | 10BASE-T1L PCS status |
| #define | [MDIO\_PMA\_B10L\_CTRL\_TX\_DIS\_MODE\_EN](#ga0d68932ddfa3b8194b6b085def230aa4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L Transmit Disable Mode |
| #define | [MDIO\_PMA\_B10L\_CTRL\_TX\_LVL\_HI](#gae27e01f297d07281f2210f82ce1c41cb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L Transmit Voltage Amplitude Control |
| #define | [MDIO\_PMA\_B10L\_CTRL\_EEE](#ga1d8b5fa13bc9b3e685f5123614ceeac0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | 10BASE-T1L EEE Enable |
| #define | [MDIO\_PMA\_B10L\_CTRL\_LB\_PMA\_LOC\_EN](#gaf5e632085ce3efb8fbbd33ca166e577d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L PMA Loopback |
| #define | [MDIO\_PMA\_B10L\_STAT\_LINK](#gaa3e658df0baa6377224b1580a7d2bd1c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L PMA receive link up |
| #define | [MDIO\_PMA\_B10L\_STAT\_FAULT](#ga8a3919a982c3d7b038b4774aefec0289)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | 10BASE-T1L Fault condition detected |
| #define | [MDIO\_PMA\_B10L\_STAT\_POLARITY](#gafad692e7e73ca3ba3ee267915745aa5b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | 10BASE-T1L Receive polarity is reversed |
| #define | [MDIO\_PMA\_B10L\_STAT\_RECV\_FAULT](#ga1017896c84e1a32568f695bc84834894)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | 10BASE-T1L Able to detect fault on receive path |
| #define | [MDIO\_PMA\_B10L\_STAT\_EEE](#ga54bec9909ebcc69b84da93a6e7bdbba6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | 10BASE-T1L PHY has EEE ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_LOW\_POWER](#ga6f4c3046c404635897a188ccf6c364a5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | 10BASE-T1L PMA has low-power ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_2V4\_ABLE](#gab289ba626543006aebe04da57b53b050)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L PHY has 2.4 Vpp operating mode ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_LB\_ABLE](#gade5d7df4d74c0bcc3c6260d49d6d51a1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | 10BASE-T1L PHY has loopback ability |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK\_LL](#gaff70ac51be8f32a0cbcb5046f92a727f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | 10BASE-T1L Remote Receiver Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK](#gac03f000f6beef4a1debadaaca339b601)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | 10BASE-T1L Remote Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK\_LL](#ga51784a68c7a237a32d846723c01ec873)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | 10BASE-T1L Local Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK](#ga08ca50389a30a21148525c7d9b212b6f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | 10BASE-T1L Local Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK\_LL](#ga9b6a1e683e1cc964bc41cefbc2f9d91b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | 10BASE-T1L Descrambler Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK](#gabdd013ea8c586918c54c258a6f1ae2eb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | 10BASE-T1L Descrambler Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK\_LL](#ga987f6dabf90e98985d0d11b7392701fc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | 10BASE-T1L Link Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK](#gab7d5ca01e536e68d9f9b90b7f24d0bf5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L Link Status OK |
| #define | [MDIO\_PCS\_B10L\_CTRL\_LB\_PCS\_EN](#ga6d2c4c50608d24fb8106841ca9a79714)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L PCS Loopback Enable |
| #define | [MDIO\_PCS\_B10L\_STAT\_DSCR\_STAT\_OK\_LL](#gab6abfd0df706b72684124db458491d9b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | 10BASE-T1L PCS Descrambler Status |
| #define | [MDIO\_AN\_EEE\_ADV\_1000T](#ga535402b2cc3207645ed5485b762cd52f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Advertise 1000T capability. |
| #define | [MDIO\_AN\_EEE\_ADV\_100TX](#ga13b78fc17dcf75c515b58bf3571608ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Advertise 100TX capability. |

| Enumerations | |
| --- | --- |
| enum | [mdio\_opcode](#ga304f668820ee91a63512c174e405b492) {     [MDIO\_OP\_C22\_WRITE](#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d) = 1 , [MDIO\_OP\_C22\_READ](#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46) = 2 , [MDIO\_OP\_C45\_ADDRESS](#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371) = 0 , [MDIO\_OP\_C45\_WRITE](#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f) = 1 ,     [MDIO\_OP\_C45\_READ\_INC](#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd) = 2 , [MDIO\_OP\_C45\_READ](#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1) = 3   } |
|  | MDIO transaction operation code. [More...](#ga304f668820ee91a63512c174e405b492) |

## Detailed Description

Definitions for IEEE 802.3 management interface.

Since
:   3.5

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gabe093365122e043bbceb08f6c354dda2)MDIO\_AN\_EEE\_ADV

| #define MDIO\_AN\_EEE\_ADV   0x003CU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

## [◆ ](#ga535402b2cc3207645ed5485b762cd52f)MDIO\_AN\_EEE\_ADV\_1000T

| #define MDIO\_AN\_EEE\_ADV\_1000T   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Advertise 1000T capability.

## [◆ ](#ga13b78fc17dcf75c515b58bf3571608ce)MDIO\_AN\_EEE\_ADV\_100TX

| #define MDIO\_AN\_EEE\_ADV\_100TX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Advertise 100TX capability.

## [◆ ](#ga85201e69432f1749c9f29f351565d8f2)MDIO\_AN\_T1\_ADV\_H

| #define MDIO\_AN\_T1\_ADV\_H   0x0204U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 Auto-negotiation advertisement register [47:32].

## [◆ ](#ga581d91721dd6f1aab1462c63df48d50a)MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI

| #define MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L High Level Transmit Operating Mode Ability

## [◆ ](#ga534444217d2388e5d752d60a03ca68b0)MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI\_REQ

| #define MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI\_REQ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L High Level Transmit Operating Mode Request

## [◆ ](#ga69e18d3aafb29972b8746b2ca5e67b3b)MDIO\_AN\_T1\_ADV\_L

| #define MDIO\_AN\_T1\_ADV\_L   0x0202U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 Auto-negotiation advertisement register [15:0].

## [◆ ](#gaf6f17971533580a89bde8c52bc110363)MDIO\_AN\_T1\_ADV\_L\_ACK

| #define MDIO\_AN\_T1\_ADV\_L\_ACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Acknowledge (ACK).

## [◆ ](#gaa227d9a74c324e64935e77811e7c2dcc)MDIO\_AN\_T1\_ADV\_L\_FORCE\_MS

| #define MDIO\_AN\_T1\_ADV\_L\_FORCE\_MS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Force Master/Slave Configuration.

## [◆ ](#gab69a2d9ebd289f792aba878bc831079a)MDIO\_AN\_T1\_ADV\_L\_NEXT\_PAGE\_REQ

| #define MDIO\_AN\_T1\_ADV\_L\_NEXT\_PAGE\_REQ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Next Page Request.

## [◆ ](#gae19eabc9238eae96ef8055f37fb0882e)MDIO\_AN\_T1\_ADV\_L\_PAUSE\_ASYM

| #define MDIO\_AN\_T1\_ADV\_L\_PAUSE\_ASYM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Pause Ability.

## [◆ ](#ga404345912bcad2c6691483910928f85a)MDIO\_AN\_T1\_ADV\_L\_PAUSE\_CAP

| #define MDIO\_AN\_T1\_ADV\_L\_PAUSE\_CAP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Pause Ability.

## [◆ ](#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)MDIO\_AN\_T1\_ADV\_L\_REMOTE\_FAULT

| #define MDIO\_AN\_T1\_ADV\_L\_REMOTE\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Remote Fault.

## [◆ ](#gad870783cb015fd3bf7e07a437b429ec6)MDIO\_AN\_T1\_ADV\_M

| #define MDIO\_AN\_T1\_ADV\_M   0x0203U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 Auto-negotiation advertisement register [31:16].

## [◆ ](#ga32e41aa9618bc858f9ca70fabef9bf37)MDIO\_AN\_T1\_ADV\_M\_B10L

| #define MDIO\_AN\_T1\_ADV\_M\_B10L   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Ability

## [◆ ](#ga2ada131bfc4e87d3c8993ce3d0ca2d48)MDIO\_AN\_T1\_ADV\_M\_MST

| #define MDIO\_AN\_T1\_ADV\_M\_MST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Master/slave Configuration.

## [◆ ](#ga52b4b4aac146d80fe6581f612878df09)MDIO\_AN\_T1\_CTRL

| #define MDIO\_AN\_T1\_CTRL   0x0200U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 Auto-negotiation control.

## [◆ ](#gac186dd4bb083f29368b2af4750daece7)MDIO\_AN\_T1\_CTRL\_EN

| #define MDIO\_AN\_T1\_CTRL\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation Enable.

## [◆ ](#gabef35b68eb8a6e27c90dc5c5ea2001aa)MDIO\_AN\_T1\_CTRL\_RESTART

| #define MDIO\_AN\_T1\_CTRL\_RESTART   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation Restart.

## [◆ ](#ga698a5175bfa98c727579e0be12204cff)MDIO\_AN\_T1\_STAT

| #define MDIO\_AN\_T1\_STAT   0x0201U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 Auto-negotiation status.

## [◆ ](#ga912f2bddd1b8573e6420152e43060bdc)MDIO\_AN\_T1\_STAT\_ABLE

| #define MDIO\_AN\_T1\_STAT\_ABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation Ability.

## [◆ ](#ga5f1496d45ba3404aabd05ae9f574ade7)MDIO\_AN\_T1\_STAT\_COMPLETE

| #define MDIO\_AN\_T1\_STAT\_COMPLETE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation Complete.

## [◆ ](#gac1f927e0b3fbd99a1f4a85bada0f7a94)MDIO\_AN\_T1\_STAT\_LINK\_STATUS

| #define MDIO\_AN\_T1\_STAT\_LINK\_STATUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Link Status.

## [◆ ](#ga638f63292ab5ddd4e301ddd9e4d70418)MDIO\_AN\_T1\_STAT\_PAGE\_RX

| #define MDIO\_AN\_T1\_STAT\_PAGE\_RX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Page Received.

## [◆ ](#ga7acdb2f35803d1f3e8e5ce2e340a6e30)MDIO\_AN\_T1\_STAT\_REMOTE\_FAULT

| #define MDIO\_AN\_T1\_STAT\_REMOTE\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation Remote Fault.

## [◆ ](#gaab4d7fa609d78bb982f2e0baae2facc9)MDIO\_CTRL1

| #define MDIO\_CTRL1   0x0000U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Control 1.

## [◆ ](#ga3c3d4c2f16cfdd4f2a4f6781069b2395)MDIO\_CTRL2

| #define MDIO\_CTRL2   0x0007U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Control 2.

## [◆ ](#ga8a63e5b18fa478566b230f22172e998f)MDIO\_DEVID1

| #define MDIO\_DEVID1   0x0002U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Device identifier (1).

## [◆ ](#gaafa088ec5cbe2a4b4023a2c8310b1ae1)MDIO\_DEVID2

| #define MDIO\_DEVID2   0x0003U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Device identifier (2).

## [◆ ](#ga210f57aa1971b2f77765fdc47a2b00f2)MDIO\_DEVS1

| #define MDIO\_DEVS1   0x0005U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Devices in package (1).

## [◆ ](#ga4d095f2392dd8d94ff014e510e164a16)MDIO\_DEVS2

| #define MDIO\_DEVS2   0x0006U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Devices in package (2).

## [◆ ](#ga47459e9e120969a7fc3a7ada2abdd440)MDIO\_MMD\_AN

| #define MDIO\_MMD\_AN   0x07U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Auto-negotiation.

## [◆ ](#gab8a03ec360a743225345dd6bb64882f1)MDIO\_MMD\_C22EXT

| #define MDIO\_MMD\_C22EXT   0x1DU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Clause 22 extension.

## [◆ ](#gaa8e0fb0cf10bc5584d34eed46d3d21ff)MDIO\_MMD\_DTEXS

| #define MDIO\_MMD\_DTEXS   0x05U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

DTE Extender Sublayer.

## [◆ ](#gab071c192b965230e107b7111fa901c23)MDIO\_MMD\_PCS

| #define MDIO\_MMD\_PCS   0x03U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Physical Coding Sublayer.

## [◆ ](#ga7e34a58a18740b276e54095bae9b0421)MDIO\_MMD\_PHYXS

| #define MDIO\_MMD\_PHYXS   0x04U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

PHY Extender Sublayer.

## [◆ ](#ga2aa490a7b68e2ad92d01440a240c118e)MDIO\_MMD\_PMAPMD

| #define MDIO\_MMD\_PMAPMD   0x01U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Physical Medium Attachment / Physical Medium Dependent.

## [◆ ](#ga991d5fc38be73371ac3b0bae8a04f63d)MDIO\_MMD\_SEPARATED\_PMA1

| #define MDIO\_MMD\_SEPARATED\_PMA1   0x08U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Separated PMA (1).

## [◆ ](#gacde2c812689ada4b7006e1ab4262eaf2)MDIO\_MMD\_SEPARATED\_PMA2

| #define MDIO\_MMD\_SEPARATED\_PMA2   0x09U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Separated PMA (2).

## [◆ ](#gaee49981a836d3b2a2cf12b3e4bb703b5)MDIO\_MMD\_SEPARATED\_PMA3

| #define MDIO\_MMD\_SEPARATED\_PMA3   0x0AU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Separated PMA (3).

## [◆ ](#gac57c99dcb72884df7e538e2af1804244)MDIO\_MMD\_SEPARATED\_PMA4

| #define MDIO\_MMD\_SEPARATED\_PMA4   0x0BU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Separated PMA (4).

## [◆ ](#gaf6a80fb3d3090cba631aad20026e23c1)MDIO\_MMD\_TC

| #define MDIO\_MMD\_TC   0x06U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Transmission Convergence.

## [◆ ](#ga71e8d72d50c484557a2e39c622490956)MDIO\_MMD\_VENDOR\_SPECIFIC1

| #define MDIO\_MMD\_VENDOR\_SPECIFIC1   0x1EU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Vendor Specific 1.

## [◆ ](#gaac45f28f75bcfeca861d06b99239cc77)MDIO\_MMD\_VENDOR\_SPECIFIC2

| #define MDIO\_MMD\_VENDOR\_SPECIFIC2   0x1FU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Vendor Specific 2.

## [◆ ](#ga3e8b5218550de81211db3d78e16b5f7c)MDIO\_MMD\_WIS

| #define MDIO\_MMD\_WIS   0x02U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

WAN Interface Sublayer.

## [◆ ](#gaafbb9fbd657bf59ee11a1c832ff4d4a0)MDIO\_PCS\_B10L\_CTRL

| #define MDIO\_PCS\_B10L\_CTRL   0x08E6U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PCS control

## [◆ ](#ga6d2c4c50608d24fb8106841ca9a79714)MDIO\_PCS\_B10L\_CTRL\_LB\_PCS\_EN

| #define MDIO\_PCS\_B10L\_CTRL\_LB\_PCS\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PCS Loopback Enable

## [◆ ](#ga66181040f5b5d5301203914700d02dd7)MDIO\_PCS\_B10L\_STAT

| #define MDIO\_PCS\_B10L\_STAT   0x08E7U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PCS status

## [◆ ](#gab6abfd0df706b72684124db458491d9b)MDIO\_PCS\_B10L\_STAT\_DSCR\_STAT\_OK\_LL

| #define MDIO\_PCS\_B10L\_STAT\_DSCR\_STAT\_OK\_LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PCS Descrambler Status

## [◆ ](#ga12b7f932606a306043434433c6c721ff)MDIO\_PCS\_EEE\_CAP

| #define MDIO\_PCS\_EEE\_CAP   0x0014U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

## [◆ ](#gaead8a046d17d07f54cf5cae793cc7392)MDIO\_PKGID1

| #define MDIO\_PKGID1   0x000EU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Package identifier (1).

## [◆ ](#gadd799e84b3cc7a31f57962fe29a1800f)MDIO\_PKGID2

| #define MDIO\_PKGID2   0x000FU |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Package identifier (2).

## [◆ ](#ga490f3bb0e91ddbe9783864040d2054a8)MDIO\_PMA\_B10L\_CTRL

| #define MDIO\_PMA\_B10L\_CTRL   0x08F6U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA control

## [◆ ](#ga1d8b5fa13bc9b3e685f5123614ceeac0)MDIO\_PMA\_B10L\_CTRL\_EEE

| #define MDIO\_PMA\_B10L\_CTRL\_EEE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L EEE Enable

## [◆ ](#gaf5e632085ce3efb8fbbd33ca166e577d)MDIO\_PMA\_B10L\_CTRL\_LB\_PMA\_LOC\_EN

| #define MDIO\_PMA\_B10L\_CTRL\_LB\_PMA\_LOC\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA Loopback

## [◆ ](#ga0d68932ddfa3b8194b6b085def230aa4)MDIO\_PMA\_B10L\_CTRL\_TX\_DIS\_MODE\_EN

| #define MDIO\_PMA\_B10L\_CTRL\_TX\_DIS\_MODE\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Transmit Disable Mode

## [◆ ](#gae27e01f297d07281f2210f82ce1c41cb)MDIO\_PMA\_B10L\_CTRL\_TX\_LVL\_HI

| #define MDIO\_PMA\_B10L\_CTRL\_TX\_LVL\_HI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Transmit Voltage Amplitude Control

## [◆ ](#gad55902f2a79193162459a6b90d508a41)MDIO\_PMA\_B10L\_LINK\_STAT

| #define MDIO\_PMA\_B10L\_LINK\_STAT   0x8302U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA link status

## [◆ ](#gabdd013ea8c586918c54c258a6f1ae2eb)MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Descrambler Status OK

## [◆ ](#ga9b6a1e683e1cc964bc41cefbc2f9d91b)MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK\_LL

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK\_LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Descrambler Status OK Latch Low

## [◆ ](#gab7d5ca01e536e68d9f9b90b7f24d0bf5)MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Link Status OK

## [◆ ](#ga987f6dabf90e98985d0d11b7392701fc)MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK\_LL

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK\_LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Link Status OK Latch Low

## [◆ ](#ga08ca50389a30a21148525c7d9b212b6f)MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Local Receiver Status OK

## [◆ ](#ga51784a68c7a237a32d846723c01ec873)MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK\_LL

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK\_LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Local Receiver Status OK

## [◆ ](#gac03f000f6beef4a1debadaaca339b601)MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Remote Receiver Status OK

## [◆ ](#gaff70ac51be8f32a0cbcb5046f92a727f)MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK\_LL

| #define MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK\_LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Remote Receiver Status OK Latch Low

## [◆ ](#ga17955956be0807edf50f24f3d6b1a175)MDIO\_PMA\_B10L\_STAT

| #define MDIO\_PMA\_B10L\_STAT   0x08F7U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA status

## [◆ ](#gab289ba626543006aebe04da57b53b050)MDIO\_PMA\_B10L\_STAT\_2V4\_ABLE

| #define MDIO\_PMA\_B10L\_STAT\_2V4\_ABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PHY has 2.4 Vpp operating mode ability

## [◆ ](#ga54bec9909ebcc69b84da93a6e7bdbba6)MDIO\_PMA\_B10L\_STAT\_EEE

| #define MDIO\_PMA\_B10L\_STAT\_EEE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PHY has EEE ability

## [◆ ](#ga8a3919a982c3d7b038b4774aefec0289)MDIO\_PMA\_B10L\_STAT\_FAULT

| #define MDIO\_PMA\_B10L\_STAT\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Fault condition detected

## [◆ ](#gade5d7df4d74c0bcc3c6260d49d6d51a1)MDIO\_PMA\_B10L\_STAT\_LB\_ABLE

| #define MDIO\_PMA\_B10L\_STAT\_LB\_ABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PHY has loopback ability

## [◆ ](#gaa3e658df0baa6377224b1580a7d2bd1c)MDIO\_PMA\_B10L\_STAT\_LINK

| #define MDIO\_PMA\_B10L\_STAT\_LINK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA receive link up

## [◆ ](#ga6f4c3046c404635897a188ccf6c364a5)MDIO\_PMA\_B10L\_STAT\_LOW\_POWER

| #define MDIO\_PMA\_B10L\_STAT\_LOW\_POWER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L PMA has low-power ability

## [◆ ](#gafad692e7e73ca3ba3ee267915745aa5b)MDIO\_PMA\_B10L\_STAT\_POLARITY

| #define MDIO\_PMA\_B10L\_STAT\_POLARITY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Receive polarity is reversed

## [◆ ](#ga1017896c84e1a32568f695bc84834894)MDIO\_PMA\_B10L\_STAT\_RECV\_FAULT

| #define MDIO\_PMA\_B10L\_STAT\_RECV\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

10BASE-T1L Able to detect fault on receive path

## [◆ ](#ga8a2295bc2f17aa0444e302ebadb34f6b)MDIO\_PMA\_PMD\_BT1\_CTRL

| #define MDIO\_PMA\_PMD\_BT1\_CTRL   0x0834U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 PMA/PMD control register.

## [◆ ](#ga11863eaaeb876c1d3dc83d1ee9e045d2)MDIO\_PMA\_PMD\_BT1\_CTRL\_CFG\_MST

| #define MDIO\_PMA\_PMD\_BT1\_CTRL\_CFG\_MST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

BASE-T1 master/slave configuration.

## [◆ ](#ga75c8d4845abbcb0d0b283dcf24ea684a)MDIO\_SPEED

| #define MDIO\_SPEED   0x0004U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Speed ability.

## [◆ ](#ga684cd28a49124170c327f279db8ba512)MDIO\_STAT1

| #define MDIO\_STAT1   0x0001U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Status 1.

## [◆ ](#ga1cc7343ad758f8c070f6b28b568e2a00)MDIO\_STAT2

| #define MDIO\_STAT2   0x0008U |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

Status 2.

## Enumeration Type Documentation

## [◆ ](#ga304f668820ee91a63512c174e405b492)mdio\_opcode

| enum [mdio\_opcode](#ga304f668820ee91a63512c174e405b492) |
| --- |

`#include <[mdio.h](net_2mdio_8h.md)>`

MDIO transaction operation code.

| Enumerator | |
| --- | --- |
| MDIO\_OP\_C22\_WRITE | IEEE 802.3 22.2.4.5.4 write operation. |
| MDIO\_OP\_C22\_READ | IEEE 802.3 22.2.4.5.4 read operation. |
| MDIO\_OP\_C45\_ADDRESS | IEEE 802.3 45.3.4 address operation. |
| MDIO\_OP\_C45\_WRITE | IEEE 802.3 45.3.4 write operation. |
| MDIO\_OP\_C45\_READ\_INC | IEEE 802.3 45.3.4 post-read-increment-address operation. |
| MDIO\_OP\_C45\_READ | IEEE 802.3 45.3.4 read operation. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
