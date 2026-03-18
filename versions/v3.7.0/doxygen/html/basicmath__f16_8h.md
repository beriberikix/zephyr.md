---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/basicmath__f16_8h.html
original_path: doxygen/html/basicmath__f16_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

basicmath\_f16.h File Reference

Public APIs for DSP basicmath for 16 bit floating point.
[More...](#details)

`#include <[zephyr/dsp/dsp.h](dsp_8h_source.md)>`

[Go to the source code of this file.](basicmath__f16_8h_source.md)

| Functions | |
| --- | --- |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_mult\_f16](group__math__dsp__basic__mult.md#ga795bc69852005a0e547c3f2794c5397a) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector multiplication. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_add\_f16](group__math__dsp__basic__add.md#ga3ad2849433440c2d1175cd6f18e6eade) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector addition. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_sub\_f16](group__math__dsp__basic__sub.md#ga500f6403d4382bc797231d7962275230) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector subtraction. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_scale\_f16](group__math__dsp__basic__scale.md#ga26c461531e82511c18902ba908f36230) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) scale, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a floating-point vector by a scalar. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_abs\_f16](group__math__dsp__basic__abs.md#gaf178acd8862a2928a65e98f4fef1380b) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector absolute value. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_dot\_prod\_f16](group__math__dsp__basic__dot.md#ga11af65d379fa201a04408544ddca8354) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*result) |
|  | Dot product of floating-point vectors. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_offset\_f16](group__math__dsp__basic__offset.md#ga60d4ef0543308773e651a0f40b3b0fe1) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) offset, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a floating-point vector. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_negate\_f16](group__math__dsp__basic__negate.md#ga7aacb425c3dfb2c5d8664a7cf4031c3b) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a floating-point vector. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_clip\_f16](group__math__dsp__basic__clip.md#ga4edd7ba5b9c3791d7857a2c7d1541cab) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) low, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise floating-point clipping. |

## Detailed Description

Public APIs for DSP basicmath for 16 bit floating point.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [basicmath\_f16.h](basicmath__f16_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
