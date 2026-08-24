---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/buf_8h_source.html
original_path: doxygen/html/buf_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

buf.h

[Go to the documentation of this file.](buf_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_

13

20

21#include <stddef.h>

22#include <[stdint.h](stdint_8h.md)>

23

24#include <zephyr/autoconf.h>

25#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

26#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

27#include <[zephyr/net\_buf.h](net__buf_8h.md)>

28#include <[zephyr/sys/util.h](sys_2util_8h.md)>

29#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

30#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

31#include <[zephyr/toolchain.h](toolchain_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 38](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b)enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) {

[ 40](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d) [BT\_BUF\_TYPE\_NONE](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d) = 0,

[ 42](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1) [BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 44](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5) [BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 46](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) [BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 48](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13) [BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 50](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) [BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 52](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e) [BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

53};

54

[ 56](group__bt__buf.md#gaba424dbbb447b1826cbbe715a228744c)enum [bt\_buf\_dir](group__bt__buf.md#gaba424dbbb447b1826cbbe715a228744c) {

[ 58](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77) [BT\_BUF\_IN](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77),

[ 60](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05) [BT\_BUF\_OUT](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05),

61};

62

[ 68](group__bt__buf.md#gae355c6555a1d514332b2d594bcaf416c)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_buf\_type\_to\_h4](group__bt__buf.md#gae355c6555a1d514332b2d594bcaf416c)(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type)

69{

70 switch (type) {

71 case [BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1):

72 return [BT\_HCI\_H4\_CMD](hci__types_8h.md#a524788ee4d21fe9a4625c35e1756bfe9);

73 case [BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13):

74 case [BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091):

75 return [BT\_HCI\_H4\_ACL](hci__types_8h.md#a17386452bbd60c85959296b6539232bd);

76 case [BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e):

77 case [BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e):

78 return [BT\_HCI\_H4\_ISO](hci__types_8h.md#af5e6a53cc7d9619f4ac2ea5bd3256149);

79 case [BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5):

80 return [BT\_HCI\_H4\_EVT](hci__types_8h.md#a783053bc2846063e50755f1590e81ba8);

81 default:

82 \_\_ASSERT\_NO\_MSG(false);

83 return 0;

84 }

85}

86

[ 93](group__bt__buf.md#ga01c7d236ef77e4ba334401c628f582a9)static inline enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) [bt\_buf\_type\_from\_h4](group__bt__buf.md#ga01c7d236ef77e4ba334401c628f582a9)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) h4\_type, enum [bt\_buf\_dir](group__bt__buf.md#gaba424dbbb447b1826cbbe715a228744c) dir)

94{

95 switch (h4\_type) {

96 case [BT\_HCI\_H4\_CMD](hci__types_8h.md#a524788ee4d21fe9a4625c35e1756bfe9):

97 return [BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1);

98 case [BT\_HCI\_H4\_ACL](hci__types_8h.md#a17386452bbd60c85959296b6539232bd):

99 return dir == [BT\_BUF\_OUT](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05) ? [BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091) : [BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13);

100 case [BT\_HCI\_H4\_EVT](hci__types_8h.md#a783053bc2846063e50755f1590e81ba8):

101 return [BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5);

102 case [BT\_HCI\_H4\_ISO](hci__types_8h.md#af5e6a53cc7d9619f4ac2ea5bd3256149):

103 return dir == [BT\_BUF\_OUT](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05) ? [BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e) : [BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e);

104 default:

105 return [BT\_BUF\_TYPE\_NONE](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d);

106 }

107}

108

109/\* Headroom reserved in buffers, primarily for HCI transport encoding purposes \*/

[ 110](group__bt__buf.md#ga41f80f3995e79982f704f832394a6bef)#define BT\_BUF\_RESERVE 1

111

[ 113](group__bt__buf.md#ga9c114a415dc8fc2b84503736b1283468)#define BT\_BUF\_SIZE(size) (BT\_BUF\_RESERVE + (size))

114

[ 116](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)#define BT\_BUF\_ACL\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_ACL\_HDR\_SIZE + (size))

117

[ 119](group__bt__buf.md#ga098d042ed58592d7c2428967928ee478)#define BT\_BUF\_EVT\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_EVT\_HDR\_SIZE + (size))

120

[ 122](group__bt__buf.md#ga9dc9de00be5e8bf673ec60921ea6681b)#define BT\_BUF\_CMD\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_CMD\_HDR\_SIZE + (size))

123

[ 125](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)#define BT\_BUF\_ISO\_SIZE(size) BT\_BUF\_SIZE(BT\_HCI\_ISO\_HDR\_SIZE + \

126 BT\_HCI\_ISO\_SDU\_TS\_HDR\_SIZE + \

127 (size))

128

[ 130](group__bt__buf.md#ga3ad106326ce13d6eb61d0ac16f592003)#define BT\_BUF\_ACL\_RX\_SIZE BT\_BUF\_ACL\_SIZE(CONFIG\_BT\_BUF\_ACL\_RX\_SIZE)

131

[ 133](group__bt__buf.md#gac76caf2a7fce82ba652eab094162ec66)#define BT\_BUF\_EVT\_RX\_SIZE BT\_BUF\_EVT\_SIZE(CONFIG\_BT\_BUF\_EVT\_RX\_SIZE)

134

135#if defined(CONFIG\_BT\_ISO)

136#define BT\_BUF\_ISO\_RX\_SIZE BT\_BUF\_ISO\_SIZE(CONFIG\_BT\_ISO\_RX\_MTU)

137#define BT\_BUF\_ISO\_RX\_COUNT CONFIG\_BT\_ISO\_RX\_BUF\_COUNT

138#else

[ 139](group__bt__buf.md#gae5db5f9f282f9675fe620842e0c50337)#define BT\_BUF\_ISO\_RX\_SIZE 0

[ 140](group__bt__buf.md#gac45f7915fff9516d9d156a42794e8221)#define BT\_BUF\_ISO\_RX\_COUNT 0

141#endif /\* CONFIG\_BT\_ISO \*/

142

143/\* see Core Spec v6.0 vol.4 part E 7.4.5 \*/

[ 144](group__bt__buf.md#ga9a196035ab78158867ce301c698c08e1)#define BT\_BUF\_ACL\_RX\_COUNT\_MAX 65535

145

146#if defined(CONFIG\_BT\_CONN) && defined(CONFIG\_BT\_HCI\_HOST)

147 /\* The host needs more ACL buffers than maximum ACL links. This is because of

148 \* the way we re-assemble ACL packets into L2CAP PDUs.

149 \*

150 \* We keep around the first buffer (that comes from the driver) to do

151 \* re-assembly into, and if all links are re-assembling, there will be no buffer

152 \* available for the HCI driver to allocate from.

153 \*

154 \* TODO: When CONFIG\_BT\_BUF\_ACL\_RX\_COUNT is removed,

155 \* remove the MAX and only keep the 1.

156 \*/

157#define BT\_BUF\_ACL\_RX\_COUNT\_EXTRA CONFIG\_BT\_BUF\_ACL\_RX\_COUNT\_EXTRA

158#define BT\_BUF\_ACL\_RX\_COUNT (MAX(CONFIG\_BT\_BUF\_ACL\_RX\_COUNT, 1) + BT\_BUF\_ACL\_RX\_COUNT\_EXTRA)

159#else

[ 160](group__bt__buf.md#ga2a43657d82801ab838928fd544d93f1f)#define BT\_BUF\_ACL\_RX\_COUNT\_EXTRA 0

[ 161](group__bt__buf.md#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)#define BT\_BUF\_ACL\_RX\_COUNT 0

162#endif /\* CONFIG\_BT\_CONN && CONFIG\_BT\_HCI\_HOST \*/

163

164#if defined(CONFIG\_BT\_BUF\_ACL\_RX\_COUNT) && CONFIG\_BT\_BUF\_ACL\_RX\_COUNT > 0

165#warning "CONFIG\_BT\_BUF\_ACL\_RX\_COUNT is deprecated, see Zephyr 4.1 migration guide"

166#endif /\* CONFIG\_BT\_BUF\_ACL\_RX\_COUNT && CONFIG\_BT\_BUF\_ACL\_RX\_COUNT > 0 \*/

167

168BUILD\_ASSERT([BT\_BUF\_ACL\_RX\_COUNT](group__bt__buf.md#ga1f2226f2fb0a4ea2b215e1c5572ecbf6) <= [BT\_BUF\_ACL\_RX\_COUNT\_MAX](group__bt__buf.md#ga9a196035ab78158867ce301c698c08e1),

169 "Maximum number of ACL RX buffer is 65535, reduce CONFIG\_BT\_BUF\_ACL\_RX\_COUNT\_EXTRA");

170

[ 172](group__bt__buf.md#ga3e16a5f4c0c9c4c9117d972b7043d82b)#define BT\_BUF\_RX\_SIZE (MAX(MAX(BT\_BUF\_ACL\_RX\_SIZE, BT\_BUF\_EVT\_RX\_SIZE), \

173 BT\_BUF\_ISO\_RX\_SIZE))

174

175/\* Controller can generate up to CONFIG\_BT\_BUF\_ACL\_TX\_COUNT number of unique HCI Number of Completed

176 \* Packets events.

177 \*/

178BUILD\_ASSERT(CONFIG\_BT\_BUF\_EVT\_RX\_COUNT > CONFIG\_BT\_BUF\_ACL\_TX\_COUNT,

179 "Increase Event RX buffer count to be greater than ACL TX buffer count");

180

[ 182](group__bt__buf.md#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)#define BT\_BUF\_RX\_COUNT (CONFIG\_BT\_BUF\_EVT\_RX\_COUNT + \

183 MAX(BT\_BUF\_ACL\_RX\_COUNT, BT\_BUF\_ISO\_RX\_COUNT))

184

[ 186](group__bt__buf.md#ga366c2eee5dcc6056430b203d1c020042)#define BT\_BUF\_CMD\_TX\_SIZE BT\_BUF\_CMD\_SIZE(CONFIG\_BT\_BUF\_CMD\_TX\_SIZE)

187

[ 198](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_rx](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout);

199

[ 212](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040)typedef void (\*[bt\_buf\_rx\_freed\_cb\_t](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040))(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type\_mask);

213

[ 219](group__bt__buf.md#gaf946b1bf3706fe74c6d0c9faaaf478f5)void [bt\_buf\_rx\_freed\_cb\_set](group__bt__buf.md#gaf946b1bf3706fe74c6d0c9faaaf478f5)([bt\_buf\_rx\_freed\_cb\_t](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040) cb);

220

[ 232](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_tx](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)(enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type, [k\_timeout\_t](structk__timeout__t.md) timeout,

233 const void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

234

[ 245](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)struct [net\_buf](structnet__buf.md) \*[bt\_buf\_get\_evt](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, bool discardable, [k\_timeout\_t](structk__timeout__t.md) timeout);

246

[ 253](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)static inline void \_\_deprecated [bt\_buf\_set\_type](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)(struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) type)

254{

255 \_\_ASSERT\_NO\_MSG([net\_buf\_headroom](group__net__buf.md#gac9a09897f44e708f920064826aa2f703)(buf) >= 1);

256 [net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)(buf, [bt\_buf\_type\_to\_h4](group__bt__buf.md#gae355c6555a1d514332b2d594bcaf416c)(type));

257}

258

259

[ 267](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)static inline enum [bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b) \_\_deprecated [bt\_buf\_get\_type](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)(struct [net\_buf](structnet__buf.md) \*buf)

268{

269 /\* We have to assume the direction since the H:4 type doesn't tell us

270 \* if the buffer is incoming or outgoing. The common use case of this API is for outgoing

271 \* buffers, so we assume that.

272 \*/

273 return [bt\_buf\_type\_from\_h4](group__bt__buf.md#ga01c7d236ef77e4ba334401c628f582a9)([net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)(buf), [BT\_BUF\_OUT](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05));

274}

275

279

280#ifdef \_\_cplusplus

281}

282#endif

283

284#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BUF\_H\_ \*/

[bt\_buf\_type\_from\_h4](group__bt__buf.md#ga01c7d236ef77e4ba334401c628f582a9)

static enum bt\_buf\_type bt\_buf\_type\_from\_h4(uint8\_t h4\_type, enum bt\_buf\_dir dir)

Convert from H:4 type to bt\_buf\_type.

**Definition** buf.h:93

[BT\_BUF\_ACL\_RX\_COUNT](group__bt__buf.md#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)

#define BT\_BUF\_ACL\_RX\_COUNT

**Definition** buf.h:161

[bt\_buf\_get\_type](group__bt__buf.md#ga2e35f0593e54d28bad62d6b8933f1599)

static enum bt\_buf\_type bt\_buf\_get\_type(struct net\_buf \*buf)

Get the buffer type.

**Definition** buf.h:267

[bt\_buf\_get\_rx](group__bt__buf.md#ga4013cce9637f5aa2742d1f1aaa00e7ee)

struct net\_buf \* bt\_buf\_get\_rx(enum bt\_buf\_type type, k\_timeout\_t timeout)

Allocate a buffer for incoming data.

[bt\_buf\_get\_tx](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700)

struct net\_buf \* bt\_buf\_get\_tx(enum bt\_buf\_type type, k\_timeout\_t timeout, const void \*data, size\_t size)

Allocate a buffer for outgoing data.

[bt\_buf\_get\_evt](group__bt__buf.md#ga7b7a19302881dea458fbd2e9e2309b30)

struct net\_buf \* bt\_buf\_get\_evt(uint8\_t evt, bool discardable, k\_timeout\_t timeout)

Allocate a buffer for an HCI Event.

[BT\_BUF\_ACL\_RX\_COUNT\_MAX](group__bt__buf.md#ga9a196035ab78158867ce301c698c08e1)

#define BT\_BUF\_ACL\_RX\_COUNT\_MAX

**Definition** buf.h:144

[bt\_buf\_dir](group__bt__buf.md#gaba424dbbb447b1826cbbe715a228744c)

bt\_buf\_dir

Direction of HCI packets.

**Definition** buf.h:56

[bt\_buf\_type\_to\_h4](group__bt__buf.md#gae355c6555a1d514332b2d594bcaf416c)

static uint8\_t bt\_buf\_type\_to\_h4(enum bt\_buf\_type type)

Convert from bt\_buf\_type to H:4 type.

**Definition** buf.h:68

[bt\_buf\_set\_type](group__bt__buf.md#gaec645aec3d6fb845f214c07f2a864fec)

static void bt\_buf\_set\_type(struct net\_buf \*buf, enum bt\_buf\_type type)

Set the buffer type.

**Definition** buf.h:253

[bt\_buf\_rx\_freed\_cb\_t](group__bt__buf.md#gaf5c7be1db66cc51c588938fe0b332040)

void(\* bt\_buf\_rx\_freed\_cb\_t)(enum bt\_buf\_type type\_mask)

A callback to notify about freed buffer in the incoming data pool.

**Definition** buf.h:212

[bt\_buf\_rx\_freed\_cb\_set](group__bt__buf.md#gaf946b1bf3706fe74c6d0c9faaaf478f5)

void bt\_buf\_rx\_freed\_cb\_set(bt\_buf\_rx\_freed\_cb\_t cb)

Set the callback to notify about freed buffer in the incoming data pool.

[bt\_buf\_type](group__bt__buf.md#gafe1539a89ba3389d52d010a071620d7b)

bt\_buf\_type

Possible types of buffers passed around the Bluetooth stack in a form of bitmask.

**Definition** buf.h:38

[BT\_BUF\_OUT](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05)

@ BT\_BUF\_OUT

Packet from the host to the controller.

**Definition** buf.h:60

[BT\_BUF\_IN](group__bt__buf.md#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77)

@ BT\_BUF\_IN

Packet from the controller to the host.

**Definition** buf.h:58

[BT\_BUF\_EVT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5)

@ BT\_BUF\_EVT

HCI event.

**Definition** buf.h:44

[BT\_BUF\_TYPE\_NONE](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d)

@ BT\_BUF\_TYPE\_NONE

Unknown/invalid packet type, used for error checking.

**Definition** buf.h:40

[BT\_BUF\_ISO\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e)

@ BT\_BUF\_ISO\_OUT

Outgoing ISO data.

**Definition** buf.h:50

[BT\_BUF\_ACL\_OUT](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091)

@ BT\_BUF\_ACL\_OUT

Outgoing ACL data.

**Definition** buf.h:46

[BT\_BUF\_ISO\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e)

@ BT\_BUF\_ISO\_IN

Incoming ISO data.

**Definition** buf.h:52

[BT\_BUF\_CMD](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)

@ BT\_BUF\_CMD

HCI command.

**Definition** buf.h:42

[BT\_BUF\_ACL\_IN](group__bt__buf.md#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13)

@ BT\_BUF\_ACL\_IN

Incoming ACL data.

**Definition** buf.h:48

[net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)

static uint8\_t net\_buf\_pull\_u8(struct net\_buf \*buf)

Remove a 8-bit value from the beginning of the buffer.

**Definition** net\_buf.h:2258

[net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)

static void net\_buf\_push\_u8(struct net\_buf \*buf, uint8\_t val)

Push 8-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2043

[net\_buf\_headroom](group__net__buf.md#gac9a09897f44e708f920064826aa2f703)

static size\_t net\_buf\_headroom(const struct net\_buf \*buf)

Check buffer headroom.

**Definition** net\_buf.h:2466

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci.h](hci_8h.md)

[hci\_types.h](hci__types_8h.md)

[BT\_HCI\_H4\_ACL](hci__types_8h.md#a17386452bbd60c85959296b6539232bd)

#define BT\_HCI\_H4\_ACL

**Definition** hci\_types.h:31

[BT\_HCI\_H4\_CMD](hci__types_8h.md#a524788ee4d21fe9a4625c35e1756bfe9)

#define BT\_HCI\_H4\_CMD

**Definition** hci\_types.h:30

[BT\_HCI\_H4\_EVT](hci__types_8h.md#a783053bc2846063e50755f1590e81ba8)

#define BT\_HCI\_H4\_EVT

**Definition** hci\_types.h:33

[BT\_HCI\_H4\_ISO](hci__types_8h.md#af5e6a53cc7d9619f4ac2ea5bd3256149)

#define BT\_HCI\_H4\_ISO

**Definition** hci\_types.h:34

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:1032

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_clock.h](sys__clock_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [buf.h](buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
