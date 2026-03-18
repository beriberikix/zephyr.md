---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ptp__time_8h_source.html
original_path: doxygen/html/ptp__time_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24

25#include <[zephyr/net/net\_core.h](net__core_8h.md)>

26#include <[zephyr/net/net\_time.h](net__time_8h.md)>

27#include <[zephyr/toolchain.h](toolchain_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 109](structnet__ptp__time.md)struct [net\_ptp\_time](structnet__ptp__time.md) {

111 union {

112 struct {

113#ifdef CONFIG\_LITTLE\_ENDIAN

114 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__time.md#a99751ad079c5f2652a5c4121a0d108bf);

115 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__time.md#a011cafdfcc04757e0bc3b84642d7dde6);

116 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__time.md#a91cf8ed8438c4ad54ac0d65a9cd88802);

117#else

[ 118](structnet__ptp__time.md#a91cf8ed8438c4ad54ac0d65a9cd88802) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__time.md#a91cf8ed8438c4ad54ac0d65a9cd88802);

[ 119](structnet__ptp__time.md#a011cafdfcc04757e0bc3b84642d7dde6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__time.md#a011cafdfcc04757e0bc3b84642d7dde6);

[ 120](structnet__ptp__time.md#a99751ad079c5f2652a5c4121a0d108bf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__time.md#a99751ad079c5f2652a5c4121a0d108bf);

121#endif

122 } \_sec;

[ 123](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

124 };

125

[ 127](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

128};

129

130#ifdef \_\_cplusplus

131}

132#endif

133

[ 147](structnet__ptp__extended__time.md)struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) {

149 union {

150 struct {

151#ifdef CONFIG\_LITTLE\_ENDIAN

152 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d);

153 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce);

154 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115);

155#else

[ 156](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115);

[ 157](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce);

[ 158](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d);

159#endif

160 } \_sec;

[ 161](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [second](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55);

162 };

163

165 union {

166 struct {

167#ifdef CONFIG\_LITTLE\_ENDIAN

168 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d);

169 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce);

170 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115);

171#else

172 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unused](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115);

173 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [high](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce);

174 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d);

175#endif

176 } \_fns;

[ 177](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [fract\_nsecond](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587);

178 };

179} \_\_packed;

180

[ 193](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(struct [net\_ptp\_time](structnet__ptp__time.md) \*ts)

194{

195 if (!ts) {

196 return 0;

197 }

198

199 if (ts->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) >= [NET\_TIME\_SEC\_MAX](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)) {

200 return [NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199);

201 }

202

203 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ts->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) \* [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) + ts->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

204}

205

[ 214](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)static inline struct [net\_ptp\_time](structnet__ptp__time.md) [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)([net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) nsec)

215{

216 struct [net\_ptp\_time](structnet__ptp__time.md) ts;

217

218 \_\_ASSERT\_NO\_MSG(nsec >= 0);

219

220 ts.[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04) = nsec / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

221 ts.[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e) = nsec % [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

222 return ts;

223}

224

228

229#endif /\* ZEPHYR\_INCLUDE\_NET\_PTP\_TIME\_H\_ \*/

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:107

[NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199)

#define NET\_TIME\_MAX

The largest positive time value that can be represented by net\_time\_t.

**Definition** net\_time.h:104

[NET\_TIME\_SEC\_MAX](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)

#define NET\_TIME\_SEC\_MAX

The largest positive number of seconds that can be safely represented by net\_time\_t.

**Definition** net\_time.h:110

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:101

[net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)

static net\_time\_t net\_ptp\_time\_to\_ns(struct net\_ptp\_time \*ts)

Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network refere...

**Definition** ptp\_time.h:193

[ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)

static struct net\_ptp\_time ns\_to\_net\_ptp\_time(net\_time\_t nsec)

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network refere...

**Definition** ptp\_time.h:214

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

**Definition** ptp\_time.h:147

[net\_ptp\_extended\_time::unused](structnet__ptp__extended__time.md#a20379af8395fe3afc1f6f9c45b711115)

uint16\_t unused

**Definition** ptp\_time.h:156

[net\_ptp\_extended\_time::high](structnet__ptp__extended__time.md#a3b4b8dcfa8e6aab5dd0e7ef26ad129ce)

uint16\_t high

**Definition** ptp\_time.h:157

[net\_ptp\_extended\_time::fract\_nsecond](structnet__ptp__extended__time.md#a94ec079b5d38fcd12ec54baf707ec587)

uint64\_t fract\_nsecond

**Definition** ptp\_time.h:177

[net\_ptp\_extended\_time::second](structnet__ptp__extended__time.md#a97b1711e17fa229bab129da4148c3e55)

uint64\_t second

**Definition** ptp\_time.h:161

[net\_ptp\_extended\_time::low](structnet__ptp__extended__time.md#a9fa067e7bb793c0eda1f30cba570a15d)

uint32\_t low

**Definition** ptp\_time.h:158

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:109

[net\_ptp\_time::high](structnet__ptp__time.md#a011cafdfcc04757e0bc3b84642d7dde6)

uint16\_t high

**Definition** ptp\_time.h:119

[net\_ptp\_time::nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e)

uint32\_t nanosecond

Nanoseconds.

**Definition** ptp\_time.h:127

[net\_ptp\_time::second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04)

uint64\_t second

**Definition** ptp\_time.h:123

[net\_ptp\_time::unused](structnet__ptp__time.md#a91cf8ed8438c4ad54ac0d65a9cd88802)

uint16\_t unused

**Definition** ptp\_time.h:118

[net\_ptp\_time::low](structnet__ptp__time.md#a99751ad079c5f2652a5c4121a0d108bf)

uint32\_t low

**Definition** ptp\_time.h:120

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ptp\_time.h](ptp__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
