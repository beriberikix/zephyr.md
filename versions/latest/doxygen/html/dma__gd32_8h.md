---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__gd32_8h.html
original_path: doxygen/html/dma__gd32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_gd32.h File Reference

[Go to the source code of this file.](dma__gd32_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GD32\_DMA\_CONFIG\_DIRECTION](#a0bfc50da9b666c382ca00e53612c08e8)(config) |
| #define | [GD32\_DMA\_CONFIG\_PERIPH\_ADDR\_INC](#a12c9387cd798e45a97a025d892fee048)(config) |
| #define | [GD32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC](#a6048bfaf2929f8ace82bfdf910a85224)(config) |
| #define | [GD32\_DMA\_CONFIG\_PERIPH\_WIDTH](#ae09b2bd2a0abf46f92afbc93c8f0b1f2)(config) |
| #define | [GD32\_DMA\_CONFIG\_MEMORY\_WIDTH](#af6d346ff11af7445ef216ff86943de58)(config) |
| #define | [GD32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED](#a3c35875713e5534e753068e77c4a8796)(config) |
| #define | [GD32\_DMA\_CONFIG\_PRIORITY](#acfb3e4c8ef6bed1484348f72be5a2fb9)(config) |
| #define | [GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD](#af41c61ae669ce510d514ccb9ff6204f9)(threshold) |

## Macro Definition Documentation

## [◆ ](#a0bfc50da9b666c382ca00e53612c08e8)GD32\_DMA\_CONFIG\_DIRECTION

| #define GD32\_DMA\_CONFIG\_DIRECTION | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 6) & 0x3)

## [◆ ](#a6048bfaf2929f8ace82bfdf910a85224)GD32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC

| #define GD32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 10) & 0x1)

## [◆ ](#af6d346ff11af7445ef216ff86943de58)GD32\_DMA\_CONFIG\_MEMORY\_WIDTH

| #define GD32\_DMA\_CONFIG\_MEMORY\_WIDTH | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 13) & 0x3)

## [◆ ](#a12c9387cd798e45a97a025d892fee048)GD32\_DMA\_CONFIG\_PERIPH\_ADDR\_INC

| #define GD32\_DMA\_CONFIG\_PERIPH\_ADDR\_INC | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 9) & 0x1)

## [◆ ](#ae09b2bd2a0abf46f92afbc93c8f0b1f2)GD32\_DMA\_CONFIG\_PERIPH\_WIDTH

| #define GD32\_DMA\_CONFIG\_PERIPH\_WIDTH | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 11) & 0x3)

## [◆ ](#a3c35875713e5534e753068e77c4a8796)GD32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED

| #define GD32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 15) & 0x1)

## [◆ ](#acfb3e4c8ef6bed1484348f72be5a2fb9)GD32\_DMA\_CONFIG\_PRIORITY

| #define GD32\_DMA\_CONFIG\_PRIORITY | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 16) & 0x3)

## [◆ ](#af41c61ae669ce510d514ccb9ff6204f9)GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD

| #define GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD | ( |  | *threshold* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(threshold & 0x3)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_gd32.h](dma__gd32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
