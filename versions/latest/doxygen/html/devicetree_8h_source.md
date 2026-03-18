---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/devicetree_8h_source.html
original_path: doxygen/html/devicetree_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h

[Go to the documentation of this file.](devicetree_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \* Copyright (c) 2020 Nordic Semiconductor

4 \* Copyright (c) 2020, Linaro Ltd.

5 \*

6 \* Not a generated file. Feel free to modify.

7 \*/

8

15

16#ifndef DEVICETREE\_H

17#define DEVICETREE\_H

18

19#include <devicetree\_generated.h>

20#include <[zephyr/irq\_multilevel.h](irq__multilevel_8h.md)>

21

22#if !defined(\_LINKER) && !defined(\_ASMLANGUAGE)

23#include <[stdint.h](stdint_8h.md)>

24#endif

25

26#include <[zephyr/sys/util.h](util_8h.md)>

27

34

35/\*

36 \* Property suffixes

37 \* -----------------

38 \*

39 \* These are the optional parts that come after the \_P\_<property>

40 \* part in DT\_N\_<path-id>\_P\_<property-id> macros, or the "prop-suf"

41 \* nonterminal in the DT guide's macros.bnf file.

42 \*

43 \* Before adding new ones, check this list to avoid conflicts. If any

44 \* are missing from this list, please add them. It should be complete.

45 \*

46 \* \_ENUM\_IDX: property's value as an index into bindings enum

47 \* \_ENUM\_VAL\_<val>\_EXISTS property's value as a token exists

48 \* \_ENUM\_TOKEN: property's value as a token into bindings enum (string

49 \* enum values are identifiers) [deprecated, use \_STRING\_TOKEN]

50 \* \_ENUM\_UPPER\_TOKEN: like \_ENUM\_TOKEN, but uppercased [deprecated, use

51 \* \_STRING\_UPPER\_TOKEN]

52 \* \_EXISTS: property is defined

53 \* \_FOREACH\_PROP\_ELEM: helper for "iterating" over values in the property

54 \* \_FOREACH\_PROP\_ELEM\_VARGS: foreach functions with variable number of arguments

55 \* \_IDX\_<i>: logical index into property

56 \* \_IDX\_<i>\_EXISTS: logical index into property is defined

57 \* \_IDX\_<i>\_PH: phandle array's phandle by index (or phandle, phandles)

58 \* \_IDX\_<i>\_STRING\_TOKEN: string array element value as a token

59 \* \_IDX\_<i>\_STRING\_UPPER\_TOKEN: string array element value as a uppercased token

60 \* \_IDX <i>\_STRING\_UNQUOTED: string array element value as a sequence of tokens, with no quotes

61 \* \_IDX\_<i>\_VAL\_<val>: phandle array's specifier value by index

62 \* \_IDX\_<i>\_VAL\_<val>\_EXISTS: cell value exists, by index

63 \* \_LEN: property logical length

64 \* \_NAME\_<name>\_PH: phandle array's phandle by name

65 \* \_NAME\_<name>\_VAL\_<val>: phandle array's property specifier by name

66 \* \_NAME\_<name>\_VAL\_<val>\_EXISTS: cell value exists, by name

67 \* \_STRING\_TOKEN: string property's value as a token

68 \* \_STRING\_UPPER\_TOKEN: like \_STRING\_TOKEN, but uppercased

69 \* \_STRING\_UNQUOTED: string property's value as a sequence of tokens, with no quotes

70 \*/

71

77

[ 85](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)#define DT\_INVALID\_NODE \_

86

[ 90](group__devicetree-generic-id.md#gad65aa36621281687b22fa5d72db33e86)#define DT\_ROOT DT\_N

91

[ 142](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)#define DT\_PATH(...) DT\_PATH\_INTERNAL(\_\_VA\_ARGS\_\_)

143

[ 198](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)#define DT\_NODELABEL(label) DT\_CAT(DT\_N\_NODELABEL\_, label)

199

[ 238](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)#define DT\_ALIAS(alias) DT\_CAT(DT\_N\_ALIAS\_, alias)

239

[ 334](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)#define DT\_INST(inst, compat) UTIL\_CAT(DT\_N\_INST, DT\_DASH(inst, compat))

335

[ 359](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)#define DT\_PARENT(node\_id) DT\_CAT(node\_id, \_PARENT)

360

[ 384](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)#define DT\_GPARENT(node\_id) DT\_PARENT(DT\_PARENT(node\_id))

385

[ 421](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)#define DT\_CHILD(node\_id, child) UTIL\_CAT(node\_id, DT\_S\_PREFIX(child))

422

[ 464](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat) \

465 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

466 (DT\_INST(0, compat)), \

467 (DT\_INVALID\_NODE))

468

[ 496](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)#define DT\_NODE\_PATH(node\_id) DT\_CAT(node\_id, \_PATH)

497

[ 522](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)#define DT\_NODE\_FULL\_NAME(node\_id) DT\_CAT(node\_id, \_FULL\_NAME)

523

[ 550](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)#define DT\_NODE\_CHILD\_IDX(node\_id) DT\_CAT(node\_id, \_CHILD\_IDX)

551

[ 572](group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)#define DT\_SAME\_NODE(node\_id1, node\_id2) \

573 (DT\_DEP\_ORD(node\_id1) == (DT\_DEP\_ORD(node\_id2)))

574

578

584

