---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgnss__satellite.html
original_path: doxygen/html/structgnss__satellite.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_satellite Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS satellite structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prn](#a03543a7425f27c78e743b0ec180ccea7) |
|  | Pseudo-random noise sequence. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snr](#a6818083aad878aa8b06d2cbeca53b1da) |
|  | Signal-to-noise ratio in dB. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [elevation](#a3d99c5ad18242a42f95b5de496ca501d) |
|  | Elevation in degrees [0, 90]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [azimuth](#a27a864422f5207b5d38efbd8b50893a3) |
|  | Azimuth relative to True North in degrees [0, 359]. |
| enum [gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) | [system](#ad9b31c85dd0e162979d384b049142549) |
|  | System of satellite. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_tracked](#ae4c596c298ed158a188ea4a5fbd6181c): 1 |
|  | True if satellite is being tracked. |

## Detailed Description

GNSS satellite structure.

## Field Documentation

## [◆ ](#a27a864422f5207b5d38efbd8b50893a3)azimuth

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gnss\_satellite::azimuth |
| --- |

Azimuth relative to True North in degrees [0, 359].

## [◆ ](#a3d99c5ad18242a42f95b5de496ca501d)elevation

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_satellite::elevation |
| --- |

Elevation in degrees [0, 90].

## [◆ ](#ae4c596c298ed158a188ea4a5fbd6181c)is\_tracked

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_satellite::is\_tracked |
| --- |

True if satellite is being tracked.

## [◆ ](#a03543a7425f27c78e743b0ec180ccea7)prn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_satellite::prn |
| --- |

Pseudo-random noise sequence.

## [◆ ](#a6818083aad878aa8b06d2cbeca53b1da)snr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_satellite::snr |
| --- |

Signal-to-noise ratio in dB.

## [◆ ](#ad9b31c85dd0e162979d384b049142549)system

| enum [gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) gnss\_satellite::system |
| --- |

System of satellite.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_satellite](structgnss__satellite.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
