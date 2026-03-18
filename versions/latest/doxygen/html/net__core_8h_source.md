---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__core_8h_source.html
original_path: doxygen/html/net__core_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22

23#include <[zephyr/net/net\_timeout.h](net__timeout_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

36

43

45

46/\* Network subsystem logging helpers \*/

47#ifdef CONFIG\_THREAD\_NAME

48#define NET\_DBG(fmt, ...) LOG\_DBG("(%s): " fmt, \

49 k\_thread\_name\_get(k\_current\_get()), \

50 ##\_\_VA\_ARGS\_\_)

51#else

52#define NET\_DBG(fmt, ...) LOG\_DBG("(%p): " fmt, k\_current\_get(), \

53 ##\_\_VA\_ARGS\_\_)

54#endif /\* CONFIG\_THREAD\_NAME \*/

55#define NET\_ERR(fmt, ...) LOG\_ERR(fmt, ##\_\_VA\_ARGS\_\_)

56#define NET\_WARN(fmt, ...) LOG\_WRN(fmt, ##\_\_VA\_ARGS\_\_)

57#define NET\_INFO(fmt, ...) LOG\_INF(fmt, ##\_\_VA\_ARGS\_\_)

58

59#define NET\_HEXDUMP\_DBG(\_data, \_length, \_str) LOG\_HEXDUMP\_DBG(\_data, \_length, \_str)

60#define NET\_HEXDUMP\_ERR(\_data, \_length, \_str) LOG\_HEXDUMP\_ERR(\_data, \_length, \_str)

61#define NET\_HEXDUMP\_WARN(\_data, \_length, \_str) LOG\_HEXDUMP\_WRN(\_data, \_length, \_str)

62#define NET\_HEXDUMP\_INFO(\_data, \_length, \_str) LOG\_HEXDUMP\_INF(\_data, \_length, \_str)

63

64#define NET\_ASSERT(cond, ...) \_\_ASSERT(cond, "" \_\_VA\_ARGS\_\_)

65

66/\* This needs to be here in order to avoid circular include dependency between

67 \* net\_pkt.h and net\_if.h

68 \*/

69#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

70 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

71#if !defined(NET\_PKT\_DETAIL\_STATS\_COUNT)

72#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL)

73

74#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

75#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

76#else

77#define NET\_PKT\_DETAIL\_STATS\_COUNT 3

78#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

79

80#else

81#define NET\_PKT\_DETAIL\_STATS\_COUNT 4

82#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL \*/

83

84#endif /\* !NET\_PKT\_DETAIL\_STATS\_COUNT \*/

85#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

86 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

87

89

90struct [net\_buf](structnet__buf.md);

91struct [net\_pkt](structnet__pkt.md);

92struct [net\_context](structnet__context.md);

93struct [net\_if](structnet__if.md);

94

[ 98](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) {

[ 100](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047),

[ 104](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) [NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f),

[ 106](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3),

107};

108

[ 119](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)int [net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

120

[ 133](group__net__core.md#ga1a1699666716229a59486a51e46044fc)int [net\_send\_data](group__net__core.md#ga1a1699666716229a59486a51e46044fc)(struct [net\_pkt](structnet__pkt.md) \*pkt);

134

136

137/\* Some helper defines for traffic class support \*/

138#if defined(CONFIG\_NET\_TC\_TX\_COUNT) && defined(CONFIG\_NET\_TC\_RX\_COUNT)

139#define NET\_TC\_TX\_COUNT CONFIG\_NET\_TC\_TX\_COUNT

140#define NET\_TC\_RX\_COUNT CONFIG\_NET\_TC\_RX\_COUNT

141

142#if NET\_TC\_TX\_COUNT > NET\_TC\_RX\_COUNT

143#define NET\_TC\_COUNT NET\_TC\_TX\_COUNT

144#else

145#define NET\_TC\_COUNT NET\_TC\_RX\_COUNT

146#endif

147#else /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

148#define NET\_TC\_TX\_COUNT 0

149#define NET\_TC\_RX\_COUNT 0

150#define NET\_TC\_COUNT 0

151#endif /\* CONFIG\_NET\_TC\_TX\_COUNT && CONFIG\_NET\_TC\_RX\_COUNT \*/

152

153/\* @endcond \*/

154

158

159#ifdef \_\_cplusplus

160}

161#endif

162

163#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CORE\_H\_ \*/

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

**Definition** net\_core.h:98

[NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)

@ NET\_OK

Packet has been taken care of.

**Definition** net\_core.h:100

[NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)

@ NET\_DROP

Packet must be dropped.

**Definition** net\_core.h:106

[NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)

@ NET\_CONTINUE

Packet has not been touched, other part should decide about its fate.

**Definition** net\_core.h:104

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[log.h](log_8h.md)

[net\_timeout.h](net__timeout_8h.md)

Network timer with wrap around.

[stdbool.h](stdbool_8h.md)

[string.h](string_8h.md)

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:201

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_core.h](net__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
