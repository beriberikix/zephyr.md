---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/devicetree_8h_source.html
original_path: doxygen/html/devicetree_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

16#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_H\_

17#define ZEPHYR\_INCLUDE\_DEVICETREE\_H\_

18

19#include <zephyr/devicetree\_generated.h>

20#include <[zephyr/irq\_multilevel.h](irq__multilevel_8h.md)>

21

22#if !defined(\_LINKER) && !defined(\_ASMLANGUAGE)

23#include <[stdint.h](stdint_8h.md)>

24#endif

25

26#include <[zephyr/sys/util.h](sys_2util_8h.md)>

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

50 \* \_EXISTS: property is defined

51 \* \_FOREACH\_PROP\_ELEM: helper for "iterating" over values in the property

52 \* \_FOREACH\_PROP\_ELEM\_VARGS: foreach functions with variable number of arguments

53 \* \_IDX\_<i>: logical index into property

54 \* \_IDX\_<i>\_EXISTS: logical index into property is defined

55 \* \_IDX\_<i>\_PH: phandle array's phandle by index (or phandle, phandles)

56 \* \_IDX\_<i>\_STRING\_TOKEN: string array element value as a token

57 \* \_IDX\_<i>\_STRING\_UPPER\_TOKEN: string array element value as a uppercased token

58 \* \_IDX <i>\_STRING\_UNQUOTED: string array element value as a sequence of tokens, with no quotes

59 \* \_IDX\_<i>\_VAL\_<val>: phandle array's specifier value by index

60 \* \_IDX\_<i>\_VAL\_<val>\_EXISTS: cell value exists, by index

61 \* \_LEN: property logical length

62 \* \_NAME\_<name>\_PH: phandle array's phandle by name

63 \* \_NAME\_<name>\_VAL\_<val>: phandle array's property specifier by name

64 \* \_NAME\_<name>\_VAL\_<val>\_EXISTS: cell value exists, by name

65 \* \_STRING\_TOKEN: string property's value as a token

66 \* \_STRING\_UPPER\_TOKEN: like \_STRING\_TOKEN, but uppercased

67 \* \_STRING\_UNQUOTED: string property's value as a sequence of tokens, with no quotes

68 \*/

69

75

[ 83](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)#define DT\_INVALID\_NODE \_

84

[ 88](group__devicetree-generic-id.md#gad65aa36621281687b22fa5d72db33e86)#define DT\_ROOT DT\_N

89

[ 140](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)#define DT\_PATH(...) DT\_PATH\_INTERNAL(\_\_VA\_ARGS\_\_)

141

[ 196](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)#define DT\_NODELABEL(label) DT\_CAT(DT\_N\_NODELABEL\_, label)

197

[ 236](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)#define DT\_ALIAS(alias) DT\_CAT(DT\_N\_ALIAS\_, alias)

237

[ 243](group__devicetree-generic-id.md#ga1f6c459577dbb195192bef33a30c5d51)#define DT\_HAS\_ALIAS(alias\_name) DT\_NODE\_EXISTS(DT\_ALIAS(alias\_name))

244

[ 253](group__devicetree-generic-id.md#ga067821c9b49437ac9333fd2a0443f1fc)#define DT\_NODE\_HASH(node\_id) DT\_CAT(node\_id, \_HASH)

254

[ 349](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)#define DT\_INST(inst, compat) UTIL\_CAT(DT\_N\_INST, DT\_DASH(inst, compat))

350

[ 374](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)#define DT\_PARENT(node\_id) DT\_CAT(node\_id, \_PARENT)

375

[ 399](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)#define DT\_GPARENT(node\_id) DT\_PARENT(DT\_PARENT(node\_id))

400

[ 436](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)#define DT\_CHILD(node\_id, child) UTIL\_CAT(node\_id, DT\_S\_PREFIX(child))

437

[ 479](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat) \

480 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

481 (DT\_INST(0, compat)), \

482 (DT\_INVALID\_NODE))

483

[ 511](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)#define DT\_NODE\_PATH(node\_id) DT\_CAT(node\_id, \_PATH)

512

[ 537](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)#define DT\_NODE\_FULL\_NAME(node\_id) DT\_CAT(node\_id, \_FULL\_NAME)

538

[ 565](group__devicetree-generic-id.md#ga8832fb6fa0e0555884621d210440fdcd)#define DT\_NODE\_FULL\_NAME\_UNQUOTED(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_UNQUOTED)

566

[ 593](group__devicetree-generic-id.md#gad24b51e728175e7d347407f2131a3850)#define DT\_NODE\_FULL\_NAME\_TOKEN(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_TOKEN)

594

[ 623](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)#define DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_UPPER\_TOKEN)

624

[ 651](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)#define DT\_NODE\_CHILD\_IDX(node\_id) DT\_CAT(node\_id, \_CHILD\_IDX)

652

[ 659](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)#define DT\_CHILD\_NUM(node\_id) DT\_CAT(node\_id, \_CHILD\_NUM)

660

661

[ 669](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)#define DT\_CHILD\_NUM\_STATUS\_OKAY(node\_id) \

670 DT\_CAT(node\_id, \_CHILD\_NUM\_STATUS\_OKAY)

671

[ 692](group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)#define DT\_SAME\_NODE(node\_id1, node\_id2) \

693 (DT\_DEP\_ORD(node\_id1) == (DT\_DEP\_ORD(node\_id2)))

694

[ 719](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)#define DT\_NODELABEL\_STRING\_ARRAY(node\_id) \

720 { DT\_FOREACH\_NODELABEL(node\_id, DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL) }

721

725

731

[ 762](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)#define DT\_PROP(node\_id, prop) DT\_CAT3(node\_id, \_P\_, prop)

763

[ 796](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)#define DT\_PROP\_LEN(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_LEN)

797

[ 812](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value) \

813 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

814 (DT\_PROP\_LEN(node\_id, prop)), (default\_value))

815

[ 836](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx) \

837 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_EXISTS))

838

[ 871](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)#define DT\_PROP\_HAS\_NAME(node\_id, prop, name) \

872 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_NAME\_, name, \_EXISTS))

873

[ 908](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)#define DT\_PROP\_BY\_IDX(node\_id, prop, idx) \

