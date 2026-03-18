---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ethernet_8h_source.html
original_path: doxygen/html/ethernet_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

20

21#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

22#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

23#include <[zephyr/net/lldp.h](lldp_8h.md)>

24#include <[zephyr/sys/util.h](util_8h.md)>

25#include <[zephyr/net/net\_if.h](net__if_8h.md)>

26#include <[zephyr/net/ethernet\_vlan.h](ethernet__vlan_8h.md)>

27#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

28

29#if defined(CONFIG\_NET\_DSA)

30#include <[zephyr/net/dsa.h](dsa_8h.md)>

31#endif

32

33#if defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

34#include <[zephyr/net/ethernet\_bridge.h](ethernet__bridge_8h.md)>

35#endif

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

47

[ 48](group__ethernet.md#ga399425f810c00bcf9babec019bc2ff12)#define NET\_ETH\_ADDR\_LEN 6U

49

[ 51](structnet__eth__addr.md)struct [net\_eth\_addr](structnet__eth__addr.md) {

[ 52](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[[NET\_ETH\_ADDR\_LEN](group__ethernet.md#ga399425f810c00bcf9babec019bc2ff12)];

53};

54

56

57#define NET\_ETH\_HDR(pkt) ((struct net\_eth\_hdr \*)net\_pkt\_data(pkt))

58

59#define NET\_ETH\_PTYPE\_CAN 0x000C /\* CAN: Controller Area Network \*/

60#define NET\_ETH\_PTYPE\_CANFD 0x000D /\* CANFD: CAN flexible data rate\*/

61#define NET\_ETH\_PTYPE\_HDLC 0x0019 /\* HDLC frames (like in PPP) \*/

62#define NET\_ETH\_PTYPE\_ARP 0x0806

63#define NET\_ETH\_PTYPE\_IP 0x0800

64#define NET\_ETH\_PTYPE\_TSN 0x22f0 /\* TSN (IEEE 1722) packet \*/

65#define NET\_ETH\_PTYPE\_IPV6 0x86dd

66#define NET\_ETH\_PTYPE\_VLAN 0x8100

67#define NET\_ETH\_PTYPE\_PTP 0x88f7

68#define NET\_ETH\_PTYPE\_LLDP 0x88cc

69#define NET\_ETH\_PTYPE\_ALL 0x0003 /\* from linux/if\_ether.h \*/

70#define NET\_ETH\_PTYPE\_ECAT 0x88a4

71#define NET\_ETH\_PTYPE\_EAPOL 0x888e

72#define NET\_ETH\_PTYPE\_IEEE802154 0x00F6 /\* from linux/if\_ether.h: IEEE802.15.4 frame \*/

73

74#if !defined(ETH\_P\_ALL)

75#define ETH\_P\_ALL NET\_ETH\_PTYPE\_ALL

76#endif

77#if !defined(ETH\_P\_IP)

78#define ETH\_P\_IP NET\_ETH\_PTYPE\_IP

79#endif

80#if !defined(ETH\_P\_ARP)

81#define ETH\_P\_ARP NET\_ETH\_PTYPE\_ARP

82#endif

83#if !defined(ETH\_P\_IPV6)

84#define ETH\_P\_IPV6 NET\_ETH\_PTYPE\_IPV6

85#endif

86#if !defined(ETH\_P\_8021Q)

87#define ETH\_P\_8021Q NET\_ETH\_PTYPE\_VLAN

88#endif

89#if !defined(ETH\_P\_TSN)

90#define ETH\_P\_TSN NET\_ETH\_PTYPE\_TSN

91#endif

92#if !defined(ETH\_P\_ECAT)

93#define ETH\_P\_ECAT NET\_ETH\_PTYPE\_ECAT

94#endif

95#if !defined(ETH\_P\_EAPOL)

96#define ETH\_P\_EAPOL NET\_ETH\_PTYPE\_EAPOL

97#endif

98#if !defined(ETH\_P\_IEEE802154)

99#define ETH\_P\_IEEE802154 NET\_ETH\_PTYPE\_IEEE802154

100#endif

101#if !defined(ETH\_P\_CAN)

102#define ETH\_P\_CAN NET\_ETH\_PTYPE\_CAN

103#endif

104#if !defined(ETH\_P\_CANFD)

105#define ETH\_P\_CANFD NET\_ETH\_PTYPE\_CANFD

106#endif

107#if !defined(ETH\_P\_HDLC)

108#define ETH\_P\_HDLC NET\_ETH\_PTYPE\_HDLC

109#endif

110

112

[ 113](group__ethernet.md#ga4cc1bb4cfa00b7749838eae3ae11048c)#define NET\_ETH\_MINIMAL\_FRAME\_SIZE 60

[ 114](group__ethernet.md#gaa337199b1edc50c9003afa5c3a951d8b)#define NET\_ETH\_MTU 1500

115

117

118#if defined(CONFIG\_NET\_VLAN)

119#define \_NET\_ETH\_MAX\_HDR\_SIZE (sizeof(struct net\_eth\_vlan\_hdr))

120#else

121#define \_NET\_ETH\_MAX\_HDR\_SIZE (sizeof(struct net\_eth\_hdr))

122#endif

123

124#define \_NET\_ETH\_MAX\_FRAME\_SIZE (NET\_ETH\_MTU + \_NET\_ETH\_MAX\_HDR\_SIZE)

125/\*

126 \* Extend the max frame size for DSA (KSZ8794) by one byte (to 1519) to

127 \* store tail tag.

128 \*/

129#if defined(CONFIG\_NET\_DSA)

130#define NET\_ETH\_MAX\_FRAME\_SIZE (\_NET\_ETH\_MAX\_FRAME\_SIZE + DSA\_TAG\_SIZE)

131#define NET\_ETH\_MAX\_HDR\_SIZE (\_NET\_ETH\_MAX\_HDR\_SIZE + DSA\_TAG\_SIZE)

132#else

133#define NET\_ETH\_MAX\_FRAME\_SIZE (\_NET\_ETH\_MAX\_FRAME\_SIZE)

134#define NET\_ETH\_MAX\_HDR\_SIZE (\_NET\_ETH\_MAX\_HDR\_SIZE)

135#endif

136

137#define NET\_ETH\_VLAN\_HDR\_SIZE 4

138

140

[ 142](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) {

[ 144](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) [ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

145

[ 147](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) [ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

148

[ 150](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) [ETHERNET\_HW\_VLAN](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

151

[ 153](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) [ETHERNET\_AUTO\_NEGOTIATION\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

154

[ 156](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) [ETHERNET\_LINK\_10BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

157

[ 159](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) [ETHERNET\_LINK\_100BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

160

[ 162](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) [ETHERNET\_LINK\_1000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

163

[ 165](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) [ETHERNET\_DUPLEX\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

166

[ 168](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) [ETHERNET\_PTP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

169

[ 171](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) [ETHERNET\_QAV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

172

[ 174](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) [ETHERNET\_PROMISC\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

175

[ 177](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) [ETHERNET\_PRIORITY\_QUEUES](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

178

[ 180](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) [ETHERNET\_HW\_FILTERING](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

181

[ 183](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) [ETHERNET\_LLDP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

184

[ 186](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) [ETHERNET\_HW\_VLAN\_TAG\_STRIP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

187

[ 189](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) [ETHERNET\_DSA\_SLAVE\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

190

[ 192](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) [ETHERNET\_DSA\_MASTER\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

193

[ 195](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) [ETHERNET\_QBV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

196

[ 198](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) [ETHERNET\_QBU](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

199

[ 201](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) [ETHERNET\_TXTIME](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

202

[ 204](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) [ETHERNET\_TXINJECTION\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

205};

206

208

209enum ethernet\_config\_type {

210 ETHERNET\_CONFIG\_TYPE\_AUTO\_NEG,

211 ETHERNET\_CONFIG\_TYPE\_LINK,

212 ETHERNET\_CONFIG\_TYPE\_DUPLEX,

213 ETHERNET\_CONFIG\_TYPE\_MAC\_ADDRESS,

214 ETHERNET\_CONFIG\_TYPE\_QAV\_PARAM,

215 ETHERNET\_CONFIG\_TYPE\_QBV\_PARAM,

216 ETHERNET\_CONFIG\_TYPE\_QBU\_PARAM,

217 ETHERNET\_CONFIG\_TYPE\_TXTIME\_PARAM,

218 ETHERNET\_CONFIG\_TYPE\_PROMISC\_MODE,

219 ETHERNET\_CONFIG\_TYPE\_PRIORITY\_QUEUES\_NUM,

220 ETHERNET\_CONFIG\_TYPE\_FILTER,

221 ETHERNET\_CONFIG\_TYPE\_PORTS\_NUM,

222 ETHERNET\_CONFIG\_TYPE\_T1S\_PARAM,

223 ETHERNET\_CONFIG\_TYPE\_TXINJECTION\_MODE,

224 ETHERNET\_CONFIG\_TYPE\_RX\_CHECKSUM\_SUPPORT,

225 ETHERNET\_CONFIG\_TYPE\_TX\_CHECKSUM\_SUPPORT

226};

227

228enum ethernet\_qav\_param\_type {

229 ETHERNET\_QAV\_PARAM\_TYPE\_DELTA\_BANDWIDTH,

230 ETHERNET\_QAV\_PARAM\_TYPE\_IDLE\_SLOPE,

231 ETHERNET\_QAV\_PARAM\_TYPE\_OPER\_IDLE\_SLOPE,

232 ETHERNET\_QAV\_PARAM\_TYPE\_TRAFFIC\_CLASS,

233 ETHERNET\_QAV\_PARAM\_TYPE\_STATUS,

234};

235

236enum ethernet\_t1s\_param\_type {

237 ETHERNET\_T1S\_PARAM\_TYPE\_PLCA\_CONFIG,

238};

239

241

[ 243](structethernet__t1s__param.md)struct [ethernet\_t1s\_param](structethernet__t1s__param.md) {

[ 245](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58) enum ethernet\_t1s\_param\_type [type](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58);

246 union {

270 struct {

[ 272](structethernet__t1s__param.md#add2f6115780c775a41da034443878955) bool [enable](structethernet__t1s__param.md#add2f6115780c775a41da034443878955);

[ 274](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_id](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9);

[ 276](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_count](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d);

[ 278](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_count](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd);

[ 280](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_timer](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71);

[ 282](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [to\_timer](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8);

[ 283](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808) } [plca](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808);

284 };

285};

286

[ 288](structethernet__qav__param.md)struct [ethernet\_qav\_param](structethernet__qav__param.md) {

[ 290](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba) int [queue\_id](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba);

[ 292](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8) enum ethernet\_qav\_param\_type [type](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8);

293 union {

[ 295](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85) bool [enabled](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85);

[ 297](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4) unsigned int [delta\_bandwidth](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4);

[ 299](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff) unsigned int [idle\_slope](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff);

[ 301](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477) unsigned int [oper\_idle\_slope](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477);

[ 303](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f) unsigned int [traffic\_class](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f);

304 };

305};

306

308

309enum ethernet\_qbv\_param\_type {

310 ETHERNET\_QBV\_PARAM\_TYPE\_STATUS,

311 ETHERNET\_QBV\_PARAM\_TYPE\_GATE\_CONTROL\_LIST,

312 ETHERNET\_QBV\_PARAM\_TYPE\_GATE\_CONTROL\_LIST\_LEN,

313 ETHERNET\_QBV\_PARAM\_TYPE\_TIME,

314};

315

316enum ethernet\_qbv\_state\_type {

317 ETHERNET\_QBV\_STATE\_TYPE\_ADMIN,

318 ETHERNET\_QBV\_STATE\_TYPE\_OPER,

319};

320

321enum ethernet\_gate\_state\_operation {

322 ETHERNET\_SET\_GATE\_STATE,

323 ETHERNET\_SET\_AND\_HOLD\_MAC\_STATE,

324 ETHERNET\_SET\_AND\_RELEASE\_MAC\_STATE,

325};

326

328

[ 330](structethernet__qbv__param.md)struct [ethernet\_qbv\_param](structethernet__qbv__param.md) {

[ 332](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd) int [port\_id](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd);

[ 334](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621) enum ethernet\_qbv\_param\_type [type](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621);

[ 336](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d) enum ethernet\_qbv\_state\_type [state](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d);

337 union {

[ 339](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064) bool [enabled](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064);

340

342 struct {

[ 344](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd) bool [gate\_status](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd)[NET\_TC\_TX\_COUNT];

345

[ 347](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7) enum ethernet\_gate\_state\_operation [operation](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7);

348

[ 350](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [time\_interval](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161);

351

[ 353](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [row](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c);

[ 354](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9) } [gate\_control](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9);

355

[ 357](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gate\_control\_list\_len](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e);

358

363 struct {

[ 365](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693) struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) [base\_time](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693);

366

[ 368](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be) struct [net\_ptp\_time](structnet__ptp__time.md) [cycle\_time](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be);

369

[ 371](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [extension\_time](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a);

372 };

373 };

374};

375

377

378enum ethernet\_qbu\_param\_type {

379 ETHERNET\_QBU\_PARAM\_TYPE\_STATUS,

380 ETHERNET\_QBU\_PARAM\_TYPE\_RELEASE\_ADVANCE,

381 ETHERNET\_QBU\_PARAM\_TYPE\_HOLD\_ADVANCE,

382 ETHERNET\_QBU\_PARAM\_TYPE\_PREEMPTION\_STATUS\_TABLE,

383

384 /\* Some preemption settings are from Qbr spec. \*/

385 ETHERNET\_QBR\_PARAM\_TYPE\_LINK\_PARTNER\_STATUS,

386 ETHERNET\_QBR\_PARAM\_TYPE\_ADDITIONAL\_FRAGMENT\_SIZE,

387};

388

389enum ethernet\_qbu\_preempt\_status {

390 ETHERNET\_QBU\_STATUS\_EXPRESS,

391 ETHERNET\_QBU\_STATUS\_PREEMPTABLE

392} \_\_packed;

393

395

[ 397](structethernet__qbu__param.md)struct [ethernet\_qbu\_param](structethernet__qbu__param.md) {

[ 399](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846) int [port\_id](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846);

[ 401](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a) enum ethernet\_qbu\_param\_type [type](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a);

402 union {

[ 404](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hold\_advance](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f);

405

[ 407](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [release\_advance](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b);

408

410 enum ethernet\_qbu\_preempt\_status

[ 411](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88) [frame\_preempt\_statuses](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)[NET\_TC\_TX\_COUNT];

412

[ 414](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5) bool [enabled](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5);

415

[ 417](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca) bool [link\_partner\_status](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca);

418

[ 423](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [additional\_fragment\_size](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb) : 2;

424 };

425};

426

428

429enum ethernet\_filter\_type {

430 ETHERNET\_FILTER\_TYPE\_SRC\_MAC\_ADDRESS,

431 ETHERNET\_FILTER\_TYPE\_DST\_MAC\_ADDRESS,

432};

433

435

[ 437](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc)enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) {

[ 439](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530) [L2\_ETH\_IF\_TYPE\_ETHERNET](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530),

440

[ 442](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671) [L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671),

443} \_\_packed;

444

[ 446](structethernet__filter.md)struct [ethernet\_filter](structethernet__filter.md) {

[ 448](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10) enum ethernet\_filter\_type [type](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10);

[ 450](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0) struct [net\_eth\_addr](structnet__eth__addr.md) [mac\_address](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0);

[ 452](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335) bool [set](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335);

453};

454

456

457enum ethernet\_txtime\_param\_type {

458 ETHERNET\_TXTIME\_PARAM\_TYPE\_ENABLE\_QUEUES,

459};

460

462

[ 464](structethernet__txtime__param.md)struct [ethernet\_txtime\_param](structethernet__txtime__param.md) {

[ 466](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99) enum ethernet\_txtime\_param\_type [type](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99);

[ 468](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165) int [queue\_id](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165);

[ 470](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27) bool [enable\_txtime](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27);

471};

472

[ 474](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede)enum [ethernet\_checksum\_support](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede) {

[ 476](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d) [ETHERNET\_CHECKSUM\_SUPPORT\_NONE](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d) = NET\_IF\_CHECKSUM\_NONE\_BIT,

[ 478](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4) [ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT,

[ 480](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9) [ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT,

[ 482](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5) [ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT,

[ 484](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be) [ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT,

[ 486](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02) [ETHERNET\_CHECKSUM\_SUPPORT\_TCP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02) = NET\_IF\_CHECKSUM\_TCP\_BIT,

[ 488](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8) [ETHERNET\_CHECKSUM\_SUPPORT\_UDP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8) = NET\_IF\_CHECKSUM\_UDP\_BIT,

489};

490

492

493struct ethernet\_config {

494 union {

495 bool auto\_negotiation;

496 bool full\_duplex;

497 bool promisc\_mode;

498 bool txinjection\_mode;

499

500 struct {

501 bool link\_10bt;

502 bool link\_100bt;

503 bool link\_1000bt;

504 } l;

505

506 struct net\_eth\_addr mac\_address;

507

508 struct ethernet\_t1s\_param t1s\_param;

509 struct ethernet\_qav\_param qav\_param;

510 struct ethernet\_qbv\_param qbv\_param;

511 struct ethernet\_qbu\_param qbu\_param;

512 struct ethernet\_txtime\_param txtime\_param;

513

514 int priority\_queues\_num;

515 int ports\_num;

516

517 enum [ethernet\_checksum\_support](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede) chksum\_support;

518

519 struct ethernet\_filter filter;

520 };

521};

522

524

[ 526](structethernet__api.md)struct [ethernet\_api](structethernet__api.md) {

[ 531](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056) struct net\_if\_api [iface\_api](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056);

532

537#if defined(CONFIG\_NET\_STATISTICS\_ETHERNET)

538 struct [net\_stats\_eth](structnet__stats__eth.md) \*(\*get\_stats)(const struct [device](structdevice.md) \*dev);

539#endif

540

[ 542](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1) int (\*[start](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1))(const struct [device](structdevice.md) \*dev);

543

[ 545](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3) int (\*[stop](structethernet__api.md#a819599fe26b90860147ccfa86f337f84))(const struct [device](structdevice.md) \*dev);

546

548 enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) (\*[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3))(const struct [device](structdevice.md) \*dev);

549

[ 551](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1) int (\*[set\_config](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1))(const struct [device](structdevice.md) \*dev,

552 enum ethernet\_config\_type type,

553 const struct ethernet\_config \*config);

554

[ 556](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81) int (\*[get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81))(const struct [device](structdevice.md) \*dev,

557 enum ethernet\_config\_type type,

558 struct ethernet\_config \*config);

559

565#if defined(CONFIG\_NET\_VLAN)

566 int (\*vlan\_setup)(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface,

567 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag, bool enable);

568#endif /\* CONFIG\_NET\_VLAN \*/

569

571#if defined(CONFIG\_PTP\_CLOCK)

572 const struct [device](structdevice.md) \*(\*get\_ptp\_clock)(const struct [device](structdevice.md) \*dev);

573#endif /\* CONFIG\_PTP\_CLOCK \*/

574

[ 576](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241) int (\*[send](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

577};

578

580

581/\* Make sure that the network interface API is properly setup inside

582 \* Ethernet API struct (it is the first one).

583 \*/

584BUILD\_ASSERT(offsetof(struct [ethernet\_api](structethernet__api.md), iface\_api) == 0);

585

586struct net\_eth\_hdr {

587 struct [net\_eth\_addr](structnet__eth__addr.md) dst;

588 struct [net\_eth\_addr](structnet__eth__addr.md) src;

589 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type;

590} \_\_packed;

591

592struct ethernet\_vlan {

594 struct net\_if \*iface;

595

597 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag;

598};

599

600#if defined(CONFIG\_NET\_VLAN\_COUNT)

601#define NET\_VLAN\_MAX\_COUNT CONFIG\_NET\_VLAN\_COUNT

602#else

603/\* Even thou there are no VLAN support, the minimum count must be set to 1.

604 \*/

605#define NET\_VLAN\_MAX\_COUNT 1

606#endif

607

609

[ 611](structethernet__lldp.md)struct [ethernet\_lldp](structethernet__lldp.md) {

[ 613](structethernet__lldp.md#a8cf37774b067ffbc4876e42c3b28e536) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structethernet__lldp.md#a8cf37774b067ffbc4876e42c3b28e536);

614

[ 616](structethernet__lldp.md#aede4281b7f53be43f524d47bb2c606d1) const struct [net\_lldpdu](structnet__lldpdu.md) \*[lldpdu](structethernet__lldp.md#aede4281b7f53be43f524d47bb2c606d1);

617

[ 619](structethernet__lldp.md#a732d685dd27d2be5cb6b51175b8af70f) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[optional\_du](structethernet__lldp.md#a732d685dd27d2be5cb6b51175b8af70f);

620

[ 622](structethernet__lldp.md#aabc1141bbc72a17e3884138c61bd5b0c) size\_t [optional\_len](structethernet__lldp.md#aabc1141bbc72a17e3884138c61bd5b0c);

623

[ 625](structethernet__lldp.md#ae15dfbab311c17a9075c94b6915b5fd6) struct [net\_if](structnet__if.md) \*[iface](structethernet__lldp.md#ae15dfbab311c17a9075c94b6915b5fd6);

626

[ 628](structethernet__lldp.md#af4c5d4a5ad00e08dc311e5ab6fa44a97) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [tx\_timer\_start](structethernet__lldp.md#af4c5d4a5ad00e08dc311e5ab6fa44a97);

629

[ 631](structethernet__lldp.md#af179e53f86d44af34608a2a40a5e0294) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_timer\_timeout](structethernet__lldp.md#af179e53f86d44af34608a2a40a5e0294);

632

[ 634](structethernet__lldp.md#a8d2452f182c52000bec93f4c53501220) [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) [cb](structethernet__lldp.md#a8d2452f182c52000bec93f4c53501220);

635};

636

638

639enum ethernet\_flags {

640 ETH\_CARRIER\_UP,

641};

642

644struct ethernet\_context {

648 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

649

650#if defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

651 struct eth\_bridge\_iface\_context bridge;

652#endif

653

660 struct k\_work carrier\_work;

661

663 struct net\_if \*iface;

664

665#if defined(CONFIG\_NET\_LLDP)

666 struct ethernet\_lldp lldp[NET\_VLAN\_MAX\_COUNT];

667#endif

668

672 enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) ethernet\_l2\_flags;

673

674#if defined(CONFIG\_NET\_L2\_PTP)

679 int port;

680#endif

681

682#if defined(CONFIG\_NET\_DSA)

686 [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa) dsa\_recv\_cb;

687

689 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_port\_idx;

690

692 struct dsa\_context \*dsa\_ctx;

693

695 [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b) dsa\_send;

696#endif

697

699 bool is\_net\_carrier\_up : 1;

700

702 bool is\_init : 1;

703

705 enum [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) eth\_if\_type;

706};

707

713void ethernet\_init(struct [net\_if](structnet__if.md) \*iface);

714

715#define ETHERNET\_L2\_CTX\_TYPE struct ethernet\_context

716

717/\* Separate header for VLAN as some of device interfaces might not

718 \* support VLAN.

719 \*/

720struct net\_eth\_vlan\_hdr {

721 struct net\_eth\_addr dst;

722 struct net\_eth\_addr src;

723 struct {

724 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tpid; /\* tag protocol id \*/

725 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci; /\* tag control info \*/

726 } vlan;

727 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type;

728} \_\_packed;

729

731

[ 739](group__ethernet.md#ga76a5fe39ce12478c666d87f4aec3d579)static inline bool [net\_eth\_is\_addr\_broadcast](group__ethernet.md#ga76a5fe39ce12478c666d87f4aec3d579)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

740{

741 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0xff &&

742 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0xff &&

743 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0xff &&

744 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[3] == 0xff &&

745 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[4] == 0xff &&

746 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[5] == 0xff) {

747 return true;

748 }

749

750 return false;

751}

752

[ 760](group__ethernet.md#ga237aab2d07ffa84355981d02a4576ebe)static inline bool [net\_eth\_is\_addr\_all\_zeroes](group__ethernet.md#ga237aab2d07ffa84355981d02a4576ebe)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

761{

762 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x00 &&

763 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x00 &&

764 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0x00 &&

765 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[3] == 0x00 &&

766 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[4] == 0x00 &&

767 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[5] == 0x00) {

768 return true;

769 }

770

771 return false;

772}

773

[ 781](group__ethernet.md#ga89964de263029223d119f361fbd94bfd)static inline bool [net\_eth\_is\_addr\_unspecified](group__ethernet.md#ga89964de263029223d119f361fbd94bfd)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

782{

783 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x00 &&

784 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x00 &&

785 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0x00 &&

786 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[3] == 0x00 &&

787 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[4] == 0x00 &&

788 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[5] == 0x00) {

789 return true;

790 }

791

792 return false;

793}

794

[ 802](group__ethernet.md#ga2755ecb84e9759c24302e33a56a1fc84)static inline bool [net\_eth\_is\_addr\_multicast](group__ethernet.md#ga2755ecb84e9759c24302e33a56a1fc84)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

803{

804#if defined(CONFIG\_NET\_IPV6)

805 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x33 &&

806 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x33) {

807 return true;

808 }

809#endif

810

811#if defined(CONFIG\_NET\_IPV4)

812 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x01 &&

813 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x00 &&

814 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0x5e) {

815 return true;

816 }

817#endif

818

819 return false;

820}

821

[ 829](group__ethernet.md#ga82ad9574acb697c26a9aa11316867d3c)static inline bool [net\_eth\_is\_addr\_group](group__ethernet.md#ga82ad9574acb697c26a9aa11316867d3c)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

830{

831 return addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] & 0x01;

832}

833

[ 841](group__ethernet.md#gaf20472f9d60e5cddffed2919b3091030)static inline bool [net\_eth\_is\_addr\_valid](group__ethernet.md#gaf20472f9d60e5cddffed2919b3091030)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

842{

843 return ![net\_eth\_is\_addr\_unspecified](group__ethernet.md#ga89964de263029223d119f361fbd94bfd)(addr) && ![net\_eth\_is\_addr\_group](group__ethernet.md#ga82ad9574acb697c26a9aa11316867d3c)(addr);

844}

845

[ 853](group__ethernet.md#gaec6fb3c05792bdd30596137686f3251a)static inline bool [net\_eth\_is\_addr\_lldp\_multicast](group__ethernet.md#gaec6fb3c05792bdd30596137686f3251a)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

854{

855#if defined(CONFIG\_NET\_GPTP) || defined(CONFIG\_NET\_LLDP)

856 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x01 &&

857 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x80 &&

858 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0xc2 &&

859 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[3] == 0x00 &&

860 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[4] == 0x00 &&

861 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[5] == 0x0e) {

862 return true;

863 }

864#else

865 ARG\_UNUSED(addr);

866#endif

867

868 return false;

869}

870

[ 878](group__ethernet.md#gaeddfa5b3ff6e356393114b351f87fe43)static inline bool [net\_eth\_is\_addr\_ptp\_multicast](group__ethernet.md#gaeddfa5b3ff6e356393114b351f87fe43)(struct [net\_eth\_addr](structnet__eth__addr.md) \*addr)

879{

880#if defined(CONFIG\_NET\_GPTP)

881 if (addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[0] == 0x01 &&

882 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[1] == 0x1b &&

883 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[2] == 0x19 &&

884 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[3] == 0x00 &&

885 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[4] == 0x00 &&

886 addr->[addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)[5] == 0x00) {

887 return true;

888 }

889#else

890 ARG\_UNUSED(addr);

891#endif

892

893 return false;

894}

895

[ 901](group__ethernet.md#gae66b24a847f8e0ad119c6c466331afd6)const struct [net\_eth\_addr](structnet__eth__addr.md) \*[net\_eth\_broadcast\_addr](group__ethernet.md#gae66b24a847f8e0ad119c6c466331afd6)(void);

902

[ 909](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)void [net\_eth\_ipv4\_mcast\_to\_mac\_addr](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)(const struct [in\_addr](structin__addr.md) \*ipv4\_addr,

910 struct [net\_eth\_addr](structnet__eth__addr.md) \*mac\_addr);

911

[ 918](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)void [net\_eth\_ipv6\_mcast\_to\_mac\_addr](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)(const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr,

919 struct [net\_eth\_addr](structnet__eth__addr.md) \*mac\_addr);

920

928static inline

[ 929](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) [net\_eth\_get\_hw\_capabilities](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)(struct [net\_if](structnet__if.md) \*iface)

930{

931 const struct [ethernet\_api](structethernet__api.md) \*eth =

932 (struct [ethernet\_api](structethernet__api.md) \*)[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

933

934 if (!eth->[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)) {

935 return (enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5))0;

936 }

937

938 return eth->[get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)([net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface));

939}

940

950static inline

[ 951](group__ethernet.md#ga1246be489eb7130100bbaebbb73961c5)int [net\_eth\_get\_hw\_config](group__ethernet.md#ga1246be489eb7130100bbaebbb73961c5)(struct [net\_if](structnet__if.md) \*iface, enum ethernet\_config\_type type,

952 struct ethernet\_config \*config)

953{

954 const struct [ethernet\_api](structethernet__api.md) \*eth =

955 (struct [ethernet\_api](structethernet__api.md) \*)[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

956

957 if (!eth->[get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81)) {

958 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

959 }

960

961 return eth->[get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81)([net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface), type, config);

962}

963

964

973#if defined(CONFIG\_NET\_VLAN)

974int [net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

975#else

[ 976](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)static inline int [net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

977{

978 ARG\_UNUSED(iface);

979 ARG\_UNUSED(tag);

980

981 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

982}

983#endif

984

993#if defined(CONFIG\_NET\_VLAN)

994int [net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

995#else

[ 996](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)static inline int [net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

997{

998 ARG\_UNUSED(iface);

999 ARG\_UNUSED(tag);

1000

1001 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1002}

1003#endif

1004

1016#if defined(CONFIG\_NET\_VLAN)

1017[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)(struct [net\_if](structnet__if.md) \*iface);

1018#else

[ 1019](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)(struct [net\_if](structnet__if.md) \*iface)

1020{

1021 ARG\_UNUSED(iface);

1022

1023 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

1024}

1025#endif

1026

1036#if defined(CONFIG\_NET\_VLAN)

1037struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

1038#else

1039static inline

[ 1040](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1041{

1042 ARG\_UNUSED(iface);

1043 ARG\_UNUSED(tag);

1044

1045 return NULL;

1046}

1047#endif

1048

1058#if defined(CONFIG\_NET\_VLAN)

1059struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_main](group__ethernet.md#ga010a95a0239a800131ac3d43dd54737f)(struct [net\_if](structnet__if.md) \*iface);

1060#else

1061static inline

[ 1062](group__ethernet.md#ga010a95a0239a800131ac3d43dd54737f)struct [net\_if](structnet__if.md) \*[net\_eth\_get\_vlan\_main](group__ethernet.md#ga010a95a0239a800131ac3d43dd54737f)(struct [net\_if](structnet__if.md) \*iface)

1063{

1064 ARG\_UNUSED(iface);

1065

1066 return NULL;

1067}

1068#endif

1069

1083#if defined(CONFIG\_NET\_VLAN)

1084bool [net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)(struct ethernet\_context \*ctx,

1085 struct [net\_if](structnet__if.md) \*iface);

1086#else

[ 1087](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)static inline bool [net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)(struct ethernet\_context \*ctx,

1088 struct [net\_if](structnet__if.md) \*iface)

1089{

1090 ARG\_UNUSED(ctx);

1091 ARG\_UNUSED(iface);

1092

1093 return false;

1094}

1095#endif

1096

1104#if defined(CONFIG\_NET\_VLAN)

1105bool [net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)(struct [net\_if](structnet__if.md) \*iface);

1106#else

[ 1107](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)static inline bool [net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)(struct [net\_if](structnet__if.md) \*iface)

1108{

1109 ARG\_UNUSED(iface);

1110

1111 return false;

1112}

1113#endif

1114

1122#if defined(CONFIG\_NET\_VLAN)

1123bool [net\_eth\_is\_vlan\_interface](group__ethernet.md#ga8ca1eccc88a351241298d358ec28fdf5)(struct [net\_if](structnet__if.md) \*iface);

1124#else

[ 1125](group__ethernet.md#ga8ca1eccc88a351241298d358ec28fdf5)static inline bool [net\_eth\_is\_vlan\_interface](group__ethernet.md#ga8ca1eccc88a351241298d358ec28fdf5)(struct [net\_if](structnet__if.md) \*iface)

1126{

1127 ARG\_UNUSED(iface);

1128

1129 return false;

1130}

1131#endif

1132

1134

1135#if !defined(CONFIG\_ETH\_DRIVER\_RAW\_MODE)

1136

1137#define Z\_ETH\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

1138 init\_fn, pm, data, config, prio, \

1139 api, mtu) \

1140 Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

1141 init\_fn, pm, data, config, prio, \

1142 api, ETHERNET\_L2, \

1143 NET\_L2\_GET\_CTX\_TYPE(ETHERNET\_L2), mtu)

1144

1145#else /\* CONFIG\_ETH\_DRIVER\_RAW\_MODE \*/

1146

1147#define Z\_ETH\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, instance, \

1148 init\_fn, pm, data, config, prio, \

1149 api, mtu) \

1150 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

1151 Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, \

1152 config, POST\_KERNEL, prio, api, \

1153 &Z\_DEVICE\_STATE\_NAME(dev\_id));

1154

1155#endif /\* CONFIG\_ETH\_DRIVER\_RAW\_MODE \*/

1156

1157#define Z\_ETH\_NET\_DEVICE\_INIT(node\_id, dev\_id, name, init\_fn, pm, data, \

1158 config, prio, api, mtu) \

1159 Z\_ETH\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, dev\_id, name, 0, \

1160 init\_fn, pm, data, config, prio, \

1161 api, mtu)

1162

1164

[ 1182](group__ethernet.md#ga197e02748be8eaf410f7deb57c984642)#define ETH\_NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, \

1183 prio, api, mtu) \

1184 Z\_ETH\_NET\_DEVICE\_INIT(DT\_INVALID\_NODE, dev\_id, name, init\_fn, \

1185 pm, data, config, prio, api, mtu)

1186

[ 1209](group__ethernet.md#ga3dc27a54b7ae178e8c4daeba4c84aab0)#define ETH\_NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, \

1210 pm, data, config, prio, api, mtu) \

1211 Z\_ETH\_NET\_DEVICE\_INIT\_INSTANCE(DT\_INVALID\_NODE, dev\_id, name, \

1212 instance, init\_fn, pm, data, \

1213 config, prio, api, mtu)

1214

[ 1231](group__ethernet.md#ga9f67fee695953f24b1e5d9e49041aa99)#define ETH\_NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, \

1232 prio, api, mtu) \

1233 Z\_ETH\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

1234 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, \

1235 data, config, prio, api, mtu)

1236

[ 1246](group__ethernet.md#gaecf9f102108836ed9cf7e2cdb3c90579)#define ETH\_NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

1247 ETH\_NET\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

1248

[ 1255](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)void [net\_eth\_carrier\_on](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)(struct [net\_if](structnet__if.md) \*iface);

1256

[ 1263](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)void [net\_eth\_carrier\_off](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)(struct [net\_if](structnet__if.md) \*iface);

1264

[ 1274](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)int [net\_eth\_promisc\_mode](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)(struct [net\_if](structnet__if.md) \*iface, bool enable);

1275

[ 1285](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)int [net\_eth\_txinjection\_mode](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)(struct [net\_if](structnet__if.md) \*iface, bool enable);

1286

[ 1297](group__ethernet.md#ga920bddac077675d544a21fb5650c945e)int [net\_eth\_mac\_filter](group__ethernet.md#ga920bddac077675d544a21fb5650c945e)(struct [net\_if](structnet__if.md) \*iface, struct [net\_eth\_addr](structnet__eth__addr.md) \*mac,

1298 enum ethernet\_filter\_type type, bool enable);

1307#if defined(CONFIG\_PTP\_CLOCK)

1308const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)(struct [net\_if](structnet__if.md) \*iface);

1309#else

[ 1310](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)static inline const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)(struct [net\_if](structnet__if.md) \*iface)

1311{

1312 ARG\_UNUSED(iface);

1313

1314 return NULL;

1315}

1316#endif

1317

[ 1327](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)\_\_syscall const struct [device](structdevice.md) \*[net\_eth\_get\_ptp\_clock\_by\_index](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)(int index);

1328

1336#if defined(CONFIG\_NET\_L2\_PTP)

1337int [net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)(struct [net\_if](structnet__if.md) \*iface);

1338#else

[ 1339](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)static inline int [net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)(struct [net\_if](structnet__if.md) \*iface)

1340{

1341 ARG\_UNUSED(iface);

1342

1343 return -[ENODEV](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1);

1344}

1345#endif /\* CONFIG\_NET\_L2\_PTP \*/

1346

1353#if defined(CONFIG\_NET\_L2\_PTP)

1354void [net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)(struct [net\_if](structnet__if.md) \*iface, int port);

1355#else

[ 1356](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)static inline void [net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)(struct [net\_if](structnet__if.md) \*iface, int port)

1357{

1358 ARG\_UNUSED(iface);

1359 ARG\_UNUSED(port);

1360}

1361#endif /\* CONFIG\_NET\_L2\_PTP \*/

1362

[ 1370](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)static inline bool [net\_eth\_type\_is\_wifi](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)(struct [net\_if](structnet__if.md) \*iface)

1371{

1372 const struct ethernet\_context \*ctx = (struct ethernet\_context \*)

1373 [net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)(iface);

1374

1375 return ctx->eth\_if\_type == [L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671);

1376}

1377

1381

1382#ifdef \_\_cplusplus

1383}

1384#endif

1385

1386#include <zephyr/syscalls/ethernet.h>

1387

1388#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_H\_ \*/

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

**Definition** dsa.h:72

[dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)

int(\* dsa\_send\_t)(const struct device \*dev, struct net\_pkt \*pkt)

Pointer to master interface send function.

**Definition** dsa.h:98

[net\_eth\_get\_vlan\_main](group__ethernet.md#ga010a95a0239a800131ac3d43dd54737f)

static struct net\_if \* net\_eth\_get\_vlan\_main(struct net\_if \*iface)

Return main network interface that is attached to this VLAN tag.

**Definition** ethernet.h:1062

[net\_eth\_get\_hw\_config](group__ethernet.md#ga1246be489eb7130100bbaebbb73961c5)

static int net\_eth\_get\_hw\_config(struct net\_if \*iface, enum ethernet\_config\_type type, struct ethernet\_config \*config)

Return ethernet device hardware configuration information.

**Definition** ethernet.h:951

[ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc)

ethernet\_if\_types

Types of Ethernet L2.

**Definition** ethernet.h:437

[net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231)

static void net\_eth\_set\_ptp\_port(struct net\_if \*iface, int port)

Set PTP port number attached to this interface.

**Definition** ethernet.h:1356

[net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)

static int net\_eth\_vlan\_enable(struct net\_if \*iface, uint16\_t tag)

Add VLAN tag to the interface.

**Definition** ethernet.h:976

[net\_eth\_is\_addr\_all\_zeroes](group__ethernet.md#ga237aab2d07ffa84355981d02a4576ebe)

static bool net\_eth\_is\_addr\_all\_zeroes(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a all zeroes address.

**Definition** ethernet.h:760

[net\_eth\_is\_addr\_multicast](group__ethernet.md#ga2755ecb84e9759c24302e33a56a1fc84)

static bool net\_eth\_is\_addr\_multicast(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a multicast address.

**Definition** ethernet.h:802

[net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a)

static int net\_eth\_get\_ptp\_port(struct net\_if \*iface)

Return PTP port number attached to this interface.

**Definition** ethernet.h:1339

[net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3)

static const struct device \* net\_eth\_get\_ptp\_clock(struct net\_if \*iface)

Return PTP clock that is tied to this ethernet network interface.

**Definition** ethernet.h:1310

[NET\_ETH\_ADDR\_LEN](group__ethernet.md#ga399425f810c00bcf9babec019bc2ff12)

#define NET\_ETH\_ADDR\_LEN

Ethernet MAC address length.

**Definition** ethernet.h:48

[net\_eth\_promisc\_mode](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9)

int net\_eth\_promisc\_mode(struct net\_if \*iface, bool enable)

Set promiscuous mode either ON or OFF.

[net\_eth\_carrier\_off](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75)

void net\_eth\_carrier\_off(struct net\_if \*iface)

Inform ethernet L2 driver that ethernet carrier was lost.

[net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9)

static uint16\_t net\_eth\_get\_vlan\_tag(struct net\_if \*iface)

Return VLAN tag specified to network interface.

**Definition** ethernet.h:1019

[net\_eth\_type\_is\_wifi](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d)

static bool net\_eth\_type\_is\_wifi(struct net\_if \*iface)

Check if the Ethernet L2 network interface can perform Wi-Fi.

**Definition** ethernet.h:1370

[net\_eth\_is\_addr\_broadcast](group__ethernet.md#ga76a5fe39ce12478c666d87f4aec3d579)

static bool net\_eth\_is\_addr\_broadcast(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a broadcast address.

**Definition** ethernet.h:739

[net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c)

static bool net\_eth\_get\_vlan\_status(struct net\_if \*iface)

Get VLAN status for a given network interface (enabled or not).

**Definition** ethernet.h:1107

[net\_eth\_is\_addr\_group](group__ethernet.md#ga82ad9574acb697c26a9aa11316867d3c)

static bool net\_eth\_is\_addr\_group(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a group address.

**Definition** ethernet.h:829

[net\_eth\_get\_ptp\_clock\_by\_index](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6)

const struct device \* net\_eth\_get\_ptp\_clock\_by\_index(int index)

Return PTP clock that is tied to this ethernet network interface index.

[net\_eth\_is\_addr\_unspecified](group__ethernet.md#ga89964de263029223d119f361fbd94bfd)

static bool net\_eth\_is\_addr\_unspecified(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is unspecified.

**Definition** ethernet.h:781

[net\_eth\_is\_vlan\_interface](group__ethernet.md#ga8ca1eccc88a351241298d358ec28fdf5)

static bool net\_eth\_is\_vlan\_interface(struct net\_if \*iface)

Check if the given interface is a VLAN interface.

**Definition** ethernet.h:1125

[ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)

ethernet\_hw\_caps

Ethernet hardware capabilities.

**Definition** ethernet.h:142

[net\_eth\_mac\_filter](group__ethernet.md#ga920bddac077675d544a21fb5650c945e)

int net\_eth\_mac\_filter(struct net\_if \*iface, struct net\_eth\_addr \*mac, enum ethernet\_filter\_type type, bool enable)

Set or unset HW filtering for MAC address mac.

[net\_eth\_ipv6\_mcast\_to\_mac\_addr](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f)

void net\_eth\_ipv6\_mcast\_to\_mac\_addr(const struct in6\_addr \*ipv6\_addr, struct net\_eth\_addr \*mac\_addr)

Convert IPv6 multicast address to Ethernet address.

[net\_eth\_get\_hw\_capabilities](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd)

static enum ethernet\_hw\_caps net\_eth\_get\_hw\_capabilities(struct net\_if \*iface)

Return ethernet device hardware capability information.

**Definition** ethernet.h:929

[net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50)

static int net\_eth\_vlan\_disable(struct net\_if \*iface, uint16\_t tag)

Remove VLAN tag from the interface.

**Definition** ethernet.h:996

[net\_eth\_carrier\_on](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0)

void net\_eth\_carrier\_on(struct net\_if \*iface)

Inform ethernet L2 driver that ethernet carrier is detected.

[ethernet\_checksum\_support](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede)

ethernet\_checksum\_support

Protocols that are supported by checksum offloading.

**Definition** ethernet.h:474

[net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c)

static bool net\_eth\_is\_vlan\_enabled(struct ethernet\_context \*ctx, struct net\_if \*iface)

Check if there are any VLAN interfaces enabled to this specific Ethernet network interface.

**Definition** ethernet.h:1087

[net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e)

static struct net\_if \* net\_eth\_get\_vlan\_iface(struct net\_if \*iface, uint16\_t tag)

Return network interface related to this VLAN tag.

**Definition** ethernet.h:1040

[net\_eth\_ipv4\_mcast\_to\_mac\_addr](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e)

void net\_eth\_ipv4\_mcast\_to\_mac\_addr(const struct in\_addr \*ipv4\_addr, struct net\_eth\_addr \*mac\_addr)

Convert IPv4 multicast address to Ethernet address.

[net\_eth\_broadcast\_addr](group__ethernet.md#gae66b24a847f8e0ad119c6c466331afd6)

const struct net\_eth\_addr \* net\_eth\_broadcast\_addr(void)

Return Ethernet broadcast address.

[net\_eth\_is\_addr\_lldp\_multicast](group__ethernet.md#gaec6fb3c05792bdd30596137686f3251a)

static bool net\_eth\_is\_addr\_lldp\_multicast(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a LLDP multicast address.

**Definition** ethernet.h:853

[net\_eth\_is\_addr\_ptp\_multicast](group__ethernet.md#gaeddfa5b3ff6e356393114b351f87fe43)

static bool net\_eth\_is\_addr\_ptp\_multicast(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is a PTP multicast address.

**Definition** ethernet.h:878

[net\_eth\_is\_addr\_valid](group__ethernet.md#gaf20472f9d60e5cddffed2919b3091030)

static bool net\_eth\_is\_addr\_valid(struct net\_eth\_addr \*addr)

Check if the Ethernet MAC address is valid.

**Definition** ethernet.h:841

[net\_eth\_txinjection\_mode](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984)

int net\_eth\_txinjection\_mode(struct net\_if \*iface, bool enable)

Set TX-Injection mode either ON or OFF.

[L2\_ETH\_IF\_TYPE\_ETHERNET](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)

@ L2\_ETH\_IF\_TYPE\_ETHERNET

IEEE 802.3 Ethernet (default).

**Definition** ethernet.h:439

[L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)

@ L2\_ETH\_IF\_TYPE\_WIFI

IEEE 802.11 Wi-Fi.

**Definition** ethernet.h:442

[ETHERNET\_HW\_VLAN](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)

@ ETHERNET\_HW\_VLAN

VLAN supported.

**Definition** ethernet.h:150

[ETHERNET\_PRIORITY\_QUEUES](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)

@ ETHERNET\_PRIORITY\_QUEUES

Priority queues available.

**Definition** ethernet.h:177

[ETHERNET\_DUPLEX\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc)

@ ETHERNET\_DUPLEX\_SET

Changing duplex (half/full) supported.

**Definition** ethernet.h:165

[ETHERNET\_HW\_VLAN\_TAG\_STRIP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)

@ ETHERNET\_HW\_VLAN\_TAG\_STRIP

VLAN Tag stripping.

**Definition** ethernet.h:186

[ETHERNET\_LINK\_10BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6)

@ ETHERNET\_LINK\_10BASE\_T

10 Mbits link supported

**Definition** ethernet.h:156

[ETHERNET\_HW\_FILTERING](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)

@ ETHERNET\_HW\_FILTERING

MAC address filtering supported.

**Definition** ethernet.h:180

[ETHERNET\_PTP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a)

@ ETHERNET\_PTP

IEEE 802.1AS (gPTP) clock supported.

**Definition** ethernet.h:168

[ETHERNET\_QBU](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)

@ ETHERNET\_QBU

IEEE 802.1Qbu (frame preemption) supported.

**Definition** ethernet.h:198

[ETHERNET\_LINK\_100BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e)

@ ETHERNET\_LINK\_100BASE\_T

100 Mbits link supported

**Definition** ethernet.h:159

[ETHERNET\_DSA\_MASTER\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883)

@ ETHERNET\_DSA\_MASTER\_PORT

DSA switch master port.

**Definition** ethernet.h:192

[ETHERNET\_DSA\_SLAVE\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7)

@ ETHERNET\_DSA\_SLAVE\_PORT

DSA switch slave port.

**Definition** ethernet.h:189

[ETHERNET\_TXINJECTION\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)

@ ETHERNET\_TXINJECTION\_MODE

TX-Injection supported.

**Definition** ethernet.h:204

[ETHERNET\_QAV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)

@ ETHERNET\_QAV

IEEE 802.1Qav (credit-based shaping) supported.

**Definition** ethernet.h:171

[ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)

@ ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD

RX Checksum offloading supported for all of IPv4, UDP, TCP.

**Definition** ethernet.h:147

[ETHERNET\_LINK\_1000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8)

@ ETHERNET\_LINK\_1000BASE\_T

1 Gbits link supported

**Definition** ethernet.h:162

[ETHERNET\_LLDP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)

@ ETHERNET\_LLDP

Link Layer Discovery Protocol supported.

**Definition** ethernet.h:183

[ETHERNET\_AUTO\_NEGOTIATION\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a)

@ ETHERNET\_AUTO\_NEGOTIATION\_SET

Enabling/disabling auto negotiation supported.

**Definition** ethernet.h:153

[ETHERNET\_TXTIME](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)

@ ETHERNET\_TXTIME

TXTIME supported.

**Definition** ethernet.h:201

[ETHERNET\_QBV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)

@ ETHERNET\_QBV

IEEE 802.1Qbv (scheduled traffic) supported.

**Definition** ethernet.h:195

[ETHERNET\_PROMISC\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)

@ ETHERNET\_PROMISC\_MODE

Promiscuous mode supported.

**Definition** ethernet.h:174

[ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)

@ ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD

TX Checksum offloading supported for all of IPv4, UDP, TCP.

**Definition** ethernet.h:144

[ETHERNET\_CHECKSUM\_SUPPORT\_UDP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8)

@ ETHERNET\_CHECKSUM\_SUPPORT\_UDP

Device supports UDP checksum offloading for all supported IP protocols.

**Definition** ethernet.h:488

[ETHERNET\_CHECKSUM\_SUPPORT\_TCP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02)

@ ETHERNET\_CHECKSUM\_SUPPORT\_TCP

Device supports TCP checksum offloading for all supported IP protocols.

**Definition** ethernet.h:486

[ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5)

@ ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_HEADER

Device supports checksum offloading for the IPv6 header.

**Definition** ethernet.h:482

[ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9)

@ ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_ICMP

Device supports checksum offloading for ICMPv4 payload (implies IPv4 header).

**Definition** ethernet.h:480

[ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4)

@ ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_HEADER

Device supports checksum offloading for the IPv4 header.

**Definition** ethernet.h:478

[ETHERNET\_CHECKSUM\_SUPPORT\_NONE](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d)

@ ETHERNET\_CHECKSUM\_SUPPORT\_NONE

Device does not support any L3/L4 checksum offloading.

**Definition** ethernet.h:476

[ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be)

@ ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_ICMP

Device supports checksum offloading for ICMPv6 payload (implies IPv6 header).

**Definition** ethernet.h:484

[net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf)

enum net\_verdict(\* net\_lldp\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

LLDP Receive packet callback.

**Definition** lldp.h:213

[net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0)

static void \* net\_if\_l2\_data(struct net\_if \*iface)

Get a pointer to the interface L2 private data.

**Definition** net\_if.h:926

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:941

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

**Definition** errno.h:60

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[ENODEV](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1)

#define ENODEV

No such device.

**Definition** errno.h:57

[NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)

#define NET\_VLAN\_TAG\_UNSPEC

Unspecified VLAN tag value.

**Definition** ethernet\_vlan.h:30

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[lldp.h](lldp_8h.md)

LLDP definitions and handler.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

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

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:526

[ethernet\_api::iface\_api](structethernet__api.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** ethernet.h:531

[ethernet\_api::start](structethernet__api.md#a2abe87be47f265a6d5b3e7b598682da1)

int(\* start)(const struct device \*dev)

Collect optional ethernet specific statistics.

**Definition** ethernet.h:542

[ethernet\_api::get\_config](structethernet__api.md#a3f71e6bf922b91289efa3ac97df70e81)

int(\* get\_config)(const struct device \*dev, enum ethernet\_config\_type type, struct ethernet\_config \*config)

Get hardware specific configuration.

**Definition** ethernet.h:556

[ethernet\_api::stop](structethernet__api.md#a819599fe26b90860147ccfa86f337f84)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** ethernet.h:545

[ethernet\_api::get\_capabilities](structethernet__api.md#a8731846f9bd07398b2f5c154c6ec0fe3)

enum ethernet\_hw\_caps(\* get\_capabilities)(const struct device \*dev)

Get the device capabilities.

**Definition** ethernet.h:548

[ethernet\_api::send](structethernet__api.md#a8f6fd0d640b5a883c9f5150d9ed71241)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

The IP stack will call this function when a VLAN tag is enabled or disabled.

**Definition** ethernet.h:576

[ethernet\_api::set\_config](structethernet__api.md#ae204fdf7e8c72fdea3dee67a7068afe1)

int(\* set\_config)(const struct device \*dev, enum ethernet\_config\_type type, const struct ethernet\_config \*config)

Set specific hardware configuration.

**Definition** ethernet.h:551

[ethernet\_filter](structethernet__filter.md)

Ethernet filter description.

**Definition** ethernet.h:446

[ethernet\_filter::mac\_address](structethernet__filter.md#aaacda9b89d6b21934654e0f2b19624e0)

struct net\_eth\_addr mac\_address

MAC address to filter.

**Definition** ethernet.h:450

[ethernet\_filter::set](structethernet__filter.md#ad83053c859c65e0c0432fe3f59671335)

bool set

Set (true) or unset (false) the filter.

**Definition** ethernet.h:452

[ethernet\_filter::type](structethernet__filter.md#aec00b1ecd6af658a5164d375bccdaa10)

enum ethernet\_filter\_type type

Type of filter.

**Definition** ethernet.h:448

[ethernet\_lldp](structethernet__lldp.md)

Ethernet LLDP specific parameters.

**Definition** ethernet.h:611

[ethernet\_lldp::optional\_du](structethernet__lldp.md#a732d685dd27d2be5cb6b51175b8af70f)

const uint8\_t \* optional\_du

LLDP Data Unit optional TLVs for the interface.

**Definition** ethernet.h:619

[ethernet\_lldp::node](structethernet__lldp.md#a8cf37774b067ffbc4876e42c3b28e536)

sys\_snode\_t node

Used for track timers.

**Definition** ethernet.h:613

[ethernet\_lldp::cb](structethernet__lldp.md#a8d2452f182c52000bec93f4c53501220)

net\_lldp\_recv\_cb\_t cb

LLDP RX callback function.

**Definition** ethernet.h:634

[ethernet\_lldp::optional\_len](structethernet__lldp.md#aabc1141bbc72a17e3884138c61bd5b0c)

size\_t optional\_len

Length of the optional Data Unit TLVs.

**Definition** ethernet.h:622

[ethernet\_lldp::iface](structethernet__lldp.md#ae15dfbab311c17a9075c94b6915b5fd6)

struct net\_if \* iface

Network interface that has LLDP supported.

**Definition** ethernet.h:625

[ethernet\_lldp::lldpdu](structethernet__lldp.md#aede4281b7f53be43f524d47bb2c606d1)

const struct net\_lldpdu \* lldpdu

LLDP Data Unit mandatory TLVs for the interface.

**Definition** ethernet.h:616

[ethernet\_lldp::tx\_timer\_timeout](structethernet__lldp.md#af179e53f86d44af34608a2a40a5e0294)

uint32\_t tx\_timer\_timeout

LLDP TX timeout.

**Definition** ethernet.h:631

[ethernet\_lldp::tx\_timer\_start](structethernet__lldp.md#af4c5d4a5ad00e08dc311e5ab6fa44a97)

int64\_t tx\_timer\_start

LLDP TX timer start time.

**Definition** ethernet.h:628

[ethernet\_qav\_param](structethernet__qav__param.md)

Ethernet Qav specific parameters.

**Definition** ethernet.h:288

[ethernet\_qav\_param::enabled](structethernet__qav__param.md#a031d3896b14eb8b32c3c050738421b85)

bool enabled

True if Qav is enabled for queue.

**Definition** ethernet.h:295

[ethernet\_qav\_param::oper\_idle\_slope](structethernet__qav__param.md#a0691f10a338d3c49a58d94a1adced477)

unsigned int oper\_idle\_slope

Oper Idle Slope (bits per second).

**Definition** ethernet.h:301

[ethernet\_qav\_param::type](structethernet__qav__param.md#a38861d9f790a61aa88801cb1373077a8)

enum ethernet\_qav\_param\_type type

Type of Qav parameter.

**Definition** ethernet.h:292

[ethernet\_qav\_param::traffic\_class](structethernet__qav__param.md#a4a795e4a0c7d5bcbe8212d79f772dc6f)

unsigned int traffic\_class

Traffic class the queue is bound to.

**Definition** ethernet.h:303

[ethernet\_qav\_param::queue\_id](structethernet__qav__param.md#a4e2d2967669b758422c166140af0c1ba)

int queue\_id

ID of the priority queue to use.

**Definition** ethernet.h:290

[ethernet\_qav\_param::idle\_slope](structethernet__qav__param.md#a6d43b199549cade0a07dc10adac85bff)

unsigned int idle\_slope

Idle Slope (bits per second).

**Definition** ethernet.h:299

[ethernet\_qav\_param::delta\_bandwidth](structethernet__qav__param.md#a6fde906da905c0598aaa2056c330b6f4)

unsigned int delta\_bandwidth

Delta Bandwidth (percentage of bandwidth).

**Definition** ethernet.h:297

[ethernet\_qbu\_param](structethernet__qbu__param.md)

Ethernet Qbu specific parameters.

**Definition** ethernet.h:397

[ethernet\_qbu\_param::frame\_preempt\_statuses](structethernet__qbu__param.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)

enum ethernet\_qbu\_preempt\_status frame\_preempt\_statuses[NET\_TC\_TX\_COUNT]

sequence of framePreemptionAdminStatus values

**Definition** ethernet.h:410

[ethernet\_qbu\_param::release\_advance](structethernet__qbu__param.md#a3f62d0462376225c8609c7e26ebd314b)

uint32\_t release\_advance

Release advance (nanoseconds).

**Definition** ethernet.h:407

[ethernet\_qbu\_param::type](structethernet__qbu__param.md#a4a8a3d26a12a06a787ae6b35ea40c37a)

enum ethernet\_qbu\_param\_type type

Type of Qbu parameter.

**Definition** ethernet.h:401

[ethernet\_qbu\_param::hold\_advance](structethernet__qbu__param.md#a8ffde09a540817b7a68c7180c327196f)

uint32\_t hold\_advance

Hold advance (nanoseconds).

**Definition** ethernet.h:404

[ethernet\_qbu\_param::enabled](structethernet__qbu__param.md#a9717dd68adde62a454593d72fdbc43a5)

bool enabled

True if Qbu is enabled or not.

**Definition** ethernet.h:414

[ethernet\_qbu\_param::link\_partner\_status](structethernet__qbu__param.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca)

bool link\_partner\_status

Link partner status (from Qbr).

**Definition** ethernet.h:417

[ethernet\_qbu\_param::port\_id](structethernet__qbu__param.md#ae6d61f0c9d2f2e56eb494db953a5e846)

int port\_id

Port id.

**Definition** ethernet.h:399

[ethernet\_qbu\_param::additional\_fragment\_size](structethernet__qbu__param.md#afb455507b29d84de42638e47ecacadeb)

uint8\_t additional\_fragment\_size

Additional fragment size (from Qbr).

**Definition** ethernet.h:423

[ethernet\_qbv\_param](structethernet__qbv__param.md)

Ethernet Qbv specific parameters.

**Definition** ethernet.h:330

[ethernet\_qbv\_param::port\_id](structethernet__qbv__param.md#a037492458f47905b894a2269ff7365cd)

int port\_id

Port id.

**Definition** ethernet.h:332

[ethernet\_qbv\_param::enabled](structethernet__qbv__param.md#a0742dbe52f01addbb319e2fcb354d064)

bool enabled

True if Qbv is enabled or not.

**Definition** ethernet.h:339

[ethernet\_qbv\_param::type](structethernet__qbv__param.md#a2184250d397bd749764adc52ec3a1621)

enum ethernet\_qbv\_param\_type type

Type of Qbv parameter.

**Definition** ethernet.h:334

[ethernet\_qbv\_param::row](structethernet__qbv__param.md#a2c256aa3f65dfa75434752903daa809c)

uint16\_t row

Gate control list row.

**Definition** ethernet.h:353

[ethernet\_qbv\_param::state](structethernet__qbv__param.md#a36702c57bea42c37c1341e144ced4f7d)

enum ethernet\_qbv\_state\_type state

What state (Admin/Oper) parameters are these.

**Definition** ethernet.h:336

[ethernet\_qbv\_param::gate\_status](structethernet__qbv__param.md#a44b6ce52faeae761c5ebe49fad5338cd)

bool gate\_status[NET\_TC\_TX\_COUNT]

True = open, False = closed.

**Definition** ethernet.h:344

[ethernet\_qbv\_param::base\_time](structethernet__qbv__param.md#a53646a44e8b0e1f6588c357d49d97693)

struct net\_ptp\_extended\_time base\_time

Base time.

**Definition** ethernet.h:365

[ethernet\_qbv\_param::extension\_time](structethernet__qbv__param.md#a76220e58aa31ae6cfd92268277716c7a)

uint32\_t extension\_time

Extension time (nanoseconds).

**Definition** ethernet.h:371

[ethernet\_qbv\_param::operation](structethernet__qbv__param.md#a8471f7eb20a72bb16fe7abb0b2bb24f7)

enum ethernet\_gate\_state\_operation operation

GateState operation.

**Definition** ethernet.h:347

[ethernet\_qbv\_param::gate\_control](structethernet__qbv__param.md#aa61778228274884ee782e017840acba9)

struct ethernet\_qbv\_param::@121175361150174144233316376176000350036121201324::@102147251204031207263025171335370313217251102106 gate\_control

Gate control information.

[ethernet\_qbv\_param::time\_interval](structethernet__qbv__param.md#aa6b2be0014988752e326bdc1fe6ef161)

uint32\_t time\_interval

Time interval ticks (nanoseconds).

**Definition** ethernet.h:350

[ethernet\_qbv\_param::cycle\_time](structethernet__qbv__param.md#ad07589ae6802a9c3c4c3f809427129be)

struct net\_ptp\_time cycle\_time

Cycle time.

**Definition** ethernet.h:368

[ethernet\_qbv\_param::gate\_control\_list\_len](structethernet__qbv__param.md#afc0c26fcdeee1a921a2f549de4d1c33e)

uint32\_t gate\_control\_list\_len

Number of entries in gate control list.

**Definition** ethernet.h:357

[ethernet\_t1s\_param](structethernet__t1s__param.md)

Ethernet T1S specific parameters.

**Definition** ethernet.h:243

[ethernet\_t1s\_param::burst\_count](structethernet__t1s__param.md#a081fb97c8fd027a5b6bba95f3b6d5acd)

uint8\_t burst\_count

T1S PLCA burst count range: 0x0 to 0xFF.

**Definition** ethernet.h:278

[ethernet\_t1s\_param::plca](structethernet__t1s__param.md#a2f6c32159aaacd91563c7b92fcc98808)

struct ethernet\_t1s\_param::@045104211027030365347006377040354240151366265336::@055246010323023270273151373302031315361103011354 plca

PLCA is the Physical Layer (PHY) Collision Avoidance technique employed with multidrop 10Base-T1S sta...

[ethernet\_t1s\_param::node\_count](structethernet__t1s__param.md#a40b3411132868970c4600bbe4a047d9d)

uint8\_t node\_count

T1S PLCA node count range: 1 to 255.

**Definition** ethernet.h:276

[ethernet\_t1s\_param::to\_timer](structethernet__t1s__param.md#a449472362f5bfeb2ef2ef722030416a8)

uint8\_t to\_timer

T1S PLCA TO value.

**Definition** ethernet.h:282

[ethernet\_t1s\_param::burst\_timer](structethernet__t1s__param.md#a67fba4b2ffe9affaf1cc4f6059c47e71)

uint8\_t burst\_timer

T1S PLCA burst timer.

**Definition** ethernet.h:280

[ethernet\_t1s\_param::node\_id](structethernet__t1s__param.md#a74d407f31c1a37a73e406c89a97725b9)

uint8\_t node\_id

T1S PLCA node id range: 0 to 254.

**Definition** ethernet.h:274

[ethernet\_t1s\_param::type](structethernet__t1s__param.md#a85ed896b8d1c02dbb13fe666cc232c58)

enum ethernet\_t1s\_param\_type type

Type of T1S parameter.

**Definition** ethernet.h:245

[ethernet\_t1s\_param::enable](structethernet__t1s__param.md#add2f6115780c775a41da034443878955)

bool enable

T1S PLCA enabled.

**Definition** ethernet.h:272

[ethernet\_txtime\_param](structethernet__txtime__param.md)

Ethernet TXTIME specific parameters.

**Definition** ethernet.h:464

[ethernet\_txtime\_param::enable\_txtime](structethernet__txtime__param.md#a74b1e05cf0fac8aa435ba966e110ae27)

bool enable\_txtime

Enable or disable TXTIME per queue.

**Definition** ethernet.h:470

[ethernet\_txtime\_param::queue\_id](structethernet__txtime__param.md#aa4a46b7153b2a69ca0134f4e10bc7165)

int queue\_id

Queue number for configuring TXTIME.

**Definition** ethernet.h:468

[ethernet\_txtime\_param::type](structethernet__txtime__param.md#ab4a709e6907e76f9cf23c085f5be5d99)

enum ethernet\_txtime\_param\_type type

Type of TXTIME parameter.

**Definition** ethernet.h:466

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:51

[net\_eth\_addr::addr](structnet__eth__addr.md#af370baeb1f10475331db8628c3c9efbe)

uint8\_t addr[6U]

Buffer storing the address.

**Definition** ethernet.h:52

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_lldpdu](structnet__lldpdu.md)

LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in "8.2 LLDPDU format" fro...

**Definition** lldp.h:167

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_ptp\_extended\_time](structnet__ptp__extended__time.md)

Generalized Precision Time Protocol Extended Timestamp format.

**Definition** ptp\_time.h:152

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:109

[net\_stats\_eth](structnet__stats__eth.md)

All Ethernet specific statistics.

**Definition** net\_stats.h:523

[atomic.h](sys_2atomic_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet.h](ethernet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
