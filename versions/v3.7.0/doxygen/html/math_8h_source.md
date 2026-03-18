---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/math_8h_source.html
original_path: doxygen/html/math_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

math.h

[Go to the documentation of this file.](math_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_MATH\_H\_

8#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_MATH\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#if !defined(FLT\_EVAL\_METHOD) && defined(\_\_FLT\_EVAL\_METHOD\_\_)

15#define FLT\_EVAL\_METHOD \_\_FLT\_EVAL\_METHOD\_\_

16#endif

17

18#if defined FLT\_EVAL\_METHOD

19 #if FLT\_EVAL\_METHOD == 0

20 typedef float [float\_t](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a);

21 typedef double [double\_t](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd);

22 #elif FLT\_EVAL\_METHOD == 1

23 typedef double [float\_t](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a);

24 typedef double [double\_t](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd);

25 #elif FLT\_EVAL\_METHOD == 2

26 typedef long double [float\_t](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a);

27 typedef long double [double\_t](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd);

28 #else

29 /\* Implementation-defined. Assume float\_t and double\_t have

30 \* already been defined \*/

31 #endif

32#else

[ 33](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a) typedef float [float\_t](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a);

[ 34](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd) typedef double [double\_t](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd);

35#endif

36

37/\* Useful constants. \*/

[ 38](math_8h.md#a5e9e29217f6ec61105a4520ec5942225)#define MAXFLOAT 3.40282347e+38F

39

[ 40](math_8h.md#a9bf5d952c5c93c70f9e66c9794d406c9)#define M\_E 2.7182818284590452354

[ 41](math_8h.md#ac5c747ee5bcbe892875672a0b9d8171c)#define M\_LOG2E 1.4426950408889634074

[ 42](math_8h.md#a9ed2b5582226f3896424ff6d2a3ebb14)#define M\_LOG10E 0.43429448190325182765

[ 43](math_8h.md#a92428112a5d24721208748774a4f23e6)#define M\_LN2 0.693147180559945309417

[ 44](math_8h.md#a0a53871497a155afe91424c28a8ec3c4)#define M\_LN10 2.30258509299404568402

[ 45](math_8h.md#ae71449b1cc6e6250b91f539153a7a0d3)#define M\_PI 3.14159265358979323846

[ 46](math_8h.md#a958e4508ed28ee5cc04249144312c15f)#define M\_PI\_2 1.57079632679489661923

[ 47](math_8h.md#aeb24420b096a677f3a2dc5a72b36bf22)#define M\_PI\_4 0.78539816339744830962

[ 48](math_8h.md#a08dfac3cca9601a02fc88356cc078e1d)#define M\_1\_PI 0.31830988618379067154

[ 49](math_8h.md#a97f6d6514d3d3dd50c3a2a6d622673db)#define M\_2\_PI 0.63661977236758134308

[ 50](math_8h.md#a631ff334c4a1a6db2e8a7ff4acbe48a5)#define M\_2\_SQRTPI 1.12837916709551257390

[ 51](math_8h.md#a66b3ab30f1332874326ed93969e496e0)#define M\_SQRT2 1.41421356237309504880

[ 52](math_8h.md#acdbb2c2f9429f08916f03c8786d2d2d7)#define M\_SQRT1\_2 0.70710678118654752440

53

[ 54](math_8h.md#a769abd043ac3336a53318e327f2137c2)float [sqrtf](math_8h.md#a769abd043ac3336a53318e327f2137c2)(float square);

[ 55](math_8h.md#ae0617f6dc83a7c2767e0766f5b3df203)double [sqrt](math_8h.md#ae0617f6dc83a7c2767e0766f5b3df203)(double square);

56

57#ifdef \_\_cplusplus

58}

59#endif

60

61#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_MATH\_H\_ \*/

[float\_t](math_8h.md#a3ded656bbe9849ad9fa2b28530390f0a)

float float\_t

**Definition** math.h:33

[sqrtf](math_8h.md#a769abd043ac3336a53318e327f2137c2)

float sqrtf(float square)

[double\_t](math_8h.md#ac340fde9f4743ef7a9398b79d7bea8bd)

double double\_t

**Definition** math.h:34

[sqrt](math_8h.md#ae0617f6dc83a7c2767e0766f5b3df203)

double sqrt(double square)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [math.h](math_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