909 DT\_CAT5(node\_id, \_P\_, prop, \_IDX\_, idx)

910

[ 919](group__devicetree-generic-prop.md#ga05a04871d83b31834c134a64636dcd8a)#define DT\_PROP\_LAST(node\_id, prop) \

920 DT\_PROP\_BY\_IDX(node\_id, prop, UTIL\_DEC(DT\_PROP\_LEN(node\_id, prop)))

921

[ 935](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)#define DT\_PROP\_OR(node\_id, prop, default\_value) \

936 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

937 (DT\_PROP(node\_id, prop)), (default\_value))

938

[ 994](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2)#define DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, idx) \

995 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_ENUM\_IDX)

996

[ 1003](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)#define DT\_ENUM\_IDX(node\_id, prop) DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, 0)

1004

[ 1020](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73)#define DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, idx, default\_idx\_value) \

1021 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, idx), \

1022 (DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, idx)), (default\_idx\_value))

1023

[ 1032](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value) \

1033 DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, 0, default\_idx\_value)

1034

[ 1044](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4)#define DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, idx, value) \

1045 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, prop, \_IDX\_, idx, \_ENUM\_VAL\_, value, \_EXISTS))

1046

[ 1054](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)#define DT\_ENUM\_HAS\_VALUE(node\_id, prop, value) \

1055 DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, 0, value)

1056

[ 1116](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)#define DT\_STRING\_TOKEN(node\_id, prop) \

1117 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_TOKEN)

1118

[ 1132](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value) \

1133 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1134 (DT\_STRING\_TOKEN(node\_id, prop)), (default\_value))

1135

[ 1193](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop) \

1194 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UPPER\_TOKEN)

1195

[ 1210](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value) \

1211 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1212 (DT\_STRING\_UPPER\_TOKEN(node\_id, prop)), (default\_value))

1213

[ 1254](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)#define DT\_STRING\_UNQUOTED(node\_id, prop) \

1255 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UNQUOTED)

1256

[ 1271](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)#define DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value) \

1272 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1273 (DT\_STRING\_UNQUOTED(node\_id, prop)), (default\_value))

1274

[ 1322](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1323 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_TOKEN)

1324

[ 1372](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1373 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UPPER\_TOKEN)

1374

[ 1415](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)#define DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx) \

1416 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UNQUOTED)

1417

1418/\*

1419 \* phandle properties

1420 \*

1421 \* These are special-cased to manage the impedance mismatch between

1422 \* phandles, which are just uint32\_t node properties that only make sense

1423 \* within the tree itself, and C values.

1424 \*/

1425

[ 1471](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop) \

1472 DT\_PROP(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop)

1473

[ 1493](group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b)#define DT\_PROP\_BY\_PHANDLE\_IDX\_OR(node\_id, phs, idx, prop, default\_value) \

1494 DT\_PROP\_OR(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop, default\_value)

1495

[ 1507](group__devicetree-generic-prop.md#gabc1b099dda97fb03a9259a8b21fc04d2)#define DT\_PROP\_BY\_PHANDLE(node\_id, ph, prop) \

1508 DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)

1509

[ 1564](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell) \

1565 DT\_CAT7(node\_id, \_P\_, pha, \_IDX\_, idx, \_VAL\_, cell)

1566

[ 1590](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value) \

1591 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_IDX\_, idx, \_VAL\_, cell), default\_value)

1592

[ 1600](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)#define DT\_PHA(node\_id, pha, cell) DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)

1601

[ 1616](group__devicetree-generic-prop.md#ga886559b058b24164b62ab95215d860bd)#define DT\_PHA\_OR(node\_id, pha, cell, default\_value) \

1617 DT\_PHA\_BY\_IDX\_OR(node\_id, pha, 0, cell, default\_value)

1618

[ 1659](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell) \

1660 DT\_CAT7(node\_id, \_P\_, pha, \_NAME\_, name, \_VAL\_, cell)

1661

[ 1683](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value) \

1684 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_NAME\_, name, \_VAL\_, cell), default\_value)

1685

[ 1733](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name) \

1734 DT\_CAT6(node\_id, \_P\_, pha, \_NAME\_, name, \_PH)

1735

[ 1785](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx) \

1786 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_PH)

1787

[ 1799](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)#define DT\_PHANDLE(node\_id, prop) DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)

1800

1804

1810

[ 1847](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc)#define DT\_NUM\_RANGES(node\_id) DT\_CAT(node\_id, \_RANGES\_NUM)

1848

[ 1901](group__devicetree-ranges-prop.md#gac6f54058c58b06935bd2deae9f1ec2db)#define DT\_RANGES\_HAS\_IDX(node\_id, idx) \

1902 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_EXISTS))

1903

[ 1956](group__devicetree-ranges-prop.md#ga3730c9176911bd8cc762f447eb020ecd)#define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx) \

1957 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS\_EXISTS))

1958

[ 1996](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx) \

1997 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS)

1998

[ 2045](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

2046 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_ADDRESS)

2047

[ 2094](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

2095 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_PARENT\_BUS\_ADDRESS)

2096

[ 2143](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx) \

2144 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_LENGTH)

2145

[ 2185](group__devicetree-ranges-prop.md#ga4c71a8adcfe6c53b480775510c92a632)#define DT\_FOREACH\_RANGE(node\_id, fn) \

2186 DT\_CAT(node\_id, \_FOREACH\_RANGE)(fn)

2187

2191

2197

[ 2233](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747)#define DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx) \

2234 DT\_CAT3(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx)

2235

[ 2248](group__devicetree-generic-vendor.md#gabfa4130fa24457c457961caa7e2c6276)#define DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx) \

2249 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx, \_EXISTS))

2250

[ 2265](group__devicetree-generic-vendor.md#gaa71b1152516847d51582b9b23c472f3d)#define DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2266 COND\_CODE\_1(DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx), \

2267 (DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)), (default\_value))

2268

[ 2277](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)#define DT\_NODE\_VENDOR\_OR(node\_id, default\_value) \

2278 DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, 0, default\_value)

2279

[ 2309](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)#define DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx) \

2310 DT\_CAT3(node\_id, \_COMPAT\_MODEL\_IDX\_, idx)

