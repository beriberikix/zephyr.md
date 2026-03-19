---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ast10x0__clock_8h.html
original_path: doxygen/html/ast10x0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ast10x0\_clock.h File Reference

[Go to the source code of this file.](ast10x0__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9)   (0) |
| #define | [ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f)   (32) |
| #define | [ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d)   (64) |
| #define | [ASPEED\_CLK\_MCLK](#a3b37b31cba1a39e9d641c9f97ed32a28)   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 0) |
| #define | [ASPEED\_CLK\_USB\_DEVICE](#a165a6862679163abf282c0eb67e94def)   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 7) |
| #define | [ASPEED\_CLK\_YCLK](#a74d307980b4aa1dcb0ad90c306d15448)   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 13) |
| #define | [ASPEED\_CLK\_LCLK](#a52b659f282d1bf17122e8d6cc4cb89ac)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 0) |
| #define | [ASPEED\_CLK\_ESPI](#a601a84a17a471f751ae260374e39d66c)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 1) |
| #define | [ASPEED\_CLK\_REFCLK](#a27b8f6c3f72aebbf0559e85bd43e8641)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 2) |
| #define | [ASPEED\_CLK\_LHCCLK](#a75e3ccf175dbbfd553b0fe4bf4c8b63c)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 5) |
| #define | [ASPEED\_CLK\_RSACLK](#ab111e4dccb054d2b38c7acdda204ed19)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 6) |
| #define | [ASPEED\_CLK\_I3C0](#a410403d49c1bb708d71bf8247dbdc0e2)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 8) |
| #define | [ASPEED\_CLK\_I3C1](#ae7e435ba8c54b91d2f0b4d244fe8c052)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 9) |
| #define | [ASPEED\_CLK\_I3C2](#a1d189580a83d1167491ca053ef22b7fa)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 10) |
| #define | [ASPEED\_CLK\_I3C3](#a755ef8cfe6c78e01a06113f2b3e78204)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 11) |
| #define | [ASPEED\_CLK\_UART1](#a3d645146fe6742ed4d56ece6265fc6e2)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 16) |
| #define | [ASPEED\_CLK\_UART2](#a2c86ad831ad2d720edd3a9c63ad9acb3)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 17) |
| #define | [ASPEED\_CLK\_UART3](#a8d1afc478750f1746f2bd280ec6aff74)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 18) |
| #define | [ASPEED\_CLK\_UART4](#a5eb5ae4923c04c925b8763330ead0062)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 19) |
| #define | [ASPEED\_CLK\_MAC](#ade068404e397460803ec43eac6bf2380)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 20) |
| #define | [ASPEED\_CLK\_UART6](#ab834e06518b4054ade5ad5f43971c262)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 22) |
| #define | [ASPEED\_CLK\_UART7](#a607209d0fc0eae0b7e16f9caf2e9266f)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 23) |
| #define | [ASPEED\_CLK\_UART8](#adde45b96aa4dfcacfe9830f0d18c08e7)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 24) |
| #define | [ASPEED\_CLK\_UART9](#a5a99a566a02c34e68a56d2953e885457)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 25) |
| #define | [ASPEED\_CLK\_UART10](#afc181e59d2e1deca6af256d34d57e25c)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 26) |
| #define | [ASPEED\_CLK\_UART11](#adbd0d3f7c91d1281e785363095a48077)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 27) |
| #define | [ASPEED\_CLK\_UART12](#a7d6f4a6d172b574d4a28ff4b6777df69)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 28) |
| #define | [ASPEED\_CLK\_UART13](#ad2e83af2a4c95f211c9d5f65fb1991d7)   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 29) |
| #define | [ASPEED\_CLK\_PCLK](#a9f9b71ba0ba43b4cebf27a077fd596ed)   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 0) |
| #define | [ASPEED\_CLK\_HCLK](#abc5d16026e5da37c2a09fdef727fe7ce)   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 1) |
| #define | [ASPEED\_CLK\_UART5](#a9a92e4a9a3024f13c9ba2c73a73c2ddb)   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 2) |

## Macro Definition Documentation

## [◆ ](#a601a84a17a471f751ae260374e39d66c)ASPEED\_CLK\_ESPI

| #define ASPEED\_CLK\_ESPI   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 1) |
| --- |

## [◆ ](#a037d8cf6fe0039675c6d0b3ace4421d9)ASPEED\_CLK\_GRP\_0\_OFFSET

| #define ASPEED\_CLK\_GRP\_0\_OFFSET   (0) |
| --- |

## [◆ ](#ab37a99b66163853d3e6ca8f4a9f4d57f)ASPEED\_CLK\_GRP\_1\_OFFSET

| #define ASPEED\_CLK\_GRP\_1\_OFFSET   (32) |
| --- |

## [◆ ](#a608fc420936e936d77ef94427419184d)ASPEED\_CLK\_GRP\_2\_OFFSET

| #define ASPEED\_CLK\_GRP\_2\_OFFSET   (64) |
| --- |

## [◆ ](#abc5d16026e5da37c2a09fdef727fe7ce)ASPEED\_CLK\_HCLK

| #define ASPEED\_CLK\_HCLK   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 1) |
| --- |

## [◆ ](#a410403d49c1bb708d71bf8247dbdc0e2)ASPEED\_CLK\_I3C0

| #define ASPEED\_CLK\_I3C0   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 8) |
| --- |

