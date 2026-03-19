---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__csip__set__coordinator__set__info.html
original_path: doxygen/html/structbt__csip__set__coordinator__set__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_coordinator\_set\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__csip.md)

Information about a specific set.
[More...](#details)

`#include <[csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sirk](#a50caa7b3a231e6944c807f7653edce3c) [16] |
|  | The 16 octet set Set Identity Resolving Key (SIRK). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [set\_size](#ac969998670d04d6dea96ea6f666f3fc9) |
|  | The size of the set. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rank](#a362fd6d8afbde9eb77d4f9a47aecb03c) |
|  | The rank of the set on the remote device. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lockable](#aa85b6a24ea8f020bb1312065e461c4b2) |
|  | Whether or not the set can be locked on this device. |

## Detailed Description

Information about a specific set.

## Field Documentation

## [◆ ](#aa85b6a24ea8f020bb1312065e461c4b2)lockable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_csip\_set\_coordinator\_set\_info::lockable |
| --- |

Whether or not the set can be locked on this device.

## [◆ ](#a362fd6d8afbde9eb77d4f9a47aecb03c)rank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_coordinator\_set\_info::rank |
| --- |

The rank of the set on the remote device.

Will be 0 if not exposed by the server.

## [◆ ](#ac969998670d04d6dea96ea6f666f3fc9)set\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_coordinator\_set\_info::set\_size |
| --- |

The size of the set.

Will be 0 if not exposed by the server.

## [◆ ](#a50caa7b3a231e6944c807f7653edce3c)sirk

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_coordinator\_set\_info::sirk[16] |
| --- |

The 16 octet set Set Identity Resolving Key (SIRK).

The SIRK may not be exposed by the server over Bluetooth, and may require an out-of-band solution.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
