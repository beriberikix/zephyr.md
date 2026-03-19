---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__ccid.html
original_path: doxygen/html/group__bt__ccid.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Content Control Identifier

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Content Control Identifier (CCID).
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_CCID\_MIN](#ga1be6ef63b32f44100a77e48c88a9c126)   0 |
|  | Minimum CCID value. |
| #define | [BT\_CCID\_MAX](#gaae664247d3537ab473c2f533602b2afa)   255 |
|  | Maximum CCID value. |

| Functions | |
| --- | --- |
| int | [bt\_ccid\_alloc\_value](#gad621dd750e4b1c23791afc72785990fc) (void) |
|  | Allocates a CCID value. |
| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_ccid\_find\_attr](#ga07845fe5cc445a35448881430f528609) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Get the GATT attribute of a CCID value. |

## Detailed Description

Bluetooth Content Control Identifier (CCID).

Since
:   3.7

Version
:   0.8.0

The Content Control Identifier (CCID) API manages CCIDs for [BT\_UUID\_CCID](group__bt__uuid.md#gab76981ff7b5fe1949c606e901daa33d3 "BT_UUID_CCID") characteristics.

## Macro Definition Documentation

## [◆ ](#gaae664247d3537ab473c2f533602b2afa)BT\_CCID\_MAX

| #define BT\_CCID\_MAX   255 |
| --- |

`#include <[ccid.h](ccid_8h.md)>`

Maximum CCID value.

## [◆ ](#ga1be6ef63b32f44100a77e48c88a9c126)BT\_CCID\_MIN

| #define BT\_CCID\_MIN   0 |
| --- |

`#include <[ccid.h](ccid_8h.md)>`

Minimum CCID value.

## Function Documentation

## [◆ ](#gad621dd750e4b1c23791afc72785990fc)bt\_ccid\_alloc\_value()

| int bt\_ccid\_alloc\_value | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccid.h](ccid_8h.md)>`

Allocates a CCID value.

This should always be called right before registering a GATT service that contains a [BT\_UUID\_CCID](group__bt__uuid.md#gab76981ff7b5fe1949c606e901daa33d3 "BT_UUID_CCID") characteristic. Allocating a CCID without registering the characteristic may (in very rare cases) result in duplicated CCIDs on the device.

Requires that `CONFIG_BT_CONN` is enabled.

Return values
:   | ccid | 8-bit unsigned CCID value on success |
    | --- | --- |
    | -ENOMEM | No more CCIDs can be allocated |

## [◆ ](#ga07845fe5cc445a35448881430f528609)bt\_ccid\_find\_attr()

| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* bt\_ccid\_find\_attr | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ccid* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccid.h](ccid_8h.md)>`

Get the GATT attribute of a CCID value.

Searches the current GATT database for a CCID characteristic that has the supplied CCID value.

Requires that `CONFIG_BT_CONN` is enabled.

Parameters
:   | ccid | The CCID to search for |
    | --- | --- |

Return values
:   | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | None was found |
    | --- | --- |
    | attr | Pointer to a GATT attribute |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
