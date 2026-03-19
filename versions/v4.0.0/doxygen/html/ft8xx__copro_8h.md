---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx__copro_8h.html
original_path: doxygen/html/ft8xx__copro_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_copro.h File Reference

FT8XX coprocessor functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](ft8xx__copro_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FT8XX\_OPT\_3D](group__ft8xx__copro.md#ga304badab7bd34208d499b199080fb557)   0 |
|  | Co-processor widget is drawn in 3D effect. |
| #define | [FT8XX\_OPT\_RGB565](group__ft8xx__copro.md#ga3a79c1128bdb9fe094843688691a085c)   0 |
|  | Co-processor option to decode the JPEG image to RGB565 format. |
| #define | [FT8XX\_OPT\_MONO](group__ft8xx__copro.md#ga415760ddf94db71ee9a504300bac4661)   1 |
|  | Co-processor option to decode the JPEG image to L8 format, i.e., monochrome. |
| #define | [FT8XX\_OPT\_NODL](group__ft8xx__copro.md#gacc953470460b083c0b8bd9ebbc8ed03b)   2 |
|  | No display list commands generated for bitmap decoded from JPEG image. |
| #define | [FT8XX\_OPT\_FLAT](group__ft8xx__copro.md#ga160b331fb401eec023e0992c6f4c6331)   256 |
|  | Co-processor widget is drawn without 3D effect. |
| #define | [FT8XX\_OPT\_SIGNED](group__ft8xx__copro.md#ga5a58155896cdb2d0f1693d203706ce93)   256 |
|  | The number is treated as 32 bit signed integer. |
| #define | [FT8XX\_OPT\_CENTERX](group__ft8xx__copro.md#gac2d1ccbb99eaa032ed9d39fc01d32c66)   512 |
|  | Co-processor widget centers horizontally. |
| #define | [FT8XX\_OPT\_CENTERY](group__ft8xx__copro.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a)   1024 |
|  | Co-processor widget centers vertically. |
| #define | [FT8XX\_OPT\_CENTER](group__ft8xx__copro.md#ga013968a6bf9534265c897ab1f4018eb0)   1536 |
|  | Co-processor widget centers horizontally and vertically. |
| #define | [FT8XX\_OPT\_RIGHTX](group__ft8xx__copro.md#gac864c155bc2121bf8d3954e1ed8dbb7e)   2048 |
|  | The label on the Coprocessor widget is right justified. |
| #define | [FT8XX\_OPT\_NOBACK](group__ft8xx__copro.md#gacb08df4fac256cbf808b133d4159aa29)   4096 |
|  | Co-processor widget has no background drawn. |
| #define | [FT8XX\_OPT\_NOTICKS](group__ft8xx__copro.md#ga50f4fac88e4f4b558450adcda33dae93)   8192 |
|  | Co-processor clock widget is drawn without hour ticks. |
| #define | [FT8XX\_OPT\_NOHM](group__ft8xx__copro.md#ga79938d9c1193d44a527ca8c158117a86)   16384 |
|  | Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn. |
| #define | [FT8XX\_OPT\_NOPOINTER](group__ft8xx__copro.md#ga1a9838a862ec166bfe95d64144b9a052)   16384 |
|  | The Co-processor gauge has no pointer. |
| #define | [FT8XX\_OPT\_NOSECS](group__ft8xx__copro.md#ga6416f4282d2c483d2adba8c1215ab638)   32768 |
|  | Co-processor clock widget is drawn without seconds hand. |
| #define | [FT8XX\_OPT\_NOHANDS](group__ft8xx__copro.md#gade56de46694ca420460c1ceb26a33120)   49152 |
|  | Co-processor clock widget is drawn without hour, minutes and seconds hands. |

| Functions | |
| --- | --- |
| void | [ft8xx\_copro\_cmd](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Execute a display list command by co-processor engine. |
| void | [ft8xx\_copro\_cmd\_dlstart](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602) (void) |
|  | Start a new display list. |
| void | [ft8xx\_copro\_cmd\_swap](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929) (void) |
|  | Swap the current display list. |
| void | [ft8xx\_copro\_cmd\_text](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Draw text. |
| void | [ft8xx\_copro\_cmd\_number](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n) |
|  | Draw a decimal number. |
| void | [ft8xx\_copro\_cmd\_calibrate](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Execute the touch screen calibration routine. |

## Detailed Description

FT8XX coprocessor functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_copro.h](ft8xx__copro_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
