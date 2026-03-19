---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmspi__dev__cfg.html
original_path: doxygen/html/structmspi__dev__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_dev\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI controller device specific configuration.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ce\_num](#abf8d45f88d0c8e1c4ee52ea238ff4466) |
|  | Configure CE0 or CE1 or more. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [freq](#a9490d822b67d7fab123f32f38b0ccef8) |
|  | Configure frequency. |
| enum [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) | [io\_mode](#ad0f5c1a4cd3002313087a9b1fe6cf7a1) |
|  | Configure I/O mode. |
| enum [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) | [data\_rate](#a0da8c2ccf80fdf610fcdd7fae7d159f8) |
|  | Configure data rate. |
| enum [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) | [cpp](#a2bb78caec28fadcecd787fc8a573a336) |
|  | Configure clock polarity and phase. |
| enum [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) | [endian](#a28cf9d7887e9f840344e2804c4040bc4) |
|  | Configure transfer endian. |
| enum [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) | [ce\_polarity](#ab6ed7eeb6d4b31530e06f69706b98278) |
|  | Configure chip enable polarity. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dqs\_enable](#affdcd07ac3d3d25b8a8e0882277af39a) |
|  | Configure DQS mode. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_dummy](#aae492d2e5bad4b266779be9f5bb12ee9) |
|  | Configure number of clock cycles between addr and data in RX direction. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_dummy](#a9feb1c35f7e1f5c43489771e13f2af8d) |
|  | Configure number of clock cycles between addr and data in TX direction. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_cmd](#ac9f47b226289005271a800739707456b) |
|  | Configure read command. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [write\_cmd](#acac2a0913bfbfe1f3b5e34ff1b71ff42) |
|  | Configure write command. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_length](#a0b0c9f101656e67d71d191b656738d2d) |
|  | Configure command length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr\_length](#a6dbe113d5075b1b22896c7d0c281bd3d) |
|  | Configure address length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mem\_boundary](#a3ec3e22e25440ac5eecf0f9b2d79b9e0) |
|  | Configure memory boundary. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [time\_to\_break](#a60eeb1503018fa47cc5618d150f09aa8) |
|  | Configure the time to break up a transfer into 2. |

## Detailed Description

MSPI controller device specific configuration.

## Field Documentation

## [◆ ](#a6dbe113d5075b1b22896c7d0c281bd3d)addr\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_dev\_cfg::addr\_length |
| --- |

Configure address length.

## [◆ ](#abf8d45f88d0c8e1c4ee52ea238ff4466)ce\_num

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_dev\_cfg::ce\_num |
| --- |

Configure CE0 or CE1 or more.

## [◆ ](#ab6ed7eeb6d4b31530e06f69706b98278)ce\_polarity

| enum [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) mspi\_dev\_cfg::ce\_polarity |
| --- |

Configure chip enable polarity.

## [◆ ](#a0b0c9f101656e67d71d191b656738d2d)cmd\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_dev\_cfg::cmd\_length |
| --- |

Configure command length.

## [◆ ](#a2bb78caec28fadcecd787fc8a573a336)cpp

| enum [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) mspi\_dev\_cfg::cpp |
| --- |

Configure clock polarity and phase.

## [◆ ](#a0da8c2ccf80fdf610fcdd7fae7d159f8)data\_rate

| enum [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) mspi\_dev\_cfg::data\_rate |
| --- |

Configure data rate.

## [◆ ](#affdcd07ac3d3d25b8a8e0882277af39a)dqs\_enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_dev\_cfg::dqs\_enable |
| --- |

Configure DQS mode.

## [◆ ](#a28cf9d7887e9f840344e2804c4040bc4)endian

| enum [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) mspi\_dev\_cfg::endian |
| --- |

Configure transfer endian.

## [◆ ](#a9490d822b67d7fab123f32f38b0ccef8)freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_dev\_cfg::freq |
| --- |

Configure frequency.

## [◆ ](#ad0f5c1a4cd3002313087a9b1fe6cf7a1)io\_mode

| enum [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) mspi\_dev\_cfg::io\_mode |
| --- |

Configure I/O mode.

## [◆ ](#a3ec3e22e25440ac5eecf0f9b2d79b9e0)mem\_boundary

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_dev\_cfg::mem\_boundary |
| --- |

Configure memory boundary.

## [◆ ](#ac9f47b226289005271a800739707456b)read\_cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_dev\_cfg::read\_cmd |
| --- |

Configure read command.

## [◆ ](#aae492d2e5bad4b266779be9f5bb12ee9)rx\_dummy

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_dev\_cfg::rx\_dummy |
| --- |

Configure number of clock cycles between addr and data in RX direction.

## [◆ ](#a60eeb1503018fa47cc5618d150f09aa8)time\_to\_break

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_dev\_cfg::time\_to\_break |
| --- |

Configure the time to break up a transfer into 2.

## [◆ ](#a9feb1c35f7e1f5c43489771e13f2af8d)tx\_dummy

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_dev\_cfg::tx\_dummy |
| --- |

Configure number of clock cycles between addr and data in TX direction.

## [◆ ](#acac2a0913bfbfe1f3b5e34ff1b71ff42)write\_cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_dev\_cfg::write\_cmd |
| --- |

Configure write command.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_dev\_cfg](structmspi__dev__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
