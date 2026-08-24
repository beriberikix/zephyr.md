---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dsp_2utils_8h_source.html
original_path: doxygen/html/dsp_2utils_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

32

42

50#define Z\_SHIFT\_Q7\_TO\_F32(src, m) ((float32\_t)(((src << m)) / (float32\_t)(1U << 7)))

51

59#define Z\_SHIFT\_Q15\_TO\_F32(src, m) ((float32\_t)((src << m) / (float32\_t)(1U << 15)))

60

68#define Z\_SHIFT\_Q31\_TO\_F32(src, m) ((float32\_t)(((int64\_t)src) << m) / (float32\_t)(1U << 31))

69

77#define Z\_SHIFT\_Q7\_TO\_F64(src, m) (((float64\_t)(src << m)) / (1U << 7))

78

86#define Z\_SHIFT\_Q15\_TO\_F64(src, m) (((float64\_t)(src << m)) / (1UL << 15))

87

95#define Z\_SHIFT\_Q31\_TO\_F64(src, m) ((float64\_t)(((int64\_t)src) << m) / (1ULL << 31))

96

100

110

118#define Z\_SHIFT\_F32\_TO\_Q7(src, m) \

119 ((q7\_t)Z\_CLAMP((int32\_t)(src \* (1U << 7)) >> m, INT8\_MIN, INT8\_MAX))

120

128#define Z\_SHIFT\_F32\_TO\_Q15(src, m) \

129 ((q15\_t)Z\_CLAMP((int32\_t)(src \* (1U << 15)) >> m, INT16\_MIN, INT16\_MAX))

130

138#define Z\_SHIFT\_F32\_TO\_Q31(src, m) \

139 ((q31\_t)Z\_CLAMP((int64\_t)(src \* (1U << 31)) >> m, INT32\_MIN, INT32\_MAX))

140

148#define Z\_SHIFT\_F64\_TO\_Q7(src, m) \

149 ((q7\_t)Z\_CLAMP((int32\_t)(src \* (1U << 7)) >> m, INT8\_MIN, INT8\_MAX))

150

158#define Z\_SHIFT\_F64\_TO\_Q15(src, m) \

159 ((q15\_t)Z\_CLAMP((int32\_t)(src \* (1U << 15)) >> m, INT16\_MIN, INT16\_MAX))

160

168#define Z\_SHIFT\_F64\_TO\_Q31(src, m) \

169 ((q31\_t)Z\_CLAMP((int64\_t)(src \* (1U << 31)) >> m, INT32\_MIN, INT32\_MAX))

170

174

178

179#ifdef \_\_cplusplus

180}

181#endif

182

183#endif /\* INCLUDE\_ZEPHYR\_DSP\_UTILS\_H\_ \*/

[dsp.h](dsp_8h.md)

Public APIs for Digital Signal Processing (DSP) math.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [utils.h](dsp_2utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
