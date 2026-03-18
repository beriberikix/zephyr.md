---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kinetis__sim_8h.html
original_path: doxygen/html/kinetis__sim_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kinetis\_sim.h File Reference

[Go to the source code of this file.](kinetis__sim_8h_source.md)

| Macros | |
| --- | --- |
| #define | [KINETIS\_SIM\_CORESYS\_CLK](#a0684d47ba26fd4908fa10bb2c40894b9)   0 |
| #define | [KINETIS\_SIM\_PLATFORM\_CLK](#ac083afde9dfc09d77be337ccec8613c6)   1 |
| #define | [KINETIS\_SIM\_BUS\_CLK](#a2fde3204425c877c1e0e409cac4d3f2c)   2 |
| #define | [KINETIS\_SIM\_FAST\_PERIPHERAL\_CLK](#a3b8468dcc04b28ec8c8e08c80848d9a1)   5 |
| #define | [KINETIS\_SIM\_LPO\_CLK](#aa1c209ae87c6971eb0f737baa768516b)   19 |
| #define | [KINETIS\_SIM\_DMAMUX\_CLK](#a504e4baefda2add7e54aac44cadb428d)   [KINETIS\_SIM\_BUS\_CLK](#a2fde3204425c877c1e0e409cac4d3f2c) |
| #define | [KINETIS\_SIM\_DMA\_CLK](#a236c80919664e4d41414beab57ec1fea)   [KINETIS\_SIM\_CORESYS\_CLK](#a0684d47ba26fd4908fa10bb2c40894b9) |
| #define | [KINETIS\_SIM\_SIM\_SOPT7](#aef35b68542fef8df938f4a7238299ae7)   7 |
| #define | [KINETIS\_SIM\_PLLFLLSEL\_MCGFLLCLK](#a02aa044f83da5dca652327df3dbce5d8)   0 |
| #define | [KINETIS\_SIM\_PLLFLLSEL\_MCGPLLCLK](#a3b28905b525cde569f367e17274accf8)   1 |
| #define | [KINETIS\_SIM\_PLLFLLSEL\_IRC48MHZ](#a04fcbc9ade8eb94807dbf78922ee3177)   3 |
| #define | [KINETIS\_SIM\_ER32KSEL\_OSC32KCLK](#ad107887d2ac9f8fed754889548a7ee92)   0 |
| #define | [KINETIS\_SIM\_ER32KSEL\_RTC](#a12c607155d49c7a83fce3619e63048a8)   2 |
| #define | [KINETIS\_SIM\_ER32KSEL\_LPO1KHZ](#a31926a82e92f3e7f9df4438661bdc381)   3 |
| #define | [KINETIS\_SIM\_ENET\_CLK](#a0ccfe586de3c6ab968c1440263fcd858)   4321 |
| #define | [KINETIS\_SIM\_ENET\_1588\_CLK](#a61306e18fafbb5491db88600ab03ded5)   4322 |

## Macro Definition Documentation

## [◆ ](#a2fde3204425c877c1e0e409cac4d3f2c)KINETIS\_SIM\_BUS\_CLK

| #define KINETIS\_SIM\_BUS\_CLK   2 |
| --- |

## [◆ ](#a0684d47ba26fd4908fa10bb2c40894b9)KINETIS\_SIM\_CORESYS\_CLK

| #define KINETIS\_SIM\_CORESYS\_CLK   0 |
| --- |

## [◆ ](#a236c80919664e4d41414beab57ec1fea)KINETIS\_SIM\_DMA\_CLK

| #define KINETIS\_SIM\_DMA\_CLK   [KINETIS\_SIM\_CORESYS\_CLK](#a0684d47ba26fd4908fa10bb2c40894b9) |
| --- |

## [◆ ](#a504e4baefda2add7e54aac44cadb428d)KINETIS\_SIM\_DMAMUX\_CLK

| #define KINETIS\_SIM\_DMAMUX\_CLK   [KINETIS\_SIM\_BUS\_CLK](#a2fde3204425c877c1e0e409cac4d3f2c) |
| --- |

## [◆ ](#a61306e18fafbb5491db88600ab03ded5)KINETIS\_SIM\_ENET\_1588\_CLK

| #define KINETIS\_SIM\_ENET\_1588\_CLK   4322 |
| --- |

## [◆ ](#a0ccfe586de3c6ab968c1440263fcd858)KINETIS\_SIM\_ENET\_CLK

| #define KINETIS\_SIM\_ENET\_CLK   4321 |
| --- |

## [◆ ](#a31926a82e92f3e7f9df4438661bdc381)KINETIS\_SIM\_ER32KSEL\_LPO1KHZ

| #define KINETIS\_SIM\_ER32KSEL\_LPO1KHZ   3 |
| --- |

## [◆ ](#ad107887d2ac9f8fed754889548a7ee92)KINETIS\_SIM\_ER32KSEL\_OSC32KCLK

| #define KINETIS\_SIM\_ER32KSEL\_OSC32KCLK   0 |
| --- |

## [◆ ](#a12c607155d49c7a83fce3619e63048a8)KINETIS\_SIM\_ER32KSEL\_RTC

| #define KINETIS\_SIM\_ER32KSEL\_RTC   2 |
| --- |

## [◆ ](#a3b8468dcc04b28ec8c8e08c80848d9a1)KINETIS\_SIM\_FAST\_PERIPHERAL\_CLK

| #define KINETIS\_SIM\_FAST\_PERIPHERAL\_CLK   5 |
| --- |

## [◆ ](#aa1c209ae87c6971eb0f737baa768516b)KINETIS\_SIM\_LPO\_CLK

| #define KINETIS\_SIM\_LPO\_CLK   19 |
| --- |

## [◆ ](#ac083afde9dfc09d77be337ccec8613c6)KINETIS\_SIM\_PLATFORM\_CLK

| #define KINETIS\_SIM\_PLATFORM\_CLK   1 |
| --- |

## [◆ ](#a04fcbc9ade8eb94807dbf78922ee3177)KINETIS\_SIM\_PLLFLLSEL\_IRC48MHZ

| #define KINETIS\_SIM\_PLLFLLSEL\_IRC48MHZ   3 |
| --- |

## [◆ ](#a02aa044f83da5dca652327df3dbce5d8)KINETIS\_SIM\_PLLFLLSEL\_MCGFLLCLK

| #define KINETIS\_SIM\_PLLFLLSEL\_MCGFLLCLK   0 |
| --- |

## [◆ ](#a3b28905b525cde569f367e17274accf8)KINETIS\_SIM\_PLLFLLSEL\_MCGPLLCLK

| #define KINETIS\_SIM\_PLLFLLSEL\_MCGPLLCLK   1 |
| --- |

## [◆ ](#aef35b68542fef8df938f4a7238299ae7)KINETIS\_SIM\_SIM\_SOPT7

| #define KINETIS\_SIM\_SIM\_SOPT7   7 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [kinetis\_sim.h](kinetis__sim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
