---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/armv8__timer_8h_source.html
original_path: doxygen/html/armv8__timer_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

armv8\_timer.h

[Go to the documentation of this file.](armv8__timer_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \* Copyright (c) 2022 IoT.bzh

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_ARMV8\_TIMER\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_ARMV8\_TIMER\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/drivers/timer/arm\_arch\_timer.h](arm__arch__timer_8h.md)>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](armv8__timer_8h.md#a6740222458f89442f50b688bfa69797f)#define ARM\_ARCH\_TIMER\_IRQ ARM\_TIMER\_VIRTUAL\_IRQ

[ 21](armv8__timer_8h.md#a319716e35b4e65c8480c0b90624a7899)#define ARM\_ARCH\_TIMER\_PRIO ARM\_TIMER\_VIRTUAL\_PRIO

[ 22](armv8__timer_8h.md#a2ab15e3403580f8986b7c7391f0fbbd2)#define ARM\_ARCH\_TIMER\_FLAGS ARM\_TIMER\_VIRTUAL\_FLAGS

23

[ 24](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_init](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)(void)

25{

26}

27

[ 28](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_compare](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

29{

30 [write\_cntv\_cval](cortex__a__r_2lib__helpers_8h.md#a8929efdf8cc97e99983a4e3b3a32bf4b)(val);

31}

32

[ 33](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_enable](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)(unsigned char enable)

34{

35 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cntv\_ctl;

36

37 cntv\_ctl = [read\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a260cf183f5aa1745e5439626e9480f48)();

38

39 if (enable) {

40 cntv\_ctl |= [CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8);

41 } else {

42 cntv\_ctl &= [~CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8);

43 }

44

45 [write\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a34fb23d53a92012ecd4c6f6a776983b4)(cntv\_ctl);

46}

47

[ 48](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_irq\_mask](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)(bool mask)

49{

50 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cntv\_ctl;

51

52 cntv\_ctl = [read\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a260cf183f5aa1745e5439626e9480f48)();

53

54 if (mask) {

55 cntv\_ctl |= [CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb);

56 } else {

57 cntv\_ctl &= [~CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb);

58 }

59

60 [write\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a34fb23d53a92012ecd4c6f6a776983b4)(cntv\_ctl);

61}

62

[ 63](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arm\_arch\_timer\_count](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)(void)

64{

65 return [read\_cntvct](cortex__a__r_2lib__helpers_8h.md#aadc1c2db15fb0074e0acfb554cb26d8b)();

66}

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72#endif /\* \_ASMLANGUAGE \*/

73

74#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_ARMV8\_TIMER\_H\_ \*/

[CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8)

#define CNTV\_CTL\_ENABLE\_BIT

**Definition** cpu.h:78

[CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb)

#define CNTV\_CTL\_IMASK\_BIT

**Definition** cpu.h:79

[arm\_arch\_timer.h](arm__arch__timer_8h.md)

[arm\_arch\_timer\_count](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)

static ALWAYS\_INLINE uint64\_t arm\_arch\_timer\_count(void)

**Definition** armv8\_timer.h:63

[arm\_arch\_timer\_set\_irq\_mask](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)

static ALWAYS\_INLINE void arm\_arch\_timer\_set\_irq\_mask(bool mask)

**Definition** armv8\_timer.h:48

[arm\_arch\_timer\_set\_compare](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)

static ALWAYS\_INLINE void arm\_arch\_timer\_set\_compare(uint64\_t val)

**Definition** armv8\_timer.h:28

[arm\_arch\_timer\_enable](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)

static ALWAYS\_INLINE void arm\_arch\_timer\_enable(unsigned char enable)

**Definition** armv8\_timer.h:33

[arm\_arch\_timer\_init](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)

static ALWAYS\_INLINE void arm\_arch\_timer\_init(void)

**Definition** armv8\_timer.h:24

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[read\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a260cf183f5aa1745e5439626e9480f48)

static ALWAYS\_INLINE uint32\_t read\_cntv\_ctl(void)

**Definition** lib\_helpers.h:73

[write\_cntv\_ctl](cortex__a__r_2lib__helpers_8h.md#a34fb23d53a92012ecd4c6f6a776983b4)

static ALWAYS\_INLINE void write\_cntv\_ctl(uint32\_t val)

**Definition** lib\_helpers.h:73

[write\_cntv\_cval](cortex__a__r_2lib__helpers_8h.md#a8929efdf8cc97e99983a4e3b3a32bf4b)

static ALWAYS\_INLINE void write\_cntv\_cval(uint64\_t val)

**Definition** lib\_helpers.h:78

[read\_cntvct](cortex__a__r_2lib__helpers_8h.md#aadc1c2db15fb0074e0acfb554cb26d8b)

static ALWAYS\_INLINE uint64\_t read\_cntvct(void)

**Definition** lib\_helpers.h:77

[types.h](include_2zephyr_2types_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [armv8\_timer.h](armv8__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
