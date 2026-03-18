---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sip__svc__agilex__smc_8h.html
original_path: doxygen/html/sip__svc__agilex__smc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_agilex\_smc.h File Reference

Intel SoC FPGA Agilex customized Arm SiP Services SMC protocol.
[More...](#details)

[Go to the source code of this file.](sip__svc__agilex__smc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SMC\_STATUS\_INVALID](#abca52daa3ed42c3acacd0a2f27a64c8b)   0xFFFFFFFF |
| #define | [SMC\_STATUS\_OKAY](#aff7de6199219a46e9c177557a55b20ad)   0 |
| #define | [SMC\_STATUS\_BUSY](#a8959eae5cbbe690922a6aa35c3e6ad19)   1 |
| #define | [SMC\_STATUS\_REJECT](#a2350309516a2c57ec3250a53305d0627)   2 |
| #define | [SMC\_STATUS\_NO\_RESPONSE](#a1b99b2307df8b02a1f3dd36614077269)   3 |
| #define | [SMC\_STATUS\_ERROR](#a0f21a71f1245c31ef3a3a468901a7fe3)   4 |
| #define | [SMC\_PLAT\_PROTO\_VER](#a149c807c9429c49b48febb7493ded05a)   0x0 |
| #define | [SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#aaf01ecddc145b991b1437dc4ccd88854)   0 |
| #define | [SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a8fe58b94720ef6bb2cb46351c9e3da8f)   0xFF |
| #define | [SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET](#ae9827c60ec0c0e0d62167672b443d136)   60 |
| #define | [SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK](#a14cf7302d786ab126a18abbd0e757fed)   0xF |
| #define | [SMC\_PLAT\_PROTO\_HEADER](#a0ac21d31ae06d1fa1fd86253526baff2)   (([SMC\_PLAT\_PROTO\_VER](#a149c807c9429c49b48febb7493ded05a) & [SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK](#a14cf7302d786ab126a18abbd0e757fed)) << [SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET](#ae9827c60ec0c0e0d62167672b443d136)) |
| #define | [SMC\_PLAT\_PROTO\_HEADER\_SET\_TRANS\_ID](#aee5f5ecdeb83631a3114593e2e487a43)(header, trans\_id) |
| #define | [SMC\_FUNC\_ID\_GET\_SVC\_VERSION](#afa8c0dca448e2074bfc6abeaffd26464)   0xC2000400 |
| #define | [SMC\_FUNC\_ID\_REG\_READ](#afcaee0b300ae5fbe475c51c1d20b8e48)   0xC2000401 |
| #define | [SMC\_FUNC\_ID\_REG\_WRITE](#ab619bffd89340c1d72f3786d2c8d326b)   0xC2000402 |
| #define | [SMC\_FUNC\_ID\_REG\_UPDATE](#ad56834ca5734a3d105e6810cb4821406)   0xC2000403 |
| #define | [SMC\_FUNC\_ID\_SET\_HPS\_BRIDGES](#a382037b06541eb54757b3ad9fd7df8a4)   0xC2000404 |
| #define | [SMC\_FUNC\_ID\_RSU\_UPDATE\_ADDR](#abf081ba2e3a8039b42c40f8a7135c113)   0xC2000405 |
| #define | [SMC\_FUNC\_ID\_MAILBOX\_SEND\_COMMAND](#a98d77f81a2b07bcf8305e28e0be1e4c4)   0xC2000420 |
| #define | [SMC\_FUNC\_ID\_MAILBOX\_POLL\_RESPONSE](#ac26572cb1321697ff33adcd471e27874)   0xC2000421 |
| #define | [MAILBOX\_CANCEL\_COMMAND](#a0a1d2a2c6a290c6b293fa71cd04975fb)   0x03 |

## Detailed Description

Intel SoC FPGA Agilex customized Arm SiP Services SMC protocol.

## Macro Definition Documentation

## [◆ ](#a0a1d2a2c6a290c6b293fa71cd04975fb)MAILBOX\_CANCEL\_COMMAND

| #define MAILBOX\_CANCEL\_COMMAND   0x03 |
| --- |

## [◆ ](#afa8c0dca448e2074bfc6abeaffd26464)SMC\_FUNC\_ID\_GET\_SVC\_VERSION

| #define SMC\_FUNC\_ID\_GET\_SVC\_VERSION   0xC2000400 |
| --- |

## [◆ ](#ac26572cb1321697ff33adcd471e27874)SMC\_FUNC\_ID\_MAILBOX\_POLL\_RESPONSE

| #define SMC\_FUNC\_ID\_MAILBOX\_POLL\_RESPONSE   0xC2000421 |
| --- |

## [◆ ](#a98d77f81a2b07bcf8305e28e0be1e4c4)SMC\_FUNC\_ID\_MAILBOX\_SEND\_COMMAND

| #define SMC\_FUNC\_ID\_MAILBOX\_SEND\_COMMAND   0xC2000420 |
| --- |

## [◆ ](#afcaee0b300ae5fbe475c51c1d20b8e48)SMC\_FUNC\_ID\_REG\_READ

| #define SMC\_FUNC\_ID\_REG\_READ   0xC2000401 |
| --- |

## [◆ ](#ad56834ca5734a3d105e6810cb4821406)SMC\_FUNC\_ID\_REG\_UPDATE

| #define SMC\_FUNC\_ID\_REG\_UPDATE   0xC2000403 |
| --- |

## [◆ ](#ab619bffd89340c1d72f3786d2c8d326b)SMC\_FUNC\_ID\_REG\_WRITE

| #define SMC\_FUNC\_ID\_REG\_WRITE   0xC2000402 |
| --- |

## [◆ ](#abf081ba2e3a8039b42c40f8a7135c113)SMC\_FUNC\_ID\_RSU\_UPDATE\_ADDR

| #define SMC\_FUNC\_ID\_RSU\_UPDATE\_ADDR   0xC2000405 |
| --- |

## [◆ ](#a382037b06541eb54757b3ad9fd7df8a4)SMC\_FUNC\_ID\_SET\_HPS\_BRIDGES

| #define SMC\_FUNC\_ID\_SET\_HPS\_BRIDGES   0xC2000404 |
| --- |

## [◆ ](#a0ac21d31ae06d1fa1fd86253526baff2)SMC\_PLAT\_PROTO\_HEADER

| #define SMC\_PLAT\_PROTO\_HEADER   (([SMC\_PLAT\_PROTO\_VER](#a149c807c9429c49b48febb7493ded05a) & [SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK](#a14cf7302d786ab126a18abbd0e757fed)) << [SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET](#ae9827c60ec0c0e0d62167672b443d136)) |
| --- |

## [◆ ](#aee5f5ecdeb83631a3114593e2e487a43)SMC\_PLAT\_PROTO\_HEADER\_SET\_TRANS\_ID

| #define SMC\_PLAT\_PROTO\_HEADER\_SET\_TRANS\_ID | ( |  | *header*, |
| --- | --- | --- | --- |
|  |  |  | *trans\_id* ) |

**Value:**

(header) &= \

~([SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a8fe58b94720ef6bb2cb46351c9e3da8f) << [SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#aaf01ecddc145b991b1437dc4ccd88854)); \

(header) |= (((trans\_id)&[SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a8fe58b94720ef6bb2cb46351c9e3da8f)) \

<< [SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#aaf01ecddc145b991b1437dc4ccd88854));

[SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a8fe58b94720ef6bb2cb46351c9e3da8f)

#define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK

**Definition** sip\_svc\_agilex\_smc.h:36

[SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#aaf01ecddc145b991b1437dc4ccd88854)

#define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET

**Definition** sip\_svc\_agilex\_smc.h:35

## [◆ ](#a8fe58b94720ef6bb2cb46351c9e3da8f)SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK

| #define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK   0xFF |
| --- |

## [◆ ](#aaf01ecddc145b991b1437dc4ccd88854)SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET

| #define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET   0 |
| --- |

## [◆ ](#a14cf7302d786ab126a18abbd0e757fed)SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK

| #define SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK   0xF |
| --- |

## [◆ ](#ae9827c60ec0c0e0d62167672b443d136)SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET

| #define SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET   60 |
| --- |

## [◆ ](#a149c807c9429c49b48febb7493ded05a)SMC\_PLAT\_PROTO\_VER

| #define SMC\_PLAT\_PROTO\_VER   0x0 |
| --- |

## [◆ ](#a8959eae5cbbe690922a6aa35c3e6ad19)SMC\_STATUS\_BUSY

| #define SMC\_STATUS\_BUSY   1 |
| --- |

## [◆ ](#a0f21a71f1245c31ef3a3a468901a7fe3)SMC\_STATUS\_ERROR

| #define SMC\_STATUS\_ERROR   4 |
| --- |

## [◆ ](#abca52daa3ed42c3acacd0a2f27a64c8b)SMC\_STATUS\_INVALID

| #define SMC\_STATUS\_INVALID   0xFFFFFFFF |
| --- |

## [◆ ](#a1b99b2307df8b02a1f3dd36614077269)SMC\_STATUS\_NO\_RESPONSE

| #define SMC\_STATUS\_NO\_RESPONSE   3 |
| --- |

## [◆ ](#aff7de6199219a46e9c177557a55b20ad)SMC\_STATUS\_OKAY

| #define SMC\_STATUS\_OKAY   0 |
| --- |

## [◆ ](#a2350309516a2c57ec3250a53305d0627)SMC\_STATUS\_REJECT

| #define SMC\_STATUS\_REJECT   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_agilex\_smc.h](sip__svc__agilex__smc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
