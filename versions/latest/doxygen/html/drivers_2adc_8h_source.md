---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2adc_8h_source.html
original_path: doxygen/html/drivers_2adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc.h

[Go to the documentation of this file.](drivers_2adc_8h.md)

1

5

6/\*

7 \* Copyright (c) 2018 Nordic Semiconductor ASA

8 \* Copyright (c) 2015 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/dt-bindings/adc/adc.h](dt-bindings_2adc_2adc_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

32

[ 34](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0)enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) {

[ 35](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1) [ADC\_GAIN\_1\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1),

[ 36](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9) [ADC\_GAIN\_1\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9),

[ 37](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8) [ADC\_GAIN\_1\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8),

[ 38](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a30cf06d8c6d323a8bfef3a508f2c3388) [ADC\_GAIN\_2\_7](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a30cf06d8c6d323a8bfef3a508f2c3388),

[ 39](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee) [ADC\_GAIN\_1\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee),

[ 40](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0) [ADC\_GAIN\_2\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0),

[ 41](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2) [ADC\_GAIN\_1\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2),

[ 42](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62) [ADC\_GAIN\_2\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62),

[ 43](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df) [ADC\_GAIN\_4\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df),

[ 44](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54) [ADC\_GAIN\_1](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54),

[ 45](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868) [ADC\_GAIN\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868),

[ 46](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e) [ADC\_GAIN\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e),

[ 47](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300) [ADC\_GAIN\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300),

[ 48](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8) [ADC\_GAIN\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8),

[ 49](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3) [ADC\_GAIN\_8](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3),

[ 50](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8) [ADC\_GAIN\_12](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8),

[ 51](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970) [ADC\_GAIN\_16](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970),

[ 52](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33) [ADC\_GAIN\_24](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33),

[ 53](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f) [ADC\_GAIN\_32](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f),

[ 54](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb) [ADC\_GAIN\_64](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb),

[ 55](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829) [ADC\_GAIN\_128](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829),

56};

57

