---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gd32__dma_8h.html
original_path: doxygen/html/gd32__dma_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32\_dma.h File Reference

[Go to the source code of this file.](gd32__dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(val) |
| #define | [GD32\_DMA\_MEMORY\_TO\_MEMORY](#ac66caaa6fd58e811ca1173afffb6eee0)   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(0) |
| #define | [GD32\_DMA\_MEMORY\_TO\_PERIPH](#a133ee2eba1696a8a88e553899b42215d)   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(1) |
| #define | [GD32\_DMA\_PERIPH\_TO\_MEMORY](#a6db732bda87b175e5594e47120b50fc4)   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(2) |
| #define | [GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#ad0abcd3eb77751438884eb14376a4249)(val) |
| #define | [GD32\_DMA\_NO\_PERIPH\_ADDR\_INC](#a3190a823bcefea6dea75b22751437469)   [GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#ad0abcd3eb77751438884eb14376a4249)(0) |
| #define | [GD32\_DMA\_PERIPH\_ADDR\_INC](#a886f483d28ecb076d76cab9807dbd9ae)   [GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#ad0abcd3eb77751438884eb14376a4249)(1) |
| #define | [GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC](#ae55d797279e2483a9de15ddb250d9c01)(val) |
| #define | [GD32\_DMA\_NO\_MEMORY\_ADDR\_INC](#a45eb42e1d19daa3d40831c93ad0ba0a0)   [GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC](#ae55d797279e2483a9de15ddb250d9c01)(0) |
| #define | [GD32\_DMA\_MEMORY\_ADDR\_INC](#a1dfa4abe03789cb06229e071479a68d3)   [GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC](#ae55d797279e2483a9de15ddb250d9c01)(1) |
| #define | [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(val) |
| #define | [GD32\_DMA\_PERIPH\_WIDTH\_8BIT](#a43f8444f017382621385497e88bc28eb)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(0) |
| #define | [GD32\_DMA\_PERIPH\_WIDTH\_16BIT](#acd17760bf971b4efae57cbb7413c7993)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(1) |
| #define | [GD32\_DMA\_PERIPH\_WIDTH\_32BIT](#ac8071edf3e9c36beb96f8a2f41f9b297)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(2) |
| #define | [GD32\_DMA\_CH\_CFG\_MEMORY\_WIDTH](#a7e46c2dd560ad05b3ef2d49e8e934634)(val) |
| #define | [GD32\_DMA\_MEMORY\_WIDTH\_8BIT](#aa02a7efc2fca50aa800f39e94b3759b4)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(0) |
| #define | [GD32\_DMA\_MEMORY\_WIDTH\_16BIT](#a0787852dc6f450f4eff8eea7be3a6b89)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(1) |
| #define | [GD32\_DMA\_MEMORY\_WIDTH\_32BIT](#a2d77c7ecc44a7c91dfecbf94044ec5a0)   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(2) |
| #define | [GD32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a0eecb55bada0630383167b56d82c4892)(val) |
| #define | [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(val) |
| #define | [GD32\_DMA\_PRIORITY\_LOW](#ae68917539c8744ddcfbad918e69db56e)   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(0) |
| #define | [GD32\_DMA\_PRIORITY\_MEDIUM](#a548fac07f1b1c5cdd61670178c7ecc8b)   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(1) |
| #define | [GD32\_DMA\_PRIORITY\_HIGH](#a17a02cccc8980fd5a273f251b4e02ea6)   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(2) |
| #define | [GD32\_DMA\_PRIORITY\_VERY\_HIGH](#ad6e846a9a5b52f0838c1b214ba39b6b3)   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(3) |

## Macro Definition Documentation

## [◆ ](#ae2a0d7ee983ce7229d00424fc9bd561a)GD32\_DMA\_CH\_CFG\_DIRECTION

| #define GD32\_DMA\_CH\_CFG\_DIRECTION | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 6)

## [◆ ](#ae55d797279e2483a9de15ddb250d9c01)GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC

| #define GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 10)

## [◆ ](#a7e46c2dd560ad05b3ef2d49e8e934634)GD32\_DMA\_CH\_CFG\_MEMORY\_WIDTH

| #define GD32\_DMA\_CH\_CFG\_MEMORY\_WIDTH | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 13)

## [◆ ](#ad0abcd3eb77751438884eb14376a4249)GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC

| #define GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 9)

## [◆ ](#a0eecb55bada0630383167b56d82c4892)GD32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED

| #define GD32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 15)

## [◆ ](#a7ee975a1a1338f3fcbf9779a4f66ec7c)GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH

| #define GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 11)

## [◆ ](#a7a95cc521b5445314d9d64528d885724)GD32\_DMA\_CH\_CFG\_PRIORITY

| #define GD32\_DMA\_CH\_CFG\_PRIORITY | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 16)

## [◆ ](#a1dfa4abe03789cb06229e071479a68d3)GD32\_DMA\_MEMORY\_ADDR\_INC

| #define GD32\_DMA\_MEMORY\_ADDR\_INC   [GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC](#ae55d797279e2483a9de15ddb250d9c01)(1) |
| --- |

## [◆ ](#ac66caaa6fd58e811ca1173afffb6eee0)GD32\_DMA\_MEMORY\_TO\_MEMORY

| #define GD32\_DMA\_MEMORY\_TO\_MEMORY   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(0) |
| --- |

## [◆ ](#a133ee2eba1696a8a88e553899b42215d)GD32\_DMA\_MEMORY\_TO\_PERIPH

| #define GD32\_DMA\_MEMORY\_TO\_PERIPH   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(1) |
| --- |

## [◆ ](#a0787852dc6f450f4eff8eea7be3a6b89)GD32\_DMA\_MEMORY\_WIDTH\_16BIT

| #define GD32\_DMA\_MEMORY\_WIDTH\_16BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(1) |
| --- |

## [◆ ](#a2d77c7ecc44a7c91dfecbf94044ec5a0)GD32\_DMA\_MEMORY\_WIDTH\_32BIT

| #define GD32\_DMA\_MEMORY\_WIDTH\_32BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(2) |
| --- |

## [◆ ](#aa02a7efc2fca50aa800f39e94b3759b4)GD32\_DMA\_MEMORY\_WIDTH\_8BIT

| #define GD32\_DMA\_MEMORY\_WIDTH\_8BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(0) |
| --- |

## [◆ ](#a45eb42e1d19daa3d40831c93ad0ba0a0)GD32\_DMA\_NO\_MEMORY\_ADDR\_INC

| #define GD32\_DMA\_NO\_MEMORY\_ADDR\_INC   [GD32\_DMA\_CH\_CFG\_MEMORY\_ADDR\_INC](#ae55d797279e2483a9de15ddb250d9c01)(0) |
| --- |

## [◆ ](#a3190a823bcefea6dea75b22751437469)GD32\_DMA\_NO\_PERIPH\_ADDR\_INC

| #define GD32\_DMA\_NO\_PERIPH\_ADDR\_INC   [GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#ad0abcd3eb77751438884eb14376a4249)(0) |
| --- |

## [◆ ](#a886f483d28ecb076d76cab9807dbd9ae)GD32\_DMA\_PERIPH\_ADDR\_INC

| #define GD32\_DMA\_PERIPH\_ADDR\_INC   [GD32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#ad0abcd3eb77751438884eb14376a4249)(1) |
| --- |

## [◆ ](#a6db732bda87b175e5594e47120b50fc4)GD32\_DMA\_PERIPH\_TO\_MEMORY

| #define GD32\_DMA\_PERIPH\_TO\_MEMORY   [GD32\_DMA\_CH\_CFG\_DIRECTION](#ae2a0d7ee983ce7229d00424fc9bd561a)(2) |
| --- |

## [◆ ](#acd17760bf971b4efae57cbb7413c7993)GD32\_DMA\_PERIPH\_WIDTH\_16BIT

| #define GD32\_DMA\_PERIPH\_WIDTH\_16BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(1) |
| --- |

## [◆ ](#ac8071edf3e9c36beb96f8a2f41f9b297)GD32\_DMA\_PERIPH\_WIDTH\_32BIT

| #define GD32\_DMA\_PERIPH\_WIDTH\_32BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(2) |
| --- |

## [◆ ](#a43f8444f017382621385497e88bc28eb)GD32\_DMA\_PERIPH\_WIDTH\_8BIT

| #define GD32\_DMA\_PERIPH\_WIDTH\_8BIT   [GD32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a7ee975a1a1338f3fcbf9779a4f66ec7c)(0) |
| --- |

## [◆ ](#a17a02cccc8980fd5a273f251b4e02ea6)GD32\_DMA\_PRIORITY\_HIGH

| #define GD32\_DMA\_PRIORITY\_HIGH   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(2) |
| --- |

## [◆ ](#ae68917539c8744ddcfbad918e69db56e)GD32\_DMA\_PRIORITY\_LOW

| #define GD32\_DMA\_PRIORITY\_LOW   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(0) |
| --- |

## [◆ ](#a548fac07f1b1c5cdd61670178c7ecc8b)GD32\_DMA\_PRIORITY\_MEDIUM

| #define GD32\_DMA\_PRIORITY\_MEDIUM   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(1) |
| --- |

## [◆ ](#ad6e846a9a5b52f0838c1b214ba39b6b3)GD32\_DMA\_PRIORITY\_VERY\_HIGH

| #define GD32\_DMA\_PRIORITY\_VERY\_HIGH   [GD32\_DMA\_CH\_CFG\_PRIORITY](#a7a95cc521b5445314d9d64528d885724)(3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [gd32\_dma.h](gd32__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
