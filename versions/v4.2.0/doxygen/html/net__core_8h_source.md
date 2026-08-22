---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__core_8h_source.html
original_path: doxygen/html/net__core_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_core.h

[Go to the documentation of this file.](net__core_8h.md)

1

6

7/\*

8 \* Copyright (c) 2015 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_

15

16#include <[stdbool.h](stdbool_8h.md)>

17#include <[string.h](string_8h.md)>

18

19#include <[zephyr/logging/log.h](log_8h.md)>

20#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

21#include <[zephyr/kernel.h](kernel_8h.md)>

22

23#include <[zephyr/net/net\_timeout.h](net__timeout_8h.md)>

24#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

39

48

50

51/\* Network subsystem logging helpers \*/

52#ifdef CONFIG\_THREAD\_NAME

53#define NET\_DBG(fmt, ...) LOG\_DBG("(%s): " fmt, \

54 k\_thread\_name\_get(k\_current\_get()), \

55 ##\_\_VA\_ARGS\_\_)

56#else

57#define NET\_DBG(fmt, ...) LOG\_DBG("(%p): " fmt, k\_current\_get(), \

58 ##\_\_VA\_ARGS\_\_)

59#endif /\* CONFIG\_THREAD\_NAME \*/

60#define NET\_ERR(fmt, ...) LOG\_ERR(fmt, ##\_\_VA\_ARGS\_\_)

61#define NET\_WARN(fmt, ...) LOG\_WRN(fmt, ##\_\_VA\_ARGS\_\_)

62#define NET\_INFO(fmt, ...) LOG\_INF(fmt, ##\_\_VA\_ARGS\_\_)

63

64#define NET\_HEXDUMP\_DBG(\_data, \_length, \_str) LOG\_HEXDUMP\_DBG(\_data, \_length, \_str)

65#define NET\_HEXDUMP\_ERR(\_data, \_length, \_str) LOG\_HEXDUMP\_ERR(\_data, \_length, \_str)

66#define NET\_HEXDUMP\_WARN(\_data, \_length, \_str) LOG\_HEXDUMP\_WRN(\_data, \_length, \_str)

67#define NET\_HEXDUMP\_INFO(\_data, \_length, \_str) LOG\_HEXDUMP\_INF(\_data, \_length, \_str)

68

69#define NET\_ASSERT(cond, ...) \_\_ASSERT(cond, "" \_\_VA\_ARGS\_\_)

70

71/\* This needs to be here in order to avoid circular include dependency between

72 \* net\_pkt.h and net\_if.h

73 \*/

74#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

75 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

76#if !defined(NET\_PKT\_DETAIL\_STATS\_COUNT)

77#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

78

79#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

80#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

81#else

82#define NET\_PKT\_DETAIL\_STATS\_COUNT 3

83#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

84

85#else

86#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

87#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL \*/

88

89#endif /\* !NET\_PKT\_DETAIL\_STATS\_COUNT \*/

90#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

91 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

92

94

95struct [net\_buf](structnet__buf.md);

96struct [net\_pkt](structnet__pkt.md);

97struct [net\_context](structnet__context.md);

98struct [net\_if](structnet__if.md);

99

[ 103](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) {

[ 105](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047),

[ 109](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) [NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f),

[ 111](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3),

112};

113

[ 124](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)int [net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

125

[ 139](group__net__core.md#gaade26b02f8fbac7989fe1b021269b08c)int [net\_try\_send\_data](group__net__core.md#gaade26b02f8fbac7989fe1b021269b08c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

140

[ 153](group__net__core.md#ga815b4cf2db95b80bfd9a576f12ebf6ff)static inline int [net\_send\_data](group__net__core.md#ga815b4cf2db95b80bfd9a576f12ebf6ff)(struct [net\_pkt](structnet__pkt.md) \*pkt)

154{

155 [k\_timeout\_t](structk__timeout__t.md) timeout = [k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)() ? [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) : [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca);

156

157 return [net\_try\_send\_data](group__net__core.md#gaade26b02f8fbac7989fe1b021269b08c)(pkt, timeout);

158}

159

161

162/\* Some helper defines for traffic class support \*/

163#if defined(CONFIG\_NET\_TC\_TX\_COUNT) && defined(CONFIG\_NET\_TC\_RX\_COUNT)

164#define NET\_TC\_TX\_COUNT CONFIG\_NET\_TC\_TX\_COUNT

165#define NET\_TC\_RX\_COUNT CONFIG\_NET\_TC\_RX\_COUNT

166

167#if NET\_TC\_TX\_COUNT > NET\_TC\_RX\_COUNT

168#define NET\_TC\_COUNT NET\_TC\_TX\_COUNT

169#else

170#define NET\_TC\_COUNT NET\_TC\_RX\_COUNT

171#endif

172#else /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

173#define NET\_TC\_TX\_COUNT 0

174#define NET\_TC\_RX\_COUNT 0

175#define NET\_TC\_COUNT 0

176#endif /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

177

185struct net\_l3\_register {

189 const char \* const name;

191 const struct net\_l2 \* const l2;

200 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*handler)(struct net\_if \*iface,

201 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype,

202 struct net\_pkt \*pkt);

204 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype;

205};

206

207#define NET\_L3\_GET\_NAME(l3\_name, ptype) \_\_net\_l3\_register\_##l3\_name##\_##ptype

208

209#define NET\_L3\_REGISTER(\_l2\_type, \_name, \_ptype, \_handler) \

210 static const STRUCT\_SECTION\_ITERABLE(net\_l3\_register, \

211 NET\_L3\_GET\_NAME(\_name, \_ptype)) = { \

212 .ptype = \_ptype, \

213 .handler = \_handler, \

214 .name = STRINGIFY(\_name), \

215 .l2 = \_l2\_type, \

216 };

217

218/\* @endcond \*/

219

223

224#ifdef \_\_cplusplus

225}

226#endif

227

228#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1481

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1371

[k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16)

bool k\_is\_in\_isr(void)

Determine if code is running at interrupt level.

[net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)

int net\_recv\_data(struct net\_if \*iface, struct net\_pkt \*pkt)

Called by lower network stack or network device driver when a network packet has been received.

[net\_send\_data](group__net__core.md#ga815b4cf2db95b80bfd9a576f12ebf6ff)

static int net\_send\_data(struct net\_pkt \*pkt)

Send data to network.

**Definition** net\_core.h:153

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[net\_try\_send\_data](group__net__core.md#gaade26b02f8fbac7989fe1b021269b08c)

int net\_try\_send\_data(struct net\_pkt \*pkt, k\_timeout\_t timeout)

Try sending data to network.

[NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)

@ NET\_OK

Packet has been taken care of.

**Definition** net\_core.h:105

[NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)

@ NET\_DROP

Packet must be dropped.

**Definition** net\_core.h:111

[NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)

@ NET\_CONTINUE

Packet has not been touched, other part should decide about its fate.

**Definition** net\_core.h:109

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log.h](log_8h.md)

[net\_linkaddr.h](net__linkaddr_8h.md)

Public API for network link address.

[net\_timeout.h](net__timeout_8h.md)

Network timer with wrap around.

[stdbool.h](stdbool_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[string.h](string_8h.md)

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:208

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_core.h](net__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
