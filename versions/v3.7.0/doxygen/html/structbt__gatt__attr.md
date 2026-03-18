---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__attr.html
original_path: doxygen/html/structbt__gatt__attr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_attr Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT Attribute structure.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a6958f507f9ff172018be458ebc86106f) |
|  | Attribute UUID. |
| [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) | [read](#a074abc719494ca35997a452f526e7ecc) |
|  | Attribute read callback. |
| [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) | [write](#a1ecd78536067f4bded506e0daccefd35) |
|  | Attribute write callback. |
| void \* | [user\_data](#adeb063fb101fab45dd789c7212c43357) |
|  | Attribute user data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#aeee42a3d3ca15e40cf11cc0c3fde106b) |
|  | Attribute handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [perm](#a0849a40254622080d05e8559c4fdb9e2) |
|  | Attribute permissions. |

## Detailed Description

GATT Attribute structure.

## Field Documentation

## [◆ ](#aeee42a3d3ca15e40cf11cc0c3fde106b)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr::handle |
| --- |

Attribute handle.

## [◆ ](#a0849a40254622080d05e8559c4fdb9e2)perm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr::perm |
| --- |

Attribute permissions.

Will be 0 if returned from [bt\_gatt\_discover()](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd "GATT Discover function.").

## [◆ ](#a074abc719494ca35997a452f526e7ecc)read

| [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) bt\_gatt\_attr::read |
| --- |

Attribute read callback.

## [◆ ](#adeb063fb101fab45dd789c7212c43357)user\_data

| void\* bt\_gatt\_attr::user\_data |
| --- |

Attribute user data.

## [◆ ](#a6958f507f9ff172018be458ebc86106f)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_attr::uuid |
| --- |

Attribute UUID.

## [◆ ](#a1ecd78536067f4bded506e0daccefd35)write

| [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) bt\_gatt\_attr::write |
| --- |

Attribute write callback.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_attr](structbt__gatt__attr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