## [◆ ](#ae7e435ba8c54b91d2f0b4d244fe8c052)ASPEED\_CLK\_I3C1

| #define ASPEED\_CLK\_I3C1   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 9) |
| --- |

## [◆ ](#a1d189580a83d1167491ca053ef22b7fa)ASPEED\_CLK\_I3C2

| #define ASPEED\_CLK\_I3C2   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 10) |
| --- |

## [◆ ](#a755ef8cfe6c78e01a06113f2b3e78204)ASPEED\_CLK\_I3C3

| #define ASPEED\_CLK\_I3C3   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 11) |
| --- |

## [◆ ](#a52b659f282d1bf17122e8d6cc4cb89ac)ASPEED\_CLK\_LCLK

| #define ASPEED\_CLK\_LCLK   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 0) |
| --- |

## [◆ ](#a75e3ccf175dbbfd553b0fe4bf4c8b63c)ASPEED\_CLK\_LHCCLK

| #define ASPEED\_CLK\_LHCCLK   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 5) |
| --- |

## [◆ ](#ade068404e397460803ec43eac6bf2380)ASPEED\_CLK\_MAC

| #define ASPEED\_CLK\_MAC   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 20) |
| --- |

## [◆ ](#a3b37b31cba1a39e9d641c9f97ed32a28)ASPEED\_CLK\_MCLK

| #define ASPEED\_CLK\_MCLK   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 0) |
| --- |

## [◆ ](#a9f9b71ba0ba43b4cebf27a077fd596ed)ASPEED\_CLK\_PCLK

| #define ASPEED\_CLK\_PCLK   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 0) |
| --- |

## [◆ ](#a27b8f6c3f72aebbf0559e85bd43e8641)ASPEED\_CLK\_REFCLK

| #define ASPEED\_CLK\_REFCLK   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 2) |
| --- |

## [◆ ](#ab111e4dccb054d2b38c7acdda204ed19)ASPEED\_CLK\_RSACLK

| #define ASPEED\_CLK\_RSACLK   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 6) |
| --- |

## [◆ ](#a3d645146fe6742ed4d56ece6265fc6e2)ASPEED\_CLK\_UART1

| #define ASPEED\_CLK\_UART1   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 16) |
| --- |

## [◆ ](#afc181e59d2e1deca6af256d34d57e25c)ASPEED\_CLK\_UART10

| #define ASPEED\_CLK\_UART10   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 26) |
| --- |

## [◆ ](#adbd0d3f7c91d1281e785363095a48077)ASPEED\_CLK\_UART11

| #define ASPEED\_CLK\_UART11   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 27) |
| --- |

## [◆ ](#a7d6f4a6d172b574d4a28ff4b6777df69)ASPEED\_CLK\_UART12

| #define ASPEED\_CLK\_UART12   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 28) |
| --- |

## [◆ ](#ad2e83af2a4c95f211c9d5f65fb1991d7)ASPEED\_CLK\_UART13

| #define ASPEED\_CLK\_UART13   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 29) |
| --- |

## [◆ ](#a2c86ad831ad2d720edd3a9c63ad9acb3)ASPEED\_CLK\_UART2

| #define ASPEED\_CLK\_UART2   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 17) |
| --- |

## [◆ ](#a8d1afc478750f1746f2bd280ec6aff74)ASPEED\_CLK\_UART3

| #define ASPEED\_CLK\_UART3   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 18) |
| --- |

## [◆ ](#a5eb5ae4923c04c925b8763330ead0062)ASPEED\_CLK\_UART4

| #define ASPEED\_CLK\_UART4   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 19) |
| --- |

## [◆ ](#a9a92e4a9a3024f13c9ba2c73a73c2ddb)ASPEED\_CLK\_UART5

| #define ASPEED\_CLK\_UART5   ([ASPEED\_CLK\_GRP\_2\_OFFSET](#a608fc420936e936d77ef94427419184d) + 2) |
| --- |

## [◆ ](#ab834e06518b4054ade5ad5f43971c262)ASPEED\_CLK\_UART6

| #define ASPEED\_CLK\_UART6   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 22) |
| --- |

## [◆ ](#a607209d0fc0eae0b7e16f9caf2e9266f)ASPEED\_CLK\_UART7

| #define ASPEED\_CLK\_UART7   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 23) |
| --- |

## [◆ ](#adde45b96aa4dfcacfe9830f0d18c08e7)ASPEED\_CLK\_UART8

| #define ASPEED\_CLK\_UART8   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 24) |
| --- |

## [◆ ](#a5a99a566a02c34e68a56d2953e885457)ASPEED\_CLK\_UART9

| #define ASPEED\_CLK\_UART9   ([ASPEED\_CLK\_GRP\_1\_OFFSET](#ab37a99b66163853d3e6ca8f4a9f4d57f) + 25) |
| --- |

## [◆ ](#a165a6862679163abf282c0eb67e94def)ASPEED\_CLK\_USB\_DEVICE

| #define ASPEED\_CLK\_USB\_DEVICE   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 7) |
| --- |

## [◆ ](#a74d307980b4aa1dcb0ad90c306d15448)ASPEED\_CLK\_YCLK

| #define ASPEED\_CLK\_YCLK   ([ASPEED\_CLK\_GRP\_0\_OFFSET](#a037d8cf6fe0039675c6d0b3ace4421d9) + 13) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ast10x0\_clock.h](ast10x0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
