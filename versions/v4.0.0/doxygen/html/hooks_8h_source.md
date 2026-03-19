---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hooks_8h_source.html
original_path: doxygen/html/hooks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hooks.h

[Go to the documentation of this file.](hooks_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_PLATFORM\_PLATFORM\_H\_

7#define ZEPHYR\_INCLUDE\_PLATFORM\_PLATFORM\_H\_

8

21

22

[ 29](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)void [soc\_reset\_hook](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)(void);

30

[ 38](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)void [soc\_prep\_hook](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)(void);

39

40/\*

41 \* @brief SoC hook executed before the kernel and devices are initialized.

42 \*

43 \* This hook is implemented by the SoC and can be used to perform any

44 \* SoC-specific initialization.

45 \*/

[ 46](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)void [soc\_early\_init\_hook](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)(void);

47

48/\*

49 \* @brief SoC hook executed after the kernel and devices are initialized.

50 \*

51 \* This hook is implemented by the SoC and can be used to perform any

52 \* SoC-specific initialization.

53 \*/

[ 54](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)void [soc\_late\_init\_hook](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)(void);

55

56/\*

57 \* @brief Board hook executed before the kernel starts.

58 \*

59 \* This is called before the kernel has started. This hook

60 \* is implemented by the board and can be used to perform any board-specific

61 \* initialization.

62 \*/

[ 63](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)void [board\_early\_init\_hook](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)(void);

64

65/\*

66 \* @brief Board hook executed after the kernel starts.

67

68 \* This is called after the kernel has started, but before the main function is

69 \* called. This hook is implemented by the board and can be used to perform

70 \* any board-specific initialization.

71 \*/

[ 72](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)void [board\_late\_init\_hook](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)(void);

73

74#endif

[soc\_early\_init\_hook](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)

void soc\_early\_init\_hook(void)

[board\_early\_init\_hook](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)

void board\_early\_init\_hook(void)

[soc\_late\_init\_hook](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)

void soc\_late\_init\_hook(void)

[soc\_reset\_hook](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)

void soc\_reset\_hook(void)

SoC hook executed at the beginning of the reset vector.

[soc\_prep\_hook](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)

void soc\_prep\_hook(void)

SoC hook executed after the reset vector.

[board\_late\_init\_hook](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)

void board\_late\_init\_hook(void)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [platform](dir_0ba13cd2a44aeab16da188d21efe06c8.md)
- [hooks.h](hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
