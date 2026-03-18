---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pm__s2ram_8h_source.html
original_path: doxygen/html/pm__s2ram_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_s2ram.h

[Go to the documentation of this file.](pm__s2ram_8h.md)

1/\*

2 \* Copyright (c) 2022, Carlo Caione <ccaione@baylibre.com>

3 \*/

4

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_PM\_S2RAM\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_PM\_S2RAM\_H\_

16

17#ifdef \_ASMLANGUAGE

18GTEXT([arch\_pm\_s2ram\_suspend](group__pm__s2ram.md#ga6b82cf263c595b0d5cb353759000615c));

19#else

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 39](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53)typedef int (\*[pm\_s2ram\_system\_off\_fn\_t](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53))(void);

40

[ 58](group__pm__s2ram.md#ga6b82cf263c595b0d5cb353759000615c)int [arch\_pm\_s2ram\_suspend](group__pm__s2ram.md#ga6b82cf263c595b0d5cb353759000615c)([pm\_s2ram\_system\_off\_fn\_t](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53) system\_off);

59

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif /\* \_ASMLANGUAGE \*/

69

70#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_PM\_S2RAM\_H\_ \*/

[pm\_s2ram\_system\_off\_fn\_t](group__pm__s2ram.md#ga61b569a4b9053443c9b82b0ea1bfae53)

int(\* pm\_s2ram\_system\_off\_fn\_t)(void)

System off function.

**Definition** pm\_s2ram.h:39

[arch\_pm\_s2ram\_suspend](group__pm__s2ram.md#ga6b82cf263c595b0d5cb353759000615c)

int arch\_pm\_s2ram\_suspend(pm\_s2ram\_system\_off\_fn\_t system\_off)

Save CPU context on suspend.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [pm\_s2ram.h](pm__s2ram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
