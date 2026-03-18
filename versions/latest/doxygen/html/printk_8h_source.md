---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/printk_8h_source.html
original_path: doxygen/html/printk_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

printk.h

[Go to the documentation of this file.](printk_8h.md)

1/\* printk.h - low-level debug output \*/

2

3/\*

4 \* Copyright (c) 2010-2012, 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_SYS\_PRINTK\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_PRINTK\_H\_

10

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <stddef.h>

13#include <stdarg.h>

14#include <[inttypes.h](inttypes_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

45#ifdef CONFIG\_PRINTK

46

47\_\_printf\_like(1, 2) void [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)(const char \*fmt, ...);

48\_\_printf\_like(1, 0) void [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(const char \*fmt, va\_list ap);

49

50#else

[ 51](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)static inline \_\_printf\_like(1, 2) void [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)(const char \*fmt, ...)

52{

53 ARG\_UNUSED(fmt);

54}

55

[ 56](printk_8h.md#a23609ef1acea586b44f71d32283fea23)static inline \_\_printf\_like(1, 0) void [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(const char \*fmt, va\_list ap)

57{

58 ARG\_UNUSED(fmt);

59 ARG\_UNUSED(ap);

60}

61#endif

62

63#ifdef CONFIG\_PICOLIBC

64

65#include <[stdio.h](stdio_8h.md)>

66

67#define snprintk(...) snprintf(\_\_VA\_ARGS\_\_)

68#define vsnprintk(str, size, fmt, ap) vsnprintf(str, size, fmt, ap)

69

70#else

71

[ 72](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)\_\_printf\_like(3, 4) int [snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)(char \*str, size\_t size,

73 const char \*fmt, ...);

[ 74](printk_8h.md#ae824cc3368607ee5d45f860a1389794a)\_\_printf\_like(3, 0) int [vsnprintk](printk_8h.md#ae824cc3368607ee5d45f860a1389794a)(char \*str, size\_t size,

75 const char \*fmt, va\_list ap);

76

77#endif

78

79#ifdef \_\_cplusplus

80}

81#endif

82

83#endif

[inttypes.h](inttypes_8h.md)

[snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)

int snprintk(char \*str, size\_t size, const char \*fmt,...)

[vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)

static void vprintk(const char \*fmt, va\_list ap)

**Definition** printk.h:56

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

[vsnprintk](printk_8h.md#ae824cc3368607ee5d45f860a1389794a)

int vsnprintk(char \*str, size\_t size, const char \*fmt, va\_list ap)

[stdio.h](stdio_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [printk.h](printk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
