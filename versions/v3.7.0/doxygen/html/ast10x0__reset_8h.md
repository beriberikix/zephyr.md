---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ast10x0__reset_8h.html
original_path: doxygen/html/ast10x0__reset_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ast10x0\_reset.h File Reference

[Go to the source code of this file.](ast10x0__reset_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4)   (0) |
| #define | [ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8)   (32) |
| #define | [ASPEED\_RESET\_HACE](#a18a69d795a56e9077333b8d50fac36b0)   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 4) |
| #define | [ASPEED\_RESET\_USB](#aa63cefb88f641936f49389acaff04cbc)   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 3) |
| #define | [ASPEED\_RESET\_SRAM](#a54fbdaa166cf43dadb6a4d9777b581c3)   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 0) |
| #define | [ASPEED\_RESET\_UART4](#a19e6207b2212a0a58b8dc5c736748df1)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 31) |
| #define | [ASPEED\_RESET\_UART3](#a31e0692dd65c0adbe937daebee4477e2)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 30) |
| #define | [ASPEED\_RESET\_UART2](#a67087547f237de76d2ab1e9c2fd774f1)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 29) |
| #define | [ASPEED\_RESET\_UART1](#ab7429f58459c26d3cf637e4d9e764d67)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 28) |
| #define | [ASPEED\_RESET\_JTAG\_M0](#a2000c2cd1474abe2acf6716293f9a656)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 26) |
| #define | [ASPEED\_RESET\_ESPI](#a76bc43a3b57f919db372e4a79dc79b6f)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 25) |
| #define | [ASPEED\_RESET\_ADC](#ac8cad68c9911554194574d460d3f3814)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 23) |
| #define | [ASPEED\_RESET\_JTAG\_M1](#a8e20719b17e4f21c9673a7e740362b8e)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 22) |
| #define | [ASPEED\_RESET\_MAC](#ae546e699360d23e89ddba7310d637c8a)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 20) |
| #define | [ASPEED\_RESET\_I3C3](#a6eb1a65fee7f7d589e5c40acb06a59a7)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 11) |
| #define | [ASPEED\_RESET\_I3C2](#a3e76867407846a68533e1ef13e5612e0)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 10) |
| #define | [ASPEED\_RESET\_I3C1](#a792d63822aaf04bcf8670471c6f5cb5c)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 9) |
| #define | [ASPEED\_RESET\_I3C0](#a392ac704a9bbddcee588e9f52af8557e)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 8) |
| #define | [ASPEED\_RESET\_I3C](#a49e0d2e074659166bb20ad0a9a603435)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 7) |
| #define | [ASPEED\_RESET\_PWM\_TACH](#a49f53d3791ab6d0104837204c31eb1ad)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 5) |
| #define | [ASPEED\_RESET\_PECI](#a6cab61e115cc50636d3c5aa8b509f5c5)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 4) |
| #define | [ASPEED\_RESET\_MII](#abb494d1ccc9ab01d50fc21bb7c2eb7de)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 3) |
| #define | [ASPEED\_RESET\_I2C](#a235bf82edd62f2f72fb9de4efa11c7f9)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 2) |
| #define | [ASPEED\_RESET\_LPC](#a93f2fc81c8a9cdfee97548fb48281bed)   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 0) |

## Macro Definition Documentation

## [◆ ](#ac8cad68c9911554194574d460d3f3814)ASPEED\_RESET\_ADC

| #define ASPEED\_RESET\_ADC   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 23) |
| --- |

## [◆ ](#a76bc43a3b57f919db372e4a79dc79b6f)ASPEED\_RESET\_ESPI

| #define ASPEED\_RESET\_ESPI   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 25) |
| --- |

## [◆ ](#a58f51601c877080d344167774969c9b4)ASPEED\_RESET\_GRP\_0\_OFFSET

| #define ASPEED\_RESET\_GRP\_0\_OFFSET   (0) |
| --- |

## [◆ ](#af60cf3c19df220966fcc6aeb553677a8)ASPEED\_RESET\_GRP\_1\_OFFSET

| #define ASPEED\_RESET\_GRP\_1\_OFFSET   (32) |
| --- |

## [◆ ](#a18a69d795a56e9077333b8d50fac36b0)ASPEED\_RESET\_HACE

