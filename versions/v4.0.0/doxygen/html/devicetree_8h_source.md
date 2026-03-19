---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_8h_source.html
original_path: doxygen/html/devicetree_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 332](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)#define DT\_INST(inst, compat) UTIL\_CAT(DT\_N\_INST, DT\_DASH(inst, compat))

333

[ 357](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)#define DT\_PARENT(node\_id) DT\_CAT(node\_id, \_PARENT)

358

[ 382](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)#define DT\_GPARENT(node\_id) DT\_PARENT(DT\_PARENT(node\_id))

383

[ 419](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)#define DT\_CHILD(node\_id, child) UTIL\_CAT(node\_id, DT\_S\_PREFIX(child))

420

[ 462](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat) \

463 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

464 (DT\_INST(0, compat)), \

465 (DT\_INVALID\_NODE))

466

[ 494](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)#define DT\_NODE\_PATH(node\_id) DT\_CAT(node\_id, \_PATH)

495

[ 520](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)#define DT\_NODE\_FULL\_NAME(node\_id) DT\_CAT(node\_id, \_FULL\_NAME)

521

[ 548](group__devicetree-generic-id.md#ga8832fb6fa0e0555884621d210440fdcd)#define DT\_NODE\_FULL\_NAME\_UNQUOTED(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_UNQUOTED)

549

[ 576](group__devicetree-generic-id.md#gad24b51e728175e7d347407f2131a3850)#define DT\_NODE\_FULL\_NAME\_TOKEN(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_TOKEN)

577

[ 606](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)#define DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id) DT\_CAT(node\_id, \_FULL\_NAME\_UPPER\_TOKEN)

607

[ 634](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)#define DT\_NODE\_CHILD\_IDX(node\_id) DT\_CAT(node\_id, \_CHILD\_IDX)

635

[ 642](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)#define DT\_CHILD\_NUM(node\_id) DT\_CAT(node\_id, \_CHILD\_NUM)

643

644

[ 652](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)#define DT\_CHILD\_NUM\_STATUS\_OKAY(node\_id) \

653 DT\_CAT(node\_id, \_CHILD\_NUM\_STATUS\_OKAY)

654

[ 675](group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)#define DT\_SAME\_NODE(node\_id1, node\_id2) \

676 (DT\_DEP\_ORD(node\_id1) == (DT\_DEP\_ORD(node\_id2)))

677

[ 702](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)#define DT\_NODELABEL\_STRING\_ARRAY(node\_id) \

703 { DT\_FOREACH\_NODELABEL(node\_id, DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL) }

704

708

714

[ 745](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)#define DT\_PROP(node\_id, prop) DT\_CAT3(node\_id, \_P\_, prop)

746

[ 779](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)#define DT\_PROP\_LEN(node\_id, prop) DT\_CAT4(node\_id, \_P\_, prop, \_LEN)

780

[ 795](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value) \

796 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

797 (DT\_PROP\_LEN(node\_id, prop)), (default\_value))

798

[ 819](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx) \

820 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_EXISTS))

821

[ 854](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)#define DT\_PROP\_HAS\_NAME(node\_id, prop, name) \

855 IS\_ENABLED(DT\_CAT6(node\_id, \_P\_, prop, \_NAME\_, name, \_EXISTS))

856

[ 891](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)#define DT\_PROP\_BY\_IDX(node\_id, prop, idx) \

892 DT\_CAT5(node\_id, \_P\_, prop, \_IDX\_, idx)

893

[ 907](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)#define DT\_PROP\_OR(node\_id, prop, default\_value) \

908 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

909 (DT\_PROP(node\_id, prop)), (default\_value))

910

[ 966](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2)#define DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, idx) \

967 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_ENUM\_IDX)

968

[ 975](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)#define DT\_ENUM\_IDX(node\_id, prop) DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, 0)

976

[ 992](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73)#define DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, idx, default\_idx\_value) \

993 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, idx), \

994 (DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, idx)), (default\_idx\_value))

995

[ 1004](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value) \

1005 DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, 0, default\_idx\_value)

1006

[ 1016](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4)#define DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, idx, value) \

1017 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, prop, \_IDX\_, idx, \_ENUM\_VAL\_, value, \_EXISTS))

1018

[ 1026](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)#define DT\_ENUM\_HAS\_VALUE(node\_id, prop, value) \

1027 DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, 0, value)

1028

[ 1088](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)#define DT\_STRING\_TOKEN(node\_id, prop) \

1089 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_TOKEN)

1090

[ 1104](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value) \

1105 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1106 (DT\_STRING\_TOKEN(node\_id, prop)), (default\_value))

1107

[ 1165](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop) \

1166 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UPPER\_TOKEN)

1167

[ 1182](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value) \

1183 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1184 (DT\_STRING\_UPPER\_TOKEN(node\_id, prop)), (default\_value))

1185

[ 1226](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)#define DT\_STRING\_UNQUOTED(node\_id, prop) \

1227 DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UNQUOTED)

1228

[ 1243](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)#define DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value) \

1244 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

1245 (DT\_STRING\_UNQUOTED(node\_id, prop)), (default\_value))

1246

[ 1294](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1295 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_TOKEN)

1296

[ 1344](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx) \

1345 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UPPER\_TOKEN)

1346

[ 1387](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)#define DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx) \

1388 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UNQUOTED)

1389

1390/\*

1391 \* phandle properties

1392 \*

1393 \* These are special-cased to manage the impedance mismatch between

1394 \* phandles, which are just uint32\_t node properties that only make sense

1395 \* within the tree itself, and C values.

1396 \*/

1397

[ 1443](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop) \

1444 DT\_PROP(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop)

1445

[ 1465](group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b)#define DT\_PROP\_BY\_PHANDLE\_IDX\_OR(node\_id, phs, idx, prop, default\_value) \

1466 DT\_PROP\_OR(DT\_PHANDLE\_BY\_IDX(node\_id, phs, idx), prop, default\_value)

1467