[ 615](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)#define DT\_PROP(node\_id, prop) DT\_CAT3(node\_id, \_P\_, prop)

616

[ 649](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)#define DT\_PROP\_LEN(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_LEN)

650

[ 665](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value) \

666 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

667 (DT\_PROP\_LEN(node\_id, prop)), (default\_value))

668

[ 689](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx) \

690 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_EXISTS))

691

[ 724](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)#define DT\_PROP\_HAS\_NAME(node\_id, prop, name) \

725 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_NAME\_, name, \_EXISTS))

726

[ 761](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)#define DT\_PROP\_BY\_IDX(node\_id, prop, idx) \

762 DT\_CAT5(node\_id, \_P\_, prop, \_IDX\_, idx)

763

[ 777](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)#define DT\_PROP\_OR(node\_id, prop, default\_value) \

778 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

779 (DT\_PROP(node\_id, prop)), (default\_value))

780

[ 821](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)#define DT\_ENUM\_IDX(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_ENUM\_IDX)

822

[ 837](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value) \

838 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

839 (DT\_ENUM\_IDX(node\_id, prop)), (default\_idx\_value))

840

[ 849](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)#define DT\_ENUM\_HAS\_VALUE(node\_id, prop, value) \

850 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_ENUM\_VAL\_, value, \_EXISTS))

851

[ 911](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)#define DT\_STRING\_TOKEN(node\_id, prop) \

912 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_TOKEN)

913

[ 927](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value) \

928 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

929 (DT\_STRING\_TOKEN(node\_id, prop)), (default\_value))

930

[ 988](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop) \

989 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UPPER\_TOKEN)

990

[ 1005](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value) \

1006 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1007 (DT\_STRING\_UPPER\_TOKEN(node\_id, prop)), (default\_value))

1008

[ 1049](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)#define DT\_STRING\_UNQUOTED(node\_id, prop) \

1050 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UNQUOTED)

1051

[ 1066](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)#define DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value) \

1067 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1068 (DT\_STRING\_UNQUOTED(node\_id, prop)), (default\_value))

1069

[ 1117](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1118 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_TOKEN)

1119

[ 1167](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1168 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UPPER\_TOKEN)

1169

[ 1210](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)#define DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx) \

1211 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UNQUOTED)

1212

1213/\*

1214 \* phandle properties

1215 \*

1216 \* These are special-cased to manage the impedance mismatch between

1217 \* phandles, which are just uint32\_t node properties that only make sense

1218 \* within the tree itself, and C values.

1219 \*/

1220

[ 1266](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop) \

1267 DT\_PROP(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop)

1268

[ 1288](group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b)#define DT\_PROP\_BY\_PHANDLE\_IDX\_OR(node\_id, phs, idx, prop, default\_value) \

1289 DT\_PROP\_OR(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop, default\_value)

1290

[ 1302](group__devicetree-generic-prop.md#gabc1b099dda97fb03a9259a8b21fc04d2)#define DT\_PROP\_BY\_PHANDLE(node\_id, ph, prop) \

1303 DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)

1304

[ 1359](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell) \

1360 DT\_CAT7(node\_id, \_P\_, pha, \_IDX\_, idx, \_VAL\_, cell)

1361

[ 1385](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value) \

1386 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_IDX\_, idx, \_VAL\_, cell), default\_value)

1387

[ 1395](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)#define DT\_PHA(node\_id, pha, cell) DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)

1396

[ 1411](group__devicetree-generic-prop.md#ga886559b058b24164b62ab95215d860bd)#define DT\_PHA\_OR(node\_id, pha, cell, default\_value) \

1412 DT\_PHA\_BY\_IDX\_OR(node\_id, pha, 0, cell, default\_value)

1413

[ 1454](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell) \

1455 DT\_CAT7(node\_id, \_P\_, pha, \_NAME\_, name, \_VAL\_, cell)

1456

[ 1478](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value) \

1479 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_NAME\_, name, \_VAL\_, cell), default\_value)

1480

[ 1528](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name) \

1529 DT\_CAT6(node\_id, \_P\_, pha, \_NAME\_, name, \_PH)

1530

[ 1580](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx) \

1581 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_PH)

1582

[ 1594](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)#define DT\_PHANDLE(node\_id, prop) DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)

1595

1599

1605

[ 1642](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc)#define DT\_NUM\_RANGES(node\_id) DT\_CAT(node\_id, \_RANGES\_NUM)

1643

[ 1696](group__devicetree-ranges-prop.md#gac6f54058c58b06935bd2deae9f1ec2db)#define DT\_RANGES\_HAS\_IDX(node\_id, idx) \

1697 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_EXISTS))

1698

[ 1751](group__devicetree-ranges-prop.md#ga3730c9176911bd8cc762f447eb020ecd)#define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx) \

1752 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS\_EXISTS))

1753

[ 1791](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx) \

1792 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS)

1793

[ 1840](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

1841 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_ADDRESS)

1842

[ 1889](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

1890 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_PARENT\_BUS\_ADDRESS)

1891

[ 1938](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx) \

1939 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_LENGTH)

1940

[ 1980](group__devicetree-ranges-prop.md#ga4c71a8adcfe6c53b480775510c92a632)#define DT\_FOREACH\_RANGE(node\_id, fn) \

1981 DT\_CAT(node\_id, \_FOREACH\_RANGE)(fn)

1982

1986

1992

[ 2028](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747)#define DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx) \

2029 DT\_CAT3(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx)

2030

[ 2043](group__devicetree-generic-vendor.md#gabfa4130fa24457c457961caa7e2c6276)#define DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx) \

2044 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx, \_EXISTS))