| #define ASPEED\_RESET\_HACE   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 4) |
| --- |

## [◆ ](#a235bf82edd62f2f72fb9de4efa11c7f9)ASPEED\_RESET\_I2C

| #define ASPEED\_RESET\_I2C   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 2) |
| --- |

## [◆ ](#a49e0d2e074659166bb20ad0a9a603435)ASPEED\_RESET\_I3C

| #define ASPEED\_RESET\_I3C   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 7) |
| --- |

## [◆ ](#a392ac704a9bbddcee588e9f52af8557e)ASPEED\_RESET\_I3C0

| #define ASPEED\_RESET\_I3C0   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 8) |
| --- |

## [◆ ](#a792d63822aaf04bcf8670471c6f5cb5c)ASPEED\_RESET\_I3C1

| #define ASPEED\_RESET\_I3C1   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 9) |
| --- |

## [◆ ](#a3e76867407846a68533e1ef13e5612e0)ASPEED\_RESET\_I3C2

| #define ASPEED\_RESET\_I3C2   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 10) |
| --- |

## [◆ ](#a6eb1a65fee7f7d589e5c40acb06a59a7)ASPEED\_RESET\_I3C3

| #define ASPEED\_RESET\_I3C3   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 11) |
| --- |

## [◆ ](#a2000c2cd1474abe2acf6716293f9a656)ASPEED\_RESET\_JTAG\_M0

| #define ASPEED\_RESET\_JTAG\_M0   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 26) |
| --- |

## [◆ ](#a8e20719b17e4f21c9673a7e740362b8e)ASPEED\_RESET\_JTAG\_M1

| #define ASPEED\_RESET\_JTAG\_M1   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 22) |
| --- |

## [◆ ](#a93f2fc81c8a9cdfee97548fb48281bed)ASPEED\_RESET\_LPC

| #define ASPEED\_RESET\_LPC   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 0) |
| --- |

## [◆ ](#ae546e699360d23e89ddba7310d637c8a)ASPEED\_RESET\_MAC

| #define ASPEED\_RESET\_MAC   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 20) |
| --- |

## [◆ ](#abb494d1ccc9ab01d50fc21bb7c2eb7de)ASPEED\_RESET\_MII

| #define ASPEED\_RESET\_MII   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 3) |
| --- |

## [◆ ](#a6cab61e115cc50636d3c5aa8b509f5c5)ASPEED\_RESET\_PECI

| #define ASPEED\_RESET\_PECI   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 4) |
| --- |

## [◆ ](#a49f53d3791ab6d0104837204c31eb1ad)ASPEED\_RESET\_PWM\_TACH

| #define ASPEED\_RESET\_PWM\_TACH   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 5) |
| --- |

## [◆ ](#a54fbdaa166cf43dadb6a4d9777b581c3)ASPEED\_RESET\_SRAM

| #define ASPEED\_RESET\_SRAM   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 0) |
| --- |

## [◆ ](#ab7429f58459c26d3cf637e4d9e764d67)ASPEED\_RESET\_UART1

| #define ASPEED\_RESET\_UART1   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 28) |
| --- |

## [◆ ](#a67087547f237de76d2ab1e9c2fd774f1)ASPEED\_RESET\_UART2

| #define ASPEED\_RESET\_UART2   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 29) |
| --- |

## [◆ ](#a31e0692dd65c0adbe937daebee4477e2)ASPEED\_RESET\_UART3

| #define ASPEED\_RESET\_UART3   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 30) |
| --- |

## [◆ ](#a19e6207b2212a0a58b8dc5c736748df1)ASPEED\_RESET\_UART4

| #define ASPEED\_RESET\_UART4   ([ASPEED\_RESET\_GRP\_1\_OFFSET](#af60cf3c19df220966fcc6aeb553677a8) + 31) |
| --- |

## [◆ ](#aa63cefb88f641936f49389acaff04cbc)ASPEED\_RESET\_USB

| #define ASPEED\_RESET\_USB   ([ASPEED\_RESET\_GRP\_0\_OFFSET](#a58f51601c877080d344167774969c9b4) + 3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [ast10x0\_reset.h](ast10x0__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