[ 1479](group__devicetree-generic-prop.md#gabc1b099dda97fb03a9259a8b21fc04d2)#define DT\_PROP\_BY\_PHANDLE(node\_id, ph, prop) \

1480 DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)

1481

[ 1536](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell) \

1537 DT\_CAT7(node\_id, \_P\_, pha, \_IDX\_, idx, \_VAL\_, cell)

1538

[ 1562](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value) \

1563 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_IDX\_, idx, \_VAL\_, cell), default\_value)

1564

[ 1572](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)#define DT\_PHA(node\_id, pha, cell) DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)

1573

[ 1588](group__devicetree-generic-prop.md#ga886559b058b24164b62ab95215d860bd)#define DT\_PHA\_OR(node\_id, pha, cell, default\_value) \

1589 DT\_PHA\_BY\_IDX\_OR(node\_id, pha, 0, cell, default\_value)

1590

[ 1631](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell) \

1632 DT\_CAT7(node\_id, \_P\_, pha, \_NAME\_, name, \_VAL\_, cell)

1633

[ 1655](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value) \

1656 DT\_PROP\_OR(node\_id, DT\_CAT5(pha, \_NAME\_, name, \_VAL\_, cell), default\_value)

1657

[ 1705](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name) \

1706 DT\_CAT6(node\_id, \_P\_, pha, \_NAME\_, name, \_PH)

1707

[ 1757](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx) \

1758 DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_PH)

1759

[ 1771](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)#define DT\_PHANDLE(node\_id, prop) DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)

1772

1776

1782

[ 1819](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc)#define DT\_NUM\_RANGES(node\_id) DT\_CAT(node\_id, \_RANGES\_NUM)

1820

[ 1873](group__devicetree-ranges-prop.md#gac6f54058c58b06935bd2deae9f1ec2db)#define DT\_RANGES\_HAS\_IDX(node\_id, idx) \

1874 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_EXISTS))

1875

[ 1928](group__devicetree-ranges-prop.md#ga3730c9176911bd8cc762f447eb020ecd)#define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx) \

1929 IS\_ENABLED(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS\_EXISTS))

1930

[ 1968](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx) \

1969 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS)

1970

[ 2017](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

2018 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_ADDRESS)

2019

[ 2066](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx) \

2067 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_PARENT\_BUS\_ADDRESS)

2068

[ 2115](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx) \

2116 DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_LENGTH)

2117

[ 2157](group__devicetree-ranges-prop.md#ga4c71a8adcfe6c53b480775510c92a632)#define DT\_FOREACH\_RANGE(node\_id, fn) \

2158 DT\_CAT(node\_id, \_FOREACH\_RANGE)(fn)

2159

2163

2169

[ 2205](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747)#define DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx) \

2206 DT\_CAT3(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx)

2207

[ 2220](group__devicetree-generic-vendor.md#gabfa4130fa24457c457961caa7e2c6276)#define DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx) \

2221 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx, \_EXISTS))

2222

[ 2237](group__devicetree-generic-vendor.md#gaa71b1152516847d51582b9b23c472f3d)#define DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2238 COND\_CODE\_1(DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx), \

2239 (DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)), (default\_value))

2240

[ 2249](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)#define DT\_NODE\_VENDOR\_OR(node\_id, default\_value) \

2250 DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, 0, default\_value)

2251

[ 2281](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)#define DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx) \

2282 DT\_CAT3(node\_id, \_COMPAT\_MODEL\_IDX\_, idx)

2283

[ 2296](group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)#define DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx) \

2297 IS\_ENABLED(DT\_CAT4(node\_id, \_COMPAT\_MODEL\_IDX\_, idx, \_EXISTS))

2298

[ 2313](group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)#define DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, idx, default\_value) \

2314 COND\_CODE\_1(DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx), \

2315 (DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)), (default\_value))

2316

[ 2325](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)#define DT\_NODE\_MODEL\_OR(node\_id, default\_value) \

2326 DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, 0, default\_value)

2327

2331

2337

[ 2345](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)#define DT\_NUM\_REGS(node\_id) DT\_CAT(node\_id, \_REG\_NUM)

2346

[ 2358](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)#define DT\_REG\_HAS\_IDX(node\_id, idx) \

2359 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_EXISTS))

2360

[ 2372](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)#define DT\_REG\_HAS\_NAME(node\_id, name) \

2373 IS\_ENABLED(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_EXISTS))

2374

[ 2386](group__devicetree-reg-prop.md#ga226e23a6bb94beee690ff6e1cdfbab91)#define DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx) \

2387 DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

2388

[ 2400](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)#define DT\_REG\_ADDR\_RAW(node\_id) \

2401 DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, 0)

2402

[ 2409](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx) \

2410 DT\_U32\_C(DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx))

2411

[ 2423](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx) \

2424 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE))

2425

[ 2433](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)#define DT\_REG\_ADDR(node\_id) DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)

2434

[ 2445](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)#define DT\_REG\_ADDR\_U64(node\_id) DT\_U64\_C(DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, 0))

2446

[ 2454](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)#define DT\_REG\_SIZE(node\_id) DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)

2455

[ 2462](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name) \

2463 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

2464

[ 2473](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)#define DT\_REG\_ADDR\_BY\_NAME\_OR(node\_id, name, default\_value) \

2474 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2475 (DT\_REG\_ADDR\_BY\_NAME(node\_id, name)), (default\_value))

2476

[ 2489](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)#define DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name) \

2490 DT\_U64\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

2491

[ 2498](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name) \

2499 DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE))

2500

[ 2509](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)#define DT\_REG\_SIZE\_BY\_NAME\_OR(node\_id, name, default\_value) \

2510 COND\_CODE\_1(DT\_REG\_HAS\_NAME(node\_id, name), \

2511 (DT\_REG\_SIZE\_BY\_NAME(node\_id, name)), (default\_value))

2512

2513

2517

2523

[ 2532](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)#define DT\_NUM\_IRQS(node\_id) DT\_CAT(node\_id, \_IRQ\_NUM)

