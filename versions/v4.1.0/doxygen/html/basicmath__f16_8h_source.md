---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/basicmath__f16_8h_source.html
original_path: doxygen/html/basicmath__f16_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

basicmath\_f16.h

[Go to the documentation of this file.](basicmath__f16_8h.md)

1/\* Copyright (C) 2010-2021 ARM Limited or its affiliates. All rights reserved.

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

10

11#ifndef ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_F16\_H\_

12#define ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_F16\_H\_

13

14#ifndef CONFIG\_FP16

15#error "Cannot use float16 DSP functionality without CONFIG\_FP16 enabled"

16#endif /\* CONFIG\_FP16 \*/

17

18#include <[zephyr/dsp/dsp.h](dsp_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 32](group__math__dsp__basic__mult.md#ga795bc69852005a0e547c3f2794c5397a)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_mult\_f16](group__math__dsp__basic__mult.md#ga795bc69852005a0e547c3f2794c5397a)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst,

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

34

[ 43](group__math__dsp__basic__add.md#ga3ad2849433440c2d1175cd6f18e6eade)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_add\_f16](group__math__dsp__basic__add.md#ga3ad2849433440c2d1175cd6f18e6eade)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst,

44 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

45

[ 54](group__math__dsp__basic__sub.md#ga500f6403d4382bc797231d7962275230)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_sub\_f16](group__math__dsp__basic__sub.md#ga500f6403d4382bc797231d7962275230)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst,

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

56

[ 65](group__math__dsp__basic__scale.md#ga26c461531e82511c18902ba908f36230)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_scale\_f16](group__math__dsp__basic__scale.md#ga26c461531e82511c18902ba908f36230)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) scale, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst,

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

67

[ 75](group__math__dsp__basic__abs.md#gaf178acd8862a2928a65e98f4fef1380b)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_abs\_f16](group__math__dsp__basic__abs.md#gaf178acd8862a2928a65e98f4fef1380b)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

76

[ 85](group__math__dsp__basic__dot.md#ga11af65d379fa201a04408544ddca8354)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_dot\_prod\_f16](group__math__dsp__basic__dot.md#ga11af65d379fa201a04408544ddca8354)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b,

86 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*result);

87

[ 96](group__math__dsp__basic__offset.md#ga60d4ef0543308773e651a0f40b3b0fe1)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_offset\_f16](group__math__dsp__basic__offset.md#ga60d4ef0543308773e651a0f40b3b0fe1)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) offset, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst,

97 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

98

[ 106](group__math__dsp__basic__negate.md#ga7aacb425c3dfb2c5d8664a7cf4031c3b)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_negate\_f16](group__math__dsp__basic__negate.md#ga7aacb425c3dfb2c5d8664a7cf4031c3b)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

107

[ 117](group__math__dsp__basic__clip.md#ga4edd7ba5b9c3791d7857a2c7d1541cab)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_clip\_f16](group__math__dsp__basic__clip.md#ga4edd7ba5b9c3791d7857a2c7d1541cab)(const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) low,

118 [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples);

119

120#ifdef \_\_cplusplus

121}

122#endif

123

124#endif /\* ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_F16\_H\_ \*/

[dsp.h](dsp_8h.md)

Public APIs for Digital Signal Processing (DSP) math.

[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7)

#define DSP\_FUNC\_SCOPE

**Definition** dsp.h:17

[zdsp\_abs\_f16](group__math__dsp__basic__abs.md#gaf178acd8862a2928a65e98f4fef1380b)

DSP\_FUNC\_SCOPE void zdsp\_abs\_f16(const float16\_t \*src, float16\_t \*dst, uint32\_t block\_size)

Floating-point vector absolute value.

[zdsp\_add\_f16](group__math__dsp__basic__add.md#ga3ad2849433440c2d1175cd6f18e6eade)

DSP\_FUNC\_SCOPE void zdsp\_add\_f16(const float16\_t \*src\_a, const float16\_t \*src\_b, float16\_t \*dst, uint32\_t block\_size)

Floating-point vector addition.

[zdsp\_clip\_f16](group__math__dsp__basic__clip.md#ga4edd7ba5b9c3791d7857a2c7d1541cab)

DSP\_FUNC\_SCOPE void zdsp\_clip\_f16(const float16\_t \*src, float16\_t \*dst, float16\_t low, float16\_t high, uint32\_t num\_samples)

Elementwise floating-point clipping.

[zdsp\_dot\_prod\_f16](group__math__dsp__basic__dot.md#ga11af65d379fa201a04408544ddca8354)

DSP\_FUNC\_SCOPE void zdsp\_dot\_prod\_f16(const float16\_t \*src\_a, const float16\_t \*src\_b, uint32\_t block\_size, float16\_t \*result)

Dot product of floating-point vectors.

[zdsp\_mult\_f16](group__math__dsp__basic__mult.md#ga795bc69852005a0e547c3f2794c5397a)

DSP\_FUNC\_SCOPE void zdsp\_mult\_f16(const float16\_t \*src\_a, const float16\_t \*src\_b, float16\_t \*dst, uint32\_t block\_size)

Floating-point vector multiplication.

[zdsp\_negate\_f16](group__math__dsp__basic__negate.md#ga7aacb425c3dfb2c5d8664a7cf4031c3b)

DSP\_FUNC\_SCOPE void zdsp\_negate\_f16(const float16\_t \*src, float16\_t \*dst, uint32\_t block\_size)

Negates the elements of a floating-point vector.

[zdsp\_offset\_f16](group__math__dsp__basic__offset.md#ga60d4ef0543308773e651a0f40b3b0fe1)

DSP\_FUNC\_SCOPE void zdsp\_offset\_f16(const float16\_t \*src, float16\_t offset, float16\_t \*dst, uint32\_t block\_size)

Adds a constant offset to a floating-point vector.

[zdsp\_scale\_f16](group__math__dsp__basic__scale.md#ga26c461531e82511c18902ba908f36230)

DSP\_FUNC\_SCOPE void zdsp\_scale\_f16(const float16\_t \*src, float16\_t scale, float16\_t \*dst, uint32\_t block\_size)

Multiplies a floating-point vector by a scalar.

[zdsp\_sub\_f16](group__math__dsp__basic__sub.md#ga500f6403d4382bc797231d7962275230)

DSP\_FUNC\_SCOPE void zdsp\_sub\_f16(const float16\_t \*src\_a, const float16\_t \*src\_b, float16\_t \*dst, uint32\_t block\_size)

Floating-point vector subtraction.

[float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f)

\_\_fp16 float16\_t

16-bit floating point type definition.

**Definition** types.h:48

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [basicmath\_f16.h](basicmath__f16_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
