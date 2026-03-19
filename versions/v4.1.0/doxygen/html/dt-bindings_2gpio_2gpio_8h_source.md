---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-bindings_2gpio_2gpio_8h_source.html
original_path: doxygen/html/dt-bindings_2gpio_2gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h

[Go to the documentation of this file.](dt-bindings_2gpio_2gpio_8h.md)

1/\*

2 \* Copyright (c) 2019 Piotr Mienkowski

3 \* Copyright (c) 2018 Linaro Limited

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_GPIO\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_GPIO\_H\_

9

16

[ 18](group__gpio__interface.md#ga335bf7efee07e03961ab91a86295897a)#define GPIO\_DT\_FLAGS\_MASK 0x3F

19

24

[ 26](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)#define GPIO\_ACTIVE\_LOW (1 << 0)

[ 28](group__gpio__interface.md#gad93badd2828d065e7fd14cf40dd05039)#define GPIO\_ACTIVE\_HIGH (0 << 0)

29

31

36

38

39/\* Configures GPIO output in single-ended mode (open drain or open source). \*/

40#define GPIO\_SINGLE\_ENDED (1 << 1)

41/\* Configures GPIO output in push-pull mode \*/

42#define GPIO\_PUSH\_PULL (0 << 1)

43

44/\* Indicates single ended open drain mode (wired AND). \*/

45#define GPIO\_LINE\_OPEN\_DRAIN (1 << 2)

46/\* Indicates single ended open source mode (wired OR). \*/

47#define GPIO\_LINE\_OPEN\_SOURCE (0 << 2)

48

50

[ 57](group__gpio__interface.md#ga72b7ac5b3613d972b88268bee9068e35)#define GPIO\_OPEN\_DRAIN (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_DRAIN)

[ 65](group__gpio__interface.md#ga5ace024873272a3f6727fc186afa0320)#define GPIO\_OPEN\_SOURCE (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_SOURCE)

66

68

73

[ 75](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970)#define GPIO\_PULL\_UP (1 << 4)

76

[ 78](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)#define GPIO\_PULL\_DOWN (1 << 5)

79

81

[ 85](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96)#define GPIO\_INT\_WAKEUP (1 << 6)

86

87/\* Note: Bits 15 downto 8 are reserved for SoC specific flags. \*/

88

92

93#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [gpio.h](dt-bindings_2gpio_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
