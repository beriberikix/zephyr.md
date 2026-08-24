---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/microchip__sam__pmc_8h.html
original_path: doxygen/html/microchip__sam__pmc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

microchip\_sam\_pmc.h File Reference

[Go to the source code of this file.](microchip__sam__pmc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PMC\_TYPE\_CORE](#a2b1fc195c22e06289bfe1955086d42dd)   0 |
| #define | [PMC\_TYPE\_SYSTEM](#a5745534115e0096059c693406055573b)   1 |
| #define | [PMC\_TYPE\_PERIPHERAL](#a60e3c44dd11ea566f718972995374019)   2 |
| #define | [PMC\_TYPE\_GCK](#ab998f9758b4c3e603ca20bfd262f3327)   3 |
| #define | [PMC\_TYPE\_PROGRAMMABLE](#a7fc62d1954529184d102cb7585973fb5)   4 |
| #define | [PMC\_SLOW](#a854154863c97c71801ff4684a407e237)   0 |
| #define | [PMC\_MCK](#a2d6b8cadcedb6522e88264b09da73d7d)   1 |
| #define | [PMC\_UTMI](#a5a54df8ddd142b8e6ed67b72d7bab401)   2 |
| #define | [PMC\_MAIN](#a072e63108608597768994a00b21d955d)   3 |
| #define | [PMC\_CPUPLL](#a1f28358ab0151521b3121ff4d57ca700)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 1) |
| #define | [PMC\_SYSPLL](#a996cc1d45786ee499ccc23355a05db37)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 2) |
| #define | [PMC\_DDRPLL](#ab8a01a73ca6952f39be1ed7a3791feb3)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 3) |
| #define | [PMC\_IMGPLL](#a441d7b97d246e52e75bf348ac3b90c76)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 4) |
| #define | [PMC\_BAUDPLL](#aae1ca2d39f81fa9fc9094619ce3b19c4)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 5) |
| #define | [PMC\_AUDIOPMCPLL](#af716bb9061d8d6a5a96ade2c0102f4c0)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 6) |
| #define | [PMC\_AUDIOIOPLL](#a2374e2a9b2baf97196cb9900ab41f2b1)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 7) |
| #define | [PMC\_ETHPLL](#a2707b5189d0c0a383e8765aa4dc0c702)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 8) |
| #define | [PMC\_CPU](#a79ea6d33c03bc659e505516f10dd4909)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 9) |
| #define | [PMC\_MCK1](#a373a027bd6c4c22ba1bb333109c4b4b5)   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 10) |
| #define | [UTMI1](#acf4ff24d07135ac8ba9095f4b0e8202f)   0 |
| #define | [UTMI2](#a536bbd6e8cf19611a64b62a6173bebae)   1 |
| #define | [UTMI3](#ab950647ecce7b6ed9a94770434a9504c)   2 |

## Macro Definition Documentation

## [◆ ](#a2374e2a9b2baf97196cb9900ab41f2b1)PMC\_AUDIOIOPLL

| #define PMC\_AUDIOIOPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 7) |
| --- |

## [◆ ](#af716bb9061d8d6a5a96ade2c0102f4c0)PMC\_AUDIOPMCPLL

| #define PMC\_AUDIOPMCPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 6) |
| --- |

## [◆ ](#aae1ca2d39f81fa9fc9094619ce3b19c4)PMC\_BAUDPLL

| #define PMC\_BAUDPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 5) |
| --- |

## [◆ ](#a79ea6d33c03bc659e505516f10dd4909)PMC\_CPU

| #define PMC\_CPU   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 9) |
| --- |

## [◆ ](#a1f28358ab0151521b3121ff4d57ca700)PMC\_CPUPLL

| #define PMC\_CPUPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 1) |
| --- |

## [◆ ](#ab8a01a73ca6952f39be1ed7a3791feb3)PMC\_DDRPLL

| #define PMC\_DDRPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 3) |
| --- |

## [◆ ](#a2707b5189d0c0a383e8765aa4dc0c702)PMC\_ETHPLL

| #define PMC\_ETHPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 8) |
| --- |

## [◆ ](#a441d7b97d246e52e75bf348ac3b90c76)PMC\_IMGPLL

| #define PMC\_IMGPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 4) |
| --- |

## [◆ ](#a072e63108608597768994a00b21d955d)PMC\_MAIN

| #define PMC\_MAIN   3 |
| --- |

## [◆ ](#a2d6b8cadcedb6522e88264b09da73d7d)PMC\_MCK

| #define PMC\_MCK   1 |
| --- |

## [◆ ](#a373a027bd6c4c22ba1bb333109c4b4b5)PMC\_MCK1

| #define PMC\_MCK1   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 10) |
| --- |

## [◆ ](#a854154863c97c71801ff4684a407e237)PMC\_SLOW

| #define PMC\_SLOW   0 |
| --- |

## [◆ ](#a996cc1d45786ee499ccc23355a05db37)PMC\_SYSPLL

| #define PMC\_SYSPLL   ([PMC\_MAIN](#a072e63108608597768994a00b21d955d) + 2) |
| --- |

## [◆ ](#a2b1fc195c22e06289bfe1955086d42dd)PMC\_TYPE\_CORE

| #define PMC\_TYPE\_CORE   0 |
| --- |

## [◆ ](#ab998f9758b4c3e603ca20bfd262f3327)PMC\_TYPE\_GCK

| #define PMC\_TYPE\_GCK   3 |
| --- |

## [◆ ](#a60e3c44dd11ea566f718972995374019)PMC\_TYPE\_PERIPHERAL

| #define PMC\_TYPE\_PERIPHERAL   2 |
| --- |

## [◆ ](#a7fc62d1954529184d102cb7585973fb5)PMC\_TYPE\_PROGRAMMABLE

| #define PMC\_TYPE\_PROGRAMMABLE   4 |
| --- |

## [◆ ](#a5745534115e0096059c693406055573b)PMC\_TYPE\_SYSTEM

| #define PMC\_TYPE\_SYSTEM   1 |
| --- |

## [◆ ](#a5a54df8ddd142b8e6ed67b72d7bab401)PMC\_UTMI

| #define PMC\_UTMI   2 |
| --- |

## [◆ ](#acf4ff24d07135ac8ba9095f4b0e8202f)UTMI1

| #define UTMI1   0 |
| --- |

## [◆ ](#a536bbd6e8cf19611a64b62a6173bebae)UTMI2

| #define UTMI2   1 |
| --- |

## [◆ ](#ab950647ecce7b6ed9a94770434a9504c)UTMI3

| #define UTMI3   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [microchip\_sam\_pmc.h](microchip__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
