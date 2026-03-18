---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/devicetree_8h_source.html
original_path: doxygen/html/devicetree_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

19#include <zephyr/devicetree\_generated.h>

20#include <[zephyr/irq\_multilevel.h](irq__multilevel_8h.md)>

21

22#if !defined(\_LINKER) && !defined(\_ASMLANGUAGE)

23#include <[stdint.h](stdint_8h.md)>

24#endif

25

26#include <[zephyr/sys/util.h](util_8h.md)>

27

36

37/\*

38 \* Property suffixes

39 \* -----------------

40 \*

41 \* These are the optional parts that come after the \_P\_<property>

42 \* part in DT\_N\_<path-id>\_P\_<property-id> macros, or the "prop-suf"

43 \* nonterminal in the DT guide's macros.bnf file.

44 \*

45 \* Before adding new ones, check this list to avoid conflicts. If any

46 \* are missing from this list, please add them. It should be complete.

47 \*

48 \* \_ENUM\_IDX: property's value as an index into bindings enum

49 \* \_ENUM\_VAL\_<val>\_EXISTS property's value as a token exists

50 \* \_ENUM\_TOKEN: property's value as a token into bindings enum (string

51 \* enum values are identifiers) [deprecated, use \_STRING\_TOKEN]

52 \* \_ENUM\_UPPER\_TOKEN: like \_ENUM\_TOKEN, but uppercased [deprecated, use

53 \* \_STRING\_UPPER\_TOKEN]

54 \* \_EXISTS: property is defined

55 \* \_FOREACH\_PROP\_ELEM: helper for "iterating" over values in the property

56 \* \_FOREACH\_PROP\_ELEM\_VARGS: foreach functions with variable number of arguments

57 \* \_IDX\_<i>: logical index into property

58 \* \_IDX\_<i>\_EXISTS: logical index into property is defined

59 \* \_IDX\_<i>\_PH: phandle array's phandle by index (or phandle, phandles)

60 \* \_IDX\_<i>\_STRING\_TOKEN: string array element value as a token

61 \* \_IDX\_<i>\_STRING\_UPPER\_TOKEN: string array element value as a uppercased token

62 \* \_IDX <i>\_STRING\_UNQUOTED: string array element value as a sequence of tokens, with no quotes

63 \* \_IDX\_<i>\_VAL\_<val>: phandle array's specifier value by index

64 \* \_IDX\_<i>\_VAL\_<val>\_EXISTS: cell value exists, by index

65 \* \_LEN: property logical length

66 \* \_NAME\_<name>\_PH: phandle array's phandle by name

67 \* \_NAME\_<name>\_VAL\_<val>: phandle array's property specifier by name

68 \* \_NAME\_<name>\_VAL\_<val>\_EXISTS: cell value exists, by name

69 \* \_STRING\_TOKEN: string property's value as a token

70 \* \_STRING\_UPPER\_TOKEN: like \_STRING\_TOKEN, but uppercased

71 \* \_STRING\_UNQUOTED: string property's value as a sequence of tokens, with no quotes

72 \*/

73

79

[ 87](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)#define DT\_INVALID\_NODE \_

88

[ 92](group__devicetree-generic-id.md#gad65aa36621281687b22fa5d72db33e86)#define DT\_ROOT DT\_N

93

[ 144](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)#define DT\_PATH(...) DT\_PATH\_INTERNAL(\_\_VA\_ARGS\_\_)

145

[ 200](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)#define DT\_NODELABEL(label) DT\_CAT(DT\_N\_NODELABEL\_, label)

201

[ 240](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)#define DT\_ALIAS(alias) DT\_CAT(DT\_N\_ALIAS\_, alias)

241

[ 336](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)#define DT\_INST(inst, compat) UTIL\_CAT(DT\_N\_INST, DT\_DASH(inst, compat))

337

[ 361](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)#define DT\_PARENT(node\_id) DT\_CAT(node\_id, \_PARENT)

362

[ 386](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)#define DT\_GPARENT(node\_id) DT\_PARENT(DT\_PARENT(node\_id))

387

[ 423](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)#define DT\_CHILD(node\_id, child) UTIL\_CAT(node\_id, DT\_S\_PREFIX(child))

424

[ 466](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat) \

467 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

468 (DT\_INST(0, compat)), \

469 (DT\_INVALID\_NODE))

470

[ 498](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)#define DT\_NODE\_PATH(node\_id) DT\_CAT(node\_id, \_PATH)

499

[ 524](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)#define DT\_NODE\_FULL\_NAME(node\_id) DT\_CAT(node\_id, \_FULL\_NAME)

525

[ 552](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)#define DT\_NODE\_CHILD\_IDX(node\_id) DT\_CAT(node\_id, \_CHILD\_IDX)

553

[ 560](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)#define DT\_CHILD\_NUM(node\_id) DT\_CAT(node\_id, \_CHILD\_NUM)

561

562

[ 570](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)#define DT\_CHILD\_NUM\_STATUS\_OKAY(node\_id) \

571 DT\_CAT(node\_id, \_CHILD\_NUM\_STATUS\_OKAY)

572

[ 593](group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)#define DT\_SAME\_NODE(node\_id1, node\_id2) \

594 (DT\_DEP\_ORD(node\_id1) == (DT\_DEP\_ORD(node\_id2)))

595

[ 620](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)#define DT\_NODELABEL\_STRING\_ARRAY(node\_id) \

621 { DT\_FOREACH\_NODELABEL(node\_id, DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL) }

622

626

632

[ 663](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)#define DT\_PROP(node\_id, prop) DT\_CAT3(node\_id, \_P\_, prop)

664

[ 697](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)#define DT\_PROP\_LEN(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_LEN)

698

[ 713](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value) \

714 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

