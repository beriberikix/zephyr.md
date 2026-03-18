---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bitarray_8h_source.html
original_path: doxygen/html/bitarray_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bitarray.h

[Go to the documentation of this file.](bitarray_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_BITARRAY\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_BITARRAY\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <stddef.h>

15#include <[stdint.h](stdint_8h.md)>

16

17#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

18#include <[zephyr/sys/util.h](util_8h.md)>

19

30

32struct sys\_bitarray {

33 /\* Number of bits \*/

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bits;

35

36 /\* Number of bundles \*/

37 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bundles;

38

39 /\* Bundle of bits \*/

40 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bundles;

41

42 /\* Spinlock guarding access to this bit array \*/

43 struct k\_spinlock lock;

44};

46

[ 48](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841)typedef struct sys\_bitarray [sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841);

49

57#define \_SYS\_BITARRAY\_DEFINE(name, total\_bits, sba\_mod) \

58 sba\_mod uint32\_t \_sys\_bitarray\_bundles\_##name \

59 [DIV\_ROUND\_UP(DIV\_ROUND\_UP(total\_bits, 8), \

60 sizeof(uint32\_t))] = {0}; \

61 sba\_mod sys\_bitarray\_t name = { \

62 .num\_bits = total\_bits, \

63 .num\_bundles = DIV\_ROUND\_UP( \

64 DIV\_ROUND\_UP(total\_bits, 8), sizeof(uint32\_t)), \

65 .bundles = \_sys\_bitarray\_bundles\_##name, \

66 }

67

[ 74](group__bitarray__apis.md#gabbe958c6b995023665651e4aa050aa62)#define SYS\_BITARRAY\_DEFINE(name, total\_bits) \

75 \_SYS\_BITARRAY\_DEFINE(name, total\_bits,)

76

[ 83](group__bitarray__apis.md#ga2c55680355b67fc25125299a35f604d1)#define SYS\_BITARRAY\_DEFINE\_STATIC(name, total\_bits) \

84 \_SYS\_BITARRAY\_DEFINE(name, total\_bits, static)

85

[ 96](group__bitarray__apis.md#ga5fe657e79fee3e111284e4184eb6b681)int [sys\_bitarray\_set\_bit](group__bitarray__apis.md#ga5fe657e79fee3e111284e4184eb6b681)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t bit);

97

[ 108](group__bitarray__apis.md#ga795e8bf81f5717addf523cec124cde4e)int [sys\_bitarray\_clear\_bit](group__bitarray__apis.md#ga795e8bf81f5717addf523cec124cde4e)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t bit);

109

[ 121](group__bitarray__apis.md#gae024ace00949fe8c565081e62818449d)int [sys\_bitarray\_test\_bit](group__bitarray__apis.md#gae024ace00949fe8c565081e62818449d)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t bit, int \*val);

122

[ 134](group__bitarray__apis.md#gad1761b9eae8a1d9302893ce5f8591923)int [sys\_bitarray\_test\_and\_set\_bit](group__bitarray__apis.md#gad1761b9eae8a1d9302893ce5f8591923)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t bit, int \*prev\_val);

135

[ 147](group__bitarray__apis.md#ga40fa4d37f1fb2da8789f70de50c599d5)int [sys\_bitarray\_test\_and\_clear\_bit](group__bitarray__apis.md#ga40fa4d37f1fb2da8789f70de50c599d5)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t bit, int \*prev\_val);

148

[ 168](group__bitarray__apis.md#gac96766d9441a3b143aa386e2ac79ffd9)int [sys\_bitarray\_alloc](group__bitarray__apis.md#gac96766d9441a3b143aa386e2ac79ffd9)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

169 size\_t \*offset);

170

[ 186](group__bitarray__apis.md#gaf9a2c34896d3b1866a5a60f78d4166b0)int [sys\_bitarray\_free](group__bitarray__apis.md#gaf9a2c34896d3b1866a5a60f78d4166b0)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

187 size\_t offset);

188

[ 202](group__bitarray__apis.md#ga2aa91a9be38b11e74dacbeb2fe5e6d6d)bool [sys\_bitarray\_is\_region\_set](group__bitarray__apis.md#ga2aa91a9be38b11e74dacbeb2fe5e6d6d)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

203 size\_t offset);

204

[ 218](group__bitarray__apis.md#ga21cd833e7118f188ca3e06f8cfd13a49)bool [sys\_bitarray\_is\_region\_cleared](group__bitarray__apis.md#ga21cd833e7118f188ca3e06f8cfd13a49)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

219 size\_t offset);

220

[ 235](group__bitarray__apis.md#ga94d1a547b9fe0a01d73acf4a5c4f308b)int [sys\_bitarray\_set\_region](group__bitarray__apis.md#ga94d1a547b9fe0a01d73acf4a5c4f308b)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

236 size\_t offset);

237

[ 260](group__bitarray__apis.md#gad18590d2ab0bf251a59996620ed6e6bf)int [sys\_bitarray\_test\_and\_set\_region](group__bitarray__apis.md#gad18590d2ab0bf251a59996620ed6e6bf)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

261 size\_t offset, bool to\_set);

262

[ 277](group__bitarray__apis.md#gad13bb2c37d0889807e026dbac6a2872d)int [sys\_bitarray\_clear\_region](group__bitarray__apis.md#gad13bb2c37d0889807e026dbac6a2872d)([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, size\_t num\_bits,

278 size\_t offset);

279

283

284#ifdef \_\_cplusplus

285}

286#endif

287

288#endif /\* ZEPHYR\_INCLUDE\_SYS\_BITARRAY\_H\_ \*/

[sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841)

struct sys\_bitarray sys\_bitarray\_t

Bitarray structure.

**Definition** bitarray.h:48

[sys\_bitarray\_is\_region\_cleared](group__bitarray__apis.md#ga21cd833e7118f188ca3e06f8cfd13a49)

bool sys\_bitarray\_is\_region\_cleared(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset)

Test if bits in a region is all cleared.

[sys\_bitarray\_is\_region\_set](group__bitarray__apis.md#ga2aa91a9be38b11e74dacbeb2fe5e6d6d)

bool sys\_bitarray\_is\_region\_set(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset)

Test if bits in a region is all set.

[sys\_bitarray\_test\_and\_clear\_bit](group__bitarray__apis.md#ga40fa4d37f1fb2da8789f70de50c599d5)

int sys\_bitarray\_test\_and\_clear\_bit(sys\_bitarray\_t \*bitarray, size\_t bit, int \*prev\_val)

Test the bit and clear it.

[sys\_bitarray\_set\_bit](group__bitarray__apis.md#ga5fe657e79fee3e111284e4184eb6b681)

int sys\_bitarray\_set\_bit(sys\_bitarray\_t \*bitarray, size\_t bit)

Set a bit in a bit array.

[sys\_bitarray\_clear\_bit](group__bitarray__apis.md#ga795e8bf81f5717addf523cec124cde4e)

int sys\_bitarray\_clear\_bit(sys\_bitarray\_t \*bitarray, size\_t bit)

Clear a bit in a bit array.

[sys\_bitarray\_set\_region](group__bitarray__apis.md#ga94d1a547b9fe0a01d73acf4a5c4f308b)

int sys\_bitarray\_set\_region(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset)

Set all bits in a region.

[sys\_bitarray\_alloc](group__bitarray__apis.md#gac96766d9441a3b143aa386e2ac79ffd9)

int sys\_bitarray\_alloc(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t \*offset)

Allocate bits in a bit array.

[sys\_bitarray\_clear\_region](group__bitarray__apis.md#gad13bb2c37d0889807e026dbac6a2872d)

int sys\_bitarray\_clear\_region(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset)

Clear all bits in a region.

[sys\_bitarray\_test\_and\_set\_bit](group__bitarray__apis.md#gad1761b9eae8a1d9302893ce5f8591923)

int sys\_bitarray\_test\_and\_set\_bit(sys\_bitarray\_t \*bitarray, size\_t bit, int \*prev\_val)

Test the bit and set it.

[sys\_bitarray\_test\_and\_set\_region](group__bitarray__apis.md#gad18590d2ab0bf251a59996620ed6e6bf)

int sys\_bitarray\_test\_and\_set\_region(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset, bool to\_set)

Test if all bits in a region are cleared/set and set/clear them in a single atomic operation.

[sys\_bitarray\_test\_bit](group__bitarray__apis.md#gae024ace00949fe8c565081e62818449d)

int sys\_bitarray\_test\_bit(sys\_bitarray\_t \*bitarray, size\_t bit, int \*val)

Test whether a bit is set or not.

[sys\_bitarray\_free](group__bitarray__apis.md#gaf9a2c34896d3b1866a5a60f78d4166b0)

int sys\_bitarray\_free(sys\_bitarray\_t \*bitarray, size\_t num\_bits, size\_t offset)

Free bits in a bit array.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [bitarray.h](bitarray_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