2045

[ 2060](group__devicetree-generic-vendor.md#gaa71b1152516847d51582b9b23c472f3d)#define DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2061 COND\_CODE\_1(DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx), \

2062 (DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)), (default\_value))

2063

[ 2072](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)#define DT\_NODE\_VENDOR\_OR(node\_id, default\_value) \

2073 DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, 0, default\_value)

2074

[ 2104](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)#define DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx) \

2105 DT\_CAT3(node\_id, \_COMPAT\_MODEL\_IDX\_, idx)

2106

[ 2119](group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)#define DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx) \

2120 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_MODEL\_IDX\_, idx, \_EXISTS))

2121

[ 2136](group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)#define DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2137 COND\_CODE\_1(DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx), \

2138 (DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)), (default\_value))

2139

[ 2148](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)#define DT\_NODE\_MODEL\_OR(node\_id, default\_value) \

2149 DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, 0, default\_value)

2150

2154

2160

[ 2168](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)#define DT\_NUM\_REGS(node\_id) DT\_CAT(node\_id, \_REG\_NUM)

2169

[ 2181](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)#define DT\_REG\_HAS\_IDX(node\_id, idx) \

2182 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_EXISTS))

2183

[ 2190](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx) \

2191 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

2192

[ 2204](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx) \

2205 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE)

2206

[ 2214](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)#define DT\_REG\_ADDR(node\_id) DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)

2215

[ 2226](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)#define DT\_REG\_ADDR\_U64(node\_id) DT\_U64\_C(DT\_REG\_ADDR(node\_id))

2227

[ 2235](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)#define DT\_REG\_SIZE(node\_id) DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)

2236

[ 2243](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name) \

2244 DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS)

2245

[ 2258](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)#define DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name) \

2259 DT\_U64\_C(DT\_REG\_ADDR\_BY\_NAME(node\_id, name))

2260

[ 2267](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name) \

2268 DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE)

2269

2273

2279

[ 2288](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)#define DT\_NUM\_IRQS(node\_id) DT\_CAT(node\_id, \_IRQ\_NUM)

2289

[ 2296](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)#define DT\_IRQ\_LEVEL(node\_id) DT\_CAT(node\_id, \_IRQ\_LEVEL)

2297

[ 2308](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)#define DT\_IRQ\_HAS\_IDX(node\_id, idx) \

2309 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_EXISTS))

2310

[ 2321](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell) \

2322 IS\_ENABLED(DT\_CAT6(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

2323

[ 2331](group__devicetree-interrupts-prop.md#gab9c94ee39db7913598a755c6172fe036)#define DT\_IRQ\_HAS\_CELL(node\_id, cell) DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)

2332

[ 2342](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)#define DT\_IRQ\_HAS\_NAME(node\_id, name) \

2343 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_VAL\_irq\_EXISTS))

2344

[ 2380](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell) \

2381 DT\_CAT5(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell)

2382

[ 2398](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)#define DT\_IRQ\_BY\_NAME(node\_id, name, cell) \

2399 DT\_CAT5(node\_id, \_IRQ\_NAME\_, name, \_VAL\_, cell)

2400

[ 2408](group__devicetree-interrupts-prop.md#gabf60fbd528d300a26c0b4e66fe80a53f)#define DT\_IRQ(node\_id, cell) DT\_IRQ\_BY\_IDX(node\_id, 0, cell)

2409

[ 2452](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx) \

2453 DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_CONTROLLER)

2454

[ 2499](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)#define DT\_IRQ\_INTC\_BY\_NAME(node\_id, name) \

2500 DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_CONTROLLER)

2501

[ 2541](group__devicetree-interrupts-prop.md#ga11d2680614de65fd8cb4a3909e93e9c9)#define DT\_IRQ\_INTC(node\_id) \

2542 DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)

2543

2547

2548/\* DT helper macro to encode a node's IRQN to level 1 according to the multi-level scheme \*/

2549#define DT\_IRQN\_L1\_INTERNAL(node\_id, idx) DT\_IRQ\_BY\_IDX(node\_id, idx, irq)

2550/\* DT helper macro to encode a node's IRQN to level 2 according to the multi-level scheme \*/

2551#define DT\_IRQN\_L2\_INTERNAL(node\_id, idx) \

2552 (IRQ\_TO\_L2(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | DT\_IRQ(DT\_IRQ\_INTC(node\_id), irq))

2553/\* DT helper macro to encode a node's IRQN to level 3 according to the multi-level scheme \*/

2554#define DT\_IRQN\_L3\_INTERNAL(node\_id, idx) \

2555 (IRQ\_TO\_L3(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2556 IRQ\_TO\_L2(DT\_IRQ(DT\_IRQ\_INTC(node\_id), irq)) | \

2557 DT\_IRQ(DT\_IRQ\_INTC(DT\_IRQ\_INTC(node\_id)), irq))

2558/\* DT helper macro for the macros above \*/

2559#define DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, level) DT\_CAT3(DT\_IRQN\_L, level, \_INTERNAL)(node\_id, idx)

2560

2565#define DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx) \

2566 DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, DT\_IRQ\_LEVEL(node\_id))

2567

2571

[ 2580](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)#define DT\_IRQN\_BY\_IDX(node\_id, idx) \

2581 COND\_CODE\_1(IS\_ENABLED(CONFIG\_MULTI\_LEVEL\_INTERRUPTS), \

2582 (DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx)), \

2583 (DT\_IRQ\_BY\_IDX(node\_id, idx, irq)))

