---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdai__ts__cfg.html
original_path: doxygen/html/structdai__ts__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai\_ts\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DAI Interface](group__dai__interface.md)

DAI timestamp configuration.
[More...](#details)

`#include <[dai.h](dai_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [walclk\_rate](#ac17d3da9de6d860f2fa04286a4c43a1d) |
|  | Rate in Hz, e.g. |
| int | [type](#a2b0be9c840de941e4a87c422fa82356d) |
|  | Type of the DAI (SSP, DMIC, HDA, etc.). |
| int | [direction](#afdaf1a4ef6a00201b3790187ec44370f) |
|  | Direction (playback/capture). |
| int | [index](#aff3dc52737d1261cd56c084c104691eb) |
|  | Index for SSPx to select correct timestamp register. |
| int | [dma\_id](#ab874249dcb9377fafa35764b4f1c0ea0) |
|  | DMA instance id. |
| int | [dma\_chan\_index](#aa87fc1e3072490e44f65bc7690f85ce8) |
|  | Used DMA channel index. |
| int | [dma\_chan\_count](#a37c6379686435994b9050d1e9c249756) |
|  | Number of channels in single DMA. |

## Detailed Description

DAI timestamp configuration.

## Field Documentation

## [◆ ](#afdaf1a4ef6a00201b3790187ec44370f)direction

| int dai\_ts\_cfg::direction |
| --- |

Direction (playback/capture).

## [◆ ](#a37c6379686435994b9050d1e9c249756)dma\_chan\_count

| int dai\_ts\_cfg::dma\_chan\_count |
| --- |

Number of channels in single DMA.

## [◆ ](#aa87fc1e3072490e44f65bc7690f85ce8)dma\_chan\_index

| int dai\_ts\_cfg::dma\_chan\_index |
| --- |

Used DMA channel index.

## [◆ ](#ab874249dcb9377fafa35764b4f1c0ea0)dma\_id

| int dai\_ts\_cfg::dma\_id |
| --- |

DMA instance id.

## [◆ ](#aff3dc52737d1261cd56c084c104691eb)index

| int dai\_ts\_cfg::index |
| --- |

Index for SSPx to select correct timestamp register.

## [◆ ](#a2b0be9c840de941e4a87c422fa82356d)type

| int dai\_ts\_cfg::type |
| --- |

Type of the DAI (SSP, DMIC, HDA, etc.).

## [◆ ](#ac17d3da9de6d860f2fa04286a4c43a1d)walclk\_rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_ts\_cfg::walclk\_rate |
| --- |

Rate in Hz, e.g.

19200000

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dai.h](dai_8h_source.md)

- [dai\_ts\_cfg](structdai__ts__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
