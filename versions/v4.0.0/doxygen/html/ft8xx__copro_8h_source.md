---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx__copro_8h_source.html
original_path: doxygen/html/ft8xx__copro_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_copro.h

[Go to the documentation of this file.](ft8xx__copro_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COPRO\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COPRO\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 29](group__ft8xx__copro.md#ga304badab7bd34208d499b199080fb557)#define FT8XX\_OPT\_3D 0

[ 31](group__ft8xx__copro.md#ga3a79c1128bdb9fe094843688691a085c)#define FT8XX\_OPT\_RGB565 0

[ 33](group__ft8xx__copro.md#ga415760ddf94db71ee9a504300bac4661)#define FT8XX\_OPT\_MONO 1

[ 35](group__ft8xx__copro.md#gacc953470460b083c0b8bd9ebbc8ed03b)#define FT8XX\_OPT\_NODL 2

[ 37](group__ft8xx__copro.md#ga160b331fb401eec023e0992c6f4c6331)#define FT8XX\_OPT\_FLAT 256

[ 39](group__ft8xx__copro.md#ga5a58155896cdb2d0f1693d203706ce93)#define FT8XX\_OPT\_SIGNED 256

[ 41](group__ft8xx__copro.md#gac2d1ccbb99eaa032ed9d39fc01d32c66)#define FT8XX\_OPT\_CENTERX 512

[ 43](group__ft8xx__copro.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a)#define FT8XX\_OPT\_CENTERY 1024

[ 45](group__ft8xx__copro.md#ga013968a6bf9534265c897ab1f4018eb0)#define FT8XX\_OPT\_CENTER 1536

[ 47](group__ft8xx__copro.md#gac864c155bc2121bf8d3954e1ed8dbb7e)#define FT8XX\_OPT\_RIGHTX 2048

[ 49](group__ft8xx__copro.md#gacb08df4fac256cbf808b133d4159aa29)#define FT8XX\_OPT\_NOBACK 4096

[ 53](group__ft8xx__copro.md#ga50f4fac88e4f4b558450adcda33dae93)#define FT8XX\_OPT\_NOTICKS 8192

[ 57](group__ft8xx__copro.md#ga79938d9c1193d44a527ca8c158117a86)#define FT8XX\_OPT\_NOHM 16384

[ 59](group__ft8xx__copro.md#ga1a9838a862ec166bfe95d64144b9a052)#define FT8XX\_OPT\_NOPOINTER 16384

[ 61](group__ft8xx__copro.md#ga6416f4282d2c483d2adba8c1215ab638)#define FT8XX\_OPT\_NOSECS 32768

[ 63](group__ft8xx__copro.md#gade56de46694ca420460c1ceb26a33120)#define FT8XX\_OPT\_NOHANDS 49152

64

[ 70](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee)void [ft8xx\_copro\_cmd](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

71

[ 75](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602)void [ft8xx\_copro\_cmd\_dlstart](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602)(void);

76

[ 80](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929)void [ft8xx\_copro\_cmd\_swap](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929)(void);

81

[ 97](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345)void [ft8xx\_copro\_cmd\_text](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x,

98 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y,

99 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font,

100 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options,

101 const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

102

[ 122](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c)void [ft8xx\_copro\_cmd\_number](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x,

123 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y,

124 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font,

125 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options,

126 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n);

127

[ 139](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b)void [ft8xx\_copro\_cmd\_calibrate](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result);

140

144

145#ifdef \_\_cplusplus

146}

147#endif

148

149#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COPRO\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[ft8xx\_copro\_cmd\_dlstart](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602)

void ft8xx\_copro\_cmd\_dlstart(void)

Start a new display list.

[ft8xx\_copro\_cmd\_number](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c)

void ft8xx\_copro\_cmd\_number(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, int32\_t n)

Draw a decimal number.

[ft8xx\_copro\_cmd\_calibrate](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b)

void ft8xx\_copro\_cmd\_calibrate(uint32\_t \*result)

Execute the touch screen calibration routine.

[ft8xx\_copro\_cmd\_swap](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929)

void ft8xx\_copro\_cmd\_swap(void)

Swap the current display list.

[ft8xx\_copro\_cmd\_text](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345)

void ft8xx\_copro\_cmd\_text(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, const char \*s)

Draw text.

[ft8xx\_copro\_cmd](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee)

void ft8xx\_copro\_cmd(uint32\_t cmd)

Execute a display list command by co-processor engine.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_copro.h](ft8xx__copro_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