2311

[ 2324](group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)#define DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx) \

2325 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_MODEL\_IDX\_, idx, \_EXISTS))

2326

[ 2341](group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)#define DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2342 COND\_CODE\_1(DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx), \

2343 (DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)), (default\_value))

2344

[ 2353](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)#define DT\_NODE\_MODEL\_OR(node\_id, default\_value) \

2354 DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, 0, default\_value)

2355

2359

2365

[ 2373](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)#define DT\_NUM\_REGS(node\_id) DT\_CAT(node\_id, \_REG\_NUM)

2374

[ 2386](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)#define DT\_REG\_HAS\_IDX(node\_id, idx) \

2387 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_EXISTS))

2388

[ 2400](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)#define DT\_REG\_HAS\_NAME(node\_id, name) \

2401 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_EXISTS))

2402

[ 2414](group__devicetree-reg-prop.md#ga226e23a6bb94beee690ff6e1cdfbab91)#define DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx) \

2415 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

2416

[ 2428](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)#define DT\_REG\_ADDR\_RAW(node\_id) \

2429 DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, 0)

2430

[ 2437](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx) \

2438 DT\_U32\_C(DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx))

2439

[ 2451](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx) \

2452 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE))

2453

[ 2461](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)#define DT\_REG\_ADDR(node\_id) DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)

2462

[ 2473](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)#define DT\_REG\_ADDR\_U64(node\_id) DT\_U64\_C(DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, 0))

2474

[ 2482](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)#define DT\_REG\_SIZE(node\_id) DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)

2483

[ 2490](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name) \

2491 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

2492

[ 2501](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)#define DT\_REG\_ADDR\_BY\_NAME\_OR(node\_id, name, default\_value) \

2502 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2503 (DT\_REG\_ADDR\_BY\_NAME(node\_id, name)), (default\_value))

2504

[ 2517](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)#define DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name) \

2518 DT\_U64\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

2519

[ 2526](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name) \

2527 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE))

2528

[ 2537](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)#define DT\_REG\_SIZE\_BY\_NAME\_OR(node\_id, name, default\_value) \

2538 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2539 (DT\_REG\_SIZE\_BY\_NAME(node\_id, name)), (default\_value))

2540

2541

2545

2551

[ 2560](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)#define DT\_NUM\_IRQS(node\_id) DT\_CAT(node\_id, \_IRQ\_NUM)

2561

[ 2586](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)#define DT\_NUM\_NODELABELS(node\_id) DT\_CAT(node\_id, \_NODELABEL\_NUM)

2587

[ 2594](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)#define DT\_IRQ\_LEVEL(node\_id) DT\_CAT(node\_id, \_IRQ\_LEVEL)

2595

[ 2606](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)#define DT\_IRQ\_HAS\_IDX(node\_id, idx) \

2607 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_EXISTS))

2608

[ 2619](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell) \

2620 IS\_ENABLED(DT\_CAT6(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

2621

[ 2629](group__devicetree-interrupts-prop.md#gab9c94ee39db7913598a755c6172fe036)#define DT\_IRQ\_HAS\_CELL(node\_id, cell) DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)

2630

[ 2640](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)#define DT\_IRQ\_HAS\_NAME(node\_id, name) \

2641 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_VAL\_irq\_EXISTS))

2642

[ 2678](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell) \

2679 DT\_CAT5(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell)

2680

[ 2696](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)#define DT\_IRQ\_BY\_NAME(node\_id, name, cell) \

2697 DT\_CAT5(node\_id, \_IRQ\_NAME\_, name, \_VAL\_, cell)

2698

[ 2706](group__devicetree-interrupts-prop.md#gabf60fbd528d300a26c0b4e66fe80a53f)#define DT\_IRQ(node\_id, cell) DT\_IRQ\_BY\_IDX(node\_id, 0, cell)

2707

[ 2750](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx) \

2751 DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_CONTROLLER)

2752

[ 2797](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)#define DT\_IRQ\_INTC\_BY\_NAME(node\_id, name) \

2798 DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_CONTROLLER)

2799

[ 2839](group__devicetree-interrupts-prop.md#ga11d2680614de65fd8cb4a3909e93e9c9)#define DT\_IRQ\_INTC(node\_id) \

2840 DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)

2841

2845

2846/\* DT helper macro to encode a node's IRQN to level 1 according to the multi-level scheme \*/

2847#define DT\_IRQN\_L1\_INTERNAL(node\_id, idx) DT\_IRQ\_BY\_IDX(node\_id, idx, irq)

2848/\* DT helper macro to encode a node's IRQN to level 2 according to the multi-level scheme \*/

2849#define DT\_IRQN\_L2\_INTERNAL(node\_id, idx) \

2850 (IRQ\_TO\_L2(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2851 DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq))

2852/\* DT helper macro to encode a node's IRQN to level 3 according to the multi-level scheme \*/

2853#define DT\_IRQN\_L3\_INTERNAL(node\_id, idx) \

2854 (IRQ\_TO\_L3(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2855 IRQ\_TO\_L2(DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq)) | \

2856 DT\_IRQ(DT\_IRQ\_INTC(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)), irq))

2857/\* DT helper macro for the macros above \*/

2858#define DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, level) DT\_CAT3(DT\_IRQN\_L, level, \_INTERNAL)(node\_id, idx)

2859

2864#define DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx) \

2865 DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, DT\_IRQ\_LEVEL(node\_id))

2866

2870

[ 2879](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)#define DT\_IRQN\_BY\_IDX(node\_id, idx) \

2880 COND\_CODE\_1(IS\_ENABLED(CONFIG\_MULTI\_LEVEL\_INTERRUPTS), \

2881 (DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx)), \

2882 (DT\_IRQ\_BY\_IDX(node\_id, idx, irq)))

2883

[ 2894](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)#define DT\_IRQN(node\_id) DT\_IRQN\_BY\_IDX(node\_id, 0)

2895

2899

2905

[ 2914](group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed)#define DT\_CHOSEN(prop) DT\_CAT(DT\_CHOSEN\_, prop)

2915

