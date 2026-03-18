---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arc__core__mpu_8h_source.html
original_path: doxygen/html/arc__core__mpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_core\_mpu.h

[Go to the documentation of this file.](arc__core__mpu_8h.md)

1/\*

2 \* Copyright (c) 2017 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MPU\_ARC\_CORE\_MPU\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MPU\_ARC\_CORE\_MPU\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13/\*

14 \* The defines below represent the region types. The MPU driver is responsible

15 \* to allocate the region accordingly to the type and set the correct

16 \* attributes.

17 \*

18 \* Each MPU is different and has a different set of attributes, hence instead

19 \* of having the attributes at this level the arc\_mpu\_core defines the intent

20 \* types.

21 \* An intent type (i.e. THREAD\_STACK\_GUARD) can correspond to a different set

22 \* of operations and attributes for each MPU and it is responsibility of the

23 \* MPU driver to select the correct ones.

24 \*

25 \* The intent based configuration can't fail hence at this level no error

26 \* is returned by the configuration functions.

27 \* If one of the operations corresponding to an intent fails the error has to

28 \* be managed inside the MPU driver and not escalated.

29 \*/

30/\* Thread Region Intent Type \*/

[ 31](arc__core__mpu_8h.md#a22720cafd5b56a589fdf78e9fde34df5)#define THREAD\_STACK\_USER\_REGION 0x0

[ 32](arc__core__mpu_8h.md#aa100568c6cd354bf10d8567342d7c015)#define THREAD\_STACK\_REGION 0x1

[ 33](arc__core__mpu_8h.md#a6d410aa5ef2d4566c6169b2be511469f)#define THREAD\_APP\_DATA\_REGION 0x2

[ 34](arc__core__mpu_8h.md#abfa3cdf9032f9ae166772cc135777857)#define THREAD\_STACK\_GUARD\_REGION 0x3

[ 35](arc__core__mpu_8h.md#a7ad5bda29d5cd51209673c0b7650c0d0)#define THREAD\_DOMAIN\_PARTITION\_REGION 0x4

36

37#if defined(CONFIG\_ARC\_CORE\_MPU)

38/\* ARC Core MPU Driver API \*/

39

40/\*

41 \* This API has to be implemented by all the MPU drivers that have

42 \* ARC\_CORE\_MPU support.

43 \*/

44

48void arc\_core\_mpu\_enable(void);

49

53void arc\_core\_mpu\_disable(void);

54

60void arc\_core\_mpu\_configure\_thread(struct [k\_thread](structk__thread.md) \*thread);

61

62/\*

63 \* Before configure the MPU regions, MPU should be disabled

64 \*/

70void arc\_core\_mpu\_default([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) region\_attr);

71

80int arc\_core\_mpu\_region([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) base, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

81 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) region\_attr);

82

83#endif /\* CONFIG\_ARC\_CORE\_MPU \*/

84

85#if defined(CONFIG\_USERSPACE)

[ 86](arc__core__mpu_8h.md#a59ab30984101e12346194700ac788c02)void [arc\_core\_mpu\_configure\_mem\_domain](arc__core__mpu_8h.md#a59ab30984101e12346194700ac788c02)(struct [k\_thread](structk__thread.md) \*thread);

[ 87](arc__core__mpu_8h.md#a65c60aedd91088211a87668e21710792)void [arc\_core\_mpu\_remove\_mem\_domain](arc__core__mpu_8h.md#a65c60aedd91088211a87668e21710792)(struct [k\_mem\_domain](structk__mem__domain.md) \*mem\_domain);

[ 88](arc__core__mpu_8h.md#a336c96a063f41feb6e40553da7d24b8d)void [arc\_core\_mpu\_remove\_mem\_partition](arc__core__mpu_8h.md#a336c96a063f41feb6e40553da7d24b8d)(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

89 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) partition\_id);

[ 90](arc__core__mpu_8h.md#ac5545b4f32734d39d0ea595ec946c798)int [arc\_core\_mpu\_get\_max\_domain\_partition\_regions](arc__core__mpu_8h.md#ac5545b4f32734d39d0ea595ec946c798)(void);

[ 91](arc__core__mpu_8h.md#ac51c1ffa76948c631893ce9a2e61aa55)int [arc\_core\_mpu\_buffer\_validate](arc__core__mpu_8h.md#ac51c1ffa76948c631893ce9a2e61aa55)(const void \*addr, size\_t size, int write);

92

93#endif

94

[ 95](arc__core__mpu_8h.md#a3f143241fb106da87db9cf78539ff802)void [configure\_mpu\_thread](arc__core__mpu_8h.md#a3f143241fb106da87db9cf78539ff802)(struct [k\_thread](structk__thread.md) \*thread);

96

97#ifdef \_\_cplusplus

98}

99#endif

100

101#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MPU\_ARC\_CORE\_MPU\_H\_ \*/

[arc\_core\_mpu\_remove\_mem\_partition](arc__core__mpu_8h.md#a336c96a063f41feb6e40553da7d24b8d)

void arc\_core\_mpu\_remove\_mem\_partition(struct k\_mem\_domain \*domain, uint32\_t partition\_id)

[configure\_mpu\_thread](arc__core__mpu_8h.md#a3f143241fb106da87db9cf78539ff802)

void configure\_mpu\_thread(struct k\_thread \*thread)

[arc\_core\_mpu\_configure\_mem\_domain](arc__core__mpu_8h.md#a59ab30984101e12346194700ac788c02)

void arc\_core\_mpu\_configure\_mem\_domain(struct k\_thread \*thread)

[arc\_core\_mpu\_remove\_mem\_domain](arc__core__mpu_8h.md#a65c60aedd91088211a87668e21710792)

void arc\_core\_mpu\_remove\_mem\_domain(struct k\_mem\_domain \*mem\_domain)

[arc\_core\_mpu\_buffer\_validate](arc__core__mpu_8h.md#ac51c1ffa76948c631893ce9a2e61aa55)

int arc\_core\_mpu\_buffer\_validate(const void \*addr, size\_t size, int write)

[arc\_core\_mpu\_get\_max\_domain\_partition\_regions](arc__core__mpu_8h.md#ac5545b4f32734d39d0ea595ec946c798)

int arc\_core\_mpu\_get\_max\_domain\_partition\_regions(void)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [mpu](dir_c51b2f0fffc5b62554252c09f16a5032.md)
- [arc\_core\_mpu.h](arc__core__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