2533

[ 2558](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)#define DT\_NUM\_NODELABELS(node\_id) DT\_CAT(node\_id, \_NODELABEL\_NUM)

2559

[ 2566](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)#define DT\_IRQ\_LEVEL(node\_id) DT\_CAT(node\_id, \_IRQ\_LEVEL)

2567

[ 2578](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)#define DT\_IRQ\_HAS\_IDX(node\_id, idx) \

2579 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_EXISTS))

2580

[ 2591](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell) \

2592 IS\_ENABLED(DT\_CAT6(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

2593

[ 2601](group__devicetree-interrupts-prop.md#gab9c94ee39db7913598a755c6172fe036)#define DT\_IRQ\_HAS\_CELL(node\_id, cell) DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)

2602

[ 2612](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)#define DT\_IRQ\_HAS\_NAME(node\_id, name) \

2613 IS\_ENABLED(DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_VAL\_irq\_EXISTS))

2614

[ 2650](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell) \

2651 DT\_CAT5(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell)

2652

[ 2668](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)#define DT\_IRQ\_BY\_NAME(node\_id, name, cell) \

2669 DT\_CAT5(node\_id, \_IRQ\_NAME\_, name, \_VAL\_, cell)

2670

[ 2678](group__devicetree-interrupts-prop.md#gabf60fbd528d300a26c0b4e66fe80a53f)#define DT\_IRQ(node\_id, cell) DT\_IRQ\_BY\_IDX(node\_id, 0, cell)

2679

[ 2722](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx) \

2723 DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_CONTROLLER)

2724

[ 2769](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)#define DT\_IRQ\_INTC\_BY\_NAME(node\_id, name) \

2770 DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_CONTROLLER)

2771

[ 2811](group__devicetree-interrupts-prop.md#ga11d2680614de65fd8cb4a3909e93e9c9)#define DT\_IRQ\_INTC(node\_id) \

2812 DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)

2813

2817

2818/\* DT helper macro to encode a node's IRQN to level 1 according to the multi-level scheme \*/

2819#define DT\_IRQN\_L1\_INTERNAL(node\_id, idx) DT\_IRQ\_BY\_IDX(node\_id, idx, irq)

2820/\* DT helper macro to encode a node's IRQN to level 2 according to the multi-level scheme \*/

2821#define DT\_IRQN\_L2\_INTERNAL(node\_id, idx) \

2822 (IRQ\_TO\_L2(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2823 DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq))

2824/\* DT helper macro to encode a node's IRQN to level 3 according to the multi-level scheme \*/

2825#define DT\_IRQN\_L3\_INTERNAL(node\_id, idx) \

2826 (IRQ\_TO\_L3(DT\_IRQN\_L1\_INTERNAL(node\_id, idx)) | \

2827 IRQ\_TO\_L2(DT\_IRQ(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx), irq)) | \

2828 DT\_IRQ(DT\_IRQ\_INTC(DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)), irq))

2829/\* DT helper macro for the macros above \*/

2830#define DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, level) DT\_CAT3(DT\_IRQN\_L, level, \_INTERNAL)(node\_id, idx)

2831

2836#define DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx) \

2837 DT\_IRQN\_LVL\_INTERNAL(node\_id, idx, DT\_IRQ\_LEVEL(node\_id))

2838

2842

[ 2851](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)#define DT\_IRQN\_BY\_IDX(node\_id, idx) \

2852 COND\_CODE\_1(IS\_ENABLED(CONFIG\_MULTI\_LEVEL\_INTERRUPTS), \

2853 (DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx)), \

2854 (DT\_IRQ\_BY\_IDX(node\_id, idx, irq)))

2855

[ 2866](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)#define DT\_IRQN(node\_id) DT\_IRQN\_BY\_IDX(node\_id, 0)

2867

2871

2877

[ 2886](group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed)#define DT\_CHOSEN(prop) DT\_CAT(DT\_CHOSEN\_, prop)

2887

[ 2894](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)#define DT\_HAS\_CHOSEN(prop) IS\_ENABLED(DT\_CAT3(DT\_CHOSEN\_, prop, \_EXISTS))

2895

2899

2905

[ 2915](group__devicetree-generic-foreach.md#gad27b29ae71a3d3294984fd3bc721121d)#define DT\_FOREACH\_NODE(fn) DT\_FOREACH\_HELPER(fn)

2916

[ 2929](group__devicetree-generic-foreach.md#ga4e708120bf839568b1215a6c21c54eed)#define DT\_FOREACH\_NODE\_VARGS(fn, ...) DT\_FOREACH\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2930

[ 2942](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn) DT\_FOREACH\_OKAY\_HELPER(fn)

2943

[ 2958](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)#define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn, ...) DT\_FOREACH\_OKAY\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

2959

[ 3003](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)#define DT\_FOREACH\_CHILD(node\_id, fn) \

3004 DT\_CAT(node\_id, \_FOREACH\_CHILD)(fn)

3005

[ 3046](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep) \

3047 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP)(fn, sep)

3048

[ 3064](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)#define DT\_FOREACH\_CHILD\_VARGS(node\_id, fn, ...) \

3065 DT\_CAT(node\_id, \_FOREACH\_CHILD\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3066

[ 3082](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)#define DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep, ...) \

3083 DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

3084

[ 3100](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn) \

3101 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY)(fn)

3102

[ 3119](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep) \

3120 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP)(fn, sep)

3121

[ 3141](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn, ...) \

3142 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3143

[ 3162](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep, ...) \

3163 DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

3164

[ 3215](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn) \

3216 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM)(fn)

3217

[ 3260](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep) \

3261 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP)(fn, sep)

3262

[ 3283](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn, ...) \

3284 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3285

[ 3302](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)#define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep, ...) \

3303 DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP\_VARGS)( \

3304 fn, sep, \_\_VA\_ARGS\_\_)

3305

[ 3359](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)#define DT\_FOREACH\_STATUS\_OKAY(compat, fn) \

