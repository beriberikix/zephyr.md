---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0__clock_8h.html
original_path: doxygen/html/mspm0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0\_clock.h File Reference

[Go to the source code of this file.](mspm0__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(clk, bit) |
| #define | [MSPM0\_CLOCK\_PERIPH\_REG\_MASK](#a35877f69e306437ad9c8bea5ce455e11)(X) |
| #define | [MSPM0\_CLOCK\_SYSOSC](#a7df45c402fe047a5b5742c1dda57c6b5)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x0, 0x0) |
| #define | [MSPM0\_CLOCK\_LFCLK](#a1eef26082f2c6a8bf57cfb33a8ae7bca)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x1, 0x2) |
| #define | [MSPM0\_CLOCK\_MFCLK](#a3a35970f45fab5f68466339e14a5dcb1)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x2, 0x4) |
| #define | [MSPM0\_CLOCK\_BUSCLK](#a86b9a5c73fae48eace61eaddb94a7309)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x3, 0x8) |
| #define | [MSPM0\_CLOCK\_ULPCLK](#a9b1175ca378a2e7cfcda5f1ed0c0759a)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x4, 0x8) |
| #define | [MSPM0\_CLOCK\_MCLK](#aa8a1076dd4b533aa15b2ee838047546c)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x5, 0x8) |
| #define | [MSPM0\_CLOCK\_MFPCLK](#aa4b3c20657ab23b60f249d1f459829fd)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x6, 0x0) |
| #define | [MSPM0\_CLOCK\_CANCLK](#abb0965a9382c3e85ec418ac911766094)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x7, 0x0) |
| #define | [MSPM0\_CLOCK\_CLK\_OUT](#ad2a34eb409acbd0a2058434cdcf3c40c)   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x8, 0x0) |

## Macro Definition Documentation

## [◆ ](#a546f50fc3a86ada7e34d3c5b78526e5e)MSPM0\_CLOCK

| #define MSPM0\_CLOCK | ( |  | *clk*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

((clk << 8) | bit)

## [◆ ](#a86b9a5c73fae48eace61eaddb94a7309)MSPM0\_CLOCK\_BUSCLK

| #define MSPM0\_CLOCK\_BUSCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x3, 0x8) |
| --- |

## [◆ ](#abb0965a9382c3e85ec418ac911766094)MSPM0\_CLOCK\_CANCLK

| #define MSPM0\_CLOCK\_CANCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x7, 0x0) |
| --- |

## [◆ ](#ad2a34eb409acbd0a2058434cdcf3c40c)MSPM0\_CLOCK\_CLK\_OUT

| #define MSPM0\_CLOCK\_CLK\_OUT   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x8, 0x0) |
| --- |

## [◆ ](#a1eef26082f2c6a8bf57cfb33a8ae7bca)MSPM0\_CLOCK\_LFCLK

| #define MSPM0\_CLOCK\_LFCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x1, 0x2) |
| --- |

## [◆ ](#aa8a1076dd4b533aa15b2ee838047546c)MSPM0\_CLOCK\_MCLK

| #define MSPM0\_CLOCK\_MCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x5, 0x8) |
| --- |

## [◆ ](#a3a35970f45fab5f68466339e14a5dcb1)MSPM0\_CLOCK\_MFCLK

| #define MSPM0\_CLOCK\_MFCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x2, 0x4) |
| --- |

## [◆ ](#aa4b3c20657ab23b60f249d1f459829fd)MSPM0\_CLOCK\_MFPCLK

| #define MSPM0\_CLOCK\_MFPCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x6, 0x0) |
| --- |

## [◆ ](#a35877f69e306437ad9c8bea5ce455e11)MSPM0\_CLOCK\_PERIPH\_REG\_MASK

| #define MSPM0\_CLOCK\_PERIPH\_REG\_MASK | ( |  | *X* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(X & 0xFF)

## [◆ ](#a7df45c402fe047a5b5742c1dda57c6b5)MSPM0\_CLOCK\_SYSOSC

| #define MSPM0\_CLOCK\_SYSOSC   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x0, 0x0) |
| --- |

## [◆ ](#a9b1175ca378a2e7cfcda5f1ed0c0759a)MSPM0\_CLOCK\_ULPCLK

| #define MSPM0\_CLOCK\_ULPCLK   [MSPM0\_CLOCK](#a546f50fc3a86ada7e34d3c5b78526e5e)(0x4, 0x8) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mspm0\_clock.h](mspm0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
