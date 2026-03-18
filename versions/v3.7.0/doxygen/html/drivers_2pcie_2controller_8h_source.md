---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2pcie_2controller_8h_source.html
original_path: doxygen/html/drivers_2pcie_2controller_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

controller.h

[Go to the documentation of this file.](drivers_2pcie_2controller_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 BayLibre, SAS

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CONTROLLERS\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CONTROLLERS\_H\_

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17

18#ifdef CONFIG\_PCIE\_MSI

19#include <[zephyr/drivers/pcie/msi.h](msi_8h.md)>

20#endif

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 44](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a))(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

45 unsigned int reg);

46

[ 58](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109)typedef void (\*[pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109))(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

59 unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

60

[ 78](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d))(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

79 bool mem, bool mem64, size\_t bar\_size,

80 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr);

81

[ 97](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a))(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

98 bool mem, bool mem64, size\_t align,

99 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr);

100

[ 120](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f))(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

121 bool mem, bool mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr,

122 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr);

123

124#ifdef CONFIG\_PCIE\_MSI

125typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*pcie\_ctrl\_msi\_device\_setup\_t)(const struct [device](structdevice.md) \*dev, unsigned int priority,

126 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector);

127#endif

128

[ 141](group__pcie__controller__interface.md#gaa16b59c39f273a654b72d9e209f3ba2e)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_generic\_ctrl\_conf\_read](group__pcie__controller__interface.md#gaa16b59c39f273a654b72d9e209f3ba2e)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, unsigned int reg);

142

143

[ 156](group__pcie__controller__interface.md#ga709ecedbd0585b4eb17fc2f5923a8f61)void [pcie\_generic\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga709ecedbd0585b4eb17fc2f5923a8f61)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

157 unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

158

[ 169](group__pcie__controller__interface.md#ga75910ea4255a740b57e35a596a90b7bb)void [pcie\_generic\_ctrl\_enumerate](group__pcie__controller__interface.md#ga75910ea4255a740b57e35a596a90b7bb)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf\_start);

170

[ 174](structpcie__ctrl__driver__api.md)\_\_subsystem struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) {

[ 175](structpcie__ctrl__driver__api.md#a20c1faf02c71e88da165c889550a76ae) [pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a) [conf\_read](structpcie__ctrl__driver__api.md#a20c1faf02c71e88da165c889550a76ae);

[ 176](structpcie__ctrl__driver__api.md#a46fa0fd3a759fe2dc960546b49c53979) [pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109) [conf\_write](structpcie__ctrl__driver__api.md#a46fa0fd3a759fe2dc960546b49c53979);

[ 177](structpcie__ctrl__driver__api.md#a46191bf9aad7ab7ac1319918873b8b29) [pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d) [region\_allocate](structpcie__ctrl__driver__api.md#a46191bf9aad7ab7ac1319918873b8b29);

[ 178](structpcie__ctrl__driver__api.md#a5d7687cd738bd86a785fc281781d2759) [pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a) [region\_get\_allocate\_base](structpcie__ctrl__driver__api.md#a5d7687cd738bd86a785fc281781d2759);

[ 179](structpcie__ctrl__driver__api.md#a71a4d13492bb3098bdb2c0e0ff7b94cf) [pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f) [region\_translate](structpcie__ctrl__driver__api.md#a71a4d13492bb3098bdb2c0e0ff7b94cf);

180#ifdef CONFIG\_PCIE\_MSI

181 pcie\_ctrl\_msi\_device\_setup\_t msi\_device\_setup;

182#endif

183};

184

[ 196](group__pcie__controller__interface.md#ga1d978b8075191d6e571349684c731a43)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_ctrl\_conf\_read](group__pcie__controller__interface.md#ga1d978b8075191d6e571349684c731a43)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

197 unsigned int reg)

198{

199 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

200 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

201

202 return api->[conf\_read](structpcie__ctrl__driver__api.md#a20c1faf02c71e88da165c889550a76ae)(dev, bdf, reg);

203}

204

[ 216](group__pcie__controller__interface.md#ga5cfe01762e5af8dc0cc5fbd550ff7e74)static inline void [pcie\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga5cfe01762e5af8dc0cc5fbd550ff7e74)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

217 unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

218{

219 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

220 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

221

222 api->[conf\_write](structpcie__ctrl__driver__api.md#a46fa0fd3a759fe2dc960546b49c53979)(dev, bdf, reg, data);

223}

224

[ 242](group__pcie__controller__interface.md#ga1de030e2e8b07509d75de5a348297f42)static inline bool [pcie\_ctrl\_region\_allocate](group__pcie__controller__interface.md#ga1de030e2e8b07509d75de5a348297f42)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

243 bool mem, bool mem64, size\_t bar\_size,

244 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr)

245{

246 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

247 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

248

249 return api->[region\_allocate](structpcie__ctrl__driver__api.md#a46191bf9aad7ab7ac1319918873b8b29)(dev, bdf, mem, mem64, bar\_size, bar\_bus\_addr);

250}

251

[ 267](group__pcie__controller__interface.md#gae7c109ca138adfd906fef5b6f3dca385)static inline bool [pcie\_ctrl\_region\_get\_allocate\_base](group__pcie__controller__interface.md#gae7c109ca138adfd906fef5b6f3dca385)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

268 bool mem, bool mem64, size\_t align,

269 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr)

270{

271 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

272 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

273

274 return api->[region\_get\_allocate\_base](structpcie__ctrl__driver__api.md#a5d7687cd738bd86a785fc281781d2759)(dev, bdf, mem, mem64, align, bar\_base\_addr);

275}

276

[ 295](group__pcie__controller__interface.md#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)static inline bool [pcie\_ctrl\_region\_translate](group__pcie__controller__interface.md#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)(const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

296 bool mem, bool mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr,

297 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr)

298{

299 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

300 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

301

302 if (!api->[region\_translate](structpcie__ctrl__driver__api.md#a71a4d13492bb3098bdb2c0e0ff7b94cf)) {

303 \*bar\_addr = bar\_bus\_addr;

304 return true;

305 } else {

306 return api->[region\_translate](structpcie__ctrl__driver__api.md#a71a4d13492bb3098bdb2c0e0ff7b94cf)(dev, bdf, mem, mem64, bar\_bus\_addr, bar\_addr);

307 }

308}

309

310#ifdef CONFIG\_PCIE\_MSI

311static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcie\_ctrl\_msi\_device\_setup(const struct [device](structdevice.md) \*dev, unsigned int priority,

312 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector)

313{

314 const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*api =

315 (const struct [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

316

317 return api->msi\_device\_setup(dev, priority, vectors, n\_vector);

318}

319#endif

320

[ 323](structpcie__ctrl__config.md)struct [pcie\_ctrl\_config](structpcie__ctrl__config.md) {

324#ifdef CONFIG\_PCIE\_MSI

325 const struct [device](structdevice.md) \*msi\_parent;

326#endif

327 /\* Configuration space physical address \*/

[ 328](structpcie__ctrl__config.md#a3de0f32aaf3ddb377897974dfdfe67bd) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [cfg\_addr](structpcie__ctrl__config.md#a3de0f32aaf3ddb377897974dfdfe67bd);

329 /\* Configuration space physical size \*/

[ 330](structpcie__ctrl__config.md#adb1b8ed76f3f994f2da72c8e8b40d4f0) size\_t [cfg\_size](structpcie__ctrl__config.md#adb1b8ed76f3f994f2da72c8e8b40d4f0);

331 /\* BAR regions translation ranges count \*/

[ 332](structpcie__ctrl__config.md#a4a620f03546490b65ba4d097329928e8) size\_t [ranges\_count](structpcie__ctrl__config.md#a4a620f03546490b65ba4d097329928e8);

333 /\* BAR regions translation ranges table \*/

334 struct {

335 /\* Flags as defined in the PCI Bus Binding to IEEE Std 1275-1994 \*/

[ 336](structpcie__ctrl__config.md#a90e48aaca78a8284caa449ee3972d87b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structpcie__ctrl__config.md#a90e48aaca78a8284caa449ee3972d87b);

337 /\* bus-centric offset from the start of the region \*/

[ 338](structpcie__ctrl__config.md#a45f9fa1124aa64bbfd7ff2c5519cbb4b) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [pcie\_bus\_addr](structpcie__ctrl__config.md#a45f9fa1124aa64bbfd7ff2c5519cbb4b);

339 /\* CPU-centric offset from the start of the region \*/

[ 340](structpcie__ctrl__config.md#ace0b3505edc0aff3678a91b630244963) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [host\_map\_addr](structpcie__ctrl__config.md#ace0b3505edc0aff3678a91b630244963);

341 /\* region size \*/

[ 342](structpcie__ctrl__config.md#ae3dd8d3d72a1597ee135b49e46e31bec) size\_t [map\_length](structpcie__ctrl__config.md#ae3dd8d3d72a1597ee135b49e46e31bec);

[ 343](structpcie__ctrl__config.md#a1a59bec03927f2c6b5fd0aed8c36e6b4) } [ranges](structpcie__ctrl__config.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)[];

344};

345

346/\*

347 \* Fills the pcie\_ctrl\_config.ranges table from DT

348 \*/

[ 349](group__pcie__controller__interface.md#ga91525130b94b07187633abd1e017aa61)#define PCIE\_RANGE\_FORMAT(node\_id, idx) \

350{ \

351 .flags = DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx), \

352 .pcie\_bus\_addr = DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx), \

353 .host\_map\_addr = DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx), \

354 .map\_length = DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx), \

355},

356

357#ifdef \_\_cplusplus

358}

359#endif

360

364

365#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_CONTROLLERS\_H\_ \*/

[device.h](device_8h.md)

[pcie\_ctrl\_conf\_read](group__pcie__controller__interface.md#ga1d978b8075191d6e571349684c731a43)

static uint32\_t pcie\_ctrl\_conf\_read(const struct device \*dev, pcie\_bdf\_t bdf, unsigned int reg)

Read a 32-bit word from an endpoint's configuration space.

**Definition** controller.h:196

[pcie\_ctrl\_region\_allocate](group__pcie__controller__interface.md#ga1de030e2e8b07509d75de5a348297f42)

static bool pcie\_ctrl\_region\_allocate(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, size\_t bar\_size, uintptr\_t \*bar\_bus\_addr)

Allocate a memory region subset for an endpoint Base Address Register.

**Definition** controller.h:242

[pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109)

void(\* pcie\_ctrl\_conf\_write\_t)(const struct device \*dev, pcie\_bdf\_t bdf, unsigned int reg, uint32\_t data)

Function called to write a 32-bit word to an endpoint's configuration space.

**Definition** controller.h:58

[pcie\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga5cfe01762e5af8dc0cc5fbd550ff7e74)

static void pcie\_ctrl\_conf\_write(const struct device \*dev, pcie\_bdf\_t bdf, unsigned int reg, uint32\_t data)

Write a 32-bit word to an endpoint's configuration space.

**Definition** controller.h:216

[pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d)

bool(\* pcie\_ctrl\_region\_allocate\_t)(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, size\_t bar\_size, uintptr\_t \*bar\_bus\_addr)

Function called to allocate a memory region subset for an endpoint Base Address Register.

**Definition** controller.h:78

[pcie\_generic\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga709ecedbd0585b4eb17fc2f5923a8f61)

void pcie\_generic\_ctrl\_conf\_write(mm\_reg\_t cfg\_addr, pcie\_bdf\_t bdf, unsigned int reg, uint32\_t data)

Write a 32-bit word to a Memory-Mapped endpoint's configuration space.

[pcie\_generic\_ctrl\_enumerate](group__pcie__controller__interface.md#ga75910ea4255a740b57e35a596a90b7bb)

void pcie\_generic\_ctrl\_enumerate(const struct device \*dev, pcie\_bdf\_t bdf\_start)

Start PCIe Endpoints enumeration.

[pcie\_generic\_ctrl\_conf\_read](group__pcie__controller__interface.md#gaa16b59c39f273a654b72d9e209f3ba2e)

uint32\_t pcie\_generic\_ctrl\_conf\_read(mm\_reg\_t cfg\_addr, pcie\_bdf\_t bdf, unsigned int reg)

Read a 32-bit word from a Memory-Mapped endpoint's configuration space.

[pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a)

bool(\* pcie\_ctrl\_region\_get\_allocate\_base\_t)(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, size\_t align, uintptr\_t \*bar\_base\_addr)

Function called to get the current allocation base of a memory region subset for an endpoint Base Add...

**Definition** controller.h:97

[pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f)

bool(\* pcie\_ctrl\_region\_translate\_t)(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, uintptr\_t bar\_bus\_addr, uintptr\_t \*bar\_addr)

Function called to translate an endpoint Base Address Register bus-centric address into Physical addr...

**Definition** controller.h:120

[pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a)

uint32\_t(\* pcie\_ctrl\_conf\_read\_t)(const struct device \*dev, pcie\_bdf\_t bdf, unsigned int reg)

Function called to read a 32-bit word from an endpoint's configuration space.

**Definition** controller.h:44

[pcie\_ctrl\_region\_translate](group__pcie__controller__interface.md#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)

static bool pcie\_ctrl\_region\_translate(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, uintptr\_t bar\_bus\_addr, uintptr\_t \*bar\_addr)

Translate an endpoint Base Address Register bus-centric address into Physical address.

**Definition** controller.h:295

[pcie\_ctrl\_region\_get\_allocate\_base](group__pcie__controller__interface.md#gae7c109ca138adfd906fef5b6f3dca385)

static bool pcie\_ctrl\_region\_get\_allocate\_base(const struct device \*dev, pcie\_bdf\_t bdf, bool mem, bool mem64, size\_t align, uintptr\_t \*bar\_base\_addr)

Function called to get the current allocation base of a memory region subset for an endpoint Base Add...

**Definition** controller.h:267

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231)

struct msi\_vector msi\_vector\_t

**Definition** msi.h:60

[types.h](include_2zephyr_2types_8h.md)

[msi.h](msi_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[pcie\_ctrl\_config](structpcie__ctrl__config.md)

Structure describing a device that supports the PCI Express Controller API.

**Definition** controller.h:323

[pcie\_ctrl\_config::ranges](structpcie__ctrl__config.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)

struct pcie\_ctrl\_config::@233346376111331064333012004165050322010071233050 ranges[]

[pcie\_ctrl\_config::cfg\_addr](structpcie__ctrl__config.md#a3de0f32aaf3ddb377897974dfdfe67bd)

uintptr\_t cfg\_addr

**Definition** controller.h:328

[pcie\_ctrl\_config::pcie\_bus\_addr](structpcie__ctrl__config.md#a45f9fa1124aa64bbfd7ff2c5519cbb4b)

uintptr\_t pcie\_bus\_addr

**Definition** controller.h:338

[pcie\_ctrl\_config::ranges\_count](structpcie__ctrl__config.md#a4a620f03546490b65ba4d097329928e8)

size\_t ranges\_count

**Definition** controller.h:332

[pcie\_ctrl\_config::flags](structpcie__ctrl__config.md#a90e48aaca78a8284caa449ee3972d87b)

uint32\_t flags

**Definition** controller.h:336

[pcie\_ctrl\_config::host\_map\_addr](structpcie__ctrl__config.md#ace0b3505edc0aff3678a91b630244963)

uintptr\_t host\_map\_addr

**Definition** controller.h:340

[pcie\_ctrl\_config::cfg\_size](structpcie__ctrl__config.md#adb1b8ed76f3f994f2da72c8e8b40d4f0)

size\_t cfg\_size

**Definition** controller.h:330

[pcie\_ctrl\_config::map\_length](structpcie__ctrl__config.md#ae3dd8d3d72a1597ee135b49e46e31bec)

size\_t map\_length

**Definition** controller.h:342

[pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md)

Structure providing callbacks to be implemented for devices that supports the PCI Express Controller ...

**Definition** controller.h:174

[pcie\_ctrl\_driver\_api::conf\_read](structpcie__ctrl__driver__api.md#a20c1faf02c71e88da165c889550a76ae)

pcie\_ctrl\_conf\_read\_t conf\_read

**Definition** controller.h:175

[pcie\_ctrl\_driver\_api::region\_allocate](structpcie__ctrl__driver__api.md#a46191bf9aad7ab7ac1319918873b8b29)

pcie\_ctrl\_region\_allocate\_t region\_allocate

**Definition** controller.h:177

[pcie\_ctrl\_driver\_api::conf\_write](structpcie__ctrl__driver__api.md#a46fa0fd3a759fe2dc960546b49c53979)

pcie\_ctrl\_conf\_write\_t conf\_write

**Definition** controller.h:176

[pcie\_ctrl\_driver\_api::region\_get\_allocate\_base](structpcie__ctrl__driver__api.md#a5d7687cd738bd86a785fc281781d2759)

pcie\_ctrl\_region\_get\_allocate\_base\_t region\_get\_allocate\_base

**Definition** controller.h:178

[pcie\_ctrl\_driver\_api::region\_translate](structpcie__ctrl__driver__api.md#a71a4d13492bb3098bdb2c0e0ff7b94cf)

pcie\_ctrl\_region\_translate\_t region\_translate

**Definition** controller.h:179

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [controller.h](drivers_2pcie_2controller_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