3360 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3361 (UTIL\_CAT(DT\_FOREACH\_OKAY\_, compat)(fn)), \

3362 ())

3363

[ 3408](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3409 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3410 (DT\_CAT(DT\_FOREACH\_OKAY\_VARGS\_, \

3411 compat)(fn, \_\_VA\_ARGS\_\_)), \

3412 ())

3413

[ 3426](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9)#define DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn, ...) \

3427 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3428 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

3429 compat)(fn, compat, \_\_VA\_ARGS\_\_)), \

3430 ())

3431

3432

[ 3471](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)#define DT\_FOREACH\_NODELABEL(node\_id, fn) DT\_CAT(node\_id, \_FOREACH\_NODELABEL)(fn)

3472

[ 3510](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)#define DT\_FOREACH\_NODELABEL\_VARGS(node\_id, fn, ...) \

3511 DT\_CAT(node\_id, \_FOREACH\_NODELABEL\_VARGS)(fn, \_\_VA\_ARGS\_\_)

3512

3516

3522

[ 3537](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)#define DT\_NODE\_EXISTS(node\_id) IS\_ENABLED(DT\_CAT(node\_id, \_EXISTS))

3538

[ 3560](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)#define DT\_NODE\_HAS\_STATUS(node\_id, status) \

3561 DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status)

3562

[ 3583](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)#define DT\_NODE\_HAS\_STATUS\_OKAY(node\_id) DT\_NODE\_HAS\_STATUS(node\_id, okay)

3584

[ 3604](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat) \

3605 IS\_ENABLED(DT\_CAT(DT\_COMPAT\_HAS\_OKAY\_, compat))

3606

