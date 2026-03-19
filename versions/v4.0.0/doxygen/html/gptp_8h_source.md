---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gptp_8h_source.html
original_path: doxygen/html/gptp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp.h

[Go to the documentation of this file.](gptp_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_GPTP\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_GPTP\_H\_

15

24

25#include <[zephyr/net/net\_core.h](net__core_8h.md)>

26#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

27#include <[stdbool.h](stdbool_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

34

35#define GPTP\_OFFSET\_SCALED\_LOG\_VAR\_UNKNOWN 0x436A

36

37#define GPTP\_PRIORITY1\_NON\_GM\_CAPABLE 255

38#define GPTP\_PRIORITY1\_GM\_CAPABLE 248

39

40#if defined(CONFIG\_NET\_GPTP\_BMCA\_PRIORITY2)

41#define GPTP\_PRIORITY2\_DEFAULT CONFIG\_NET\_GPTP\_BMCA\_PRIORITY2

42#else

43#define GPTP\_PRIORITY2\_DEFAULT 248

44#endif

45

47

[ 51](structgptp__scaled__ns.md)struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) {

[ 53](structgptp__scaled__ns.md#af35add15383b49b677e604d61b3d9739) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [high](structgptp__scaled__ns.md#af35add15383b49b677e604d61b3d9739);

54

[ 56](structgptp__scaled__ns.md#ac1e95f32bdb1a98f945d9d05a28e8f7f) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [low](structgptp__scaled__ns.md#ac1e95f32bdb1a98f945d9d05a28e8f7f);

57} \_\_packed;

58

[ 62](structgptp__uscaled__ns.md)struct [gptp\_uscaled\_ns](structgptp__uscaled__ns.md) {

[ 64](structgptp__uscaled__ns.md#a11cd4f2cc15731ba91dab742fcea248f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [high](structgptp__uscaled__ns.md#a11cd4f2cc15731ba91dab742fcea248f);

65

[ 67](structgptp__uscaled__ns.md#ae374e99c81753ecd26ff9a7cac35dfa4) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [low](structgptp__uscaled__ns.md#ae374e99c81753ecd26ff9a7cac35dfa4);

68} \_\_packed;

69

71

72#if defined(CONFIG\_NEWLIB\_LIBC)

73#include <[math.h](math_8h.md)>

74

75#define GPTP\_POW2(exp) pow(2, exp)

76#else

77

78static inline double gptp\_pow2(int exp)

79{

80 double res;

81

82 if (exp >= 0) {

83 res = 1 << exp;

84 } else {

85 res = 1.0;

86

87 while (exp++) {

88 res /= 2;

89 }

90 }

91

92 return res;

93}

94

95#define GPTP\_POW2(exp) gptp\_pow2(exp)

96#endif

97

98/\* Pre-calculated constants \*/

99/\* 2^16 \*/

100#define GPTP\_POW2\_16 65536.0

101/\* 2^41 \*/

102#define GPTP\_POW2\_41 2199023255552.0

103

104/\* Message types. Event messages have BIT(3) set to 0, and general messages

105 \* have that bit set to 1. IEEE 802.1AS chapter 10.5.2.2.2

106 \*/

107#define GPTP\_SYNC\_MESSAGE 0x00

108#define GPTP\_DELAY\_REQ\_MESSAGE 0x01

109#define GPTP\_PATH\_DELAY\_REQ\_MESSAGE 0x02

110#define GPTP\_PATH\_DELAY\_RESP\_MESSAGE 0x03

111#define GPTP\_FOLLOWUP\_MESSAGE 0x08

112#define GPTP\_DELAY\_RESP\_MESSAGE 0x09

113#define GPTP\_PATH\_DELAY\_FOLLOWUP\_MESSAGE 0x0a

114#define GPTP\_ANNOUNCE\_MESSAGE 0x0b

115#define GPTP\_SIGNALING\_MESSAGE 0x0c

116#define GPTP\_MANAGEMENT\_MESSAGE 0x0d

117

118#define GPTP\_IS\_EVENT\_MSG(msg\_type) (!((msg\_type) & BIT(3)))

119

120#define GPTP\_CLOCK\_ID\_LEN 8

121

123

[ 127](structgptp__port__identity.md)struct [gptp\_port\_identity](structgptp__port__identity.md) {

[ 129](structgptp__port__identity.md#a6e8473ae6ecb4ec35e3a6b5d79851fc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clk\_id](structgptp__port__identity.md#a6e8473ae6ecb4ec35e3a6b5d79851fc3)[GPTP\_CLOCK\_ID\_LEN];

130

[ 132](structgptp__port__identity.md#a5a0d4038aa88792290bc4619379ee48f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port\_number](structgptp__port__identity.md#a5a0d4038aa88792290bc4619379ee48f);

133} \_\_packed;

134

[ 136](structgptp__flags.md)struct [gptp\_flags](structgptp__flags.md) {

137 union {

[ 139](structgptp__flags.md#a90b2862e78ece1b9b7f5109f5cd5f0fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [octets](structgptp__flags.md#a90b2862e78ece1b9b7f5109f5cd5f0fd)[2];

140

[ 142](structgptp__flags.md#a36871fbae0484379b00c415affdb3f9d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [all](structgptp__flags.md#a36871fbae0484379b00c415affdb3f9d);

143 };

144} \_\_packed;

145

[ 147](structgptp__hdr.md)struct [gptp\_hdr](structgptp__hdr.md) {

[ 149](structgptp__hdr.md#adbc9eed0fdaf07410542780c3794d642) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [message\_type](structgptp__hdr.md#adbc9eed0fdaf07410542780c3794d642):4;

150

[ 152](structgptp__hdr.md#acc57b0662f64bda3bc21c9c8b6286052) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transport\_specific](structgptp__hdr.md#acc57b0662f64bda3bc21c9c8b6286052):4;

153

[ 155](structgptp__hdr.md#aab942e44507bcff9af8e0a168b9fb810) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ptp\_version](structgptp__hdr.md#aab942e44507bcff9af8e0a168b9fb810):4;

156

[ 158](structgptp__hdr.md#af9f79833695719ef42ecf0536bdfc317) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved0](structgptp__hdr.md#af9f79833695719ef42ecf0536bdfc317):4;

159

[ 161](structgptp__hdr.md#ab58626c44b57827266606a4b85bf25cc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_length](structgptp__hdr.md#ab58626c44b57827266606a4b85bf25cc);

162

[ 164](structgptp__hdr.md#a435a37858ba67222f22d4cfde3322511) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_number](structgptp__hdr.md#a435a37858ba67222f22d4cfde3322511);

165

[ 167](structgptp__hdr.md#aec4214f5392123bb3cd328b94aea8d2a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved1](structgptp__hdr.md#aec4214f5392123bb3cd328b94aea8d2a);

168

[ 170](structgptp__hdr.md#a4c6eadb27839a3b45461df5e2078b5a7) struct [gptp\_flags](structgptp__flags.md) [flags](structgptp__hdr.md#a4c6eadb27839a3b45461df5e2078b5a7);

171

[ 173](structgptp__hdr.md#a38d80a7ef0ed94c50baf6285b735cf4d) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [correction\_field](structgptp__hdr.md#a38d80a7ef0ed94c50baf6285b735cf4d);

174

[ 176](structgptp__hdr.md#ac6340bd434fad75f7faa8386bb591412) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved2](structgptp__hdr.md#ac6340bd434fad75f7faa8386bb591412);

177

[ 179](structgptp__hdr.md#a7e89c039b956b5fa7229b58dde855a20) struct [gptp\_port\_identity](structgptp__port__identity.md) [port\_id](structgptp__hdr.md#a7e89c039b956b5fa7229b58dde855a20);

180

[ 182](structgptp__hdr.md#a50f192fb70ae8633c80fa5eeb178f852) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sequence\_id](structgptp__hdr.md#a50f192fb70ae8633c80fa5eeb178f852);

183

[ 185](structgptp__hdr.md#a68f6642239b801f2fe602a4331743d83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [control](structgptp__hdr.md#a68f6642239b801f2fe602a4331743d83);

186

[ 188](structgptp__hdr.md#a5fab00d293c3fb38fedf483b11f72890) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [log\_msg\_interval](structgptp__hdr.md#a5fab00d293c3fb38fedf483b11f72890);

189} \_\_packed;

190

192

193#define GPTP\_GET\_CURRENT\_TIME\_USCALED\_NS(port, uscaled\_ns\_ptr) \

194 do { \

195 (uscaled\_ns\_ptr)->low = \

196 gptp\_get\_current\_time\_nanosecond(port) << 16; \

197 (uscaled\_ns\_ptr)->high = 0; \

198 } while (false)

199

201

[ 215](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b)typedef void (\*[gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b))(

216 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*gm\_identity,

217 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*time\_base,

218 struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) \*last\_gm\_ph\_change,

219 double \*last\_gm\_freq\_change);

220

[ 229](structgptp__phase__dis__cb.md)struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) {

[ 231](structgptp__phase__dis__cb.md#a9801de29992ae2f23bbe89c417d58fe3) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structgptp__phase__dis__cb.md#a9801de29992ae2f23bbe89c417d58fe3);

232

[ 234](structgptp__phase__dis__cb.md#a8294a9abac55d1f4406923ea4e8ed144) [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b) [cb](structgptp__phase__dis__cb.md#a8294a9abac55d1f4406923ea4e8ed144);

235};

236

[ 242](structgptp__clk__src__time__invoke__params.md)struct [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) {

[ 244](structgptp__clk__src__time__invoke__params.md#aaf1ca90ce4e1b216c2edbb9fa72b044a) double [last\_gm\_freq\_change](structgptp__clk__src__time__invoke__params.md#aaf1ca90ce4e1b216c2edbb9fa72b044a);

245

[ 247](structgptp__clk__src__time__invoke__params.md#a990360a4fdc5bdc8f6626e9dfdc05563) struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) [src\_time](structgptp__clk__src__time__invoke__params.md#a990360a4fdc5bdc8f6626e9dfdc05563);

248

[ 250](structgptp__clk__src__time__invoke__params.md#ab2328d1a7458ccc8e7fe771e50b463eb) struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) [last\_gm\_phase\_change](structgptp__clk__src__time__invoke__params.md#ab2328d1a7458ccc8e7fe771e50b463eb);

251

[ 253](structgptp__clk__src__time__invoke__params.md#ada4c313104488059a520d4a2ffff33b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [time\_base\_indicator](structgptp__clk__src__time__invoke__params.md#ada4c313104488059a520d4a2ffff33b4);

254};

255

[ 262](group__gptp.md#gaad2282df9cbf7f05f557285323af8f07)void [gptp\_register\_phase\_dis\_cb](group__gptp.md#gaad2282df9cbf7f05f557285323af8f07)(struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis,

263 [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b) cb);

264

[ 270](group__gptp.md#ga55d95859e5ec586cb2341929901220dd)void [gptp\_unregister\_phase\_dis\_cb](group__gptp.md#ga55d95859e5ec586cb2341929901220dd)(struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis);

271

[ 275](group__gptp.md#ga29bf157d06a5ec5bb5a2a8a0e986709d)void [gptp\_call\_phase\_dis\_cb](group__gptp.md#ga29bf157d06a5ec5bb5a2a8a0e986709d)(void);

276

[ 286](group__gptp.md#ga9a8e2ccf20d0430b4e62f3302462c6eb)int [gptp\_event\_capture](group__gptp.md#ga9a8e2ccf20d0430b4e62f3302462c6eb)(struct [net\_ptp\_time](structnet__ptp__time.md) \*slave\_time, bool \*gm\_present);

287

[ 297](group__gptp.md#ga40121c2957d58b0b5bb4468eac5de259)char \*[gptp\_sprint\_clock\_id](group__gptp.md#ga40121c2957d58b0b5bb4468eac5de259)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*clk\_id, char \*output,

298 size\_t output\_len);

299

[ 308](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d)typedef void (\*[gptp\_port\_cb\_t](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d))(int port, struct [net\_if](structnet__if.md) \*iface,

309 void \*user\_data);

310

[ 317](group__gptp.md#ga06ddd41c7adf9e387d1b23bcdfccbddc)void [gptp\_foreach\_port](group__gptp.md#ga06ddd41c7adf9e387d1b23bcdfccbddc)([gptp\_port\_cb\_t](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d) cb, void \*user\_data);

318

[ 325](group__gptp.md#gae4c3aac6b88e9ce21a32ba3263b9ad59)struct gptp\_domain \*[gptp\_get\_domain](group__gptp.md#gae4c3aac6b88e9ce21a32ba3263b9ad59)(void);

326

[ 333](group__gptp.md#ga9b27c9a741fb0ca72eff78e334e629fe)void [gptp\_clk\_src\_time\_invoke](group__gptp.md#ga9b27c9a741fb0ca72eff78e334e629fe)(struct [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) \*arg);

334

[ 342](group__gptp.md#ga5b46fb7bbe1a380e3c327c8f5abbabeb)struct [gptp\_hdr](structgptp__hdr.md) \*[gptp\_get\_hdr](group__gptp.md#ga5b46fb7bbe1a380e3c327c8f5abbabeb)(struct [net\_pkt](structnet__pkt.md) \*pkt);

343

344#ifdef \_\_cplusplus

345}

346#endif

347

351

352#endif /\* ZEPHYR\_INCLUDE\_NET\_GPTP\_H\_ \*/

[gptp\_foreach\_port](group__gptp.md#ga06ddd41c7adf9e387d1b23bcdfccbddc)

void gptp\_foreach\_port(gptp\_port\_cb\_t cb, void \*user\_data)

Go through all the gPTP ports and call callback for each of them.

[gptp\_call\_phase\_dis\_cb](group__gptp.md#ga29bf157d06a5ec5bb5a2a8a0e986709d)

void gptp\_call\_phase\_dis\_cb(void)

Call a phase discontinuity callback function.

[gptp\_sprint\_clock\_id](group__gptp.md#ga40121c2957d58b0b5bb4468eac5de259)

char \* gptp\_sprint\_clock\_id(const uint8\_t \*clk\_id, char \*output, size\_t output\_len)

Utility function to print clock id to a user supplied buffer.

[gptp\_unregister\_phase\_dis\_cb](group__gptp.md#ga55d95859e5ec586cb2341929901220dd)

void gptp\_unregister\_phase\_dis\_cb(struct gptp\_phase\_dis\_cb \*phase\_dis)

Unregister a phase discontinuity callback.

[gptp\_get\_hdr](group__gptp.md#ga5b46fb7bbe1a380e3c327c8f5abbabeb)

struct gptp\_hdr \* gptp\_get\_hdr(struct net\_pkt \*pkt)

Return pointer to gPTP packet header in network packet.

[gptp\_event\_capture](group__gptp.md#ga9a8e2ccf20d0430b4e62f3302462c6eb)

int gptp\_event\_capture(struct net\_ptp\_time \*slave\_time, bool \*gm\_present)

Get gPTP time.

[gptp\_clk\_src\_time\_invoke](group__gptp.md#ga9b27c9a741fb0ca72eff78e334e629fe)

void gptp\_clk\_src\_time\_invoke(struct gptp\_clk\_src\_time\_invoke\_params \*arg)

This interface is used by the ClockSource entity to provide time to the ClockMaster entity of a time-...

[gptp\_port\_cb\_t](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d)

void(\* gptp\_port\_cb\_t)(int port, struct net\_if \*iface, void \*user\_data)

Callback used while iterating over gPTP ports.

**Definition** gptp.h:308

[gptp\_register\_phase\_dis\_cb](group__gptp.md#gaad2282df9cbf7f05f557285323af8f07)

void gptp\_register\_phase\_dis\_cb(struct gptp\_phase\_dis\_cb \*phase\_dis, gptp\_phase\_dis\_callback\_t cb)

Register a phase discontinuity callback.

[gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b)

void(\* gptp\_phase\_dis\_callback\_t)(uint8\_t \*gm\_identity, uint16\_t \*time\_base, struct gptp\_scaled\_ns \*last\_gm\_ph\_change, double \*last\_gm\_freq\_change)

Define callback that is called after a phase discontinuity has been sent by the grandmaster.

**Definition** gptp.h:215

[gptp\_get\_domain](group__gptp.md#gae4c3aac6b88e9ce21a32ba3263b9ad59)

struct gptp\_domain \* gptp\_get\_domain(void)

Get gPTP domain.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[math.h](math_8h.md)

[net\_core.h](net__core_8h.md)

Network core definitions.

[ptp\_time.h](ptp__time_8h.md)

Public functions for the Precision Time Protocol time specification.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

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

[gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md)

ClockSourceTime.invoke function parameters.

**Definition** gptp.h:242

[gptp\_clk\_src\_time\_invoke\_params::src\_time](structgptp__clk__src__time__invoke__params.md#a990360a4fdc5bdc8f6626e9dfdc05563)

struct net\_ptp\_extended\_time src\_time

The time this function is invoked.

**Definition** gptp.h:247

[gptp\_clk\_src\_time\_invoke\_params::last\_gm\_freq\_change](structgptp__clk__src__time__invoke__params.md#aaf1ca90ce4e1b216c2edbb9fa72b044a)

double last\_gm\_freq\_change

Frequency change on the last Time Base Indicator Change.

**Definition** gptp.h:244

[gptp\_clk\_src\_time\_invoke\_params::last\_gm\_phase\_change](structgptp__clk__src__time__invoke__params.md#ab2328d1a7458ccc8e7fe771e50b463eb)

struct gptp\_scaled\_ns last\_gm\_phase\_change

Phase change on the last Time Base Indicator Change.

**Definition** gptp.h:250

[gptp\_clk\_src\_time\_invoke\_params::time\_base\_indicator](structgptp__clk__src__time__invoke__params.md#ada4c313104488059a520d4a2ffff33b4)

uint16\_t time\_base\_indicator

Time Base - changed only if Phase or Frequency changes.

**Definition** gptp.h:253

[gptp\_flags](structgptp__flags.md)

gPTP message flags

**Definition** gptp.h:136

[gptp\_flags::all](structgptp__flags.md#a36871fbae0484379b00c415affdb3f9d)

uint16\_t all

Whole field access.

**Definition** gptp.h:142

[gptp\_flags::octets](structgptp__flags.md#a90b2862e78ece1b9b7f5109f5cd5f0fd)

uint8\_t octets[2]

Byte access.

**Definition** gptp.h:139

[gptp\_hdr](structgptp__hdr.md)

gPTP message header

**Definition** gptp.h:147

[gptp\_hdr::correction\_field](structgptp__hdr.md#a38d80a7ef0ed94c50baf6285b735cf4d)

int64\_t correction\_field

Correction Field.

**Definition** gptp.h:173

[gptp\_hdr::domain\_number](structgptp__hdr.md#a435a37858ba67222f22d4cfde3322511)

uint8\_t domain\_number

Domain number, always 0.

**Definition** gptp.h:164

[gptp\_hdr::flags](structgptp__hdr.md#a4c6eadb27839a3b45461df5e2078b5a7)

struct gptp\_flags flags

Message flags.

**Definition** gptp.h:170

[gptp\_hdr::sequence\_id](structgptp__hdr.md#a50f192fb70ae8633c80fa5eeb178f852)

uint16\_t sequence\_id

Sequence Id.

**Definition** gptp.h:182

[gptp\_hdr::log\_msg\_interval](structgptp__hdr.md#a5fab00d293c3fb38fedf483b11f72890)

int8\_t log\_msg\_interval

Message Interval in Log2 for Sync and Announce messages.

**Definition** gptp.h:188

[gptp\_hdr::control](structgptp__hdr.md#a68f6642239b801f2fe602a4331743d83)

uint8\_t control

Control value.

**Definition** gptp.h:185

[gptp\_hdr::port\_id](structgptp__hdr.md#a7e89c039b956b5fa7229b58dde855a20)

struct gptp\_port\_identity port\_id

Port Identity of the sender.

**Definition** gptp.h:179

[gptp\_hdr::ptp\_version](structgptp__hdr.md#aab942e44507bcff9af8e0a168b9fb810)

uint8\_t ptp\_version

Version of the PTP, always 2.

**Definition** gptp.h:155

[gptp\_hdr::message\_length](structgptp__hdr.md#ab58626c44b57827266606a4b85bf25cc)

uint16\_t message\_length

Total length of the message from the header to the last TLV.

**Definition** gptp.h:161

[gptp\_hdr::reserved2](structgptp__hdr.md#ac6340bd434fad75f7faa8386bb591412)

uint32\_t reserved2

Reserved field.

**Definition** gptp.h:176

[gptp\_hdr::transport\_specific](structgptp__hdr.md#acc57b0662f64bda3bc21c9c8b6286052)

uint8\_t transport\_specific

Transport specific, always 1.

**Definition** gptp.h:152

[gptp\_hdr::message\_type](structgptp__hdr.md#adbc9eed0fdaf07410542780c3794d642)

uint8\_t message\_type

Type of the message.

**Definition** gptp.h:149

[gptp\_hdr::reserved1](structgptp__hdr.md#aec4214f5392123bb3cd328b94aea8d2a)

uint8\_t reserved1

Reserved field.

**Definition** gptp.h:167

[gptp\_hdr::reserved0](structgptp__hdr.md#af9f79833695719ef42ecf0536bdfc317)

uint8\_t reserved0

Reserved field.

**Definition** gptp.h:158

[gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md)

Phase discontinuity callback structure.

**Definition** gptp.h:229

[gptp\_phase\_dis\_cb::cb](structgptp__phase__dis__cb.md#a8294a9abac55d1f4406923ea4e8ed144)

gptp\_phase\_dis\_callback\_t cb

Phase discontinuity callback.

**Definition** gptp.h:234

[gptp\_phase\_dis\_cb::node](structgptp__phase__dis__cb.md#a9801de29992ae2f23bbe89c417d58fe3)

sys\_snode\_t node

Node information for the slist.

**Definition** gptp.h:231

[gptp\_port\_identity](structgptp__port__identity.md)

Port Identity.

**Definition** gptp.h:127

[gptp\_port\_identity::port\_number](structgptp__port__identity.md#a5a0d4038aa88792290bc4619379ee48f)

uint16\_t port\_number

Number of the port.

**Definition** gptp.h:132

[gptp\_port\_identity::clk\_id](structgptp__port__identity.md#a6e8473ae6ecb4ec35e3a6b5d79851fc3)

uint8\_t clk\_id[GPTP\_CLOCK\_ID\_LEN]

Clock identity of the port.

**Definition** gptp.h:129

[gptp\_scaled\_ns](structgptp__scaled__ns.md)

Scaled Nanoseconds.

**Definition** gptp.h:51

[gptp\_scaled\_ns::low](structgptp__scaled__ns.md#ac1e95f32bdb1a98f945d9d05a28e8f7f)

int64\_t low

Low half.

**Definition** gptp.h:56

[gptp\_scaled\_ns::high](structgptp__scaled__ns.md#af35add15383b49b677e604d61b3d9739)

int32\_t high

High half.

**Definition** gptp.h:53

[gptp\_uscaled\_ns](structgptp__uscaled__ns.md)

UScaled Nanoseconds.

**Definition** gptp.h:62

[gptp\_uscaled\_ns::high](structgptp__uscaled__ns.md#a11cd4f2cc15731ba91dab742fcea248f)

uint32\_t high

High half.

**Definition** gptp.h:64

[gptp\_uscaled\_ns::low](structgptp__uscaled__ns.md#ae374e99c81753ecd26ff9a7cac35dfa4)

uint64\_t low

Low half.

**Definition** gptp.h:67

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[net\_ptp\_extended\_time](structnet__ptp__extended__time.md)

Generalized Precision Time Protocol Extended Timestamp format.

**Definition** ptp\_time.h:154

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:111

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [gptp.h](gptp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
