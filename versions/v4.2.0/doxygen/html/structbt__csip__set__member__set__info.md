---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__csip__set__member__set__info.html
original_path: doxygen/html/structbt__csip__set__member__set__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_member\_set\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__csip.md)

Struct to hold information about a service instance.
[More...](#details)

`#include <[zephyr/bluetooth/audio/csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sirk](#aec69fc3bc6e66d7bda2810c20a260d9c) [16] |
|  | The 16-octet SIRK. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [set\_size](#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa) |
|  | The set size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rank](#aa715eda78908c603ec11a48846018845) |
|  | The rank. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lockable](#a52ba91f4e3ee911f575160355368aae5): 1 |
|  | Whether the set is lockable. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [locked](#ae0e082aac881500f2005489d6aa88090): 1 |
|  | Whether the set is currently locked. |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [lock\_client\_addr](#a75ca9b78932626f167b186b203611c27) |
|  | The address of the client that currently holds the lock. |

## Detailed Description

Struct to hold information about a service instance.

## Field Documentation

## [◆ ](#a75ca9b78932626f167b186b203611c27)lock\_client\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_csip\_set\_member\_set\_info::lock\_client\_addr |
| --- |

The address of the client that currently holds the lock.

Will be [BT\_ADDR\_LE\_NONE](group__bt__addr.md#gadfcc0281e453cba990b623631c26f80b "BT_ADDR_LE_NONE") if the server holds the lock

## [◆ ](#a52ba91f4e3ee911f575160355368aae5)lockable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_csip\_set\_member\_set\_info::lockable |
| --- |

Whether the set is lockable.

## [◆ ](#ae0e082aac881500f2005489d6aa88090)locked

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_csip\_set\_member\_set\_info::locked |
| --- |

Whether the set is currently locked.

## [◆ ](#aa715eda78908c603ec11a48846018845)rank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_set\_info::rank |
| --- |

The rank.

May be 0 if the set is not lockable

## [◆ ](#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa)set\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_set\_info::set\_size |
| --- |

The set size.

## [◆ ](#aec69fc3bc6e66d7bda2810c20a260d9c)sirk

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_csip\_set\_member\_set\_info::sirk[16] |
| --- |

The 16-octet SIRK.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_member\_set\_info](structbt__csip__set__member__set__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