[ 3613](group__devicetree-generic-exist.md#ga45c268d7f0d604a72dc0bcf5cd0733b0)#define DT\_NUM\_INST\_STATUS\_OKAY(compat) \

3614 UTIL\_AND(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

3615 UTIL\_CAT(DT\_N\_INST, DT\_DASH(compat, NUM\_OKAY)))

3616

[ 3644](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)#define DT\_NODE\_HAS\_COMPAT(node\_id, compat) \

3645 IS\_ENABLED(DT\_CAT3(node\_id, \_COMPAT\_MATCHES\_, compat))

3646

[ 3661](group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)#define DT\_NODE\_HAS\_COMPAT\_STATUS(node\_id, compat, status) \

3662 UTIL\_AND(DT\_NODE\_HAS\_COMPAT(node\_id, compat), DT\_NODE\_HAS\_STATUS(node\_id, status))

3663

[ 3677](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)#define DT\_NODE\_HAS\_PROP(node\_id, prop) \

3678 IS\_ENABLED(DT\_CAT4(node\_id, \_P\_, prop, \_EXISTS))

3679

3680

[ 3697](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell) \

3698 IS\_ENABLED(DT\_CAT8(node\_id, \_P\_, pha, \

3699 \_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

3700

[ 3710](group__devicetree-generic-exist.md#gaece280102681cbadf318c5dabfb3d719)#define DT\_PHA\_HAS\_CELL(node\_id, pha, cell) \

3711 DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)

3712

3716

3722

[ 3754](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)#define DT\_BUS(node\_id) DT\_CAT(node\_id, \_BUS)

3755

[ 3784](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)#define DT\_ON\_BUS(node\_id, bus) IS\_ENABLED(DT\_CAT3(node\_id, \_BUS\_, bus))

3785

3789

3795

[ 3802](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)#define DT\_DRV\_INST(inst) DT\_INST(inst, DT\_DRV\_COMPAT)

3803

[ 3811](group__devicetree-inst.md#ga176760ce1a019020b5465eebd4f44ff5)#define DT\_INST\_PARENT(inst) DT\_PARENT(DT\_DRV\_INST(inst))

3812

[ 3820](group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)#define DT\_INST\_GPARENT(inst) DT\_GPARENT(DT\_DRV\_INST(inst))

3821

[ 3831](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)#define DT\_INST\_CHILD(inst, child) \

3832 DT\_CHILD(DT\_DRV\_INST(inst), child)

3833

[ 3843](group__devicetree-inst.md#ga49e2e39f4d93956217584df40316290b)#define DT\_INST\_CHILD\_NUM(inst) DT\_CHILD\_NUM(DT\_DRV\_INST(inst))

3844

[ 3854](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)#define DT\_INST\_CHILD\_NUM\_STATUS\_OKAY(inst) \

3855 DT\_CHILD\_NUM\_STATUS\_OKAY(DT\_DRV\_INST(inst))

3856

[ 3865](group__devicetree-inst.md#gaabb1a53b444221d82d865ec8d23c8278)#define DT\_INST\_NODELABEL\_STRING\_ARRAY(inst) DT\_NODELABEL\_STRING\_ARRAY(DT\_DRV\_INST(inst))

3866

[ 3875](group__devicetree-inst.md#ga2c43ec7309f5cdf8139a8b5fab63f786)#define DT\_INST\_NUM\_NODELABELS(inst) DT\_NUM\_NODELABELS(DT\_DRV\_INST(inst))

3876

[ 3891](group__devicetree-inst.md#ga98f3fccc6f3004f72c3602a5f2b3a08e)#define DT\_INST\_FOREACH\_CHILD(inst, fn) \

3892 DT\_FOREACH\_CHILD(DT\_DRV\_INST(inst), fn)

3893

[ 3907](group__devicetree-inst.md#gae8d01eb2d6a576246f225a5cbbec34e5)#define DT\_INST\_FOREACH\_CHILD\_SEP(inst, fn, sep) \

3908 DT\_FOREACH\_CHILD\_SEP(DT\_DRV\_INST(inst), fn, sep)

3909

[ 3925](group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651)#define DT\_INST\_FOREACH\_CHILD\_VARGS(inst, fn, ...) \

3926 DT\_FOREACH\_CHILD\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3927

[ 3942](group__devicetree-inst.md#gac70fcf3052d9dfa949d7e197fece1413)#define DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS(inst, fn, sep, ...) \

3943 DT\_FOREACH\_CHILD\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

3944

[ 3956](group__devicetree-inst.md#gad416dd269b1af1e392ef81397b9bc814)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY(inst, fn) \

3957 DT\_FOREACH\_CHILD\_STATUS\_OKAY(DT\_DRV\_INST(inst), fn)

3958

[ 3973](group__devicetree-inst.md#gae28554827ab7aaac3578ef07747a589d)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(inst, fn, sep) \

3974 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(DT\_DRV\_INST(inst), fn, sep)

3975

[ 3989](group__devicetree-inst.md#gac6dd19b2b6e603c11701cd07daec73d3)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(inst, fn, ...) \

3990 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

3991

[ 4007](group__devicetree-inst.md#ga236cca0984f1c701c9b4855111c6cb29)#define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(inst, fn, sep, ...) \

4008 DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(DT\_DRV\_INST(inst), fn, sep, \_\_VA\_ARGS\_\_)

4009

[ 4017](group__devicetree-inst.md#ga9de99aff4800b0f6f461fdb48bcc3969)#define DT\_INST\_ENUM\_IDX\_BY\_IDX(inst, prop, idx) \

4018 DT\_ENUM\_IDX\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4019

[ 4026](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2)#define DT\_INST\_ENUM\_IDX(inst, prop) \

4027 DT\_ENUM\_IDX(DT\_DRV\_INST(inst), prop)

4028

[ 4038](group__devicetree-inst.md#ga48315c386a33d9384078c4a4fcccfd5d)#define DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR(inst, prop, idx, default\_idx\_value) \

4039 DT\_ENUM\_IDX\_BY\_IDX\_OR(DT\_DRV\_INST(inst), prop, idx, default\_idx\_value)

4040

[ 4049](group__devicetree-inst.md#gafbf64148f9171ffd322f7689297e0da8)#define DT\_INST\_ENUM\_IDX\_OR(inst, prop, default\_idx\_value) \

4050 DT\_ENUM\_IDX\_OR(DT\_DRV\_INST(inst), prop, default\_idx\_value)

4051

[ 4060](group__devicetree-inst.md#ga5057571e3996451258ae5c29a06d9ede)#define DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX(inst, prop, idx, value) \

4061 DT\_ENUM\_HAS\_VALUE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx, value)

4062

[ 4071](group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601)#define DT\_INST\_ENUM\_HAS\_VALUE(inst, prop, value) \

4072 DT\_ENUM\_HAS\_VALUE(DT\_DRV\_INST(inst), prop, value)

4073

[ 4080](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)#define DT\_INST\_PROP(inst, prop) DT\_PROP(DT\_DRV\_INST(inst), prop)

4081

[ 4088](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365)#define DT\_INST\_PROP\_LEN(inst, prop) DT\_PROP\_LEN(DT\_DRV\_INST(inst), prop)

4089

[ 4099](group__devicetree-inst.md#ga2c51745f8d51b1d9cdfb1cde69911d48)#define DT\_INST\_PROP\_HAS\_IDX(inst, prop, idx) \

4100 DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx)

4101

[ 4110](group__devicetree-inst.md#ga75e13dcdbcc51da1334fa14653411dd8)#define DT\_INST\_PROP\_HAS\_NAME(inst, prop, name) \

4111 DT\_PROP\_HAS\_NAME(DT\_DRV\_INST(inst), prop, name)

4112

[ 4120](group__devicetree-inst.md#ga5b60f4ed4f5dadc5dd425f5905f23b00)#define DT\_INST\_PROP\_BY\_IDX(inst, prop, idx) \

4121 DT\_PROP\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4122

[ 4130](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)#define DT\_INST\_PROP\_OR(inst, prop, default\_value) \

4131 DT\_PROP\_OR(DT\_DRV\_INST(inst), prop, default\_value)

4132

[ 4140](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)#define DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value) \

4141 DT\_PROP\_LEN\_OR(DT\_DRV\_INST(inst), prop, default\_value)

4142

[ 4152](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484)#define DT\_INST\_STRING\_TOKEN(inst, prop) \

4153 DT\_STRING\_TOKEN(DT\_DRV\_INST(inst), prop)

4154

[ 4162](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5)#define DT\_INST\_STRING\_UPPER\_TOKEN(inst, prop) \

4163 DT\_STRING\_UPPER\_TOKEN(DT\_DRV\_INST(inst), prop)

4164

[ 4173](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228)#define DT\_INST\_STRING\_UNQUOTED(inst, prop) \

4174 DT\_STRING\_UNQUOTED(DT\_DRV\_INST(inst), prop)

4175

[ 4183](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97)#define DT\_INST\_STRING\_TOKEN\_BY\_IDX(inst, prop, idx) \

4184 DT\_STRING\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4185

[ 4193](group__devicetree-inst.md#ga4ceceec8375d70b40a4dec1a8ab5ee29)#define DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX(inst, prop, idx) \

4194 DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4195

[ 4203](group__devicetree-inst.md#gac5768077e2a3d14a69efc653cfc59d5d)#define DT\_INST\_STRING\_UNQUOTED\_BY\_IDX(inst, prop, idx) \

4204 DT\_STRING\_UNQUOTED\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4205

[ 4214](group__devicetree-inst.md#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)#define DT\_INST\_PROP\_BY\_PHANDLE(inst, ph, prop) \

4215 DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, ph, 0, prop)

4216

[ 4228](group__devicetree-inst.md#gad027963bdf159942cf6fb28b04e8d48e)#define DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop) \

4229 DT\_PROP\_BY\_PHANDLE\_IDX(DT\_DRV\_INST(inst), phs, idx, prop)

4230

[ 4239](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018)#define DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell) \

4240 DT\_PHA\_BY\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4241

[ 4251](group__devicetree-inst.md#ga3db4c00e072bd93fa92e36907b2b5e86)#define DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value) \

4252 DT\_PHA\_BY\_IDX\_OR(DT\_DRV\_INST(inst), pha, idx, cell, default\_value)

4253

[ 4262](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8)#define DT\_INST\_PHA(inst, pha, cell) DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)

4263

[ 4272](group__devicetree-inst.md#ga491ad421602e41c4295bac61b595fc94)#define DT\_INST\_PHA\_OR(inst, pha, cell, default\_value) \

4273 DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, 0, cell, default\_value)

4274

[ 4284](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8)#define DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell) \

4285 DT\_PHA\_BY\_NAME(DT\_DRV\_INST(inst), pha, name, cell)

4286

[ 4296](group__devicetree-inst.md#gaaebc5c643b60319f7e767e46ca226729)#define DT\_INST\_PHA\_BY\_NAME\_OR(inst, pha, name, cell, default\_value) \

4297 DT\_PHA\_BY\_NAME\_OR(DT\_DRV\_INST(inst), pha, name, cell, default\_value)

4298

[ 4307](group__devicetree-inst.md#ga64d8ddaad8b2d3852e30686d3adf6551)#define DT\_INST\_PHANDLE\_BY\_NAME(inst, pha, name) \

4308 DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), pha, name) \

4309

4310

[ 4319](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx) \

4320 DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

4321

[ 4330](group__devicetree-inst.md#ga81c10f478c86e5a4c18eb7a990447137)#define DT\_INST\_PHANDLE(inst, prop) DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, 0)

4331

[ 4339](group__devicetree-inst.md#ga26bbff9ebaed549140d2530a0b99e8a4)#define DT\_INST\_REG\_HAS\_IDX(inst, idx) DT\_REG\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4340

[ 4348](group__devicetree-inst.md#ga8b15b84b03c3dc6fd9d7e127a44392b3)#define DT\_INST\_REG\_HAS\_NAME(inst, name) DT\_REG\_HAS\_NAME(DT\_DRV\_INST(inst), name)

4349

[ 4356](group__devicetree-inst.md#gade870f8f5c78c3c6244ada35049334a5)#define DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW(inst, idx) DT\_REG\_ADDR\_BY\_IDX\_RAW(DT\_DRV\_INST(inst), idx)

4357

[ 4364](group__devicetree-inst.md#ga0fe0403821883598da6cfad4f3962115)#define DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx) DT\_REG\_ADDR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4365

[ 4372](group__devicetree-inst.md#gab1152c9f069c69b0269c1a4e744b9dd9)#define DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx) \

4373 DT\_REG\_SIZE\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4374

[ 4381](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c)#define DT\_INST\_REG\_ADDR\_BY\_NAME(inst, name) \

4382 DT\_REG\_ADDR\_BY\_NAME(DT\_DRV\_INST(inst), name)

4383

[ 4392](group__devicetree-inst.md#gaf8d6ec7f68f566360743f7ea7cb7f8fb)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_OR(inst, name, default\_value) \

4393 DT\_REG\_ADDR\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4394

[ 4407](group__devicetree-inst.md#ga8af83c4c65e607b93aa60a690295d625)#define DT\_INST\_REG\_ADDR\_BY\_NAME\_U64(inst, name) \

4408 DT\_REG\_ADDR\_BY\_NAME\_U64(DT\_DRV\_INST(inst), name)

4409

[ 4416](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714)#define DT\_INST\_REG\_SIZE\_BY\_NAME(inst, name) \

4417 DT\_REG\_SIZE\_BY\_NAME(DT\_DRV\_INST(inst), name)

4418

[ 4427](group__devicetree-inst.md#ga8494b94b6dbec875eba61e10f269cce6)#define DT\_INST\_REG\_SIZE\_BY\_NAME\_OR(inst, name, default\_value) \

4428 DT\_REG\_SIZE\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

4429

[ 4435](group__devicetree-inst.md#ga79627566ff2486cfd2425a04974d71a3)#define DT\_INST\_REG\_ADDR\_RAW(inst) DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW(inst, 0)

4436

[ 4442](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7)#define DT\_INST\_REG\_ADDR(inst) DT\_INST\_REG\_ADDR\_BY\_IDX(inst, 0)

4443

[ 4455](group__devicetree-inst.md#gaba47dcabd8754eda87e35efd7289f976)#define DT\_INST\_REG\_ADDR\_U64(inst) DT\_REG\_ADDR\_U64(DT\_DRV\_INST(inst))

4456

[ 4462](group__devicetree-inst.md#gaa7cea29435e1db59470302abb5ee88dd)#define DT\_INST\_REG\_SIZE(inst) DT\_INST\_REG\_SIZE\_BY\_IDX(inst, 0)

4463

[ 4470](group__devicetree-inst.md#ga446d4b9c267e7c9da73dfb8a07701f2a)#define DT\_INST\_NUM\_IRQS(inst) DT\_NUM\_IRQS(DT\_DRV\_INST(inst))

4471

[ 4478](group__devicetree-inst.md#ga5c06043fd17c891e2cbbe0508248b638)#define DT\_INST\_IRQ\_LEVEL(inst) DT\_IRQ\_LEVEL(DT\_DRV\_INST(inst))

4479

[ 4487](group__devicetree-inst.md#gad0d69a61ad842aa1dc3a5d4a304c3f2f)#define DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell) \

4488 DT\_IRQ\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

4489

[ 4496](group__devicetree-inst.md#gab29f18e52d7475245c9fbeb4cd8e7769)#define DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx) \

4497 DT\_IRQ\_INTC\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4498

[ 4505](group__devicetree-inst.md#gadd0f339e10b071da34d44922ad0c7bfd)#define DT\_INST\_IRQ\_INTC\_BY\_NAME(inst, name) \

4506 DT\_IRQ\_INTC\_BY\_NAME(DT\_DRV\_INST(inst), name)

4507

[ 4515](group__devicetree-inst.md#gabf127c8370af849d2b5560e87ee04809)#define DT\_INST\_IRQ\_INTC(inst) \

4516 DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, 0)

4517

[ 4525](group__devicetree-inst.md#ga1ff6f24f9c97d4b611e4bf50ce5175d3)#define DT\_INST\_IRQ\_BY\_NAME(inst, name, cell) \

4526 DT\_IRQ\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

4527

[ 4534](group__devicetree-inst.md#ga789eb58422bab7b3a79b487c4a8a82d6)#define DT\_INST\_IRQ(inst, cell) DT\_INST\_IRQ\_BY\_IDX(inst, 0, cell)

4535

[ 4541](group__devicetree-inst.md#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)#define DT\_INST\_IRQN(inst) DT\_IRQN(DT\_DRV\_INST(inst))

4542

[ 4549](group__devicetree-inst.md#gaeb0c023f53ed87a6707bbca8ba05ce45)#define DT\_INST\_IRQN\_BY\_IDX(inst, idx) DT\_IRQN\_BY\_IDX(DT\_DRV\_INST(inst), idx)

4550

[ 4556](group__devicetree-inst.md#gacecb46743315738dcd9a0765ea78276a)#define DT\_INST\_BUS(inst) DT\_BUS(DT\_DRV\_INST(inst))

4557

[ 4565](group__devicetree-inst.md#ga7a29bda946b399a7af92ec9cd09b4e98)#define DT\_INST\_ON\_BUS(inst, bus) DT\_ON\_BUS(DT\_DRV\_INST(inst), bus)

4566

[ 4576](group__devicetree-inst.md#ga79fd00d1ece5538f7705c241ab869ea8)#define DT\_INST\_STRING\_TOKEN\_OR(inst, name, default\_value) \

4577 DT\_STRING\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4578

[ 4587](group__devicetree-inst.md#ga72981780b2ede73c49ef9e5a7c6247c2)#define DT\_INST\_STRING\_UPPER\_TOKEN\_OR(inst, name, default\_value) \

4588 DT\_STRING\_UPPER\_TOKEN\_OR(DT\_DRV\_INST(inst), name, default\_value)

4589

[ 4598](group__devicetree-inst.md#ga56bc0c0a46f6be421082119604cde643)#define DT\_INST\_STRING\_UNQUOTED\_OR(inst, name, default\_value) \

4599 DT\_STRING\_UNQUOTED\_OR(DT\_DRV\_INST(inst), name, default\_value)

4600

4601/\*

4602 \* @brief Test if any enabled node with the given compatible is on

4603 \* the given bus type

4604 \*

4605 \* This is like DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(), except it can also

4606 \* be useful for handling multiple compatibles in single source file.

4607 \*

4608 \* Example devicetree overlay:

4609 \*

4610 \* @code{.dts}

4611 \* &i2c0 {

4612 \* temp: temperature-sensor@76 {

4613 \* compatible = "vnd,some-sensor";

4614 \* reg = <0x76>;

4615 \* };

4616 \* };

4617 \* @endcode

4618 \*

4619 \* Example usage, assuming `i2c0` is an I2C bus controller node, and

4620 \* therefore `temp` is on an I2C bus:

4621 \*

4622 \* @code{.c}

4623 \* DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(vnd\_some\_sensor, i2c) // 1

4624 \* @endcode

4625 \*

4626 \* @param compat lowercase-and-underscores compatible, without quotes

4627 \* @param bus a binding's bus type as a C token, lowercased and without quotes

4628 \* @return 1 if any enabled node with that compatible is on that bus type,

4629 \* 0 otherwise

4630 \*/

[ 4631](group__devicetree-inst.md#ga1727af4beed08b248a98ad68bc5f1027)#define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus) \

4632 IS\_ENABLED(DT\_CAT4(DT\_COMPAT\_, compat, \_BUS\_, bus))

4633

[ 4666](group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)#define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus) \

4667 DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(DT\_DRV\_COMPAT, bus)

4668

[ 4713](group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735)#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop) \

4714 COND\_CODE\_1(IS\_EMPTY(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop)), (0), (1))

4715

[ 4760](group__devicetree-inst.md#ga052727464d4f04768eaa71b7522c9a61)#define DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY(compat, prop) \

4761 (DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, DT\_COMPAT\_NODE\_HAS\_PROP\_AND\_OR, prop) 0)

4762

[ 4828](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)#define DT\_INST\_FOREACH\_STATUS\_OKAY(fn) \

4829 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4830 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_, \

4831 DT\_DRV\_COMPAT)(fn)), \

4832 ())

4833

[ 4846](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38)#define DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(fn, ...) \

4847 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), \

4848 (UTIL\_CAT(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

4849 DT\_DRV\_COMPAT)(fn, \_\_VA\_ARGS\_\_)), \

4850 ())

4851

[ 4861](group__devicetree-inst.md#gafd15350971dee495f955f2fcc7edd82c)#define DT\_INST\_FOREACH\_NODELABEL(inst, fn) \

4862 DT\_FOREACH\_NODELABEL(DT\_DRV\_INST(inst), fn)

4863

[ 4875](group__devicetree-inst.md#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)#define DT\_INST\_FOREACH\_NODELABEL\_VARGS(inst, fn, ...) \

4876 DT\_FOREACH\_NODELABEL\_VARGS(DT\_DRV\_INST(inst), fn, \_\_VA\_ARGS\_\_)

4877

[ 4888](group__devicetree-inst.md#gaf163f2f85b3893ca46c87f0fcbe65255)#define DT\_INST\_FOREACH\_PROP\_ELEM(inst, prop, fn) \

4889 DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)

4890

[ 4903](group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP(inst, prop, fn, sep) \

4904 DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)

4905

[ 4920](group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)#define DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS(inst, prop, fn, ...) \

4921 DT\_FOREACH\_PROP\_ELEM\_VARGS(DT\_DRV\_INST(inst), prop, fn, \_\_VA\_ARGS\_\_)

4922

[ 4940](group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)#define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(inst, prop, fn, sep, ...) \

4941 DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(DT\_DRV\_INST(inst), prop, fn, sep, \

4942 \_\_VA\_ARGS\_\_)

4943

[ 4950](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)#define DT\_INST\_NODE\_HAS\_PROP(inst, prop) \

4951 DT\_NODE\_HAS\_PROP(DT\_DRV\_INST(inst), prop)

4952

[ 4959](group__devicetree-inst.md#gaf88c7dc0e935ad7097e317e54c362ba0)#define DT\_INST\_NODE\_HAS\_COMPAT(inst, compat) \

4960 DT\_NODE\_HAS\_COMPAT(DT\_DRV\_INST(inst), compat)

4961

[ 4972](group__devicetree-inst.md#gae054b89701ec9fae577320fb7b9cae1e)#define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell) \

4973 DT\_PHA\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), pha, idx, cell)

4974

[ 4984](group__devicetree-inst.md#gab8083dae430aeb93a967bbf98aa9eefc)#define DT\_INST\_PHA\_HAS\_CELL(inst, pha, cell) \

4985 DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, 0, cell)

4986

[ 4994](group__devicetree-inst.md#gabb45132ef78818512c02bdf1f5a38068)#define DT\_INST\_IRQ\_HAS\_IDX(inst, idx) DT\_IRQ\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

4995

[ 5004](group__devicetree-inst.md#gab176ff07912cea915c811406e8f5e386)#define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell) \

5005 DT\_IRQ\_HAS\_CELL\_AT\_IDX(DT\_DRV\_INST(inst), idx, cell)

5006

[ 5014](group__devicetree-inst.md#gabec43df3451bd917120b283d76c57054)#define DT\_INST\_IRQ\_HAS\_CELL(inst, cell) \

5015 DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, 0, cell)

5016

[ 5023](group__devicetree-inst.md#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)#define DT\_INST\_IRQ\_HAS\_NAME(inst, name) \

5024 DT\_IRQ\_HAS\_NAME(DT\_DRV\_INST(inst), name)

5025

5029

5031

5043#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_(idx, prop) \

5044 COND\_CODE\_1(DT\_INST\_NODE\_HAS\_PROP(idx, prop), (1,), ())

5057#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop) \

5058 DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_\_, prop)

5059

5060#define DT\_PATH\_INTERNAL(...) \

5061 UTIL\_CAT(DT\_ROOT, MACRO\_MAP\_CAT(DT\_S\_PREFIX, \_\_VA\_ARGS\_\_))

5067#define DT\_S\_PREFIX(name) \_S\_##name

5068

5083#define DT\_CAT(a1, a2) a1 ## a2

5085#define DT\_CAT3(a1, a2, a3) a1 ## a2 ## a3

5087#define DT\_CAT4(a1, a2, a3, a4) a1 ## a2 ## a3 ## a4

5089#define DT\_CAT5(a1, a2, a3, a4, a5) a1 ## a2 ## a3 ## a4 ## a5

5091#define DT\_CAT6(a1, a2, a3, a4, a5, a6) a1 ## a2 ## a3 ## a4 ## a5 ## a6

5093#define DT\_CAT7(a1, a2, a3, a4, a5, a6, a7) \

5094 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7

5096#define DT\_CAT8(a1, a2, a3, a4, a5, a6, a7, a8) \

5097 a1 ## a2 ## a3 ## a4 ## a5 ## a6 ## a7 ## a8

5098/\*

5099 \* If you need to define a bigger DT\_CATN(), do so here. Don't leave

5100 \* any "holes" of undefined macros, please.

5101 \*/

5102

5104#define DT\_DASH(...) MACRO\_MAP\_CAT(DT\_DASH\_PREFIX, \_\_VA\_ARGS\_\_)

5106#define DT\_DASH\_PREFIX(name) \_##name

5108#define DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status) \

5109 IS\_ENABLED(DT\_CAT3(node\_id, \_STATUS\_, status))

5110

5114#define DT\_COMPAT\_NODE\_HAS\_PROP\_AND\_OR(inst, compat, prop) \

5115 DT\_NODE\_HAS\_PROP(DT\_INST(inst, compat), prop) ||

5116

5121#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

5122#define DT\_U32\_C(\_v) (\_v)

5123#else

5124#define DT\_U32\_C(\_v) UINT32\_C(\_v)

5125#endif

5126

5131#if defined(\_LINKER) || defined(\_ASMLANGUAGE)

5132#define DT\_U64\_C(\_v) (\_v)

5133#else

5134#define DT\_U64\_C(\_v) UINT64\_C(\_v)

5135#endif

5136

5137/\* Helpers for DT\_NODELABEL\_STRING\_ARRAY. We define our own stringify

5138 \* in order to avoid adding a dependency on toolchain.h..

5139 \*/

5140#define DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL(nodelabel) DT\_STRINGIFY\_INTERNAL(nodelabel),

5141#define DT\_STRINGIFY\_INTERNAL(arg) DT\_STRINGIFY\_INTERNAL\_HELPER(arg)

5142#define DT\_STRINGIFY\_INTERNAL\_HELPER(arg) #arg

5143

5145

5146/\* have these last so they have access to all previously defined macros \*/

5147#include <[zephyr/devicetree/io-channels.h](io-channels_8h.md)>

5148#include <[zephyr/devicetree/clocks.h](clocks_8h.md)>

5149#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h.md)>

5150#include <[zephyr/devicetree/spi.h](devicetree_2spi_8h.md)>

5151#include <[zephyr/devicetree/dma.h](devicetree_2dma_8h.md)>

5152#include <[zephyr/devicetree/pwms.h](pwms_8h.md)>

5153#include <[zephyr/devicetree/fixed-partitions.h](fixed-partitions_8h.md)>

5154#include <[zephyr/devicetree/ordinals.h](ordinals_8h.md)>

5155#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

5156#include <[zephyr/devicetree/can.h](devicetree_2can_8h.md)>

5157#include <[zephyr/devicetree/reset.h](devicetree_2reset_8h.md)>

5158#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h.md)>

5159

5160#endif /\* DEVICETREE\_H \*/

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

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree.h](devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
