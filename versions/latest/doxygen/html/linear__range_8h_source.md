---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/linear__range_8h_source.html
original_path: doxygen/html/linear__range_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linear\_range.h

[Go to the documentation of this file.](linear__range_8h.md)

1/\*

2 \* Copyright (C) 2022, Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef INCLUDE\_ZEPHYR\_SYS\_LINEAR\_RANGE\_H\_

7#define INCLUDE\_ZEPHYR\_SYS\_LINEAR\_RANGE\_H\_

8

9#include <[errno.h](errno_8h.md)>

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdlib.h](stdlib_8h.md)>

12

13#include <[zephyr/sys/util.h](util_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

59

[ 61](structlinear__range.md)struct [linear\_range](structlinear__range.md) {

[ 63](structlinear__range.md#a4523369fa49fa1d6aa58f0d2634eb41d) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [min](structlinear__range.md#a4523369fa49fa1d6aa58f0d2634eb41d);

[ 65](structlinear__range.md#a963889c27dd8541f7cd6528ac82401b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [step](structlinear__range.md#a963889c27dd8541f7cd6528ac82401b3);

[ 67](structlinear__range.md#a705275f156fc4bcf5bb111be01aff6ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_idx](structlinear__range.md#a705275f156fc4bcf5bb111be01aff6ef);

[ 69](structlinear__range.md#a84af63957a1b3e829cf1d53fa6342982) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_idx](structlinear__range.md#a84af63957a1b3e829cf1d53fa6342982);

70};

71

[ 80](group__linear__range.md#ga3f936124e81ea46aa5f8dd4d9bde9ece)#define LINEAR\_RANGE\_INIT(\_min, \_step, \_min\_idx, \_max\_idx) \

81 { \

82 .min = (\_min), \

83 .step = (\_step), \

84 .min\_idx = (\_min\_idx), \

85 .max\_idx = (\_max\_idx), \

86 }

87

[ 95](group__linear__range.md#gae02547c7922e5a36c815dc89bc1df128)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [linear\_range\_values\_count](group__linear__range.md#gae02547c7922e5a36c815dc89bc1df128)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

96{

97 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->max\_idx - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx + 1U;

98}

99

[ 108](group__linear__range.md#ga67b24d9d6e7088daf39020c8c02f8d96)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [linear\_range\_group\_values\_count](group__linear__range.md#ga67b24d9d6e7088daf39020c8c02f8d96)(

109 const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), size\_t r\_cnt)

110{

111 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) values = 0U;

112

113 for (size\_t i = 0U; i < r\_cnt; i++) {

114 values += [linear\_range\_values\_count](group__linear__range.md#gae02547c7922e5a36c815dc89bc1df128)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i]);

115 }

116

117 return values;

118}

119

[ 127](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))

128{

129 return [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min + ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step \* ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->max\_idx - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx));

130}

131

[ 142](group__linear__range.md#ga72b800d1c6af44cb247130139176a59e)static inline int [linear\_range\_get\_value](group__linear__range.md#ga72b800d1c6af44cb247130139176a59e)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

143 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val)

144{

145 if ((idx < r->min\_idx) || (idx > [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->max\_idx)) {

146 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

147 }

148

149 \*val = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min + ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step \* (idx - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx));

150

151 return 0;

152}

153

[ 165](group__linear__range.md#gac054f5cc2aad11de223fa968ebeaa55c)static inline int [linear\_range\_group\_get\_value](group__linear__range.md#gac054f5cc2aad11de223fa968ebeaa55c)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

166 size\_t r\_cnt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx,

167 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val)

168{

169 int ret = -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

170

171 for (size\_t i = 0U; (ret != 0) && (i < r\_cnt); i++) {

172 ret = [linear\_range\_get\_value](group__linear__range.md#ga72b800d1c6af44cb247130139176a59e)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i], idx, val);

173 }

174

175 return ret;

176}

177

[ 193](group__linear__range.md#ga90610e42e63eb4290e5ae6187a53143f)static inline int [linear\_range\_get\_index](group__linear__range.md#ga90610e42e63eb4290e5ae6187a53143f)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

194 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx)

195{

196 if (val < r->min) {

197 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx;

198 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

199 }

200

201 if (val > [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2))) {

202 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->max\_idx;

203 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

204 }

205

206 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step == 0U) {

207 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx;

208 } else {

209 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx + [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(val - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min),

210 [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step);

211 }

212

213 return 0;

214}

215

[ 231](group__linear__range.md#gab8b661f6ed1caba2ab4796a02c1b24a8)static inline int [linear\_range\_group\_get\_index](group__linear__range.md#gab8b661f6ed1caba2ab4796a02c1b24a8)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

232 size\_t r\_cnt, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val,

233 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx)

234{

235 for (size\_t i = 0U; i < r\_cnt; i++) {

236 if ((val > [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i])) &&

237 (i < (r\_cnt - 1U))) {

238 continue;

239 }

240

241 return [linear\_range\_get\_index](group__linear__range.md#ga90610e42e63eb4290e5ae6187a53143f)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i], val, idx);

242 }

243

244 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

245}

246

[ 265](group__linear__range.md#ga6c06a26d629f4d7a195188e7c5df5db1)static inline int [linear\_range\_get\_win\_index](group__linear__range.md#ga6c06a26d629f4d7a195188e7c5df5db1)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

266 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max,

267 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx)

268{

269 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) r\_max = [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

270

271 if ((val\_max < r->min) || (val\_min > r\_max)) {

272 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

273 }

274

275 if (val\_min < r->min) {

276 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx;

277 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

278 }

279

280 if (val\_max > r\_max) {

281 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->max\_idx;

282 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

283 }

284

285 if ([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step == 0U) {

286 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx;

287 return 0;

288 }

289

290 \*idx = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx + [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(val\_min - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min), [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step);

291 if (([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min + [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->step \* (\*idx - [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)->min\_idx)) > val\_max) {

292 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

293 }

294

295 return 0;

296}

297

[ 318](group__linear__range.md#ga11dc5408be53887e9ddf992b574aa16c)static inline int [linear\_range\_group\_get\_win\_index](group__linear__range.md#ga11dc5408be53887e9ddf992b574aa16c)(const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

319 size\_t r\_cnt,

320 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min,

321 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max,

322 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx)

323{

324 for (size\_t i = 0U; i < r\_cnt; i++) {

325 if (val\_min > [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i])) {

326 continue;

327 }

328

329 return [linear\_range\_get\_win\_index](group__linear__range.md#ga6c06a26d629f4d7a195188e7c5df5db1)(&[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[i], val\_min, val\_max, idx);

330 }

331

332 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

333}

334

336

337#ifdef \_\_cplusplus

338}

339#endif

340

341#endif /\* INCLUDE\_ZEPHYR\_SYS\_LINEAR\_RANGE\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[errno.h](errno_8h.md)

System error numbers.

[linear\_range\_group\_get\_win\_index](group__linear__range.md#ga11dc5408be53887e9ddf992b574aa16c)

static int linear\_range\_group\_get\_win\_index(const struct linear\_range \*r, size\_t r\_cnt, int32\_t val\_min, int32\_t val\_max, uint16\_t \*idx)

Obtain index in a group given a value that must be within a window of values.

**Definition** linear\_range.h:318

[linear\_range\_group\_values\_count](group__linear__range.md#ga67b24d9d6e7088daf39020c8c02f8d96)

static uint32\_t linear\_range\_group\_values\_count(const struct linear\_range \*r, size\_t r\_cnt)

Obtain the number of values representable by a group of linear ranges.

**Definition** linear\_range.h:108

[linear\_range\_get\_win\_index](group__linear__range.md#ga6c06a26d629f4d7a195188e7c5df5db1)

static int linear\_range\_get\_win\_index(const struct linear\_range \*r, int32\_t val\_min, int32\_t val\_max, uint16\_t \*idx)

Obtain index given a window of values.

**Definition** linear\_range.h:265

[linear\_range\_get\_value](group__linear__range.md#ga72b800d1c6af44cb247130139176a59e)

static int linear\_range\_get\_value(const struct linear\_range \*r, uint16\_t idx, int32\_t \*val)

Obtain value given a linear range index.

**Definition** linear\_range.h:142

[linear\_range\_get\_index](group__linear__range.md#ga90610e42e63eb4290e5ae6187a53143f)

static int linear\_range\_get\_index(const struct linear\_range \*r, int32\_t val, uint16\_t \*idx)

Obtain index given a value.

**Definition** linear\_range.h:193

[linear\_range\_group\_get\_index](group__linear__range.md#gab8b661f6ed1caba2ab4796a02c1b24a8)

static int linear\_range\_group\_get\_index(const struct linear\_range \*r, size\_t r\_cnt, int32\_t val, uint16\_t \*idx)

Obtain index in a group given a value.

**Definition** linear\_range.h:231

[linear\_range\_group\_get\_value](group__linear__range.md#gac054f5cc2aad11de223fa968ebeaa55c)

static int linear\_range\_group\_get\_value(const struct linear\_range \*r, size\_t r\_cnt, uint16\_t idx, int32\_t \*val)

Obtain value in a group given a linear range index.

**Definition** linear\_range.h:165

[linear\_range\_values\_count](group__linear__range.md#gae02547c7922e5a36c815dc89bc1df128)

static uint32\_t linear\_range\_values\_count(const struct linear\_range \*r)

Obtain the number of values representable in a linear range.

**Definition** linear\_range.h:95

[linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c)

static int32\_t linear\_range\_get\_max\_value(const struct linear\_range \*r)

Obtain the maximum value representable by a linear range.

**Definition** linear\_range.h:127

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:318

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:73

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[stdlib.h](stdlib_8h.md)

[linear\_range](structlinear__range.md)

Linear range.

**Definition** linear\_range.h:61

[linear\_range::min](structlinear__range.md#a4523369fa49fa1d6aa58f0d2634eb41d)

int32\_t min

Minimum value.

**Definition** linear\_range.h:63

[linear\_range::min\_idx](structlinear__range.md#a705275f156fc4bcf5bb111be01aff6ef)

uint16\_t min\_idx

Minimum index (must be <= maximum index).

**Definition** linear\_range.h:67

[linear\_range::max\_idx](structlinear__range.md#a84af63957a1b3e829cf1d53fa6342982)

uint16\_t max\_idx

Maximum index (must be >= minimum index).

**Definition** linear\_range.h:69

[linear\_range::step](structlinear__range.md#a963889c27dd8541f7cd6528ac82401b3)

uint32\_t step

Step value.

**Definition** linear\_range.h:65

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [linear\_range.h](linear__range_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