715 (DT\_PROP\_LEN(node\_id, prop)), (default\_value))

716

[ 737](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx) \

738 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_EXISTS))

739

[ 772](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)#define DT\_PROP\_HAS\_NAME(node\_id, prop, name) \

773 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_NAME\_, name, \_EXISTS))

774

[ 809](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)#define DT\_PROP\_BY\_IDX(node\_id, prop, idx) \

810 DT\_CAT5(node\_id, \_P\_, prop, \_IDX\_, idx)

811

[ 825](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)#define DT\_PROP\_OR(node\_id, prop, default\_value) \

826 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

827 (DT\_PROP(node\_id, prop)), (default\_value))

828

[ 869](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)#define DT\_ENUM\_IDX(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_ENUM\_IDX)

870

[ 885](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value) \

886 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

887 (DT\_ENUM\_IDX(node\_id, prop)), (default\_idx\_value))

888

[ 897](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)#define DT\_ENUM\_HAS\_VALUE(node\_id, prop, value) \

898 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_ENUM\_VAL\_, value, \_EXISTS))

899

[ 959](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)#define DT\_STRING\_TOKEN(node\_id, prop) \

960 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_TOKEN)

961

[ 975](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value) \

976 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

977 (DT\_STRING\_TOKEN(node\_id, prop)), (default\_value))

978

[ 1036](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop) \

1037 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UPPER\_TOKEN)

1038

[ 1053](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value) \

1054 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1055 (DT\_STRING\_UPPER\_TOKEN(node\_id, prop)), (default\_value))

1056

[ 1097](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)#define DT\_STRING\_UNQUOTED(node\_id, prop) \

1098 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UNQUOTED)

1099

[ 1114](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)#define DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value) \

1115 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1116 (DT\_STRING\_UNQUOTED(node\_id, prop)), (default\_value))

1117

[ 1165](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1166 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_TOKEN)

1167

[ 1215](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1216 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UPPER\_TOKEN)

1217

[ 1258](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)#define DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx) \

1259 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UNQUOTED)

1260

1261/\*

1262 \* phandle properties

1263 \*

1264 \* These are special-cased to manage the impedance mismatch between

1265 \* phandles, which are just uint32\_t node properties that only make sense

1266 \* within the tree itself, and C values.

1267 \*/

1268

[ 1314](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop) \

1315 DT\_PROP(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop)

1316

[ 1336](group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b)#define DT\_PROP\_BY\_PHANDLE\_IDX\_OR(node\_id, phs, idx, prop, default\_value) \

1337 DT\_PROP\_OR(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop, default\_value)

1338

[ 1350](group__devicetree-generic-prop.md#gabc1b099dda97fb03a9259a8b21fc04d2)#define DT\_PROP\_BY\_PHANDLE(node\_id, ph, prop) \

1351 DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)

1352

[ 1407](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell) \

1408 DT\_CAT7(node\_id, \_P\_, pha, \_IDX\_, idx, \_VAL\_, cell)

1409

[ 1433](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value) \

1434 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_IDX\_, idx, \_VAL\_, cell), default\_value)

1435

[ 1443](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)#define DT\_PHA(node\_id, pha, cell) DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)

1444

[ 1459](group__devicetree-generic-prop.md#ga886559b058b24164b62ab95215d860bd)#define DT\_PHA\_OR(node\_id, pha, cell, default\_value) \

1460 DT\_PHA\_BY\_IDX\_OR(node\_id, pha, 0, cell, default\_value)

1461

[ 1502](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell) \

1503 DT\_CAT7(node\_id, \_P\_, pha, \_NAME\_, name, \_VAL\_, cell)

1504

[ 1526](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value) \

1527 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_NAME\_, name, \_VAL\_, cell), default\_value)

1528

[ 1576](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name) \

1577 DT\_CAT6(node\_id, \_P\_, pha, \_NAME\_, name, \_PH)

1578

[ 1628](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx) \

1629 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_PH)

1630

[ 1642](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)#define DT\_PHANDLE(node\_id, prop) DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)

1643

1647

1653

[ 1690](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc)#define DT\_NUM\_RANGES(node\_id) DT\_CAT(node\_id, \_RANGES\_NUM)

1691

[ 1744](group__devicetree-ranges-prop.md#gac6f54058c58b06935bd2deae9f1ec2db)#define DT\_RANGES\_HAS\_IDX(node\_id, idx) \

1745 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_EXISTS))

1746

[ 1799](group__devicetree-ranges-prop.md#ga3730c9176911bd8cc762f447eb020ecd)#define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx) \

1800 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS\_EXISTS))

1801

[ 1839](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx) \

1840 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS)

1841

[ 1888](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

1889 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_ADDRESS)

1890

[ 1937](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

1938 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_PARENT\_BUS\_ADDRESS)

1939

[ 1986](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx) \

1987 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_LENGTH)

1988

[ 2028](group__devicetree-ranges-prop.md#ga4c71a8adcfe6c53b480775510c92a632)#define DT\_FOREACH\_RANGE(node\_id, fn) \

2029 DT\_CAT(node\_id, \_FOREACH\_RANGE)(fn)

2030

2034

2040

[ 2076](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747)#define DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx) \

2077 DT\_CAT3(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx)

2078

[ 2091](group__devicetree-generic-vendor.md#gabfa4130fa24457c457961caa7e2c6276)#define DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx) \

2092 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx, \_EXISTS))

2093

[ 2108](group__devicetree-generic-vendor.md#gaa71b1152516847d51582b9b23c472f3d)#define DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2109 COND\_CODE\_1(DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx), \

2110 (DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)), (default\_value))

2111

[ 2120](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)#define DT\_NODE\_VENDOR\_OR(node\_id, default\_value) \

2121 DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, 0, default\_value)

2122

