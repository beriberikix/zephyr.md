---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net_2mdio_8h.html
original_path: doxygen/html/net_2mdio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdio.h File Reference

Definitions for IEEE 802.3 management interface.
[More...](#details)

[Go to the source code of this file.](net_2mdio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MDIO\_MMD\_PMAPMD](group__ethernet__mdio.md#ga2aa490a7b68e2ad92d01440a240c118e)   0x01U |
|  | Physical Medium Attachment / Physical Medium Dependent. |
| #define | [MDIO\_MMD\_WIS](group__ethernet__mdio.md#ga3e8b5218550de81211db3d78e16b5f7c)   0x02U |
|  | WAN Interface Sublayer. |
| #define | [MDIO\_MMD\_PCS](group__ethernet__mdio.md#gab071c192b965230e107b7111fa901c23)   0x03U |
|  | Physical Coding Sublayer. |
| #define | [MDIO\_MMD\_PHYXS](group__ethernet__mdio.md#ga7e34a58a18740b276e54095bae9b0421)   0x04U |
|  | PHY Extender Sublayer. |
| #define | [MDIO\_MMD\_DTEXS](group__ethernet__mdio.md#gaa8e0fb0cf10bc5584d34eed46d3d21ff)   0x05U |
|  | DTE Extender Sublayer. |
| #define | [MDIO\_MMD\_TC](group__ethernet__mdio.md#gaf6a80fb3d3090cba631aad20026e23c1)   0x06U |
|  | Transmission Convergence. |
| #define | [MDIO\_MMD\_AN](group__ethernet__mdio.md#ga47459e9e120969a7fc3a7ada2abdd440)   0x07U |
|  | Auto-negotiation. |
| #define | [MDIO\_MMD\_SEPARATED\_PMA1](group__ethernet__mdio.md#ga991d5fc38be73371ac3b0bae8a04f63d)   0x08U |
|  | Separated PMA (1). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA2](group__ethernet__mdio.md#gacde2c812689ada4b7006e1ab4262eaf2)   0x09U |
|  | Separated PMA (2). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA3](group__ethernet__mdio.md#gaee49981a836d3b2a2cf12b3e4bb703b5)   0x0AU |
|  | Separated PMA (3). |
| #define | [MDIO\_MMD\_SEPARATED\_PMA4](group__ethernet__mdio.md#gac57c99dcb72884df7e538e2af1804244)   0x0BU |
|  | Separated PMA (4). |
| #define | [MDIO\_MMD\_C22EXT](group__ethernet__mdio.md#gab8a03ec360a743225345dd6bb64882f1)   0x1DU |
|  | Clause 22 extension. |
| #define | [MDIO\_MMD\_VENDOR\_SPECIFIC1](group__ethernet__mdio.md#ga71e8d72d50c484557a2e39c622490956)   0x1EU |
|  | Vendor Specific 1. |
| #define | [MDIO\_MMD\_VENDOR\_SPECIFIC2](group__ethernet__mdio.md#gaac45f28f75bcfeca861d06b99239cc77)   0x1FU |
|  | Vendor Specific 2. |
| #define | [MDIO\_CTRL1](group__ethernet__mdio.md#gaab4d7fa609d78bb982f2e0baae2facc9)   0x0000U |
|  | Control 1. |
| #define | [MDIO\_STAT1](group__ethernet__mdio.md#ga684cd28a49124170c327f279db8ba512)   0x0001U |
|  | Status 1. |
| #define | [MDIO\_DEVID1](group__ethernet__mdio.md#ga8a63e5b18fa478566b230f22172e998f)   0x0002U |
|  | Device identifier (1). |
| #define | [MDIO\_DEVID2](group__ethernet__mdio.md#gaafa088ec5cbe2a4b4023a2c8310b1ae1)   0x0003U |
|  | Device identifier (2). |
| #define | [MDIO\_SPEED](group__ethernet__mdio.md#ga75c8d4845abbcb0d0b283dcf24ea684a)   0x0004U |
|  | Speed ability. |
| #define | [MDIO\_DEVS1](group__ethernet__mdio.md#ga210f57aa1971b2f77765fdc47a2b00f2)   0x0005U |
|  | Devices in package (1). |
| #define | [MDIO\_DEVS2](group__ethernet__mdio.md#ga4d095f2392dd8d94ff014e510e164a16)   0x0006U |
|  | Devices in package (2). |
| #define | [MDIO\_CTRL2](group__ethernet__mdio.md#ga3c3d4c2f16cfdd4f2a4f6781069b2395)   0x0007U |
|  | Control 2. |
| #define | [MDIO\_STAT2](group__ethernet__mdio.md#ga1cc7343ad758f8c070f6b28b568e2a00)   0x0008U |
|  | Status 2. |
| #define | [MDIO\_PKGID1](group__ethernet__mdio.md#gaead8a046d17d07f54cf5cae793cc7392)   0x000EU |
|  | Package identifier (1). |
| #define | [MDIO\_PKGID2](group__ethernet__mdio.md#gadd799e84b3cc7a31f57962fe29a1800f)   0x000FU |
|  | Package identifier (2). |
| #define | [MDIO\_AN\_T1\_CTRL](group__ethernet__mdio.md#ga52b4b4aac146d80fe6581f612878df09)   0x0200U |
|  | BASE-T1 Auto-negotiation control. |
| #define | [MDIO\_AN\_T1\_STAT](group__ethernet__mdio.md#ga698a5175bfa98c727579e0be12204cff)   0x0201U |
|  | BASE-T1 Auto-negotiation status. |
| #define | [MDIO\_AN\_T1\_ADV\_L](group__ethernet__mdio.md#ga69e18d3aafb29972b8746b2ca5e67b3b)   0x0202U |
|  | BASE-T1 Auto-negotiation advertisement register [15:0]. |
| #define | [MDIO\_AN\_T1\_ADV\_M](group__ethernet__mdio.md#gad870783cb015fd3bf7e07a437b429ec6)   0x0203U |
|  | BASE-T1 Auto-negotiation advertisement register [31:16]. |
| #define | [MDIO\_AN\_T1\_ADV\_H](group__ethernet__mdio.md#ga85201e69432f1749c9f29f351565d8f2)   0x0204U |
|  | BASE-T1 Auto-negotiation advertisement register [47:32]. |
| #define | [MDIO\_PMA\_PMD\_BT1\_CTRL](group__ethernet__mdio.md#ga8a2295bc2f17aa0444e302ebadb34f6b)   0x0834U |
|  | BASE-T1 PMA/PMD control register. |
| #define | [MDIO\_AN\_T1\_CTRL\_RESTART](group__ethernet__mdio.md#gabef35b68eb8a6e27c90dc5c5ea2001aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Auto-negotiation Restart. |
| #define | [MDIO\_AN\_T1\_CTRL\_EN](group__ethernet__mdio.md#gac186dd4bb083f29368b2af4750daece7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Auto-negotiation Enable. |
| #define | [MDIO\_AN\_T1\_STAT\_LINK\_STATUS](group__ethernet__mdio.md#gac1f927e0b3fbd99a1f4a85bada0f7a94)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Link Status. |
| #define | [MDIO\_AN\_T1\_STAT\_ABLE](group__ethernet__mdio.md#ga912f2bddd1b8573e6420152e43060bdc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Auto-negotiation Ability. |
| #define | [MDIO\_AN\_T1\_STAT\_REMOTE\_FAULT](group__ethernet__mdio.md#ga7acdb2f35803d1f3e8e5ce2e340a6e30)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Auto-negotiation Remote Fault. |
| #define | [MDIO\_AN\_T1\_STAT\_COMPLETE](group__ethernet__mdio.md#ga5f1496d45ba3404aabd05ae9f574ade7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Auto-negotiation Complete. |
| #define | [MDIO\_AN\_T1\_STAT\_PAGE\_RX](group__ethernet__mdio.md#ga638f63292ab5ddd4e301ddd9e4d70418)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Page Received. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_PAUSE\_CAP](group__ethernet__mdio.md#ga404345912bcad2c6691483910928f85a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Pause Ability. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_PAUSE\_ASYM](group__ethernet__mdio.md#gae19eabc9238eae96ef8055f37fb0882e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Pause Ability. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_FORCE\_MS](group__ethernet__mdio.md#gaa227d9a74c324e64935e77811e7c2dcc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Force Master/Slave Configuration. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_REMOTE\_FAULT](group__ethernet__mdio.md#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Remote Fault. |
| #define | [MDIO\_AN\_T1\_ADV\_L\_ACK](group__ethernet__mdio.md#gaf6f17971533580a89bde8c52bc110363)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Acknowledge (ACK). |
| #define | [MDIO\_AN\_T1\_ADV\_L\_NEXT\_PAGE\_REQ](group__ethernet__mdio.md#gab69a2d9ebd289f792aba878bc831079a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Next Page Request. |
| #define | [MDIO\_AN\_T1\_ADV\_M\_B10L](group__ethernet__mdio.md#ga32e41aa9618bc858f9ca70fabef9bf37)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L Ability |
| #define | [MDIO\_AN\_T1\_ADV\_M\_MST](group__ethernet__mdio.md#ga2ada131bfc4e87d3c8993ce3d0ca2d48)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Master/slave Configuration. |
| #define | [MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI\_REQ](group__ethernet__mdio.md#ga534444217d2388e5d752d60a03ca68b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L High Level Transmit Operating Mode Request |
| #define | [MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI](group__ethernet__mdio.md#ga581d91721dd6f1aab1462c63df48d50a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | 10BASE-T1L High Level Transmit Operating Mode Ability |
| #define | [MDIO\_PMA\_PMD\_BT1\_CTRL\_CFG\_MST](group__ethernet__mdio.md#ga11863eaaeb876c1d3dc83d1ee9e045d2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | BASE-T1 master/slave configuration. |
| #define | [MDIO\_PMA\_B10L\_CTRL](group__ethernet__mdio.md#ga490f3bb0e91ddbe9783864040d2054a8)   0x08F6U |
|  | 10BASE-T1L PMA control |
| #define | [MDIO\_PMA\_B10L\_STAT](group__ethernet__mdio.md#ga17955956be0807edf50f24f3d6b1a175)   0x08F7U |
|  | 10BASE-T1L PMA status |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT](group__ethernet__mdio.md#gad55902f2a79193162459a6b90d508a41)   0x8302U |
|  | 10BASE-T1L PMA link status |
| #define | [MDIO\_PCS\_B10L\_CTRL](group__ethernet__mdio.md#gaafbb9fbd657bf59ee11a1c832ff4d4a0)   0x08E6U |
|  | 10BASE-T1L PCS control |
| #define | [MDIO\_PCS\_B10L\_STAT](group__ethernet__mdio.md#ga66181040f5b5d5301203914700d02dd7)   0x08E7U |
|  | 10BASE-T1L PCS status |
| #define | [MDIO\_PMA\_B10L\_CTRL\_TX\_DIS\_MODE\_EN](group__ethernet__mdio.md#ga0d68932ddfa3b8194b6b085def230aa4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L Transmit Disable Mode |
| #define | [MDIO\_PMA\_B10L\_CTRL\_TX\_LVL\_HI](group__ethernet__mdio.md#gae27e01f297d07281f2210f82ce1c41cb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L Transmit Voltage Amplitude Control |
| #define | [MDIO\_PMA\_B10L\_CTRL\_EEE](group__ethernet__mdio.md#ga1d8b5fa13bc9b3e685f5123614ceeac0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | 10BASE-T1L EEE Enable |
| #define | [MDIO\_PMA\_B10L\_CTRL\_LB\_PMA\_LOC\_EN](group__ethernet__mdio.md#gaf5e632085ce3efb8fbbd33ca166e577d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L PMA Loopback |
| #define | [MDIO\_PMA\_B10L\_STAT\_LINK](group__ethernet__mdio.md#gaa3e658df0baa6377224b1580a7d2bd1c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L PMA receive link up |
| #define | [MDIO\_PMA\_B10L\_STAT\_FAULT](group__ethernet__mdio.md#ga8a3919a982c3d7b038b4774aefec0289)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | 10BASE-T1L Fault condition detected |
| #define | [MDIO\_PMA\_B10L\_STAT\_POLARITY](group__ethernet__mdio.md#gafad692e7e73ca3ba3ee267915745aa5b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | 10BASE-T1L Receive polarity is reversed |
| #define | [MDIO\_PMA\_B10L\_STAT\_RECV\_FAULT](group__ethernet__mdio.md#ga1017896c84e1a32568f695bc84834894)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | 10BASE-T1L Able to detect fault on receive path |
| #define | [MDIO\_PMA\_B10L\_STAT\_EEE](group__ethernet__mdio.md#ga54bec9909ebcc69b84da93a6e7bdbba6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | 10BASE-T1L PHY has EEE ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_LOW\_POWER](group__ethernet__mdio.md#ga6f4c3046c404635897a188ccf6c364a5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | 10BASE-T1L PMA has low-power ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_2V4\_ABLE](group__ethernet__mdio.md#gab289ba626543006aebe04da57b53b050)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | 10BASE-T1L PHY has 2.4 Vpp operating mode ability |
| #define | [MDIO\_PMA\_B10L\_STAT\_LB\_ABLE](group__ethernet__mdio.md#gade5d7df4d74c0bcc3c6260d49d6d51a1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | 10BASE-T1L PHY has loopback ability |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK\_LL](group__ethernet__mdio.md#gaff70ac51be8f32a0cbcb5046f92a727f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | 10BASE-T1L Remote Receiver Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK](group__ethernet__mdio.md#gac03f000f6beef4a1debadaaca339b601)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | 10BASE-T1L Remote Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK\_LL](group__ethernet__mdio.md#ga51784a68c7a237a32d846723c01ec873)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | 10BASE-T1L Local Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK](group__ethernet__mdio.md#ga08ca50389a30a21148525c7d9b212b6f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | 10BASE-T1L Local Receiver Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK\_LL](group__ethernet__mdio.md#ga9b6a1e683e1cc964bc41cefbc2f9d91b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | 10BASE-T1L Descrambler Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK](group__ethernet__mdio.md#gabdd013ea8c586918c54c258a6f1ae2eb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | 10BASE-T1L Descrambler Status OK |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK\_LL](group__ethernet__mdio.md#ga987f6dabf90e98985d0d11b7392701fc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | 10BASE-T1L Link Status OK Latch Low |
| #define | [MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK](group__ethernet__mdio.md#gab7d5ca01e536e68d9f9b90b7f24d0bf5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | 10BASE-T1L Link Status OK |
| #define | [MDIO\_PCS\_B10L\_CTRL\_LB\_PCS\_EN](group__ethernet__mdio.md#ga6d2c4c50608d24fb8106841ca9a79714)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | 10BASE-T1L PCS Loopback Enable |
| #define | [MDIO\_PCS\_B10L\_STAT\_DSCR\_STAT\_OK\_LL](group__ethernet__mdio.md#gab6abfd0df706b72684124db458491d9b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | 10BASE-T1L PCS Descrambler Status |

| Enumerations | |
| --- | --- |
| enum | [mdio\_opcode](group__ethernet__mdio.md#ga304f668820ee91a63512c174e405b492) {     [MDIO\_OP\_C22\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d) = 1 , [MDIO\_OP\_C22\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46) = 2 , [MDIO\_OP\_C45\_ADDRESS](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371) = 0 , [MDIO\_OP\_C45\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f) = 1 ,     [MDIO\_OP\_C45\_READ\_INC](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd) = 2 , [MDIO\_OP\_C45\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1) = 3   } |
|  | MDIO transaction operation code. [More...](group__ethernet__mdio.md#ga304f668820ee91a63512c174e405b492) |

## Detailed Description

Definitions for IEEE 802.3 management interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mdio.h](net_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
