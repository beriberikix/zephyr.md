---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ethernet_8h_source.html
original_path: doxygen/html/ethernet_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet.h

[Go to the documentation of this file.](ethernet_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_ETHERNET\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_ETHERNET\_H\_

15

16#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/sys/atomic.h](atomic_8h.md)>

20

21#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

22#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

23

24#if defined(CONFIG\_NET\_LLDP)

25#include <[zephyr/net/lldp.h](lldp_8h.md)>

26#endif

27

28#include <[zephyr/sys/util.h](util_8h.md)>

29#include <[zephyr/net/net\_if.h](net__if_8h.md)>

30#include <[zephyr/net/ethernet\_vlan.h](ethernet__vlan_8h.md)>

31#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

32

33#if defined(CONFIG\_NET\_DSA)

34#include <[zephyr/net/dsa.h](dsa_8h.md)>

35#endif

36

37#if defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

38#include <[zephyr/net/ethernet\_bridge.h](ethernet__bridge_8h.md)>

39#endif

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

51

53

54struct net\_eth\_addr {

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr[6];

56};

57

58#define NET\_ETH\_HDR(pkt) ((struct net\_eth\_hdr \*)net\_pkt\_data(pkt))

59

60#define NET\_ETH\_PTYPE\_ARP 0x0806

61#define NET\_ETH\_PTYPE\_IP 0x0800

62#define NET\_ETH\_PTYPE\_TSN 0x22f0 /\* TSN (IEEE 1722) packet \*/

63#define NET\_ETH\_PTYPE\_IPV6 0x86dd

64#define NET\_ETH\_PTYPE\_VLAN 0x8100

65#define NET\_ETH\_PTYPE\_PTP 0x88f7

66#define NET\_ETH\_PTYPE\_LLDP 0x88cc

67#define NET\_ETH\_PTYPE\_ALL 0x0003 /\* from linux/if\_ether.h \*/

68#define NET\_ETH\_PTYPE\_ECAT 0x88a4

69#define NET\_ETH\_PTYPE\_EAPOL 0x888e

70#define NET\_ETH\_PTYPE\_IEEE802154 0x00F6 /\* from linux/if\_ether.h: IEEE802.15.4 frame \*/

71

72#if !defined(ETH\_P\_ALL)

73#define ETH\_P\_ALL NET\_ETH\_PTYPE\_ALL

74#endif

75#if !defined(ETH\_P\_IP)

76#define ETH\_P\_IP NET\_ETH\_PTYPE\_IP

77#endif

78#if !defined(ETH\_P\_ARP)

79#define ETH\_P\_ARP NET\_ETH\_PTYPE\_ARP

80#endif

81#if !defined(ETH\_P\_IPV6)

82#define ETH\_P\_IPV6 NET\_ETH\_PTYPE\_IPV6

83#endif

84#if !defined(ETH\_P\_8021Q)

85#define ETH\_P\_8021Q NET\_ETH\_PTYPE\_VLAN

86#endif

87#if !defined(ETH\_P\_TSN)

88#define ETH\_P\_TSN NET\_ETH\_PTYPE\_TSN

89#endif

90#if !defined(ETH\_P\_ECAT)

91#define ETH\_P\_ECAT NET\_ETH\_PTYPE\_ECAT

92#endif

93#if !defined(ETH\_P\_IEEE802154)

94#define ETH\_P\_IEEE802154 NET\_ETH\_PTYPE\_IEEE802154

95#endif

96

97#define NET\_ETH\_MINIMAL\_FRAME\_SIZE 60

98#define NET\_ETH\_MTU 1500

99

100#if defined(CONFIG\_NET\_VLAN)

101#define \_NET\_ETH\_MAX\_HDR\_SIZE (sizeof(struct net\_eth\_vlan\_hdr))

102#else

103#define \_NET\_ETH\_MAX\_HDR\_SIZE (sizeof(struct net\_eth\_hdr))

104#endif

105

106#define \_NET\_ETH\_MAX\_FRAME\_SIZE (NET\_ETH\_MTU + \_NET\_ETH\_MAX\_HDR\_SIZE)

107/\*

108 \* Extend the max frame size for DSA (KSZ8794) by one byte (to 1519) to

109 \* store tail tag.

110 \*/

111#if defined(CONFIG\_NET\_DSA)

112#define NET\_ETH\_MAX\_FRAME\_SIZE (\_NET\_ETH\_MAX\_FRAME\_SIZE + DSA\_TAG\_SIZE)

113#define NET\_ETH\_MAX\_HDR\_SIZE (\_NET\_ETH\_MAX\_HDR\_SIZE + DSA\_TAG\_SIZE)

114#else

115#define NET\_ETH\_MAX\_FRAME\_SIZE (\_NET\_ETH\_MAX\_FRAME\_SIZE)

116#define NET\_ETH\_MAX\_HDR\_SIZE (\_NET\_ETH\_MAX\_HDR\_SIZE)

117#endif

118

119#define NET\_ETH\_VLAN\_HDR\_SIZE 4

120

122

[ 124](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) {

[ 126](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) [ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

127

[ 129](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) [ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

130

[ 132](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) [ETHERNET\_HW\_VLAN](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

133

[ 135](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) [ETHERNET\_AUTO\_NEGOTIATION\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

136

[ 138](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) [ETHERNET\_LINK\_10BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

139

[ 141](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) [ETHERNET\_LINK\_100BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

142

[ 144](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) [ETHERNET\_LINK\_1000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

145

[ 147](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) [ETHERNET\_DUPLEX\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

148

[ 150](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) [ETHERNET\_PTP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

151

[ 153](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) [ETHERNET\_QAV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

154

[ 156](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) [ETHERNET\_PROMISC\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

157

[ 159](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) [ETHERNET\_PRIORITY\_QUEUES](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

160

[ 162](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) [ETHERNET\_HW\_FILTERING](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

163

[ 165](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) [ETHERNET\_LLDP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

166

[ 168](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) [ETHERNET\_HW\_VLAN\_TAG\_STRIP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

169

[ 171](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) [ETHERNET\_DSA\_SLAVE\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 172](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) [ETHERNET\_DSA\_MASTER\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

173

[ 175](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) [ETHERNET\_QBV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

176

[ 178](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) [ETHERNET\_QBU](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

179

[ 181](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) [ETHERNET\_TXTIME](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

182

[ 184](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) [ETHERNET\_TXINJECTION\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

185};

186

188

189enum ethernet\_config\_type {

190 ETHERNET\_CONFIG\_TYPE\_AUTO\_NEG,

191 ETHERNET\_CONFIG\_TYPE\_LINK,

192 ETHERNET\_CONFIG\_TYPE\_DUPLEX,

193 ETHERNET\_CONFIG\_TYPE\_MAC\_ADDRESS,

194 ETHERNET\_CONFIG\_TYPE\_QAV\_PARAM,

195 ETHERNET\_CONFIG\_TYPE\_QBV\_PARAM,

196 ETHERNET\_CONFIG\_TYPE\_QBU\_PARAM,

197 ETHERNET\_CONFIG\_TYPE\_TXTIME\_PARAM,

198 ETHERNET\_CONFIG\_TYPE\_PROMISC\_MODE,

199 ETHERNET\_CONFIG\_TYPE\_PRIORITY\_QUEUES\_NUM,

200 ETHERNET\_CONFIG\_TYPE\_FILTER,

201 ETHERNET\_CONFIG\_TYPE\_PORTS\_NUM,

202 ETHERNET\_CONFIG\_TYPE\_T1S\_PARAM,

203 ETHERNET\_CONFIG\_TYPE\_TXINJECTION\_MODE,

204};

205

206enum ethernet\_qav\_param\_type {

207 ETHERNET\_QAV\_PARAM\_TYPE\_DELTA\_BANDWIDTH,

208 ETHERNET\_QAV\_PARAM\_TYPE\_IDLE\_SLOPE,

209 ETHERNET\_QAV\_PARAM\_TYPE\_OPER\_IDLE\_SLOPE,

210 ETHERNET\_QAV\_PARAM\_TYPE\_TRAFFIC\_CLASS,

211 ETHERNET\_QAV\_PARAM\_TYPE\_STATUS,

212};

213

214enum ethernet\_t1s\_param\_type {

215 ETHERNET\_T1S\_PARAM\_TYPE\_PLCA\_CONFIG,

216};

217

[ 219](structethernet__t1s__param.md)struct [ethernet\_t1s\_param](structethernet__t1s__param.md) {

[ 221](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58) enum ethernet\_t1s\_param\_type [type](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58);

222 union {

223 /\* PLCA is the Physical Layer (PHY) Collision

224 \* Avoidance technique employed with multidrop

225 \* 10Base-T1S standard.

226 \*

227 \* The PLCA parameters are described in standard [1]

228 \* as registers in memory map 4 (MMS = 4) (point 9.6).

229 \*

230 \* IDVER (PLCA ID Version)

231 \* CTRL0 (PLCA Control 0)

232 \* CTRL1 (PLCA Control 1)

233 \* STATUS (PLCA Status)

234 \* TOTMR (PLCA TO Control)

235 \* BURST (PLCA Burst Control)

236 \*

237 \* Those registers are implemented by each OA TC6

238 \* compliant vendor (like for e.g. LAN865x - e.g. [2]).

239 \*

240 \* Documents:

241 \* [1] - "OPEN Alliance 10BASE-T1x MAC-PHY Serial

242 \* Interface" (ver. 1.1)

243 \* [2] - "DS60001734C" - LAN865x data sheet

244 \*/

245 struct {

[ 247](structethernet__t1s__param.md#add2f6115780c775a41da034443878955) bool [enable](structethernet__t1s__param.md#add2f6115780c775a41da034443878955);

[ 249](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_id](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9);

[ 251](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_count](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d);

[ 253](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_count](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd);

[ 255](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_timer](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71);

[ 257](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [to\_timer](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8);

[ 258](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808) } [plca](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808);

259 };

260};

261

[ 262](structethernet__qav__param.md)struct [ethernet\_qav\_param](structethernet__qav__param.md) {

[ 264](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba) int [queue\_id](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba);

[ 266](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8) enum ethernet\_qav\_param\_type [type](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8);

267 union {

[ 269](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85) bool [enabled](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85);

[ 271](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4) unsigned int [delta\_bandwidth](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4);

[ 273](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff) unsigned int [idle\_slope](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff);

[ 275](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477) unsigned int [oper\_idle\_slope](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477);

[ 277](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f) unsigned int [traffic\_class](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f);

278 };

279};

280

282

283enum ethernet\_qbv\_param\_type {

284 ETHERNET\_QBV\_PARAM\_TYPE\_STATUS,

285 ETHERNET\_QBV\_PARAM\_TYPE\_GATE\_CONTROL\_LIST,

286 ETHERNET\_QBV\_PARAM\_TYPE\_GATE\_CONTROL\_LIST\_LEN,

287 ETHERNET\_QBV\_PARAM\_TYPE\_TIME,

288};

289

290enum ethernet\_qbv\_state\_type {

291 ETHERNET\_QBV\_STATE\_TYPE\_ADMIN,

292 ETHERNET\_QBV\_STATE\_TYPE\_OPER,

293};

294

295enum ethernet\_gate\_state\_operation {

296 ETHERNET\_SET\_GATE\_STATE,

297 ETHERNET\_SET\_AND\_HOLD\_MAC\_STATE,

298 ETHERNET\_SET\_AND\_RELEASE\_MAC\_STATE,

299};

300

302

[ 303](structethernet__qbv__param.md)struct [ethernet\_qbv\_param](structethernet__qbv__param.md) {

[ 305](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd) int [port\_id](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd);

[ 307](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621) enum ethernet\_qbv\_param\_type [type](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621);

[ 309](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d) enum ethernet\_qbv\_state\_type [state](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d);

310 union {

[ 312](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064) bool [enabled](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064);

313

314 struct {

[ 316](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd) bool [gate\_status](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd)[NET\_TC\_TX\_COUNT];

317

[ 319](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7) enum ethernet\_gate\_state\_operation [operation](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7);

320

[ 322](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [time\_interval](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161);

323

[ 325](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [row](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c);

[ 326](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9) } [gate\_control](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9);

327

[ 329](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gate\_control\_list\_len](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e);

330

331 /\* The time values are set in one go when type is set to

332 \* ETHERNET\_QBV\_PARAM\_TYPE\_TIME

333 \*/

334 struct {

[ 336](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693) struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) [base\_time](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693);

337

[ 339](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be) struct [net\_ptp\_time](structnet__ptp__time.md) [cycle\_time](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be);

340

[ 342](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [extension\_time](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a);

343 };

344 };

345};

346

348

349enum ethernet\_qbu\_param\_type {

350 ETHERNET\_QBU\_PARAM\_TYPE\_STATUS,

351 ETHERNET\_QBU\_PARAM\_TYPE\_RELEASE\_ADVANCE,

352 ETHERNET\_QBU\_PARAM\_TYPE\_HOLD\_ADVANCE,

353 ETHERNET\_QBU\_PARAM\_TYPE\_PREEMPTION\_STATUS\_TABLE,

354

355 /\* Some preemption settings are from Qbr spec. \*/

356 ETHERNET\_QBR\_PARAM\_TYPE\_LINK\_PARTNER\_STATUS,

357 ETHERNET\_QBR\_PARAM\_TYPE\_ADDITIONAL\_FRAGMENT\_SIZE,

358};

359

360enum ethernet\_qbu\_preempt\_status {

361 ETHERNET\_QBU\_STATUS\_EXPRESS,

362 ETHERNET\_QBU\_STATUS\_PREEMPTABLE

363} \_\_packed;

364

366

[ 367](structethernet__qbu__param.md)struct [ethernet\_qbu\_param](structethernet__qbu__param.md) {

[ 369](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846) int [port\_id](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846);

[ 371](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a) enum ethernet\_qbu\_param\_type [type](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a);

372 union {

[ 374](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hold\_advance](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f);

375

[ 377](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [release\_advance](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b);

378

381 enum ethernet\_qbu\_preempt\_status

[ 382](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88) [frame\_preempt\_statuses](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)[NET\_TC\_TX\_COUNT];

383

[ 385](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5) bool [enabled](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5);

386

[ 388](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca) bool [link\_partner\_status](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca);

389

[ 393](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [additional\_fragment\_size](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb) : 2;

394 };

395};

396

397

399

400enum ethernet\_filter\_type {

401 ETHERNET\_FILTER\_TYPE\_SRC\_MAC\_ADDRESS,

402 ETHERNET\_FILTER\_TYPE\_DST\_MAC\_ADDRESS,

403};

404

406

[ 408](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc)enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) {

[ 410](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530) [L2\_ETH\_IF\_TYPE\_ETHERNET](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530),

411

[ 413](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671) [L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671),

414} \_\_packed;

415

416

[ 417](structethernet__filter.md)struct [ethernet\_filter](structethernet__filter.md) {

[ 419](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10) enum ethernet\_filter\_type [type](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10);

[ 421](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0) struct net\_eth\_addr [mac\_address](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0);

[ 423](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335) bool [set](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335);

424};

425

427

428enum ethernet\_txtime\_param\_type {

429 ETHERNET\_TXTIME\_PARAM\_TYPE\_ENABLE\_QUEUES,

430};

431

433

[ 434](structethernet__txtime__param.md)struct [ethernet\_txtime\_param](structethernet__txtime__param.md) {

[ 436](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99) enum ethernet\_txtime\_param\_type [type](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99);

[ 438](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165) int [queue\_id](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165);

[ 440](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27) bool [enable\_txtime](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27);

441};

442

444struct ethernet\_config {

445 union {

446 bool auto\_negotiation;

447 bool full\_duplex;

448 bool promisc\_mode;

449 bool txinjection\_mode;

450

451 struct {

452 bool link\_10bt;

453 bool link\_100bt;

454 bool link\_1000bt;

455 } l;

456

457 struct net\_eth\_addr mac\_address;

458

459 struct [ethernet\_t1s\_param](structethernet__t1s__param.md) t1s\_param;

460 struct [ethernet\_qav\_param](structethernet__qav__param.md) qav\_param;

461 struct [ethernet\_qbv\_param](structethernet__qbv__param.md) qbv\_param;

462 struct [ethernet\_qbu\_param](structethernet__qbu__param.md) qbu\_param;

463 struct [ethernet\_txtime\_param](structethernet__txtime__param.md) txtime\_param;

464

465 int priority\_queues\_num;

466 int ports\_num;

467

468 struct [ethernet\_filter](structethernet__filter.md) filter;

469 };

470};

472

[ 473](structethernet__api.md)struct [ethernet\_api](structethernet__api.md) {

[ 478](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056) struct net\_if\_api [iface\_api](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056);

479

480#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

485 struct [net\_stats\_eth](structnet__stats__eth.md) \*(\*get\_stats)(const struct [device](structdevice.md) \*dev);

486#endif

487

[ 489](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1) int (\*[start](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1))(const struct [device](structdevice.md) \*dev);

490

[ 492](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3) int (\*[stop](structethernet__api.md#a819599fe26b90860147ccfa86f337f84))(const struct [device](structdevice.md) \*dev);

493

495 enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) (\*[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3))(const struct [device](structdevice.md) \*dev);

496

[ 498](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1) int (\*[set\_config](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1))(const struct [device](structdevice.md) \*dev,

499 enum ethernet\_config\_type type,

500 const struct ethernet\_config \*config);

501

[ 503](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81) int (\*[get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81))(const struct [device](structdevice.md) \*dev,

504 enum ethernet\_config\_type type,

505 struct ethernet\_config \*config);

506

507#if defined(CONFIG\_NET\_VLAN)

513 int (\*vlan\_setup)(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface,

514 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag, bool enable);

515#endif /\* CONFIG\_NET\_VLAN \*/

516

517#if defined(CONFIG\_PTP\_CLOCK)

519 const struct [device](structdevice.md) \*(\*get\_ptp\_clock)(const struct [device](structdevice.md) \*dev);

520#endif /\* CONFIG\_PTP\_CLOCK \*/

521

[ 523](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241) int (\*[send](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

524};

525

526/\* Make sure that the network interface API is properly setup inside

527 \* Ethernet API struct (it is the first one).

528 \*/

529BUILD\_ASSERT(offsetof(struct [ethernet\_api](structethernet__api.md), iface\_api) == 0);

530

532struct net\_eth\_hdr {

533 struct net\_eth\_addr dst;

534 struct net\_eth\_addr src;

535 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type;

536} \_\_packed;

537

538struct ethernet\_vlan {

540 struct net\_if \*iface;

541

543 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag;

544};

545

546#if defined(CONFIG\_NET\_VLAN\_COUNT)

547#define NET\_VLAN\_MAX\_COUNT CONFIG\_NET\_VLAN\_COUNT

548#else

549/\* Even thou there are no VLAN support, the minimum count must be set to 1.

550 \*/

551#define NET\_VLAN\_MAX\_COUNT 1

552#endif

553

555

556#if defined(CONFIG\_NET\_LLDP)

557struct ethernet\_lldp {

559 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

560

562 const struct net\_lldpdu \*lldpdu;

563

565 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*optional\_du;

566

568 size\_t optional\_len;

569

571 struct net\_if \*iface;

572

574 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) tx\_timer\_start;

575

577 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx\_timer\_timeout;

578

580 [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) cb;

581};

582#endif /\* CONFIG\_NET\_LLDP \*/

583

[ 584](group__ethernet.md#ga97d926fe9e96a1205b00b808120dda88)enum [ethernet\_flags](group__ethernet.md#ga97d926fe9e96a1205b00b808120dda88) {

[ 585](group__ethernet.md#gga97d926fe9e96a1205b00b808120dda88ae630377e05a087a99649647593c38135) [ETH\_CARRIER\_UP](group__ethernet.md#gga97d926fe9e96a1205b00b808120dda88ae630377e05a087a99649647593c38135),

586};

587

[ 589](structethernet__context.md)struct [ethernet\_context](structethernet__context.md) {

[ 593](structethernet__context.md#a800f7b276341771addd3f1f1ffb5329b) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](structethernet__context.md#a800f7b276341771addd3f1f1ffb5329b);

594

595#if defined(CONFIG\_NET\_VLAN)

596 struct ethernet\_vlan vlan[NET\_VLAN\_MAX\_COUNT];

597

603 [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)(interfaces, NET\_VLAN\_MAX\_COUNT);

604#endif

605

606#if defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

607 struct [eth\_bridge\_iface\_context](structeth__bridge__iface__context.md) bridge;

608#endif

609

[ 616](structethernet__context.md#a4c152bdc054a3e86a5baedcf4e8eed1d) struct [k\_work](structk__work.md) [carrier\_work](structethernet__context.md#a4c152bdc054a3e86a5baedcf4e8eed1d);

617

[ 619](structethernet__context.md#a2358d48d02192220f2621dd96e353f37) struct [net\_if](structnet__if.md) \*[iface](structethernet__context.md#a2358d48d02192220f2621dd96e353f37);

620

621#if defined(CONFIG\_NET\_LLDP)

622 struct ethernet\_lldp lldp[NET\_VLAN\_MAX\_COUNT];

623#endif

624

[ 628](structethernet__context.md#a49f0358828531ab6e3cc398ebaf6f6f9) enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [ethernet\_l2\_flags](structethernet__context.md#a49f0358828531ab6e3cc398ebaf6f6f9);

629

630#if defined(CONFIG\_NET\_L2\_PTP)

635 int port;

636#endif

637

638#if defined(CONFIG\_NET\_DSA)

642 [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa) dsa\_recv\_cb;

643

645 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_port\_idx;

646

648 struct dsa\_context \*dsa\_ctx;

649

651 [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b) dsa\_send;

652#endif

653

654#if defined(CONFIG\_NET\_VLAN)

659 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) vlan\_enabled;

660#endif

661

[ 663](structethernet__context.md#a483abbb2e14fea59b01d6ee74466c702) bool [is\_net\_carrier\_up](structethernet__context.md#a483abbb2e14fea59b01d6ee74466c702) : 1;

664

[ 666](structethernet__context.md#ab7ea3afc9bd0ac19893d4a7edf2be057) bool [is\_init](structethernet__context.md#ab7ea3afc9bd0ac19893d4a7edf2be057) : 1;

667

[ 669](structethernet__context.md#a81e35df9b1648c1e2dc6234bb2eb2d76) enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) [eth\_if\_type](structethernet__context.md#a81e35df9b1648c1e2dc6234bb2eb2d76);

670};

671

[ 677](group__ethernet.md#gacd67360df806183cbc15159b0480bfa0)void [ethernet\_init](group__ethernet.md#gacd67360df806183cbc15159b0480bfa0)(struct [net\_if](structnet__if.md) \*iface);

678

680

681#define ETHERNET\_L2\_CTX\_TYPE struct ethernet\_context

682

683/\* Separate header for VLAN as some of device interfaces might not

684 \* support VLAN.

685 \*/

686struct net\_eth\_vlan\_hdr {

687 struct net\_eth\_addr dst;

688 struct net\_eth\_addr src;

689 struct {

690 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tpid; /\* tag protocol id \*/

691 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci; /\* tag control info \*/

692 } vlan;

693 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type;

694} \_\_packed;

695

696

697static inline bool net\_eth\_is\_addr\_broadcast(struct net\_eth\_addr \*addr)

698{

699 if (addr->addr[0] == 0xff &&

700 addr->addr[1] == 0xff &&

701 addr->addr[2] == 0xff &&

702 addr->addr[3] == 0xff &&

703 addr->addr[4] == 0xff &&

704 addr->addr[5] == 0xff) {

705 return true;

706 }

707

708 return false;

709}

710

711static inline bool net\_eth\_is\_addr\_unspecified(struct net\_eth\_addr \*addr)

712{

713 if (addr->addr[0] == 0x00 &&

714 addr->addr[1] == 0x00 &&

715 addr->addr[2] == 0x00 &&

716 addr->addr[3] == 0x00 &&

717 addr->addr[4] == 0x00 &&

718 addr->addr[5] == 0x00) {

719 return true;

720 }

721

722 return false;

723}

724

725static inline bool net\_eth\_is\_addr\_multicast(struct net\_eth\_addr \*addr)

726{

727#if defined(CONFIG\_NET\_IPV6)

728 if (addr->addr[0] == 0x33 &&

729 addr->addr[1] == 0x33) {

730 return true;

731 }

732#endif

733

734#if defined(CONFIG\_NET\_IPV4)

735 if (addr->addr[0] == 0x01 &&

736 addr->addr[1] == 0x00 &&

737 addr->addr[2] == 0x5e) {

738 return true;

739 }

740#endif

741

742 return false;

743}

744

745static inline bool net\_eth\_is\_addr\_group(struct net\_eth\_addr \*addr)

746{

747 return addr->addr[0] & 0x01;

748}

749

750static inline bool net\_eth\_is\_addr\_valid(struct net\_eth\_addr \*addr)

751{

752 return !net\_eth\_is\_addr\_unspecified(addr) && !net\_eth\_is\_addr\_group(addr);

753}

754

755static inline bool net\_eth\_is\_addr\_lldp\_multicast(struct net\_eth\_addr \*addr)

756{

757#if defined(CONFIG\_NET\_GPTP) || defined(CONFIG\_NET\_LLDP)

758 if (addr->addr[0] == 0x01 &&

759 addr->addr[1] == 0x80 &&

760 addr->addr[2] == 0xc2 &&

761 addr->addr[3] == 0x00 &&

762 addr->addr[4] == 0x00 &&

763 addr->addr[5] == 0x0e) {

764 return true;

765 }

766#endif

767

768 return false;

769}

770

771static inline bool net\_eth\_is\_addr\_ptp\_multicast(struct net\_eth\_addr \*addr)

772{

773#if defined(CONFIG\_NET\_GPTP)

774 if (addr->addr[0] == 0x01 &&

775 addr->addr[1] == 0x1b &&

776 addr->addr[2] == 0x19 &&

777 addr->addr[3] == 0x00 &&

778 addr->addr[4] == 0x00 &&

779 addr->addr[5] == 0x00) {

780 return true;

781 }

782#endif

783

784 return false;

785}

786

787const struct net\_eth\_addr \*net\_eth\_broadcast\_addr(void);

788

790

[ 797](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)void [net\_eth\_ipv4\_mcast\_to\_mac\_addr](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)(const struct [in\_addr](structin__addr.md) \*ipv4\_addr,

798 struct net\_eth\_addr \*mac\_addr);

799

[ 806](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)void [net\_eth\_ipv6\_mcast\_to\_mac\_addr](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)(const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr,

807 struct net\_eth\_addr \*mac\_addr);

808

816static inline

[ 817](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) [net\_eth\_get\_hw\_capabilities](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)(struct [net\_if](structnet__if.md) \*iface)

818{

819 const struct [ethernet\_api](structethernet__api.md) \*eth =

820 (struct [ethernet\_api](structethernet__api.md) \*)[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

821

822 if (!eth->[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)) {

823 return (enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5))0;

824 }

825

826 return eth->[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)([net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface));

827}

828

837#if defined(CONFIG\_NET\_VLAN)

838int [net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

839#else

[ 840](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)static inline int [net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

841{

842 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

843}

844#endif

845

854#if defined(CONFIG\_NET\_VLAN)

855int [net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

856#else

[ 857](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)static inline int [net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

858{

859 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

860}

861#endif

862

871#if defined(CONFIG\_NET\_VLAN)

872[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)(struct [net\_if](structnet__if.md) \*iface);

873#else

[ 874](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)(struct [net\_if](structnet__if.md) \*iface)

875{

876 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

877}

878#endif

879

890#if defined(CONFIG\_NET\_VLAN)

891struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

892#else

893static inline

[ 894](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

895{

896 return NULL;

897}

898#endif

899

908#if defined(CONFIG\_NET\_VLAN)

909bool [net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)(struct [ethernet\_context](structethernet__context.md) \*ctx,

910 struct [net\_if](structnet__if.md) \*iface);

911#else

[ 912](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)static inline bool [net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)(struct [ethernet\_context](structethernet__context.md) \*ctx,

913 struct [net\_if](structnet__if.md) \*iface)

914{

915 return false;

916}

917#endif

918

926#if defined(CONFIG\_NET\_VLAN)

927bool [net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)(struct [net\_if](structnet__if.md) \*iface);

928#else

[ 929](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)static inline bool [net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)(struct [net\_if](structnet__if.md) \*iface)

930{

931 return false;

932}

933#endif

934

935#if defined(CONFIG\_NET\_VLAN)

936#define Z\_ETH\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

937 config, prio, api, mtu) \

938 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

939 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

940 config, POST\_KERNEL, prio, api, \

941 &Z\_DEVICE\_STATE\_NAME(dev\_id)); \

942 NET\_L2\_DATA\_INIT(dev\_id, 0, NET\_L2\_GET\_CTX\_TYPE(ETHERNET\_L2)); \

943 NET\_IF\_INIT(dev\_id, 0, ETHERNET\_L2, mtu, NET\_VLAN\_MAX\_COUNT)

944

945#else /\* CONFIG\_NET\_VLAN \*/

946

947#define Z\_ETH\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

948 config, prio, api, mtu) \

949 Z\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

950 config, prio, api, ETHERNET\_L2, \

951 NET\_L2\_GET\_CTX\_TYPE(ETHERNET\_L2), mtu)

952#endif /\* CONFIG\_NET\_VLAN \*/

953

[ 971](group__ethernet.md#ga197e02748be8eaf410f7deb57c984642)#define ETH\_NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, \

972 prio, api, mtu) \

973 Z\_ETH\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, \

974 pm, data, config, prio, api, mtu)

975

[ 992](group__ethernet.md#ga9f67fee695953f24b1e5d9e49041aa99)#define ETH\_NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, \

993 prio, api, mtu) \

994 Z\_ETH\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

995 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

996 data, config, prio, api, mtu)

997

[ 1007](group__ethernet.md#gaecf9f102108836ed9cf7e2cdb3c90579)#define ETH\_NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

1008 ETH\_NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

1009

[ 1016](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)void [net\_eth\_carrier\_on](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)(struct [net\_if](structnet__if.md) \*iface);

1017

[ 1024](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)void [net\_eth\_carrier\_off](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)(struct [net\_if](structnet__if.md) \*iface);

1025

[ 1035](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)int [net\_eth\_promisc\_mode](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)(struct [net\_if](structnet__if.md) \*iface, bool enable);

1036

[ 1046](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)int [net\_eth\_txinjection\_mode](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)(struct [net\_if](structnet__if.md) \*iface, bool enable);

1047

1056#if defined(CONFIG\_PTP\_CLOCK)

1057const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)(struct [net\_if](structnet__if.md) \*iface);

1058#else

[ 1059](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)static inline const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)(struct [net\_if](structnet__if.md) \*iface)

1060{

1061 ARG\_UNUSED(iface);

1062

1063 return NULL;

1064}

1065#endif

1066

[ 1076](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)\_\_syscall const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock\_by\_index](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)(int index);

1077

1085#if defined(CONFIG\_NET\_L2\_PTP)

1086int [net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)(struct [net\_if](structnet__if.md) \*iface);

1087#else

[ 1088](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)static inline int [net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)(struct [net\_if](structnet__if.md) \*iface)

1089{

1090 ARG\_UNUSED(iface);

1091

1092 return -[ENODEV](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1);

1093}

1094#endif /\* CONFIG\_NET\_L2\_PTP \*/

1095

1102#if defined(CONFIG\_NET\_L2\_PTP)

1103void [net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)(struct [net\_if](structnet__if.md) \*iface, int port);

1104#else

[ 1105](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)static inline void [net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)(struct [net\_if](structnet__if.md) \*iface, int port)

1106{

1107 ARG\_UNUSED(iface);

1108 ARG\_UNUSED(port);

1109}

1110#endif /\* CONFIG\_NET\_L2\_PTP \*/

1111

[ 1119](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)static inline bool [net\_eth\_type\_is\_wifi](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)(struct [net\_if](structnet__if.md) \*iface)

1120{

1121 const struct [ethernet\_context](structethernet__context.md) \*ctx = (struct [ethernet\_context](structethernet__context.md) \*)

1122 [net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)([iface](structethernet__context.md#a2358d48d02192220f2621dd96e353f37));

1123

1124 return ctx->[eth\_if\_type](structethernet__context.md#a81e35df9b1648c1e2dc6234bb2eb2d76) == [L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671);

1125}

1126

1130

1131#ifdef \_\_cplusplus

1132}

1133#endif

1134

1135#include <syscalls/ethernet.h>

1136

1137#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[dsa.h](dsa_8h.md)

DSA definitions and handlers.

[ethernet\_bridge.h](ethernet__bridge_8h.md)

Ethernet Bridge public header file.

[ethernet\_vlan.h](ethernet__vlan_8h.md)

VLAN specific definitions.

[dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)

enum net\_verdict(\* dsa\_net\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

DSA (MGMT) Receive packet callback.

**Definition** dsa.h:68

[dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)

int(\* dsa\_send\_t)(const struct device \*dev, struct net\_pkt \*pkt)

Pointer to master interface send function.

**Definition** dsa.h:94

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc)

ethernet\_if\_types

Types of Ethernet L2.

**Definition** ethernet.h:408

[net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)

static void net\_eth\_set\_ptp\_port(struct net\_if \*iface, int port)

Set PTP port number attached to this interface.

**Definition** ethernet.h:1105

[net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)

static int net\_eth\_vlan\_enable(struct net\_if \*iface, uint16\_t tag)

Add VLAN tag to the interface.

**Definition** ethernet.h:840

[net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)

static int net\_eth\_get\_ptp\_port(struct net\_if \*iface)

Return PTP port number attached to this interface.

**Definition** ethernet.h:1088

[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)

static const struct device \* net\_eth\_get\_ptp\_clock(struct net\_if \*iface)

Return PTP clock that is tied to this ethernet network interface.

**Definition** ethernet.h:1059

[net\_eth\_promisc\_mode](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)

int net\_eth\_promisc\_mode(struct net\_if \*iface, bool enable)

Set promiscuous mode either ON or OFF.

[net\_eth\_carrier\_off](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)

void net\_eth\_carrier\_off(struct net\_if \*iface)

Inform ethernet L2 driver that ethernet carrier was lost.

[net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)

static uint16\_t net\_eth\_get\_vlan\_tag(struct net\_if \*iface)

Return VLAN tag specified to network interface.

**Definition** ethernet.h:874

[net\_eth\_type\_is\_wifi](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)

static bool net\_eth\_type\_is\_wifi(struct net\_if \*iface)

Check if the Ethernet L2 network interface can perform Wi-Fi.

**Definition** ethernet.h:1119

[net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)

static bool net\_eth\_get\_vlan\_status(struct net\_if \*iface)

Get VLAN status for a given network interface (enabled or not).

**Definition** ethernet.h:929

[net\_eth\_get\_ptp\_clock\_by\_index](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)

const struct device \* net\_eth\_get\_ptp\_clock\_by\_index(int index)

Return PTP clock that is tied to this ethernet network interface index.

[ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)

ethernet\_hw\_caps

Ethernet hardware capabilities.

**Definition** ethernet.h:124

[ethernet\_flags](group__ethernet.md#ga97d926fe9e96a1205b00b808120dda88)

ethernet\_flags

**Definition** ethernet.h:584

[net\_eth\_ipv6\_mcast\_to\_mac\_addr](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)

void net\_eth\_ipv6\_mcast\_to\_mac\_addr(const struct in6\_addr \*ipv6\_addr, struct net\_eth\_addr \*mac\_addr)

Convert IPv6 multicast address to Ethernet address.

[net\_eth\_get\_hw\_capabilities](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)

static enum ethernet\_hw\_caps net\_eth\_get\_hw\_capabilities(struct net\_if \*iface)

Return ethernet device hardware capability information.

**Definition** ethernet.h:817

[net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)

static int net\_eth\_vlan\_disable(struct net\_if \*iface, uint16\_t tag)

Remove VLAN tag from the interface.

**Definition** ethernet.h:857

[net\_eth\_carrier\_on](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)

void net\_eth\_carrier\_on(struct net\_if \*iface)

Inform ethernet L2 driver that ethernet carrier is detected.

[net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)

static bool net\_eth\_is\_vlan\_enabled(struct ethernet\_context \*ctx, struct net\_if \*iface)

Check if VLAN is enabled for a specific network interface.

**Definition** ethernet.h:912

[ethernet\_init](group__ethernet.md#gacd67360df806183cbc15159b0480bfa0)

void ethernet\_init(struct net\_if \*iface)

Initialize Ethernet L2 stack for a given interface.

[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)

static struct net\_if \* net\_eth\_get\_vlan\_iface(struct net\_if \*iface, uint16\_t tag)

Return network interface related to this VLAN tag.

**Definition** ethernet.h:894

[net\_eth\_ipv4\_mcast\_to\_mac\_addr](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)

void net\_eth\_ipv4\_mcast\_to\_mac\_addr(const struct in\_addr \*ipv4\_addr, struct net\_eth\_addr \*mac\_addr)

Convert IPv4 multicast address to Ethernet address.

[net\_eth\_txinjection\_mode](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)

int net\_eth\_txinjection\_mode(struct net\_if \*iface, bool enable)

Set TX-Injection mode either ON or OFF.

[L2\_ETH\_IF\_TYPE\_ETHERNET](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)

@ L2\_ETH\_IF\_TYPE\_ETHERNET

IEEE 802.3 Ethernet (default).

**Definition** ethernet.h:410

[L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)

@ L2\_ETH\_IF\_TYPE\_WIFI

IEEE 802.11 Wi-Fi.

**Definition** ethernet.h:413

[ETHERNET\_HW\_VLAN](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)

@ ETHERNET\_HW\_VLAN

VLAN supported.

**Definition** ethernet.h:132

[ETHERNET\_PRIORITY\_QUEUES](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)

@ ETHERNET\_PRIORITY\_QUEUES

Priority queues available.

**Definition** ethernet.h:159

[ETHERNET\_DUPLEX\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc)

@ ETHERNET\_DUPLEX\_SET

Changing duplex (half/full) supported.

**Definition** ethernet.h:147

[ETHERNET\_HW\_VLAN\_TAG\_STRIP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)

@ ETHERNET\_HW\_VLAN\_TAG\_STRIP

VLAN Tag stripping.

**Definition** ethernet.h:168

[ETHERNET\_LINK\_10BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6)

@ ETHERNET\_LINK\_10BASE\_T

10 Mbits link supported

**Definition** ethernet.h:138

[ETHERNET\_HW\_FILTERING](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)

@ ETHERNET\_HW\_FILTERING

MAC address filtering supported.

**Definition** ethernet.h:162

[ETHERNET\_PTP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a)

@ ETHERNET\_PTP

IEEE 802.1AS (gPTP) clock supported.

**Definition** ethernet.h:150

[ETHERNET\_QBU](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)

@ ETHERNET\_QBU

IEEE 802.1Qbu (frame preemption) supported.

**Definition** ethernet.h:178

[ETHERNET\_LINK\_100BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e)

@ ETHERNET\_LINK\_100BASE\_T

100 Mbits link supported

**Definition** ethernet.h:141

[ETHERNET\_DSA\_MASTER\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883)

@ ETHERNET\_DSA\_MASTER\_PORT

**Definition** ethernet.h:172

[ETHERNET\_DSA\_SLAVE\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7)

@ ETHERNET\_DSA\_SLAVE\_PORT

DSA switch.

**Definition** ethernet.h:171

[ETHERNET\_TXINJECTION\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)

@ ETHERNET\_TXINJECTION\_MODE

TX-Injection supported.

**Definition** ethernet.h:184

[ETHERNET\_QAV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)

@ ETHERNET\_QAV

IEEE 802.1Qav (credit-based shaping) supported.

**Definition** ethernet.h:153

[ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)

@ ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD

RX Checksum offloading supported for all of IPv4, UDP, TCP.

**Definition** ethernet.h:129

[ETHERNET\_LINK\_1000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8)

@ ETHERNET\_LINK\_1000BASE\_T

1 Gbits link supported

**Definition** ethernet.h:144

[ETHERNET\_LLDP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)

@ ETHERNET\_LLDP

Link Layer Discovery Protocol supported.

**Definition** ethernet.h:165

[ETHERNET\_AUTO\_NEGOTIATION\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a)

@ ETHERNET\_AUTO\_NEGOTIATION\_SET

Enabling/disabling auto negotiation supported.

**Definition** ethernet.h:135

[ETHERNET\_TXTIME](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)

@ ETHERNET\_TXTIME

TXTIME supported.

**Definition** ethernet.h:181

[ETHERNET\_QBV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)

@ ETHERNET\_QBV

IEEE 802.1Qbv (scheduled traffic) supported.

**Definition** ethernet.h:175

[ETHERNET\_PROMISC\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)

@ ETHERNET\_PROMISC\_MODE

Promiscuous mode supported.

**Definition** ethernet.h:156

[ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)

@ ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD

TX Checksum offloading supported for all of IPv4, UDP, TCP.

**Definition** ethernet.h:126

[ETH\_CARRIER\_UP](group__ethernet.md#gga97d926fe9e96a1205b00b808120dda88ae630377e05a087a99649647593c38135)

@ ETH\_CARRIER\_UP

**Definition** ethernet.h:585

[net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf)

enum net\_verdict(\* net\_lldp\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

LLDP Receive packet callback.

**Definition** lldp.h:213

[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)

static void \* net\_if\_l2\_data(struct net\_if \*iface)

Get a pointer to the interface L2 private data.

**Definition** net\_if.h:842

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:857

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:34

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENODEV](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1)

#define ENODEV

No such device.

**Definition** errno.h:58

[NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)

#define NET\_VLAN\_TAG\_UNSPEC

Unspecified VLAN tag value.

**Definition** ethernet\_vlan.h:30

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[lldp.h](lldp_8h.md)

LLDP definitions and handler.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[ptp\_time.h](ptp__time_8h.md)

Public functions for the Precision Time Protocol time specification.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[eth\_bridge\_iface\_context](structeth__bridge__iface__context.md)

**Definition** ethernet\_bridge.h:59

[ethernet\_api](structethernet__api.md)

**Definition** ethernet.h:473

[ethernet\_api::iface\_api](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** ethernet.h:478

[ethernet\_api::start](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** ethernet.h:489

[ethernet\_api::get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81)

int(\* get\_config)(const struct device \*dev, enum ethernet\_config\_type type, struct ethernet\_config \*config)

Get hardware specific configuration.

**Definition** ethernet.h:503

[ethernet\_api::stop](structethernet__api.md#a819599fe26b90860147ccfa86f337f84)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** ethernet.h:492

[ethernet\_api::get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)

enum ethernet\_hw\_caps(\* get\_capabilities)(const struct device \*dev)

Get the device capabilities.

**Definition** ethernet.h:495

[ethernet\_api::send](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

Send a network packet.

**Definition** ethernet.h:523

[ethernet\_api::set\_config](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1)

int(\* set\_config)(const struct device \*dev, enum ethernet\_config\_type type, const struct ethernet\_config \*config)

Set specific hardware configuration.

**Definition** ethernet.h:498

[ethernet\_context](structethernet__context.md)

Ethernet L2 context that is needed for VLAN.

**Definition** ethernet.h:589

[ethernet\_context::iface](structethernet__context.md#a2358d48d02192220f2621dd96e353f37)

struct net\_if \* iface

Network interface.

**Definition** ethernet.h:619

[ethernet\_context::is\_net\_carrier\_up](structethernet__context.md#a483abbb2e14fea59b01d6ee74466c702)

bool is\_net\_carrier\_up

Is network carrier up.

**Definition** ethernet.h:663

[ethernet\_context::ethernet\_l2\_flags](structethernet__context.md#a49f0358828531ab6e3cc398ebaf6f6f9)

enum net\_l2\_flags ethernet\_l2\_flags

This tells what L2 features does ethernet support.

**Definition** ethernet.h:628

[ethernet\_context::carrier\_work](structethernet__context.md#a4c152bdc054a3e86a5baedcf4e8eed1d)

struct k\_work carrier\_work

Carrier ON/OFF handler worker.

**Definition** ethernet.h:616

[ethernet\_context::flags](structethernet__context.md#a800f7b276341771addd3f1f1ffb5329b)

atomic\_t flags

Flags representing ethernet state, which are accessed from multiple threads.

**Definition** ethernet.h:593

[ethernet\_context::eth\_if\_type](structethernet__context.md#a81e35df9b1648c1e2dc6234bb2eb2d76)

enum ethernet\_if\_types eth\_if\_type

Types of Ethernet network interfaces.

**Definition** ethernet.h:669

[ethernet\_context::is\_init](structethernet__context.md#ab7ea3afc9bd0ac19893d4a7edf2be057)

bool is\_init

Is this context already initialized.

**Definition** ethernet.h:666

[ethernet\_filter](structethernet__filter.md)

**Definition** ethernet.h:417

[ethernet\_filter::mac\_address](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0)

struct net\_eth\_addr mac\_address

MAC address to filter.

**Definition** ethernet.h:421

[ethernet\_filter::set](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335)

bool set

Set (true) or unset (false) the filter.

**Definition** ethernet.h:423

[ethernet\_filter::type](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10)

enum ethernet\_filter\_type type

Type of filter.

**Definition** ethernet.h:419

[ethernet\_qav\_param](structethernet__qav__param.md)

**Definition** ethernet.h:262

[ethernet\_qav\_param::enabled](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85)

bool enabled

True if Qav is enabled for queue.

**Definition** ethernet.h:269

[ethernet\_qav\_param::oper\_idle\_slope](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477)

unsigned int oper\_idle\_slope

Oper Idle Slope (bits per second).

**Definition** ethernet.h:275

[ethernet\_qav\_param::type](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8)

enum ethernet\_qav\_param\_type type

Type of Qav parameter.

**Definition** ethernet.h:266

[ethernet\_qav\_param::traffic\_class](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f)

unsigned int traffic\_class

Traffic class the queue is bound to.

**Definition** ethernet.h:277

[ethernet\_qav\_param::queue\_id](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba)

int queue\_id

ID of the priority queue to use.

**Definition** ethernet.h:264

[ethernet\_qav\_param::idle\_slope](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff)

unsigned int idle\_slope

Idle Slope (bits per second).

**Definition** ethernet.h:273

[ethernet\_qav\_param::delta\_bandwidth](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4)

unsigned int delta\_bandwidth

Delta Bandwidth (percentage of bandwidth).

**Definition** ethernet.h:271

[ethernet\_qbu\_param](structethernet__qbu__param.md)

**Definition** ethernet.h:367

[ethernet\_qbu\_param::frame\_preempt\_statuses](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)

enum ethernet\_qbu\_preempt\_status frame\_preempt\_statuses[NET\_TC\_TX\_COUNT]

sequence of framePreemptionAdminStatus values.

**Definition** ethernet.h:381

[ethernet\_qbu\_param::release\_advance](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b)

uint32\_t release\_advance

Release advance (nanoseconds).

**Definition** ethernet.h:377

[ethernet\_qbu\_param::type](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a)

enum ethernet\_qbu\_param\_type type

Type of Qbu parameter.

**Definition** ethernet.h:371

[ethernet\_qbu\_param::hold\_advance](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f)

uint32\_t hold\_advance

Hold advance (nanoseconds).

**Definition** ethernet.h:374

[ethernet\_qbu\_param::enabled](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5)

bool enabled

True if Qbu is enabled or not.

**Definition** ethernet.h:385

[ethernet\_qbu\_param::link\_partner\_status](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca)

bool link\_partner\_status

Link partner status (from Qbr).

**Definition** ethernet.h:388

[ethernet\_qbu\_param::port\_id](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846)

int port\_id

Port id.

**Definition** ethernet.h:369

[ethernet\_qbu\_param::additional\_fragment\_size](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb)

uint8\_t additional\_fragment\_size

Additional fragment size (from Qbr).

**Definition** ethernet.h:393

[ethernet\_qbv\_param](structethernet__qbv__param.md)

**Definition** ethernet.h:303

[ethernet\_qbv\_param::port\_id](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd)

int port\_id

Port id.

**Definition** ethernet.h:305

[ethernet\_qbv\_param::enabled](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064)

bool enabled

True if Qbv is enabled or not.

**Definition** ethernet.h:312

[ethernet\_qbv\_param::type](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621)

enum ethernet\_qbv\_param\_type type

Type of Qbv parameter.

**Definition** ethernet.h:307

[ethernet\_qbv\_param::row](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c)

uint16\_t row

Gate control list row.

**Definition** ethernet.h:325

[ethernet\_qbv\_param::state](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d)

enum ethernet\_qbv\_state\_type state

What state (Admin/Oper) parameters are these.

**Definition** ethernet.h:309

[ethernet\_qbv\_param::gate\_status](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd)

bool gate\_status[NET\_TC\_TX\_COUNT]

True = open, False = closed.

**Definition** ethernet.h:316

[ethernet\_qbv\_param::base\_time](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693)

struct net\_ptp\_extended\_time base\_time

Base time.

**Definition** ethernet.h:336

[ethernet\_qbv\_param::extension\_time](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a)

uint32\_t extension\_time

Extension time (nanoseconds).

**Definition** ethernet.h:342

[ethernet\_qbv\_param::operation](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7)

enum ethernet\_gate\_state\_operation operation

GateState operation.

**Definition** ethernet.h:319

[ethernet\_qbv\_param::gate\_control](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9)

struct ethernet\_qbv\_param::@121175361150174144233316376176000350036121201324::@102147251204031207263025171335370313217251102106 gate\_control

[ethernet\_qbv\_param::time\_interval](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161)

uint32\_t time\_interval

Time interval ticks (nanoseconds).

**Definition** ethernet.h:322

[ethernet\_qbv\_param::cycle\_time](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be)

struct net\_ptp\_time cycle\_time

Cycle time.

**Definition** ethernet.h:339

[ethernet\_qbv\_param::gate\_control\_list\_len](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e)

uint32\_t gate\_control\_list\_len

Number of entries in gate control list.

**Definition** ethernet.h:329

[ethernet\_t1s\_param](structethernet__t1s__param.md)

**Definition** ethernet.h:219

[ethernet\_t1s\_param::burst\_count](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd)

uint8\_t burst\_count

T1S PLCA burst count range: 0x0 to 0xFF.

**Definition** ethernet.h:253

[ethernet\_t1s\_param::plca](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808)

struct ethernet\_t1s\_param::@045104211027030365347006377040354240151366265336::@055246010323023270273151373302031315361103011354 plca

[ethernet\_t1s\_param::node\_count](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d)

uint8\_t node\_count

T1S PLCA node count range: 1 to 255.

**Definition** ethernet.h:251

[ethernet\_t1s\_param::to\_timer](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8)

uint8\_t to\_timer

T1S PLCA TO value.

**Definition** ethernet.h:257

[ethernet\_t1s\_param::burst\_timer](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71)

uint8\_t burst\_timer

T1S PLCA burst timer.

**Definition** ethernet.h:255

[ethernet\_t1s\_param::node\_id](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9)

uint8\_t node\_id

T1S PLCA node id range: 0 to 254.

**Definition** ethernet.h:249

[ethernet\_t1s\_param::type](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58)

enum ethernet\_t1s\_param\_type type

Type of T1S parameter.

**Definition** ethernet.h:221

[ethernet\_t1s\_param::enable](structethernet__t1s__param.md#add2f6115780c775a41da034443878955)

bool enable

T1S PLCA enabled.

**Definition** ethernet.h:247

[ethernet\_txtime\_param](structethernet__txtime__param.md)

**Definition** ethernet.h:434

[ethernet\_txtime\_param::enable\_txtime](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27)

bool enable\_txtime

Enable or disable TXTIME per queue.

**Definition** ethernet.h:440

[ethernet\_txtime\_param::queue\_id](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165)

int queue\_id

Queue number for configuring TXTIME.

**Definition** ethernet.h:438

[ethernet\_txtime\_param::type](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99)

enum ethernet\_txtime\_param\_type type

Type of TXTIME parameter.

**Definition** ethernet.h:436

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[net\_ptp\_extended\_time](structnet__ptp__extended__time.md)

Generalized Precision Time Protocol Extended Timestamp format.

**Definition** ptp\_time.h:147

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:109

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:441

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet.h](ethernet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