[ 74](group__adc__interface.md#ga5af65795f58e8e92672bf31dc2418e23)int [adc\_gain\_invert](group__adc__interface.md#ga5af65795f58e8e92672bf31dc2418e23)(enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

75

[ 92](group__adc__interface.md#ga252581edcc0c516108260169d797c02f)int [adc\_gain\_invert\_64](group__adc__interface.md#ga252581edcc0c516108260169d797c02f)(enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value);

93

[ 95](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56)enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) {

[ 96](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3) [ADC\_REF\_VDD\_1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3),

[ 97](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d) [ADC\_REF\_VDD\_1\_2](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d),

[ 98](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1) [ADC\_REF\_VDD\_1\_3](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1),

[ 99](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c) [ADC\_REF\_VDD\_1\_4](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c),

[ 100](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) [ADC\_REF\_INTERNAL](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709),

[ 101](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6) [ADC\_REF\_EXTERNAL0](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6),

[ 102](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a) [ADC\_REF\_EXTERNAL1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a),

103};

104

[ 108](structadc__channel__cfg.md)struct [adc\_channel\_cfg](structadc__channel__cfg.md) {

[ 110](structadc__channel__cfg.md#a20996396fa5b1d27eeea7da9ea9df848) enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) [gain](structadc__channel__cfg.md#a20996396fa5b1d27eeea7da9ea9df848);

111

[ 113](structadc__channel__cfg.md#a73d11ad6411a62f8f21cbfa492bc1b20) enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) [reference](structadc__channel__cfg.md#a73d11ad6411a62f8f21cbfa492bc1b20);

114

[ 124](structadc__channel__cfg.md#a426a74cf53a4b801e91c2eeb1db3477d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acquisition\_time](structadc__channel__cfg.md#a426a74cf53a4b801e91c2eeb1db3477d);

125

[ 148](structadc__channel__cfg.md#aeec90a3fb60f93427a92e083326c8fcf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_id](structadc__channel__cfg.md#aeec90a3fb60f93427a92e083326c8fcf) : 5;

149

[ 151](structadc__channel__cfg.md#a372f298a2dd87660b9508ca1387084b6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [differential](structadc__channel__cfg.md#a372f298a2dd87660b9508ca1387084b6) : 1;

152

153#ifdef CONFIG\_ADC\_CONFIGURABLE\_INPUTS

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_positive;

160

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_negative;

167#endif /\* CONFIG\_ADC\_CONFIGURABLE\_INPUTS \*/

168

169#ifdef CONFIG\_ADC\_CONFIGURABLE\_EXCITATION\_CURRENT\_SOURCE\_PIN

170 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) current\_source\_pin\_set : 1;

177 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) current\_source\_pin[2];

178#endif /\* CONFIG\_ADC\_CONFIGURABLE\_EXCITATION\_CURRENT\_SOURCE\_PIN \*/

179

180#ifdef CONFIG\_ADC\_CONFIGURABLE\_VBIAS\_PIN

189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vbias\_pins;

190#endif /\* CONFIG\_ADC\_CONFIGURABLE\_VBIAS\_PIN \*/

191};

192

[ 257](group__adc__interface.md#ga8d1f7d55c94fed3247c830a4569ab05e)#define ADC\_CHANNEL\_CFG\_DT(node\_id) { \

258 .gain = DT\_STRING\_TOKEN(node\_id, zephyr\_gain), \

259 .reference = DT\_STRING\_TOKEN(node\_id, zephyr\_reference), \

260 .acquisition\_time = DT\_PROP(node\_id, zephyr\_acquisition\_time), \

261 .channel\_id = DT\_REG\_ADDR(node\_id), \

262IF\_ENABLED(UTIL\_OR(DT\_PROP(node\_id, zephyr\_differential), \

263 UTIL\_AND(CONFIG\_ADC\_CONFIGURABLE\_INPUTS, \

264 DT\_NODE\_HAS\_PROP(node\_id, zephyr\_input\_negative))), \

265 (.differential = true,)) \

266IF\_ENABLED(CONFIG\_ADC\_CONFIGURABLE\_INPUTS, \

267 (.input\_positive = DT\_PROP\_OR(node\_id, zephyr\_input\_positive, 0), \

268 .input\_negative = DT\_PROP\_OR(node\_id, zephyr\_input\_negative, 0),)) \

269IF\_ENABLED(CONFIG\_ADC\_CONFIGURABLE\_EXCITATION\_CURRENT\_SOURCE\_PIN, \

270 (.current\_source\_pin\_set = DT\_NODE\_HAS\_PROP(node\_id, zephyr\_current\_source\_pin), \

271 .current\_source\_pin = DT\_PROP\_OR(node\_id, zephyr\_current\_source\_pin, {0}),)) \

272IF\_ENABLED(CONFIG\_ADC\_CONFIGURABLE\_VBIAS\_PIN, \

273 (.vbias\_pins = DT\_PROP\_OR(node\_id, zephyr\_vbias\_pins, 0),)) \

274}

275

[ 282](structadc__dt__spec.md)struct [adc\_dt\_spec](structadc__dt__spec.md) {

[ 287](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44) const struct [device](structdevice.md) \*[dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44);

288

[ 290](structadc__dt__spec.md#a083e6c5bc707606c2ea1459fb58e29a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_id](structadc__dt__spec.md#a083e6c5bc707606c2ea1459fb58e29a8);

291

[ 297](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612) bool [channel\_cfg\_dt\_node\_exists](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612);

298

[ 304](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d) struct [adc\_channel\_cfg](structadc__channel__cfg.md) [channel\_cfg](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d);

305

[ 312](structadc__dt__spec.md#a9e120f52e3a905768d8e6bdc3469d20a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vref\_mv](structadc__dt__spec.md#a9e120f52e3a905768d8e6bdc3469d20a);

313

[ 319](structadc__dt__spec.md#abbe7052a144541b8d16afee3fd231c10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resolution](structadc__dt__spec.md#abbe7052a144541b8d16afee3fd231c10);

320

[ 326](structadc__dt__spec.md#aa7daf451a3438847ff989f32eae11e97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oversampling](structadc__dt__spec.md#aa7daf451a3438847ff989f32eae11e97);

327};

328

330

331#define ADC\_DT\_SPEC\_STRUCT(ctlr, input) { \

332 .dev = DEVICE\_DT\_GET(ctlr), \

333 .channel\_id = input, \

334 ADC\_CHANNEL\_CFG\_FROM\_DT\_NODE(\

335 ADC\_CHANNEL\_DT\_NODE(ctlr, input)) \

336 }

337

338#define ADC\_CHANNEL\_DT\_NODE(ctlr, input) \

339 DT\_FOREACH\_CHILD\_VARGS(ctlr, ADC\_FOREACH\_INPUT, input)

340

341#define ADC\_FOREACH\_INPUT(node, input) \

342 IF\_ENABLED(IS\_EQ(DT\_REG\_ADDR\_RAW(node), input), (node))

343

344#define ADC\_CHANNEL\_CFG\_FROM\_DT\_NODE(node\_id) \

345 IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

346 (.channel\_cfg\_dt\_node\_exists = true, \

347 .channel\_cfg = ADC\_CHANNEL\_CFG\_DT(node\_id), \

348 .vref\_mv = DT\_PROP\_OR(node\_id, zephyr\_vref\_mv, 0), \

349 .resolution = DT\_PROP\_OR(node\_id, zephyr\_resolution, 0), \

350 .oversampling = DT\_PROP\_OR(node\_id, zephyr\_oversampling, 0),))

351

353

[ 422](group__adc__interface.md#ga058dbc619b7bbf624cd48518b429bb58)#define ADC\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name) \

423 ADC\_DT\_SPEC\_STRUCT(DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(node\_id, name), \

424 DT\_IO\_CHANNELS\_INPUT\_BY\_NAME(node\_id, name))

425

[ 436](group__adc__interface.md#ga48139728bd2cec25208ef37d9bbcc34f)#define ADC\_DT\_SPEC\_INST\_GET\_BY\_NAME(inst, name) \

437 ADC\_DT\_SPEC\_GET\_BY\_NAME(DT\_DRV\_INST(inst), name)

438

[ 508](group__adc__interface.md#gae9867df7a034d45ed3d3c58c69c246ed)#define ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx) \

509 ADC\_DT\_SPEC\_STRUCT(DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, idx), \

510 DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, idx))

511

[ 522](group__adc__interface.md#ga4705a1e2cc22fe73b7e967e8ba220584)#define ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx) \

523 ADC\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

524

[ 534](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)#define ADC\_DT\_SPEC\_GET(node\_id) ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)

535

[ 544](group__adc__interface.md#ga96222a7d374e21d477b99f74d715bae1)#define ADC\_DT\_SPEC\_INST\_GET(inst) ADC\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

545

546/\* Forward declaration of the adc\_sequence structure. \*/

547struct [adc\_sequence](structadc__sequence.md);

548

[ 552](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917)enum [adc\_action](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917) {

[ 554](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917ac875a64d997cb883b49447006554ba92) [ADC\_ACTION\_CONTINUE](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917ac875a64d997cb883b49447006554ba92) = 0,

555

[ 560](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715) [ADC\_ACTION\_REPEAT](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715),

561

[ 563](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9) [ADC\_ACTION\_FINISH](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9),

564};

565

585typedef enum [adc\_action](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917) (\*[adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d))(const struct [device](structdevice.md) \*dev,

586 const struct [adc\_sequence](structadc__sequence.md) \*sequence,

587 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sampling\_index);

588

[ 592](structadc__sequence__options.md)struct [adc\_sequence\_options](structadc__sequence__options.md) {

[ 602](structadc__sequence__options.md#ad2f11727ab0eb7e32a5fbd07f04a85b2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_us](structadc__sequence__options.md#ad2f11727ab0eb7e32a5fbd07f04a85b2);

603

[ 608](structadc__sequence__options.md#a71bd082c14f01a1b5d1b491e7510aa91) [adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d) [callback](structadc__sequence__options.md#a71bd082c14f01a1b5d1b491e7510aa91);

609

[ 614](structadc__sequence__options.md#a262fd6daefb22df02c726aafcddc6d47) void \*[user\_data](structadc__sequence__options.md#a262fd6daefb22df02c726aafcddc6d47);

615

[ 620](structadc__sequence__options.md#a29f8ac4cdf6740f56bcd70a0a027e56a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [extra\_samplings](structadc__sequence__options.md#a29f8ac4cdf6740f56bcd70a0a027e56a);

621};

622

[ 626](structadc__sequence.md)struct [adc\_sequence](structadc__sequence.md) {

[ 631](structadc__sequence.md#a379c6f92153dfa97439d39cbef222451) const struct [adc\_sequence\_options](structadc__sequence__options.md) \*[options](structadc__sequence.md#a379c6f92153dfa97439d39cbef222451);

632

[ 640](structadc__sequence.md#a5c497c4a5de20e8591063ca8661f79c1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channels](structadc__sequence.md#a5c497c4a5de20e8591063ca8661f79c1);

641

[ 653](structadc__sequence.md#a5df0ee0e6d3215aa052f108476bd57ec) void \*[buffer](structadc__sequence.md#a5df0ee0e6d3215aa052f108476bd57ec);

654

[ 661](structadc__sequence.md#a8e1bc9a4361e274bbdaedeb3151b71e5) size\_t [buffer\_size](structadc__sequence.md#a8e1bc9a4361e274bbdaedeb3151b71e5);

662

[ 670](structadc__sequence.md#ad5480691be25ed9ee81130b775743125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resolution](structadc__sequence.md#ad5480691be25ed9ee81130b775743125);

671

[ 678](structadc__sequence.md#a233e8b20b57bb2fdbebf2c85f076c802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oversampling](structadc__sequence.md#a233e8b20b57bb2fdbebf2c85f076c802);

679

[ 688](structadc__sequence.md#a6023e3bec29deaa11b44c4df40eb7b04) bool [calibrate](structadc__sequence.md#a6023e3bec29deaa11b44c4df40eb7b04);

689};

690

691

[ 696](group__adc__interface.md#ga871680cf9f390bfe19a10a61eb1ca092)typedef int (\*[adc\_api\_channel\_setup](group__adc__interface.md#ga871680cf9f390bfe19a10a61eb1ca092))(const struct [device](structdevice.md) \*dev,

697 const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg);

698

[ 703](group__adc__interface.md#ga4d4484e52ff7727fd316f50b2f404adf)typedef int (\*[adc\_api\_read](group__adc__interface.md#ga4d4484e52ff7727fd316f50b2f404adf))(const struct [device](structdevice.md) \*dev,

704 const struct [adc\_sequence](structadc__sequence.md) \*sequence);

705

[ 711](group__adc__interface.md#gad0160f455d1901ebfe06568e8418a22c)typedef int (\*[adc\_api\_read\_async](group__adc__interface.md#gad0160f455d1901ebfe06568e8418a22c))(const struct [device](structdevice.md) \*dev,

712 const struct [adc\_sequence](structadc__sequence.md) \*sequence,

713 struct [k\_poll\_signal](structk__poll__signal.md) \*async);

714

[ 720](structadc__driver__api.md)\_\_subsystem struct [adc\_driver\_api](structadc__driver__api.md) {

[ 721](structadc__driver__api.md#ad14fe480ff7a0c4efe78e2fcb9bf6ee2) [adc\_api\_channel\_setup](group__adc__interface.md#ga871680cf9f390bfe19a10a61eb1ca092) [channel\_setup](structadc__driver__api.md#ad14fe480ff7a0c4efe78e2fcb9bf6ee2);

[ 722](structadc__driver__api.md#a489ba3478e4d36379e591fa1a3fc425b) [adc\_api\_read](group__adc__interface.md#ga4d4484e52ff7727fd316f50b2f404adf) [read](structadc__driver__api.md#a489ba3478e4d36379e591fa1a3fc425b);

723#ifdef CONFIG\_ADC\_ASYNC

724 [adc\_api\_read\_async](group__adc__interface.md#gad0160f455d1901ebfe06568e8418a22c) read\_async;

725#endif

[ 726](structadc__driver__api.md#ad12d4f5fa0eb0e45e14553deab0edbed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ref\_internal](structadc__driver__api.md#ad12d4f5fa0eb0e45e14553deab0edbed); /\* mV \*/

727};

728

[ 741](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf)\_\_syscall int [adc\_channel\_setup](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf)(const struct [device](structdevice.md) \*dev,

742 const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg);

743

744static inline int z\_impl\_adc\_channel\_setup(const struct [device](structdevice.md) \*dev,

745 const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg)

746{

747 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(adc, dev)->channel\_setup(dev, channel\_cfg);

748}

749

[ 759](group__adc__interface.md#gaec29595ff149508847c51f14c41a5bad)static inline int [adc\_channel\_setup\_dt](group__adc__interface.md#gaec29595ff149508847c51f14c41a5bad)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec)

760{

761 if (!spec->[channel\_cfg\_dt\_node\_exists](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612)) {

762 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

763 }

764

765 return [adc\_channel\_setup](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf)(spec->[dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44), &spec->[channel\_cfg](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d));

766}

767

[ 789](group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3)\_\_syscall int [adc\_read](group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3)(const struct [device](structdevice.md) \*dev,

790 const struct [adc\_sequence](structadc__sequence.md) \*sequence);

791

792static inline int z\_impl\_adc\_read(const struct [device](structdevice.md) \*dev,

793 const struct [adc\_sequence](structadc__sequence.md) \*sequence)

794{

795 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(adc, dev)->read(dev, sequence);

796}

797

[ 807](group__adc__interface.md#ga303a57dfd56f0870c62ba203483e96aa)static inline int [adc\_read\_dt](group__adc__interface.md#ga303a57dfd56f0870c62ba203483e96aa)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec,

808 const struct [adc\_sequence](structadc__sequence.md) \*sequence)

809{

810 return [adc\_read](group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3)(spec->[dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44), sequence);

811}

812

[ 833](group__adc__interface.md#ga009e3733b5b20eb6b26a201c9f9734fc)\_\_syscall int [adc\_read\_async](group__adc__interface.md#ga009e3733b5b20eb6b26a201c9f9734fc)(const struct [device](structdevice.md) \*dev,

834 const struct [adc\_sequence](structadc__sequence.md) \*sequence,

835 struct [k\_poll\_signal](structk__poll__signal.md) \*async);

836

837

838#ifdef CONFIG\_ADC\_ASYNC

839static inline int z\_impl\_adc\_read\_async(const struct [device](structdevice.md) \*dev,

840 const struct [adc\_sequence](structadc__sequence.md) \*sequence,

841 struct [k\_poll\_signal](structk__poll__signal.md) \*async)

842{

843 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(adc, dev)->read\_async(dev, sequence, async);

844}

845#endif /\* CONFIG\_ADC\_ASYNC \*/

846

[ 856](group__adc__interface.md#gad11845f5621d0b0d03da4b6484d79aa4)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [adc\_ref\_internal](group__adc__interface.md#gad11845f5621d0b0d03da4b6484d79aa4)(const struct [device](structdevice.md) \*dev)

857{

858 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(adc, dev)->ref\_internal;

859}

860

[ 884](group__adc__interface.md#ga37d3183c11465aef0890484ffd1f5144)typedef int (\*[adc\_raw\_to\_x\_fn](group__adc__interface.md#ga37d3183c11465aef0890484ffd1f5144))([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ref\_mv, enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution,

885 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp);

886

[ 892](group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950)static inline int [adc\_raw\_to\_millivolts](group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ref\_mv, enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution,

893 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp)

894{

895 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) adc\_mv = \*valp \* ref\_mv;

896 int ret = [adc\_gain\_invert](group__adc__interface.md#ga5af65795f58e8e92672bf31dc2418e23)(gain, &adc\_mv);

897

898 if (ret == 0) {

899 \*valp = (adc\_mv >> resolution);

900 }

901

902 return ret;

903}

904

[ 910](group__adc__interface.md#ga443772e29554fb289032c3b0b7d2fe8d)static inline int [adc\_raw\_to\_microvolts](group__adc__interface.md#ga443772e29554fb289032c3b0b7d2fe8d)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ref\_mv, enum [adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution,

911 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp)

912{

913 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) adc\_uv = ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))\*valp \* ref\_mv \* 1000;

914 int ret = [adc\_gain\_invert\_64](group__adc__interface.md#ga252581edcc0c516108260169d797c02f)(gain, &adc\_uv);

915

916 if (ret == 0) {

917 \*valp = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(adc\_uv >> resolution);

918 }

919

920 return ret;

921}

922

[ 939](group__adc__interface.md#ga21f68d7f81524dc7c83289f74b86d62b)static inline int [adc\_raw\_to\_x\_dt\_chan](group__adc__interface.md#ga21f68d7f81524dc7c83289f74b86d62b)([adc\_raw\_to\_x\_fn](group__adc__interface.md#ga37d3183c11465aef0890484ffd1f5144) conv\_func,

940 const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec,

941 const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg,

942 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp)

943{

944 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) vref\_mv;

945 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution;

946

947 if (!spec->[channel\_cfg\_dt\_node\_exists](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612)) {

948 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

949 }

950

951 if (channel\_cfg->[reference](structadc__channel__cfg.md#a73d11ad6411a62f8f21cbfa492bc1b20) == [ADC\_REF\_INTERNAL](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709)) {

952 vref\_mv = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))[adc\_ref\_internal](group__adc__interface.md#gad11845f5621d0b0d03da4b6484d79aa4)(spec->[dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44));

953 } else {

954 vref\_mv = spec->[vref\_mv](structadc__dt__spec.md#a9e120f52e3a905768d8e6bdc3469d20a);

955 }

956

957 resolution = spec->[resolution](structadc__dt__spec.md#abbe7052a144541b8d16afee3fd231c10);

958

959 /\*

960 \* For differential channels, one bit less needs to be specified

961 \* for resolution to achieve correct conversion.

962 \*/

963 if (channel\_cfg->[differential](structadc__channel__cfg.md#a372f298a2dd87660b9508ca1387084b6)) {

964 resolution -= 1U;

965 }

966

967 return conv\_func(vref\_mv, channel\_cfg->[gain](structadc__channel__cfg.md#a20996396fa5b1d27eeea7da9ea9df848), resolution, valp);

968}

969

970

[ 984](group__adc__interface.md#ga11cf9c8f345a83f66704af83a2a26911)static inline int [adc\_raw\_to\_millivolts\_dt](group__adc__interface.md#ga11cf9c8f345a83f66704af83a2a26911)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp)

985{

986 return [adc\_raw\_to\_x\_dt\_chan](group__adc__interface.md#ga21f68d7f81524dc7c83289f74b86d62b)([adc\_raw\_to\_millivolts](group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950), spec, &spec->[channel\_cfg](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d), valp);

987}

988

[ 1002](group__adc__interface.md#ga47faafc73cea1828a5bc2af9d857f1b2)static inline int [adc\_raw\_to\_microvolts\_dt](group__adc__interface.md#ga47faafc73cea1828a5bc2af9d857f1b2)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp)

1003{

1004 return [adc\_raw\_to\_x\_dt\_chan](group__adc__interface.md#ga21f68d7f81524dc7c83289f74b86d62b)([adc\_raw\_to\_microvolts](group__adc__interface.md#ga443772e29554fb289032c3b0b7d2fe8d), spec, &spec->[channel\_cfg](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d), valp);

1005}

1006

[ 1025](group__adc__interface.md#ga5629d37dde5eb43faa93f4d167333f94)static inline int [adc\_sequence\_init\_dt](group__adc__interface.md#ga5629d37dde5eb43faa93f4d167333f94)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec,

1026 struct [adc\_sequence](structadc__sequence.md) \*seq)

1027{

1028 if (!spec->[channel\_cfg\_dt\_node\_exists](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612)) {

1029 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1030 }

1031

1032 seq->[channels](structadc__sequence.md#a5c497c4a5de20e8591063ca8661f79c1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(spec->[channel\_id](structadc__dt__spec.md#a083e6c5bc707606c2ea1459fb58e29a8));

1033 seq->[resolution](structadc__sequence.md#ad5480691be25ed9ee81130b775743125) = spec->[resolution](structadc__dt__spec.md#abbe7052a144541b8d16afee3fd231c10);

1034 seq->[oversampling](structadc__sequence.md#a233e8b20b57bb2fdbebf2c85f076c802) = spec->[oversampling](structadc__dt__spec.md#aa7daf451a3438847ff989f32eae11e97);

1035

1036 return 0;

1037}

1038

[ 1046](group__adc__interface.md#ga37412f10ad2c4874e4cce0d5fa8599a0)static inline bool [adc\_is\_ready\_dt](group__adc__interface.md#ga37412f10ad2c4874e4cce0d5fa8599a0)(const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec)

1047{

1048 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44));

1049}

1050

1054

1055#ifdef \_\_cplusplus

1056}

1057#endif

1058

1059#include <zephyr/syscalls/adc.h>

1060

1061#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1350

[adc.h](dt-bindings_2adc_2adc_8h.md)

[adc\_read\_async](group__adc__interface.md#ga009e3733b5b20eb6b26a201c9f9734fc)

int adc\_read\_async(const struct device \*dev, const struct adc\_sequence \*sequence, struct k\_poll\_signal \*async)

Set an asynchronous read request.

[adc\_raw\_to\_millivolts\_dt](group__adc__interface.md#ga11cf9c8f345a83f66704af83a2a26911)

static int adc\_raw\_to\_millivolts\_dt(const struct adc\_dt\_spec \*spec, int32\_t \*valp)

Convert a raw ADC value to millivolts using information stored in a struct adc\_dt\_spec.

**Definition** adc.h:984

[adc\_raw\_to\_x\_dt\_chan](group__adc__interface.md#ga21f68d7f81524dc7c83289f74b86d62b)

static int adc\_raw\_to\_x\_dt\_chan(adc\_raw\_to\_x\_fn conv\_func, const struct adc\_dt\_spec \*spec, const struct adc\_channel\_cfg \*channel\_cfg, int32\_t \*valp)

Convert a raw ADC value to an arbitrary output unit.

**Definition** adc.h:939

[adc\_gain\_invert\_64](group__adc__interface.md#ga252581edcc0c516108260169d797c02f)

int adc\_gain\_invert\_64(enum adc\_gain gain, int64\_t \*value)

Invert the application of gain to a measurement value.

[adc\_read\_dt](group__adc__interface.md#ga303a57dfd56f0870c62ba203483e96aa)

static int adc\_read\_dt(const struct adc\_dt\_spec \*spec, const struct adc\_sequence \*sequence)

Set a read request from a struct adc\_dt\_spec.

**Definition** adc.h:807

[adc\_gain](group__adc__interface.md#ga306f882323c66b263d3797124ca5f3a0)

adc\_gain

ADC channel gain factors.

**Definition** adc.h:34

[adc\_is\_ready\_dt](group__adc__interface.md#ga37412f10ad2c4874e4cce0d5fa8599a0)

static bool adc\_is\_ready\_dt(const struct adc\_dt\_spec \*spec)

Validate that the ADC device is ready.

**Definition** adc.h:1046

[adc\_raw\_to\_x\_fn](group__adc__interface.md#ga37d3183c11465aef0890484ffd1f5144)

int(\* adc\_raw\_to\_x\_fn)(int32\_t ref\_mv, enum adc\_gain gain, uint8\_t resolution, int32\_t \*valp)

Conversion from raw ADC units to a specific output unit.

**Definition** adc.h:884

[adc\_raw\_to\_microvolts](group__adc__interface.md#ga443772e29554fb289032c3b0b7d2fe8d)

static int adc\_raw\_to\_microvolts(int32\_t ref\_mv, enum adc\_gain gain, uint8\_t resolution, int32\_t \*valp)

Convert a raw ADC value to microvolts.

**Definition** adc.h:910

[adc\_raw\_to\_microvolts\_dt](group__adc__interface.md#ga47faafc73cea1828a5bc2af9d857f1b2)

static int adc\_raw\_to\_microvolts\_dt(const struct adc\_dt\_spec \*spec, int32\_t \*valp)

Convert a raw ADC value to microvolts using information stored in a struct adc\_dt\_spec.

**Definition** adc.h:1002

[adc\_api\_read](group__adc__interface.md#ga4d4484e52ff7727fd316f50b2f404adf)

int(\* adc\_api\_read)(const struct device \*dev, const struct adc\_sequence \*sequence)

Type definition of ADC API function for setting a read request.

**Definition** adc.h:703

[adc\_sequence\_init\_dt](group__adc__interface.md#ga5629d37dde5eb43faa93f4d167333f94)

static int adc\_sequence\_init\_dt(const struct adc\_dt\_spec \*spec, struct adc\_sequence \*seq)

Initialize a struct adc\_sequence from information stored in struct adc\_dt\_spec.

**Definition** adc.h:1025

[adc\_gain\_invert](group__adc__interface.md#ga5af65795f58e8e92672bf31dc2418e23)

int adc\_gain\_invert(enum adc\_gain gain, int32\_t \*value)

Invert the application of gain to a measurement value.

[adc\_read](group__adc__interface.md#ga7567ce3b03ebb294620b4e32b7561ab3)

int adc\_read(const struct device \*dev, const struct adc\_sequence \*sequence)

Set a read request.

[adc\_channel\_setup](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf)

int adc\_channel\_setup(const struct device \*dev, const struct adc\_channel\_cfg \*channel\_cfg)

Configure an ADC channel.

[adc\_api\_channel\_setup](group__adc__interface.md#ga871680cf9f390bfe19a10a61eb1ca092)

int(\* adc\_api\_channel\_setup)(const struct device \*dev, const struct adc\_channel\_cfg \*channel\_cfg)

Type definition of ADC API function for configuring a channel.

**Definition** adc.h:696

[adc\_action](group__adc__interface.md#ga8f6df993405679f852ae4cd8c63c6917)

adc\_action

Action to be performed after a sampling is done.

**Definition** adc.h:552

[adc\_sequence\_callback](group__adc__interface.md#ga9150eb6dc53d1c62b9fa225c0a371d6d)

enum adc\_action(\* adc\_sequence\_callback)(const struct device \*dev, const struct adc\_sequence \*sequence, uint16\_t sampling\_index)

Type definition of the optional callback function to be called after a requested sampling is done.

**Definition** adc.h:585

[adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56)

adc\_reference

ADC references.

**Definition** adc.h:95

[adc\_api\_read\_async](group__adc__interface.md#gad0160f455d1901ebfe06568e8418a22c)

int(\* adc\_api\_read\_async)(const struct device \*dev, const struct adc\_sequence \*sequence, struct k\_poll\_signal \*async)

Type definition of ADC API function for setting an asynchronous read request.

**Definition** adc.h:711

[adc\_ref\_internal](group__adc__interface.md#gad11845f5621d0b0d03da4b6484d79aa4)

static uint16\_t adc\_ref\_internal(const struct device \*dev)

Get the internal reference voltage.

**Definition** adc.h:856

[adc\_channel\_setup\_dt](group__adc__interface.md#gaec29595ff149508847c51f14c41a5bad)

static int adc\_channel\_setup\_dt(const struct adc\_dt\_spec \*spec)

Configure an ADC channel from a struct adc\_dt\_spec.

**Definition** adc.h:759

[adc\_raw\_to\_millivolts](group__adc__interface.md#gaef98dabea3e0dc1cef8add298171a950)

static int adc\_raw\_to\_millivolts(int32\_t ref\_mv, enum adc\_gain gain, uint8\_t resolution, int32\_t \*valp)

Convert a raw ADC value to millivolts.

**Definition** adc.h:892

[ADC\_GAIN\_64](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb)

@ ADC\_GAIN\_64

x 64.

**Definition** adc.h:54

[ADC\_GAIN\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e)

@ ADC\_GAIN\_3

x 3.

**Definition** adc.h:46

[ADC\_GAIN\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300)

@ ADC\_GAIN\_4

x 4.

**Definition** adc.h:47

[ADC\_GAIN\_1\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9)

@ ADC\_GAIN\_1\_5

x 1/5.

**Definition** adc.h:36

[ADC\_GAIN\_128](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829)

@ ADC\_GAIN\_128

x 128.

**Definition** adc.h:55

[ADC\_GAIN\_1\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2)

@ ADC\_GAIN\_1\_2

x 1/2.

**Definition** adc.h:41

[ADC\_GAIN\_2\_7](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a30cf06d8c6d323a8bfef3a508f2c3388)

@ ADC\_GAIN\_2\_7

x 2/7.

**Definition** adc.h:38

[ADC\_GAIN\_12](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8)

@ ADC\_GAIN\_12

x 12.

**Definition** adc.h:50

[ADC\_GAIN\_2\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0)

@ ADC\_GAIN\_2\_5

x 2/5.

**Definition** adc.h:40

[ADC\_GAIN\_16](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970)

@ ADC\_GAIN\_16

x 16.

**Definition** adc.h:51

[ADC\_GAIN\_24](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33)

@ ADC\_GAIN\_24

x 24.

**Definition** adc.h:52

[ADC\_GAIN\_1](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54)

@ ADC\_GAIN\_1

x 1.

**Definition** adc.h:44

[ADC\_GAIN\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8)

@ ADC\_GAIN\_6

x 6.

**Definition** adc.h:48

[ADC\_GAIN\_1\_6](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1)

@ ADC\_GAIN\_1\_6

x 1/6.

**Definition** adc.h:35

[ADC\_GAIN\_32](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f)

@ ADC\_GAIN\_32

x 32.

**Definition** adc.h:53

[ADC\_GAIN\_2\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62)

@ ADC\_GAIN\_2\_3

x 2/3.

**Definition** adc.h:42

[ADC\_GAIN\_4\_5](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df)

@ ADC\_GAIN\_4\_5

x 4/5.

**Definition** adc.h:43

[ADC\_GAIN\_8](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3)

@ ADC\_GAIN\_8

x 8.

**Definition** adc.h:49

[ADC\_GAIN\_1\_3](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee)

@ ADC\_GAIN\_1\_3

x 1/3.

**Definition** adc.h:39

[ADC\_GAIN\_1\_4](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8)

@ ADC\_GAIN\_1\_4

x 1/4.

**Definition** adc.h:37

[ADC\_GAIN\_2](group__adc__interface.md#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868)

@ ADC\_GAIN\_2

x 2.

**Definition** adc.h:45

[ADC\_ACTION\_FINISH](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9)

@ ADC\_ACTION\_FINISH

The sequence should be finished immediately.

**Definition** adc.h:563

[ADC\_ACTION\_REPEAT](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715)

@ ADC\_ACTION\_REPEAT

The sampling should be repeated.

**Definition** adc.h:560

[ADC\_ACTION\_CONTINUE](group__adc__interface.md#gga8f6df993405679f852ae4cd8c63c6917ac875a64d997cb883b49447006554ba92)

@ ADC\_ACTION\_CONTINUE

The sequence should be continued normally.

**Definition** adc.h:554

[ADC\_REF\_INTERNAL](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709)

@ ADC\_REF\_INTERNAL

Internal.

**Definition** adc.h:100

[ADC\_REF\_EXTERNAL1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a)

@ ADC\_REF\_EXTERNAL1

External, input 1.

**Definition** adc.h:102

[ADC\_REF\_VDD\_1\_2](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d)

@ ADC\_REF\_VDD\_1\_2

VDD/2.

**Definition** adc.h:97

[ADC\_REF\_VDD\_1\_3](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1)

@ ADC\_REF\_VDD\_1\_3

VDD/3.

**Definition** adc.h:98

[ADC\_REF\_VDD\_1\_4](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c)

@ ADC\_REF\_VDD\_1\_4

VDD/4.

**Definition** adc.h:99

[ADC\_REF\_VDD\_1](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3)

@ ADC\_REF\_VDD\_1

VDD.

**Definition** adc.h:96

[ADC\_REF\_EXTERNAL0](group__adc__interface.md#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6)

@ ADC\_REF\_EXTERNAL0

External, input 0.

**Definition** adc.h:101

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[adc\_channel\_cfg](structadc__channel__cfg.md)

Structure for specifying the configuration of an ADC channel.

**Definition** adc.h:108

[adc\_channel\_cfg::gain](structadc__channel__cfg.md#a20996396fa5b1d27eeea7da9ea9df848)

enum adc\_gain gain

Gain selection.

**Definition** adc.h:110

[adc\_channel\_cfg::differential](structadc__channel__cfg.md#a372f298a2dd87660b9508ca1387084b6)

uint8\_t differential

Channel type: single-ended or differential.

**Definition** adc.h:151

[adc\_channel\_cfg::acquisition\_time](structadc__channel__cfg.md#a426a74cf53a4b801e91c2eeb1db3477d)

uint16\_t acquisition\_time

Acquisition time.

**Definition** adc.h:124

[adc\_channel\_cfg::reference](structadc__channel__cfg.md#a73d11ad6411a62f8f21cbfa492bc1b20)

enum adc\_reference reference

Reference selection.

**Definition** adc.h:113

[adc\_channel\_cfg::channel\_id](structadc__channel__cfg.md#aeec90a3fb60f93427a92e083326c8fcf)

uint8\_t channel\_id

Channel identifier.

**Definition** adc.h:148

[adc\_driver\_api](structadc__driver__api.md)

ADC driver API.

**Definition** adc.h:720

[adc\_driver\_api::read](structadc__driver__api.md#a489ba3478e4d36379e591fa1a3fc425b)

adc\_api\_read read

**Definition** adc.h:722

[adc\_driver\_api::ref\_internal](structadc__driver__api.md#ad12d4f5fa0eb0e45e14553deab0edbed)

uint16\_t ref\_internal

**Definition** adc.h:726

[adc\_driver\_api::channel\_setup](structadc__driver__api.md#ad14fe480ff7a0c4efe78e2fcb9bf6ee2)

adc\_api\_channel\_setup channel\_setup

**Definition** adc.h:721

[adc\_dt\_spec](structadc__dt__spec.md)

Container for ADC channel information specified in devicetree.

**Definition** adc.h:282

[adc\_dt\_spec::channel\_cfg](structadc__dt__spec.md#a056b22daa13da07cb3ff37bd4adf199d)

struct adc\_channel\_cfg channel\_cfg

Configuration of the associated ADC channel specified in devicetree.

**Definition** adc.h:304

[adc\_dt\_spec::channel\_id](structadc__dt__spec.md#a083e6c5bc707606c2ea1459fb58e29a8)

uint8\_t channel\_id

ADC channel identifier used by this io-channel.

**Definition** adc.h:290

[adc\_dt\_spec::vref\_mv](structadc__dt__spec.md#a9e120f52e3a905768d8e6bdc3469d20a)

uint16\_t vref\_mv

Voltage of the reference selected for the channel or 0 if this value is not provided in devicetree.

**Definition** adc.h:312

[adc\_dt\_spec::dev](structadc__dt__spec.md#aa2656b923d105743eaee3e03691edc44)

const struct device \* dev

Pointer to the device structure for the ADC driver instance used by this io-channel.

**Definition** adc.h:287

[adc\_dt\_spec::oversampling](structadc__dt__spec.md#aa7daf451a3438847ff989f32eae11e97)

uint8\_t oversampling

Oversampling setting to be used for that channel.

**Definition** adc.h:326

[adc\_dt\_spec::channel\_cfg\_dt\_node\_exists](structadc__dt__spec.md#aaf239b0c62b34158bac1a3b63e35f612)

bool channel\_cfg\_dt\_node\_exists

Flag indicating whether configuration of the associated ADC channel is provided as a child node of th...

**Definition** adc.h:297

[adc\_dt\_spec::resolution](structadc__dt__spec.md#abbe7052a144541b8d16afee3fd231c10)

uint8\_t resolution

ADC resolution to be used for that channel.

**Definition** adc.h:319

[adc\_sequence\_options](structadc__sequence__options.md)

Structure defining additional options for an ADC sampling sequence.

**Definition** adc.h:592

[adc\_sequence\_options::user\_data](structadc__sequence__options.md#a262fd6daefb22df02c726aafcddc6d47)

void \* user\_data

Pointer to user data.

**Definition** adc.h:614

[adc\_sequence\_options::extra\_samplings](structadc__sequence__options.md#a29f8ac4cdf6740f56bcd70a0a027e56a)

uint16\_t extra\_samplings

Number of extra samplings to perform (the total number of samplings is 1 + extra\_samplings).

**Definition** adc.h:620

[adc\_sequence\_options::callback](structadc__sequence__options.md#a71bd082c14f01a1b5d1b491e7510aa91)

adc\_sequence\_callback callback

Callback function to be called after each sampling is done.

**Definition** adc.h:608

[adc\_sequence\_options::interval\_us](structadc__sequence__options.md#ad2f11727ab0eb7e32a5fbd07f04a85b2)

uint32\_t interval\_us

Interval between consecutive samplings (in microseconds), 0 means sample as fast as possible,...

**Definition** adc.h:602

[adc\_sequence](structadc__sequence.md)

Structure defining an ADC sampling sequence.

**Definition** adc.h:626

[adc\_sequence::oversampling](structadc__sequence.md#a233e8b20b57bb2fdbebf2c85f076c802)

uint8\_t oversampling

Oversampling setting.

**Definition** adc.h:678

[adc\_sequence::options](structadc__sequence.md#a379c6f92153dfa97439d39cbef222451)

const struct adc\_sequence\_options \* options

Pointer to a structure defining additional options for the sequence.

**Definition** adc.h:631

[adc\_sequence::channels](structadc__sequence.md#a5c497c4a5de20e8591063ca8661f79c1)

uint32\_t channels

Bit-mask indicating the channels to be included in each sampling of this sequence.

**Definition** adc.h:640

[adc\_sequence::buffer](structadc__sequence.md#a5df0ee0e6d3215aa052f108476bd57ec)

void \* buffer

Pointer to a buffer where the samples are to be written.

**Definition** adc.h:653

[adc\_sequence::calibrate](structadc__sequence.md#a6023e3bec29deaa11b44c4df40eb7b04)

bool calibrate

Perform calibration before the reading is taken if requested.

**Definition** adc.h:688

[adc\_sequence::buffer\_size](structadc__sequence.md#a8e1bc9a4361e274bbdaedeb3151b71e5)

size\_t buffer\_size

Specifies the actual size of the buffer pointed by the "buffer" field (in bytes).

**Definition** adc.h:661

[adc\_sequence::resolution](structadc__sequence.md#ad5480691be25ed9ee81130b775743125)

uint8\_t resolution

ADC resolution.

**Definition** adc.h:670

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:6122

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc.h](drivers_2adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
