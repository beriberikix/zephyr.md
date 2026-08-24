---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/checksum_8h_source.html
original_path: doxygen/html/checksum_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

checksum.h

[Go to the documentation of this file.](checksum_8h.md)

1/\*

2 \* Copyright (c) 2025 Croxel Inc.

3 \* Copyright (c) 2025 CogniPilot Foundation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_MODEM\_UBX\_CHECKSUM\_

9#define ZEPHYR\_MODEM\_UBX\_CHECKSUM\_

10

12

[ 13](checksum_8h.md#a6d1496f64e46cba548340c9c98697758)#define UBX\_CSUM\_A(...) UBX\_CSUM\_A\_(\_\_VA\_ARGS\_\_)

14

[ 15](checksum_8h.md#a326f038f1130800d50ff861f5a7e0d9d)#define UBX\_CSUM\_A\_(...) UBX\_CSUM\_A\_I(\_\_VA\_ARGS\_\_, \

16 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

17

[ 18](checksum_8h.md#a72257fa1af8c2e6addda019b8da4b19c)#define UBX\_CSUM\_A\_I(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, \

19 a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...) \

20 ((a1) + (a2) + (a3) + (a4) + (a5) + (a6) + (a7) + (a8) + (a9) + (a10) + \

21 (a11) + (a12) + (a13) + (a14) + (a15) + (a16) + (a17) + (a18) + (a19) + (a20)) & 0xFF

22

[ 23](checksum_8h.md#a01922620d77048df31c70368a68062c0)#define UBX\_CSUM\_B(...) UBX\_CSUM\_B\_(\_\_VA\_ARGS\_\_)

24

[ 25](checksum_8h.md#a6d53729decd2998ddd2894d711397e0d)#define UBX\_CSUM\_B\_(...) UBX\_CSUM\_B\_I(NUM\_VA\_ARGS(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_, \

26 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

27

[ 28](checksum_8h.md#a98cbec44089842c71101b16342be39ac)#define UBX\_CSUM\_B\_I(len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, \

29 a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...) \

30 (((len) \* a1) + ((len - 1) \* a2) + ((len - 2) \* a3) + ((len - 3) \* a4) + \

31 ((len - 4) \* a5) + ((len - 5) \* a6) + ((len - 6) \* a7) + ((len - 7) \* a8) + \

32 ((len - 8) \* a9) + ((len - 9) \* a10) + ((len - 10) \* a11) + ((len - 11) \* a12) + \

33 ((len - 12) \* a13) + ((len - 13) \* a14) + ((len - 14) \* a15) + ((len - 15) \* a16) + \

34 ((len - 16) \* a17) + ((len - 17) \* a18) + ((len - 18) \* a19) + ((len - 19) \* a20)) & 0xFF

35

[ 36](checksum_8h.md#af30e21304d2621a9ef9d2a6edfe7332c)#define UBX\_CSUM(...) UBX\_CSUM\_A(\_\_VA\_ARGS\_\_), UBX\_CSUM\_B(\_\_VA\_ARGS\_\_)

37

38#endif /\* ZEPHYR\_MODEM\_UBX\_CHECKSUM\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [checksum.h](checksum_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
