---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__attr.html
original_path: doxygen/html/structbt__gatt__attr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_attr Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT Attribute.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a6958f507f9ff172018be458ebc86106f) |
|  | Attribute Type. |
| [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) | [read](#a074abc719494ca35997a452f526e7ecc) |
|  | Attribute Value read method. |
| [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) | [write](#a1ecd78536067f4bded506e0daccefd35) |
|  | Attribute Value write method. |
| void \* | [user\_data](#adeb063fb101fab45dd789c7212c43357) |
|  | Private data for [read()](#a074abc719494ca35997a452f526e7ecc) and [write()](#a1ecd78536067f4bded506e0daccefd35) implementation. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#aeee42a3d3ca15e40cf11cc0c3fde106b) |
|  | Attribute Handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [perm](#a0849a40254622080d05e8559c4fdb9e2): 15 |
|  | Attribute Permissions. |

## Detailed Description

GATT Attribute.

This type primarily represents an ATT Attribute that may be an entry in the local ATT database. The objects of this type must be part of an array that forms a GATT service.

While the formed GATT service is registered with the local GATT server, pointers to this type can typically be given to GATT server APIs, like [bt\_gatt\_notify()](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a "Notify attribute value change.").

Note
:   This type is given as an argument to the [bt\_gatt\_discover()](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd "GATT Discover function.") application callback, but it's not a proper object of this type. The field [perm](#a0849a40254622080d05e8559c4fdb9e2), and methods [read()](#a074abc719494ca35997a452f526e7ecc) and [write()](#a1ecd78536067f4bded506e0daccefd35) are not available, and it's unsound to pass the pointer to GATT server APIs.

## Field Documentation

## [◆ ](#aeee42a3d3ca15e40cf11cc0c3fde106b)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr::handle |
| --- |

Attribute Handle.

The Attribute Handle is an index corresponding to a specific Attribute in the ATT database.

Note
:   Use [bt\_gatt\_attr\_get\_handle()](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7 "Get Attribute handle.") for attributes in the local ATT database.

## [◆ ](#a0849a40254622080d05e8559c4fdb9e2)perm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr::perm |
| --- |

Attribute Permissions.

Bit field of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm").

The permissions are security requirements that must be satisfied before calling [read()](#a074abc719494ca35997a452f526e7ecc) or [write()](#a1ecd78536067f4bded506e0daccefd35).

## [◆ ](#a074abc719494ca35997a452f526e7ecc)read

| [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b) bt\_gatt\_attr::read |
| --- |

Attribute Value read method.

Readable Attributes must implement this method.

Must be NULL if the attribute is not readable.

The behavior of this method is determined by the Attribute Type.

See [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b "bt_gatt_attr_read_func_t").

## [◆ ](#adeb063fb101fab45dd789c7212c43357)user\_data

| void\* bt\_gatt\_attr::user\_data |
| --- |

Private data for [read()](#a074abc719494ca35997a452f526e7ecc) and [write()](#a1ecd78536067f4bded506e0daccefd35) implementation.

The meaning of this field varies and is not specified here.

Note
:   Attributes may have the same Attribute Type but have different implementations, with incompatible user data. Attribute Type alone must not be used to infer the type of the user data.

See also
:   [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13 "Discover attribute callback function.") about this field.

## [◆ ](#a6958f507f9ff172018be458ebc86106f)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_attr::uuid |
| --- |

Attribute Type.

The Attribute Type is a UUID which determines the interface that can be expected from the [read()](#a074abc719494ca35997a452f526e7ecc) and [write()](#a1ecd78536067f4bded506e0daccefd35) methods and the possible permission configurations.

E.g. Attribute of type [BT\_UUID\_GATT\_CPF](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022 "BT_UUID_GATT_CPF") will act as a GATT Characteristic Presentation Format descriptor as specified in Core Specification 3.G.3.3.3.5.

You can define a new Attribute Type.

## [◆ ](#a1ecd78536067f4bded506e0daccefd35)write

| [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1) bt\_gatt\_attr::write |
| --- |

Attribute Value write method.

Writeable Attributes must implement this method.

Must be NULL if the attribute is not writable.

The behavior of this method is determined by the Attribute Type.

See [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1 "bt_gatt_attr_write_func_t").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_attr](structbt__gatt__attr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
