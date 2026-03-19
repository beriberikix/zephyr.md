---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bindesc_8h_source.html
original_path: doxygen/html/bindesc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bindesc.h

[Go to the documentation of this file.](bindesc_8h.md)

1/\*

2 \* Copyright (c) 2023 Yonatan Schachter

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_

9

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif /\* \_\_cplusplus \*/

15

16/\*

17 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

18 \* Do not change without syncing the definitions in both files!

19 \*/

[ 20](bindesc_8h.md#a8e7d54173280f72eb5f031d752c19197)#define BINDESC\_MAGIC 0xb9863e5a7ea46046

[ 21](bindesc_8h.md#a674bcf8c1d881131b5e82d5dec48ee33)#define BINDESC\_ALIGNMENT 4

[ 22](bindesc_8h.md#adac0fea8ab54ea428c533f509058b910)#define BINDESC\_TYPE\_UINT 0x0

[ 23](bindesc_8h.md#a68acc09b5e324134e5c83eeaa064fc41)#define BINDESC\_TYPE\_STR 0x1

[ 24](bindesc_8h.md#a24e6723b552f65cc1f143bcb7f66f125)#define BINDESC\_TYPE\_BYTES 0x2

[ 25](bindesc_8h.md#ac98ab7042b1b3f6654e910fa4d0c2d40)#define BINDESC\_TYPE\_DESCRIPTORS\_END 0xf

26/\* sizeof ignores the data as it's a flexible array \*/

[ 27](bindesc_8h.md#a3327af407c3d5a7c05e9fd5c3c53380a)#define BINDESC\_ENTRY\_HEADER\_SIZE (sizeof(struct bindesc\_entry))

28

35

36/\*

37 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

38 \* Do not change without syncing the definitions in both files!

39 \*/

40

[ 42](group__bindesc__define.md#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)#define BINDESC\_ID\_APP\_VERSION\_STRING 0x800

43

[ 45](group__bindesc__define.md#ga94f405178c0139626718b143e6f22734)#define BINDESC\_ID\_APP\_VERSION\_MAJOR 0x801

46

[ 48](group__bindesc__define.md#gaab4f7cdf7ea4f766be1fa7779eef1bdb)#define BINDESC\_ID\_APP\_VERSION\_MINOR 0x802

49

[ 51](group__bindesc__define.md#ga90eb8f252c3484103eee18dbb1aabdc6)#define BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL 0x803

52

[ 54](group__bindesc__define.md#ga66b25585ff23de9906814ddecb4ac4ea)#define BINDESC\_ID\_APP\_VERSION\_NUMBER 0x804

55

[ 57](group__bindesc__define.md#gadde3e821958da17070aa91dc82c51265)#define BINDESC\_ID\_APP\_BUILD\_VERSION 0x805

58

[ 60](group__bindesc__define.md#ga35fdf13eb11dd4eeca1bf2dc57782777)#define BINDESC\_ID\_KERNEL\_VERSION\_STRING 0x900

61

[ 63](group__bindesc__define.md#gabd5e9193c56495faa19f299371a02fd0)#define BINDESC\_ID\_KERNEL\_VERSION\_MAJOR 0x901

64

[ 66](group__bindesc__define.md#ga9ab56a8cef01c648a313bb4e5b7983e4)#define BINDESC\_ID\_KERNEL\_VERSION\_MINOR 0x902

67

[ 69](group__bindesc__define.md#ga2ef91c2cd49d61c9f3e95ac5292e6983)#define BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL 0x903

70

[ 72](group__bindesc__define.md#gad2c5489eaa1a191a49ffd409462b1af4)#define BINDESC\_ID\_KERNEL\_VERSION\_NUMBER 0x904

73

[ 75](group__bindesc__define.md#gaf7b25978649c3d9339e13ecaa1090c74)#define BINDESC\_ID\_KERNEL\_BUILD\_VERSION 0x905

76

[ 78](group__bindesc__define.md#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)#define BINDESC\_ID\_BUILD\_TIME\_YEAR 0xa00

79

[ 81](group__bindesc__define.md#ga8e68f8226d05415c040f6fb74bada6fc)#define BINDESC\_ID\_BUILD\_TIME\_MONTH 0xa01

82

[ 84](group__bindesc__define.md#ga5710e218f4f10e5049d039b17a376d0b)#define BINDESC\_ID\_BUILD\_TIME\_DAY 0xa02

85

[ 87](group__bindesc__define.md#gaeed1651e0d025ff74092a88b6d57e408)#define BINDESC\_ID\_BUILD\_TIME\_HOUR 0xa03

88

[ 90](group__bindesc__define.md#ga67f679968aeea5517e02da6e5e67d73e)#define BINDESC\_ID\_BUILD\_TIME\_MINUTE 0xa04

91

[ 93](group__bindesc__define.md#gacdff70f58c8098e23611327c1264a7dd)#define BINDESC\_ID\_BUILD\_TIME\_SECOND 0xa05

94

[ 96](group__bindesc__define.md#gab0eefe2d83294d6ebe4ca6299f05d785)#define BINDESC\_ID\_BUILD\_TIME\_UNIX 0xa06

97

[ 99](group__bindesc__define.md#gad8803e832ed0a42fd7033e277f8d8362)#define BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING 0xa07

100

[ 102](group__bindesc__define.md#ga8bf6d98fb9495f2cca6b0403dffd0752)#define BINDESC\_ID\_BUILD\_DATE\_STRING 0xa08

103

[ 105](group__bindesc__define.md#gac4f75b876a81072e14bb39e3fb1c1f8a)#define BINDESC\_ID\_BUILD\_TIME\_STRING 0xa09

106

[ 108](group__bindesc__define.md#ga4cc66094d33709d9738b49e181a6eec3)#define BINDESC\_ID\_HOST\_NAME 0xb00

109

[ 111](group__bindesc__define.md#ga51b3fdd47d3dd94101134523c4dca144)#define BINDESC\_ID\_C\_COMPILER\_NAME 0xb01

112

[ 114](group__bindesc__define.md#gac4c6c9576b31cb2c26b085537648552b)#define BINDESC\_ID\_C\_COMPILER\_VERSION 0xb02

115

[ 117](group__bindesc__define.md#ga6f198590afdb2524b587e0194598b8eb)#define BINDESC\_ID\_CXX\_COMPILER\_NAME 0xb03

118

[ 120](group__bindesc__define.md#ga7ec0430daae1f99bdeeae6a636a263d8)#define BINDESC\_ID\_CXX\_COMPILER\_VERSION 0xb04

121

[ 122](group__bindesc__define.md#gac12b3cbf6d132fb54bbf702fd581373f)#define BINDESC\_TAG\_DESCRIPTORS\_END BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff)

123

127

128/\*

129 \* Utility macro to generate a tag from a type and an ID

130 \*

131 \* type - Type of the descriptor, UINT, STR or BYTES

132 \* id - Unique ID for the descriptor, must fit in 12 bits

133 \*/

134#define BINDESC\_TAG(type, id) ((BINDESC\_TYPE\_##type & 0xf) << 12 | (id & 0x0fff))

135

141#define BINDESC\_GET\_TAG\_TYPE(tag) ((tag >> 12) & 0xf)

142

146

147#if !defined(\_LINKER) || defined(\_\_DOXYGEN\_\_)

148

149#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

150#include <[zephyr/device.h](device_8h.md)>

151

155

156/\*

157 \* Utility macro to get the name of a bindesc entry

158 \*/

159#define BINDESC\_NAME(name) bindesc\_entry\_##name

160

161/\* Convenience helper for declaring a binary descriptor entry. \*/

162#define \_\_BINDESC\_ENTRY\_DEFINE(name) \

163 \_\_aligned(BINDESC\_ALIGNMENT) const struct bindesc\_entry BINDESC\_NAME(name) \

164 \_\_in\_section(\_bindesc\_entry, static, name) \_\_used \_\_noasan

165

169

[ 184](group__bindesc__define.md#gacfba0fe843c53a86271e685394078b22)#define BINDESC\_STR\_DEFINE(name, id, value) \

185 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

186 .tag = BINDESC\_TAG(STR, id), \

187 .len = (uint16\_t)sizeof(value), \

188 .data = value, \

189 }; \

190 BUILD\_ASSERT(sizeof(value) <= CONFIG\_BINDESC\_DEFINE\_MAX\_DATA\_SIZE, \

191 "Bindesc " STRINGIFY(name) " exceeded maximum size, consider reducing the" \

192 " size or changing CONFIG\_BINDESC\_DEFINE\_MAX\_DATA\_SIZE. ")

193

[ 208](group__bindesc__define.md#gac603068b1abdac72d5f668fea3b3cdff)#define BINDESC\_UINT\_DEFINE(name, id, value) \

209 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

210 .tag = BINDESC\_TAG(UINT, id), \

211 .len = (uint16\_t)sizeof(uint32\_t), \

212 .data = sys\_uint32\_to\_array(value), \

213 }

214

[ 233](group__bindesc__define.md#ga137cc1f8fcc0e36e71c8ea4b8c0e8885)#define BINDESC\_BYTES\_DEFINE(name, id, value) \

234 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

235 .tag = BINDESC\_TAG(BYTES, id), \

236 .len = (uint16\_t)sizeof((uint8\_t [])\_\_DEBRACKET value), \

237 .data = \_\_DEBRACKET value, \

238 }; \

239 BUILD\_ASSERT(sizeof((uint8\_t [])\_\_DEBRACKET value) <= \

240 CONFIG\_BINDESC\_DEFINE\_MAX\_DATA\_SIZE, \

241 "Bindesc " STRINGIFY(name) " exceeded maximum size, consider reducing the" \

242 " size or changing CONFIG\_BINDESC\_DEFINE\_MAX\_DATA\_SIZE. ")

243

[ 253](group__bindesc__define.md#gaf7628498209bc6729a6abf36a92d0cbd)#define BINDESC\_GET\_STR(name) BINDESC\_NAME(name).data

254

[ 264](group__bindesc__define.md#ga8f738fd9f99f52f0c7ce81011c8e7b98)#define BINDESC\_GET\_UINT(name) \*(uint32\_t \*)&(BINDESC\_NAME(name).data)

265

[ 278](group__bindesc__define.md#ga1fbf08f04e66c250aecdd70045242a37)#define BINDESC\_GET\_BYTES(name) BINDESC\_NAME(name).data

279

[ 289](group__bindesc__define.md#gace8f89f0a8d25a12503c1b337f74dd30)#define BINDESC\_GET\_SIZE(name) BINDESC\_NAME(name).len

290

294

295/\*

296 \* An entry of the binary descriptor header. Each descriptor is

297 \* described by one of these entries.

298 \*/

[ 299](structbindesc__entry.md)struct [bindesc\_entry](structbindesc__entry.md) {

[ 301](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tag](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112);

[ 303](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4);

[ 305](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41)[];

306} \_\_packed;

307

308/\*

309 \* We're assuming that `struct bindesc\_entry` has a specific layout in

310 \* memory, so it's worth making sure that the layout is really what we

311 \* think it is. If these assertions fail for your toolchain/platform,

312 \* please open a bug report.

313 \*/

[ 314](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641)BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), tag) == 0, "Incorrect memory layout");

315BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), len) == 2, "Incorrect memory layout");

316BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), data) == 4, "Incorrect memory layout");

317

[ 318](structbindesc__handle.md)struct [bindesc\_handle](structbindesc__handle.md) {

[ 319](structbindesc__handle.md#a40eb18bdca234d91bf7395ed7d6be37d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[address](structbindesc__handle.md#a40eb18bdca234d91bf7395ed7d6be37d);

320 enum {

[ 321](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca6b384bd5837e71fd2b16f20e6b656488) [BINDESC\_HANDLE\_TYPE\_RAM](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca6b384bd5837e71fd2b16f20e6b656488),

[ 322](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca934b7d04129a28cac848dd472ab6bdd9) [BINDESC\_HANDLE\_TYPE\_MEMORY\_MAPPED\_FLASH](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca934b7d04129a28cac848dd472ab6bdd9),

[ 323](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054caa79bb2c6316f34fe69662abcb9995d55) [BINDESC\_HANDLE\_TYPE\_FLASH](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054caa79bb2c6316f34fe69662abcb9995d55),

[ 324](structbindesc__handle.md#ac598522ba071536349778973692b473c) } [type](structbindesc__handle.md#ac598522ba071536349778973692b473c);

[ 325](structbindesc__handle.md#aca15669b5589c20d6ea0e1296e0ff233) size\_t [size\_limit](structbindesc__handle.md#aca15669b5589c20d6ea0e1296e0ff233);

326#if IS\_ENABLED(CONFIG\_BINDESC\_READ\_FLASH)

327 const struct [device](structdevice.md) \*flash\_device;

328 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buffer[sizeof(struct [bindesc\_entry](structbindesc__entry.md)) +

329 CONFIG\_BINDESC\_READ\_FLASH\_MAX\_DATA\_SIZE] \_\_aligned([BINDESC\_ALIGNMENT](bindesc_8h.md#a674bcf8c1d881131b5e82d5dec48ee33));

330#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_READ\_FLASH) \*/

331};

332

339

[ 348](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519)typedef int (\*[bindesc\_callback\_t](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519))(const struct [bindesc\_entry](structbindesc__entry.md) \*entry, void \*user\_data);

349

[ 364](group__bindesc__read.md#ga3ed93a855c2ee2981f2ca76450c57d99)int [bindesc\_open\_memory\_mapped\_flash](group__bindesc__read.md#ga3ed93a855c2ee2981f2ca76450c57d99)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, size\_t offset);

365

[ 384](group__bindesc__read.md#gadec0f4f828c1e4cdcef63b67c0fbafcf)int [bindesc\_open\_ram](group__bindesc__read.md#gadec0f4f828c1e4cdcef63b67c0fbafcf)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*address, size\_t max\_size);

385

[ 402](group__bindesc__read.md#ga724d940fecd648523c3d3bd840785498)int [bindesc\_open\_flash](group__bindesc__read.md#ga724d940fecd648523c3d3bd840785498)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, size\_t offset,

403 const struct [device](structdevice.md) \*flash\_device);

404

[ 418](group__bindesc__read.md#ga8d7f293d620a80b49797d4c1d6d2998f)int [bindesc\_foreach](group__bindesc__read.md#ga8d7f293d620a80b49797d4c1d6d2998f)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, [bindesc\_callback\_t](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519) callback, void \*user\_data);

419

[ 434](group__bindesc__read.md#ga422708cc9ffb1a911b4990eff0270e76)int [bindesc\_find\_str](group__bindesc__read.md#ga422708cc9ffb1a911b4990eff0270e76)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const char \*\*result);

435

[ 450](group__bindesc__read.md#gad3ae2bde011c2115a33c836caff37811)int [bindesc\_find\_uint](group__bindesc__read.md#gad3ae2bde011c2115a33c836caff37811)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*result);

451

[ 467](group__bindesc__read.md#gaf8b8b3a883f5c835d5a0581768d801d4)int [bindesc\_find\_bytes](group__bindesc__read.md#gaf8b8b3a883f5c835d5a0581768d801d4)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*result,

468 size\_t \*result\_size);

469

[ 482](group__bindesc__read.md#ga7df52ef12aa9572d3a2ff4245529d8fd)int [bindesc\_get\_size](group__bindesc__read.md#ga7df52ef12aa9572d3a2ff4245529d8fd)(struct [bindesc\_handle](structbindesc__handle.md) \*handle, size\_t \*result);

483

487

488#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING)

489extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_string);

490#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING) \*/

491

492#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR)

493extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_major);

494#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR) \*/

495

496#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR)

497extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_minor);

498#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR) \*/

499

500#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL)

501extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_patchlevel);

502#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL) \*/

503

504#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER)

505extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_number);

506#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER) \*/

507

508#if defined(CONFIG\_BINDESC\_KERNEL\_BUILD\_VERSION)

509extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_build\_version);

510#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_BUILD\_VERSION) \*/

511

512#if defined(CONFIG\_BINDESC\_APP\_VERSION\_STRING)

513extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_string);

514#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_STRING) \*/

515

516#if defined(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR)

517extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_major);

518#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR) \*/

519

520#if defined(CONFIG\_BINDESC\_APP\_VERSION\_MINOR)

521extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_minor);

522#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_MINOR) \*/

523

524#if defined(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL)

525extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_patchlevel);

526#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL) \*/

527

528#if defined(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER)

529extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_number);

530#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER) \*/

531

532#if defined(CONFIG\_BINDESC\_APP\_BUILD\_VERSION)

533extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_build\_version);

534#endif /\* defined(CONFIG\_BINDESC\_APP\_BUILD\_VERSION) \*/

535

536#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR)

537extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_year);

538#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR) \*/

539

540#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH)

541extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_month);

542#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH) \*/

543

544#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_DAY)

545extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_day);

546#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_DAY) \*/

547

548#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR)

549extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_hour);

550#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR) \*/

551

552#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE)

553extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_minute);

554#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE) \*/

555

556#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND)

557extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_second);

558#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND) \*/

559

560#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX)

561extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_unix);

562#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX) \*/

563

564#if defined(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING)

565extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_date\_time\_string);

566#endif /\* defined(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING) \*/

567

568#if defined(CONFIG\_BINDESC\_BUILD\_DATE\_STRING)

569extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_date\_string);

570#endif /\* defined(CONFIG\_BINDESC\_BUILD\_DATE\_STRING) \*/

571

572#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_STRING)

573extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_string);

574#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_STRING) \*/

575

576#if defined(CONFIG\_BINDESC\_HOST\_NAME)

577extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(host\_name);

578#endif /\* defined(CONFIG\_BINDESC\_HOST\_NAME) \*/

579

580#if defined(CONFIG\_BINDESC\_C\_COMPILER\_NAME)

581extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(c\_compiler\_name);

582#endif /\* defined(CONFIG\_BINDESC\_C\_COMPILER\_NAME) \*/

583

584#if defined(CONFIG\_BINDESC\_C\_COMPILER\_VERSION)

585extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(c\_compiler\_version);

586#endif /\* defined(CONFIG\_BINDESC\_C\_COMPILER\_VERSION) \*/

587

588#if defined(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME)

589extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(cxx\_compiler\_name);

590#endif /\* defined(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME) \*/

591

592#if defined(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION)

593extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(cxx\_compiler\_version);

594#endif /\* defined(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION) \*/

595

596#endif /\* !defined(\_LINKER) \*/

597

598#ifdef \_\_cplusplus

599}

600#endif

601

602#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_ \*/

[BINDESC\_ALIGNMENT](bindesc_8h.md#a674bcf8c1d881131b5e82d5dec48ee33)

#define BINDESC\_ALIGNMENT

**Definition** bindesc.h:21

[device.h](device_8h.md)

[bindesc\_open\_memory\_mapped\_flash](group__bindesc__read.md#ga3ed93a855c2ee2981f2ca76450c57d99)

int bindesc\_open\_memory\_mapped\_flash(struct bindesc\_handle \*handle, size\_t offset)

Open an image's binary descriptors for reading, from a memory mapped flash.

[bindesc\_find\_str](group__bindesc__read.md#ga422708cc9ffb1a911b4990eff0270e76)

int bindesc\_find\_str(struct bindesc\_handle \*handle, uint16\_t id, const char \*\*result)

Find a specific descriptor of type string.

[bindesc\_callback\_t](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519)

int(\* bindesc\_callback\_t)(const struct bindesc\_entry \*entry, void \*user\_data)

Callback type to be called on descriptors found during a walk.

**Definition** bindesc.h:348

[bindesc\_open\_flash](group__bindesc__read.md#ga724d940fecd648523c3d3bd840785498)

int bindesc\_open\_flash(struct bindesc\_handle \*handle, size\_t offset, const struct device \*flash\_device)

Open an image's binary descriptors for reading, from flash.

[bindesc\_get\_size](group__bindesc__read.md#ga7df52ef12aa9572d3a2ff4245529d8fd)

int bindesc\_get\_size(struct bindesc\_handle \*handle, size\_t \*result)

Get the size of an image's binary descriptors.

[bindesc\_foreach](group__bindesc__read.md#ga8d7f293d620a80b49797d4c1d6d2998f)

int bindesc\_foreach(struct bindesc\_handle \*handle, bindesc\_callback\_t callback, void \*user\_data)

Walk the binary descriptors and run a user defined callback on each of them.

[bindesc\_find\_uint](group__bindesc__read.md#gad3ae2bde011c2115a33c836caff37811)

int bindesc\_find\_uint(struct bindesc\_handle \*handle, uint16\_t id, const uint32\_t \*\*result)

Find a specific descriptor of type uint.

[bindesc\_open\_ram](group__bindesc__read.md#gadec0f4f828c1e4cdcef63b67c0fbafcf)

int bindesc\_open\_ram(struct bindesc\_handle \*handle, const uint8\_t \*address, size\_t max\_size)

Open an image's binary descriptors for reading, from RAM.

[bindesc\_find\_bytes](group__bindesc__read.md#gaf8b8b3a883f5c835d5a0581768d801d4)

int bindesc\_find\_bytes(struct bindesc\_handle \*handle, uint16\_t id, const uint8\_t \*\*result, size\_t \*result\_size)

Find a specific descriptor of type bytes.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bindesc\_entry](structbindesc__entry.md)

**Definition** bindesc.h:299

[bindesc\_entry::data](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41)

uint8\_t data[]

Value of the entry.

**Definition** bindesc.h:305

[bindesc\_entry::tag](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112)

uint16\_t tag

Tag of the entry.

**Definition** bindesc.h:301

[bindesc\_entry::len](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4)

uint16\_t len

Length of the descriptor data.

**Definition** bindesc.h:303

[bindesc\_handle](structbindesc__handle.md)

**Definition** bindesc.h:318

[bindesc\_handle::BINDESC\_HANDLE\_TYPE\_RAM](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca6b384bd5837e71fd2b16f20e6b656488)

@ BINDESC\_HANDLE\_TYPE\_RAM

**Definition** bindesc.h:321

[bindesc\_handle::BINDESC\_HANDLE\_TYPE\_MEMORY\_MAPPED\_FLASH](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054ca934b7d04129a28cac848dd472ab6bdd9)

@ BINDESC\_HANDLE\_TYPE\_MEMORY\_MAPPED\_FLASH

**Definition** bindesc.h:322

[bindesc\_handle::BINDESC\_HANDLE\_TYPE\_FLASH](structbindesc__handle.md#a3367bd6f8c28a54305ba47f3f47f054caa79bb2c6316f34fe69662abcb9995d55)

@ BINDESC\_HANDLE\_TYPE\_FLASH

**Definition** bindesc.h:323

[bindesc\_handle::address](structbindesc__handle.md#a40eb18bdca234d91bf7395ed7d6be37d)

const uint8\_t \* address

**Definition** bindesc.h:319

[bindesc\_handle::type](structbindesc__handle.md#ac598522ba071536349778973692b473c)

enum bindesc\_handle::@024232357357202240030275011026126114147031266101 type

[bindesc\_handle::size\_limit](structbindesc__handle.md#aca15669b5589c20d6ea0e1296e0ff233)

size\_t size\_limit

**Definition** bindesc.h:325

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bindesc.h](bindesc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
