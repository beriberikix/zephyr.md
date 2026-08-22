---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/basicmath_8h_source.html
original_path: doxygen/html/basicmath_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

basicmath.h

[Go to the documentation of this file.](basicmath_8h.md)

1/\* Copyright (C) 2010-2021 ARM Limited or its affiliates. All rights reserved.

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

10

11#ifndef ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_H\_

12#define ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_H\_

13

14#include <[zephyr/dsp/dsp.h](dsp_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

26

38

[ 51](group__math__dsp__basic__mult.md#gae0792b036a40a19af1c25b3a6a23e988)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_mult\_q7](group__math__dsp__basic__mult.md#gae0792b036a40a19af1c25b3a6a23e988)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b,

52 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

53

[ 66](group__math__dsp__basic__mult.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_mult\_q15](group__math__dsp__basic__mult.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b,

67 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

68

[ 81](group__math__dsp__basic__mult.md#ga0e4e4ff5e33e792feecf811cb8e96d18)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_mult\_q31](group__math__dsp__basic__mult.md#ga0e4e4ff5e33e792feecf811cb8e96d18)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b,

82 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

83

[ 91](group__math__dsp__basic__mult.md#gac9513150fc602b6bab481faf36f81ca4)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_mult\_f32](group__math__dsp__basic__mult.md#gac9513150fc602b6bab481faf36f81ca4)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b,

92 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

93

97

109

[ 117](group__math__dsp__basic__add.md#gae890add140205717dcb4b1c39650b797)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_add\_f32](group__math__dsp__basic__add.md#gae890add140205717dcb4b1c39650b797)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b,

118 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

119

[ 132](group__math__dsp__basic__add.md#gae5d919e8595e80216302953797fcf987)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_add\_q7](group__math__dsp__basic__add.md#gae5d919e8595e80216302953797fcf987)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b,

133 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

134

[ 147](group__math__dsp__basic__add.md#ga978af9251a9c8b8d62b47a921dcf9d38)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_add\_q15](group__math__dsp__basic__add.md#ga978af9251a9c8b8d62b47a921dcf9d38)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b,

148 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

149

[ 162](group__math__dsp__basic__add.md#gad2bbabc990f868b3ecfe270458e22657)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_add\_q31](group__math__dsp__basic__add.md#gad2bbabc990f868b3ecfe270458e22657)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b,

163 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

164

168

180

[ 188](group__math__dsp__basic__sub.md#gafc66edd5888b19174cb24c2ea858d24d)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_sub\_f32](group__math__dsp__basic__sub.md#gafc66edd5888b19174cb24c2ea858d24d)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b,

189 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

190

[ 203](group__math__dsp__basic__sub.md#ga4eb67772a48933a9f24a68f73228adbf)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_sub\_q7](group__math__dsp__basic__sub.md#ga4eb67772a48933a9f24a68f73228adbf)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b,

204 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

205

[ 218](group__math__dsp__basic__sub.md#gab9698353b69654eefbd76ff6f723a4f3)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_sub\_q15](group__math__dsp__basic__sub.md#gab9698353b69654eefbd76ff6f723a4f3)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b,

219 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

220

[ 233](group__math__dsp__basic__sub.md#ga693b9677fdf54694e49e03a9b629b35d)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_sub\_q31](group__math__dsp__basic__sub.md#ga693b9677fdf54694e49e03a9b629b35d)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b,

234 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

235

239

265

[ 273](group__math__dsp__basic__scale.md#ga3a07935285b763bb9e9106db42292466)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_scale\_f32](group__math__dsp__basic__scale.md#ga3a07935285b763bb9e9106db42292466)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) scale,

274 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

275

[ 290](group__math__dsp__basic__scale.md#ga2158a3f20bd5af0516f5b3af824c32e1)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_scale\_q7](group__math__dsp__basic__scale.md#ga2158a3f20bd5af0516f5b3af824c32e1)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift,

291 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

292

[ 307](group__math__dsp__basic__scale.md#ga95e03e993542ff1710c771a9dc0eb01b)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_scale\_q15](group__math__dsp__basic__scale.md#ga95e03e993542ff1710c771a9dc0eb01b)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift,

308 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

309

[ 324](group__math__dsp__basic__scale.md#ga63eaab2b1ef431e4bceb90b0a701c879)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_scale\_q31](group__math__dsp__basic__scale.md#ga63eaab2b1ef431e4bceb90b0a701c879)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift,

325 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

326

330

344

[ 351](group__math__dsp__basic__abs.md#ga5a5358fb90f726256f064757fbab1bcd)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_abs\_f32](group__math__dsp__basic__abs.md#ga5a5358fb90f726256f064757fbab1bcd)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst,

352 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

353

[ 365](group__math__dsp__basic__abs.md#ga69c38809979de090a3458ec9b31f4cb4)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_abs\_q7](group__math__dsp__basic__abs.md#ga69c38809979de090a3458ec9b31f4cb4)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

366

[ 378](group__math__dsp__basic__abs.md#ga53ee6bbc05423703f6299fd60c8e1d44)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_abs\_q15](group__math__dsp__basic__abs.md#ga53ee6bbc05423703f6299fd60c8e1d44)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst,

379 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

380

[ 393](group__math__dsp__basic__abs.md#ga74ccbbaf60257ca482fc96e1d40edeca)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_abs\_q31](group__math__dsp__basic__abs.md#ga74ccbbaf60257ca482fc96e1d40edeca)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst,

394 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

395

399

412

[ 420](group__math__dsp__basic__dot.md#ga66932c50dc7e2b7207ad5c8218c110a6)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_dot\_prod\_f32](group__math__dsp__basic__dot.md#ga66932c50dc7e2b7207ad5c8218c110a6)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a,

421 const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size,

422 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*result);

423

[ 438](group__math__dsp__basic__dot.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_dot\_prod\_q7](group__math__dsp__basic__dot.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b,

439 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*result);

440

[ 455](group__math__dsp__basic__dot.md#ga5a76ac790b7d981b97143f7473587ccf)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_dot\_prod\_q15](group__math__dsp__basic__dot.md#ga5a76ac790b7d981b97143f7473587ccf)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b,

456 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result);

457

[ 473](group__math__dsp__basic__dot.md#gaae752f1d9645d8c80fcdabc0f0b249f8)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_dot\_prod\_q31](group__math__dsp__basic__dot.md#gaae752f1d9645d8c80fcdabc0f0b249f8)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b,

474 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result);

475

479

496

[ 510](group__math__dsp__basic__shift.md#ga8eb72ff139c173d3e1794a1d1c1c8fde)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_shift\_q7](group__math__dsp__basic__shift.md#ga8eb72ff139c173d3e1794a1d1c1c8fde)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst,

511 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

512

[ 526](group__math__dsp__basic__shift.md#ga738fc0fe86b9c910a30fceff7dc4a789)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_shift\_q15](group__math__dsp__basic__shift.md#ga738fc0fe86b9c910a30fceff7dc4a789)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits,

527 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

528

[ 542](group__math__dsp__basic__shift.md#gaf9af89a3c76ad385eec0225185b522c9)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_shift\_q31](group__math__dsp__basic__shift.md#gaf9af89a3c76ad385eec0225185b522c9)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits,

543 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

544

548

563

[ 571](group__math__dsp__basic__offset.md#ga1f14e702ad5dc6482fcdb4758ad862c3)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_offset\_f32](group__math__dsp__basic__offset.md#ga1f14e702ad5dc6482fcdb4758ad862c3)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) offset,

572 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

573

[ 586](group__math__dsp__basic__offset.md#ga701b8bbd1437e0f19807c38fd4d0e7e9)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_offset\_q7](group__math__dsp__basic__offset.md#ga701b8bbd1437e0f19807c38fd4d0e7e9)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) offset, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst,

587 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

588

[ 601](group__math__dsp__basic__offset.md#ga1740996532090e41ce20913bb201023c)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_offset\_q15](group__math__dsp__basic__offset.md#ga1740996532090e41ce20913bb201023c)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) offset, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst,

602 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

603

[ 616](group__math__dsp__basic__offset.md#ga2b5958ec0fc8bb26662c41136ec46b3e)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_offset\_q31](group__math__dsp__basic__offset.md#ga2b5958ec0fc8bb26662c41136ec46b3e)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) offset, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst,

617 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

618

622

637

[ 644](group__math__dsp__basic__negate.md#gad8760ce77fcf2198f73813278fa15343)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_negate\_f32](group__math__dsp__basic__negate.md#gad8760ce77fcf2198f73813278fa15343)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst,

645 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

646

[ 658](group__math__dsp__basic__negate.md#ga578a3cee7cff2d818e41ec974066d55a)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_negate\_q7](group__math__dsp__basic__negate.md#ga578a3cee7cff2d818e41ec974066d55a)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst,

659 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

660

[ 672](group__math__dsp__basic__negate.md#ga41dc3e0d8a0bd3654f74cbbd9038153d)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_negate\_q15](group__math__dsp__basic__negate.md#ga41dc3e0d8a0bd3654f74cbbd9038153d)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst,

673 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

674

[ 686](group__math__dsp__basic__negate.md#ga08591323e804b4d7932c7bade4331705)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_negate\_q31](group__math__dsp__basic__negate.md#ga08591323e804b4d7932c7bade4331705)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst,

687 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

688

692

702

[ 710](group__math__dsp__basic__and.md#ga22c8c022d4f8cd9e34f1e1e47433d121)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_and\_u8](group__math__dsp__basic__and.md#ga22c8c022d4f8cd9e34f1e1e47433d121)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b,

711 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

712

[ 720](group__math__dsp__basic__and.md#ga988879dc54666692130793f6ce26fd23)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_and\_u16](group__math__dsp__basic__and.md#ga988879dc54666692130793f6ce26fd23)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b,

721 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

722

[ 730](group__math__dsp__basic__and.md#ga99019932e69574ca8aef86b4ace9c3b6)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_and\_u32](group__math__dsp__basic__and.md#ga99019932e69574ca8aef86b4ace9c3b6)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b,

731 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

732

736

746

[ 754](group__math__dsp__basic__or.md#gabf9687bce70f19c4192b2ddba7b0d2da)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_or\_u8](group__math__dsp__basic__or.md#gabf9687bce70f19c4192b2ddba7b0d2da)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b,

755 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

756

[ 764](group__math__dsp__basic__or.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_or\_u16](group__math__dsp__basic__or.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b,

765 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

766

[ 774](group__math__dsp__basic__or.md#gaa218930efe8ab83663eb00b4f6f170bc)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_or\_u32](group__math__dsp__basic__or.md#gaa218930efe8ab83663eb00b4f6f170bc)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b,

775 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

776

780

790

[ 797](group__math__dsp__basic__not.md#gaafd38edd648a03d328d51b5ca9097b5d)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_not\_u8](group__math__dsp__basic__not.md#gaafd38edd648a03d328d51b5ca9097b5d)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst,

798 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

799

[ 806](group__math__dsp__basic__not.md#ga3bca20f3c626e1a64dd79d0e22a43bed)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_not\_u16](group__math__dsp__basic__not.md#ga3bca20f3c626e1a64dd79d0e22a43bed)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst,

807 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

808

[ 815](group__math__dsp__basic__not.md#gafd6993acd6abeaa529dea84f3fd4d3a9)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_not\_u32](group__math__dsp__basic__not.md#gafd6993acd6abeaa529dea84f3fd4d3a9)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst,

816 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

817

821

831

[ 839](group__math__dsp__basic__xor.md#ga4f5a442ce2ce79a6d09fde4648ceb100)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_xor\_u8](group__math__dsp__basic__xor.md#ga4f5a442ce2ce79a6d09fde4648ceb100)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b,

840 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

841

[ 849](group__math__dsp__basic__xor.md#gaa4d486a9a9022120e86e6e5d62940444)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_xor\_u16](group__math__dsp__basic__xor.md#gaa4d486a9a9022120e86e6e5d62940444)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b,

850 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

851

[ 859](group__math__dsp__basic__xor.md#gac4dd8fed6e7485a0e989fb37b3fe0c77)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_xor\_u32](group__math__dsp__basic__xor.md#gac4dd8fed6e7485a0e989fb37b3fe0c77)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b,

860 [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size);

861

865

877

[ 886](group__math__dsp__basic__clip.md#gaa81f891d1946313161d1a2989aafe0e1)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_clip\_f32](group__math__dsp__basic__clip.md#gaa81f891d1946313161d1a2989aafe0e1)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst,

887 [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) low, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples);

888

[ 897](group__math__dsp__basic__clip.md#ga2a7483cb8150e3caee8fade382dc3ceb)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_clip\_q31](group__math__dsp__basic__clip.md#ga2a7483cb8150e3caee8fade382dc3ceb)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) low,

898 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples);

899

[ 908](group__math__dsp__basic__clip.md#ga7c83f52241784bfdf81baf14581435b9)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_clip\_q15](group__math__dsp__basic__clip.md#ga7c83f52241784bfdf81baf14581435b9)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) low,

909 [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples);

910

[ 919](group__math__dsp__basic__clip.md#ga4e368fccf4ec5f46e82127816ecfc22e)[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void [zdsp\_clip\_q7](group__math__dsp__basic__clip.md#ga4e368fccf4ec5f46e82127816ecfc22e)(const [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) low, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) high,

920 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples);

921

925

929

930#ifdef \_\_cplusplus

931}

932#endif

933

934#ifdef CONFIG\_FP16

935#include <[zephyr/dsp/basicmath\_f16.h](basicmath__f16_8h.md)>

936#endif /\* CONFIG\_FP16 \*/

937

938#endif /\* ZEPHYR\_INCLUDE\_DSP\_BASICMATH\_H\_ \*/

[basicmath\_f16.h](basicmath__f16_8h.md)

Public APIs for DSP basicmath for 16 bit floating point.

[dsp.h](dsp_8h.md)

Public APIs for Digital Signal Processing (DSP) math.

[DSP\_DATA](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c)

#define DSP\_DATA

**Definition** dsp.h:23

[DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7)

#define DSP\_FUNC\_SCOPE

**Definition** dsp.h:17

[zdsp\_abs\_q15](group__math__dsp__basic__abs.md#ga53ee6bbc05423703f6299fd60c8e1d44)

void zdsp\_abs\_q15(const q15\_t \*src, q15\_t \*dst, uint32\_t block\_size)

Q15 vector absolute value.

[zdsp\_abs\_f32](group__math__dsp__basic__abs.md#ga5a5358fb90f726256f064757fbab1bcd)

void zdsp\_abs\_f32(const float32\_t \*src, float32\_t \*dst, uint32\_t block\_size)

Floating-point vector absolute value.

[zdsp\_abs\_q7](group__math__dsp__basic__abs.md#ga69c38809979de090a3458ec9b31f4cb4)

void zdsp\_abs\_q7(const q7\_t \*src, q7\_t \*dst, uint32\_t block\_size)

Q7 vector absolute value.

[zdsp\_abs\_q31](group__math__dsp__basic__abs.md#ga74ccbbaf60257ca482fc96e1d40edeca)

void zdsp\_abs\_q31(const q31\_t \*src, q31\_t \*dst, uint32\_t block\_size)

Q31 vector absolute value.

[zdsp\_add\_q15](group__math__dsp__basic__add.md#ga978af9251a9c8b8d62b47a921dcf9d38)

void zdsp\_add\_q15(const q15\_t \*src\_a, const q15\_t \*src\_b, q15\_t \*dst, uint32\_t block\_size)

Q15 vector addition.

[zdsp\_add\_q31](group__math__dsp__basic__add.md#gad2bbabc990f868b3ecfe270458e22657)

void zdsp\_add\_q31(const q31\_t \*src\_a, const q31\_t \*src\_b, q31\_t \*dst, uint32\_t block\_size)

Q31 vector addition.

[zdsp\_add\_q7](group__math__dsp__basic__add.md#gae5d919e8595e80216302953797fcf987)

void zdsp\_add\_q7(const q7\_t \*src\_a, const q7\_t \*src\_b, q7\_t \*dst, uint32\_t block\_size)

Q7 vector addition.

[zdsp\_add\_f32](group__math__dsp__basic__add.md#gae890add140205717dcb4b1c39650b797)

void zdsp\_add\_f32(const float32\_t \*src\_a, const float32\_t \*src\_b, float32\_t \*dst, uint32\_t block\_size)

Floating-point vector addition.

[zdsp\_and\_u8](group__math__dsp__basic__and.md#ga22c8c022d4f8cd9e34f1e1e47433d121)

void zdsp\_and\_u8(const uint8\_t \*src\_a, const uint8\_t \*src\_b, uint8\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise AND of two fixed-point vectors.

[zdsp\_and\_u16](group__math__dsp__basic__and.md#ga988879dc54666692130793f6ce26fd23)

void zdsp\_and\_u16(const uint16\_t \*src\_a, const uint16\_t \*src\_b, uint16\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise AND of two fixed-point vectors.

[zdsp\_and\_u32](group__math__dsp__basic__and.md#ga99019932e69574ca8aef86b4ace9c3b6)

void zdsp\_and\_u32(const uint32\_t \*src\_a, const uint32\_t \*src\_b, uint32\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise AND of two fixed-point vectors.

[zdsp\_clip\_q31](group__math__dsp__basic__clip.md#ga2a7483cb8150e3caee8fade382dc3ceb)

void zdsp\_clip\_q31(const q31\_t \*src, q31\_t \*dst, q31\_t low, q31\_t high, uint32\_t num\_samples)

Elementwise fixed-point clipping.

[zdsp\_clip\_q7](group__math__dsp__basic__clip.md#ga4e368fccf4ec5f46e82127816ecfc22e)

void zdsp\_clip\_q7(const q7\_t \*src, q7\_t \*dst, q7\_t low, q7\_t high, uint32\_t num\_samples)

Elementwise fixed-point clipping.

[zdsp\_clip\_q15](group__math__dsp__basic__clip.md#ga7c83f52241784bfdf81baf14581435b9)

void zdsp\_clip\_q15(const q15\_t \*src, q15\_t \*dst, q15\_t low, q15\_t high, uint32\_t num\_samples)

Elementwise fixed-point clipping.

[zdsp\_clip\_f32](group__math__dsp__basic__clip.md#gaa81f891d1946313161d1a2989aafe0e1)

void zdsp\_clip\_f32(const float32\_t \*src, float32\_t \*dst, float32\_t low, float32\_t high, uint32\_t num\_samples)

Elementwise floating-point clipping.

[zdsp\_dot\_prod\_q15](group__math__dsp__basic__dot.md#ga5a76ac790b7d981b97143f7473587ccf)

void zdsp\_dot\_prod\_q15(const q15\_t \*src\_a, const q15\_t \*src\_b, uint32\_t block\_size, q63\_t \*result)

Dot product of Q15 vectors.

[zdsp\_dot\_prod\_f32](group__math__dsp__basic__dot.md#ga66932c50dc7e2b7207ad5c8218c110a6)

void zdsp\_dot\_prod\_f32(const float32\_t \*src\_a, const float32\_t \*src\_b, uint32\_t block\_size, float32\_t \*result)

Dot product of floating-point vectors.

[zdsp\_dot\_prod\_q7](group__math__dsp__basic__dot.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb)

void zdsp\_dot\_prod\_q7(const q7\_t \*src\_a, const q7\_t \*src\_b, uint32\_t block\_size, q31\_t \*result)

Dot product of Q7 vectors.

[zdsp\_dot\_prod\_q31](group__math__dsp__basic__dot.md#gaae752f1d9645d8c80fcdabc0f0b249f8)

void zdsp\_dot\_prod\_q31(const q31\_t \*src\_a, const q31\_t \*src\_b, uint32\_t block\_size, q63\_t \*result)

Dot product of Q31 vectors.

[zdsp\_mult\_q31](group__math__dsp__basic__mult.md#ga0e4e4ff5e33e792feecf811cb8e96d18)

void zdsp\_mult\_q31(const q31\_t \*src\_a, const q31\_t \*src\_b, q31\_t \*dst, uint32\_t block\_size)

Q31 vector multiplication.

[zdsp\_mult\_f32](group__math__dsp__basic__mult.md#gac9513150fc602b6bab481faf36f81ca4)

void zdsp\_mult\_f32(const float32\_t \*src\_a, const float32\_t \*src\_b, float32\_t \*dst, uint32\_t block\_size)

Floating-point vector multiplication.

[zdsp\_mult\_q7](group__math__dsp__basic__mult.md#gae0792b036a40a19af1c25b3a6a23e988)

void zdsp\_mult\_q7(const q7\_t \*src\_a, const q7\_t \*src\_b, q7\_t \*dst, uint32\_t block\_size)

Q7 vector multiplication.

[zdsp\_mult\_q15](group__math__dsp__basic__mult.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7)

void zdsp\_mult\_q15(const q15\_t \*src\_a, const q15\_t \*src\_b, q15\_t \*dst, uint32\_t block\_size)

Q15 vector multiplication.

[zdsp\_negate\_q31](group__math__dsp__basic__negate.md#ga08591323e804b4d7932c7bade4331705)

void zdsp\_negate\_q31(const q31\_t \*src, q31\_t \*dst, uint32\_t block\_size)

Negates the elements of a Q31 vector.

[zdsp\_negate\_q15](group__math__dsp__basic__negate.md#ga41dc3e0d8a0bd3654f74cbbd9038153d)

void zdsp\_negate\_q15(const q15\_t \*src, q15\_t \*dst, uint32\_t block\_size)

Negates the elements of a Q15 vector.

[zdsp\_negate\_q7](group__math__dsp__basic__negate.md#ga578a3cee7cff2d818e41ec974066d55a)

void zdsp\_negate\_q7(const q7\_t \*src, q7\_t \*dst, uint32\_t block\_size)

Negates the elements of a Q7 vector.

[zdsp\_negate\_f32](group__math__dsp__basic__negate.md#gad8760ce77fcf2198f73813278fa15343)

void zdsp\_negate\_f32(const float32\_t \*src, float32\_t \*dst, uint32\_t block\_size)

Negates the elements of a floating-point vector.

[zdsp\_not\_u16](group__math__dsp__basic__not.md#ga3bca20f3c626e1a64dd79d0e22a43bed)

void zdsp\_not\_u16(const uint16\_t \*src, uint16\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise NOT of a fixed-point vector.

[zdsp\_not\_u8](group__math__dsp__basic__not.md#gaafd38edd648a03d328d51b5ca9097b5d)

void zdsp\_not\_u8(const uint8\_t \*src, uint8\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise NOT of a fixed-point vector.

[zdsp\_not\_u32](group__math__dsp__basic__not.md#gafd6993acd6abeaa529dea84f3fd4d3a9)

void zdsp\_not\_u32(const uint32\_t \*src, uint32\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise NOT of a fixed-point vector.

[zdsp\_offset\_q15](group__math__dsp__basic__offset.md#ga1740996532090e41ce20913bb201023c)

void zdsp\_offset\_q15(const q15\_t \*src, q15\_t offset, q15\_t \*dst, uint32\_t block\_size)

Adds a constant offset to a Q15 vector.

[zdsp\_offset\_f32](group__math__dsp__basic__offset.md#ga1f14e702ad5dc6482fcdb4758ad862c3)

void zdsp\_offset\_f32(const float32\_t \*src, float32\_t offset, float32\_t \*dst, uint32\_t block\_size)

Adds a constant offset to a floating-point vector.

[zdsp\_offset\_q31](group__math__dsp__basic__offset.md#ga2b5958ec0fc8bb26662c41136ec46b3e)

void zdsp\_offset\_q31(const q31\_t \*src, q31\_t offset, q31\_t \*dst, uint32\_t block\_size)

Adds a constant offset to a Q31 vector.

[zdsp\_offset\_q7](group__math__dsp__basic__offset.md#ga701b8bbd1437e0f19807c38fd4d0e7e9)

void zdsp\_offset\_q7(const q7\_t \*src, q7\_t offset, q7\_t \*dst, uint32\_t block\_size)

Adds a constant offset to a Q7 vector.

[zdsp\_or\_u16](group__math__dsp__basic__or.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a)

void zdsp\_or\_u16(const uint16\_t \*src\_a, const uint16\_t \*src\_b, uint16\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise OR of two fixed-point vectors.

[zdsp\_or\_u32](group__math__dsp__basic__or.md#gaa218930efe8ab83663eb00b4f6f170bc)

void zdsp\_or\_u32(const uint32\_t \*src\_a, const uint32\_t \*src\_b, uint32\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise OR of two fixed-point vectors.

[zdsp\_or\_u8](group__math__dsp__basic__or.md#gabf9687bce70f19c4192b2ddba7b0d2da)

void zdsp\_or\_u8(const uint8\_t \*src\_a, const uint8\_t \*src\_b, uint8\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise OR of two fixed-point vectors.

[zdsp\_scale\_q7](group__math__dsp__basic__scale.md#ga2158a3f20bd5af0516f5b3af824c32e1)

void zdsp\_scale\_q7(const q7\_t \*src, q7\_t scale\_fract, int8\_t shift, q7\_t \*dst, uint32\_t block\_size)

Multiplies a Q7 vector by a scalar.

[zdsp\_scale\_f32](group__math__dsp__basic__scale.md#ga3a07935285b763bb9e9106db42292466)

void zdsp\_scale\_f32(const float32\_t \*src, float32\_t scale, float32\_t \*dst, uint32\_t block\_size)

Multiplies a floating-point vector by a scalar.

[zdsp\_scale\_q31](group__math__dsp__basic__scale.md#ga63eaab2b1ef431e4bceb90b0a701c879)

void zdsp\_scale\_q31(const q31\_t \*src, q31\_t scale\_fract, int8\_t shift, q31\_t \*dst, uint32\_t block\_size)

Multiplies a Q31 vector by a scalar.

[zdsp\_scale\_q15](group__math__dsp__basic__scale.md#ga95e03e993542ff1710c771a9dc0eb01b)

void zdsp\_scale\_q15(const q15\_t \*src, q15\_t scale\_fract, int8\_t shift, q15\_t \*dst, uint32\_t block\_size)

Multiplies a Q15 vector by a scalar.

[zdsp\_shift\_q15](group__math__dsp__basic__shift.md#ga738fc0fe86b9c910a30fceff7dc4a789)

void zdsp\_shift\_q15(const q15\_t \*src, int8\_t shift\_bits, q15\_t \*dst, uint32\_t block\_size)

Shifts the elements of a Q15 vector a specified number of bits.

[zdsp\_shift\_q7](group__math__dsp__basic__shift.md#ga8eb72ff139c173d3e1794a1d1c1c8fde)

void zdsp\_shift\_q7(const q7\_t \*src, int8\_t shift\_bits, q7\_t \*dst, uint32\_t block\_size)

Shifts the elements of a Q7 vector a specified number of bits.

[zdsp\_shift\_q31](group__math__dsp__basic__shift.md#gaf9af89a3c76ad385eec0225185b522c9)

void zdsp\_shift\_q31(const q31\_t \*src, int8\_t shift\_bits, q31\_t \*dst, uint32\_t block\_size)

Shifts the elements of a Q31 vector a specified number of bits.

[zdsp\_sub\_q7](group__math__dsp__basic__sub.md#ga4eb67772a48933a9f24a68f73228adbf)

void zdsp\_sub\_q7(const q7\_t \*src\_a, const q7\_t \*src\_b, q7\_t \*dst, uint32\_t block\_size)

Q7 vector subtraction.

[zdsp\_sub\_q31](group__math__dsp__basic__sub.md#ga693b9677fdf54694e49e03a9b629b35d)

void zdsp\_sub\_q31(const q31\_t \*src\_a, const q31\_t \*src\_b, q31\_t \*dst, uint32\_t block\_size)

Q31 vector subtraction.

[zdsp\_sub\_q15](group__math__dsp__basic__sub.md#gab9698353b69654eefbd76ff6f723a4f3)

void zdsp\_sub\_q15(const q15\_t \*src\_a, const q15\_t \*src\_b, q15\_t \*dst, uint32\_t block\_size)

Q15 vector subtraction.

[zdsp\_sub\_f32](group__math__dsp__basic__sub.md#gafc66edd5888b19174cb24c2ea858d24d)

void zdsp\_sub\_f32(const float32\_t \*src\_a, const float32\_t \*src\_b, float32\_t \*dst, uint32\_t block\_size)

Floating-point vector subtraction.

[zdsp\_xor\_u8](group__math__dsp__basic__xor.md#ga4f5a442ce2ce79a6d09fde4648ceb100)

void zdsp\_xor\_u8(const uint8\_t \*src\_a, const uint8\_t \*src\_b, uint8\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise XOR of two fixed-point vectors.

[zdsp\_xor\_u16](group__math__dsp__basic__xor.md#gaa4d486a9a9022120e86e6e5d62940444)

void zdsp\_xor\_u16(const uint16\_t \*src\_a, const uint16\_t \*src\_b, uint16\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise XOR of two fixed-point vectors.

[zdsp\_xor\_u32](group__math__dsp__basic__xor.md#gac4dd8fed6e7485a0e989fb37b3fe0c77)

void zdsp\_xor\_u32(const uint32\_t \*src\_a, const uint32\_t \*src\_b, uint32\_t \*dst, uint32\_t block\_size)

Compute the logical bitwise XOR of two fixed-point vectors.

[float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715)

float float32\_t

32-bit floating-point type definition.

**Definition** types.h:55

[q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)

int64\_t q63\_t

64-bit fractional data type in 1.63 format.

**Definition** types.h:41

[q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea)

int16\_t q15\_t

16-bit fractional data type in 1.15 format.

**Definition** types.h:29

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263)

int8\_t q7\_t

8-bit fractional data type in 1.7 format.

**Definition** types.h:23

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [basicmath.h](basicmath_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
