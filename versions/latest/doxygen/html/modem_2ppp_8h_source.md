---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/modem_2ppp_8h_source.html
original_path: doxygen/html/modem_2ppp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/net/net\_if.h](net__if_8h.md)>

10#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

11#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

12#include <[zephyr/sys/atomic.h](atomic_8h.md)>

13

14#include <[zephyr/modem/pipe.h](pipe_8h.md)>

15

16#ifndef ZEPHYR\_MODEM\_PPP\_

[ 17](modem_2ppp_8h.md#a4c10bd93401ebba9cc89f81a6f9ab6f2)#define ZEPHYR\_MODEM\_PPP\_

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

[ 31](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad)typedef void (\*[modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad))(struct [net\_if](structnet__if.md) \*iface);

32

36

37enum modem\_ppp\_receive\_state {

38 /\* Searching for start of frame and header \*/

39 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_SOF = 0,

40 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_FF,

41 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_7D,

42 MODEM\_PPP\_RECEIVE\_STATE\_HDR\_23,

43 /\* Writing bytes to network packet \*/

44 MODEM\_PPP\_RECEIVE\_STATE\_WRITING,

45 /\* Unescaping next byte before writing to network packet \*/

46 MODEM\_PPP\_RECEIVE\_STATE\_UNESCAPING,

47};

48

49enum modem\_ppp\_transmit\_state {

50 /\* Idle \*/

51 MODEM\_PPP\_TRANSMIT\_STATE\_IDLE = 0,

52 /\* Writing header \*/

53 MODEM\_PPP\_TRANSMIT\_STATE\_SOF,

54 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_FF,

55 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_7D,

56 MODEM\_PPP\_TRANSMIT\_STATE\_HDR\_23,

57 /\* Writing protocol \*/

58 MODEM\_PPP\_TRANSMIT\_STATE\_PROTOCOL\_HIGH,

59 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_PROTOCOL\_HIGH,

60 MODEM\_PPP\_TRANSMIT\_STATE\_PROTOCOL\_LOW,

61 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_PROTOCOL\_LOW,

62 /\* Writing data \*/

63 MODEM\_PPP\_TRANSMIT\_STATE\_DATA,

64 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_DATA,

65 /\* Writing FCS \*/

66 MODEM\_PPP\_TRANSMIT\_STATE\_FCS\_LOW,

67 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_FCS\_LOW,

68 MODEM\_PPP\_TRANSMIT\_STATE\_FCS\_HIGH,

69 MODEM\_PPP\_TRANSMIT\_STATE\_ESCAPING\_FCS\_HIGH,

70 /\* Writing end of frame \*/

71 MODEM\_PPP\_TRANSMIT\_STATE\_EOF,

72};

73

74struct modem\_ppp {

75 /\* Network interface instance is bound to \*/

76 struct net\_if \*iface;

77

78 /\* Hook for PPP L2 network interface initialization \*/

79 [modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad) init\_iface;

80

81 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

82

83 /\* Buffers used for processing partial frames \*/

84 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*receive\_buf;

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit\_buf;

86 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_size;

87

88 /\* Wrapped PPP frames are sent and received through this pipe \*/

89 struct modem\_pipe \*pipe;

90

91 /\* Receive PPP frame state \*/

92 enum modem\_ppp\_receive\_state receive\_state;

93

94 /\* Allocated network packet being created \*/

95 struct net\_pkt \*rx\_pkt;

96

97 /\* Packet being sent \*/

98 enum modem\_ppp\_transmit\_state transmit\_state;

99 struct net\_pkt \*tx\_pkt;

100 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_pkt\_escaped;

101 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx\_pkt\_protocol;

102 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx\_pkt\_fcs;

103

104 /\* Ring buffer used for transmitting partial PPP frame \*/

105 struct ring\_buf transmit\_rb;

106

107 struct k\_fifo tx\_pkt\_fifo;

108

109 /\* Work \*/

110 struct k\_work send\_work;

111 struct k\_work process\_work;

112

113#if defined(CONFIG\_NET\_STATISTICS\_PPP)

114 struct net\_stats\_ppp stats;

115#endif

116};

117

121

[ 128](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88)int [modem\_ppp\_attach](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88)(struct modem\_ppp \*ppp, struct modem\_pipe \*pipe);

129

[ 136](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b)struct [net\_if](structnet__if.md) \*[modem\_ppp\_get\_iface](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b)(struct modem\_ppp \*ppp);

137

[ 143](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3)void [modem\_ppp\_release](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3)(struct modem\_ppp \*ppp);

144

148

154int modem\_ppp\_init\_internal(const struct [device](structdevice.md) \*dev);

155

159

[ 173](group__modem__ppp.md#ga78bbcfb655ae8009a6abbc8e09dfbcc0)#define MODEM\_PPP\_DEFINE(\_name, \_init\_iface, \_prio, \_mtu, \_buf\_size) \

174 extern const struct ppp\_api modem\_ppp\_ppp\_api; \

175 \

176 static uint8\_t \_CONCAT(\_name, \_receive\_buf)[\_buf\_size]; \

177 static uint8\_t \_CONCAT(\_name, \_transmit\_buf)[\_buf\_size]; \

178 \

179 static struct modem\_ppp \_name = { \

180 .init\_iface = \_init\_iface, \

181 .receive\_buf = \_CONCAT(\_name, \_receive\_buf), \

182 .transmit\_buf = \_CONCAT(\_name, \_transmit\_buf), \

183 .buf\_size = \_buf\_size, \

184 }; \

185 \

186 NET\_DEVICE\_INIT(\_CONCAT(ppp\_net\_dev\_, \_name), "modem\_ppp\_" # \_name, \

187 modem\_ppp\_init\_internal, NULL, &\_name, NULL, \_prio, &modem\_ppp\_ppp\_api, \

188 PPP\_L2, NET\_L2\_GET\_CTX\_TYPE(PPP\_L2), \_mtu)

189

193

194#ifdef \_\_cplusplus

195}

196#endif

197

198#endif /\* ZEPHYR\_MODEM\_PPP\_ \*/

[atomic.h](atomic_8h.md)

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

**Definition** ppp.h:31

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** device.h:387

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ppp.h](modem_2ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
