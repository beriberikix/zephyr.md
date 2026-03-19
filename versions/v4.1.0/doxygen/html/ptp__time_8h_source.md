---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ptp__time_8h_source.html
original_path: doxygen/html/ptp__time_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp\_time.h

[Go to the documentation of this file.](ptp__time_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_PTP\_TIME\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_PTP\_TIME\_H\_

17

26

27#include <[zephyr/net/net\_core.h](net__core_8h.md)>

28#include <[zephyr/net/net\_time.h](net__time_8h.md)>

29#include <[zephyr/toolchain.h](toolchain_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 111](structnet__ptp__time.md)struct [net\_ptp\_time](structnet__ptp__time.md) {

113 union {

114

116 struct {

117#ifdef CONFIG\_LITTLE\_ENDIAN

118 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

119 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

120 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

121#else

122 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

123 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

124 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

125#endif

126 } \_sec;

128

[ 130](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

131 };

132

[ 134](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

135};

136

137#ifdef \_\_cplusplus

138}

139#endif

140

[ 154](structnet__ptp__extended__time.md)struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) {

156 union {

157

159 struct {

160#ifdef CONFIG\_LITTLE\_ENDIAN

161 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

162 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

163 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

164#else

165 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

166 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

167 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

168#endif

169 } \_sec;

171

[ 173](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [second](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55);

174 };

175

177 union {

178

180 struct {

181#ifdef CONFIG\_LITTLE\_ENDIAN

182 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

183 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

184 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

185#else

186 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unused;

187 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) high;

188 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) low;

189#endif

190 } \_fns;

192

[ 194](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [fract\_nsecond](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587);

195 };

196} \_\_packed;

197

[ 210](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(struct [net\_ptp\_time](structnet__ptp__time.md) \*ts)

211{

212 if (!ts) {

213 return 0;

214 }

215

216 if (ts->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) >= [NET\_TIME\_SEC\_MAX](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)) {

217 return [NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199);

218 }

219

220 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ts->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) \* [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) + ts->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

221}

222

[ 231](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)static inline struct [net\_ptp\_time](structnet__ptp__time.md) [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)([net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) nsec)

232{

233 struct [net\_ptp\_time](structnet__ptp__time.md) ts;

234

235 \_\_ASSERT\_NO\_MSG(nsec >= 0);

236

237 ts.[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) = nsec / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

238 ts.[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e) = nsec % [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

239 return ts;

240}

241

245

246#endif /\* ZEPHYR\_INCLUDE\_NET\_PTP\_TIME\_H\_ \*/

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:113

[NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199)

#define NET\_TIME\_MAX

The largest positive time value that can be represented by net\_time\_t.

**Definition** net\_time.h:106

[NET\_TIME\_SEC\_MAX](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)

#define NET\_TIME\_SEC\_MAX

The largest positive number of seconds that can be safely represented by net\_time\_t.

**Definition** net\_time.h:112

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:103

[net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)

static net\_time\_t net\_ptp\_time\_to\_ns(struct net\_ptp\_time \*ts)

Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network refere...

**Definition** ptp\_time.h:210

[ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)

static struct net\_ptp\_time ns\_to\_net\_ptp\_time(net\_time\_t nsec)

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network refere...

**Definition** ptp\_time.h:231

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_time.h](net__time_8h.md)

Representation of nanosecond resolution elapsed time and timestamps in the network stack.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[net\_ptp\_extended\_time](structnet__ptp__extended__time.md)

Generalized Precision Time Protocol Extended Timestamp format.

**Definition** ptp\_time.h:154

[net\_ptp\_extended\_time::fract\_nsecond](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587)

uint64\_t fract\_nsecond

Fractional nanoseconds value.

**Definition** ptp\_time.h:194

[net\_ptp\_extended\_time::second](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55)

uint64\_t second

Second value.

**Definition** ptp\_time.h:173

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:111

[net\_ptp\_time::nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e)

uint32\_t nanosecond

Nanoseconds.

**Definition** ptp\_time.h:134

[net\_ptp\_time::second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04)

uint64\_t second

Second value.

**Definition** ptp\_time.h:130

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ptp\_time.h](ptp__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
