---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dsp_2utils_8h_source.html
original_path: doxygen/html/dsp_2utils_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utils.h

[Go to the documentation of this file.](dsp_2utils_8h.md)

1/\*

2 \* Copyright (C) 2024 OWL Services LLC. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef INCLUDE\_ZEPHYR\_DSP\_UTILS\_H\_

14#define INCLUDE\_ZEPHYR\_DSP\_UTILS\_H\_

15

16#include <[stdint.h](stdint_8h.md)>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18#include <[zephyr/dsp/dsp.h](dsp_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

28

38

46#define Z\_SHIFT\_Q7\_TO\_F32(src, m) ((float32\_t)(((src << m)) / (float32\_t)(1U << 7)))

47

55#define Z\_SHIFT\_Q15\_TO\_F32(src, m) ((float32\_t)((src << m) / (float32\_t)(1U << 15)))

56

64#define Z\_SHIFT\_Q31\_TO\_F32(src, m) ((float32\_t)(((int64\_t)src) << m) / (float32\_t)(1U << 31))

65

73#define Z\_SHIFT\_Q7\_TO\_F64(src, m) (((float64\_t)(src << m)) / (1U << 7))

74

82#define Z\_SHIFT\_Q15\_TO\_F64(src, m) (((float64\_t)(src << m)) / (1UL << 15))

83

91#define Z\_SHIFT\_Q31\_TO\_F64(src, m) ((float64\_t)(((int64\_t)src) << m) / (1ULL << 31))

92

96

106

114#define Z\_SHIFT\_F32\_TO\_Q7(src, m) \

115 ((q7\_t)Z\_CLAMP((int32\_t)(src \* (1U << 7)) >> m, INT8\_MIN, INT8\_MAX))

116

124#define Z\_SHIFT\_F32\_TO\_Q15(src, m) \

125 ((q15\_t)Z\_CLAMP((int32\_t)(src \* (1U << 15)) >> m, INT16\_MIN, INT16\_MAX))

126

134#define Z\_SHIFT\_F32\_TO\_Q31(src, m) \

135 ((q31\_t)Z\_CLAMP((int64\_t)(src \* (1U << 31)) >> m, INT32\_MIN, INT32\_MAX))

136

144#define Z\_SHIFT\_F64\_TO\_Q7(src, m) \

145 ((q7\_t)Z\_CLAMP((int32\_t)(src \* (1U << 7)) >> m, INT8\_MIN, INT8\_MAX))

146

154#define Z\_SHIFT\_F64\_TO\_Q15(src, m) \

155 ((q15\_t)Z\_CLAMP((int32\_t)(src \* (1U << 15)) >> m, INT16\_MIN, INT16\_MAX))

156

164#define Z\_SHIFT\_F64\_TO\_Q31(src, m) \

165 ((q31\_t)Z\_CLAMP((int64\_t)(src \* (1U << 31)) >> m, INT32\_MIN, INT32\_MAX))

166

170

171#ifdef \_\_cplusplus

172}

173#endif

174

175#endif /\* INCLUDE\_ZEPHYR\_DSP\_UTILS\_H\_ \*/

[dsp.h](dsp_8h.md)

Public APIs for Digital Signal Processing (DSP) math.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [utils.h](dsp_2utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