2584

[ 2595](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)#define DT\_IRQN(node\_id) DT\_IRQN\_BY\_IDX(node\_id, 0)

2596

2600

2606

[ 2615](group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed)#define DT\_CHOSEN(prop) DT\_CAT(DT\_CHOSEN\_, prop)

2616

[ 2623](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)#define DT\_HAS\_CHOSEN(prop) IS\_ENABLED(DT\_CAT3(DT\_CHOSEN\_, prop, \_EXISTS))

2624

2628

2634

[ 2644](group__devicetree-generic-foreach.md#gad27b29ae71a3d3294984fd3bc721121d)#define DT\_FOREACH\_NODE(fn) DT\_FOREACH\_HELPER(fn)

2645

[ 2658](group__devicetree-generic-foreach.md#ga4e708120bf839568b1215a6c21c54eed)#define DT\_FOREACH\_NODE\_VARGS(fn, ...) DT\_FOREACH\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2659

[ 2671](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn) DT\_FOREACH\_OKAY\_HELPER(fn)

2672

[ 2687](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)#define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn, ...) DT\_FOREACH\_OKAY\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2688

[ 2732](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)#define DT\_FOREACH\_CHILD(node\_id, fn) \

2733 DT\_CAT(node\_id, \_FOREACH\_CHILD)(fn)

2734

[ 2775](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep) \

2776 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP)(fn, sep)

2777

[ 2793](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)#define DT\_FOREACH\_CHILD\_VARGS(node\_id, fn, ...) \

2794 DT\_CAT(node\_id, \_FOREACH\_CHILD\_VARGS)(fn, \_\_VA\_ARGS\_\_)

2795

[ 2811](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)#define DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep, ...) \

2812 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

2813

[ 2829](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn) \

2830 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY)(fn)

2831

[ 2848](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep) \

2849 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP)(fn, sep)

2850

[ 2870](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn, ...) \

2871 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS)(fn, \_\_VA\_ARGS\_\_)

2872

[ 2891](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep, ...) \

2892 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

2893

[ 2944](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn) \

2945 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM)(fn)

2946

[ 2989](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep) \

2990 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP)(fn, sep)

2991

[ 3012](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn, ...) \

3013 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3014

[ 3031](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)#define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep, ...) \

3032 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP\_VARGS)( \

3033 fn, sep, \_\_VA\_ARGS\_\_)

3034

[ 3088](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)#define DT\_FOREACH\_STATUS\_OKAY(compat, fn) \

3089 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3090 (DT\_CAT(DT\_FOREACH\_OKAY\_, compat)(fn)), \

3091 ())

3092

[ 3137](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3138 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3139 (DT\_CAT(DT\_FOREACH\_OKAY\_VARGS\_, \

3140 compat)(fn, \_\_VA\_ARGS\_\_)), \

3141 ())

3142

3146

3152

[ 3167](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)#define DT\_NODE\_EXISTS(node\_id) IS\_ENABLED(DT\_CAT(node\_id, \_EXISTS))

3168

[ 3190](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)#define DT\_NODE\_HAS\_STATUS(node\_id, status) \

3191 DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status)

3192

[ 3212](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat) \

3213 IS\_ENABLED(DT\_CAT(DT\_COMPAT\_HAS\_OKAY\_, compat))

3214

