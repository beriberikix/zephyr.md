---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net_2mdio_8h_source.html
original_path: doxygen/html/net_2mdio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdio.h

[Go to the documentation of this file.](net_2mdio_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_MDIO\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_MDIO\_H\_

14

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 27](group__ethernet__mdio.md#ga304f668820ee91a63512c174e405b492)enum [mdio\_opcode](group__ethernet__mdio.md#ga304f668820ee91a63512c174e405b492) {

[ 29](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d) [MDIO\_OP\_C22\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d) = 1,

30

[ 32](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46) [MDIO\_OP\_C22\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46) = 2,

33

[ 35](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371) [MDIO\_OP\_C45\_ADDRESS](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371) = 0,

36

[ 38](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f) [MDIO\_OP\_C45\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f) = 1,

39

[ 41](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd) [MDIO\_OP\_C45\_READ\_INC](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd) = 2,

42

[ 44](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1) [MDIO\_OP\_C45\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1) = 3

45};

46

47/\* MDIO Manageable Device addresses \*/

[ 49](group__ethernet__mdio.md#ga2aa490a7b68e2ad92d01440a240c118e)#define MDIO\_MMD\_PMAPMD 0x01U

[ 51](group__ethernet__mdio.md#ga3e8b5218550de81211db3d78e16b5f7c)#define MDIO\_MMD\_WIS 0x02U

[ 53](group__ethernet__mdio.md#gab071c192b965230e107b7111fa901c23)#define MDIO\_MMD\_PCS 0x03U

[ 55](group__ethernet__mdio.md#ga7e34a58a18740b276e54095bae9b0421)#define MDIO\_MMD\_PHYXS 0x04U

[ 57](group__ethernet__mdio.md#gaa8e0fb0cf10bc5584d34eed46d3d21ff)#define MDIO\_MMD\_DTEXS 0x05U

[ 59](group__ethernet__mdio.md#gaf6a80fb3d3090cba631aad20026e23c1)#define MDIO\_MMD\_TC 0x06U

[ 61](group__ethernet__mdio.md#ga47459e9e120969a7fc3a7ada2abdd440)#define MDIO\_MMD\_AN 0x07U

[ 63](group__ethernet__mdio.md#ga991d5fc38be73371ac3b0bae8a04f63d)#define MDIO\_MMD\_SEPARATED\_PMA1 0x08U

[ 65](group__ethernet__mdio.md#gacde2c812689ada4b7006e1ab4262eaf2)#define MDIO\_MMD\_SEPARATED\_PMA2 0x09U

[ 67](group__ethernet__mdio.md#gaee49981a836d3b2a2cf12b3e4bb703b5)#define MDIO\_MMD\_SEPARATED\_PMA3 0x0AU

[ 69](group__ethernet__mdio.md#gac57c99dcb72884df7e538e2af1804244)#define MDIO\_MMD\_SEPARATED\_PMA4 0x0BU

[ 71](group__ethernet__mdio.md#gab8a03ec360a743225345dd6bb64882f1)#define MDIO\_MMD\_C22EXT 0x1DU

[ 73](group__ethernet__mdio.md#ga71e8d72d50c484557a2e39c622490956)#define MDIO\_MMD\_VENDOR\_SPECIFIC1 0x1EU

[ 75](group__ethernet__mdio.md#gaac45f28f75bcfeca861d06b99239cc77)#define MDIO\_MMD\_VENDOR\_SPECIFIC2 0x1FU

76

77/\* MDIO generic registers \*/

[ 79](group__ethernet__mdio.md#gaab4d7fa609d78bb982f2e0baae2facc9)#define MDIO\_CTRL1 0x0000U

[ 81](group__ethernet__mdio.md#ga684cd28a49124170c327f279db8ba512)#define MDIO\_STAT1 0x0001U

[ 83](group__ethernet__mdio.md#ga8a63e5b18fa478566b230f22172e998f)#define MDIO\_DEVID1 0x0002U

[ 85](group__ethernet__mdio.md#gaafa088ec5cbe2a4b4023a2c8310b1ae1)#define MDIO\_DEVID2 0x0003U

[ 87](group__ethernet__mdio.md#ga75c8d4845abbcb0d0b283dcf24ea684a)#define MDIO\_SPEED 0x0004U

[ 89](group__ethernet__mdio.md#ga210f57aa1971b2f77765fdc47a2b00f2)#define MDIO\_DEVS1 0x0005U

[ 91](group__ethernet__mdio.md#ga4d095f2392dd8d94ff014e510e164a16)#define MDIO\_DEVS2 0x0006U

[ 93](group__ethernet__mdio.md#ga3c3d4c2f16cfdd4f2a4f6781069b2395)#define MDIO\_CTRL2 0x0007U

[ 95](group__ethernet__mdio.md#ga1cc7343ad758f8c070f6b28b568e2a00)#define MDIO\_STAT2 0x0008U

[ 97](group__ethernet__mdio.md#gaead8a046d17d07f54cf5cae793cc7392)#define MDIO\_PKGID1 0x000EU

[ 99](group__ethernet__mdio.md#gadd799e84b3cc7a31f57962fe29a1800f)#define MDIO\_PKGID2 0x000FU

100

101

102/\* BASE-T1 registers \*/

[ 104](group__ethernet__mdio.md#ga52b4b4aac146d80fe6581f612878df09)#define MDIO\_AN\_T1\_CTRL 0x0200U

[ 106](group__ethernet__mdio.md#ga698a5175bfa98c727579e0be12204cff)#define MDIO\_AN\_T1\_STAT 0x0201U

[ 108](group__ethernet__mdio.md#ga69e18d3aafb29972b8746b2ca5e67b3b)#define MDIO\_AN\_T1\_ADV\_L 0x0202U

[ 110](group__ethernet__mdio.md#gad870783cb015fd3bf7e07a437b429ec6)#define MDIO\_AN\_T1\_ADV\_M 0x0203U

[ 112](group__ethernet__mdio.md#ga85201e69432f1749c9f29f351565d8f2)#define MDIO\_AN\_T1\_ADV\_H 0x0204U

[ 114](group__ethernet__mdio.md#ga8a2295bc2f17aa0444e302ebadb34f6b)#define MDIO\_PMA\_PMD\_BT1\_CTRL 0x0834U

115

116/\* BASE-T1 Auto-negotiation Control register \*/

[ 118](group__ethernet__mdio.md#gabef35b68eb8a6e27c90dc5c5ea2001aa)#define MDIO\_AN\_T1\_CTRL\_RESTART BIT(9)

[ 120](group__ethernet__mdio.md#gac186dd4bb083f29368b2af4750daece7)#define MDIO\_AN\_T1\_CTRL\_EN BIT(12)

121

122/\* BASE-T1 Auto-negotiation Status register \*/

[ 124](group__ethernet__mdio.md#gac1f927e0b3fbd99a1f4a85bada0f7a94)#define MDIO\_AN\_T1\_STAT\_LINK\_STATUS BIT(2)

[ 126](group__ethernet__mdio.md#ga912f2bddd1b8573e6420152e43060bdc)#define MDIO\_AN\_T1\_STAT\_ABLE BIT(3)

[ 128](group__ethernet__mdio.md#ga7acdb2f35803d1f3e8e5ce2e340a6e30)#define MDIO\_AN\_T1\_STAT\_REMOTE\_FAULT BIT(4)

[ 130](group__ethernet__mdio.md#ga5f1496d45ba3404aabd05ae9f574ade7)#define MDIO\_AN\_T1\_STAT\_COMPLETE BIT(5)

[ 132](group__ethernet__mdio.md#ga638f63292ab5ddd4e301ddd9e4d70418)#define MDIO\_AN\_T1\_STAT\_PAGE\_RX BIT(6)

133

134/\* BASE-T1 Auto-negotiation Advertisement register [15:0] \*/

[ 136](group__ethernet__mdio.md#ga404345912bcad2c6691483910928f85a)#define MDIO\_AN\_T1\_ADV\_L\_PAUSE\_CAP BIT(10)

[ 138](group__ethernet__mdio.md#gae19eabc9238eae96ef8055f37fb0882e)#define MDIO\_AN\_T1\_ADV\_L\_PAUSE\_ASYM BIT(11)

[ 140](group__ethernet__mdio.md#gaa227d9a74c324e64935e77811e7c2dcc)#define MDIO\_AN\_T1\_ADV\_L\_FORCE\_MS BIT(12)

[ 142](group__ethernet__mdio.md#gabc9d0dfa5a8e534f0b3c33a94ed0dd03)#define MDIO\_AN\_T1\_ADV\_L\_REMOTE\_FAULT BIT(13)

[ 144](group__ethernet__mdio.md#gaf6f17971533580a89bde8c52bc110363)#define MDIO\_AN\_T1\_ADV\_L\_ACK BIT(14)

[ 146](group__ethernet__mdio.md#gab69a2d9ebd289f792aba878bc831079a)#define MDIO\_AN\_T1\_ADV\_L\_NEXT\_PAGE\_REQ BIT(15)

147

148/\* BASE-T1 Auto-negotiation Advertisement register [31:16] \*/

[ 150](group__ethernet__mdio.md#ga32e41aa9618bc858f9ca70fabef9bf37)#define MDIO\_AN\_T1\_ADV\_M\_B10L BIT(14)

[ 152](group__ethernet__mdio.md#ga2ada131bfc4e87d3c8993ce3d0ca2d48)#define MDIO\_AN\_T1\_ADV\_M\_MST BIT(4)

153

154/\* BASE-T1 Auto-negotiation Advertisement register [47:32] \*/

[ 156](group__ethernet__mdio.md#ga534444217d2388e5d752d60a03ca68b0)#define MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI\_REQ BIT(12)

[ 158](group__ethernet__mdio.md#ga581d91721dd6f1aab1462c63df48d50a)#define MDIO\_AN\_T1\_ADV\_H\_10L\_TX\_HI BIT(13)

159

160/\* BASE-T1 PMA/PMD control register \*/

[ 162](group__ethernet__mdio.md#ga11863eaaeb876c1d3dc83d1ee9e045d2)#define MDIO\_PMA\_PMD\_BT1\_CTRL\_CFG\_MST BIT(14)

163

164

165/\* 10BASE-T1L registers \*/

[ 167](group__ethernet__mdio.md#ga490f3bb0e91ddbe9783864040d2054a8)#define MDIO\_PMA\_B10L\_CTRL 0x08F6U

[ 169](group__ethernet__mdio.md#ga17955956be0807edf50f24f3d6b1a175)#define MDIO\_PMA\_B10L\_STAT 0x08F7U

[ 171](group__ethernet__mdio.md#gad55902f2a79193162459a6b90d508a41)#define MDIO\_PMA\_B10L\_LINK\_STAT 0x8302U

[ 173](group__ethernet__mdio.md#gaafbb9fbd657bf59ee11a1c832ff4d4a0)#define MDIO\_PCS\_B10L\_CTRL 0x08E6U

[ 175](group__ethernet__mdio.md#ga66181040f5b5d5301203914700d02dd7)#define MDIO\_PCS\_B10L\_STAT 0x08E7U

176

177/\* 10BASE-T1L PMA control register \*/

[ 179](group__ethernet__mdio.md#ga0d68932ddfa3b8194b6b085def230aa4)#define MDIO\_PMA\_B10L\_CTRL\_TX\_DIS\_MODE\_EN BIT(14)

[ 181](group__ethernet__mdio.md#gae27e01f297d07281f2210f82ce1c41cb)#define MDIO\_PMA\_B10L\_CTRL\_TX\_LVL\_HI BIT(12)

[ 183](group__ethernet__mdio.md#ga1d8b5fa13bc9b3e685f5123614ceeac0)#define MDIO\_PMA\_B10L\_CTRL\_EEE BIT(10)

[ 185](group__ethernet__mdio.md#gaf5e632085ce3efb8fbbd33ca166e577d)#define MDIO\_PMA\_B10L\_CTRL\_LB\_PMA\_LOC\_EN BIT(0)

186

187/\* 10BASE-T1L PMA status register \*/

[ 189](group__ethernet__mdio.md#gaa3e658df0baa6377224b1580a7d2bd1c)#define MDIO\_PMA\_B10L\_STAT\_LINK BIT(0)

[ 191](group__ethernet__mdio.md#ga8a3919a982c3d7b038b4774aefec0289)#define MDIO\_PMA\_B10L\_STAT\_FAULT BIT(1)

[ 193](group__ethernet__mdio.md#gafad692e7e73ca3ba3ee267915745aa5b)#define MDIO\_PMA\_B10L\_STAT\_POLARITY BIT(2)

[ 195](group__ethernet__mdio.md#ga1017896c84e1a32568f695bc84834894)#define MDIO\_PMA\_B10L\_STAT\_RECV\_FAULT BIT(9)

[ 197](group__ethernet__mdio.md#ga54bec9909ebcc69b84da93a6e7bdbba6)#define MDIO\_PMA\_B10L\_STAT\_EEE BIT(10)

[ 199](group__ethernet__mdio.md#ga6f4c3046c404635897a188ccf6c364a5)#define MDIO\_PMA\_B10L\_STAT\_LOW\_POWER BIT(11)

[ 201](group__ethernet__mdio.md#gab289ba626543006aebe04da57b53b050)#define MDIO\_PMA\_B10L\_STAT\_2V4\_ABLE BIT(12)

[ 203](group__ethernet__mdio.md#gade5d7df4d74c0bcc3c6260d49d6d51a1)#define MDIO\_PMA\_B10L\_STAT\_LB\_ABLE BIT(13)

204

205/\* 10BASE-T1L PMA link status\*/

[ 207](group__ethernet__mdio.md#gaff70ac51be8f32a0cbcb5046f92a727f)#define MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK\_LL BIT(9)

[ 209](group__ethernet__mdio.md#gac03f000f6beef4a1debadaaca339b601)#define MDIO\_PMA\_B10L\_LINK\_STAT\_REM\_RCVR\_STAT\_OK BIT(8)

[ 211](group__ethernet__mdio.md#ga51784a68c7a237a32d846723c01ec873)#define MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK\_LL BIT(7)

[ 213](group__ethernet__mdio.md#ga08ca50389a30a21148525c7d9b212b6f)#define MDIO\_PMA\_B10L\_LINK\_STAT\_LOC\_RCVR\_STAT\_OK BIT(6)

[ 215](group__ethernet__mdio.md#ga9b6a1e683e1cc964bc41cefbc2f9d91b)#define MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK\_LL BIT(5)

[ 217](group__ethernet__mdio.md#gabdd013ea8c586918c54c258a6f1ae2eb)#define MDIO\_PMA\_B10L\_LINK\_STAT\_DSCR\_STAT\_OK BIT(4)

[ 219](group__ethernet__mdio.md#ga987f6dabf90e98985d0d11b7392701fc)#define MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK\_LL BIT(1)

[ 221](group__ethernet__mdio.md#gab7d5ca01e536e68d9f9b90b7f24d0bf5)#define MDIO\_PMA\_B10L\_LINK\_STAT\_LINK\_STAT\_OK BIT(0)

222

223/\* 10BASE-T1L PCS control \*/

[ 225](group__ethernet__mdio.md#ga6d2c4c50608d24fb8106841ca9a79714)#define MDIO\_PCS\_B10L\_CTRL\_LB\_PCS\_EN BIT(14)

226

227/\* 10BASE-T1L PCS status \*/

[ 229](group__ethernet__mdio.md#gab6abfd0df706b72684124db458491d9b)#define MDIO\_PCS\_B10L\_STAT\_DSCR\_STAT\_OK\_LL BIT(2)

230

231#ifdef \_\_cplusplus

232}

233#endif

234

238

239#endif /\* ZEPHYR\_INCLUDE\_NET\_MDIO\_H\_ \*/

[mdio\_opcode](group__ethernet__mdio.md#ga304f668820ee91a63512c174e405b492)

mdio\_opcode

MDIO transaction operation code.

**Definition** mdio.h:27

[MDIO\_OP\_C45\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a0335bfebfd1557bc33cac6daedbf11b1)

@ MDIO\_OP\_C45\_READ

IEEE 802.3 45.3.4 read operation.

**Definition** mdio.h:44

[MDIO\_OP\_C22\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1792985f314fb97951befbd6bef29e6d)

@ MDIO\_OP\_C22\_WRITE

IEEE 802.3 22.2.4.5.4 write operation.

**Definition** mdio.h:29

[MDIO\_OP\_C22\_READ](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a1990de139b54d7e17f57245ad254db46)

@ MDIO\_OP\_C22\_READ

IEEE 802.3 22.2.4.5.4 read operation.

**Definition** mdio.h:32

[MDIO\_OP\_C45\_READ\_INC](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492a2b901e2c23d60d424ec9c9d2610483dd)

@ MDIO\_OP\_C45\_READ\_INC

IEEE 802.3 45.3.4 post-read-increment-address operation.

**Definition** mdio.h:41

[MDIO\_OP\_C45\_ADDRESS](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492ad6ad469f50d382878c1d1b57c2a6a371)

@ MDIO\_OP\_C45\_ADDRESS

IEEE 802.3 45.3.4 address operation.

**Definition** mdio.h:35

[MDIO\_OP\_C45\_WRITE](group__ethernet__mdio.md#gga304f668820ee91a63512c174e405b492af969ce4b1ebc4dd291edc4c14f6c551f)

@ MDIO\_OP\_C45\_WRITE

IEEE 802.3 45.3.4 write operation.

**Definition** mdio.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mdio.h](net_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
