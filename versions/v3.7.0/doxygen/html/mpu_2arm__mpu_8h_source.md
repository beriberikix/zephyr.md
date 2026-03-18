---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mpu_2arm__mpu_8h_source.html
original_path: doxygen/html/mpu_2arm__mpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu.h

[Go to the documentation of this file.](mpu_2arm__mpu_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_ARM\_MPU\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_ARM\_MPU\_H\_

8

9#if defined(CONFIG\_CPU\_CORTEX\_M0PLUS) || \

10 defined(CONFIG\_CPU\_CORTEX\_M3) || \

11 defined(CONFIG\_CPU\_CORTEX\_M4) || \

12 defined(CONFIG\_CPU\_CORTEX\_M7) || \

13 defined(CONFIG\_ARMV7\_R)

14#include <[zephyr/arch/arm/mpu/arm\_mpu\_v7m.h](arm__mpu__v7m_8h.md)>

15#elif defined(CONFIG\_CPU\_CORTEX\_M23) || \

16 defined(CONFIG\_CPU\_CORTEX\_M33) || \

17 defined(CONFIG\_CPU\_CORTEX\_M55) || \

18 defined(CONFIG\_CPU\_CORTEX\_M85) || \

19 defined(CONFIG\_AARCH32\_ARMV8\_R)

20#include <[zephyr/arch/arm/mpu/arm\_mpu\_v8.h](arm__mpu__v8_8h.md)>

21#else

22#error "Unsupported ARM CPU"

23#endif

24

25#ifndef \_ASMLANGUAGE

26

27/\* Region definition data structure \*/

[ 28](structarm__mpu__region.md)struct [arm\_mpu\_region](structarm__mpu__region.md) {

29 /\* Region Base Address \*/

[ 30](structarm__mpu__region.md#a1639ea642561dc45d33774817e6a67b6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base](structarm__mpu__region.md#a1639ea642561dc45d33774817e6a67b6);

31 /\* Region Name \*/

[ 32](structarm__mpu__region.md#a18f2dc7696fd55c1fdcce57ae16b46e4) const char \*[name](structarm__mpu__region.md#a18f2dc7696fd55c1fdcce57ae16b46e4);

33#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R)

34 /\* Region Size \*/

35 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size;

36#endif

37 /\* Region Attributes \*/

[ 38](structarm__mpu__region.md#aa94b10ac6e6780c154c25cee91e7921e) [arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6) [attr](structarm__mpu__region.md#aa94b10ac6e6780c154c25cee91e7921e);

39};

40

41/\* MPU configuration data structure \*/

[ 42](structarm__mpu__config.md)struct [arm\_mpu\_config](structarm__mpu__config.md) {

43 /\* Number of regions \*/

[ 44](structarm__mpu__config.md#a13216be94d5dfea0e4eb069f24400fdc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structarm__mpu__config.md#a13216be94d5dfea0e4eb069f24400fdc);

45 /\* Regions \*/

[ 46](structarm__mpu__config.md#ac25f09decb52172736a1ab1e0327a6bc) const struct [arm\_mpu\_region](structarm__mpu__region.md) \*[mpu\_regions](structarm__mpu__config.md#ac25f09decb52172736a1ab1e0327a6bc);

47};

48

49#if defined(CONFIG\_ARMV7\_R)

50#define MPU\_REGION\_ENTRY(\_name, \_base, \_size, \_attr) \

51 {\

52 .name = \_name, \

53 .base = \_base, \

54 .size = \_size, \

55 .attr = \_attr, \

56 }

57#else

[ 58](mpu_2arm__mpu_8h.md#ab0bd4273967fcfcc4c3929157d1775e1)#define MPU\_REGION\_ENTRY(\_name, \_base, \_attr) \

59 {\

60 .name = \_name, \

61 .base = \_base, \

62 .attr = \_attr, \

63 }

64#endif

65

66/\* Reference to the MPU configuration.

67 \*

68 \* This struct is defined and populated for each SoC (in the SoC definition),

69 \* and holds the build-time configuration information for the fixed MPU

70 \* regions enabled during kernel initialization. Dynamic MPU regions (e.g.

71 \* for Thread Stack, Stack Guards, etc.) are programmed during runtime, thus,

72 \* not kept here.

73 \*/

74extern const struct [arm\_mpu\_config](structarm__mpu__config.md) [mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1);

75

76#endif /\* \_ASMLANGUAGE \*/

77

78#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_ARM\_MPU\_H\_ \*/

[mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1)

struct arc\_mpu\_config mpu\_config

[arm\_mpu\_v7m.h](arm__mpu__v7m_8h.md)

[arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)

struct arm\_mpu\_region\_attr arm\_mpu\_region\_attr\_t

**Definition** arm\_mpu\_v7m.h:157

[arm\_mpu\_v8.h](arm__mpu__v8_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arm\_mpu\_config](structarm__mpu__config.md)

**Definition** arm\_mpu.h:42

[arm\_mpu\_config::num\_regions](structarm__mpu__config.md#a13216be94d5dfea0e4eb069f24400fdc)

uint32\_t num\_regions

**Definition** arm\_mpu.h:44

[arm\_mpu\_config::mpu\_regions](structarm__mpu__config.md#ac25f09decb52172736a1ab1e0327a6bc)

const struct arm\_mpu\_region \* mpu\_regions

**Definition** arm\_mpu.h:46

[arm\_mpu\_region](structarm__mpu__region.md)

**Definition** arm\_mpu.h:28

[arm\_mpu\_region::base](structarm__mpu__region.md#a1639ea642561dc45d33774817e6a67b6)

uint32\_t base

**Definition** arm\_mpu.h:30

[arm\_mpu\_region::name](structarm__mpu__region.md#a18f2dc7696fd55c1fdcce57ae16b46e4)

const char \* name

**Definition** arm\_mpu.h:32

[arm\_mpu\_region::attr](structarm__mpu__region.md#aa94b10ac6e6780c154c25cee91e7921e)

arm\_mpu\_region\_attr\_t attr

**Definition** arm\_mpu.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu.h](mpu_2arm__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
