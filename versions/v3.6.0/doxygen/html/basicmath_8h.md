---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/basicmath_8h.html
original_path: doxygen/html/basicmath_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

basicmath.h File Reference

Public APIs for DSP basicmath.
[More...](#details)

`#include <[zephyr/dsp/dsp.h](dsp_8h_source.md)>`  
`#include <[zephyr/dsp/basicmath_f16.h](basicmath__f16_8h_source.md)>`

[Go to the source code of this file.](basicmath_8h_source.md)

| Functions | |
| --- | --- |
| void | [zdsp\_mult\_q7](group__math__dsp__basic__mult.md#gae0792b036a40a19af1c25b3a6a23e988) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector multiplication. |
| void | [zdsp\_mult\_q15](group__math__dsp__basic__mult.md#gaf8aa8d6e976c9ee5f4ac836506da3bc7) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector multiplication. |
| void | [zdsp\_mult\_q31](group__math__dsp__basic__mult.md#ga0e4e4ff5e33e792feecf811cb8e96d18) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector multiplication. |
| void | [zdsp\_mult\_f32](group__math__dsp__basic__mult.md#gac9513150fc602b6bab481faf36f81ca4) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector multiplication. |
| void | [zdsp\_add\_f32](group__math__dsp__basic__add.md#gae890add140205717dcb4b1c39650b797) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector addition. |
| void | [zdsp\_add\_q7](group__math__dsp__basic__add.md#gae5d919e8595e80216302953797fcf987) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector addition. |
| void | [zdsp\_add\_q15](group__math__dsp__basic__add.md#ga978af9251a9c8b8d62b47a921dcf9d38) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector addition. |
| void | [zdsp\_add\_q31](group__math__dsp__basic__add.md#gad2bbabc990f868b3ecfe270458e22657) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector addition. |
| void | [zdsp\_sub\_f32](group__math__dsp__basic__sub.md#gafc66edd5888b19174cb24c2ea858d24d) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector subtraction. |
| void | [zdsp\_sub\_q7](group__math__dsp__basic__sub.md#ga4eb67772a48933a9f24a68f73228adbf) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector subtraction. |
| void | [zdsp\_sub\_q15](group__math__dsp__basic__sub.md#gab9698353b69654eefbd76ff6f723a4f3) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector subtraction. |
| void | [zdsp\_sub\_q31](group__math__dsp__basic__sub.md#ga693b9677fdf54694e49e03a9b629b35d) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector subtraction. |
| void | [zdsp\_scale\_f32](group__math__dsp__basic__scale.md#ga3a07935285b763bb9e9106db42292466) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) scale, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a floating-point vector by a scalar. |
| void | [zdsp\_scale\_q7](group__math__dsp__basic__scale.md#ga2158a3f20bd5af0516f5b3af824c32e1) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q7 vector by a scalar. |
| void | [zdsp\_scale\_q15](group__math__dsp__basic__scale.md#ga95e03e993542ff1710c771a9dc0eb01b) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q15 vector by a scalar. |
| void | [zdsp\_scale\_q31](group__math__dsp__basic__scale.md#ga63eaab2b1ef431e4bceb90b0a701c879) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q31 vector by a scalar. |
| void | [zdsp\_abs\_f32](group__math__dsp__basic__abs.md#ga5a5358fb90f726256f064757fbab1bcd) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector absolute value. |
| void | [zdsp\_abs\_q7](group__math__dsp__basic__abs.md#ga69c38809979de090a3458ec9b31f4cb4) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector absolute value. |
| void | [zdsp\_abs\_q15](group__math__dsp__basic__abs.md#ga53ee6bbc05423703f6299fd60c8e1d44) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector absolute value. |
| void | [zdsp\_abs\_q31](group__math__dsp__basic__abs.md#ga74ccbbaf60257ca482fc96e1d40edeca) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector absolute value. |
| void | [zdsp\_dot\_prod\_f32](group__math__dsp__basic__dot.md#ga66932c50dc7e2b7207ad5c8218c110a6) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*result) |
|  | Dot product of floating-point vectors. |
| void | [zdsp\_dot\_prod\_q7](group__math__dsp__basic__dot.md#gaa6bdeed693734e5d1c7b93b58eaf9eeb) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*result) |
|  | Dot product of Q7 vectors. |
| void | [zdsp\_dot\_prod\_q15](group__math__dsp__basic__dot.md#ga5a76ac790b7d981b97143f7473587ccf) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result) |
|  | Dot product of Q15 vectors. |
| void | [zdsp\_dot\_prod\_q31](group__math__dsp__basic__dot.md#gaae752f1d9645d8c80fcdabc0f0b249f8) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result) |
|  | Dot product of Q31 vectors. |
| void | [zdsp\_shift\_q7](group__math__dsp__basic__shift.md#ga8eb72ff139c173d3e1794a1d1c1c8fde) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q7 vector a specified number of bits. |
| void | [zdsp\_shift\_q15](group__math__dsp__basic__shift.md#ga738fc0fe86b9c910a30fceff7dc4a789) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q15 vector a specified number of bits. |
| void | [zdsp\_shift\_q31](group__math__dsp__basic__shift.md#gaf9af89a3c76ad385eec0225185b522c9) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q31 vector a specified number of bits. |
| void | [zdsp\_offset\_f32](group__math__dsp__basic__offset.md#ga1f14e702ad5dc6482fcdb4758ad862c3) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) offset, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a floating-point vector. |
| void | [zdsp\_offset\_q7](group__math__dsp__basic__offset.md#ga701b8bbd1437e0f19807c38fd4d0e7e9) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) offset, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q7 vector. |
| void | [zdsp\_offset\_q15](group__math__dsp__basic__offset.md#ga1740996532090e41ce20913bb201023c) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) offset, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q15 vector. |
| void | [zdsp\_offset\_q31](group__math__dsp__basic__offset.md#ga2b5958ec0fc8bb26662c41136ec46b3e) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) offset, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q31 vector. |
| void | [zdsp\_negate\_f32](group__math__dsp__basic__negate.md#gad8760ce77fcf2198f73813278fa15343) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a floating-point vector. |
| void | [zdsp\_negate\_q7](group__math__dsp__basic__negate.md#ga578a3cee7cff2d818e41ec974066d55a) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q7 vector. |
| void | [zdsp\_negate\_q15](group__math__dsp__basic__negate.md#ga41dc3e0d8a0bd3654f74cbbd9038153d) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q15 vector. |
| void | [zdsp\_negate\_q31](group__math__dsp__basic__negate.md#ga08591323e804b4d7932c7bade4331705) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q31 vector. |
| void | [zdsp\_and\_u8](group__math__dsp__basic__and.md#ga22c8c022d4f8cd9e34f1e1e47433d121) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise AND of two fixed-point vectors. |
| void | [zdsp\_and\_u16](group__math__dsp__basic__and.md#ga988879dc54666692130793f6ce26fd23) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise AND of two fixed-point vectors. |
| void | [zdsp\_and\_u32](group__math__dsp__basic__and.md#ga99019932e69574ca8aef86b4ace9c3b6) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise AND of two fixed-point vectors. |
| void | [zdsp\_or\_u8](group__math__dsp__basic__or.md#gabf9687bce70f19c4192b2ddba7b0d2da) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |
| void | [zdsp\_or\_u16](group__math__dsp__basic__or.md#ga979e50ef34a5e5c8dc28f1cfc5ef708a) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |
| void | [zdsp\_or\_u32](group__math__dsp__basic__or.md#gaa218930efe8ab83663eb00b4f6f170bc) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |
| void | [zdsp\_not\_u8](group__math__dsp__basic__not.md#gaafd38edd648a03d328d51b5ca9097b5d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |
| void | [zdsp\_not\_u16](group__math__dsp__basic__not.md#ga3bca20f3c626e1a64dd79d0e22a43bed) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |
| void | [zdsp\_not\_u32](group__math__dsp__basic__not.md#gafd6993acd6abeaa529dea84f3fd4d3a9) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |
| void | [zdsp\_xor\_u8](group__math__dsp__basic__xor.md#ga4f5a442ce2ce79a6d09fde4648ceb100) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |
| void | [zdsp\_xor\_u16](group__math__dsp__basic__xor.md#gaa4d486a9a9022120e86e6e5d62940444) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |
| void | [zdsp\_xor\_u32](group__math__dsp__basic__xor.md#gac4dd8fed6e7485a0e989fb37b3fe0c77) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |
| void | [zdsp\_clip\_f32](group__math__dsp__basic__clip.md#gaa81f891d1946313161d1a2989aafe0e1) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) low, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise floating-point clipping. |
| void | [zdsp\_clip\_q31](group__math__dsp__basic__clip.md#ga2a7483cb8150e3caee8fade382dc3ceb) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) low, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |
| void | [zdsp\_clip\_q15](group__math__dsp__basic__clip.md#ga7c83f52241784bfdf81baf14581435b9) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) low, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |
| void | [zdsp\_clip\_q7](group__math__dsp__basic__clip.md#ga4e368fccf4ec5f46e82127816ecfc22e) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) low, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |

## Detailed Description

Public APIs for DSP basicmath.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [basicmath.h](basicmath_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
