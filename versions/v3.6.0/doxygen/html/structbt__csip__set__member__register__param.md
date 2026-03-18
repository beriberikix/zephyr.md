---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__csip__set__member__register__param.html
original_path: doxygen/html/structbt__csip__set__member__register__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_member\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__gatt__csip.md)

Register structure for Coordinated Set Identification Service.
[More...](#details)

`#include <[csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [set\_size](#af8814b6e0695001e0a70025f5c2b4e83) |
|  | Size of the set. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [set\_sirk](#a30e502d6f9c13e0cbf1903755f51c085) [16] |
|  | The unique Set Identity Resolving Key (SIRK). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lockable](#abc87df6590e3c55a2cd860f86398346d) |
|  | Boolean to set whether the set is lockable by clients. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rank](#af38436c47f52ec285cadb5d23c67ea0a) |
|  | Rank of this device in this set. |
| struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) \* | [cb](#a1878a8d50ab190920435aaef611b69f1) |
|  | Pointer to the callback structure. |

## Detailed Description

Register structure for Coordinated Set Identification Service.

## Field Documentation

## [◆ ](#a1878a8d50ab190920435aaef611b69f1)cb

| struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md)\* bt\_csip\_set\_member\_register\_param::cb |
| --- |

Pointer to the callback structure.

## [◆ ](#abc87df6590e3c55a2cd860f86398346d)lockable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_csip\_set\_member\_register\_param::lockable |
| --- |

Boolean to set whether the set is lockable by clients.

Setting this to false will disable the lock characteristic.

## [◆ ](#af38436c47f52ec285cadb5d23c67ea0a)rank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_register\_param::rank |
| --- |

Rank of this device in this set.

If the lockable parameter is set to true, this shall be > 0 and <= to the set\_size. If the lockable parameter is set to false, this may be set to 0 to disable the rank characteristic.

## [◆ ](#a30e502d6f9c13e0cbf1903755f51c085)set\_sirk

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_register\_param::set\_sirk[16] |
| --- |

The unique Set Identity Resolving Key (SIRK).

This shall be unique between different sets, and shall be the same for each set member for each set.

## [◆ ](#af8814b6e0695001e0a70025f5c2b4e83)set\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_register\_param::set\_size |
| --- |

Size of the set.

If set to 0, the set size characteristic won't be initialized.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
