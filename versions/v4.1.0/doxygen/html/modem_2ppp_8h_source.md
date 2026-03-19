---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/modem_2ppp_8h_source.html
original_path: doxygen/html/modem_2ppp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp.h

[Go to the documentation of this file.](modem_2ppp_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/kernel.h](kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/net/net\_if.h](net__if_8h.md)>

10#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

11#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13

14#include <[zephyr/modem/pipe.h](pipe_8h.md)>

15#include <[zephyr/modem/stats.h](modem_2stats_8h.md)>

16

17#ifndef ZEPHYR\_MODEM\_PPP\_

[ 18](modem_2ppp_8h.md#a4c10bd93401ebba9cc89f81a6f9ab6f2)#define ZEPHYR\_MODEM\_PPP\_

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

30

[ 32](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad)typedef void (\*[modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad))(struct [net\_if](structnet__if.md) \*iface);

33

37

38enum modem\_ppp\_receive\_state {

39 /\* Searching for start of frame and header \*/

40 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_SOF = 0,

41 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_FF,

42 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_7D,

43 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_23,

44 /\* Writing bytes to network packet \*/

45 MODEM\_PPP\_RECEIVE\_STATE\_WRITING,

46 /\* Unescaping next byte before writing to network packet \*/

47 MODEM\_PPP\_RECEIVE\_STATE\_UNESCAPING,

48};

49

50enum modem\_ppp\_transmit\_state {

51 /\* Idle \*/

52 MODEM\_PPP\_TRANSMIT\_STATE\_IDLE = 0,

53 /\* Writing header \*/

54 MODEM\_PPP\_TRANSMIT\_STATE\_SOF,

55 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_FF,

56 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_7D,

57 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_23,

58 /\* Writing protocol \*/

59 MODEM\_PPP\_TRANSMIT\_STATE\_PROTOCOL\_HIGH,

60 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_PROTOCOL\_HIGH,

61 MODEM\_PPP\_TRANSMIT\_STATE\_PROTOCOL\_LOW,

62 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_PROTOCOL\_LOW,

63 /\* Writing data \*/

64 MODEM\_PPP\_TRANSMIT\_STATE\_DATA,

65 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_DATA,

66 /\* Writing FCS \*/

67 MODEM\_PPP\_TRANSMIT\_STATE\_FCS\_LOW,

68 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_FCS\_LOW,

69 MODEM\_PPP\_TRANSMIT\_STATE\_FCS\_HIGH,

70 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_FCS\_HIGH,

71 /\* Writing end of frame \*/

72 MODEM\_PPP\_TRANSMIT\_STATE\_EOF,

73};

74

75struct modem\_ppp {

76 /\* Network interface instance is bound to \*/

77 struct net\_if \*iface;

78

79 /\* Hook for PPP L2 network interface initialization \*/

80 [modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad) init\_iface;

81

82 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

83

84 /\* Buffers used for processing partial frames \*/

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*receive\_buf;

86 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit\_buf;

87 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_size;

88

89 /\* Wrapped PPP frames are sent and received through this pipe \*/

90 struct modem\_pipe \*pipe;

91

92 /\* Receive PPP frame state \*/

93 enum modem\_ppp\_receive\_state receive\_state;

94

95 /\* Allocated network packet being created \*/

96 struct net\_pkt \*rx\_pkt;

97

98 /\* Packet being sent \*/

99 enum modem\_ppp\_transmit\_state transmit\_state;

100 struct net\_pkt \*tx\_pkt;

101 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_pkt\_escaped;

102 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx\_pkt\_protocol;

103 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx\_pkt\_fcs;

104

105 /\* Ring buffer used for transmitting partial PPP frame \*/

106 struct ring\_buf transmit\_rb;

107

108 struct k\_fifo tx\_pkt\_fifo;

109

110 /\* Work \*/

111 struct k\_work send\_work;

112 struct k\_work process\_work;

113

114#if defined(CONFIG\_NET\_STATISTICS\_PPP)

115 struct net\_stats\_ppp stats;

116#endif

117

118#if CONFIG\_MODEM\_STATS

119 struct modem\_stats\_buffer receive\_buf\_stats;

120 struct modem\_stats\_buffer transmit\_buf\_stats;

121#endif

122};

123

127

[ 134](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88)int [modem\_ppp\_attach](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88)(struct modem\_ppp \*ppp, struct modem\_pipe \*pipe);

135

[ 142](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b)struct [net\_if](structnet__if.md) \*[modem\_ppp\_get\_iface](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b)(struct modem\_ppp \*ppp);

143

[ 149](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3)void [modem\_ppp\_release](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3)(struct modem\_ppp \*ppp);

150

154

160int modem\_ppp\_init\_internal(const struct [device](structdevice.md) \*dev);

161

165

[ 179](group__modem__ppp.md#ga78bbcfb655ae8009a6abbc8e09dfbcc0)#define MODEM\_PPP\_DEFINE(\_name, \_init\_iface, \_prio, \_mtu, \_buf\_size) \

180 extern const struct ppp\_api modem\_ppp\_ppp\_api; \

181 \

182 static uint8\_t \_CONCAT(\_name, \_receive\_buf)[\_buf\_size]; \

183 static uint8\_t \_CONCAT(\_name, \_transmit\_buf)[\_buf\_size]; \

184 \

185 static struct modem\_ppp \_name = { \

186 .init\_iface = \_init\_iface, \

187 .receive\_buf = \_CONCAT(\_name, \_receive\_buf), \

188 .transmit\_buf = \_CONCAT(\_name, \_transmit\_buf), \

189 .buf\_size = \_buf\_size, \

190 }; \

191 \

192 NET\_DEVICE\_INIT(\_CONCAT(ppp\_net\_dev\_, \_name), "modem\_ppp\_" # \_name, \

193 modem\_ppp\_init\_internal, NULL, &\_name, NULL, \_prio, &modem\_ppp\_ppp\_api, \

194 PPP\_L2, NET\_L2\_GET\_CTX\_TYPE(PPP\_L2), \_mtu)

195

199

200#ifdef \_\_cplusplus

201}

202#endif

203

204#endif /\* ZEPHYR\_MODEM\_PPP\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[modem\_ppp\_attach](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88)

int modem\_ppp\_attach(struct modem\_ppp \*ppp, struct modem\_pipe \*pipe)

Attach pipe to instance and connect.

[modem\_ppp\_get\_iface](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b)

struct net\_if \* modem\_ppp\_get\_iface(struct modem\_ppp \*ppp)

Get network interface modem PPP instance is bound to.

[modem\_ppp\_release](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3)

void modem\_ppp\_release(struct modem\_ppp \*ppp)

Release pipe from instance.

[modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad)

void(\* modem\_ppp\_init\_iface)(struct net\_if \*iface)

L2 network interface init callback.

**Definition** ppp.h:32

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stats.h](modem_2stats_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[pipe.h](pipe_8h.md)

[ring\_buffer.h](ring__buffer_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ppp.h](modem_2ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
