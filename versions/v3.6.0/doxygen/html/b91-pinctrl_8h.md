---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/b91-pinctrl_8h.html
original_path: doxygen/html/b91-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

b91-pinctrl.h File Reference

[Go to the source code of this file.](b91-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [B91\_FUNC\_A](#af74802aac35370a78d734c183d065927)   0x00 |
| #define | [B91\_FUNC\_B](#a80e3477cd2f866955e3e61712e88fe15)   0x01 |
| #define | [B91\_FUNC\_C](#ae00f63d1146dc5aa3e3fb586672be187)   0x02 |
| #define | [B91\_PORT\_A](#aafb690574da4bba9bd1394013a3b8c5f)   0x00 |
| #define | [B91\_PORT\_B](#a7a07ae7763882f9dde2372bfd2e7ed5f)   0x01 |
| #define | [B91\_PORT\_C](#a31164e5af693e763aee5a65f2566e71b)   0x02 |
| #define | [B91\_PORT\_D](#a85a32b0056d25e1b65495e94aefb0b0d)   0x03 |
| #define | [B91\_PORT\_E](#a4eb94b2b81a87fc1868752a1f23e19b9)   0x04 |
| #define | [B91\_PIN\_0](#a26acab82d9dfd476f8ad2234463de25e)   0x01 |
| #define | [B91\_PIN\_1](#af5abb58004aebaddfd3536e3e7431032)   0x02 |
| #define | [B91\_PIN\_2](#a3bebe3d7a004486830f25887ba6784e4)   0x04 |
| #define | [B91\_PIN\_3](#a564cda0e7550d1ac7eade1a6478e6c5f)   0x08 |
| #define | [B91\_PIN\_4](#a4d4c50821490a48bf5c180d38e6562f7)   0x10 |
| #define | [B91\_PIN\_5](#aab839f7de5cd44c6501aa87918377e63)   0x20 |
| #define | [B91\_PIN\_6](#ad560e7cd90341acb45bcf7f971f50344)   0x40 |
| #define | [B91\_PIN\_7](#a1daded0f866fbeecc396ce8b460dfaf4)   0x80 |
| #define | [B91\_PULL\_NONE](#ab92d8f065db3db13bdf6f34681dba5f5)   0 |
| #define | [B91\_PULL\_DOWN](#adabf515b2ca84d1b392128de1ca2c784)   2 |
| #define | [B91\_PULL\_UP](#aca2b2bc1fe29735ad65a7b498473b3fc)   3 |
| #define | [B91\_PIN\_0\_FUNC\_POS](#a878ccfc0e6ee8b60108529fdde076434)   0x00 |
| #define | [B91\_PIN\_1\_FUNC\_POS](#a650fe8f7c3f5fb117149922d7e6fd4b2)   0x02 |
| #define | [B91\_PIN\_2\_FUNC\_POS](#af06c878c2b3ed58fbc216df02e2bd441)   0x04 |
| #define | [B91\_PIN\_3\_FUNC\_POS](#aa892ca9aafc68810179f074fe3977bdb)   0x06 |
| #define | [B91\_PIN\_4\_FUNC\_POS](#a29c13feae83222745e41d0533ab79028)   0x00 |
| #define | [B91\_PIN\_5\_FUNC\_POS](#a39e7598c002022c51c4756841c19765b)   0x02 |
| #define | [B91\_PIN\_6\_FUNC\_POS](#a1add045066251ac9562dbe9c957600ec)   0x04 |
| #define | [B91\_PIN\_7\_FUNC\_POS](#ad9b891a9dadf35a028978d9cab96821b)   0x06 |
| #define | [B91\_PULL\_POS](#acd069bef9c0ea38053d084042549e2c4)   19 |
| #define | [B91\_PULL\_MSK](#a63f6911e764836b3a3357352b2a88a86)   0x3 |
| #define | [B91\_FUNC\_POS](#a3d36f61c5c08be8735749041347680e4)   16 |
| #define | [B91\_FUNC\_MSK](#a78cdf57b4bcbefaf7459a45cf35e9612)   0x3 |
| #define | [B91\_PORT\_POS](#a1de5dc69a54207b3aeb315df26e9fbce)   8 |
| #define | [B91\_PORT\_MSK](#a05301516ef9160c2e7e12464034ca5f4)   0xFF |
| #define | [B91\_PIN\_POS](#add4262e10e4c8f626e4e5f29a794d8ad)   0 |
| #define | [B91\_PIN\_MSK](#ad623894f4b0db2e5ccee6c481f36e096)   0xFFFF |
| #define | [B91\_PIN\_ID\_MSK](#a31bc586c21d89de9ae8f56febbc9b6af)   0xFF |
| #define | [B91\_PINMUX\_SET](#af803cc8ae922bcf9ec7890173163c884)(port, pin, func) |
| #define | [B91\_PINMUX\_GET\_PULL](#a0859825b3954344a5fa3b81b5f2e709b)(pinmux) |
| #define | [B91\_PINMUX\_GET\_FUNC](#abde379851baa2cf7678a2c12a66f7056)(pinmux) |
| #define | [B91\_PINMUX\_GET\_PIN](#a3deef9c25fa8d14801cd406f0d56b153)(pinmux) |
| #define | [B91\_PINMUX\_GET\_PIN\_ID](#ac79594fdd959968e627091f6f57a89eb)(pinmux) |

## Macro Definition Documentation

## [◆ ](#af74802aac35370a78d734c183d065927)B91\_FUNC\_A

| #define B91\_FUNC\_A   0x00 |
| --- |

## [◆ ](#a80e3477cd2f866955e3e61712e88fe15)B91\_FUNC\_B

| #define B91\_FUNC\_B   0x01 |
| --- |

## [◆ ](#ae00f63d1146dc5aa3e3fb586672be187)B91\_FUNC\_C

| #define B91\_FUNC\_C   0x02 |
| --- |

## [◆ ](#a78cdf57b4bcbefaf7459a45cf35e9612)B91\_FUNC\_MSK

| #define B91\_FUNC\_MSK   0x3 |
| --- |

## [◆ ](#a3d36f61c5c08be8735749041347680e4)B91\_FUNC\_POS

| #define B91\_FUNC\_POS   16 |
| --- |

## [◆ ](#a26acab82d9dfd476f8ad2234463de25e)B91\_PIN\_0

| #define B91\_PIN\_0   0x01 |
| --- |

## [◆ ](#a878ccfc0e6ee8b60108529fdde076434)B91\_PIN\_0\_FUNC\_POS

| #define B91\_PIN\_0\_FUNC\_POS   0x00 |
| --- |

## [◆ ](#af5abb58004aebaddfd3536e3e7431032)B91\_PIN\_1

| #define B91\_PIN\_1   0x02 |
| --- |

## [◆ ](#a650fe8f7c3f5fb117149922d7e6fd4b2)B91\_PIN\_1\_FUNC\_POS

| #define B91\_PIN\_1\_FUNC\_POS   0x02 |
| --- |

## [◆ ](#a3bebe3d7a004486830f25887ba6784e4)B91\_PIN\_2

| #define B91\_PIN\_2   0x04 |
| --- |

## [◆ ](#af06c878c2b3ed58fbc216df02e2bd441)B91\_PIN\_2\_FUNC\_POS

| #define B91\_PIN\_2\_FUNC\_POS   0x04 |
| --- |

## [◆ ](#a564cda0e7550d1ac7eade1a6478e6c5f)B91\_PIN\_3

| #define B91\_PIN\_3   0x08 |
| --- |

## [◆ ](#aa892ca9aafc68810179f074fe3977bdb)B91\_PIN\_3\_FUNC\_POS

| #define B91\_PIN\_3\_FUNC\_POS   0x06 |
| --- |

## [◆ ](#a4d4c50821490a48bf5c180d38e6562f7)B91\_PIN\_4

| #define B91\_PIN\_4   0x10 |
| --- |

## [◆ ](#a29c13feae83222745e41d0533ab79028)B91\_PIN\_4\_FUNC\_POS

| #define B91\_PIN\_4\_FUNC\_POS   0x00 |
| --- |

## [◆ ](#aab839f7de5cd44c6501aa87918377e63)B91\_PIN\_5

| #define B91\_PIN\_5   0x20 |
| --- |

## [◆ ](#a39e7598c002022c51c4756841c19765b)B91\_PIN\_5\_FUNC\_POS

| #define B91\_PIN\_5\_FUNC\_POS   0x02 |
| --- |

## [◆ ](#ad560e7cd90341acb45bcf7f971f50344)B91\_PIN\_6

| #define B91\_PIN\_6   0x40 |
| --- |

## [◆ ](#a1add045066251ac9562dbe9c957600ec)B91\_PIN\_6\_FUNC\_POS

| #define B91\_PIN\_6\_FUNC\_POS   0x04 |
| --- |

## [◆ ](#a1daded0f866fbeecc396ce8b460dfaf4)B91\_PIN\_7

| #define B91\_PIN\_7   0x80 |
| --- |

## [◆ ](#ad9b891a9dadf35a028978d9cab96821b)B91\_PIN\_7\_FUNC\_POS

| #define B91\_PIN\_7\_FUNC\_POS   0x06 |
| --- |

## [◆ ](#a31bc586c21d89de9ae8f56febbc9b6af)B91\_PIN\_ID\_MSK

| #define B91\_PIN\_ID\_MSK   0xFF |
| --- |

## [◆ ](#ad623894f4b0db2e5ccee6c481f36e096)B91\_PIN\_MSK

| #define B91\_PIN\_MSK   0xFFFF |
| --- |

## [◆ ](#add4262e10e4c8f626e4e5f29a794d8ad)B91\_PIN\_POS

| #define B91\_PIN\_POS   0 |
| --- |

## [◆ ](#abde379851baa2cf7678a2c12a66f7056)B91\_PINMUX\_GET\_FUNC

| #define B91\_PINMUX\_GET\_FUNC | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((pinmux >> [B91\_FUNC\_POS](#a3d36f61c5c08be8735749041347680e4)) & [B91\_FUNC\_MSK](#a78cdf57b4bcbefaf7459a45cf35e9612))

[B91\_FUNC\_POS](#a3d36f61c5c08be8735749041347680e4)

#define B91\_FUNC\_POS

**Definition** b91-pinctrl.h:56

[B91\_FUNC\_MSK](#a78cdf57b4bcbefaf7459a45cf35e9612)

#define B91\_FUNC\_MSK

**Definition** b91-pinctrl.h:57

## [◆ ](#a3deef9c25fa8d14801cd406f0d56b153)B91\_PINMUX\_GET\_PIN

| #define B91\_PINMUX\_GET\_PIN | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((pinmux >> [B91\_PIN\_POS](#add4262e10e4c8f626e4e5f29a794d8ad)) & [B91\_PIN\_MSK](#ad623894f4b0db2e5ccee6c481f36e096))

[B91\_PIN\_MSK](#ad623894f4b0db2e5ccee6c481f36e096)

#define B91\_PIN\_MSK

**Definition** b91-pinctrl.h:61

[B91\_PIN\_POS](#add4262e10e4c8f626e4e5f29a794d8ad)

#define B91\_PIN\_POS

**Definition** b91-pinctrl.h:60

## [◆ ](#ac79594fdd959968e627091f6f57a89eb)B91\_PINMUX\_GET\_PIN\_ID

| #define B91\_PINMUX\_GET\_PIN\_ID | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((pinmux >> [B91\_PIN\_POS](#add4262e10e4c8f626e4e5f29a794d8ad)) & [B91\_PIN\_ID\_MSK](#a31bc586c21d89de9ae8f56febbc9b6af))

[B91\_PIN\_ID\_MSK](#a31bc586c21d89de9ae8f56febbc9b6af)

#define B91\_PIN\_ID\_MSK

**Definition** b91-pinctrl.h:62

## [◆ ](#a0859825b3954344a5fa3b81b5f2e709b)B91\_PINMUX\_GET\_PULL

| #define B91\_PINMUX\_GET\_PULL | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((pinmux >> [B91\_PULL\_POS](#acd069bef9c0ea38053d084042549e2c4)) & [B91\_PULL\_MSK](#a63f6911e764836b3a3357352b2a88a86))

[B91\_PULL\_MSK](#a63f6911e764836b3a3357352b2a88a86)

#define B91\_PULL\_MSK

**Definition** b91-pinctrl.h:55

[B91\_PULL\_POS](#acd069bef9c0ea38053d084042549e2c4)

#define B91\_PULL\_POS

**Definition** b91-pinctrl.h:54

## [◆ ](#af803cc8ae922bcf9ec7890173163c884)B91\_PINMUX\_SET

| #define B91\_PINMUX\_SET | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *func* ) |

**Value:**

((func << [B91\_FUNC\_POS](#a3d36f61c5c08be8735749041347680e4)) | \

(port << [B91\_PORT\_POS](#a1de5dc69a54207b3aeb315df26e9fbce)) | \

(pin << [B91\_PIN\_POS](#add4262e10e4c8f626e4e5f29a794d8ad)))

[B91\_PORT\_POS](#a1de5dc69a54207b3aeb315df26e9fbce)

#define B91\_PORT\_POS

**Definition** b91-pinctrl.h:58

## [◆ ](#aafb690574da4bba9bd1394013a3b8c5f)B91\_PORT\_A

| #define B91\_PORT\_A   0x00 |
| --- |

## [◆ ](#a7a07ae7763882f9dde2372bfd2e7ed5f)B91\_PORT\_B

| #define B91\_PORT\_B   0x01 |
| --- |

## [◆ ](#a31164e5af693e763aee5a65f2566e71b)B91\_PORT\_C

| #define B91\_PORT\_C   0x02 |
| --- |

## [◆ ](#a85a32b0056d25e1b65495e94aefb0b0d)B91\_PORT\_D

| #define B91\_PORT\_D   0x03 |
| --- |

## [◆ ](#a4eb94b2b81a87fc1868752a1f23e19b9)B91\_PORT\_E

| #define B91\_PORT\_E   0x04 |
| --- |

## [◆ ](#a05301516ef9160c2e7e12464034ca5f4)B91\_PORT\_MSK

| #define B91\_PORT\_MSK   0xFF |
| --- |

## [◆ ](#a1de5dc69a54207b3aeb315df26e9fbce)B91\_PORT\_POS

| #define B91\_PORT\_POS   8 |
| --- |

## [◆ ](#adabf515b2ca84d1b392128de1ca2c784)B91\_PULL\_DOWN

| #define B91\_PULL\_DOWN   2 |
| --- |

## [◆ ](#a63f6911e764836b3a3357352b2a88a86)B91\_PULL\_MSK

| #define B91\_PULL\_MSK   0x3 |
| --- |

## [◆ ](#ab92d8f065db3db13bdf6f34681dba5f5)B91\_PULL\_NONE

| #define B91\_PULL\_NONE   0 |
| --- |

## [◆ ](#acd069bef9c0ea38053d084042549e2c4)B91\_PULL\_POS

| #define B91\_PULL\_POS   19 |
| --- |

## [◆ ](#aca2b2bc1fe29735ad65a7b498473b3fc)B91\_PULL\_UP

| #define B91\_PULL\_UP   3 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [b91-pinctrl.h](b91-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