[ 2152](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)#define DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx) \

2153 DT\_CAT3(node\_id, \_COMPAT\_MODEL\_IDX\_, idx)

2154

[ 2167](group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)#define DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx) \

2168 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_MODEL\_IDX\_, idx, \_EXISTS))

2169

[ 2184](group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)#define DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2185 COND\_CODE\_1(DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx), \

2186 (DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)), (default\_value))

2187

[ 2196](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)#define DT\_NODE\_MODEL\_OR(node\_id, default\_value) \

2197 DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, 0, default\_value)

2198

2202

2208

[ 2216](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)#define DT\_NUM\_REGS(node\_id) DT\_CAT(node\_id, \_REG\_NUM)

2217

[ 2229](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)#define DT\_REG\_HAS\_IDX(node\_id, idx) \

2230 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_EXISTS))

2231

[ 2243](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)#define DT\_REG\_HAS\_NAME(node\_id, name) \

2244 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_EXISTS))

2245

[ 2252](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx) \

2253 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

2254

[ 2266](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx) \

2267 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE)

2268

[ 2276](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)#define DT\_REG\_ADDR(node\_id) DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)

2277

[ 2288](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)#define DT\_REG\_ADDR\_U64(node\_id) DT\_U64\_C(DT\_REG\_ADDR(node\_id))

2289

[ 2297](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)#define DT\_REG\_SIZE(node\_id) DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)

2298

[ 2305](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name) \

2306 DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS)

2307

[ 2316](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)#define DT\_REG\_ADDR\_BY\_NAME\_OR(node\_id, name, default\_value) \

2317 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2318 (DT\_REG\_ADDR\_BY\_NAME(node\_id, name)), (default\_value))

2319

[ 2332](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)#define DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name) \

2333 DT\_U64\_C(DT\_REG\_ADDR\_BY\_NAME(node\_id, name))

2334

[ 2341](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name) \

2342 DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE)

2343

[ 2352](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)#define DT\_REG\_SIZE\_BY\_NAME\_OR(node\_id, name, default\_value) \

2353 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2354 (DT\_REG\_SIZE\_BY\_NAME(node\_id, name)), (default\_value))

2355

2356

2360

2366

[ 2375](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)#define DT\_NUM\_IRQS(node\_id) DT\_CAT(node\_id, \_IRQ\_NUM)

2376

[ 2401](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)#define DT\_NUM\_NODELABELS(node\_id) DT\_CAT(node\_id, \_NODELABEL\_NUM)

2402

[ 2409](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)#define DT\_IRQ\_LEVEL(node\_id) DT\_CAT(node\_id, \_IRQ\_LEVEL)

2410

[ 2421](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)#define DT\_IRQ\_HAS\_IDX(node\_id, idx) \

2422 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_EXISTS))

2423

[ 2434](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell) \

2435 IS\_ENABLED(DT\_CAT6(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

2436

[ 2444](group__devicetree-interrupts-prop.md#gab9c94ee39db7913598a755c6172fe036)#define DT\_IRQ\_HAS\_CELL(node\_id, cell) DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)

2445

[ 2455](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)#define DT\_IRQ\_HAS\_NAME(node\_id, name) \

2456 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_VAL\_irq\_EXISTS))

2457

[ 2493](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell) \

2494 DT\_CAT5(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell)

2495

[ 2511](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)#define DT\_IRQ\_BY\_NAME(node\_id, name, cell) \

2512 DT\_CAT5(node\_id, \_IRQ\_NAME\_, name, \_VAL\_, cell)

2513

[ 2521](group__devicetree-interrupts-prop.md#gabf60fbd528d300a26c0b4e66fe80a53f)#define DT\_IRQ(node\_id, cell) DT\_IRQ\_BY\_IDX(node\_id, 0, cell)

2522

[ 2565](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx) \

2566 DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_CONTROLLER)

2567

[ 2612](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)#define DT\_IRQ\_INTC\_BY\_NAME(node\_id, name) \

2613 DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_CONTROLLER)

2614

[ 2654](group__devicetree-interrupts-prop.md#ga11d2680614de65fd8cb4a3909e93e9c9)#define DT\_IRQ\_INTC(node\_id) \

2655 DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)

2656

2660

2661/\* DT helper macro to encode a node's IRQN to level 1 according to the multi-level scheme \*/

2662#define DT\_IRQN\_L1\_INTERNAL(node\_id, idx) DT\_IRQ\_BY\_IDX(node\_id, idx, irq)

2663/\* DT helper macro to encode a node's IRQN to level 2 according to the multi-level scheme \*/

2664#define DT\_IRQN\_L2\_INTERNAL(node\_id, idx) \

2665 (IRQ\_TO\_L2(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2666 DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq))

2667/\* DT helper macro to encode a node's IRQN to level 3 according to the multi-level scheme \*/

2668#define DT\_IRQN\_L3\_INTERNAL(node\_id, idx) \

2669 (IRQ\_TO\_L3(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2670 IRQ\_TO\_L2(DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq)) | \

2671 DT\_IRQ(DT\_IRQ\_INTC(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)), irq))

2672/\* DT helper macro for the macros above \*/

2673#define DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, level) DT\_CAT3(DT\_IRQN\_L, level, \_INTERNAL)(node\_id, idx)

2674

2679#define DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx) \

2680 DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, DT\_IRQ\_LEVEL(node\_id))

2681

2685

[ 2694](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)#define DT\_IRQN\_BY\_IDX(node\_id, idx) \

2695 COND\_CODE\_1(IS\_ENABLED(CONFIG\_MULTI\_LEVEL\_INTERRUPTS), \

2696 (DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx)), \

2697 (DT\_IRQ\_BY\_IDX(node\_id, idx, irq)))

2698

