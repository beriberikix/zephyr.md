---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ft8xx__copro.html
original_path: doxygen/html/group__ft8xx__copro.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx co-processor

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [FT8xx driver APIs](group__ft8xx__interface.md)

FT8xx co-processor engine functions.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [FT8XX\_OPT\_3D](#ga304badab7bd34208d499b199080fb557)   0 |
|  | Co-processor widget is drawn in 3D effect. |
| #define | [FT8XX\_OPT\_RGB565](#ga3a79c1128bdb9fe094843688691a085c)   0 |
|  | Co-processor option to decode the JPEG image to RGB565 format. |
| #define | [FT8XX\_OPT\_MONO](#ga415760ddf94db71ee9a504300bac4661)   1 |
|  | Co-processor option to decode the JPEG image to L8 format, i.e., monochrome. |
| #define | [FT8XX\_OPT\_NODL](#gacc953470460b083c0b8bd9ebbc8ed03b)   2 |
|  | No display list commands generated for bitmap decoded from JPEG image. |
| #define | [FT8XX\_OPT\_FLAT](#ga160b331fb401eec023e0992c6f4c6331)   256 |
|  | Co-processor widget is drawn without 3D effect. |
| #define | [FT8XX\_OPT\_SIGNED](#ga5a58155896cdb2d0f1693d203706ce93)   256 |
|  | The number is treated as 32 bit signed integer. |
| #define | [FT8XX\_OPT\_CENTERX](#gac2d1ccbb99eaa032ed9d39fc01d32c66)   512 |
|  | Co-processor widget centers horizontally. |
| #define | [FT8XX\_OPT\_CENTERY](#ga65b3a1e29ae425b2f1c3e66b4ea1449a)   1024 |
|  | Co-processor widget centers vertically. |
| #define | [FT8XX\_OPT\_CENTER](#ga013968a6bf9534265c897ab1f4018eb0)   1536 |
|  | Co-processor widget centers horizontally and vertically. |
| #define | [FT8XX\_OPT\_RIGHTX](#gac864c155bc2121bf8d3954e1ed8dbb7e)   2048 |
|  | The label on the Coprocessor widget is right justified. |
| #define | [FT8XX\_OPT\_NOBACK](#gacb08df4fac256cbf808b133d4159aa29)   4096 |
|  | Co-processor widget has no background drawn. |
| #define | [FT8XX\_OPT\_NOTICKS](#ga50f4fac88e4f4b558450adcda33dae93)   8192 |
|  | Co-processor clock widget is drawn without hour ticks. |
| #define | [FT8XX\_OPT\_NOHM](#ga79938d9c1193d44a527ca8c158117a86)   16384 |
|  | Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn. |
| #define | [FT8XX\_OPT\_NOPOINTER](#ga1a9838a862ec166bfe95d64144b9a052)   16384 |
|  | The Co-processor gauge has no pointer. |
| #define | [FT8XX\_OPT\_NOSECS](#ga6416f4282d2c483d2adba8c1215ab638)   32768 |
|  | Co-processor clock widget is drawn without seconds hand. |
| #define | [FT8XX\_OPT\_NOHANDS](#gade56de46694ca420460c1ceb26a33120)   49152 |
|  | Co-processor clock widget is drawn without hour, minutes and seconds hands. |

| Functions | |
| --- | --- |
| void | [ft8xx\_copro\_cmd](#gae64451b001196d2062d2d0a940dadcee) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Execute a display list command by co-processor engine. |
| void | [ft8xx\_copro\_cmd\_dlstart](#ga5ac02fe4d5d3af941b3eca7bc18a9602) (void) |
|  | Start a new display list. |
| void | [ft8xx\_copro\_cmd\_swap](#gaa6df956e01bc2919c147f6eafb839929) (void) |
|  | Swap the current display list. |
| void | [ft8xx\_copro\_cmd\_text](#gac5cf196bb23196642415b73cb377e345) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Draw text. |
| void | [ft8xx\_copro\_cmd\_number](#ga6193d853b2105a120619343ccaa62c0c) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n) |
|  | Draw a decimal number. |
| void | [ft8xx\_copro\_cmd\_calibrate](#ga770a86ae67d3d30135bc3c48ab4e888b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Execute the touch screen calibration routine. |

## Detailed Description

FT8xx co-processor engine functions.

## Macro Definition Documentation

## [◆ ](#ga304badab7bd34208d499b199080fb557)FT8XX\_OPT\_3D

| #define FT8XX\_OPT\_3D   0 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget is drawn in 3D effect.

## [◆ ](#ga013968a6bf9534265c897ab1f4018eb0)FT8XX\_OPT\_CENTER

| #define FT8XX\_OPT\_CENTER   1536 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget centers horizontally and vertically.

## [◆ ](#gac2d1ccbb99eaa032ed9d39fc01d32c66)FT8XX\_OPT\_CENTERX

| #define FT8XX\_OPT\_CENTERX   512 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget centers horizontally.

## [◆ ](#ga65b3a1e29ae425b2f1c3e66b4ea1449a)FT8XX\_OPT\_CENTERY

| #define FT8XX\_OPT\_CENTERY   1024 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget centers vertically.

## [◆ ](#ga160b331fb401eec023e0992c6f4c6331)FT8XX\_OPT\_FLAT

| #define FT8XX\_OPT\_FLAT   256 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget is drawn without 3D effect.

## [◆ ](#ga415760ddf94db71ee9a504300bac4661)FT8XX\_OPT\_MONO

| #define FT8XX\_OPT\_MONO   1 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor option to decode the JPEG image to L8 format, i.e., monochrome.

## [◆ ](#gacb08df4fac256cbf808b133d4159aa29)FT8XX\_OPT\_NOBACK

| #define FT8XX\_OPT\_NOBACK   4096 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor widget has no background drawn.

## [◆ ](#gacc953470460b083c0b8bd9ebbc8ed03b)FT8XX\_OPT\_NODL

| #define FT8XX\_OPT\_NODL   2 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

No display list commands generated for bitmap decoded from JPEG image.

## [◆ ](#gade56de46694ca420460c1ceb26a33120)FT8XX\_OPT\_NOHANDS

| #define FT8XX\_OPT\_NOHANDS   49152 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor clock widget is drawn without hour, minutes and seconds hands.

## [◆ ](#ga79938d9c1193d44a527ca8c158117a86)FT8XX\_OPT\_NOHM

| #define FT8XX\_OPT\_NOHM   16384 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn.

## [◆ ](#ga1a9838a862ec166bfe95d64144b9a052)FT8XX\_OPT\_NOPOINTER

| #define FT8XX\_OPT\_NOPOINTER   16384 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

The Co-processor gauge has no pointer.

## [◆ ](#ga6416f4282d2c483d2adba8c1215ab638)FT8XX\_OPT\_NOSECS

| #define FT8XX\_OPT\_NOSECS   32768 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor clock widget is drawn without seconds hand.

## [◆ ](#ga50f4fac88e4f4b558450adcda33dae93)FT8XX\_OPT\_NOTICKS

| #define FT8XX\_OPT\_NOTICKS   8192 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor clock widget is drawn without hour ticks.

Gauge widget is drawn without major and minor ticks.

## [◆ ](#ga3a79c1128bdb9fe094843688691a085c)FT8XX\_OPT\_RGB565

| #define FT8XX\_OPT\_RGB565   0 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Co-processor option to decode the JPEG image to RGB565 format.

## [◆ ](#gac864c155bc2121bf8d3954e1ed8dbb7e)FT8XX\_OPT\_RIGHTX

| #define FT8XX\_OPT\_RIGHTX   2048 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

The label on the Coprocessor widget is right justified.

## [◆ ](#ga5a58155896cdb2d0f1693d203706ce93)FT8XX\_OPT\_SIGNED

| #define FT8XX\_OPT\_SIGNED   256 |
| --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

The number is treated as 32 bit signed integer.

## Function Documentation

## [◆ ](#gae64451b001196d2062d2d0a940dadcee)ft8xx\_copro\_cmd()

| void ft8xx\_copro\_cmd | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cmd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Execute a display list command by co-processor engine.

Parameters
:   | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Display list command to execute |
    | --- | --- |

## [◆ ](#ga770a86ae67d3d30135bc3c48ab4e888b)ft8xx\_copro\_cmd\_calibrate()

| void ft8xx\_copro\_cmd\_calibrate | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Execute the touch screen calibration routine.

The calibration procedure collects three touches from the touch screen, then computes and loads an appropriate matrix into REG\_TOUCH\_TRANSFORM\_A-F. To use it, create a display list and then use CMD\_CALIBRATE. The co-processor engine overlays the touch targets on the current display list, gathers the calibration input and updates REG\_TOUCH\_TRANSFORM\_A-F.

Parameters
:   | result | Calibration result, written with 0 on failure of calibration |
    | --- | --- |

## [◆ ](#ga5ac02fe4d5d3af941b3eca7bc18a9602)ft8xx\_copro\_cmd\_dlstart()

| void ft8xx\_copro\_cmd\_dlstart | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Start a new display list.

## [◆ ](#ga6193d853b2105a120619343ccaa62c0c)ft8xx\_copro\_cmd\_number()

| void ft8xx\_copro\_cmd\_number | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *font*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *options*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *n* ) |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Draw a decimal number.

By default (`x`, `y`) is the top-left pixel of the text. [FT8XX\_OPT\_CENTERX](#gac2d1ccbb99eaa032ed9d39fc01d32c66) centers the text horizontally, [FT8XX\_OPT\_CENTERY](#ga65b3a1e29ae425b2f1c3e66b4ea1449a) centers it vertically. [FT8XX\_OPT\_CENTER](#ga013968a6bf9534265c897ab1f4018eb0) centers the text in both directions. [FT8XX\_OPT\_RIGHTX](#gac864c155bc2121bf8d3954e1ed8dbb7e) right-justifies the text, so that the `x` is the rightmost pixel. By default the number is displayed with no leading zeroes, but if a width 1-9 is specified in the `options`, then the number is padded if necessary with leading zeroes so that it has the given width. If [FT8XX\_OPT\_SIGNED](#ga5a58155896cdb2d0f1693d203706ce93) is given, the number is treated as signed, and prefixed by a minus sign if negative.

Parameters
:   | x | x-coordinate of text base, in pixels |
    | --- | --- |
    | y | y-coordinate of text base, in pixels |
    | font | Font to use for text, 0-31. 16-31 are ROM fonts |
    | options | Options to apply |
    | n | The number to display. |

## [◆ ](#gaa6df956e01bc2919c147f6eafb839929)ft8xx\_copro\_cmd\_swap()

| void ft8xx\_copro\_cmd\_swap | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Swap the current display list.

## [◆ ](#gac5cf196bb23196642415b73cb377e345)ft8xx\_copro\_cmd\_text()

| void ft8xx\_copro\_cmd\_text | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *font*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *options*, |
|  |  | const char \* | *s* ) |

`#include <[ft8xx_copro.h](ft8xx__copro_8h.md)>`

Draw text.

By default (`x`, `y`) is the top-left pixel of the text and the value of `options` is zero. [FT8XX\_OPT\_CENTERX](#gac2d1ccbb99eaa032ed9d39fc01d32c66) centers the text horizontally, [FT8XX\_OPT\_CENTERY](#ga65b3a1e29ae425b2f1c3e66b4ea1449a) centers it vertically. [FT8XX\_OPT\_CENTER](#ga013968a6bf9534265c897ab1f4018eb0) centers the text in both directions. [FT8XX\_OPT\_RIGHTX](#gac864c155bc2121bf8d3954e1ed8dbb7e) right-justifies the text, so that the `x` is the rightmost pixel.

Parameters
:   | x | x-coordinate of text base, in pixels |
    | --- | --- |
    | y | y-coordinate of text base, in pixels |
    | font | Font to use for text, 0-31. 16-31 are ROM fonts |
    | options | Options to apply |
    | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Character string to display, terminated with a null character |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
