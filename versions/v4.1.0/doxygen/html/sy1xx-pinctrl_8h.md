---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sy1xx-pinctrl_8h.html
original_path: doxygen/html/sy1xx-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sy1xx-pinctrl.h File Reference

[Go to the source code of this file.](sy1xx-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SY1XX\_PAD](#ad75005e085a8960d58f6d092b36a3457)(pad) |
| #define | [SY1XX\_UART0\_PAD\_CFG0](#adc483e38c6c02d891a22b9bf84935b56)   0x0020 |
| #define | [SY1XX\_UART1\_PAD\_CFG0](#a055d907bbf5efca0c1aa99ebd22702ed)   0x0024 |
| #define | [SY1XX\_UART2\_PAD\_CFG0](#add2c72f1fbe994a823a20ca3201edafe)   0x0028 |
| #define | [SY1XX\_SPI0\_PAD\_CFG0](#a404e66d6cf88171347e3db0c3717157a)   0x002c |
| #define | [SY1XX\_SPI0\_PAD\_CFG1](#ae18b46685cdfd24b547632490ff10072)   0x0030 |
| #define | [SY1XX\_SPI1\_PAD\_CFG0](#a9bf78b4c068d29050c35c26a55fbc20c)   0x0034 |
| #define | [SY1XX\_SPI1\_PAD\_CFG1](#af4cf0968a02d32f9ac353a7326cc87f6)   0x0038 |
| #define | [SY1XX\_SPI2\_PAD\_CFG0](#a6eecae08e7eec2034789a71b59e993ae)   0x003c |
| #define | [SY1XX\_SPI2\_PAD\_CFG1](#aadd9f2a4ae588a04d9fb6ecdd0e23814)   0x0040 |
| #define | [SY1XX\_SPI3\_PAD\_CFG0](#a76f73bbaf1481d2635ef98eb3059cbcc)   0x0044 |
| #define | [SY1XX\_SPI3\_PAD\_CFG1](#ab2806c2b057c0e3fbf067f51a2c44f1a)   0x0048 |
| #define | [SY1XX\_SPI4\_PAD\_CFG0](#ab2fa82fdb2937f3609fa750cde52e31a)   0x004c |
| #define | [SY1XX\_SPI4\_PAD\_CFG1](#a8e75504deacf337c617a53edca490e0e)   0x0050 |
| #define | [SY1XX\_SPI5\_PAD\_CFG0](#ac7d17056cdeceb0e829ad72a06ef9d09)   0x0054 |
| #define | [SY1XX\_SPI5\_PAD\_CFG1](#a958f75d6c7419e2a9dba1c6577852696)   0x0058 |
| #define | [SY1XX\_SPI6\_PAD\_CFG0](#a4b2305ff3b154e1d3c0daf811059043f)   0x005c |
| #define | [SY1XX\_SPI6\_PAD\_CFG1](#a8e0105c1d92748e3e51c333be3b919b0)   0x0060 |
| #define | [SY1XX\_I2C0\_PAD\_CFG0](#a01bf7ff6920aca87fcda6b2a5136d989)   0x0100 |
| #define | [SY1XX\_I2C1\_PAD\_CFG0](#ae7b8ecc3c5082bbddd99f9de460c8537)   0x0104 |
| #define | [SY1XX\_I2C2\_PAD\_CFG0](#a35a4e2514b7237892e772e4d9f0e5c0d)   0x0108 |
| #define | [SY1XX\_I2C3\_PAD\_CFG0](#a1b911fab051ea7108e0c273f5a491bde)   0x010c |
| #define | [SY1XX\_GPIO0\_PAD\_CFG0](#ab4c601da01a0e39445cf963e07ac29e0)   0x0110 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG1](#a5159756f8ea829e08ba3b5a4533c7fc0)   0x0114 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG2](#a57de6bad22780defb68c4ee449450c36)   0x0118 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG3](#ac6fa6736e2d16b2a8f7fdebb335b5105)   0x011c |
| #define | [SY1XX\_GPIO0\_PAD\_CFG4](#a5da7b457738900d954c54d00e05ba187)   0x0120 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG5](#a3891aced0a6f74c1756916dba97bcfcb)   0x0124 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG6](#ae1e986b4c50e8cfb0b8e0a98ef1baea9)   0x0128 |
| #define | [SY1XX\_GPIO0\_PAD\_CFG7](#a4135e0f0c3d9c4157e9c253fdc739cf4)   0x012c |
| #define | [SY1XX\_RGMII0\_PAD\_CFG0](#a13cce7da530425788383e11b9f35b5ce)   0x0130 |
| #define | [SY1XX\_RGMII0\_PAD\_CFG1](#a06f53391cd6d71e86fa0736c089660b8)   0x0134 |
| #define | [SY1XX\_RGMII0\_PAD\_CFG2](#a2a57254b422b7248d3d1f7fa56fa3ffe)   0x0138 |
| #define | [SY1XX\_RGMII0\_PAD\_CFG3](#a2d1d2134971e68e70e23fe42f9f316d3)   0x013c |
| #define | [SY1XX\_CAN0\_PAD\_CFG0](#a7853e14b27de17f111a1a7edc94b6a67)   0x0140 |
| #define | [SY1XX\_I2S0\_PAD\_CFG0](#a92ed448d69e0232a2a16e364c8482d96)   0x0144 |
| #define | [SY1XX\_I2S1\_PAD\_CFG0](#a55234d106fcfe72c40dc8e6bf7026c76)   0x0148 |
| #define | [SY1XX\_I2S2\_PAD\_CFG0](#a2a9de099a9542907ed1ee1f79b52d98a)   0x014c |
| #define | [SY1XX\_I2S3\_PAD\_CFG0](#aeeec7f5df0f5a63c45e078d4eb11f3a0)   0x0150 |
| #define | [SY1XX\_HBUS0\_PAD\_CFG0](#a9a3d3cbbc4be0098c258b20c2dd70d6e)   0x0154 |
| #define | [SY1XX\_HBUS0\_PAD\_CFG1](#a9eac3698c460c2b97ca180af2327bdf4)   0x0158 |
| #define | [SY1XX\_HBUS0\_PAD\_CFG2](#a0ced8b047437b1b00b135f87557d46bd)   0x015c |
| #define | [SY1XX\_HBUS0\_PAD\_CFG3](#a2dca17d2f18be0dfe9146740c6e8fec3)   0x0160 |
| #define | [SY1XX\_QSPI0\_PAD\_CFG0](#a901d32212b2702f2d1a12e6627c805fe)   0x0164 |
| #define | [SY1XX\_QSPI0\_PAD\_CFG1](#aa473544922299dfa761d8594ddb7cedc)   0x0168 |

## Macro Definition Documentation

## [◆ ](#a7853e14b27de17f111a1a7edc94b6a67)SY1XX\_CAN0\_PAD\_CFG0

| #define SY1XX\_CAN0\_PAD\_CFG0   0x0140 |
| --- |

## [◆ ](#ab4c601da01a0e39445cf963e07ac29e0)SY1XX\_GPIO0\_PAD\_CFG0

| #define SY1XX\_GPIO0\_PAD\_CFG0   0x0110 |
| --- |

## [◆ ](#a5159756f8ea829e08ba3b5a4533c7fc0)SY1XX\_GPIO0\_PAD\_CFG1

| #define SY1XX\_GPIO0\_PAD\_CFG1   0x0114 |
| --- |

## [◆ ](#a57de6bad22780defb68c4ee449450c36)SY1XX\_GPIO0\_PAD\_CFG2

| #define SY1XX\_GPIO0\_PAD\_CFG2   0x0118 |
| --- |

## [◆ ](#ac6fa6736e2d16b2a8f7fdebb335b5105)SY1XX\_GPIO0\_PAD\_CFG3

| #define SY1XX\_GPIO0\_PAD\_CFG3   0x011c |
| --- |

## [◆ ](#a5da7b457738900d954c54d00e05ba187)SY1XX\_GPIO0\_PAD\_CFG4

| #define SY1XX\_GPIO0\_PAD\_CFG4   0x0120 |
| --- |

## [◆ ](#a3891aced0a6f74c1756916dba97bcfcb)SY1XX\_GPIO0\_PAD\_CFG5

| #define SY1XX\_GPIO0\_PAD\_CFG5   0x0124 |
| --- |

## [◆ ](#ae1e986b4c50e8cfb0b8e0a98ef1baea9)SY1XX\_GPIO0\_PAD\_CFG6

| #define SY1XX\_GPIO0\_PAD\_CFG6   0x0128 |
| --- |

## [◆ ](#a4135e0f0c3d9c4157e9c253fdc739cf4)SY1XX\_GPIO0\_PAD\_CFG7

| #define SY1XX\_GPIO0\_PAD\_CFG7   0x012c |
| --- |

## [◆ ](#a9a3d3cbbc4be0098c258b20c2dd70d6e)SY1XX\_HBUS0\_PAD\_CFG0

| #define SY1XX\_HBUS0\_PAD\_CFG0   0x0154 |
| --- |

## [◆ ](#a9eac3698c460c2b97ca180af2327bdf4)SY1XX\_HBUS0\_PAD\_CFG1

| #define SY1XX\_HBUS0\_PAD\_CFG1   0x0158 |
| --- |

## [◆ ](#a0ced8b047437b1b00b135f87557d46bd)SY1XX\_HBUS0\_PAD\_CFG2

| #define SY1XX\_HBUS0\_PAD\_CFG2   0x015c |
| --- |

## [◆ ](#a2dca17d2f18be0dfe9146740c6e8fec3)SY1XX\_HBUS0\_PAD\_CFG3

| #define SY1XX\_HBUS0\_PAD\_CFG3   0x0160 |
| --- |

## [◆ ](#a01bf7ff6920aca87fcda6b2a5136d989)SY1XX\_I2C0\_PAD\_CFG0

| #define SY1XX\_I2C0\_PAD\_CFG0   0x0100 |
| --- |

## [◆ ](#ae7b8ecc3c5082bbddd99f9de460c8537)SY1XX\_I2C1\_PAD\_CFG0

| #define SY1XX\_I2C1\_PAD\_CFG0   0x0104 |
| --- |

## [◆ ](#a35a4e2514b7237892e772e4d9f0e5c0d)SY1XX\_I2C2\_PAD\_CFG0

| #define SY1XX\_I2C2\_PAD\_CFG0   0x0108 |
| --- |

## [◆ ](#a1b911fab051ea7108e0c273f5a491bde)SY1XX\_I2C3\_PAD\_CFG0

| #define SY1XX\_I2C3\_PAD\_CFG0   0x010c |
| --- |

## [◆ ](#a92ed448d69e0232a2a16e364c8482d96)SY1XX\_I2S0\_PAD\_CFG0

| #define SY1XX\_I2S0\_PAD\_CFG0   0x0144 |
| --- |

## [◆ ](#a55234d106fcfe72c40dc8e6bf7026c76)SY1XX\_I2S1\_PAD\_CFG0

| #define SY1XX\_I2S1\_PAD\_CFG0   0x0148 |
| --- |

## [◆ ](#a2a9de099a9542907ed1ee1f79b52d98a)SY1XX\_I2S2\_PAD\_CFG0

| #define SY1XX\_I2S2\_PAD\_CFG0   0x014c |
| --- |

## [◆ ](#aeeec7f5df0f5a63c45e078d4eb11f3a0)SY1XX\_I2S3\_PAD\_CFG0

| #define SY1XX\_I2S3\_PAD\_CFG0   0x0150 |
| --- |

## [◆ ](#ad75005e085a8960d58f6d092b36a3457)SY1XX\_PAD

| #define SY1XX\_PAD | ( |  | *pad* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(pad \* 8)

## [◆ ](#a901d32212b2702f2d1a12e6627c805fe)SY1XX\_QSPI0\_PAD\_CFG0

| #define SY1XX\_QSPI0\_PAD\_CFG0   0x0164 |
| --- |

## [◆ ](#aa473544922299dfa761d8594ddb7cedc)SY1XX\_QSPI0\_PAD\_CFG1

| #define SY1XX\_QSPI0\_PAD\_CFG1   0x0168 |
| --- |

## [◆ ](#a13cce7da530425788383e11b9f35b5ce)SY1XX\_RGMII0\_PAD\_CFG0

| #define SY1XX\_RGMII0\_PAD\_CFG0   0x0130 |
| --- |

## [◆ ](#a06f53391cd6d71e86fa0736c089660b8)SY1XX\_RGMII0\_PAD\_CFG1

| #define SY1XX\_RGMII0\_PAD\_CFG1   0x0134 |
| --- |

## [◆ ](#a2a57254b422b7248d3d1f7fa56fa3ffe)SY1XX\_RGMII0\_PAD\_CFG2

| #define SY1XX\_RGMII0\_PAD\_CFG2   0x0138 |
| --- |

## [◆ ](#a2d1d2134971e68e70e23fe42f9f316d3)SY1XX\_RGMII0\_PAD\_CFG3

| #define SY1XX\_RGMII0\_PAD\_CFG3   0x013c |
| --- |

## [◆ ](#a404e66d6cf88171347e3db0c3717157a)SY1XX\_SPI0\_PAD\_CFG0

| #define SY1XX\_SPI0\_PAD\_CFG0   0x002c |
| --- |

## [◆ ](#ae18b46685cdfd24b547632490ff10072)SY1XX\_SPI0\_PAD\_CFG1

| #define SY1XX\_SPI0\_PAD\_CFG1   0x0030 |
| --- |

## [◆ ](#a9bf78b4c068d29050c35c26a55fbc20c)SY1XX\_SPI1\_PAD\_CFG0

| #define SY1XX\_SPI1\_PAD\_CFG0   0x0034 |
| --- |

## [◆ ](#af4cf0968a02d32f9ac353a7326cc87f6)SY1XX\_SPI1\_PAD\_CFG1

| #define SY1XX\_SPI1\_PAD\_CFG1   0x0038 |
| --- |

## [◆ ](#a6eecae08e7eec2034789a71b59e993ae)SY1XX\_SPI2\_PAD\_CFG0

| #define SY1XX\_SPI2\_PAD\_CFG0   0x003c |
| --- |

## [◆ ](#aadd9f2a4ae588a04d9fb6ecdd0e23814)SY1XX\_SPI2\_PAD\_CFG1

| #define SY1XX\_SPI2\_PAD\_CFG1   0x0040 |
| --- |

## [◆ ](#a76f73bbaf1481d2635ef98eb3059cbcc)SY1XX\_SPI3\_PAD\_CFG0

| #define SY1XX\_SPI3\_PAD\_CFG0   0x0044 |
| --- |

## [◆ ](#ab2806c2b057c0e3fbf067f51a2c44f1a)SY1XX\_SPI3\_PAD\_CFG1

| #define SY1XX\_SPI3\_PAD\_CFG1   0x0048 |
| --- |

## [◆ ](#ab2fa82fdb2937f3609fa750cde52e31a)SY1XX\_SPI4\_PAD\_CFG0

| #define SY1XX\_SPI4\_PAD\_CFG0   0x004c |
| --- |

## [◆ ](#a8e75504deacf337c617a53edca490e0e)SY1XX\_SPI4\_PAD\_CFG1

| #define SY1XX\_SPI4\_PAD\_CFG1   0x0050 |
| --- |

## [◆ ](#ac7d17056cdeceb0e829ad72a06ef9d09)SY1XX\_SPI5\_PAD\_CFG0

| #define SY1XX\_SPI5\_PAD\_CFG0   0x0054 |
| --- |

## [◆ ](#a958f75d6c7419e2a9dba1c6577852696)SY1XX\_SPI5\_PAD\_CFG1

| #define SY1XX\_SPI5\_PAD\_CFG1   0x0058 |
| --- |

## [◆ ](#a4b2305ff3b154e1d3c0daf811059043f)SY1XX\_SPI6\_PAD\_CFG0

| #define SY1XX\_SPI6\_PAD\_CFG0   0x005c |
| --- |

## [◆ ](#a8e0105c1d92748e3e51c333be3b919b0)SY1XX\_SPI6\_PAD\_CFG1

| #define SY1XX\_SPI6\_PAD\_CFG1   0x0060 |
| --- |

## [◆ ](#adc483e38c6c02d891a22b9bf84935b56)SY1XX\_UART0\_PAD\_CFG0

| #define SY1XX\_UART0\_PAD\_CFG0   0x0020 |
| --- |

## [◆ ](#a055d907bbf5efca0c1aa99ebd22702ed)SY1XX\_UART1\_PAD\_CFG0

| #define SY1XX\_UART1\_PAD\_CFG0   0x0024 |
| --- |

## [◆ ](#add2c72f1fbe994a823a20ca3201edafe)SY1XX\_UART2\_PAD\_CFG0

| #define SY1XX\_UART2\_PAD\_CFG0   0x0028 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [sy1xx-pinctrl.h](sy1xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
