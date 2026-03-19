---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sip__svc__agilex__mailbox_8h.html
original_path: doxygen/html/sip__svc__agilex__mailbox_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_agilex\_mailbox.h File Reference

Intel SoC FPGA Agilex customized SDM Mailbox communication protocol handler.
[More...](#details)

[Go to the source code of this file.](sip__svc__agilex__mailbox_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SIP\_SVP\_MB\_MAX\_WORD\_SIZE](#aa56d732f7a2de4298a5dda992b1405de)   1024 |
| #define | [SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3)   24 |
| #define | [SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK](#a3532db48b21765fb2aa419522a794a94)   0xFF |
| #define | [SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET](#a6c24e3a782d918ebc001fca12ba8321a)   12 |
| #define | [SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK](#a66f47d95a199a02038c3d25f49e46b37)   0x7FF |
| #define | [SIP\_SVC\_MB\_HEADER\_GET\_CLIENT\_ID](#a6a29fa9f750979dce255ee2b56b0a953)(header) |
| #define | [SIP\_SVC\_MB\_HEADER\_GET\_TRANS\_ID](#abb0c7166d5c2ae113ba20315c0eb44ea)(header) |
| #define | [SIP\_SVC\_MB\_HEADER\_SET\_TRANS\_ID](#ad960abd8b2e9acb4d78da132d1481705)(header, id) |
| #define | [SIP\_SVC\_MB\_HEADER\_GET\_LENGTH](#af6e53a9a4c1e4cad501a541cf0a82e48)(header) |

## Detailed Description

Intel SoC FPGA Agilex customized SDM Mailbox communication protocol handler.

SDM Mailbox protocol will be embedded in Arm SiP Services SMC protocol and sent to/from SDM via Arm SiP Services.

## Macro Definition Documentation

## [◆ ](#a6a29fa9f750979dce255ee2b56b0a953)SIP\_SVC\_MB\_HEADER\_GET\_CLIENT\_ID

| #define SIP\_SVC\_MB\_HEADER\_GET\_CLIENT\_ID | ( |  | *header* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((header) >> SIP\_SVP\_MB\_HEADER\_CLIENT\_ID\_OFFSET & \

SIP\_SVP\_MB\_HEADER\_CLIENT\_ID\_MASK)

## [◆ ](#af6e53a9a4c1e4cad501a541cf0a82e48)SIP\_SVC\_MB\_HEADER\_GET\_LENGTH

| #define SIP\_SVC\_MB\_HEADER\_GET\_LENGTH | ( |  | *header* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((header) >> [SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET](#a6c24e3a782d918ebc001fca12ba8321a) & \

[SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK](#a66f47d95a199a02038c3d25f49e46b37))

[SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK](#a66f47d95a199a02038c3d25f49e46b37)

#define SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK

**Definition** sip\_svc\_agilex\_mailbox.h:22

[SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET](#a6c24e3a782d918ebc001fca12ba8321a)

#define SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET

**Definition** sip\_svc\_agilex\_mailbox.h:21

## [◆ ](#abb0c7166d5c2ae113ba20315c0eb44ea)SIP\_SVC\_MB\_HEADER\_GET\_TRANS\_ID

| #define SIP\_SVC\_MB\_HEADER\_GET\_TRANS\_ID | ( |  | *header* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((header) >> [SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3) & \

[SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK](#a3532db48b21765fb2aa419522a794a94))

[SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK](#a3532db48b21765fb2aa419522a794a94)

#define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK

**Definition** sip\_svc\_agilex\_mailbox.h:20

[SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3)

#define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET

**Definition** sip\_svc\_agilex\_mailbox.h:19

## [◆ ](#ad960abd8b2e9acb4d78da132d1481705)SIP\_SVC\_MB\_HEADER\_SET\_TRANS\_ID

| #define SIP\_SVC\_MB\_HEADER\_SET\_TRANS\_ID | ( |  | *header*, |
| --- | --- | --- | --- |
|  |  |  | *id* ) |

**Value:**

(header) &= ~([SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK](#a3532db48b21765fb2aa419522a794a94) << \

[SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3)); \

(header) |= (((id) & [SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK](#a3532db48b21765fb2aa419522a794a94)) << \

[SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET](#afccd6d2a8364c2273de2b31a448f5de3));

## [◆ ](#a66f47d95a199a02038c3d25f49e46b37)SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK

| #define SIP\_SVP\_MB\_HEADER\_LENGTH\_MASK   0x7FF |
| --- |

## [◆ ](#a6c24e3a782d918ebc001fca12ba8321a)SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET

| #define SIP\_SVP\_MB\_HEADER\_LENGTH\_OFFSET   12 |
| --- |

## [◆ ](#a3532db48b21765fb2aa419522a794a94)SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK

| #define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_MASK   0xFF |
| --- |

## [◆ ](#afccd6d2a8364c2273de2b31a448f5de3)SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET

| #define SIP\_SVP\_MB\_HEADER\_TRANS\_ID\_OFFSET   24 |
| --- |

## [◆ ](#aa56d732f7a2de4298a5dda992b1405de)SIP\_SVP\_MB\_MAX\_WORD\_SIZE

| #define SIP\_SVP\_MB\_MAX\_WORD\_SIZE   1024 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_agilex\_mailbox.h](sip__svc__agilex__mailbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
