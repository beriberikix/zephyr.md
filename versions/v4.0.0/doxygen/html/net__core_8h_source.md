---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__core_8h_source.html
original_path: doxygen/html/net__core_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

38

47

49

50/\* Network subsystem logging helpers \*/

51#ifdef CONFIG\_THREAD\_NAME

52#define NET\_DBG(fmt, ...) LOG\_DBG("(%s): " fmt, \

53 k\_thread\_name\_get(k\_current\_get()), \

54 ##\_\_VA\_ARGS\_\_)

55#else

56#define NET\_DBG(fmt, ...) LOG\_DBG("(%p): " fmt, k\_current\_get(), \

57 ##\_\_VA\_ARGS\_\_)

58#endif /\* CONFIG\_THREAD\_NAME \*/

59#define NET\_ERR(fmt, ...) LOG\_ERR(fmt, ##\_\_VA\_ARGS\_\_)

60#define NET\_WARN(fmt, ...) LOG\_WRN(fmt, ##\_\_VA\_ARGS\_\_)

61#define NET\_INFO(fmt, ...) LOG\_INF(fmt, ##\_\_VA\_ARGS\_\_)

62

63#define NET\_HEXDUMP\_DBG(\_data, \_length, \_str) LOG\_HEXDUMP\_DBG(\_data, \_length, \_str)

64#define NET\_HEXDUMP\_ERR(\_data, \_length, \_str) LOG\_HEXDUMP\_ERR(\_data, \_length, \_str)

65#define NET\_HEXDUMP\_WARN(\_data, \_length, \_str) LOG\_HEXDUMP\_WRN(\_data, \_length, \_str)

66#define NET\_HEXDUMP\_INFO(\_data, \_length, \_str) LOG\_HEXDUMP\_INF(\_data, \_length, \_str)

67

68#define NET\_ASSERT(cond, ...) \_\_ASSERT(cond, "" \_\_VA\_ARGS\_\_)

69

70/\* This needs to be here in order to avoid circular include dependency between

71 \* net\_pkt.h and net\_if.h

72 \*/

73#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

74 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

75#if !defined(NET\_PKT\_DETAIL\_STATS\_COUNT)

76#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

77

78#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

79#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

80#else

81#define NET\_PKT\_DETAIL\_STATS\_COUNT 3

82#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

83

84#else

85#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

86#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL \*/

87

88#endif /\* !NET\_PKT\_DETAIL\_STATS\_COUNT \*/

89#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

90 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

91

93

94struct [net\_buf](structnet__buf.md);

95struct [net\_pkt](structnet__pkt.md);

96struct [net\_context](structnet__context.md);

97struct [net\_if](structnet__if.md);

98

[ 102](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) {

[ 104](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047),

[ 108](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) [NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f),

[ 110](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3),

111};

112

[ 123](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)int [net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

124

[ 137](group__net__core.md#ga1a1699666716229a59486a51e46044fc)int [net\_send\_data](group__net__core.md#ga1a1699666716229a59486a51e46044fc)(struct [net\_pkt](structnet__pkt.md) \*pkt);

138

140

141/\* Some helper defines for traffic class support \*/

142#if defined(CONFIG\_NET\_TC\_TX\_COUNT) && defined(CONFIG\_NET\_TC\_RX\_COUNT)

143#define NET\_TC\_TX\_COUNT CONFIG\_NET\_TC\_TX\_COUNT

144#define NET\_TC\_RX\_COUNT CONFIG\_NET\_TC\_RX\_COUNT

145

146#if NET\_TC\_TX\_COUNT > NET\_TC\_RX\_COUNT

147#define NET\_TC\_COUNT NET\_TC\_TX\_COUNT

148#else

149#define NET\_TC\_COUNT NET\_TC\_RX\_COUNT

150#endif

151#else /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

152#define NET\_TC\_TX\_COUNT 0

153#define NET\_TC\_RX\_COUNT 0

154#define NET\_TC\_COUNT 0

155#endif /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

156

157/\* @endcond \*/

158

162

163#ifdef \_\_cplusplus

164}

165#endif

166

167#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[net\_send\_data](group__net__core.md#ga1a1699666716229a59486a51e46044fc)

int net\_send\_data(struct net\_pkt \*pkt)

Send data to network.

[net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)

int net\_recv\_data(struct net\_if \*iface, struct net\_pkt \*pkt)

Called by lower network stack or network device driver when a network packet has been received.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:102

[NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)

@ NET\_OK

Packet has been taken care of.

**Definition** net\_core.h:104

[NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)

@ NET\_DROP

Packet must be dropped.

**Definition** net\_core.h:110

[NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)

@ NET\_CONTINUE

Packet has not been touched, other part should decide about its fate.

**Definition** net\_core.h:108

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log.h](log_8h.md)

[net\_timeout.h](net__timeout_8h.md)

Network timer with wrap around.

[stdbool.h](stdbool_8h.md)

[string.h](string_8h.md)

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:207

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_core.h](net__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