[ 2922](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)#define DT\_HAS\_CHOSEN(prop) IS\_ENABLED(DT\_CAT3(DT\_CHOSEN\_, prop, \_EXISTS))

2923

2927

2963

[ 2973](group__devicetree-generic-foreach.md#gad27b29ae71a3d3294984fd3bc721121d)#define DT\_FOREACH\_NODE(fn) DT\_FOREACH\_HELPER(fn)

2974

[ 2987](group__devicetree-generic-foreach.md#ga4e708120bf839568b1215a6c21c54eed)#define DT\_FOREACH\_NODE\_VARGS(fn, ...) DT\_FOREACH\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2988

[ 3000](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn) DT\_FOREACH\_OKAY\_HELPER(fn)

3001

[ 3016](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)#define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn, ...) DT\_FOREACH\_OKAY\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

3017

[ 3064](group__devicetree-generic-foreach.md#gac4f9fee38bffbd5d315d386fe3c7bc91)#define DT\_FOREACH\_ANCESTOR(node\_id, fn) \

3065 DT\_CAT(node\_id, \_FOREACH\_ANCESTOR)(fn)

3066

[ 3110](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)#define DT\_FOREACH\_CHILD(node\_id, fn) \

3111 DT\_CAT(node\_id, \_FOREACH\_CHILD)(fn)

3112

[ 3153](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep) \

3154 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP)(fn, sep)

3155

[ 3171](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)#define DT\_FOREACH\_CHILD\_VARGS(node\_id, fn, ...) \

3172 DT\_CAT(node\_id, \_FOREACH\_CHILD\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3173

[ 3189](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)#define DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep, ...) \

3190 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

3191

[ 3207](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn) \

3208 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY)(fn)

3209

[ 3226](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep) \

3227 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP)(fn, sep)

3228

[ 3248](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn, ...) \

3249 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3250

[ 3269](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep, ...) \

3270 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

3271

[ 3322](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn) \

3323 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM)(fn)

3324

[ 3367](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep) \

3368 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP)(fn, sep)

3369

[ 3390](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn, ...) \

3391 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3392

[ 3409](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)#define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep, ...) \

3410 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP\_VARGS)( \

3411 fn, sep, \_\_VA\_ARGS\_\_)

3412

[ 3466](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)#define DT\_FOREACH\_STATUS\_OKAY(compat, fn) \

3467 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3468 (UTIL\_CAT(DT\_FOREACH\_OKAY\_, compat)(fn)), \

3469 ())

3470

[ 3515](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3516 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3517 (DT\_CAT(DT\_FOREACH\_OKAY\_VARGS\_, \

3518 compat)(fn, \_\_VA\_ARGS\_\_)), \

3519 ())

3520

[ 3533](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9)#define DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3534 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3535 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

3536 compat)(fn, compat, \_\_VA\_ARGS\_\_)), \

3537 ())

3538

3539

[ 3578](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)#define DT\_FOREACH\_NODELABEL(node\_id, fn) DT\_CAT(node\_id, \_FOREACH\_NODELABEL)(fn)

3579

[ 3617](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)#define DT\_FOREACH\_NODELABEL\_VARGS(node\_id, fn, ...) \

3618 DT\_CAT(node\_id, \_FOREACH\_NODELABEL\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3619

3623

3629

[ 3644](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)#define DT\_NODE\_EXISTS(node\_id) IS\_ENABLED(DT\_CAT(node\_id, \_EXISTS))

3645

[ 3667](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)#define DT\_NODE\_HAS\_STATUS(node\_id, status) \

3668 DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status)

3669

[ 3690](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)#define DT\_NODE\_HAS\_STATUS\_OKAY(node\_id) DT\_NODE\_HAS\_STATUS(node\_id, okay)

3691

[ 3711](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat) \

3712 IS\_ENABLED(DT\_CAT(DT\_COMPAT\_HAS\_OKAY\_, compat))

3713