[ 3221](group__devicetree-generic-exist.md#ga45c268d7f0d604a72dc0bcf5cd0733b0)#define DT\_NUM\_INST\_STATUS\_OKAY(compat) \

3222 UTIL\_AND(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3223 UTIL\_CAT(DT\_N\_INST, DT\_DASH(compat, NUM\_OKAY)))

3224

[ 3252](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)#define DT\_NODE\_HAS\_COMPAT(node\_id, compat) \

3253 IS\_ENABLED(DT\_CAT3(node\_id, \_COMPAT\_MATCHES\_, compat))

3254

[ 3269](group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)#define DT\_NODE\_HAS\_COMPAT\_STATUS(node\_id, compat, status) \

3270 DT\_NODE\_HAS\_COMPAT(node\_id, compat) && DT\_NODE\_HAS\_STATUS(node\_id, status)

3271

[ 3285](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)#define DT\_NODE\_HAS\_PROP(node\_id, prop) \

3286 IS\_ENABLED(DT\_CAT4(node\_id, \_P\_, prop, \_EXISTS))

3287

3288

[ 3305](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell) \

3306 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, pha, \

3307 \_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

3308

[ 3318](group__devicetree-generic-exist.md#gaece280102681cbadf318c5dabfb3d719)#define DT\_PHA\_HAS\_CELL(node\_id, pha, cell) \

3319 DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)

3320

3324

3330

[ 3362](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)#define DT\_BUS(node\_id) DT\_CAT(node\_id, \_BUS)

3363

[ 3392](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)#define DT\_ON\_BUS(node\_id, bus) IS\_ENABLED(DT\_CAT3(node\_id, \_BUS\_, bus))

3393

3397

3403

[ 3410](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)#define DT\_DRV\_INST(inst) DT\_INST(inst, DT\_DRV\_COMPAT)

3411

[ 3419](group__devicetree-inst.md#ga176760ce1a019020b5465eebd4f44ff5)#define DT\_INST\_PARENT(inst) DT\_PARENT(DT\_DRV\_INST(inst))

3420

[ 3428](group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)#define DT\_INST\_GPARENT(inst) DT\_GPARENT(DT\_DRV\_INST(inst))

3429

[ 3439](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)#define DT\_INST\_CHILD(inst, child) \

3440 DT\_CHILD(DT\_DRV\_INST(inst), child)

3441

[ 3456](group__devicetree-inst.md#ga98f3fccc6f3004f72c3602a5f2b3a08e)#define DT\_INST\_FOREACH\_CHILD(inst, fn) \

3457 DT\_FOREACH\_CHILD(DT\_DRV\_INST(inst), fn)

3458

[ 3472](group__devicetree-inst.md#gae8d01eb2d6a576246f225a5cbbec34e5)#define DT\_INST\_FOREACH\_CHILD\_SEP(inst, fn, sep) \

3473 DT\_FOREACH\_CHILD\_SEP(DT\_DRV\_INST(inst), fn, sep)

3474

[ 3490](group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651)#define DT\_INST\_FOREACH\_CHILD\_VARGS(inst, fn, ...) \

3491 DT\_FOREACH\_CHILD\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3492

[ 3507](group__devicetree-inst.md#gac70fcf3052d9dfa949d7e197fece1413)#define DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS(inst, fn, sep, ...) \

3508 DT\_FOREACH\_CHILD\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

3509

[ 3521](group__devicetree-inst.md#gad416dd269b1af1e392ef81397b9bc814)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY(inst, fn) \

3522 DT\_FOREACH\_CHILD\_STATUS\_OKAY(DT\_DRV\_INST(inst), fn)

3523

[ 3538](group__devicetree-inst.md#gae28554827ab7aaac3578ef07747a589d)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(inst, fn, sep) \

3539 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(DT\_DRV\_INST(inst), fn, sep)

3540

[ 3554](group__devicetree-inst.md#gac6dd19b2b6e603c11701cd07daec73d3)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(inst, fn, ...) \

3555 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3556

[ 3572](group__devicetree-inst.md#ga236cca0984f1c701c9b4855111c6cb29)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(inst, fn, sep, ...) \

3573 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

3574

[ 3581](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2)#define DT\_INST\_ENUM\_IDX(inst, prop) \

3582 DT\_ENUM\_IDX(DT\_DRV\_INST(inst), prop)

3583

[ 3592](group__devicetree-inst.md#gafbf64148f9171ffd322f7689297e0da8)#define DT\_INST\_ENUM\_IDX\_OR(inst, prop, default\_idx\_value) \

3593 DT\_ENUM\_IDX\_OR(DT\_DRV\_INST(inst), prop, default\_idx\_value)

3594

[ 3603](group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601)#define DT\_INST\_ENUM\_HAS\_VALUE(inst, prop, value) \

3604 DT\_ENUM\_HAS\_VALUE(DT\_DRV\_INST(inst), prop, value)

3605

[ 3612](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)#define DT\_INST\_PROP(inst, prop) DT\_PROP(DT\_DRV\_INST(inst), prop)

3613

[ 3620](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365)#define DT\_INST\_PROP\_LEN(inst, prop) DT\_PROP\_LEN(DT\_DRV\_INST(inst), prop)

3621

[ 3631](group__devicetree-inst.md#ga2c51745f8d51b1d9cdfb1cde69911d48)#define DT\_INST\_PROP\_HAS\_IDX(inst, prop, idx) \

3632 DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx)

3633

[ 3642](group__devicetree-inst.md#ga75e13dcdbcc51da1334fa14653411dd8)#define DT\_INST\_PROP\_HAS\_NAME(inst, prop, name) \

3643 DT\_PROP\_HAS\_NAME(DT\_DRV\_INST(inst), prop, name)

3644

[ 3652](group__devicetree-inst.md#ga5b60f4ed4f5dadc5dd425f5905f23b00)#define DT\_INST\_PROP\_BY\_IDX(inst, prop, idx) \

3653 DT\_PROP\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3654

[ 3662](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)#define DT\_INST\_PROP\_OR(inst, prop, default\_value) \

3663 DT\_PROP\_OR(DT\_DRV\_INST(inst), prop, default\_value)

3664

[ 3672](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)#define DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value) \

3673 DT\_PROP\_LEN\_OR(DT\_DRV\_INST(inst), prop, default\_value)

3674

[ 3684](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484)#define DT\_INST\_STRING\_TOKEN(inst, prop) \

3685 DT\_STRING\_TOKEN(DT\_DRV\_INST(inst), prop)

3686

[ 3694](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5)#define DT\_INST\_STRING\_UPPER\_TOKEN(inst, prop) \

3695 DT\_STRING\_UPPER\_TOKEN(DT\_DRV\_INST(inst), prop)

3696

[ 3705](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228)#define DT\_INST\_STRING\_UNQUOTED(inst, prop) \

3706 DT\_STRING\_UNQUOTED(DT\_DRV\_INST(inst), prop)

3707

[ 3715](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97)#define DT\_INST\_STRING\_TOKEN\_BY\_IDX(inst, prop, idx) \

3716 DT\_STRING\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3717

[ 3725](group__devicetree-inst.md#ga4ceceec8375d70b40a4dec1a8ab5ee29)#define DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX(inst, prop, idx) \

3726 DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3727

[ 3735](group__devicetree-inst.md#gac5768077e2a3d14a69efc653cfc59d5d)#define DT\_INST\_STRING\_UNQUOTED\_BY\_IDX(inst, prop, idx) \

3736 DT\_STRING\_UNQUOTED\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3737

[ 3746](group__devicetree-inst.md#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)#define DT\_INST\_PROP\_BY\_PHANDLE(inst, ph, prop) \

3747 DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, ph, 0, prop)

3748

[ 3760](group__devicetree-inst.md#gad027963bdf159942cf6fb28b04e8d48e)#define DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop) \

3761 DT\_PROP\_BY\_PHANDLE\_IDX(DT\_DRV\_INST(inst), phs, idx, prop)

3762

[ 3771](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018)#define DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell) \

3772 DT\_PHA\_BY\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

3773

[ 3783](group__devicetree-inst.md#ga3db4c00e072bd93fa92e36907b2b5e86)#define DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value) \

3784 DT\_PHA\_BY\_IDX\_OR(DT\_DRV\_INST(inst), pha, idx, cell, default\_value)

3785

[ 3794](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8)#define DT\_INST\_PHA(inst, pha, cell) DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)

3795

[ 3804](group__devicetree-inst.md#ga491ad421602e41c4295bac61b595fc94)#define DT\_INST\_PHA\_OR(inst, pha, cell, default\_value) \

3805 DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, 0, cell, default\_value)

3806

[ 3816](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8)#define DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell) \

3817 DT\_PHA\_BY\_NAME(DT\_DRV\_INST(inst), pha, name, cell)

3818

[ 3828](group__devicetree-inst.md#gaaebc5c643b60319f7e767e46ca226729)#define DT\_INST\_PHA\_BY\_NAME\_OR(inst, pha, name, cell, default\_value) \

3829 DT\_PHA\_BY\_NAME\_OR(DT\_DRV\_INST(inst), pha, name, cell, default\_value)

3830

[ 3839](group__devicetree-inst.md#ga64d8ddaad8b2d3852e30686d3adf6551)#define DT\_INST\_PHANDLE\_BY\_NAME(inst, pha, name) \

3840 DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), pha, name) \

3841

3842

[ 3851](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx) \

3852 DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3853

[ 3862](group__devicetree-inst.md#ga81c10f478c86e5a4c18eb7a990447137)#define DT\_INST\_PHANDLE(inst, prop) DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, 0)

3863

[ 3871](group__devicetree-inst.md#ga26bbff9ebaed549140d2530a0b99e8a4)#define DT\_INST\_REG\_HAS\_IDX(inst, idx) DT\_REG\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

3872

[ 3879](group__devicetree-inst.md#ga0fe0403821883598da6cfad4f3962115)#define DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx) DT\_REG\_ADDR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

3880

[ 3887](group__devicetree-inst.md#gab1152c9f069c69b0269c1a4e744b9dd9)#define DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx) \

3888 DT\_REG\_SIZE\_BY\_IDX(DT\_DRV\_INST(inst), idx)

3889

[ 3896](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c)#define DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name) \

3897 DT\_REG\_ADDR\_BY\_NAME(DT\_DRV\_INST(inst), name)

3898

[ 3911](group__devicetree-inst.md#ga8af83c4c65e607b93aa60a690295d625)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_U64(inst, name) \

3912 DT\_U64\_C(DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name))

3913

[ 3920](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714)#define DT\_INST\_REG\_SIZE\_BY\_NAME(inst, name) \

3921 DT\_REG\_SIZE\_BY\_NAME(DT\_DRV\_INST(inst), name)

3922

[ 3928](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7)#define DT\_INST\_REG\_ADDR(inst) DT\_INST\_REG\_ADDR\_BY\_IDX(inst, 0)

3929

[ 3941](group__devicetree-inst.md#gaba47dcabd8754eda87e35efd7289f976)#define DT\_INST\_REG\_ADDR\_U64(inst) DT\_U64\_C(DT\_INST\_REG\_ADDR(inst))

3942

[ 3948](group__devicetree-inst.md#gaa7cea29435e1db59470302abb5ee88dd)#define DT\_INST\_REG\_SIZE(inst) DT\_INST\_REG\_SIZE\_BY\_IDX(inst, 0)

3949

[ 3956](group__devicetree-inst.md#ga5c06043fd17c891e2cbbe0508248b638)#define DT\_INST\_IRQ\_LEVEL(inst) DT\_IRQ\_LEVEL(DT\_DRV\_INST(inst))

3957

[ 3965](group__devicetree-inst.md#gad0d69a61ad842aa1dc3a5d4a304c3f2f)#define DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell) \

3966 DT\_IRQ\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

3967

[ 3974](group__devicetree-inst.md#gab29f18e52d7475245c9fbeb4cd8e7769)#define DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx) \

3975 DT\_IRQ\_INTC\_BY\_IDX(DT\_DRV\_INST(inst), idx)

3976

[ 3983](group__devicetree-inst.md#gadd0f339e10b071da34d44922ad0c7bfd)#define DT\_INST\_IRQ\_INTC\_BY\_NAME(inst, name) \

3984 DT\_IRQ\_INTC\_BY\_NAME(DT\_DRV\_INST(inst), name)

3985

[ 3993](group__devicetree-inst.md#gabf127c8370af849d2b5560e87ee04809)#define DT\_INST\_IRQ\_INTC(inst) \

3994 DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, 0)

3995

[ 4003](group__devicetree-inst.md#ga1ff6f24f9c97d4b611e4bf50ce5175d3)#define DT\_INST\_IRQ\_BY\_NAME(inst, name, cell) \

4004 DT\_IRQ\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

4005

[ 4012](group__devicetree-inst.md#ga789eb58422bab7b3a79b487c4a8a82d6)#define DT\_INST\_IRQ(inst, cell) DT\_INST\_IRQ\_BY\_IDX(inst, 0, cell)

4013

[ 4019](group__devicetree-inst.md#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)#define DT\_INST\_IRQN(inst) DT\_IRQN(DT\_DRV\_INST(inst))

4020

[ 4027](group__devicetree-inst.md#gaeb0c023f53ed87a6707bbca8ba05ce45)#define DT\_INST\_IRQN\_BY\_IDX(inst, idx) DT\_IRQN\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4028

[ 4034](group__devicetree-inst.md#gacecb46743315738dcd9a0765ea78276a)#define DT\_INST\_BUS(inst) DT\_BUS(DT\_DRV\_INST(inst))

4035

[ 4043](group__devicetree-inst.md#ga7a29bda946b399a7af92ec9cd09b4e98)#define DT\_INST\_ON\_BUS(inst, bus) DT\_ON\_BUS(DT\_DRV\_INST(inst), bus)

4044

[ 4054](group__devicetree-inst.md#ga79fd00d1ece5538f7705c241ab869ea8)#define DT\_INST\_STRING\_TOKEN\_OR(inst, name, default\_value) \

4055 DT\_STRING\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4056

[ 4065](group__devicetree-inst.md#ga72981780b2ede73c49ef9e5a7c6247c2)#define DT\_INST\_STRING\_UPPER\_TOKEN\_OR(inst, name, default\_value) \

4066 DT\_STRING\_UPPER\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4067

[ 4076](group__devicetree-inst.md#ga56bc0c0a46f6be421082119604cde643)#define DT\_INST\_STRING\_UNQUOTED\_OR(inst, name, default\_value) \

4077 DT\_STRING\_UNQUOTED\_OR(DT\_DRV\_INST(inst), name, default\_value)

4078

4079/\*

4080 \* @brief Test if any enabled node with the given compatible is on

4081 \* the given bus type

4082 \*

4083 \* This is like DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(), except it can also

4084 \* be useful for handling multiple compatibles in single source file.

4085 \*

4086 \* Example devicetree overlay:

4087 \*

4088 \* @code{.dts}

4089 \* &i2c0 {

4090 \* temp: temperature-sensor@76 {

4091 \* compatible = "vnd,some-sensor";

4092 \* reg = <0x76>;

4093 \* };

4094 \* };

4095 \* @endcode

4096 \*

4097 \* Example usage, assuming `i2c0` is an I2C bus controller node, and

4098 \* therefore `temp` is on an I2C bus:

4099 \*

4100 \* @code{.c}

4101 \* DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(vnd\_some\_sensor, i2c) // 1

4102 \* @endcode

4103 \*

4104 \* @param compat lowercase-and-underscores compatible, without quotes

4105 \* @param bus a binding's bus type as a C token, lowercased and without quotes

4106 \* @return 1 if any enabled node with that compatible is on that bus type,

4107 \* 0 otherwise

4108 \*/

[ 4109](group__devicetree-inst.md#ga1727af4beed08b248a98ad68bc5f1027)#define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus) \

4110 IS\_ENABLED(DT\_CAT4(DT\_COMPAT\_, compat, \_BUS\_, bus))

4111

[ 4144](group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)#define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus) \

4145 DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(DT\_DRV\_COMPAT, bus)

4146

[ 4191](group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735)#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop) \

4192 (DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(DT\_INST\_NODE\_HAS\_PROP\_AND\_OR, prop) 0)

4193

[ 4259](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)#define DT\_INST\_FOREACH\_STATUS\_OKAY(fn) \

4260 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4261 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_, \

4262 DT\_DRV\_COMPAT)(fn)), \

4263 ())

4264

[ 4276](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38)#define DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(fn, ...) \

4277 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4278 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

4279 DT\_DRV\_COMPAT)(fn, \_\_VA\_ARGS\_\_)), \

4280 ())

4281

[ 4292](group__devicetree-inst.md#gaf163f2f85b3893ca46c87f0fcbe65255)#define DT\_INST\_FOREACH\_PROP\_ELEM(inst, prop, fn) \

4293 DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)

4294

[ 4307](group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP(inst, prop, fn, sep) \

4308 DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)

4309

[ 4324](group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)#define DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS(inst, prop, fn, ...) \

4325 DT\_FOREACH\_PROP\_ELEM\_VARGS(DT\_DRV\_INST(inst), prop, fn, \_\_VA\_ARGS\_\_)

4326

[ 4344](group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(inst, prop, fn, sep, ...) \

4345 DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(DT\_DRV\_INST(inst), prop, fn, sep, \

4346 \_\_VA\_ARGS\_\_)

4347

[ 4354](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)#define DT\_INST\_NODE\_HAS\_PROP(inst, prop) \

4355 DT\_NODE\_HAS\_PROP(DT\_DRV\_INST(inst), prop)

4356

[ 4367](group__devicetree-inst.md#gae054b89701ec9fae577320fb7b9cae1e)#define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell) \

4368 DT\_PHA\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4369

[ 4379](group__devicetree-inst.md#gab8083dae430aeb93a967bbf98aa9eefc)#define DT\_INST\_PHA\_HAS\_CELL(inst, pha, cell) \

4380 DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, 0, cell)

4381

[ 4389](group__devicetree-inst.md#gabb45132ef78818512c02bdf1f5a38068)#define DT\_INST\_IRQ\_HAS\_IDX(inst, idx) DT\_IRQ\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4390

[ 4399](group__devicetree-inst.md#gab176ff07912cea915c811406e8f5e386)#define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell) \

4400 DT\_IRQ\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), idx, cell)

4401

[ 4409](group__devicetree-inst.md#gabec43df3451bd917120b283d76c57054)#define DT\_INST\_IRQ\_HAS\_CELL(inst, cell) \

4410 DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, 0, cell)

4411

[ 4418](group__devicetree-inst.md#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)#define DT\_INST\_IRQ\_HAS\_NAME(inst, name) \

4419 DT\_IRQ\_HAS\_NAME(DT\_DRV\_INST(inst), name)

4420

4424

4426

4427#define DT\_PATH\_INTERNAL(...) \

4428 UTIL\_CAT(DT\_ROOT, MACRO\_MAP\_CAT(DT\_S\_PREFIX, \_\_VA\_ARGS\_\_))

4434#define DT\_S\_PREFIX(name) \_S\_##name

4435

4450#define DT\_CAT(a1, a2) a1 ## a2

4452#define DT\_CAT3(a1, a2, a3) a1 ## a2 ## a3

4454#define DT\_CAT4(a1, a2, a3, a4) a1 ## a2 ## a3 ## a4

4456#define DT\_CAT5(a1, a2, a3, a4, a5) a1 ## a2 ## a3 ## a4 ## a5

4458#define DT\_CAT6(a1, a2, a3, a4, a5, a6) a1 ## a2 ## a3 ## a4 ## a5 ## a6

4460#define DT\_CAT7(a1, a2, a3, a4, a5, a6, a7) \

4461 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7

4463#define DT\_CAT8(a1, a2, a3, a4, a5, a6, a7, a8) \

4464 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7 ## a8

4465/\*

4466 \* If you need to define a bigger DT\_CATN(), do so here. Don't leave

4467 \* any "holes" of undefined macros, please.

4468 \*/

4469

4471#define DT\_DASH(...) MACRO\_MAP\_CAT(DT\_DASH\_PREFIX, \_\_VA\_ARGS\_\_)

4473#define DT\_DASH\_PREFIX(name) \_##name

4475#define DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status) \

4476 IS\_ENABLED(DT\_CAT3(node\_id, \_STATUS\_, status))

4477

4479#define DT\_INST\_NODE\_HAS\_PROP\_AND\_OR(inst, prop) \

4480 DT\_INST\_NODE\_HAS\_PROP(inst, prop) ||

4481

4486#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

4487#define DT\_U64\_C(\_v) (\_v)

4488#else

4489#define DT\_U64\_C(\_v) UINT64\_C(\_v)

4490#endif

4491

4493

4494/\* have these last so they have access to all previously defined macros \*/

4495#include <[zephyr/devicetree/io-channels.h](io-channels_8h.md)>

4496#include <[zephyr/devicetree/clocks.h](clocks_8h.md)>

4497#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h.md)>

4498#include <[zephyr/devicetree/spi.h](devicetree_2spi_8h.md)>

4499#include <[zephyr/devicetree/dma.h](devicetree_2dma_8h.md)>

4500#include <[zephyr/devicetree/pwms.h](pwms_8h.md)>

4501#include <[zephyr/devicetree/fixed-partitions.h](fixed-partitions_8h.md)>

4502#include <[zephyr/devicetree/ordinals.h](ordinals_8h.md)>

4503#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

4504#include <[zephyr/devicetree/can.h](devicetree_2can_8h.md)>

4505#include <[zephyr/devicetree/reset.h](devicetree_2reset_8h.md)>

4506#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h.md)>

4507

4508#endif /\* DEVICETREE\_H \*/

[clocks.h](clocks_8h.md)

Clocks Devicetree macro public API header file.

[can.h](devicetree_2can_8h.md)

CAN devicetree macro public API header file.

[dma.h](devicetree_2dma_8h.md)

DMA Devicetree macro public API header file.

[gpio.h](devicetree_2gpio_8h.md)

GPIO Devicetree macro public API header file.

[mbox.h](devicetree_2mbox_8h.md)

MBOX Devicetree macro public API header file.

[pinctrl.h](devicetree_2pinctrl_8h.md)

Devicetree pin control helpers.

[reset.h](devicetree_2reset_8h.md)

Reset Controller Devicetree macro public API header file.

[spi.h](devicetree_2spi_8h.md)

SPI Devicetree macro public API header file.

[fixed-partitions.h](fixed-partitions_8h.md)

Flash Devicetree macro public API header file.

[io-channels.h](io-channels_8h.md)

IO channels devicetree macro public API header file.

[irq\_multilevel.h](irq__multilevel_8h.md)

Public interface for multi-level interrupts.

[ordinals.h](ordinals_8h.md)

Devicetree node dependency ordinals.

[pwms.h](pwms_8h.md)

PWMs Devicetree macro public API header file.

[stdint.h](stdint_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree.h](devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
