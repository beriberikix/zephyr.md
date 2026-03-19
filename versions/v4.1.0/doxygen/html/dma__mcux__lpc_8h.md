---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dma__mcux__lpc_8h.html
original_path: doxygen/html/dma__mcux__lpc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_lpc.h File Reference

[Go to the source code of this file.](dma__mcux__lpc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LPC\_DMA\_PERIPH\_REQ\_EN](#a4d1f2a9bd076336bce0fd5e535cfc580)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [LPC\_DMA\_HWTRIG\_EN](#a738b7a640e92bd64a95172b236f10544)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [LPC\_DMA\_TRIGPOL\_HIGH\_RISING](#a6c9492c7479a678b11a54e28f7bc3df8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [LPC\_DMA\_TRIGTYPE\_LEVEL](#a0f5ed8f5fbe87d13e4f21e0a3018ab64)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [LPC\_DMA\_TRIGBURST](#a4d9e1928d741d1950384f7ab83600ee2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [LPC\_DMA\_BURSTPOWER](#acfa31048d38fa62b9cb3681886472609)(pwr) |
| #define | [LPC\_DMA\_GET\_BURSTPOWER](#a0e9624882342df7556aa29a8f7ee74f3)(slot) |

## Macro Definition Documentation

## [◆ ](#acfa31048d38fa62b9cb3681886472609)LPC\_DMA\_BURSTPOWER

| #define LPC\_DMA\_BURSTPOWER | ( |  | *pwr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pwr) & 0x7) << 5)

## [◆ ](#a0e9624882342df7556aa29a8f7ee74f3)LPC\_DMA\_GET\_BURSTPOWER

| #define LPC\_DMA\_GET\_BURSTPOWER | ( |  | *slot* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((slot) & 0xE0) >> 5)

## [◆ ](#a738b7a640e92bd64a95172b236f10544)LPC\_DMA\_HWTRIG\_EN

| #define LPC\_DMA\_HWTRIG\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4d1f2a9bd076336bce0fd5e535cfc580)LPC\_DMA\_PERIPH\_REQ\_EN

| #define LPC\_DMA\_PERIPH\_REQ\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a4d9e1928d741d1950384f7ab83600ee2)LPC\_DMA\_TRIGBURST

| #define LPC\_DMA\_TRIGBURST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a6c9492c7479a678b11a54e28f7bc3df8)LPC\_DMA\_TRIGPOL\_HIGH\_RISING

| #define LPC\_DMA\_TRIGPOL\_HIGH\_RISING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a0f5ed8f5fbe87d13e4f21e0a3018ab64)LPC\_DMA\_TRIGTYPE\_LEVEL

| #define LPC\_DMA\_TRIGTYPE\_LEVEL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_lpc.h](dma__mcux__lpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
