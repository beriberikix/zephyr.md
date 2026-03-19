---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xtensa_2mpu_8h_source.html
original_path: doxygen/html/xtensa_2mpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpu.h

[Go to the documentation of this file.](xtensa_2mpu_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[stdint.h](stdint_8h.md)>

8

9#include <[zephyr/toolchain.h](toolchain_8h.md)>

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11

12#include <xtensa/config/core-isa.h>

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MPU\_H

15#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MPU\_H

16

22

[ 24](group__xtensa__mpu__apis.md#gae63365117939d9460202c55cf006cb7a)#define XTENSA\_MPU\_NUM\_ENTRIES XCHAL\_MPU\_ENTRIES

25

33

[ 35](group__xtensa__mpu__apis.md#gaf961b245ca7818f754c7162319efa197)#define XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA (0)

36

[ 38](group__xtensa__mpu__apis.md#gaf323d5434ff922f485fe80a86c2c1b44)#define XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA (2)

39

[ 41](group__xtensa__mpu__apis.md#ga6d73b17148096bf132eda0083d1ea924)#define XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X (3)

42

[ 44](group__xtensa__mpu__apis.md#ga164fd2142e9804ef65dda8930f6fc849)#define XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA (4)

45

[ 47](group__xtensa__mpu__apis.md#ga8de59e1ff974516355606efde2e00fb9)#define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA (5)

48

[ 50](group__xtensa__mpu__apis.md#ga04d4edd823a1ace779c3f1f036c2f2e2)#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA (6)

51

[ 53](group__xtensa__mpu__apis.md#gaf00699a52e155c8b22aabf979e020109)#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA (7)

54

[ 56](group__xtensa__mpu__apis.md#ga2c10985c0c74a2690e9f093d5815d9d9)#define XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO (8)

57

[ 59](group__xtensa__mpu__apis.md#ga7fa9272228eb0ffc7455cfc671a23459)#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX (9)

60

[ 62](group__xtensa__mpu__apis.md#ga42641dfd4809bd38ef6ace8d757f9e24)#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO (10)

63

[ 65](group__xtensa__mpu__apis.md#ga1abe9e7d4f8929518b8287619ea5754d)#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX (11)

66

[ 68](group__xtensa__mpu__apis.md#ga840b2bd13d49212c3334d7137523f16c)#define XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO (12)

69

[ 71](group__xtensa__mpu__apis.md#gae47e13ff73f39d819b97f311a7f53dcd)#define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX (13)

72

[ 74](group__xtensa__mpu__apis.md#ga4cce80414ae35dc45260c6a5e5dc4582)#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW (14)

75

[ 77](group__xtensa__mpu__apis.md#ga41a662ee819f702fc9030ee7f40dbbe6)#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX (15)

78

82

[ 89](structxtensa__mpu__entry.md)struct [xtensa\_mpu\_entry](structxtensa__mpu__entry.md) {

95 union {

[ 97](structxtensa__mpu__entry.md#a77dc5a2d8512fca38c9c305b722556f5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw](structxtensa__mpu__entry.md#a77dc5a2d8512fca38c9c305b722556f5);

98

100 struct {

[ 107](structxtensa__mpu__entry.md#af18d88c18df4dfb17ceb78c560bd2e61) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enable](structxtensa__mpu__entry.md#af18d88c18df4dfb17ceb78c560bd2e61):1;

108

[ 121](structxtensa__mpu__entry.md#a9dbb164dd9e942b0d2e91621724d81ae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lock](structxtensa__mpu__entry.md#a9dbb164dd9e942b0d2e91621724d81ae):1;

122

[ 124](structxtensa__mpu__entry.md#a09cb878dd936700c64c8d2df10b58ed4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbz](structxtensa__mpu__entry.md#a09cb878dd936700c64c8d2df10b58ed4):3;

125

[ 132](structxtensa__mpu__entry.md#ada352b7ede662f57bb162e5df1f819bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start\_addr](structxtensa__mpu__entry.md#ada352b7ede662f57bb162e5df1f819bd):27;

[ 133](structxtensa__mpu__entry.md#a32bfc370b92a904abe8fe522afb9a813) } [p](structxtensa__mpu__entry.md#a32bfc370b92a904abe8fe522afb9a813);

[ 134](structxtensa__mpu__entry.md#a359f3d970a15c764d5b5cc3ac00b87c0) } [as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4);

135

141 union {

143 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw](structxtensa__mpu__entry.md#a77dc5a2d8512fca38c9c305b722556f5);

144

146 struct {

[ 148](structxtensa__mpu__entry.md#a26879b4bb6ec5c2040a864a1286b177f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [segment](structxtensa__mpu__entry.md#a26879b4bb6ec5c2040a864a1286b177f):5;

149

[ 151](structxtensa__mpu__entry.md#a0461da13881e2cde2a8607783073eeec) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbz1](structxtensa__mpu__entry.md#a0461da13881e2cde2a8607783073eeec):3;

152

[ 161](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041):4;

162

[ 175](structxtensa__mpu__entry.md#a1b9764368a50f0674ede7bc3450485c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [memory\_type](structxtensa__mpu__entry.md#a1b9764368a50f0674ede7bc3450485c7):9;

176

[ 178](structxtensa__mpu__entry.md#af4bb525147d4ba54bf46c626b3c0a888) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbz2](structxtensa__mpu__entry.md#af4bb525147d4ba54bf46c626b3c0a888):11;

[ 179](structxtensa__mpu__entry.md#a9fa96af81c4af48faa1084cdde720ca9) } [p](structxtensa__mpu__entry.md#a32bfc370b92a904abe8fe522afb9a813);

[ 180](structxtensa__mpu__entry.md#a5c41f0a0db9f71e774989dfdc5f05475) } [at](structxtensa__mpu__entry.md#a5c41f0a0db9f71e774989dfdc5f05475);

181};

182

[ 186](structxtensa__mpu__map.md)struct [xtensa\_mpu\_map](structxtensa__mpu__map.md) {

[ 190](structxtensa__mpu__map.md#ad122955b669b9834620dab88062435e1) struct [xtensa\_mpu\_entry](structxtensa__mpu__entry.md) [entries](structxtensa__mpu__map.md#ad122955b669b9834620dab88062435e1)[[XTENSA\_MPU\_NUM\_ENTRIES](group__xtensa__mpu__apis.md#gae63365117939d9460202c55cf006cb7a)];

191};

192

197

198typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

199

[ 200](group__xtensa__mpu__apis.md#gab1af4356d315b9db663cd11d65a66a91)static inline bool [xtensa\_mem\_partition\_is\_executable](group__xtensa__mpu__apis.md#gab1af4356d315b9db663cd11d65a66a91)([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) [access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041))

201{

202 bool is\_exec;

203

204 switch ([access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041)) {

205 case [XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA](group__xtensa__mpu__apis.md#gaf323d5434ff922f485fe80a86c2c1b44):

206 case [XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X](group__xtensa__mpu__apis.md#ga6d73b17148096bf132eda0083d1ea924):

207 case [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA](group__xtensa__mpu__apis.md#ga8de59e1ff974516355606efde2e00fb9):

208 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA](group__xtensa__mpu__apis.md#gaf00699a52e155c8b22aabf979e020109):

209 case [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX](group__xtensa__mpu__apis.md#ga7fa9272228eb0ffc7455cfc671a23459):

210 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX](group__xtensa__mpu__apis.md#ga1abe9e7d4f8929518b8287619ea5754d):

211 case [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](group__xtensa__mpu__apis.md#gae47e13ff73f39d819b97f311a7f53dcd):

212 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX](group__xtensa__mpu__apis.md#ga41a662ee819f702fc9030ee7f40dbbe6):

213 is\_exec = true;

214 break;

215 default:

216 is\_exec = false;

217 break;

218 };

219

220 return is\_exec;

221}

222

[ 223](group__xtensa__mpu__apis.md#ga41efdfe8839c52b3f2c1aec03c17e59a)static inline bool [xtensa\_mem\_partition\_is\_writable](group__xtensa__mpu__apis.md#ga41efdfe8839c52b3f2c1aec03c17e59a)([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) [access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041))

224{

225 bool is\_writable;

226

227 switch ([access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041)) {

228 case [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](group__xtensa__mpu__apis.md#ga04d4edd823a1ace779c3f1f036c2f2e2):

229 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA](group__xtensa__mpu__apis.md#gaf00699a52e155c8b22aabf979e020109):

230 case [XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO](group__xtensa__mpu__apis.md#ga2c10985c0c74a2690e9f093d5815d9d9):

231 case [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX](group__xtensa__mpu__apis.md#ga7fa9272228eb0ffc7455cfc671a23459):

232 case [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO](group__xtensa__mpu__apis.md#ga42641dfd4809bd38ef6ace8d757f9e24):

233 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX](group__xtensa__mpu__apis.md#ga1abe9e7d4f8929518b8287619ea5754d):

234 case [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](group__xtensa__mpu__apis.md#ga4cce80414ae35dc45260c6a5e5dc4582):

235 case [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX](group__xtensa__mpu__apis.md#ga41a662ee819f702fc9030ee7f40dbbe6):

236 is\_writable = true;

237 break;

238 default:

239 is\_writable = false;

240 break;

241 };

242

243 return is\_writable;

244}

245

[ 246](group__xtensa__mpu__apis.md#gac8344e8346f95abf209a1bce32ab554f)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(access\_rights) \

247 (xtensa\_mem\_partition\_is\_executable(access\_rights))

248

[ 249](group__xtensa__mpu__apis.md#ga3e98c2a69d6a44b0c0a7f1f71b7053e8)#define K\_MEM\_PARTITION\_IS\_WRITABLE(access\_rights) \

250 (xtensa\_mem\_partition\_is\_writable(access\_rights))

251

252/\* Read-Write access permission attributes \*/

[ 253](group__xtensa__mpu__apis.md#ga9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW \

254 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW})

[ 255](group__xtensa__mpu__apis.md#ga3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA \

256 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA})

[ 257](group__xtensa__mpu__apis.md#ga708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO \

258 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO})

[ 259](group__xtensa__mpu__apis.md#ga706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA \

260 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA})

[ 261](group__xtensa__mpu__apis.md#ga73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA \

262 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA})

263

264/\* Execution-allowed attributes \*/

[ 265](group__xtensa__mpu__apis.md#ga78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX \

266 ((k\_mem\_partition\_attr\_t) {XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX})

267

271

[ 275](structxtensa__mpu__range.md)struct [xtensa\_mpu\_range](structxtensa__mpu__range.md) {

[ 277](structxtensa__mpu__range.md#a3b24cd5cc1e5674193e7c1c20db2e66c) const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [start](structxtensa__mpu__range.md#a3b24cd5cc1e5674193e7c1c20db2e66c);

278

[ 284](structxtensa__mpu__range.md#a52444106e5fb335079ca1ed5428b1711) const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [end](structxtensa__mpu__range.md#a52444106e5fb335079ca1ed5428b1711);

285

[ 287](structxtensa__mpu__range.md#a21f446bdde0d194d3d4012342e49d151) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [access\_rights](structxtensa__mpu__range.md#a21f446bdde0d194d3d4012342e49d151):4;

288

[ 296](structxtensa__mpu__range.md#a98cbc6ec1cb0b3440e8d58e12020cd1e) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [memory\_type](structxtensa__mpu__range.md#a98cbc6ec1cb0b3440e8d58e12020cd1e):9;

297} \_\_packed;

298

306extern const struct [xtensa\_mpu\_range](structxtensa__mpu__range.md) [xtensa\_soc\_mpu\_ranges](group__xtensa__mpu__apis.md#gade19640c9ba5da25451b9200b4e9178b)[];

307

313extern const int [xtensa\_soc\_mpu\_ranges\_num](group__xtensa__mpu__apis.md#ga4b838edd5ce1332432083bd20ca7abc1);

314

[ 320](group__xtensa__mpu__apis.md#ga20524255a2b4713eddb70b8a54357771)void [xtensa\_mpu\_init](group__xtensa__mpu__apis.md#ga20524255a2b4713eddb70b8a54357771)(void);

321

325

326#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MPU\_H \*/

[as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4)

irp nz macro MOVR cc s mov cc s endm endr irp as

**Definition** asm-macro-32-bit-gnu.h:16

[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](group__xtensa__mpu__apis.md#ga04d4edd823a1ace779c3f1f036c2f2e2)

#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA

Kernel mode read and write.

**Definition** mpu.h:50

[XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX](group__xtensa__mpu__apis.md#ga1abe9e7d4f8929518b8287619ea5754d)

#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX

Kernel mode read, write and execution.

**Definition** mpu.h:65

[xtensa\_mpu\_init](group__xtensa__mpu__apis.md#ga20524255a2b4713eddb70b8a54357771)

void xtensa\_mpu\_init(void)

Initialize hardware MPU.

[XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO](group__xtensa__mpu__apis.md#ga2c10985c0c74a2690e9f093d5815d9d9)

#define XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO

Kernel and user modes write only.

**Definition** mpu.h:56

[XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX](group__xtensa__mpu__apis.md#ga41a662ee819f702fc9030ee7f40dbbe6)

#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX

Kernel and user modes read, write and execution.

**Definition** mpu.h:77

[xtensa\_mem\_partition\_is\_writable](group__xtensa__mpu__apis.md#ga41efdfe8839c52b3f2c1aec03c17e59a)

static bool xtensa\_mem\_partition\_is\_writable(k\_mem\_partition\_attr\_t access\_rights)

**Definition** mpu.h:223

[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO](group__xtensa__mpu__apis.md#ga42641dfd4809bd38ef6ace8d757f9e24)

#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO

Kernel mode read and write.

**Definition** mpu.h:62

[xtensa\_soc\_mpu\_ranges\_num](group__xtensa__mpu__apis.md#ga4b838edd5ce1332432083bd20ca7abc1)

const int xtensa\_soc\_mpu\_ranges\_num

Number of SoC additional memory regions.

[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](group__xtensa__mpu__apis.md#ga4cce80414ae35dc45260c6a5e5dc4582)

#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW

Kernel and user modes read and write.

**Definition** mpu.h:74

[XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X](group__xtensa__mpu__apis.md#ga6d73b17148096bf132eda0083d1ea924)

#define XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X

User mode execution only.

**Definition** mpu.h:41

[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX](group__xtensa__mpu__apis.md#ga7fa9272228eb0ffc7455cfc671a23459)

#define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX

Kernel mode read, write.

**Definition** mpu.h:59

[XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA](group__xtensa__mpu__apis.md#ga8de59e1ff974516355606efde2e00fb9)

#define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA

Kernel mode read and execution.

**Definition** mpu.h:47

[xtensa\_mem\_partition\_is\_executable](group__xtensa__mpu__apis.md#gab1af4356d315b9db663cd11d65a66a91)

static bool xtensa\_mem\_partition\_is\_executable(k\_mem\_partition\_attr\_t access\_rights)

**Definition** mpu.h:200

[xtensa\_soc\_mpu\_ranges](group__xtensa__mpu__apis.md#gade19640c9ba5da25451b9200b4e9178b)

const struct xtensa\_mpu\_range xtensa\_soc\_mpu\_ranges[]

Additional memory regions required by SoC.

[XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](group__xtensa__mpu__apis.md#gae47e13ff73f39d819b97f311a7f53dcd)

#define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX

Kernel and user modes read and execution.

**Definition** mpu.h:71

[XTENSA\_MPU\_NUM\_ENTRIES](group__xtensa__mpu__apis.md#gae63365117939d9460202c55cf006cb7a)

#define XTENSA\_MPU\_NUM\_ENTRIES

Number of available entries in the MPU table.

**Definition** mpu.h:24

[XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA](group__xtensa__mpu__apis.md#gaf00699a52e155c8b22aabf979e020109)

#define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA

Kernel mode read, write and execution.

**Definition** mpu.h:53

[XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA](group__xtensa__mpu__apis.md#gaf323d5434ff922f485fe80a86c2c1b44)

#define XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA

Kernel mode execution only.

**Definition** mpu.h:38

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[xtensa\_mpu\_entry](structxtensa__mpu__entry.md)

Foreground MPU Entry.

**Definition** mpu.h:89

[xtensa\_mpu\_entry::mbz1](structxtensa__mpu__entry.md#a0461da13881e2cde2a8607783073eeec)

uint32\_t mbz1

Must be zero (part 1).

**Definition** mpu.h:151

[xtensa\_mpu\_entry::mbz](structxtensa__mpu__entry.md#a09cb878dd936700c64c8d2df10b58ed4)

uint32\_t mbz

Must be zero.

**Definition** mpu.h:124

[xtensa\_mpu\_entry::memory\_type](structxtensa__mpu__entry.md#a1b9764368a50f0674ede7bc3450485c7)

uint32\_t memory\_type

Memory type associated with this MPU entry.

**Definition** mpu.h:175

[xtensa\_mpu\_entry::segment](structxtensa__mpu__entry.md#a26879b4bb6ec5c2040a864a1286b177f)

uint32\_t segment

The segment number of this MPU entry.

**Definition** mpu.h:148

[xtensa\_mpu\_entry::p](structxtensa__mpu__entry.md#a32bfc370b92a904abe8fe522afb9a813)

struct xtensa\_mpu\_entry::@016220364341304274203162046237341155201117266112::@004306361155216153354074146254203312314116117105 p

Individual parts.

[xtensa\_mpu\_entry::at](structxtensa__mpu__entry.md#a5c41f0a0db9f71e774989dfdc5f05475)

union xtensa\_mpu\_entry::@071272107232174032153354124133042007263354012331 at

Content of at register for WPTLB.

[xtensa\_mpu\_entry::raw](structxtensa__mpu__entry.md#a77dc5a2d8512fca38c9c305b722556f5)

uint32\_t raw

Raw value.

**Definition** mpu.h:97

[xtensa\_mpu\_entry::lock](structxtensa__mpu__entry.md#a9dbb164dd9e942b0d2e91621724d81ae)

uint32\_t lock

Lock bit for this entry.

**Definition** mpu.h:121

[xtensa\_mpu\_entry::access\_rights](structxtensa__mpu__entry.md#ab4a226d6c492a1fea3e2e4806ea6f041)

uint32\_t access\_rights

Access rights associated with this MPU entry.

**Definition** mpu.h:161

[xtensa\_mpu\_entry::start\_addr](structxtensa__mpu__entry.md#ada352b7ede662f57bb162e5df1f819bd)

uint32\_t start\_addr

Start address of this MPU entry.

**Definition** mpu.h:132

[xtensa\_mpu\_entry::enable](structxtensa__mpu__entry.md#af18d88c18df4dfb17ceb78c560bd2e61)

uint32\_t enable

Enable bit for this entry.

**Definition** mpu.h:107

[xtensa\_mpu\_entry::mbz2](structxtensa__mpu__entry.md#af4bb525147d4ba54bf46c626b3c0a888)

uint32\_t mbz2

Must be zero (part 2).

**Definition** mpu.h:178

[xtensa\_mpu\_map](structxtensa__mpu__map.md)

Struct to hold foreground MPU map and its entries.

**Definition** mpu.h:186

[xtensa\_mpu\_map::entries](structxtensa__mpu__map.md#ad122955b669b9834620dab88062435e1)

struct xtensa\_mpu\_entry entries[XCHAL\_MPU\_ENTRIES]

Array of MPU entries.

**Definition** mpu.h:190

[xtensa\_mpu\_range](structxtensa__mpu__range.md)

Struct to describe a memory region [start, end).

**Definition** mpu.h:275

[xtensa\_mpu\_range::access\_rights](structxtensa__mpu__range.md#a21f446bdde0d194d3d4012342e49d151)

const uint8\_t access\_rights

Access rights for the memory region.

**Definition** mpu.h:287

[xtensa\_mpu\_range::start](structxtensa__mpu__range.md#a3b24cd5cc1e5674193e7c1c20db2e66c)

const uintptr\_t start

Start address (inclusive) of the memory region.

**Definition** mpu.h:277

[xtensa\_mpu\_range::end](structxtensa__mpu__range.md#a52444106e5fb335079ca1ed5428b1711)

const uintptr\_t end

End address (exclusive) of the memory region.

**Definition** mpu.h:284

[xtensa\_mpu\_range::memory\_type](structxtensa__mpu__range.md#a98cbc6ec1cb0b3440e8d58e12020cd1e)

const uint16\_t memory\_type

Memory type for the region.

**Definition** mpu.h:296

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [mpu.h](xtensa_2mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
