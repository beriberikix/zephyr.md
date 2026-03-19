---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdma__block__config.html
original_path: doxygen/html/structdma__block__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_block\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DMA Interface](group__dma__interface.md)

DMA block configuration structure.
[More...](#details)

`#include <[dma.h](drivers_2dma_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_address](#a9fbd1deae8936a806ecc79bad3f3b9bb) |
|  | block starting address at source |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_address](#a9a66e0a647c55e94423ababf44c04325) |
|  | block starting address at destination |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [source\_gather\_interval](#a3180ef98f007ad9be7f6ff363dc125c3) |
|  | Address adjustment at gather boundary. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest\_scatter\_interval](#a18bafb80538bca9c12197955770b6511) |
|  | Address adjustment at scatter boundary. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dest\_scatter\_count](#ae38027f6262c34d9f1abe4f923d904b4) |
|  | Continuous transfer count between scatter boundaries. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_gather\_count](#a8ffcde07d02317b3cc1b327bd0b88395) |
|  | Continuous transfer count between gather boundaries. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [block\_size](#a3fdab19df16d5e96054aabffbf27fcc1) |
|  | Number of bytes to be transferred for this block. |
| struct [dma\_block\_config](structdma__block__config.md) \* | [next\_block](#a937168582c7473fe1b2b696cd1433605) |
|  | Pointer to next block in a transfer list. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_gather\_en](#abbac399f6c6e18ad2ed25359ebb799ef): 1 |
|  | Enable source gathering when set to 1. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dest\_scatter\_en](#a778935d5b806002b902b72304b845ea0): 1 |
|  | Enable destination scattering when set to 1. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_addr\_adj](#a9110f948520186aa5718f57b4bbbd24a): 2 |
|  | Source address adjustment option. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dest\_addr\_adj](#ad69502226d2c60adbdb9fe5e93dc0a05): 2 |
|  | Destination address adjustment. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_reload\_en](#a4f8f5b65002f65eaacdd3dde26c47170): 1 |
|  | Reload source address at the end of block transfer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dest\_reload\_en](#a7dedf429f44f3af6fcc0db125d6494c8): 1 |
|  | Reload destination address at the end of block transfer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fifo\_mode\_control](#a877a30b62fd8e0e1773890a10c8a2751): 4 |
|  | FIFO fill before starting transfer, HW specific meaning. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flow\_control\_mode](#aecf6805b898a70922c58d15127bafc92): 1 |
|  | Transfer flow control mode. |

## Detailed Description

DMA block configuration structure.

Aside from source address, destination address, and block size many of these options are hardware and driver dependent.

## Field Documentation

## [◆ ](#a3fdab19df16d5e96054aabffbf27fcc1)block\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_block\_config::block\_size |
| --- |

Number of bytes to be transferred for this block.

## [◆ ](#ad69502226d2c60adbdb9fe5e93dc0a05)dest\_addr\_adj

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::dest\_addr\_adj |
| --- |

Destination address adjustment.

- 0b00 increment
- 0b01 decrement
- 0b10 no change

## [◆ ](#a9a66e0a647c55e94423ababf44c04325)dest\_address

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_block\_config::dest\_address |
| --- |

block starting address at destination

## [◆ ](#a7dedf429f44f3af6fcc0db125d6494c8)dest\_reload\_en

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::dest\_reload\_en |
| --- |

Reload destination address at the end of block transfer.

## [◆ ](#ae38027f6262c34d9f1abe4f923d904b4)dest\_scatter\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::dest\_scatter\_count |
| --- |

Continuous transfer count between scatter boundaries.

## [◆ ](#a778935d5b806002b902b72304b845ea0)dest\_scatter\_en

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::dest\_scatter\_en |
| --- |

Enable destination scattering when set to 1.

## [◆ ](#a18bafb80538bca9c12197955770b6511)dest\_scatter\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_block\_config::dest\_scatter\_interval |
| --- |

Address adjustment at scatter boundary.

## [◆ ](#a877a30b62fd8e0e1773890a10c8a2751)fifo\_mode\_control

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::fifo\_mode\_control |
| --- |

FIFO fill before starting transfer, HW specific meaning.

## [◆ ](#aecf6805b898a70922c58d15127bafc92)flow\_control\_mode

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::flow\_control\_mode |
| --- |

Transfer flow control mode.

- 0b0 source request service upon data availability
- 0b1 source request postponed until destination request happens

## [◆ ](#a937168582c7473fe1b2b696cd1433605)next\_block

| struct [dma\_block\_config](structdma__block__config.md)\* dma\_block\_config::next\_block |
| --- |

Pointer to next block in a transfer list.

## [◆ ](#a9110f948520186aa5718f57b4bbbd24a)source\_addr\_adj

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::source\_addr\_adj |
| --- |

Source address adjustment option.

- 0b00 increment
- 0b01 decrement
- 0b10 no change

## [◆ ](#a9fbd1deae8936a806ecc79bad3f3b9bb)source\_address

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_block\_config::source\_address |
| --- |

block starting address at source

## [◆ ](#a8ffcde07d02317b3cc1b327bd0b88395)source\_gather\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::source\_gather\_count |
| --- |

Continuous transfer count between gather boundaries.

## [◆ ](#abbac399f6c6e18ad2ed25359ebb799ef)source\_gather\_en

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::source\_gather\_en |
| --- |

Enable source gathering when set to 1.

## [◆ ](#a3180ef98f007ad9be7f6ff363dc125c3)source\_gather\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_block\_config::source\_gather\_interval |
| --- |

Address adjustment at gather boundary.

## [◆ ](#a4f8f5b65002f65eaacdd3dde26c47170)source\_reload\_en

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dma\_block\_config::source\_reload\_en |
| --- |

Reload source address at the end of block transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dma.h](drivers_2dma_8h_source.md)

- [dma\_block\_config](structdma__block__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