[ 2709](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)#define DT\_IRQN(node\_id) DT\_IRQN\_BY\_IDX(node\_id, 0)

2710

2714

2720

[ 2729](group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed)#define DT\_CHOSEN(prop) DT\_CAT(DT\_CHOSEN\_, prop)

2730

[ 2737](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)#define DT\_HAS\_CHOSEN(prop) IS\_ENABLED(DT\_CAT3(DT\_CHOSEN\_, prop, \_EXISTS))

2738

2742

2748

[ 2758](group__devicetree-generic-foreach.md#gad27b29ae71a3d3294984fd3bc721121d)#define DT\_FOREACH\_NODE(fn) DT\_FOREACH\_HELPER(fn)

2759

[ 2772](group__devicetree-generic-foreach.md#ga4e708120bf839568b1215a6c21c54eed)#define DT\_FOREACH\_NODE\_VARGS(fn, ...) DT\_FOREACH\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2773

[ 2785](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn) DT\_FOREACH\_OKAY\_HELPER(fn)

2786

[ 2801](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)#define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn, ...) DT\_FOREACH\_OKAY\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2802

[ 2846](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)#define DT\_FOREACH\_CHILD(node\_id, fn) \

2847 DT\_CAT(node\_id, \_FOREACH\_CHILD)(fn)

2848

[ 2889](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep) \

2890 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP)(fn, sep)

2891

[ 2907](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)#define DT\_FOREACH\_CHILD\_VARGS(node\_id, fn, ...) \

2908 DT\_CAT(node\_id, \_FOREACH\_CHILD\_VARGS)(fn, \_\_VA\_ARGS\_\_)

2909

[ 2925](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)#define DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep, ...) \

2926 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

2927

[ 2943](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn) \

2944 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY)(fn)

2945

[ 2962](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep) \

2963 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP)(fn, sep)

2964

[ 2984](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn, ...) \

2985 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS)(fn, \_\_VA\_ARGS\_\_)

2986

[ 3005](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep, ...) \

3006 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

3007

[ 3058](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn) \

3059 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM)(fn)

3060

[ 3103](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep) \

3104 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP)(fn, sep)

3105

[ 3126](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn, ...) \

3127 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3128

[ 3145](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)#define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep, ...) \

3146 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP\_VARGS)( \

3147 fn, sep, \_\_VA\_ARGS\_\_)

3148

[ 3202](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)#define DT\_FOREACH\_STATUS\_OKAY(compat, fn) \

3203 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3204 (DT\_CAT(DT\_FOREACH\_OKAY\_, compat)(fn)), \

3205 ())

3206

[ 3251](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3252 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3253 (DT\_CAT(DT\_FOREACH\_OKAY\_VARGS\_, \

3254 compat)(fn, \_\_VA\_ARGS\_\_)), \

3255 ())

3256

[ 3295](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)#define DT\_FOREACH\_NODELABEL(node\_id, fn) DT\_CAT(node\_id, \_FOREACH\_NODELABEL)(fn)

3296

[ 3334](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)#define DT\_FOREACH\_NODELABEL\_VARGS(node\_id, fn, ...) \

3335 DT\_CAT(node\_id, \_FOREACH\_NODELABEL\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3336

3340

3346

[ 3361](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)#define DT\_NODE\_EXISTS(node\_id) IS\_ENABLED(DT\_CAT(node\_id, \_EXISTS))

3362

[ 3384](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)#define DT\_NODE\_HAS\_STATUS(node\_id, status) \

3385 DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status)

3386

[ 3406](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat) \

3407 IS\_ENABLED(DT\_CAT(DT\_COMPAT\_HAS\_OKAY\_, compat))

3408

