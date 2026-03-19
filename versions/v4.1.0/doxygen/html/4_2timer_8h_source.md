---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/4_2timer_8h_source.html
original_path: doxygen/html/4_2timer_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timer.h

[Go to the documentation of this file.](4_2timer_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_TIMER\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_TIMER\_H\_

9

10#ifndef \_ASMLANGUAGE

11

12#include <[limits.h](limits_8h.md)>

13

14#include <[zephyr/drivers/timer/arm\_arch\_timer.h](arm__arch__timer_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[limits.h](limits_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 22](4_2timer_8h.md#a6740222458f89442f50b688bfa69797f)#define ARM\_ARCH\_TIMER\_IRQ ARM\_TIMER\_VIRTUAL\_IRQ

[ 23](4_2timer_8h.md#a319716e35b4e65c8480c0b90624a7899)#define ARM\_ARCH\_TIMER\_PRIO ARM\_TIMER\_VIRTUAL\_PRIO

[ 24](4_2timer_8h.md#a2ab15e3403580f8986b7c7391f0fbbd2)#define ARM\_ARCH\_TIMER\_FLAGS ARM\_TIMER\_VIRTUAL\_FLAGS

25

[ 26](4_2timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_init](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)(void)

27{

28#ifdef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

29 extern int z\_clock\_hw\_cycles\_per\_sec;

30 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cntfrq\_el0 = [read\_cntfrq\_el0](4_2lib__helpers_8h.md#a258a47c46f638d2d41b30cff783ac247)();

31

32 \_\_ASSERT(cntfrq\_el0 < [INT\_MAX](limits_8h.md#a9ec306f36d50c7375e74f0d1c55a3a67), "cntfrq\_el0 cannot fit in system 'int'");

33 z\_clock\_hw\_cycles\_per\_sec = (int) cntfrq\_el0;

34#endif

35}

36

[ 37](4_2timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_compare](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

38{

39 [write\_cntv\_cval\_el0](4_2lib__helpers_8h.md#afad9883e3416574fa1ddaddaf84b2c25)(val);

40}

41

[ 42](4_2timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_enable](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)(unsigned char enable)

43{

44 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cntv\_ctl;

45

46 cntv\_ctl = [read\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#ab8455d86f57ccec61fa1ad6784c573f7)();

47

48 if (enable) {

49 cntv\_ctl |= [CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8);

50 } else {

51 cntv\_ctl &= [~CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8);

52 }

53

54 [write\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#adf8ccef22b4bfa2378d27bbbbc13ad6e)(cntv\_ctl);

55}

56

[ 57](4_2timer_8h.md#a5969eb25741240dd0030acb92018038c)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_irq\_mask](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)(bool mask)

58{

59 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cntv\_ctl;

60

61 cntv\_ctl = [read\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#ab8455d86f57ccec61fa1ad6784c573f7)();

62

63 if (mask) {

64 cntv\_ctl |= [CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb);

65 } else {

66 cntv\_ctl &= [~CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb);

67 }

68

69 [write\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#adf8ccef22b4bfa2378d27bbbbc13ad6e)(cntv\_ctl);

70}

71

[ 72](4_2timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arm\_arch\_timer\_count](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)(void)

73{

74 return [read\_cntvct\_el0](4_2lib__helpers_8h.md#a0e7c74f6816ea2107dca43a9d32de547)();

75}

76

77#ifdef \_\_cplusplus

78}

79#endif

80

81#endif /\* \_ASMLANGUAGE \*/

82

83#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_TIMER\_H\_ \*/

[read\_cntvct\_el0](4_2lib__helpers_8h.md#a0e7c74f6816ea2107dca43a9d32de547)

static ALWAYS\_INLINE uint64\_t read\_cntvct\_el0(void)

**Definition** lib\_helpers.h:65

[read\_cntfrq\_el0](4_2lib__helpers_8h.md#a258a47c46f638d2d41b30cff783ac247)

static ALWAYS\_INLINE uint64\_t read\_cntfrq\_el0(void)

**Definition** lib\_helpers.h:59

[read\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#ab8455d86f57ccec61fa1ad6784c573f7)

static ALWAYS\_INLINE uint64\_t read\_cntv\_ctl\_el0(void)

**Definition** lib\_helpers.h:63

[write\_cntv\_ctl\_el0](4_2lib__helpers_8h.md#adf8ccef22b4bfa2378d27bbbbc13ad6e)

static ALWAYS\_INLINE void write\_cntv\_ctl\_el0(uint64\_t val)

**Definition** lib\_helpers.h:63

[write\_cntv\_cval\_el0](4_2lib__helpers_8h.md#afad9883e3416574fa1ddaddaf84b2c25)

static ALWAYS\_INLINE void write\_cntv\_cval\_el0(uint64\_t val)

**Definition** lib\_helpers.h:64

[CNTV\_CTL\_ENABLE\_BIT](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8)

#define CNTV\_CTL\_ENABLE\_BIT

**Definition** cpu.h:85

[CNTV\_CTL\_IMASK\_BIT](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb)

#define CNTV\_CTL\_IMASK\_BIT

**Definition** cpu.h:86

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

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[limits.h](limits_8h.md)

[INT\_MAX](limits_8h.md#a9ec306f36d50c7375e74f0d1c55a3a67)

#define INT\_MAX

**Definition** limits.h:39

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [timer.h](4_2timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
