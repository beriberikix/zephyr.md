---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/can__sja1000_8h_source.html
original_path: doxygen/html/can__sja1000_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_sja1000.h

[Go to the documentation of this file.](can__sja1000_8h.md)

1/\*

2 \* Copyright (c) 2022 Henrik Brix Andersen <henrik@brixandersen.dk>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_SJA1000\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_SJA1000\_H\_

14

15#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

16

[ 22](can__sja1000_8h.md#aa7c14df170465c5a86eab75170f9196a)#define CAN\_SJA1000\_OCR\_OCMODE\_MASK GENMASK(1, 0)

[ 23](can__sja1000_8h.md#adbaaa75df320478924377688a677d872)#define CAN\_SJA1000\_OCR\_OCPOL0 BIT(2)

[ 24](can__sja1000_8h.md#aa931c0fc46923cab133022c4639a9918)#define CAN\_SJA1000\_OCR\_OCTN0 BIT(3)

[ 25](can__sja1000_8h.md#a80684f0201ebb730fc14410e84e96df2)#define CAN\_SJA1000\_OCR\_OCTP0 BIT(4)

[ 26](can__sja1000_8h.md#a983df1be96b35bd9e49c3c579d0cb40b)#define CAN\_SJA1000\_OCR\_OCPOL1 BIT(5)

[ 27](can__sja1000_8h.md#a1c2af47c7bcaf0dd4c98f2185c8548b4)#define CAN\_SJA1000\_OCR\_OCTN1 BIT(6)

[ 28](can__sja1000_8h.md#a838dfca73332736247f77c5116c93c45)#define CAN\_SJA1000\_OCR\_OCTP1 BIT(7)

29

[ 30](can__sja1000_8h.md#a48aa18105fe36f1cf4db8b1a5a4c0ec0)#define CAN\_SJA1000\_OCR\_OCMODE\_BIPHASE FIELD\_PREP(CAN\_SJA1000\_OCR\_OCMODE\_MASK, 0U)

[ 31](can__sja1000_8h.md#a6a59fcd698e2a066ada853b09a0b71fa)#define CAN\_SJA1000\_OCR\_OCMODE\_TEST FIELD\_PREP(CAN\_SJA1000\_OCR\_OCMODE\_MASK, 1U)

[ 32](can__sja1000_8h.md#aab6b947d5201325b3293c26418733ed0)#define CAN\_SJA1000\_OCR\_OCMODE\_NORMAL FIELD\_PREP(CAN\_SJA1000\_OCR\_OCMODE\_MASK, 2U)

[ 33](can__sja1000_8h.md#a00c2a29b797bf50ba4addb5b684cec7d)#define CAN\_SJA1000\_OCR\_OCMODE\_CLOCK FIELD\_PREP(CAN\_SJA1000\_OCR\_OCMODE\_MASK, 3U)

34

36

[ 42](can__sja1000_8h.md#a86033d45850acb3b5984a257ecb935ad)#define CAN\_SJA1000\_CDR\_CD\_MASK GENMASK(2, 0)

[ 43](can__sja1000_8h.md#af8eb9626285ac4ad3a917b84731669fb)#define CAN\_SJA1000\_CDR\_CLOCK\_OFF BIT(3)

[ 44](can__sja1000_8h.md#a5f35936e647d82aab0240e8f1628070f)#define CAN\_SJA1000\_CDR\_RXINTEN BIT(5)

[ 45](can__sja1000_8h.md#a9073e03d7173af238b28efb819969f6f)#define CAN\_SJA1000\_CDR\_CBP BIT(6)

[ 46](can__sja1000_8h.md#a3929d82be73cc8d8010867fd5a0f3ad7)#define CAN\_SJA1000\_CDR\_CAN\_MODE BIT(7)

47

[ 48](can__sja1000_8h.md#af581ccabd33280a269fe4420d5be0635)#define CAN\_SJA1000\_CDR\_CD\_DIV1 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 7U)

[ 49](can__sja1000_8h.md#aa744e2ade8c6dd6a93556039ba77dc06)#define CAN\_SJA1000\_CDR\_CD\_DIV2 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 0U)

[ 50](can__sja1000_8h.md#a6db863734edfd04eb36ca83f22802b56)#define CAN\_SJA1000\_CDR\_CD\_DIV4 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 1U)

[ 51](can__sja1000_8h.md#a038f3f02a964491b8a2f6e6bec1b09c6)#define CAN\_SJA1000\_CDR\_CD\_DIV6 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 2U)

[ 52](can__sja1000_8h.md#a8b3eccd70614f1c23db969935505fba5)#define CAN\_SJA1000\_CDR\_CD\_DIV8 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 3U)

[ 53](can__sja1000_8h.md#ae09ac444faeb0edd9e5d0889e33e5037)#define CAN\_SJA1000\_CDR\_CD\_DIV10 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 4U)

[ 54](can__sja1000_8h.md#a4bc39dfcd67d59b360015b5d4819d4ae)#define CAN\_SJA1000\_CDR\_CD\_DIV12 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 5U)

[ 55](can__sja1000_8h.md#a326fd4317bce6a3b82d1ed57fd4fc1bf)#define CAN\_SJA1000\_CDR\_CD\_DIV14 FIELD\_PREP(CAN\_SJA1000\_CDR\_CD\_MASK, 6U)

56

58

[ 62](can__sja1000_8h.md#ad396485923ad20b9662e56ae10128e4c)#define CAN\_SJA1000\_TIMING\_MIN\_INITIALIZER \

63 { \

64 .sjw = 1, \

65 .prop\_seg = 0, \

66 .phase\_seg1 = 1, \

67 .phase\_seg2 = 1, \

68 .prescaler = 1 \

69 }

70

[ 74](can__sja1000_8h.md#a245230e39b3f9eca9f1a76a1926606ab)#define CAN\_SJA1000\_TIMING\_MAX\_INITIALIZER \

75 { \

76 .sjw = 4, \

77 .prop\_seg = 0, \

78 .phase\_seg1 = 16, \

79 .phase\_seg2 = 8, \

80 .prescaler = 64 \

81 }

82

[ 90](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb)typedef void (\*[can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

91

[ 99](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg);

100

[ 104](structcan__sja1000__config.md)struct [can\_sja1000\_config](structcan__sja1000__config.md) {

[ 105](structcan__sja1000__config.md#a5f6b844c34defd6d63149629843e9dbb) const struct can\_driver\_config [common](structcan__sja1000__config.md#a5f6b844c34defd6d63149629843e9dbb);

[ 106](structcan__sja1000__config.md#a7db8fc3fbb3dfdb95d6f4d5999ec5646) [can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341) [read\_reg](structcan__sja1000__config.md#a7db8fc3fbb3dfdb95d6f4d5999ec5646);

[ 107](structcan__sja1000__config.md#ab7a864dc361c9b4a9b5917df7566c403) [can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb) [write\_reg](structcan__sja1000__config.md#ab7a864dc361c9b4a9b5917df7566c403);

[ 108](structcan__sja1000__config.md#a7949f91e0d855d701771ff4f59669b42) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ocr](structcan__sja1000__config.md#a7949f91e0d855d701771ff4f59669b42);

[ 109](structcan__sja1000__config.md#a66f62e4f7efadf3b0454173e3795886d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cdr](structcan__sja1000__config.md#a66f62e4f7efadf3b0454173e3795886d);

[ 110](structcan__sja1000__config.md#a31b21d7556a6c7d176cc955029310400) const void \*[custom](structcan__sja1000__config.md#a31b21d7556a6c7d176cc955029310400);

111};

112

[ 124](can__sja1000_8h.md#a3eda68391dfee872be4b49319d0b7437)#define CAN\_SJA1000\_DT\_CONFIG\_GET(node\_id, \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \

125 \_min\_bitrate) \

126 { \

127 .common = CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, \_min\_bitrate, 1000000), \

128 .read\_reg = \_read\_reg, \

129 .write\_reg = \_write\_reg, \

130 .ocr = \_ocr, \

131 .cdr = \_cdr, \

132 .custom = \_custom, \

133 }

134

[ 147](can__sja1000_8h.md#adf7ef5e56f8acbf0a63ca7e912976d15)#define CAN\_SJA1000\_DT\_CONFIG\_INST\_GET(inst, \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \

148 \_min\_bitrate) \

149 CAN\_SJA1000\_DT\_CONFIG\_GET(DT\_DRV\_INST(inst), \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \

150 \_min\_bitrate)

151

[ 155](structcan__sja1000__rx__filter.md)struct [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md) {

[ 156](structcan__sja1000__rx__filter.md#aee19675d5cc25ed7adec2bff84b347e5) struct [can\_filter](structcan__filter.md) [filter](structcan__sja1000__rx__filter.md#aee19675d5cc25ed7adec2bff84b347e5);

[ 157](structcan__sja1000__rx__filter.md#a7f312ad2aa06e836928da30ea012d797) [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) [callback](structcan__sja1000__rx__filter.md#a7f312ad2aa06e836928da30ea012d797);

[ 158](structcan__sja1000__rx__filter.md#addc5b07b6aa6a144ae0d2e792523f4df) void \*[user\_data](structcan__sja1000__rx__filter.md#addc5b07b6aa6a144ae0d2e792523f4df);

159};

160

[ 164](structcan__sja1000__data.md)struct [can\_sja1000\_data](structcan__sja1000__data.md) {

[ 165](structcan__sja1000__data.md#aa31ac266b0f4f976bc346fb87e62c1dc) struct can\_driver\_data [common](structcan__sja1000__data.md#aa31ac266b0f4f976bc346fb87e62c1dc);

[ 166](structcan__sja1000__data.md#afde535cdca9611a264e3feefe3f4c180) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([rx\_allocs](structcan__sja1000__data.md#afde535cdca9611a264e3feefe3f4c180), CONFIG\_CAN\_MAX\_FILTER);

[ 167](structcan__sja1000__data.md#ab4510fe2232bcea825e68777640d182d) struct [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md) [filters](structcan__sja1000__data.md#ab4510fe2232bcea825e68777640d182d)[CONFIG\_CAN\_MAX\_FILTER];

[ 168](structcan__sja1000__data.md#adc707a2852492ff0859e08976986e191) struct [k\_mutex](structk__mutex.md) [mod\_lock](structcan__sja1000__data.md#adc707a2852492ff0859e08976986e191);

[ 169](structcan__sja1000__data.md#ab2e365eb95f4440db7c42f6f6c9999a0) enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) [state](structcan__sja1000__data.md#ab2e365eb95f4440db7c42f6f6c9999a0);

[ 170](structcan__sja1000__data.md#a8152989a4408268abdb35688bfcfd02b) struct k\_sem [tx\_idle](structcan__sja1000__data.md#a8152989a4408268abdb35688bfcfd02b);

[ 171](structcan__sja1000__data.md#a3ee972b9dfd1aa226159ad3c5cf41210) [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) [tx\_callback](structcan__sja1000__data.md#a3ee972b9dfd1aa226159ad3c5cf41210);

[ 172](structcan__sja1000__data.md#ab61c31be1a91696bceb65bab188356a1) void \*[tx\_user\_data](structcan__sja1000__data.md#ab61c31be1a91696bceb65bab188356a1);

[ 173](structcan__sja1000__data.md#a2c6e39433b4d07423635cb73dd7a37e6) void \*[custom](structcan__sja1000__data.md#a2c6e39433b4d07423635cb73dd7a37e6);

174};

175

[ 180](can__sja1000_8h.md#a21aae4f3884e9737b15050fbe55d9bea)#define CAN\_SJA1000\_DATA\_INITIALIZER(\_custom) \

181 { \

182 .custom = \_custom, \

183 }

184

[ 189](can__sja1000_8h.md#a8b36e7b0defa598d4ebcd5997e714209)int [can\_sja1000\_set\_timing](can__sja1000_8h.md#a8b36e7b0defa598d4ebcd5997e714209)(const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing);

190

[ 195](can__sja1000_8h.md#a867ba15d4e2d94800d902b97db1e0482)int [can\_sja1000\_get\_capabilities](can__sja1000_8h.md#a867ba15d4e2d94800d902b97db1e0482)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

196

[ 201](can__sja1000_8h.md#ad5f343d57184fa3adf7d248fe49e97d3)int [can\_sja1000\_start](can__sja1000_8h.md#ad5f343d57184fa3adf7d248fe49e97d3)(const struct [device](structdevice.md) \*dev);

202

[ 207](can__sja1000_8h.md#a90d251f5a048f2688b111e6a4f8165fb)int [can\_sja1000\_stop](can__sja1000_8h.md#a90d251f5a048f2688b111e6a4f8165fb)(const struct [device](structdevice.md) \*dev);

208

[ 213](can__sja1000_8h.md#aee809bd3edef0fd08eaad6ef9270f5cc)int [can\_sja1000\_set\_mode](can__sja1000_8h.md#aee809bd3edef0fd08eaad6ef9270f5cc)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

214

[ 219](can__sja1000_8h.md#ab050fab94165f1ab532f8a4a9ca0748c)int [can\_sja1000\_send](can__sja1000_8h.md#ab050fab94165f1ab532f8a4a9ca0748c)(const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout,

220 [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data);

221

[ 226](can__sja1000_8h.md#a5c7c6edb274a773fd863fac96412fa0d)int [can\_sja1000\_add\_rx\_filter](can__sja1000_8h.md#a5c7c6edb274a773fd863fac96412fa0d)(const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data,

227 const struct [can\_filter](structcan__filter.md) \*filter);

228

[ 233](can__sja1000_8h.md#a5b436ad6663d3dddb7f28ec03b520b25)void [can\_sja1000\_remove\_rx\_filter](can__sja1000_8h.md#a5b436ad6663d3dddb7f28ec03b520b25)(const struct [device](structdevice.md) \*dev, int filter\_id);

234

235#ifdef CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE

240int can\_sja1000\_recover(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

241#endif /\* CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE \*/

242

[ 247](can__sja1000_8h.md#a939a87f8181236c5dbe18ba7865c1b4b)int [can\_sja1000\_get\_state](can__sja1000_8h.md#a939a87f8181236c5dbe18ba7865c1b4b)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

248 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

249

[ 254](can__sja1000_8h.md#a34df509dde4faa3ee45e6e5e0b42649e)void [can\_sja1000\_set\_state\_change\_callback](can__sja1000_8h.md#a34df509dde4faa3ee45e6e5e0b42649e)(const struct [device](structdevice.md) \*dev,

255 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data);

256

[ 261](can__sja1000_8h.md#a19ee7bbdee6b66b2b2ed5071ac881403)int [can\_sja1000\_get\_max\_filters](can__sja1000_8h.md#a19ee7bbdee6b66b2b2ed5071ac881403)(const struct [device](structdevice.md) \*dev, bool ide);

262

[ 268](can__sja1000_8h.md#a65df5350d4191fa93f7ea8054d6139c3)void [can\_sja1000\_isr](can__sja1000_8h.md#a65df5350d4191fa93f7ea8054d6139c3)(const struct [device](structdevice.md) \*dev);

269

[ 275](can__sja1000_8h.md#a5150ea6d32a3d111e5b130b60f63eb82)int [can\_sja1000\_init](can__sja1000_8h.md#a5150ea6d32a3d111e5b130b60f63eb82)(const struct [device](structdevice.md) \*dev);

276

277#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_SJA1000\_H\_ \*/

[can\_sja1000\_get\_max\_filters](can__sja1000_8h.md#a19ee7bbdee6b66b2b2ed5071ac881403)

int can\_sja1000\_get\_max\_filters(const struct device \*dev, bool ide)

SJA1000 callback API upon getting the maximum number of concurrent CAN RX filters See can\_get\_max\_fil...

[can\_sja1000\_set\_state\_change\_callback](can__sja1000_8h.md#a34df509dde4faa3ee45e6e5e0b42649e)

void can\_sja1000\_set\_state\_change\_callback(const struct device \*dev, can\_state\_change\_callback\_t callback, void \*user\_data)

SJA1000 callback API upon setting a state change callback See can\_set\_state\_change\_callback() for arg...

[can\_sja1000\_init](can__sja1000_8h.md#a5150ea6d32a3d111e5b130b60f63eb82)

int can\_sja1000\_init(const struct device \*dev)

SJA1000 driver initialization callback.

[can\_sja1000\_remove\_rx\_filter](can__sja1000_8h.md#a5b436ad6663d3dddb7f28ec03b520b25)

void can\_sja1000\_remove\_rx\_filter(const struct device \*dev, int filter\_id)

SJA1000 callback API upon removing an RX filter See can\_remove\_rx\_filter() for argument description.

[can\_sja1000\_add\_rx\_filter](can__sja1000_8h.md#a5c7c6edb274a773fd863fac96412fa0d)

int can\_sja1000\_add\_rx\_filter(const struct device \*dev, can\_rx\_callback\_t callback, void \*user\_data, const struct can\_filter \*filter)

SJA1000 callback API upon adding an RX filter See can\_add\_rx\_callback() for argument description.

[can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341)

uint8\_t(\* can\_sja1000\_read\_reg\_t)(const struct device \*dev, uint8\_t reg)

SJA1000 driver front-end callback for reading a register value.

**Definition** can\_sja1000.h:99

[can\_sja1000\_isr](can__sja1000_8h.md#a65df5350d4191fa93f7ea8054d6139c3)

void can\_sja1000\_isr(const struct device \*dev)

SJA1000 IRQ handler callback.

[can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb)

void(\* can\_sja1000\_write\_reg\_t)(const struct device \*dev, uint8\_t reg, uint8\_t val)

SJA1000 driver front-end callback for writing a register value.

**Definition** can\_sja1000.h:90

[can\_sja1000\_get\_capabilities](can__sja1000_8h.md#a867ba15d4e2d94800d902b97db1e0482)

int can\_sja1000\_get\_capabilities(const struct device \*dev, can\_mode\_t \*cap)

SJA1000 callback API upon getting CAN controller capabilities See can\_get\_capabilities() for argument...

[can\_sja1000\_set\_timing](can__sja1000_8h.md#a8b36e7b0defa598d4ebcd5997e714209)

int can\_sja1000\_set\_timing(const struct device \*dev, const struct can\_timing \*timing)

SJA1000 callback API upon setting CAN bus timing See can\_set\_timing() for argument description.

[can\_sja1000\_stop](can__sja1000_8h.md#a90d251f5a048f2688b111e6a4f8165fb)

int can\_sja1000\_stop(const struct device \*dev)

SJA1000 callback API upon stopping CAN controller See can\_stop() for argument description.

[can\_sja1000\_get\_state](can__sja1000_8h.md#a939a87f8181236c5dbe18ba7865c1b4b)

int can\_sja1000\_get\_state(const struct device \*dev, enum can\_state \*state, struct can\_bus\_err\_cnt \*err\_cnt)

SJA1000 callback API upon getting the CAN controller state See can\_get\_state() for argument descripti...

[can\_sja1000\_send](can__sja1000_8h.md#ab050fab94165f1ab532f8a4a9ca0748c)

int can\_sja1000\_send(const struct device \*dev, const struct can\_frame \*frame, k\_timeout\_t timeout, can\_tx\_callback\_t callback, void \*user\_data)

SJA1000 callback API upon sending a CAN frame See can\_send() for argument description.

[can\_sja1000\_start](can__sja1000_8h.md#ad5f343d57184fa3adf7d248fe49e97d3)

int can\_sja1000\_start(const struct device \*dev)

SJA1000 callback API upon starting CAN controller See can\_start() for argument description.

[can\_sja1000\_set\_mode](can__sja1000_8h.md#aee809bd3edef0fd08eaad6ef9270f5cc)

int can\_sja1000\_set\_mode(const struct device \*dev, can\_mode\_t mode)

SJA1000 callback API upon setting CAN controller mode See can\_set\_mode() for argument description.

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:312

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:125

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:301

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:292

[can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)

can\_state

Defines the state of the CAN controller.

**Definition** can.h:130

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[can\_bus\_err\_cnt](structcan__bus__err__cnt.md)

CAN controller error counters.

**Definition** can.h:232

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:218

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:172

[can\_sja1000\_config](structcan__sja1000__config.md)

SJA1000 driver internal configuration structure.

**Definition** can\_sja1000.h:104

[can\_sja1000\_config::custom](structcan__sja1000__config.md#a31b21d7556a6c7d176cc955029310400)

const void \* custom

**Definition** can\_sja1000.h:110

[can\_sja1000\_config::common](structcan__sja1000__config.md#a5f6b844c34defd6d63149629843e9dbb)

const struct can\_driver\_config common

**Definition** can\_sja1000.h:105

[can\_sja1000\_config::cdr](structcan__sja1000__config.md#a66f62e4f7efadf3b0454173e3795886d)

uint8\_t cdr

**Definition** can\_sja1000.h:109

[can\_sja1000\_config::ocr](structcan__sja1000__config.md#a7949f91e0d855d701771ff4f59669b42)

uint8\_t ocr

**Definition** can\_sja1000.h:108

[can\_sja1000\_config::read\_reg](structcan__sja1000__config.md#a7db8fc3fbb3dfdb95d6f4d5999ec5646)

can\_sja1000\_read\_reg\_t read\_reg

**Definition** can\_sja1000.h:106

[can\_sja1000\_config::write\_reg](structcan__sja1000__config.md#ab7a864dc361c9b4a9b5917df7566c403)

can\_sja1000\_write\_reg\_t write\_reg

**Definition** can\_sja1000.h:107

[can\_sja1000\_data](structcan__sja1000__data.md)

SJA1000 driver internal data structure.

**Definition** can\_sja1000.h:164

[can\_sja1000\_data::custom](structcan__sja1000__data.md#a2c6e39433b4d07423635cb73dd7a37e6)

void \* custom

**Definition** can\_sja1000.h:173

[can\_sja1000\_data::tx\_callback](structcan__sja1000__data.md#a3ee972b9dfd1aa226159ad3c5cf41210)

can\_tx\_callback\_t tx\_callback

**Definition** can\_sja1000.h:171

[can\_sja1000\_data::tx\_idle](structcan__sja1000__data.md#a8152989a4408268abdb35688bfcfd02b)

struct k\_sem tx\_idle

**Definition** can\_sja1000.h:170

[can\_sja1000\_data::common](structcan__sja1000__data.md#aa31ac266b0f4f976bc346fb87e62c1dc)

struct can\_driver\_data common

**Definition** can\_sja1000.h:165

[can\_sja1000\_data::state](structcan__sja1000__data.md#ab2e365eb95f4440db7c42f6f6c9999a0)

enum can\_state state

**Definition** can\_sja1000.h:169

[can\_sja1000\_data::filters](structcan__sja1000__data.md#ab4510fe2232bcea825e68777640d182d)

struct can\_sja1000\_rx\_filter filters[CONFIG\_CAN\_MAX\_FILTER]

**Definition** can\_sja1000.h:167

[can\_sja1000\_data::tx\_user\_data](structcan__sja1000__data.md#ab61c31be1a91696bceb65bab188356a1)

void \* tx\_user\_data

**Definition** can\_sja1000.h:172

[can\_sja1000\_data::mod\_lock](structcan__sja1000__data.md#adc707a2852492ff0859e08976986e191)

struct k\_mutex mod\_lock

**Definition** can\_sja1000.h:168

[can\_sja1000\_data::rx\_allocs](structcan__sja1000__data.md#afde535cdca9611a264e3feefe3f4c180)

atomic\_t rx\_allocs[ATOMIC\_BITMAP\_SIZE(CONFIG\_CAN\_MAX\_FILTER)]

**Definition** can\_sja1000.h:166

[can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md)

SJA1000 driver internal RX filter structure.

**Definition** can\_sja1000.h:155

[can\_sja1000\_rx\_filter::callback](structcan__sja1000__rx__filter.md#a7f312ad2aa06e836928da30ea012d797)

can\_rx\_callback\_t callback

**Definition** can\_sja1000.h:157

[can\_sja1000\_rx\_filter::user\_data](structcan__sja1000__rx__filter.md#addc5b07b6aa6a144ae0d2e792523f4df)

void \* user\_data

**Definition** can\_sja1000.h:158

[can\_sja1000\_rx\_filter::filter](structcan__sja1000__rx__filter.md#aee19675d5cc25ed7adec2bff84b347e5)

struct can\_filter filter

**Definition** can\_sja1000.h:156

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:271

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_sja1000.h](can__sja1000_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