[ 3415](group__devicetree-generic-exist.md#ga45c268d7f0d604a72dc0bcf5cd0733b0)#define DT\_NUM\_INST\_STATUS\_OKAY(compat) \

3416 UTIL\_AND(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3417 UTIL\_CAT(DT\_N\_INST, DT\_DASH(compat, NUM\_OKAY)))

3418

[ 3446](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)#define DT\_NODE\_HAS\_COMPAT(node\_id, compat) \

3447 IS\_ENABLED(DT\_CAT3(node\_id, \_COMPAT\_MATCHES\_, compat))

3448

[ 3463](group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)#define DT\_NODE\_HAS\_COMPAT\_STATUS(node\_id, compat, status) \

3464 UTIL\_AND(DT\_NODE\_HAS\_COMPAT(node\_id, compat), DT\_NODE\_HAS\_STATUS(node\_id, status))

3465

[ 3479](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)#define DT\_NODE\_HAS\_PROP(node\_id, prop) \

3480 IS\_ENABLED(DT\_CAT4(node\_id, \_P\_, prop, \_EXISTS))

3481

3482

[ 3499](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell) \

3500 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, pha, \

3501 \_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

3502

[ 3512](group__devicetree-generic-exist.md#gaece280102681cbadf318c5dabfb3d719)#define DT\_PHA\_HAS\_CELL(node\_id, pha, cell) \

3513 DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)

3514

3518

3524

[ 3556](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)#define DT\_BUS(node\_id) DT\_CAT(node\_id, \_BUS)

3557

[ 3586](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)#define DT\_ON\_BUS(node\_id, bus) IS\_ENABLED(DT\_CAT3(node\_id, \_BUS\_, bus))

3587

3591

3597

[ 3604](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)#define DT\_DRV\_INST(inst) DT\_INST(inst, DT\_DRV\_COMPAT)

3605

[ 3613](group__devicetree-inst.md#ga176760ce1a019020b5465eebd4f44ff5)#define DT\_INST\_PARENT(inst) DT\_PARENT(DT\_DRV\_INST(inst))

3614

[ 3622](group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)#define DT\_INST\_GPARENT(inst) DT\_GPARENT(DT\_DRV\_INST(inst))

3623

[ 3633](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)#define DT\_INST\_CHILD(inst, child) \

3634 DT\_CHILD(DT\_DRV\_INST(inst), child)

3635

[ 3645](group__devicetree-inst.md#ga49e2e39f4d93956217584df40316290b)#define DT\_INST\_CHILD\_NUM(inst) DT\_CHILD\_NUM(DT\_DRV\_INST(inst))

3646

[ 3656](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)#define DT\_INST\_CHILD\_NUM\_STATUS\_OKAY(inst) \

3657 DT\_CHILD\_NUM\_STATUS\_OKAY(DT\_DRV\_INST(inst))

3658

[ 3667](group__devicetree-inst.md#gaabb1a53b444221d82d865ec8d23c8278)#define DT\_INST\_NODELABEL\_STRING\_ARRAY(inst) DT\_NODELABEL\_STRING\_ARRAY(DT\_DRV\_INST(inst))

3668

[ 3677](group__devicetree-inst.md#ga2c43ec7309f5cdf8139a8b5fab63f786)#define DT\_INST\_NUM\_NODELABELS(inst) DT\_NUM\_NODELABELS(DT\_DRV\_INST(inst))

3678

[ 3693](group__devicetree-inst.md#ga98f3fccc6f3004f72c3602a5f2b3a08e)#define DT\_INST\_FOREACH\_CHILD(inst, fn) \

3694 DT\_FOREACH\_CHILD(DT\_DRV\_INST(inst), fn)

3695

[ 3709](group__devicetree-inst.md#gae8d01eb2d6a576246f225a5cbbec34e5)#define DT\_INST\_FOREACH\_CHILD\_SEP(inst, fn, sep) \

3710 DT\_FOREACH\_CHILD\_SEP(DT\_DRV\_INST(inst), fn, sep)

3711

[ 3727](group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651)#define DT\_INST\_FOREACH\_CHILD\_VARGS(inst, fn, ...) \

3728 DT\_FOREACH\_CHILD\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3729

[ 3744](group__devicetree-inst.md#gac70fcf3052d9dfa949d7e197fece1413)#define DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS(inst, fn, sep, ...) \

3745 DT\_FOREACH\_CHILD\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

3746

[ 3758](group__devicetree-inst.md#gad416dd269b1af1e392ef81397b9bc814)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY(inst, fn) \

3759 DT\_FOREACH\_CHILD\_STATUS\_OKAY(DT\_DRV\_INST(inst), fn)

3760

[ 3775](group__devicetree-inst.md#gae28554827ab7aaac3578ef07747a589d)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(inst, fn, sep) \

3776 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(DT\_DRV\_INST(inst), fn, sep)

3777

[ 3791](group__devicetree-inst.md#gac6dd19b2b6e603c11701cd07daec73d3)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(inst, fn, ...) \

3792 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3793

[ 3809](group__devicetree-inst.md#ga236cca0984f1c701c9b4855111c6cb29)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(inst, fn, sep, ...) \

3810 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

3811

[ 3818](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2)#define DT\_INST\_ENUM\_IDX(inst, prop) \

3819 DT\_ENUM\_IDX(DT\_DRV\_INST(inst), prop)

3820

[ 3829](group__devicetree-inst.md#gafbf64148f9171ffd322f7689297e0da8)#define DT\_INST\_ENUM\_IDX\_OR(inst, prop, default\_idx\_value) \

3830 DT\_ENUM\_IDX\_OR(DT\_DRV\_INST(inst), prop, default\_idx\_value)

3831

[ 3840](group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601)#define DT\_INST\_ENUM\_HAS\_VALUE(inst, prop, value) \

3841 DT\_ENUM\_HAS\_VALUE(DT\_DRV\_INST(inst), prop, value)

3842

[ 3849](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)#define DT\_INST\_PROP(inst, prop) DT\_PROP(DT\_DRV\_INST(inst), prop)

3850

[ 3857](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365)#define DT\_INST\_PROP\_LEN(inst, prop) DT\_PROP\_LEN(DT\_DRV\_INST(inst), prop)

3858

[ 3868](group__devicetree-inst.md#ga2c51745f8d51b1d9cdfb1cde69911d48)#define DT\_INST\_PROP\_HAS\_IDX(inst, prop, idx) \

3869 DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx)

3870

[ 3879](group__devicetree-inst.md#ga75e13dcdbcc51da1334fa14653411dd8)#define DT\_INST\_PROP\_HAS\_NAME(inst, prop, name) \

3880 DT\_PROP\_HAS\_NAME(DT\_DRV\_INST(inst), prop, name)

3881

[ 3889](group__devicetree-inst.md#ga5b60f4ed4f5dadc5dd425f5905f23b00)#define DT\_INST\_PROP\_BY\_IDX(inst, prop, idx) \

3890 DT\_PROP\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3891

[ 3899](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)#define DT\_INST\_PROP\_OR(inst, prop, default\_value) \

3900 DT\_PROP\_OR(DT\_DRV\_INST(inst), prop, default\_value)

3901

[ 3909](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)#define DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value) \

3910 DT\_PROP\_LEN\_OR(DT\_DRV\_INST(inst), prop, default\_value)

3911

[ 3921](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484)#define DT\_INST\_STRING\_TOKEN(inst, prop) \

3922 DT\_STRING\_TOKEN(DT\_DRV\_INST(inst), prop)

3923

[ 3931](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5)#define DT\_INST\_STRING\_UPPER\_TOKEN(inst, prop) \

3932 DT\_STRING\_UPPER\_TOKEN(DT\_DRV\_INST(inst), prop)

3933

[ 3942](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228)#define DT\_INST\_STRING\_UNQUOTED(inst, prop) \

3943 DT\_STRING\_UNQUOTED(DT\_DRV\_INST(inst), prop)

3944

[ 3952](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97)#define DT\_INST\_STRING\_TOKEN\_BY\_IDX(inst, prop, idx) \

3953 DT\_STRING\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3954

[ 3962](group__devicetree-inst.md#ga4ceceec8375d70b40a4dec1a8ab5ee29)#define DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX(inst, prop, idx) \

3963 DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3964

[ 3972](group__devicetree-inst.md#gac5768077e2a3d14a69efc653cfc59d5d)#define DT\_INST\_STRING\_UNQUOTED\_BY\_IDX(inst, prop, idx) \

3973 DT\_STRING\_UNQUOTED\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

3974

[ 3983](group__devicetree-inst.md#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)#define DT\_INST\_PROP\_BY\_PHANDLE(inst, ph, prop) \

3984 DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, ph, 0, prop)

3985

[ 3997](group__devicetree-inst.md#gad027963bdf159942cf6fb28b04e8d48e)#define DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop) \

3998 DT\_PROP\_BY\_PHANDLE\_IDX(DT\_DRV\_INST(inst), phs, idx, prop)

3999

[ 4008](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018)#define DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell) \

4009 DT\_PHA\_BY\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4010

[ 4020](group__devicetree-inst.md#ga3db4c00e072bd93fa92e36907b2b5e86)#define DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value) \

4021 DT\_PHA\_BY\_IDX\_OR(DT\_DRV\_INST(inst), pha, idx, cell, default\_value)

4022

[ 4031](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8)#define DT\_INST\_PHA(inst, pha, cell) DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)

4032

[ 4041](group__devicetree-inst.md#ga491ad421602e41c4295bac61b595fc94)#define DT\_INST\_PHA\_OR(inst, pha, cell, default\_value) \

4042 DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, 0, cell, default\_value)

4043

[ 4053](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8)#define DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell) \

4054 DT\_PHA\_BY\_NAME(DT\_DRV\_INST(inst), pha, name, cell)

4055

[ 4065](group__devicetree-inst.md#gaaebc5c643b60319f7e767e46ca226729)#define DT\_INST\_PHA\_BY\_NAME\_OR(inst, pha, name, cell, default\_value) \

4066 DT\_PHA\_BY\_NAME\_OR(DT\_DRV\_INST(inst), pha, name, cell, default\_value)

4067

[ 4076](group__devicetree-inst.md#ga64d8ddaad8b2d3852e30686d3adf6551)#define DT\_INST\_PHANDLE\_BY\_NAME(inst, pha, name) \

4077 DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), pha, name) \

4078

4079

[ 4088](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx) \

4089 DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4090

[ 4099](group__devicetree-inst.md#ga81c10f478c86e5a4c18eb7a990447137)#define DT\_INST\_PHANDLE(inst, prop) DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, 0)

4100

[ 4108](group__devicetree-inst.md#ga26bbff9ebaed549140d2530a0b99e8a4)#define DT\_INST\_REG\_HAS\_IDX(inst, idx) DT\_REG\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4109

[ 4117](group__devicetree-inst.md#ga8b15b84b03c3dc6fd9d7e127a44392b3)#define DT\_INST\_REG\_HAS\_NAME(inst, name) DT\_REG\_HAS\_NAME(DT\_DRV\_INST(inst), name)

4118

[ 4125](group__devicetree-inst.md#ga0fe0403821883598da6cfad4f3962115)#define DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx) DT\_REG\_ADDR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4126

[ 4133](group__devicetree-inst.md#gab1152c9f069c69b0269c1a4e744b9dd9)#define DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx) \

4134 DT\_REG\_SIZE\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4135

[ 4142](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c)#define DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name) \

4143 DT\_REG\_ADDR\_BY\_NAME(DT\_DRV\_INST(inst), name)

4144

[ 4153](group__devicetree-inst.md#gaf8d6ec7f68f566360743f7ea7cb7f8fb)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_OR(inst, name, default\_value) \

4154 DT\_REG\_ADDR\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4155

[ 4168](group__devicetree-inst.md#ga8af83c4c65e607b93aa60a690295d625)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_U64(inst, name) \

4169 DT\_U64\_C(DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name))

4170

[ 4177](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714)#define DT\_INST\_REG\_SIZE\_BY\_NAME(inst, name) \

4178 DT\_REG\_SIZE\_BY\_NAME(DT\_DRV\_INST(inst), name)

4179

[ 4188](group__devicetree-inst.md#ga8494b94b6dbec875eba61e10f269cce6)#define DT\_INST\_REG\_SIZE\_BY\_NAME\_OR(inst, name, default\_value) \

4189 DT\_REG\_SIZE\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4190

[ 4196](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7)#define DT\_INST\_REG\_ADDR(inst) DT\_INST\_REG\_ADDR\_BY\_IDX(inst, 0)

4197

[ 4209](group__devicetree-inst.md#gaba47dcabd8754eda87e35efd7289f976)#define DT\_INST\_REG\_ADDR\_U64(inst) DT\_U64\_C(DT\_INST\_REG\_ADDR(inst))

4210

[ 4216](group__devicetree-inst.md#gaa7cea29435e1db59470302abb5ee88dd)#define DT\_INST\_REG\_SIZE(inst) DT\_INST\_REG\_SIZE\_BY\_IDX(inst, 0)

4217

[ 4224](group__devicetree-inst.md#ga5c06043fd17c891e2cbbe0508248b638)#define DT\_INST\_IRQ\_LEVEL(inst) DT\_IRQ\_LEVEL(DT\_DRV\_INST(inst))

4225

[ 4233](group__devicetree-inst.md#gad0d69a61ad842aa1dc3a5d4a304c3f2f)#define DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell) \

4234 DT\_IRQ\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

4235

[ 4242](group__devicetree-inst.md#gab29f18e52d7475245c9fbeb4cd8e7769)#define DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx) \

4243 DT\_IRQ\_INTC\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4244

[ 4251](group__devicetree-inst.md#gadd0f339e10b071da34d44922ad0c7bfd)#define DT\_INST\_IRQ\_INTC\_BY\_NAME(inst, name) \

4252 DT\_IRQ\_INTC\_BY\_NAME(DT\_DRV\_INST(inst), name)

4253

[ 4261](group__devicetree-inst.md#gabf127c8370af849d2b5560e87ee04809)#define DT\_INST\_IRQ\_INTC(inst) \

4262 DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, 0)

4263

[ 4271](group__devicetree-inst.md#ga1ff6f24f9c97d4b611e4bf50ce5175d3)#define DT\_INST\_IRQ\_BY\_NAME(inst, name, cell) \

4272 DT\_IRQ\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

4273

[ 4280](group__devicetree-inst.md#ga789eb58422bab7b3a79b487c4a8a82d6)#define DT\_INST\_IRQ(inst, cell) DT\_INST\_IRQ\_BY\_IDX(inst, 0, cell)

4281

[ 4287](group__devicetree-inst.md#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)#define DT\_INST\_IRQN(inst) DT\_IRQN(DT\_DRV\_INST(inst))

4288

[ 4295](group__devicetree-inst.md#gaeb0c023f53ed87a6707bbca8ba05ce45)#define DT\_INST\_IRQN\_BY\_IDX(inst, idx) DT\_IRQN\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4296

[ 4302](group__devicetree-inst.md#gacecb46743315738dcd9a0765ea78276a)#define DT\_INST\_BUS(inst) DT\_BUS(DT\_DRV\_INST(inst))

4303

[ 4311](group__devicetree-inst.md#ga7a29bda946b399a7af92ec9cd09b4e98)#define DT\_INST\_ON\_BUS(inst, bus) DT\_ON\_BUS(DT\_DRV\_INST(inst), bus)

4312

[ 4322](group__devicetree-inst.md#ga79fd00d1ece5538f7705c241ab869ea8)#define DT\_INST\_STRING\_TOKEN\_OR(inst, name, default\_value) \

4323 DT\_STRING\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4324

[ 4333](group__devicetree-inst.md#ga72981780b2ede73c49ef9e5a7c6247c2)#define DT\_INST\_STRING\_UPPER\_TOKEN\_OR(inst, name, default\_value) \

4334 DT\_STRING\_UPPER\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4335

[ 4344](group__devicetree-inst.md#ga56bc0c0a46f6be421082119604cde643)#define DT\_INST\_STRING\_UNQUOTED\_OR(inst, name, default\_value) \

4345 DT\_STRING\_UNQUOTED\_OR(DT\_DRV\_INST(inst), name, default\_value)

4346

4347/\*

4348 \* @brief Test if any enabled node with the given compatible is on

4349 \* the given bus type

4350 \*

4351 \* This is like DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(), except it can also

4352 \* be useful for handling multiple compatibles in single source file.

4353 \*

4354 \* Example devicetree overlay:

4355 \*

4356 \* @code{.dts}

4357 \* &i2c0 {

4358 \* temp: temperature-sensor@76 {

4359 \* compatible = "vnd,some-sensor";

4360 \* reg = <0x76>;

4361 \* };

4362 \* };

4363 \* @endcode

4364 \*

4365 \* Example usage, assuming `i2c0` is an I2C bus controller node, and

4366 \* therefore `temp` is on an I2C bus:

4367 \*

4368 \* @code{.c}

4369 \* DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(vnd\_some\_sensor, i2c) // 1

4370 \* @endcode

4371 \*

4372 \* @param compat lowercase-and-underscores compatible, without quotes

4373 \* @param bus a binding's bus type as a C token, lowercased and without quotes

4374 \* @return 1 if any enabled node with that compatible is on that bus type,

4375 \* 0 otherwise

4376 \*/

[ 4377](group__devicetree-inst.md#ga1727af4beed08b248a98ad68bc5f1027)#define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus) \

4378 IS\_ENABLED(DT\_CAT4(DT\_COMPAT\_, compat, \_BUS\_, bus))

4379

[ 4412](group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)#define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus) \

4413 DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(DT\_DRV\_COMPAT, bus)

4414

[ 4459](group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735)#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop) \

4460 COND\_CODE\_1(IS\_EMPTY(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop)), (0), (1))

4461

[ 4527](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)#define DT\_INST\_FOREACH\_STATUS\_OKAY(fn) \

4528 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4529 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_, \

4530 DT\_DRV\_COMPAT)(fn)), \

4531 ())

4532

[ 4544](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38)#define DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(fn, ...) \

4545 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4546 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

4547 DT\_DRV\_COMPAT)(fn, \_\_VA\_ARGS\_\_)), \

4548 ())

4549

[ 4559](group__devicetree-inst.md#gafd15350971dee495f955f2fcc7edd82c)#define DT\_INST\_FOREACH\_NODELABEL(inst, fn) \

4560 DT\_FOREACH\_NODELABEL(DT\_DRV\_INST(inst), fn)

4561

[ 4573](group__devicetree-inst.md#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)#define DT\_INST\_FOREACH\_NODELABEL\_VARGS(inst, fn, ...) \

4574 DT\_FOREACH\_NODELABEL\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

4575

[ 4586](group__devicetree-inst.md#gaf163f2f85b3893ca46c87f0fcbe65255)#define DT\_INST\_FOREACH\_PROP\_ELEM(inst, prop, fn) \

4587 DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)

4588

[ 4601](group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP(inst, prop, fn, sep) \

4602 DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)

4603

[ 4618](group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)#define DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS(inst, prop, fn, ...) \

4619 DT\_FOREACH\_PROP\_ELEM\_VARGS(DT\_DRV\_INST(inst), prop, fn, \_\_VA\_ARGS\_\_)

4620

[ 4638](group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(inst, prop, fn, sep, ...) \

4639 DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(DT\_DRV\_INST(inst), prop, fn, sep, \

4640 \_\_VA\_ARGS\_\_)

4641

[ 4648](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)#define DT\_INST\_NODE\_HAS\_PROP(inst, prop) \

4649 DT\_NODE\_HAS\_PROP(DT\_DRV\_INST(inst), prop)

4650

[ 4657](group__devicetree-inst.md#gaf88c7dc0e935ad7097e317e54c362ba0)#define DT\_INST\_NODE\_HAS\_COMPAT(inst, compat) \

4658 DT\_NODE\_HAS\_COMPAT(DT\_DRV\_INST(inst), compat)

4659

[ 4670](group__devicetree-inst.md#gae054b89701ec9fae577320fb7b9cae1e)#define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell) \

4671 DT\_PHA\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4672

[ 4682](group__devicetree-inst.md#gab8083dae430aeb93a967bbf98aa9eefc)#define DT\_INST\_PHA\_HAS\_CELL(inst, pha, cell) \

4683 DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, 0, cell)

4684

[ 4692](group__devicetree-inst.md#gabb45132ef78818512c02bdf1f5a38068)#define DT\_INST\_IRQ\_HAS\_IDX(inst, idx) DT\_IRQ\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4693

[ 4702](group__devicetree-inst.md#gab176ff07912cea915c811406e8f5e386)#define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell) \

4703 DT\_IRQ\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), idx, cell)

4704

[ 4712](group__devicetree-inst.md#gabec43df3451bd917120b283d76c57054)#define DT\_INST\_IRQ\_HAS\_CELL(inst, cell) \

4713 DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, 0, cell)

4714

[ 4721](group__devicetree-inst.md#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)#define DT\_INST\_IRQ\_HAS\_NAME(inst, name) \

4722 DT\_IRQ\_HAS\_NAME(DT\_DRV\_INST(inst), name)

4723

4727

4729

4741#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_(idx, prop) \

4742 COND\_CODE\_1(DT\_INST\_NODE\_HAS\_PROP(idx, prop), (1,), ())

4755#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop) \

4756 DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_, prop)

4757

4758#define DT\_PATH\_INTERNAL(...) \

4759 UTIL\_CAT(DT\_ROOT, MACRO\_MAP\_CAT(DT\_S\_PREFIX, \_\_VA\_ARGS\_\_))

4765#define DT\_S\_PREFIX(name) \_S\_##name

4766

4781#define DT\_CAT(a1, a2) a1 ## a2

4783#define DT\_CAT3(a1, a2, a3) a1 ## a2 ## a3

4785#define DT\_CAT4(a1, a2, a3, a4) a1 ## a2 ## a3 ## a4

4787#define DT\_CAT5(a1, a2, a3, a4, a5) a1 ## a2 ## a3 ## a4 ## a5

4789#define DT\_CAT6(a1, a2, a3, a4, a5, a6) a1 ## a2 ## a3 ## a4 ## a5 ## a6

4791#define DT\_CAT7(a1, a2, a3, a4, a5, a6, a7) \

4792 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7

4794#define DT\_CAT8(a1, a2, a3, a4, a5, a6, a7, a8) \

4795 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7 ## a8

4796/\*

4797 \* If you need to define a bigger DT\_CATN(), do so here. Don't leave

4798 \* any "holes" of undefined macros, please.

4799 \*/

4800

4802#define DT\_DASH(...) MACRO\_MAP\_CAT(DT\_DASH\_PREFIX, \_\_VA\_ARGS\_\_)

4804#define DT\_DASH\_PREFIX(name) \_##name

4806#define DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status) \

4807 IS\_ENABLED(DT\_CAT3(node\_id, \_STATUS\_, status))

4808

4813#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

4814#define DT\_U64\_C(\_v) (\_v)

4815#else

4816#define DT\_U64\_C(\_v) UINT64\_C(\_v)

4817#endif

4818

4819/\* Helpers for DT\_NODELABEL\_STRING\_ARRAY. We define our own stringify

4820 \* in order to avoid adding a dependency on toolchain.h..

4821 \*/

4822#define DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL(nodelabel) DT\_STRINGIFY\_INTERNAL(nodelabel),

4823#define DT\_STRINGIFY\_INTERNAL(arg) DT\_STRINGIFY\_INTERNAL\_HELPER(arg)

4824#define DT\_STRINGIFY\_INTERNAL\_HELPER(arg) #arg

4825

4827

4828/\* have these last so they have access to all previously defined macros \*/

4829#include <[zephyr/devicetree/io-channels.h](io-channels_8h.md)>

4830#include <[zephyr/devicetree/clocks.h](clocks_8h.md)>

4831#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h.md)>

4832#include <[zephyr/devicetree/spi.h](devicetree_2spi_8h.md)>

4833#include <[zephyr/devicetree/dma.h](devicetree_2dma_8h.md)>

4834#include <[zephyr/devicetree/pwms.h](pwms_8h.md)>

4835#include <[zephyr/devicetree/fixed-partitions.h](fixed-partitions_8h.md)>

4836#include <[zephyr/devicetree/ordinals.h](ordinals_8h.md)>

4837#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

4838#include <[zephyr/devicetree/can.h](devicetree_2can_8h.md)>

4839#include <[zephyr/devicetree/reset.h](devicetree_2reset_8h.md)>

4840#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h.md)>

4841

4842#endif /\* DEVICETREE\_H \*/

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
