---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__core_8h_source.html
original_path: doxygen/html/net__core_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

45

47

48/\* Network subsystem logging helpers \*/

49#ifdef CONFIG\_THREAD\_NAME

50#define NET\_DBG(fmt, ...) LOG\_DBG("(%s): " fmt, \

51 k\_thread\_name\_get(k\_current\_get()), \

52 ##\_\_VA\_ARGS\_\_)

53#else

54#define NET\_DBG(fmt, ...) LOG\_DBG("(%p): " fmt, k\_current\_get(), \

55 ##\_\_VA\_ARGS\_\_)

56#endif /\* CONFIG\_THREAD\_NAME \*/

57#define NET\_ERR(fmt, ...) LOG\_ERR(fmt, ##\_\_VA\_ARGS\_\_)

58#define NET\_WARN(fmt, ...) LOG\_WRN(fmt, ##\_\_VA\_ARGS\_\_)

59#define NET\_INFO(fmt, ...) LOG\_INF(fmt, ##\_\_VA\_ARGS\_\_)

60

61#define NET\_HEXDUMP\_DBG(\_data, \_length, \_str) LOG\_HEXDUMP\_DBG(\_data, \_length, \_str)

62#define NET\_HEXDUMP\_ERR(\_data, \_length, \_str) LOG\_HEXDUMP\_ERR(\_data, \_length, \_str)

63#define NET\_HEXDUMP\_WARN(\_data, \_length, \_str) LOG\_HEXDUMP\_WRN(\_data, \_length, \_str)

64#define NET\_HEXDUMP\_INFO(\_data, \_length, \_str) LOG\_HEXDUMP\_INF(\_data, \_length, \_str)

65

66#define NET\_ASSERT(cond, ...) \_\_ASSERT(cond, "" \_\_VA\_ARGS\_\_)

67

68/\* This needs to be here in order to avoid circular include dependency between

69 \* net\_pkt.h and net\_if.h

70 \*/

71#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

72 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

73#if !defined(NET\_PKT\_DETAIL\_STATS\_COUNT)

74#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

75

76#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

77#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

78#else

79#define NET\_PKT\_DETAIL\_STATS\_COUNT 3

80#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

81

82#else

83#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

84#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL \*/

85

86#endif /\* !NET\_PKT\_DETAIL\_STATS\_COUNT \*/

87#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

88 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

89

91

92struct [net\_buf](structnet__buf.md);

93struct [net\_pkt](structnet__pkt.md);

94struct [net\_context](structnet__context.md);

95struct [net\_if](structnet__if.md);

96

[ 100](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) {

[ 102](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047),

[ 106](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) [NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f),

[ 108](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3),

109};

110

[ 121](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)int [net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

122

[ 135](group__net__core.md#ga1a1699666716229a59486a51e46044fc)int [net\_send\_data](group__net__core.md#ga1a1699666716229a59486a51e46044fc)(struct [net\_pkt](structnet__pkt.md) \*pkt);

136

138

139/\* Some helper defines for traffic class support \*/

140#if defined(CONFIG\_NET\_TC\_TX\_COUNT) && defined(CONFIG\_NET\_TC\_RX\_COUNT)

141#define NET\_TC\_TX\_COUNT CONFIG\_NET\_TC\_TX\_COUNT

142#define NET\_TC\_RX\_COUNT CONFIG\_NET\_TC\_RX\_COUNT

143

144#if NET\_TC\_TX\_COUNT > NET\_TC\_RX\_COUNT

145#define NET\_TC\_COUNT NET\_TC\_TX\_COUNT

146#else

147#define NET\_TC\_COUNT NET\_TC\_RX\_COUNT

148#endif

149#else /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

150#define NET\_TC\_TX\_COUNT 0

151#define NET\_TC\_RX\_COUNT 0

152#define NET\_TC\_COUNT 0

153#endif /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

154

155/\* @endcond \*/

156

160

161#ifdef \_\_cplusplus

162}

163#endif

164

165#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_ \*/

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

**Definition** net\_core.h:100

[NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)

@ NET\_OK

Packet has been taken care of.

**Definition** net\_core.h:102

[NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)

@ NET\_DROP

Packet must be dropped.

**Definition** net\_core.h:108

[NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)

@ NET\_CONTINUE

Packet has not been touched, other part should decide about its fate.

**Definition** net\_core.h:106

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log.h](log_8h.md)

[net\_timeout.h](net__timeout_8h.md)

Network timer with wrap around.

[stdbool.h](stdbool_8h.md)

[string.h](string_8h.md)

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:205

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_core.h](net__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