[ 3720](group__devicetree-generic-exist.md#ga45c268d7f0d604a72dc0bcf5cd0733b0)#define DT\_NUM\_INST\_STATUS\_OKAY(compat) \

3721 UTIL\_AND(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3722 UTIL\_CAT(DT\_N\_INST, DT\_DASH(compat, NUM\_OKAY)))

3723

[ 3751](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)#define DT\_NODE\_HAS\_COMPAT(node\_id, compat) \

3752 IS\_ENABLED(DT\_CAT3(node\_id, \_COMPAT\_MATCHES\_, compat))

3753

[ 3768](group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)#define DT\_NODE\_HAS\_COMPAT\_STATUS(node\_id, compat, status) \

3769 UTIL\_AND(DT\_NODE\_HAS\_COMPAT(node\_id, compat), DT\_NODE\_HAS\_STATUS(node\_id, status))

3770

[ 3784](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)#define DT\_NODE\_HAS\_PROP(node\_id, prop) \

3785 IS\_ENABLED(DT\_CAT4(node\_id, \_P\_, prop, \_EXISTS))

3786

3787

[ 3804](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell) \

3805 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, pha, \

3806 \_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

3807

[ 3817](group__devicetree-generic-exist.md#gaece280102681cbadf318c5dabfb3d719)#define DT\_PHA\_HAS\_CELL(node\_id, pha, cell) \

3818 DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)

3819

3823

3829

[ 3861](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)#define DT\_BUS(node\_id) DT\_CAT(node\_id, \_BUS)

3862

[ 3891](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)#define DT\_ON\_BUS(node\_id, bus) IS\_ENABLED(DT\_CAT3(node\_id, \_BUS\_, bus))

3892

3896

3902

[ 3909](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)#define DT\_DRV\_INST(inst) DT\_INST(inst, DT\_DRV\_COMPAT)

3910

[ 3918](group__devicetree-inst.md#ga176760ce1a019020b5465eebd4f44ff5)#define DT\_INST\_PARENT(inst) DT\_PARENT(DT\_DRV\_INST(inst))

3919

[ 3927](group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)#define DT\_INST\_GPARENT(inst) DT\_GPARENT(DT\_DRV\_INST(inst))

3928

[ 3938](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)#define DT\_INST\_CHILD(inst, child) \

3939 DT\_CHILD(DT\_DRV\_INST(inst), child)

3940

[ 3950](group__devicetree-inst.md#ga49e2e39f4d93956217584df40316290b)#define DT\_INST\_CHILD\_NUM(inst) DT\_CHILD\_NUM(DT\_DRV\_INST(inst))

3951

[ 3961](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)#define DT\_INST\_CHILD\_NUM\_STATUS\_OKAY(inst) \

3962 DT\_CHILD\_NUM\_STATUS\_OKAY(DT\_DRV\_INST(inst))

3963

[ 3972](group__devicetree-inst.md#gaabb1a53b444221d82d865ec8d23c8278)#define DT\_INST\_NODELABEL\_STRING\_ARRAY(inst) DT\_NODELABEL\_STRING\_ARRAY(DT\_DRV\_INST(inst))

3973

[ 3982](group__devicetree-inst.md#ga2c43ec7309f5cdf8139a8b5fab63f786)#define DT\_INST\_NUM\_NODELABELS(inst) DT\_NUM\_NODELABELS(DT\_DRV\_INST(inst))

3983

[ 3998](group__devicetree-inst.md#ga98f3fccc6f3004f72c3602a5f2b3a08e)#define DT\_INST\_FOREACH\_CHILD(inst, fn) \

3999 DT\_FOREACH\_CHILD(DT\_DRV\_INST(inst), fn)

4000

[ 4014](group__devicetree-inst.md#gae8d01eb2d6a576246f225a5cbbec34e5)#define DT\_INST\_FOREACH\_CHILD\_SEP(inst, fn, sep) \

4015 DT\_FOREACH\_CHILD\_SEP(DT\_DRV\_INST(inst), fn, sep)

4016

[ 4032](group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651)#define DT\_INST\_FOREACH\_CHILD\_VARGS(inst, fn, ...) \

4033 DT\_FOREACH\_CHILD\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

4034

[ 4049](group__devicetree-inst.md#gac70fcf3052d9dfa949d7e197fece1413)#define DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS(inst, fn, sep, ...) \

4050 DT\_FOREACH\_CHILD\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

4051

[ 4063](group__devicetree-inst.md#gad416dd269b1af1e392ef81397b9bc814)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY(inst, fn) \

4064 DT\_FOREACH\_CHILD\_STATUS\_OKAY(DT\_DRV\_INST(inst), fn)

4065

[ 4080](group__devicetree-inst.md#gae28554827ab7aaac3578ef07747a589d)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(inst, fn, sep) \

4081 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(DT\_DRV\_INST(inst), fn, sep)

4082

[ 4096](group__devicetree-inst.md#gac6dd19b2b6e603c11701cd07daec73d3)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(inst, fn, ...) \

4097 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

4098

[ 4114](group__devicetree-inst.md#ga236cca0984f1c701c9b4855111c6cb29)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(inst, fn, sep, ...) \

4115 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

4116

[ 4124](group__devicetree-inst.md#ga9de99aff4800b0f6f461fdb48bcc3969)#define DT\_INST\_ENUM\_IDX\_BY\_IDX(inst, prop, idx) \

4125 DT\_ENUM\_IDX\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4126

[ 4133](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2)#define DT\_INST\_ENUM\_IDX(inst, prop) \

4134 DT\_ENUM\_IDX(DT\_DRV\_INST(inst), prop)

4135

[ 4145](group__devicetree-inst.md#ga48315c386a33d9384078c4a4fcccfd5d)#define DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR(inst, prop, idx, default\_idx\_value) \

4146 DT\_ENUM\_IDX\_BY\_IDX\_OR(DT\_DRV\_INST(inst), prop, idx, default\_idx\_value)

4147

[ 4156](group__devicetree-inst.md#gafbf64148f9171ffd322f7689297e0da8)#define DT\_INST\_ENUM\_IDX\_OR(inst, prop, default\_idx\_value) \

4157 DT\_ENUM\_IDX\_OR(DT\_DRV\_INST(inst), prop, default\_idx\_value)

4158

[ 4167](group__devicetree-inst.md#ga5057571e3996451258ae5c29a06d9ede)#define DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX(inst, prop, idx, value) \

4168 DT\_ENUM\_HAS\_VALUE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx, value)

4169

[ 4178](group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601)#define DT\_INST\_ENUM\_HAS\_VALUE(inst, prop, value) \

4179 DT\_ENUM\_HAS\_VALUE(DT\_DRV\_INST(inst), prop, value)

4180

[ 4187](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)#define DT\_INST\_PROP(inst, prop) DT\_PROP(DT\_DRV\_INST(inst), prop)

4188

[ 4195](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365)#define DT\_INST\_PROP\_LEN(inst, prop) DT\_PROP\_LEN(DT\_DRV\_INST(inst), prop)

4196

[ 4206](group__devicetree-inst.md#ga2c51745f8d51b1d9cdfb1cde69911d48)#define DT\_INST\_PROP\_HAS\_IDX(inst, prop, idx) \

4207 DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx)

4208

[ 4217](group__devicetree-inst.md#ga75e13dcdbcc51da1334fa14653411dd8)#define DT\_INST\_PROP\_HAS\_NAME(inst, prop, name) \

4218 DT\_PROP\_HAS\_NAME(DT\_DRV\_INST(inst), prop, name)

4219

[ 4227](group__devicetree-inst.md#ga5b60f4ed4f5dadc5dd425f5905f23b00)#define DT\_INST\_PROP\_BY\_IDX(inst, prop, idx) \

4228 DT\_PROP\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4229

[ 4237](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)#define DT\_INST\_PROP\_OR(inst, prop, default\_value) \

4238 DT\_PROP\_OR(DT\_DRV\_INST(inst), prop, default\_value)

4239

[ 4247](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)#define DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value) \

4248 DT\_PROP\_LEN\_OR(DT\_DRV\_INST(inst), prop, default\_value)

4249

[ 4259](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484)#define DT\_INST\_STRING\_TOKEN(inst, prop) \

4260 DT\_STRING\_TOKEN(DT\_DRV\_INST(inst), prop)

4261

[ 4269](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5)#define DT\_INST\_STRING\_UPPER\_TOKEN(inst, prop) \

4270 DT\_STRING\_UPPER\_TOKEN(DT\_DRV\_INST(inst), prop)

4271

[ 4280](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228)#define DT\_INST\_STRING\_UNQUOTED(inst, prop) \

4281 DT\_STRING\_UNQUOTED(DT\_DRV\_INST(inst), prop)

4282

[ 4290](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97)#define DT\_INST\_STRING\_TOKEN\_BY\_IDX(inst, prop, idx) \

4291 DT\_STRING\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4292

[ 4300](group__devicetree-inst.md#ga4ceceec8375d70b40a4dec1a8ab5ee29)#define DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX(inst, prop, idx) \

4301 DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4302

[ 4310](group__devicetree-inst.md#gac5768077e2a3d14a69efc653cfc59d5d)#define DT\_INST\_STRING\_UNQUOTED\_BY\_IDX(inst, prop, idx) \

4311 DT\_STRING\_UNQUOTED\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4312

[ 4321](group__devicetree-inst.md#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)#define DT\_INST\_PROP\_BY\_PHANDLE(inst, ph, prop) \

4322 DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, ph, 0, prop)

4323

[ 4335](group__devicetree-inst.md#gad027963bdf159942cf6fb28b04e8d48e)#define DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop) \

4336 DT\_PROP\_BY\_PHANDLE\_IDX(DT\_DRV\_INST(inst), phs, idx, prop)

4337

[ 4346](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018)#define DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell) \

4347 DT\_PHA\_BY\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4348

[ 4358](group__devicetree-inst.md#ga3db4c00e072bd93fa92e36907b2b5e86)#define DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value) \

4359 DT\_PHA\_BY\_IDX\_OR(DT\_DRV\_INST(inst), pha, idx, cell, default\_value)

4360

[ 4369](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8)#define DT\_INST\_PHA(inst, pha, cell) DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)

4370

[ 4379](group__devicetree-inst.md#ga491ad421602e41c4295bac61b595fc94)#define DT\_INST\_PHA\_OR(inst, pha, cell, default\_value) \

4380 DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, 0, cell, default\_value)

4381

[ 4391](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8)#define DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell) \

4392 DT\_PHA\_BY\_NAME(DT\_DRV\_INST(inst), pha, name, cell)

4393

[ 4403](group__devicetree-inst.md#gaaebc5c643b60319f7e767e46ca226729)#define DT\_INST\_PHA\_BY\_NAME\_OR(inst, pha, name, cell, default\_value) \

4404 DT\_PHA\_BY\_NAME\_OR(DT\_DRV\_INST(inst), pha, name, cell, default\_value)

4405

[ 4414](group__devicetree-inst.md#ga64d8ddaad8b2d3852e30686d3adf6551)#define DT\_INST\_PHANDLE\_BY\_NAME(inst, pha, name) \

4415 DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), pha, name) \

4416

4417

[ 4426](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx) \

4427 DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4428

[ 4437](group__devicetree-inst.md#ga81c10f478c86e5a4c18eb7a990447137)#define DT\_INST\_PHANDLE(inst, prop) DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, 0)

4438

[ 4446](group__devicetree-inst.md#ga26bbff9ebaed549140d2530a0b99e8a4)#define DT\_INST\_REG\_HAS\_IDX(inst, idx) DT\_REG\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4447

[ 4455](group__devicetree-inst.md#ga8b15b84b03c3dc6fd9d7e127a44392b3)#define DT\_INST\_REG\_HAS\_NAME(inst, name) DT\_REG\_HAS\_NAME(DT\_DRV\_INST(inst), name)

4456

[ 4463](group__devicetree-inst.md#gade870f8f5c78c3c6244ada35049334a5)#define DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW(inst, idx) DT\_REG\_ADDR\_BY\_IDX\_RAW(DT\_DRV\_INST(inst), idx)

4464

[ 4471](group__devicetree-inst.md#ga0fe0403821883598da6cfad4f3962115)#define DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx) DT\_REG\_ADDR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4472

[ 4479](group__devicetree-inst.md#gab1152c9f069c69b0269c1a4e744b9dd9)#define DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx) \

4480 DT\_REG\_SIZE\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4481

[ 4488](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c)#define DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name) \

4489 DT\_REG\_ADDR\_BY\_NAME(DT\_DRV\_INST(inst), name)

4490

[ 4499](group__devicetree-inst.md#gaf8d6ec7f68f566360743f7ea7cb7f8fb)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_OR(inst, name, default\_value) \

4500 DT\_REG\_ADDR\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4501

[ 4514](group__devicetree-inst.md#ga8af83c4c65e607b93aa60a690295d625)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_U64(inst, name) \

4515 DT\_REG\_ADDR\_BY\_NAME\_U64(DT\_DRV\_INST(inst), name)

4516

[ 4523](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714)#define DT\_INST\_REG\_SIZE\_BY\_NAME(inst, name) \

4524 DT\_REG\_SIZE\_BY\_NAME(DT\_DRV\_INST(inst), name)

4525

[ 4534](group__devicetree-inst.md#ga8494b94b6dbec875eba61e10f269cce6)#define DT\_INST\_REG\_SIZE\_BY\_NAME\_OR(inst, name, default\_value) \

4535 DT\_REG\_SIZE\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4536

[ 4542](group__devicetree-inst.md#ga79627566ff2486cfd2425a04974d71a3)#define DT\_INST\_REG\_ADDR\_RAW(inst) DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW(inst, 0)

4543

[ 4549](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7)#define DT\_INST\_REG\_ADDR(inst) DT\_INST\_REG\_ADDR\_BY\_IDX(inst, 0)

4550

[ 4562](group__devicetree-inst.md#gaba47dcabd8754eda87e35efd7289f976)#define DT\_INST\_REG\_ADDR\_U64(inst) DT\_REG\_ADDR\_U64(DT\_DRV\_INST(inst))

4563

[ 4569](group__devicetree-inst.md#gaa7cea29435e1db59470302abb5ee88dd)#define DT\_INST\_REG\_SIZE(inst) DT\_INST\_REG\_SIZE\_BY\_IDX(inst, 0)

4570

[ 4577](group__devicetree-inst.md#ga446d4b9c267e7c9da73dfb8a07701f2a)#define DT\_INST\_NUM\_IRQS(inst) DT\_NUM\_IRQS(DT\_DRV\_INST(inst))

4578

[ 4585](group__devicetree-inst.md#ga5c06043fd17c891e2cbbe0508248b638)#define DT\_INST\_IRQ\_LEVEL(inst) DT\_IRQ\_LEVEL(DT\_DRV\_INST(inst))

4586

[ 4594](group__devicetree-inst.md#gad0d69a61ad842aa1dc3a5d4a304c3f2f)#define DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell) \

4595 DT\_IRQ\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

4596

[ 4603](group__devicetree-inst.md#gab29f18e52d7475245c9fbeb4cd8e7769)#define DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx) \

4604 DT\_IRQ\_INTC\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4605

[ 4612](group__devicetree-inst.md#gadd0f339e10b071da34d44922ad0c7bfd)#define DT\_INST\_IRQ\_INTC\_BY\_NAME(inst, name) \

4613 DT\_IRQ\_INTC\_BY\_NAME(DT\_DRV\_INST(inst), name)

4614

[ 4622](group__devicetree-inst.md#gabf127c8370af849d2b5560e87ee04809)#define DT\_INST\_IRQ\_INTC(inst) \

4623 DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, 0)

4624

[ 4632](group__devicetree-inst.md#ga1ff6f24f9c97d4b611e4bf50ce5175d3)#define DT\_INST\_IRQ\_BY\_NAME(inst, name, cell) \

4633 DT\_IRQ\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

4634

[ 4641](group__devicetree-inst.md#ga789eb58422bab7b3a79b487c4a8a82d6)#define DT\_INST\_IRQ(inst, cell) DT\_INST\_IRQ\_BY\_IDX(inst, 0, cell)

4642

[ 4648](group__devicetree-inst.md#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)#define DT\_INST\_IRQN(inst) DT\_IRQN(DT\_DRV\_INST(inst))

4649

[ 4656](group__devicetree-inst.md#gaeb0c023f53ed87a6707bbca8ba05ce45)#define DT\_INST\_IRQN\_BY\_IDX(inst, idx) DT\_IRQN\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4657

[ 4663](group__devicetree-inst.md#gacecb46743315738dcd9a0765ea78276a)#define DT\_INST\_BUS(inst) DT\_BUS(DT\_DRV\_INST(inst))

4664

[ 4672](group__devicetree-inst.md#ga7a29bda946b399a7af92ec9cd09b4e98)#define DT\_INST\_ON\_BUS(inst, bus) DT\_ON\_BUS(DT\_DRV\_INST(inst), bus)

4673

[ 4683](group__devicetree-inst.md#ga79fd00d1ece5538f7705c241ab869ea8)#define DT\_INST\_STRING\_TOKEN\_OR(inst, name, default\_value) \

4684 DT\_STRING\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4685

[ 4694](group__devicetree-inst.md#ga72981780b2ede73c49ef9e5a7c6247c2)#define DT\_INST\_STRING\_UPPER\_TOKEN\_OR(inst, name, default\_value) \

4695 DT\_STRING\_UPPER\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4696

[ 4705](group__devicetree-inst.md#ga56bc0c0a46f6be421082119604cde643)#define DT\_INST\_STRING\_UNQUOTED\_OR(inst, name, default\_value) \

4706 DT\_STRING\_UNQUOTED\_OR(DT\_DRV\_INST(inst), name, default\_value)

4707

[ 4738](group__devicetree-inst.md#ga1727af4beed08b248a98ad68bc5f1027)#define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus) \

4739 IS\_ENABLED(DT\_CAT4(DT\_COMPAT\_, compat, \_BUS\_, bus))

4740

[ 4773](group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)#define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus) \

4774 DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(DT\_DRV\_COMPAT, bus)

4775

[ 4820](group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735)#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop) \

4821 COND\_CODE\_1(IS\_EMPTY(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop)), (0), (1))

4822

[ 4867](group__devicetree-inst.md#ga052727464d4f04768eaa71b7522c9a61)#define DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY(compat, prop) \

4868 (DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, DT\_COMPAT\_NODE\_HAS\_PROP\_AND\_OR, prop) 0)

4869

[ 4917](group__devicetree-inst.md#gab3d2f48ad95c4e2af76eed5e34735b18)#define DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY(prop) \

4918 COND\_CODE\_1(IS\_EMPTY(DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY\_(prop)), (0), (1))

4919

[ 4985](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)#define DT\_INST\_FOREACH\_STATUS\_OKAY(fn) \

4986 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4987 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_, \

4988 DT\_DRV\_COMPAT)(fn)), \

4989 ())

4990

[ 5003](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38)#define DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(fn, ...) \

5004 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

5005 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

5006 DT\_DRV\_COMPAT)(fn, \_\_VA\_ARGS\_\_)), \

5007 ())

5008

[ 5018](group__devicetree-inst.md#gafd15350971dee495f955f2fcc7edd82c)#define DT\_INST\_FOREACH\_NODELABEL(inst, fn) \

5019 DT\_FOREACH\_NODELABEL(DT\_DRV\_INST(inst), fn)

5020

[ 5032](group__devicetree-inst.md#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)#define DT\_INST\_FOREACH\_NODELABEL\_VARGS(inst, fn, ...) \

5033 DT\_FOREACH\_NODELABEL\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

5034

[ 5045](group__devicetree-inst.md#gaf163f2f85b3893ca46c87f0fcbe65255)#define DT\_INST\_FOREACH\_PROP\_ELEM(inst, prop, fn) \

5046 DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)

5047

[ 5060](group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP(inst, prop, fn, sep) \

5061 DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)

5062

[ 5077](group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)#define DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS(inst, prop, fn, ...) \

5078 DT\_FOREACH\_PROP\_ELEM\_VARGS(DT\_DRV\_INST(inst), prop, fn, \_\_VA\_ARGS\_\_)

5079

[ 5097](group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(inst, prop, fn, sep, ...) \

5098 DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(DT\_DRV\_INST(inst), prop, fn, sep, \

5099 \_\_VA\_ARGS\_\_)

5100

[ 5107](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)#define DT\_INST\_NODE\_HAS\_PROP(inst, prop) \

5108 DT\_NODE\_HAS\_PROP(DT\_DRV\_INST(inst), prop)

5109

[ 5116](group__devicetree-inst.md#gaf88c7dc0e935ad7097e317e54c362ba0)#define DT\_INST\_NODE\_HAS\_COMPAT(inst, compat) \

5117 DT\_NODE\_HAS\_COMPAT(DT\_DRV\_INST(inst), compat)

5118

[ 5129](group__devicetree-inst.md#gae054b89701ec9fae577320fb7b9cae1e)#define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell) \

5130 DT\_PHA\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

5131

[ 5141](group__devicetree-inst.md#gab8083dae430aeb93a967bbf98aa9eefc)#define DT\_INST\_PHA\_HAS\_CELL(inst, pha, cell) \

5142 DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, 0, cell)

5143

[ 5151](group__devicetree-inst.md#gabb45132ef78818512c02bdf1f5a38068)#define DT\_INST\_IRQ\_HAS\_IDX(inst, idx) DT\_IRQ\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

5152

[ 5161](group__devicetree-inst.md#gab176ff07912cea915c811406e8f5e386)#define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell) \

5162 DT\_IRQ\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), idx, cell)

5163

[ 5171](group__devicetree-inst.md#gabec43df3451bd917120b283d76c57054)#define DT\_INST\_IRQ\_HAS\_CELL(inst, cell) \

5172 DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, 0, cell)

5173

[ 5180](group__devicetree-inst.md#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)#define DT\_INST\_IRQ\_HAS\_NAME(inst, name) \

5181 DT\_IRQ\_HAS\_NAME(DT\_DRV\_INST(inst), name)

5182

5186

5188

5200#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_(idx, prop) \

5201 COND\_CODE\_1(DT\_INST\_NODE\_HAS\_PROP(idx, prop), (1,), ())

5214#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop) \

5215 DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_, prop)

5216

5229#define DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY\_\_(idx, prop) \

5230 COND\_CODE\_1(DT\_INST\_PROP(idx, prop), (1,), ())

5243#define DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY\_(prop) \

5244 DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY\_\_, prop)

5245

5246#define DT\_PATH\_INTERNAL(...) \

5247 UTIL\_CAT(DT\_ROOT, MACRO\_MAP\_CAT(DT\_S\_PREFIX, \_\_VA\_ARGS\_\_))

5253#define DT\_S\_PREFIX(name) \_S\_##name

5254

5269#define DT\_CAT(a1, a2) a1 ## a2

5271#define DT\_CAT3(a1, a2, a3) a1 ## a2 ## a3

5273#define DT\_CAT4(a1, a2, a3, a4) a1 ## a2 ## a3 ## a4

5275#define DT\_CAT5(a1, a2, a3, a4, a5) a1 ## a2 ## a3 ## a4 ## a5

5277#define DT\_CAT6(a1, a2, a3, a4, a5, a6) a1 ## a2 ## a3 ## a4 ## a5 ## a6

5279#define DT\_CAT7(a1, a2, a3, a4, a5, a6, a7) \

5280 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7

5282#define DT\_CAT8(a1, a2, a3, a4, a5, a6, a7, a8) \

5283 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7 ## a8

5284/\*

5285 \* If you need to define a bigger DT\_CATN(), do so here. Don't leave

5286 \* any "holes" of undefined macros, please.

5287 \*/

5288

5290#define DT\_DASH(...) MACRO\_MAP\_CAT(DT\_DASH\_PREFIX, \_\_VA\_ARGS\_\_)

5292#define DT\_DASH\_PREFIX(name) \_##name

5294#define DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status) \

5295 IS\_ENABLED(DT\_CAT3(node\_id, \_STATUS\_, status))

5296

5300#define DT\_COMPAT\_NODE\_HAS\_PROP\_AND\_OR(inst, compat, prop) \

5301 DT\_NODE\_HAS\_PROP(DT\_INST(inst, compat), prop) ||

5302

5307#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

5308#define DT\_U32\_C(\_v) (\_v)

5309#else

5310#define DT\_U32\_C(\_v) UINT32\_C(\_v)

5311#endif

5312

5317#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

5318#define DT\_U64\_C(\_v) (\_v)

5319#else

5320#define DT\_U64\_C(\_v) UINT64\_C(\_v)

5321#endif

5322

5323/\* Helpers for DT\_NODELABEL\_STRING\_ARRAY. We define our own stringify

5324 \* in order to avoid adding a dependency on toolchain.h..

5325 \*/

5326#define DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL(nodelabel) DT\_STRINGIFY\_INTERNAL(nodelabel),

5327#define DT\_STRINGIFY\_INTERNAL(arg) DT\_STRINGIFY\_INTERNAL\_HELPER(arg)

5328#define DT\_STRINGIFY\_INTERNAL\_HELPER(arg) #arg

5329

5331

5332/\* have these last so they have access to all previously defined macros \*/

5333#include <[zephyr/devicetree/io-channels.h](io-channels_8h.md)>

5334#include <[zephyr/devicetree/clocks.h](clocks_8h.md)>

5335#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h.md)>

5336#include <[zephyr/devicetree/spi.h](devicetree_2spi_8h.md)>

5337#include <[zephyr/devicetree/dma.h](devicetree_2dma_8h.md)>

5338#include <[zephyr/devicetree/pwms.h](pwms_8h.md)>

5339#include <[zephyr/devicetree/fixed-partitions.h](fixed-partitions_8h.md)>

5340#include <[zephyr/devicetree/ordinals.h](ordinals_8h.md)>

5341#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

5342#include <[zephyr/devicetree/can.h](devicetree_2can_8h.md)>

5343#include <[zephyr/devicetree/reset.h](devicetree_2reset_8h.md)>

5344#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h.md)>

5345#include <[zephyr/devicetree/port-endpoint.h](port-endpoint_8h.md)>

5346

5347#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_H\_ \*/

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

[port-endpoint.h](port-endpoint_8h.md)

Port / Endpoint Devicetree macro public API header file.

[pwms.h](pwms_8h.md)

PWMs Devicetree macro public API header file.

[stdint.h](stdint_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree.h](devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
