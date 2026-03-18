---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ioapic_8h.html
original_path: doxygen/html/ioapic_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ioapic.h File Reference

[Go to the source code of this file.](ioapic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IOAPIC\_INT\_MASK](#afe15b2cc2000b86362e9fb0026ec4f32)   0x00010000 |
| #define | [IOAPIC\_TRIGGER\_MASK](#ac66c78294836c1327cbbf6bd5111282a)   0x00008000 |
| #define | [IOAPIC\_LEVEL](#afee8dca23363d2f9b785a21f6b5c4080)   0x00008000 |
| #define | [IOAPIC\_EDGE](#a1d4cfd6f7d4aba0bc773e4d53333bb1d)   0x00000000 |
| #define | [IOAPIC\_REMOTE](#a850d24fefdc5a1b0f92922a504eb43b5)   0x00004000 |
| #define | [IOAPIC\_POLARITY\_MASK](#a3d009fe11441cfd8ad68f91d764f447e)   0x00002000 |
| #define | [IOAPIC\_LOW](#a23ec31db6b36b64ad0d04c3caf2815f2)   0x00002000 |
| #define | [IOAPIC\_HIGH](#a1677a4eb3aab3bea022e9ea2bf547888)   0x00000000 |
| #define | [IOAPIC\_LOGICAL](#af9cdfb74e72ef22f3c51f7b9a8b3afe9)   0x00000800 |
| #define | [IOAPIC\_PHYSICAL](#aa4ef248efabc134ecad5f00fa34fa456)   0x00000000 |
| #define | [IOAPIC\_DELIVERY\_MODE\_MASK](#a1d1756d4b243d2235d58ffa2caf4e5fc)   0x00000700 |
| #define | [IOAPIC\_FIXED](#af84ed8737d1822ded039bb975b8f5bc9)   0x00000000 |
| #define | [IOAPIC\_LOWEST](#add788ae14ffab1b56a831c2a39d2a617)   0x00000100 |
| #define | [IOAPIC\_SMI](#aa01949d30064c45959fdfefcedd916f1)   0x00000200 |
| #define | [IOAPIC\_NMI](#a3e2f1930e2f92cff455b98b76c6c4397)   0x00000400 |
| #define | [IOAPIC\_INIT](#a16099bc753e03fdf31f6aa35f01cf2fa)   0x00000500 |
| #define | [IOAPIC\_EXTINT](#aeff81f0a6186d2b188c7109baa670c52)   0x00000700 |

## Macro Definition Documentation

## [◆ ](#a1d1756d4b243d2235d58ffa2caf4e5fc)IOAPIC\_DELIVERY\_MODE\_MASK

| #define IOAPIC\_DELIVERY\_MODE\_MASK   0x00000700 |
| --- |

## [◆ ](#a1d4cfd6f7d4aba0bc773e4d53333bb1d)IOAPIC\_EDGE

| #define IOAPIC\_EDGE   0x00000000 |
| --- |

## [◆ ](#aeff81f0a6186d2b188c7109baa670c52)IOAPIC\_EXTINT

| #define IOAPIC\_EXTINT   0x00000700 |
| --- |

## [◆ ](#af84ed8737d1822ded039bb975b8f5bc9)IOAPIC\_FIXED

| #define IOAPIC\_FIXED   0x00000000 |
| --- |

## [◆ ](#a1677a4eb3aab3bea022e9ea2bf547888)IOAPIC\_HIGH

| #define IOAPIC\_HIGH   0x00000000 |
| --- |

## [◆ ](#a16099bc753e03fdf31f6aa35f01cf2fa)IOAPIC\_INIT

| #define IOAPIC\_INIT   0x00000500 |
| --- |

## [◆ ](#afe15b2cc2000b86362e9fb0026ec4f32)IOAPIC\_INT\_MASK

| #define IOAPIC\_INT\_MASK   0x00010000 |
| --- |

## [◆ ](#afee8dca23363d2f9b785a21f6b5c4080)IOAPIC\_LEVEL

| #define IOAPIC\_LEVEL   0x00008000 |
| --- |

## [◆ ](#af9cdfb74e72ef22f3c51f7b9a8b3afe9)IOAPIC\_LOGICAL

| #define IOAPIC\_LOGICAL   0x00000800 |
| --- |

## [◆ ](#a23ec31db6b36b64ad0d04c3caf2815f2)IOAPIC\_LOW

| #define IOAPIC\_LOW   0x00002000 |
| --- |

## [◆ ](#add788ae14ffab1b56a831c2a39d2a617)IOAPIC\_LOWEST

| #define IOAPIC\_LOWEST   0x00000100 |
| --- |

## [◆ ](#a3e2f1930e2f92cff455b98b76c6c4397)IOAPIC\_NMI

| #define IOAPIC\_NMI   0x00000400 |
| --- |

## [◆ ](#aa4ef248efabc134ecad5f00fa34fa456)IOAPIC\_PHYSICAL

| #define IOAPIC\_PHYSICAL   0x00000000 |
| --- |

## [◆ ](#a3d009fe11441cfd8ad68f91d764f447e)IOAPIC\_POLARITY\_MASK

| #define IOAPIC\_POLARITY\_MASK   0x00002000 |
| --- |

## [◆ ](#a850d24fefdc5a1b0f92922a504eb43b5)IOAPIC\_REMOTE

| #define IOAPIC\_REMOTE   0x00004000 |
| --- |

## [◆ ](#aa01949d30064c45959fdfefcedd916f1)IOAPIC\_SMI

| #define IOAPIC\_SMI   0x00000200 |
| --- |

## [◆ ](#ac66c78294836c1327cbbf6bd5111282a)IOAPIC\_TRIGGER\_MASK

| #define IOAPIC\_TRIGGER\_MASK   0x00008000 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [ioapic.h](ioapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
