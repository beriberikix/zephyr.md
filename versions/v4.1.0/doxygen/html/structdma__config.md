---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdma__config.html
original_path: doxygen/html/structdma__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DMA Interface](group__dma__interface.md)

DMA configuration structure.
[More...](#details)

`#include <[dma.h](drivers_2dma_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_slot](#a8e6c5cab5ec030066a3e57e0507fbf9f): 8 |
|  | Which peripheral and direction, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [channel\_direction](#aaf903b1badff8b0fc4ef18a34c2773d7): 3 |
|  | Direction the transfers are occurring. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [complete\_callback\_en](#a39526177f03017d245651b4f51820161): 1 |
|  | Completion callback enable. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [error\_callback\_dis](#a416a0ef20318fe77d7e383caeee67e94): 1 |
|  | Error callback disable. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_handshake](#a2927e31730c6ca2f5ac8db38c255d9f7): 1 |
|  | Source handshake, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_handshake](#af570b4050200ec510df323bd31558233): 1 |
|  | Destination handshake, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [channel\_priority](#a284d96c59945aaa851d235802aee979a): 4 |
|  | Channel priority for arbitration, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_chaining\_en](#a7c77afc1f546efda6ce22f50560b8840): 1 |
|  | Source chaining enable, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_chaining\_en](#a8a304fdada9ec7fc87402449e1410486): 1 |
|  | Destination chaining enable, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [linked\_channel](#ace2dc918fcfea264a579b1084fcb7fe5): 7 |
|  | Linked channel, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cyclic](#afa70dbf1ee7bb5fb6a771f634783b7a2): 1 |
|  | Cyclic transfer list, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_data\_size](#ac9144783b4843182451b440d97ecd273): 16 |
|  | Width of source data (in bytes). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_data\_size](#adfa9efbfbef3ed41b2f8dd5b9c441e08): 16 |
|  | Width of destination data (in bytes). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_burst\_length](#ad750b724bab1503ded7c163d8228aa80): 16 |
|  | Source burst length in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_burst\_length](#aca47b00f817e55bf662fdd6767a59ed0): 16 |
|  | Destination burst length in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [block\_count](#adb776a4940c71b61cab60eb05159b2d4) |
|  | Number of blocks in transfer list. |
| struct [dma\_block\_config](structdma__block__config.md) \* | [head\_block](#aca6a1cb9b580a61bf91490fecf10cb16) |
|  | Pointer to the first block in the transfer list. |
| void \* | [user\_data](#a510eed1cadbf411c9e94e1d1fb43d39d) |
|  | Optional attached user data for callbacks. |
| [dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5) | [dma\_callback](#a69110abc43227bd7df217c4e25bb964b) |
|  | Optional callback for completion and error events. |

## Detailed Description

DMA configuration structure.

## Field Documentation

## [◆ ](#adb776a4940c71b61cab60eb05159b2d4)block\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::block\_count |
| --- |

Number of blocks in transfer list.

## [◆ ](#aaf903b1badff8b0fc4ef18a34c2773d7)channel\_direction

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::channel\_direction |
| --- |

Direction the transfers are occurring.

- 0b000 memory to memory,
- 0b001 memory to peripheral,
- 0b010 peripheral to memory,
- 0b011 peripheral to peripheral,
- 0b100 host to memory
- 0b101 memory to host
- others hardware specific

## [◆ ](#a284d96c59945aaa851d235802aee979a)channel\_priority

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::channel\_priority |
| --- |

Channel priority for arbitration, HW specific.

## [◆ ](#a39526177f03017d245651b4f51820161)complete\_callback\_en

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::complete\_callback\_en |
| --- |

Completion callback enable.

- 0b0 callback invoked at transfer list completion only
- 0b1 callback invoked at completion of each block

## [◆ ](#afa70dbf1ee7bb5fb6a771f634783b7a2)cyclic

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::cyclic |
| --- |

Cyclic transfer list, HW specific.

## [◆ ](#aca47b00f817e55bf662fdd6767a59ed0)dest\_burst\_length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::dest\_burst\_length |
| --- |

Destination burst length in bytes.

## [◆ ](#a8a304fdada9ec7fc87402449e1410486)dest\_chaining\_en

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::dest\_chaining\_en |
| --- |

Destination chaining enable, HW specific.

## [◆ ](#adfa9efbfbef3ed41b2f8dd5b9c441e08)dest\_data\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::dest\_data\_size |
| --- |

Width of destination data (in bytes).

## [◆ ](#af570b4050200ec510df323bd31558233)dest\_handshake

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::dest\_handshake |
| --- |

Destination handshake, HW specific.

- 0b0 HW
- 0b1 SW

## [◆ ](#a69110abc43227bd7df217c4e25bb964b)dma\_callback

| [dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5) dma\_config::dma\_callback |
| --- |

Optional callback for completion and error events.

## [◆ ](#a8e6c5cab5ec030066a3e57e0507fbf9f)dma\_slot

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::dma\_slot |
| --- |

Which peripheral and direction, HW specific.

## [◆ ](#a416a0ef20318fe77d7e383caeee67e94)error\_callback\_dis

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::error\_callback\_dis |
| --- |

Error callback disable.

- 0b0 error callback enabled
- 0b1 error callback disabled

## [◆ ](#aca6a1cb9b580a61bf91490fecf10cb16)head\_block

| struct [dma\_block\_config](structdma__block__config.md)\* dma\_config::head\_block |
| --- |

Pointer to the first block in the transfer list.

## [◆ ](#ace2dc918fcfea264a579b1084fcb7fe5)linked\_channel

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::linked\_channel |
| --- |

Linked channel, HW specific.

## [◆ ](#ad750b724bab1503ded7c163d8228aa80)source\_burst\_length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::source\_burst\_length |
| --- |

Source burst length in bytes.

## [◆ ](#a7c77afc1f546efda6ce22f50560b8840)source\_chaining\_en

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::source\_chaining\_en |
| --- |

Source chaining enable, HW specific.

## [◆ ](#ac9144783b4843182451b440d97ecd273)source\_data\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::source\_data\_size |
| --- |

Width of source data (in bytes).

## [◆ ](#a2927e31730c6ca2f5ac8db38c255d9f7)source\_handshake

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_config::source\_handshake |
| --- |

Source handshake, HW specific.

- 0b0 HW
- 0b1 SW

## [◆ ](#a510eed1cadbf411c9e94e1d1fb43d39d)user\_data

| void\* dma\_config::user\_data |
| --- |

Optional attached user data for callbacks.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dma.h](drivers_2dma_8h_source.md)

- [dma\_config](structdma__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
