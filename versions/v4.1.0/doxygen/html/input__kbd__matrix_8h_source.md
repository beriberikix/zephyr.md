---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/input__kbd__matrix_8h_source.html
original_path: doxygen/html/input__kbd__matrix_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_kbd\_matrix.h

[Go to the documentation of this file.](input__kbd__matrix_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_KBD\_MATRIX\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_KBD\_MATRIX\_H\_

9

16

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[zephyr/pm/device.h](pm_2device_8h.md)>

20#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

21#include <[zephyr/sys/util.h](sys_2util_8h.md)>

22#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

23#include <[zephyr/toolchain.h](toolchain_8h.md)>

24

[ 26](group__input__kbd__matrix.md#ga2f35f23d426f93f71057a31f612a88de)#define INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE -1

27

[ 29](group__input__kbd__matrix.md#ga6d27ba5612c09d80087e854b21fb9e65)#define INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL -2

30

[ 32](group__input__kbd__matrix.md#ga80a384d2041dcee27d7940a1e408d82a)#define INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES 30U

33

35#if CONFIG\_INPUT\_KBD\_MATRIX\_16\_BIT\_ROW

36typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86);

37#define PRIkbdrow "04" PRIx16

38#else

[ 39](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86);

[ 40](group__input__kbd__matrix.md#ga1343b97a8b072f8ed362e8a4f242bdd1)#define PRIkbdrow "02" PRIx8

41#endif

42

43#if defined(CONFIG\_INPUT\_KBD\_ACTUAL\_KEY\_MASK\_DYNAMIC) || defined(\_\_DOXYGEN\_\_)

[ 44](group__input__kbd__matrix.md#gaec0209680e18da8584bdf41e5229aaae)#define INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST

[ 63](group__input__kbd__matrix.md#gab35f4bf523760933294242ccc8226490)int [input\_kbd\_matrix\_actual\_key\_mask\_set](group__input__kbd__matrix.md#gab35f4bf523760933294242ccc8226490)(const struct [device](structdevice.md) \*dev,

64 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) row, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) col, bool enabled);

65#else

66#define INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST const

67#endif

68

[ 70](group__input__kbd__matrix.md#gae395cd03c295673dc9563c252ba7e022)#define INPUT\_KBD\_MATRIX\_ROW\_BITS NUM\_BITS(kbd\_row\_t)

71

[ 75](structinput__kbd__matrix__api.md)struct [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md) {

[ 86](structinput__kbd__matrix__api.md#af8211d738527ac44876dd07869862f20) void (\*[drive\_column](structinput__kbd__matrix__api.md#af8211d738527ac44876dd07869862f20))(const struct [device](structdevice.md) \*dev, int col);

[ 92](structinput__kbd__matrix__api.md#af04e3f78fde3297a70a63c8a8addb477) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) (\*[read\_row](structinput__kbd__matrix__api.md#af04e3f78fde3297a70a63c8a8addb477))(const struct [device](structdevice.md) \*dev);

[ 103](structinput__kbd__matrix__api.md#aaae2b1eb357fb4b7f1881ef496d79560) void (\*[set\_detect\_mode](structinput__kbd__matrix__api.md#aaae2b1eb357fb4b7f1881ef496d79560))(const struct [device](structdevice.md) \*dev, bool enabled);

104};

105

[ 111](structinput__kbd__matrix__common__config.md)struct [input\_kbd\_matrix\_common\_config](structinput__kbd__matrix__common__config.md) {

[ 112](structinput__kbd__matrix__common__config.md#ace0bafa079826819b7df7950cb3e8212) const struct [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md) \*[api](structinput__kbd__matrix__common__config.md#ace0bafa079826819b7df7950cb3e8212);

[ 113](structinput__kbd__matrix__common__config.md#af3c4f2bcddf50dc2dbf0ad0e54230565) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [row\_size](structinput__kbd__matrix__common__config.md#af3c4f2bcddf50dc2dbf0ad0e54230565);

[ 114](structinput__kbd__matrix__common__config.md#adfb2b978f1d41bdff28acca17cc4ed3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [col\_size](structinput__kbd__matrix__common__config.md#adfb2b978f1d41bdff28acca17cc4ed3d);

[ 115](structinput__kbd__matrix__common__config.md#a34ce838e3ed4a5cb19c8ce961a9da947) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [poll\_period\_us](structinput__kbd__matrix__common__config.md#a34ce838e3ed4a5cb19c8ce961a9da947);

[ 116](structinput__kbd__matrix__common__config.md#ac67c028c2cf743c1854dc83aed8f4db4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stable\_poll\_period\_us](structinput__kbd__matrix__common__config.md#ac67c028c2cf743c1854dc83aed8f4db4);

[ 117](structinput__kbd__matrix__common__config.md#a81ccf8e0a1f49361f55737e0149bd656) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [poll\_timeout\_ms](structinput__kbd__matrix__common__config.md#a81ccf8e0a1f49361f55737e0149bd656);

[ 118](structinput__kbd__matrix__common__config.md#a004cb35eede1e58b27730a46155540e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [debounce\_down\_us](structinput__kbd__matrix__common__config.md#a004cb35eede1e58b27730a46155540e9);

[ 119](structinput__kbd__matrix__common__config.md#a545fba8a03ced44a95d7bb7f345d763f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [debounce\_up\_us](structinput__kbd__matrix__common__config.md#a545fba8a03ced44a95d7bb7f345d763f);

[ 120](structinput__kbd__matrix__common__config.md#a13374b57becd9314ea726ae888f1702a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [settle\_time\_us](structinput__kbd__matrix__common__config.md#a13374b57becd9314ea726ae888f1702a);

[ 121](structinput__kbd__matrix__common__config.md#a2377a3c7cbd195bb6da3d4dfaf1f5972) bool [ghostkey\_check](structinput__kbd__matrix__common__config.md#a2377a3c7cbd195bb6da3d4dfaf1f5972);

[ 122](structinput__kbd__matrix__common__config.md#ac2343c08359099f383f154655b371cf6) [INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](group__input__kbd__matrix.md#gaec0209680e18da8584bdf41e5229aaae) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \*[actual\_key\_mask](structinput__kbd__matrix__common__config.md#ac2343c08359099f383f154655b371cf6);

123

124 /\* extra data pointers \*/

[ 125](structinput__kbd__matrix__common__config.md#aafb384043bed6593b696e11fd34e0f97) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \*[matrix\_stable\_state](structinput__kbd__matrix__common__config.md#aafb384043bed6593b696e11fd34e0f97);

[ 126](structinput__kbd__matrix__common__config.md#a47d4177495c1e17b76c1f616720a3aa6) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \*[matrix\_unstable\_state](structinput__kbd__matrix__common__config.md#a47d4177495c1e17b76c1f616720a3aa6);

[ 127](structinput__kbd__matrix__common__config.md#a361fd7c63b2ca643e4b957a6c1c85ae4) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \*[matrix\_previous\_state](structinput__kbd__matrix__common__config.md#a361fd7c63b2ca643e4b957a6c1c85ae4);

[ 128](structinput__kbd__matrix__common__config.md#a5da560d28d8bfc527d60c10e4aa29ffb) [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \*[matrix\_new\_state](structinput__kbd__matrix__common__config.md#a5da560d28d8bfc527d60c10e4aa29ffb);

[ 129](structinput__kbd__matrix__common__config.md#a0fbc6d10c2f15f3a0126e0c229ec9686) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[scan\_cycle\_idx](structinput__kbd__matrix__common__config.md#a0fbc6d10c2f15f3a0126e0c229ec9686);

130};

131

[ 132](group__input__kbd__matrix.md#gac7cc0314fa201b1efbcac37cf5f90576)#define INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, name) \

133 \_CONCAT(\_\_input\_kbd\_matrix\_, \

134 \_CONCAT(name, DEVICE\_DT\_NAME\_GET(node\_id)))

135

[ 140](group__input__kbd__matrix.md#gac1a4389b1afeab9c48a15c024bfb0cac)#define INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL(node\_id, \_row\_size, \_col\_size) \

141 BUILD\_ASSERT(IN\_RANGE(\_row\_size, 1, INPUT\_KBD\_MATRIX\_ROW\_BITS), "invalid row-size"); \

142 BUILD\_ASSERT(IN\_RANGE(\_col\_size, 1, UINT8\_MAX), "invalid col-size"); \

143 IF\_ENABLED(DT\_NODE\_HAS\_PROP(node\_id, actual\_key\_mask), ( \

144 BUILD\_ASSERT(DT\_PROP\_LEN(node\_id, actual\_key\_mask) == \_col\_size, \

145 "actual-key-mask size does not match the number of columns"); \

146 static INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST kbd\_row\_t \

147 INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, actual\_key\_mask)[\_col\_size] = \

148 DT\_PROP(node\_id, actual\_key\_mask); \

149 )) \

150 static kbd\_row\_t INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, stable\_state)[\_col\_size]; \

151 static kbd\_row\_t INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, unstable\_state)[\_col\_size]; \

152 static kbd\_row\_t INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, previous\_state)[\_col\_size]; \

153 static kbd\_row\_t INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, new\_state)[\_col\_size]; \

154 static uint8\_t INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, scan\_cycle\_idx)[\_row\_size \* \_col\_size];

155

[ 159](group__input__kbd__matrix.md#ga512bea2ca97569f465074ca8f231a0a3)#define INPUT\_KBD\_MATRIX\_DT\_DEFINE(node\_id) \

160 INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL( \

161 node\_id, DT\_PROP(node\_id, row\_size), DT\_PROP(node\_id, col\_size))

162

[ 171](group__input__kbd__matrix.md#ga1d3fe52f10c75dc4c32c8583c05fb2a2)#define INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL(inst, row\_size, col\_size) \

172 INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL(DT\_DRV\_INST(inst), row\_size, col\_size)

173

[ 179](group__input__kbd__matrix.md#gab3ea5b7d597574b32ced16604648a6d2)#define INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE(inst) \

180 INPUT\_KBD\_MATRIX\_DT\_DEFINE(DT\_DRV\_INST(inst))

181

[ 190](group__input__kbd__matrix.md#ga5ad9141616b4a63068bfbe8004bba67d)#define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL(node\_id, \_api, \_row\_size, \_col\_size) \

191 { \

192 .api = \_api, \

193 .row\_size = \_row\_size, \

194 .col\_size = \_col\_size, \

195 .poll\_period\_us = DT\_PROP(node\_id, poll\_period\_ms) \* USEC\_PER\_MSEC, \

196 .stable\_poll\_period\_us = DT\_PROP\_OR(node\_id, stable\_poll\_period\_ms, \

197 DT\_PROP(node\_id, poll\_period\_ms)) \* \

198 USEC\_PER\_MSEC, \

199 .poll\_timeout\_ms = DT\_PROP(node\_id, poll\_timeout\_ms), \

200 .debounce\_down\_us = DT\_PROP(node\_id, debounce\_down\_ms) \* USEC\_PER\_MSEC, \

201 .debounce\_up\_us = DT\_PROP(node\_id, debounce\_up\_ms) \* USEC\_PER\_MSEC, \

202 .settle\_time\_us = DT\_PROP(node\_id, settle\_time\_us), \

203 .ghostkey\_check = !DT\_PROP(node\_id, no\_ghostkey\_check), \

204 IF\_ENABLED(DT\_NODE\_HAS\_PROP(node\_id, actual\_key\_mask), ( \

205 .actual\_key\_mask = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, actual\_key\_mask), \

206 )) \

207 \

208 .matrix\_stable\_state = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, stable\_state), \

209 .matrix\_unstable\_state = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, unstable\_state), \

210 .matrix\_previous\_state = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, previous\_state), \

211 .matrix\_new\_state = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, new\_state), \

212 .scan\_cycle\_idx = INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, scan\_cycle\_idx), \

213 }

214

[ 221](group__input__kbd__matrix.md#ga3281b4e5909a1c07d8190092bc31cb12)#define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT(node\_id, api) \

222 INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL( \

223 node\_id, api, DT\_PROP(node\_id, row\_size), DT\_PROP(node\_id, col\_size))

224

[ 234](group__input__kbd__matrix.md#gac6baf9b284f0796cdd5dbcef338f9588)#define INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL(inst, api, row\_size, col\_size) \

235 INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL(DT\_DRV\_INST(inst), api, row\_size, col\_size)

236

[ 243](group__input__kbd__matrix.md#gab19b4a8c66c5540b4e690459655f92fd)#define INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT(inst, api) \

244 INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT(DT\_DRV\_INST(inst), api)

245

[ 251](structinput__kbd__matrix__common__data.md)struct [input\_kbd\_matrix\_common\_data](structinput__kbd__matrix__common__data.md) {

252 /\* Track previous cycles, used for debouncing. \*/

[ 253](structinput__kbd__matrix__common__data.md#ac54780c609eb2abc67e468470ac3ef83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [scan\_clk\_cycle](structinput__kbd__matrix__common__data.md#ac54780c609eb2abc67e468470ac3ef83)[[INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES](group__input__kbd__matrix.md#ga80a384d2041dcee27d7940a1e408d82a)];

[ 254](structinput__kbd__matrix__common__data.md#a53b66dca86734fa149b672583455bc61) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_cycles\_idx](structinput__kbd__matrix__common__data.md#a53b66dca86734fa149b672583455bc61);

255

[ 256](structinput__kbd__matrix__common__data.md#afe0d57cf725c825097ba26b81bd2640c) struct k\_sem [poll\_lock](structinput__kbd__matrix__common__data.md#afe0d57cf725c825097ba26b81bd2640c);

257#ifdef CONFIG\_PM\_DEVICE

258 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) suspended;

259#endif

260

[ 261](structinput__kbd__matrix__common__data.md#a526586907a6f0e4d1316c4304adda336) struct [k\_thread](structk__thread.md) [thread](structinput__kbd__matrix__common__data.md#a526586907a6f0e4d1316c4304adda336);

262

[ 263](structinput__kbd__matrix__common__data.md#ac66f323c17cd346bb1b0b0aa8fc2965a) [K\_KERNEL\_STACK\_MEMBER](structinput__kbd__matrix__common__data.md#ac66f323c17cd346bb1b0b0aa8fc2965a)(thread\_stack,

264 CONFIG\_INPUT\_KBD\_MATRIX\_THREAD\_STACK\_SIZE);

265};

266

[ 273](group__input__kbd__matrix.md#ga352d484344c93c30f5cad75551793377)#define INPUT\_KBD\_STRUCT\_CHECK(config, data) \

274 BUILD\_ASSERT(offsetof(config, common) == 0, \

275 "struct input\_kbd\_matrix\_common\_config must be placed first"); \

276 BUILD\_ASSERT(offsetof(data, common) == 0, \

277 "struct input\_kbd\_matrix\_common\_data must be placed first")

278

[ 287](group__input__kbd__matrix.md#gaf97b6ff410631f111d7c3a7aa7f64171)void [input\_kbd\_matrix\_poll\_start](group__input__kbd__matrix.md#gaf97b6ff410631f111d7c3a7aa7f64171)(const struct [device](structdevice.md) \*dev);

288

289#if defined(CONFIG\_INPUT\_KBD\_DRIVE\_COLUMN\_HOOK) || defined(\_\_DOXYGEN\_\_)

[ 302](group__input__kbd__matrix.md#ga6d843c7213bf5c0af9003c165a5f3e03)void [input\_kbd\_matrix\_drive\_column\_hook](group__input__kbd__matrix.md#ga6d843c7213bf5c0af9003c165a5f3e03)(const struct [device](structdevice.md) \*dev, int col);

303#endif

304

[ 315](group__input__kbd__matrix.md#ga938dc38da7e81e5a68b8b9dc585c4bab)int [input\_kbd\_matrix\_common\_init](group__input__kbd__matrix.md#ga938dc38da7e81e5a68b8b9dc585c4bab)(const struct [device](structdevice.md) \*dev);

316

317#ifdef CONFIG\_PM\_DEVICE

327int input\_kbd\_matrix\_pm\_action(const struct [device](structdevice.md) \*dev,

328 enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action);

329#endif

330

332

333#endif /\* ZEPHYR\_INCLUDE\_INPUT\_KBD\_MATRIX\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[input\_kbd\_matrix\_drive\_column\_hook](group__input__kbd__matrix.md#ga6d843c7213bf5c0af9003c165a5f3e03)

void input\_kbd\_matrix\_drive\_column\_hook(const struct device \*dev, int col)

Drive column hook.

[INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES](group__input__kbd__matrix.md#ga80a384d2041dcee27d7940a1e408d82a)

#define INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES

Number of tracked scan cycles.

**Definition** input\_kbd\_matrix.h:32

[input\_kbd\_matrix\_common\_init](group__input__kbd__matrix.md#ga938dc38da7e81e5a68b8b9dc585c4bab)

int input\_kbd\_matrix\_common\_init(const struct device \*dev)

Common function to initialize a keyboard matrix device at init time.

[input\_kbd\_matrix\_actual\_key\_mask\_set](group__input__kbd__matrix.md#gab35f4bf523760933294242ccc8226490)

int input\_kbd\_matrix\_actual\_key\_mask\_set(const struct device \*dev, uint8\_t row, uint8\_t col, bool enabled)

Enables or disables a specific row, column combination in the actual key mask.

[kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)

uint8\_t kbd\_row\_t

Row entry data type.

**Definition** input\_kbd\_matrix.h:39

[INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](group__input__kbd__matrix.md#gaec0209680e18da8584bdf41e5229aaae)

#define INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST

**Definition** input\_kbd\_matrix.h:44

[input\_kbd\_matrix\_poll\_start](group__input__kbd__matrix.md#gaf97b6ff410631f111d7c3a7aa7f64171)

void input\_kbd\_matrix\_poll\_start(const struct device \*dev)

Start scanning the keyboard matrix.

[pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c)

pm\_device\_action

Device PM actions.

**Definition** device.h:90

[kernel.h](kernel_8h.md)

Public kernel APIs.

[device.h](pm_2device_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md)

Keyboard matrix internal APIs.

**Definition** input\_kbd\_matrix.h:75

[input\_kbd\_matrix\_api::set\_detect\_mode](structinput__kbd__matrix__api.md#aaae2b1eb357fb4b7f1881ef496d79560)

void(\* set\_detect\_mode)(const struct device \*dev, bool enabled)

Request to put the matrix in detection mode.

**Definition** input\_kbd\_matrix.h:103

[input\_kbd\_matrix\_api::read\_row](structinput__kbd__matrix__api.md#af04e3f78fde3297a70a63c8a8addb477)

kbd\_row\_t(\* read\_row)(const struct device \*dev)

Read the matrix row.

**Definition** input\_kbd\_matrix.h:92

[input\_kbd\_matrix\_api::drive\_column](structinput__kbd__matrix__api.md#af8211d738527ac44876dd07869862f20)

void(\* drive\_column)(const struct device \*dev, int col)

Request to drive a specific column.

**Definition** input\_kbd\_matrix.h:86

[input\_kbd\_matrix\_common\_config](structinput__kbd__matrix__common__config.md)

Common keyboard matrix config.

**Definition** input\_kbd\_matrix.h:111

[input\_kbd\_matrix\_common\_config::debounce\_down\_us](structinput__kbd__matrix__common__config.md#a004cb35eede1e58b27730a46155540e9)

uint32\_t debounce\_down\_us

**Definition** input\_kbd\_matrix.h:118

[input\_kbd\_matrix\_common\_config::scan\_cycle\_idx](structinput__kbd__matrix__common__config.md#a0fbc6d10c2f15f3a0126e0c229ec9686)

uint8\_t \* scan\_cycle\_idx

**Definition** input\_kbd\_matrix.h:129

[input\_kbd\_matrix\_common\_config::settle\_time\_us](structinput__kbd__matrix__common__config.md#a13374b57becd9314ea726ae888f1702a)

uint32\_t settle\_time\_us

**Definition** input\_kbd\_matrix.h:120

[input\_kbd\_matrix\_common\_config::ghostkey\_check](structinput__kbd__matrix__common__config.md#a2377a3c7cbd195bb6da3d4dfaf1f5972)

bool ghostkey\_check

**Definition** input\_kbd\_matrix.h:121

[input\_kbd\_matrix\_common\_config::poll\_period\_us](structinput__kbd__matrix__common__config.md#a34ce838e3ed4a5cb19c8ce961a9da947)

uint32\_t poll\_period\_us

**Definition** input\_kbd\_matrix.h:115

[input\_kbd\_matrix\_common\_config::matrix\_previous\_state](structinput__kbd__matrix__common__config.md#a361fd7c63b2ca643e4b957a6c1c85ae4)

kbd\_row\_t \* matrix\_previous\_state

**Definition** input\_kbd\_matrix.h:127

[input\_kbd\_matrix\_common\_config::matrix\_unstable\_state](structinput__kbd__matrix__common__config.md#a47d4177495c1e17b76c1f616720a3aa6)

kbd\_row\_t \* matrix\_unstable\_state

**Definition** input\_kbd\_matrix.h:126

[input\_kbd\_matrix\_common\_config::debounce\_up\_us](structinput__kbd__matrix__common__config.md#a545fba8a03ced44a95d7bb7f345d763f)

uint32\_t debounce\_up\_us

**Definition** input\_kbd\_matrix.h:119

[input\_kbd\_matrix\_common\_config::matrix\_new\_state](structinput__kbd__matrix__common__config.md#a5da560d28d8bfc527d60c10e4aa29ffb)

kbd\_row\_t \* matrix\_new\_state

**Definition** input\_kbd\_matrix.h:128

[input\_kbd\_matrix\_common\_config::poll\_timeout\_ms](structinput__kbd__matrix__common__config.md#a81ccf8e0a1f49361f55737e0149bd656)

uint32\_t poll\_timeout\_ms

**Definition** input\_kbd\_matrix.h:117

[input\_kbd\_matrix\_common\_config::matrix\_stable\_state](structinput__kbd__matrix__common__config.md#aafb384043bed6593b696e11fd34e0f97)

kbd\_row\_t \* matrix\_stable\_state

**Definition** input\_kbd\_matrix.h:125

[input\_kbd\_matrix\_common\_config::actual\_key\_mask](structinput__kbd__matrix__common__config.md#ac2343c08359099f383f154655b371cf6)

kbd\_row\_t \* actual\_key\_mask

**Definition** input\_kbd\_matrix.h:122

[input\_kbd\_matrix\_common\_config::stable\_poll\_period\_us](structinput__kbd__matrix__common__config.md#ac67c028c2cf743c1854dc83aed8f4db4)

uint32\_t stable\_poll\_period\_us

**Definition** input\_kbd\_matrix.h:116

[input\_kbd\_matrix\_common\_config::api](structinput__kbd__matrix__common__config.md#ace0bafa079826819b7df7950cb3e8212)

const struct input\_kbd\_matrix\_api \* api

**Definition** input\_kbd\_matrix.h:112

[input\_kbd\_matrix\_common\_config::col\_size](structinput__kbd__matrix__common__config.md#adfb2b978f1d41bdff28acca17cc4ed3d)

uint8\_t col\_size

**Definition** input\_kbd\_matrix.h:114

[input\_kbd\_matrix\_common\_config::row\_size](structinput__kbd__matrix__common__config.md#af3c4f2bcddf50dc2dbf0ad0e54230565)

uint8\_t row\_size

**Definition** input\_kbd\_matrix.h:113

[input\_kbd\_matrix\_common\_data](structinput__kbd__matrix__common__data.md)

Common keyboard matrix data.

**Definition** input\_kbd\_matrix.h:251

[input\_kbd\_matrix\_common\_data::thread](structinput__kbd__matrix__common__data.md#a526586907a6f0e4d1316c4304adda336)

struct k\_thread thread

**Definition** input\_kbd\_matrix.h:261

[input\_kbd\_matrix\_common\_data::scan\_cycles\_idx](structinput__kbd__matrix__common__data.md#a53b66dca86734fa149b672583455bc61)

uint8\_t scan\_cycles\_idx

**Definition** input\_kbd\_matrix.h:254

[input\_kbd\_matrix\_common\_data::scan\_clk\_cycle](structinput__kbd__matrix__common__data.md#ac54780c609eb2abc67e468470ac3ef83)

uint32\_t scan\_clk\_cycle[30U]

**Definition** input\_kbd\_matrix.h:253

[input\_kbd\_matrix\_common\_data::K\_KERNEL\_STACK\_MEMBER](structinput__kbd__matrix__common__data.md#ac66f323c17cd346bb1b0b0aa8fc2965a)

K\_KERNEL\_STACK\_MEMBER(thread\_stack, CONFIG\_INPUT\_KBD\_MATRIX\_THREAD\_STACK\_SIZE)

[input\_kbd\_matrix\_common\_data::poll\_lock](structinput__kbd__matrix__common__data.md#afe0d57cf725c825097ba26b81bd2640c)

struct k\_sem poll\_lock

**Definition** input\_kbd\_matrix.h:256

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_kbd\_matrix.h](input__kbd__matrix_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
