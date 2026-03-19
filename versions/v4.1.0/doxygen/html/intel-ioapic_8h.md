---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intel-ioapic_8h.html
original_path: doxygen/html/intel-ioapic_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel-ioapic.h File Reference

[Go to the source code of this file.](intel-ioapic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7)   0x00008000 |
| #define | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc)   0x00000000 |
| #define | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)   0x00002000 |
| #define | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)   0x00000000 |
| #define | [IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231)   0x00000100 |
| #define | [IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b)   0x00000000 |
| #define | [IRQ\_TYPE\_LOWEST\_EDGE\_RISING](#a980bab4b0502b138f5fa8af9ca9833b4)   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| #define | [IRQ\_TYPE\_LOWEST\_EDGE\_FALLING](#a5a136f30dc5cb9f1b696751903b3fadd)   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| #define | [IRQ\_TYPE\_LOWEST\_LEVEL\_HIGH](#a9083a377fa943731dc24733933bae5d6)   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| #define | [IRQ\_TYPE\_LOWEST\_LEVEL\_LOW](#a15c26d56a818f5340c36117a429282a8)   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| #define | [IRQ\_TYPE\_FIXED\_EDGE\_RISING](#af1a9700940385a6aa6c9ff93fa834436)   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| #define | [IRQ\_TYPE\_FIXED\_EDGE\_FALLING](#a7f62c57495f357ec336cba12f1a12d61)   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| #define | [IRQ\_TYPE\_FIXED\_LEVEL\_HIGH](#a9a2bb018c589784edf36b204ba2daf48)   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| #define | [IRQ\_TYPE\_FIXED\_LEVEL\_LOW](#ab570a690df9e89e8a38e257ce32e9801)   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |

## Macro Definition Documentation

## [◆ ](#a19034e9b2fe534947855ad074cd5962b)IRQ\_DELIVERY\_FIXED

| #define IRQ\_DELIVERY\_FIXED   0x00000000 |
| --- |

## [◆ ](#a0c6b1b5a78c465e429a9a5633601d231)IRQ\_DELIVERY\_LOWEST

| #define IRQ\_DELIVERY\_LOWEST   0x00000100 |
| --- |

## [◆ ](#aff68b0efbc719bc28f0d56c9ba8607bc)IRQ\_TYPE\_EDGE

| #define IRQ\_TYPE\_EDGE   0x00000000 |
| --- |

## [◆ ](#a7f62c57495f357ec336cba12f1a12d61)IRQ\_TYPE\_FIXED\_EDGE\_FALLING

| #define IRQ\_TYPE\_FIXED\_EDGE\_FALLING   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| --- |

## [◆ ](#af1a9700940385a6aa6c9ff93fa834436)IRQ\_TYPE\_FIXED\_EDGE\_RISING

| #define IRQ\_TYPE\_FIXED\_EDGE\_RISING   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| --- |

## [◆ ](#a9a2bb018c589784edf36b204ba2daf48)IRQ\_TYPE\_FIXED\_LEVEL\_HIGH

| #define IRQ\_TYPE\_FIXED\_LEVEL\_HIGH   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| --- |

## [◆ ](#ab570a690df9e89e8a38e257ce32e9801)IRQ\_TYPE\_FIXED\_LEVEL\_LOW

| #define IRQ\_TYPE\_FIXED\_LEVEL\_LOW   ([IRQ\_DELIVERY\_FIXED](#a19034e9b2fe534947855ad074cd5962b) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| --- |

## [◆ ](#aeb89171ec61787d7a3ced80b30af4359)IRQ\_TYPE\_HIGH

| #define IRQ\_TYPE\_HIGH   0x00000000 |
| --- |

## [◆ ](#a296e915831223a614a6ea87dbe7735e7)IRQ\_TYPE\_LEVEL

| #define IRQ\_TYPE\_LEVEL   0x00008000 |
| --- |

## [◆ ](#a76dfa18a4a8be7f8b930115b7a9ffc93)IRQ\_TYPE\_LOW

| #define IRQ\_TYPE\_LOW   0x00002000 |
| --- |

## [◆ ](#a5a136f30dc5cb9f1b696751903b3fadd)IRQ\_TYPE\_LOWEST\_EDGE\_FALLING

| #define IRQ\_TYPE\_LOWEST\_EDGE\_FALLING   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| --- |

## [◆ ](#a980bab4b0502b138f5fa8af9ca9833b4)IRQ\_TYPE\_LOWEST\_EDGE\_RISING

| #define IRQ\_TYPE\_LOWEST\_EDGE\_RISING   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| --- |

## [◆ ](#a9083a377fa943731dc24733933bae5d6)IRQ\_TYPE\_LOWEST\_LEVEL\_HIGH

| #define IRQ\_TYPE\_LOWEST\_LEVEL\_HIGH   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_HIGH](#aeb89171ec61787d7a3ced80b30af4359)) |
| --- |

## [◆ ](#a15c26d56a818f5340c36117a429282a8)IRQ\_TYPE\_LOWEST\_LEVEL\_LOW

| #define IRQ\_TYPE\_LOWEST\_LEVEL\_LOW   ([IRQ\_DELIVERY\_LOWEST](#a0c6b1b5a78c465e429a9a5633601d231) | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7) | [IRQ\_TYPE\_LOW](#a76dfa18a4a8be7f8b930115b7a9ffc93)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [intel-ioapic.h](intel-ioapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
