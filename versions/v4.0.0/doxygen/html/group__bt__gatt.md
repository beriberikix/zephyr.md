---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__gatt.html
original_path: doxygen/html/group__bt__gatt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Generic Attribute Profile (GATT)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Generic Attribute Profile (GATT).
[More...](#details)

| Topics | |
| --- | --- |
|  | [GATT Client APIs](group__bt__gatt__client.md) |
|  | [GATT Server APIs](group__bt__gatt__server.md) |

| Data Structures | |
| --- | --- |
| struct | [bt\_gatt\_attr](structbt__gatt__attr.md) |
|  | GATT Attribute. [More...](structbt__gatt__attr.md#details) |
| struct | [bt\_gatt\_service\_static](structbt__gatt__service__static.md) |
|  | GATT Service structure. [More...](structbt__gatt__service__static.md#details) |
| struct | [bt\_gatt\_service](structbt__gatt__service.md) |
|  | GATT Service structure. [More...](structbt__gatt__service.md#details) |
| struct | [bt\_gatt\_service\_val](structbt__gatt__service__val.md) |
|  | Service Attribute Value. [More...](structbt__gatt__service__val.md#details) |
| struct | [bt\_gatt\_include](structbt__gatt__include.md) |
|  | Include Attribute Value. [More...](structbt__gatt__include.md#details) |
| struct | [bt\_gatt\_cb](structbt__gatt__cb.md) |
|  | GATT callback structure. [More...](structbt__gatt__cb.md#details) |
| struct | [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) |
|  | GATT authorization callback structure. [More...](structbt__gatt__authorization__cb.md#details) |
| struct | [bt\_gatt\_chrc](structbt__gatt__chrc.md) |
|  | Characteristic Attribute Value. [More...](structbt__gatt__chrc.md#details) |
| struct | [bt\_gatt\_cep](structbt__gatt__cep.md) |
|  | Characteristic Extended Properties Attribute Value. [More...](structbt__gatt__cep.md#details) |
| struct | [bt\_gatt\_ccc](structbt__gatt__ccc.md) |
|  | Client Characteristic Configuration Attribute Value. [More...](structbt__gatt__ccc.md#details) |
| struct | [bt\_gatt\_scc](structbt__gatt__scc.md) |
|  | Server Characteristic Configuration Attribute Value. [More...](structbt__gatt__scc.md#details) |
| struct | [bt\_gatt\_cpf](structbt__gatt__cpf.md) |
|  | GATT Characteristic Presentation Format Attribute Value. [More...](structbt__gatt__cpf.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_GATT\_ERR](#gaff31756c1bf8ee755e65b1e0fb689bb7)(\_att\_err) |
|  | Construct error return value for attribute read and write callbacks. |
| #define | [BT\_GATT\_CHRC\_BROADCAST](#ga86bddd8211e7466b0457173a0dd412f0)   0x01 |
|  | Characteristic Properties Bit field values. |
| #define | [BT\_GATT\_CHRC\_READ](#gaa243a11d6d8b3e3be815c0893e0220f3)   0x02 |
|  | Characteristic read property. |
| #define | [BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP](#ga9c029ca574eb3c5992685b279388ac85)   0x04 |
|  | Characteristic write without response property. |
| #define | [BT\_GATT\_CHRC\_WRITE](#gad482d8db34707e1f9da1d8e2ddd5507e)   0x08 |
|  | Characteristic write with response property. |
| #define | [BT\_GATT\_CHRC\_NOTIFY](#gab8cd9649bdfd125a26065a8ced762a98)   0x10 |
|  | Characteristic notify property. |
| #define | [BT\_GATT\_CHRC\_INDICATE](#gaa9639b9d655ea41767584b638add1f2b)   0x20 |
|  | Characteristic indicate property. |
| #define | [BT\_GATT\_CHRC\_AUTH](#gaab3a26a00f88a6eacd36f2841004204c)   0x40 |
|  | Characteristic Authenticated Signed Writes property. |
| #define | [BT\_GATT\_CHRC\_EXT\_PROP](#gac84d73a0ad50bfd149ad83181315de1a)   0x80 |
|  | Characteristic Extended Properties property. |
| #define | [BT\_GATT\_CEP\_RELIABLE\_WRITE](#gad1825f8deafc36d7e8f09c2835884fc6)   0x0001 |
|  | Characteristic Extended Properties Bit field values. |
| #define | [BT\_GATT\_CEP\_WRITABLE\_AUX](#ga64898ec8390c89c1fc5bdf0364220a43)   0x0002 |
| #define | [BT\_GATT\_CCC\_NOTIFY](#ga240a10df32aa7a256a103ceee7211f8d)   0x0001 |
|  | Client Characteristic Configuration Values. |
| #define | [BT\_GATT\_CCC\_INDICATE](#ga60ff2ddcc2e3148881a2f15745ba06e8)   0x0002 |
|  | Client Characteristic Configuration Indication. |
| #define | [BT\_GATT\_SCC\_BROADCAST](#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)   0x0001 |
|  | Server Characteristic Configuration Values. |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [bt\_gatt\_attr\_read\_func\_t](#ga57e36bf94652531964fd4237c203fe7b)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Attribute read callback. |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [bt\_gatt\_attr\_write\_func\_t](#ga3fd8527a0f3e8f3699dc0d3b0339eba1)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Attribute Value write implementation. |

| Enumerations | |
| --- | --- |
| enum | [bt\_gatt\_perm](#ga96e57500d2340a45badb23701cc43833) {     [BT\_GATT\_PERM\_NONE](#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) = 0 , [BT\_GATT\_PERM\_READ](#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) = BIT(0) , [BT\_GATT\_PERM\_WRITE](#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) = BIT(1) , [BT\_GATT\_PERM\_READ\_ENCRYPT](#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) = BIT(2) ,     [BT\_GATT\_PERM\_WRITE\_ENCRYPT](#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) = BIT(3) , [BT\_GATT\_PERM\_READ\_AUTHEN](#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) = BIT(4) , [BT\_GATT\_PERM\_WRITE\_AUTHEN](#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) = BIT(5) , [BT\_GATT\_PERM\_PREPARE\_WRITE](#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) = BIT(6) ,     [BT\_GATT\_PERM\_READ\_LESC](#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) = BIT(7) , [BT\_GATT\_PERM\_WRITE\_LESC](#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) = BIT(8)   } |
|  | GATT attribute permission bit field values. [More...](#ga96e57500d2340a45badb23701cc43833) |
| enum | { [BT\_GATT\_WRITE\_FLAG\_PREPARE](#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383) = BIT(0) , [BT\_GATT\_WRITE\_FLAG\_CMD](#gga11c5a2eb0b62de9a2493ad5335fae383a770df41b7d433e8ce349b19e4657ba78) = BIT(1) , [BT\_GATT\_WRITE\_FLAG\_EXECUTE](#gga11c5a2eb0b62de9a2493ad5335fae383ad4e8f43c03da10c15685bd1a0109708b) = BIT(2) } |
|  | GATT attribute write flags. [More...](#ga11c5a2eb0b62de9a2493ad5335fae383) |

## Detailed Description

Generic Attribute Profile (GATT).

## Macro Definition Documentation

## [◆ ](#ga60ff2ddcc2e3148881a2f15745ba06e8)BT\_GATT\_CCC\_INDICATE

| #define BT\_GATT\_CCC\_INDICATE   0x0002 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Client Characteristic Configuration Indication.

If set, changes to Characteristic Value shall be indicated.

## [◆ ](#ga240a10df32aa7a256a103ceee7211f8d)BT\_GATT\_CCC\_NOTIFY

| #define BT\_GATT\_CCC\_NOTIFY   0x0001 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Client Characteristic Configuration Values.

Client Characteristic Configuration Notification.

If set, changes to Characteristic Value shall be notified.

## [◆ ](#gad1825f8deafc36d7e8f09c2835884fc6)BT\_GATT\_CEP\_RELIABLE\_WRITE

| #define BT\_GATT\_CEP\_RELIABLE\_WRITE   0x0001 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic Extended Properties Bit field values.

## [◆ ](#ga64898ec8390c89c1fc5bdf0364220a43)BT\_GATT\_CEP\_WRITABLE\_AUX

| #define BT\_GATT\_CEP\_WRITABLE\_AUX   0x0002 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

## [◆ ](#gaab3a26a00f88a6eacd36f2841004204c)BT\_GATT\_CHRC\_AUTH

| #define BT\_GATT\_CHRC\_AUTH   0x40 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic Authenticated Signed Writes property.

If set, permits signed writes to the Characteristic Value.

## [◆ ](#ga86bddd8211e7466b0457173a0dd412f0)BT\_GATT\_CHRC\_BROADCAST

| #define BT\_GATT\_CHRC\_BROADCAST   0x01 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic Properties Bit field values.

Characteristic broadcast property.

If set, permits broadcasts of the Characteristic Value using Server Characteristic Configuration Descriptor.

## [◆ ](#gac84d73a0ad50bfd149ad83181315de1a)BT\_GATT\_CHRC\_EXT\_PROP

| #define BT\_GATT\_CHRC\_EXT\_PROP   0x80 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic Extended Properties property.

If set, additional characteristic properties are defined in the Characteristic Extended Properties Descriptor.

## [◆ ](#gaa9639b9d655ea41767584b638add1f2b)BT\_GATT\_CHRC\_INDICATE

| #define BT\_GATT\_CHRC\_INDICATE   0x20 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic indicate property.

If set, permits indications of a Characteristic Value with acknowledgment.

## [◆ ](#gab8cd9649bdfd125a26065a8ced762a98)BT\_GATT\_CHRC\_NOTIFY

| #define BT\_GATT\_CHRC\_NOTIFY   0x10 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic notify property.

If set, permits notifications of a Characteristic Value without acknowledgment.

## [◆ ](#gaa243a11d6d8b3e3be815c0893e0220f3)BT\_GATT\_CHRC\_READ

| #define BT\_GATT\_CHRC\_READ   0x02 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic read property.

If set, permits reads of the Characteristic Value.

## [◆ ](#gad482d8db34707e1f9da1d8e2ddd5507e)BT\_GATT\_CHRC\_WRITE

| #define BT\_GATT\_CHRC\_WRITE   0x08 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic write with response property.

If set, permits write of the Characteristic Value with response.

## [◆ ](#ga9c029ca574eb3c5992685b279388ac85)BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP

| #define BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP   0x04 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Characteristic write without response property.

If set, permits write of the Characteristic Value without response.

## [◆ ](#gaff31756c1bf8ee755e65b1e0fb689bb7)BT\_GATT\_ERR

| #define BT\_GATT\_ERR | ( |  | *\_att\_err* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

(-(\_att\_err))

Construct error return value for attribute read and write callbacks.

Parameters
:   | \_att\_err | ATT error code |
    | --- | --- |

Returns
:   Appropriate error code for the attribute callbacks.

## [◆ ](#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)BT\_GATT\_SCC\_BROADCAST

| #define BT\_GATT\_SCC\_BROADCAST   0x0001 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Server Characteristic Configuration Values.

Server Characteristic Configuration Broadcast

If set, the characteristic value shall be broadcast in the advertising data when the server is advertising.

## Typedef Documentation

## [◆ ](#ga57e36bf94652531964fd4237c203fe7b)bt\_gatt\_attr\_read\_func\_t

| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* bt\_gatt\_attr\_read\_func\_t) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Attribute read callback.

This is the type of the [bt\_gatt\_attr.read()](structbt__gatt__attr.md#a074abc719494ca35997a452f526e7ecc "Attribute Value read method.") method.

This function may safely assume the Attribute Permissions are satisfied for this read. Callers are responsible for this.

Callers may set `conn` to emulate a GATT client read, or leave it NULL for local reads.

Note
:   GATT server relies on this method to handle read operations from remote GATT clients. But this method is not reserved for the GATT server. E.g. You can lookup attributes in the local ATT database and invoke this method.
:   The GATT server propagates the return value from this method back to the remote client.

Parameters
:   | conn | The connection that is requesting to read. NULL if local. |
    | --- | --- |
    | attr | The attribute that's being read |
    | buf | Buffer to place the read result in |
    | len | Length of data to read |
    | offset | Offset to start reading from |

Returns
:   Number of bytes read, or in case of an error [BT\_GATT\_ERR()](#gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific BT\_ATT\_ERR\_\* error code.

## [◆ ](#ga3fd8527a0f3e8f3699dc0d3b0339eba1)bt\_gatt\_attr\_write\_func\_t

| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* bt\_gatt\_attr\_write\_func\_t) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Attribute Value write implementation.

This is the type of the [bt\_gatt\_attr.write()](structbt__gatt__attr.md#a1ecd78536067f4bded506e0daccefd35 "Attribute Value write method.") method.

This function may safely assume the Attribute Permissions are satisfied for this write. Callers are responsible for this.

Callers may set `conn` to emulate a GATT client write, or leave it NULL for local writes.

If `flags` contains [BT\_GATT\_WRITE\_FLAG\_PREPARE](#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383), then the method shall not perform a write, but instead only check if the write is authorized and return an error code if not.

Attribute Value write implementations can and often do have side effects besides potentially storing the value. E.g. togging an LED.

Note
:   GATT server relies on this method to handle write operations from remote GATT clients. But this method is not reserved for the GATT server. E.g. You can lookup attributes in the local ATT database and invoke this method.
:   The GATT server propagates the return value from this method back to the remote client.

Parameters
:   | conn | The connection that is requesting to write |
    | --- | --- |
    | attr | The attribute that's being written |
    | buf | Buffer with the data to write |
    | len | Number of bytes in the buffer |
    | offset | Offset to start writing from |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags (BT\_GATT\_WRITE\_FLAG\_\*) |

Returns
:   Number of bytes written, or in case of an error [BT\_GATT\_ERR()](#gaff31756c1bf8ee755e65b1e0fb689bb7) with a specific BT\_ATT\_ERR\_\* error code.

## Enumeration Type Documentation

## [◆ ](#ga11c5a2eb0b62de9a2493ad5335fae383)anonymous enum

| anonymous enum |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

GATT attribute write flags.

| Enumerator | |
| --- | --- |
| BT\_GATT\_WRITE\_FLAG\_PREPARE | Attribute prepare write flag.  If set, write callback should only check if the device is authorized but no data shall be written. |
| BT\_GATT\_WRITE\_FLAG\_CMD | Attribute write command flag.  If set, indicates that write operation is a command (Write without response) which doesn't generate any response. |
| BT\_GATT\_WRITE\_FLAG\_EXECUTE | Attribute write execute flag.  If set, indicates that write operation is a execute, which indicates the end of a long write, and will come after 1 or more [BT\_GATT\_WRITE\_FLAG\_PREPARE](#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383). |

## [◆ ](#ga96e57500d2340a45badb23701cc43833)bt\_gatt\_perm

| enum [bt\_gatt\_perm](#ga96e57500d2340a45badb23701cc43833) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

GATT attribute permission bit field values.

| Enumerator | |
| --- | --- |
| BT\_GATT\_PERM\_NONE | No operations supported, e.g.  for notify-only |
| BT\_GATT\_PERM\_READ | Attribute read permission. |
| BT\_GATT\_PERM\_WRITE | Attribute write permission. |
| BT\_GATT\_PERM\_READ\_ENCRYPT | Attribute read permission with encryption.  If set, requires encryption for read access. |
| BT\_GATT\_PERM\_WRITE\_ENCRYPT | Attribute write permission with encryption.  If set, requires encryption for write access. |
| BT\_GATT\_PERM\_READ\_AUTHEN | Attribute read permission with authentication.  If set, requires encryption using authenticated link-key for read access. |
| BT\_GATT\_PERM\_WRITE\_AUTHEN | Attribute write permission with authentication.  If set, requires encryption using authenticated link-key for write access. |
| BT\_GATT\_PERM\_PREPARE\_WRITE | Attribute prepare write permission.  If set, allows prepare writes with use of [BT\_GATT\_WRITE\_FLAG\_PREPARE](#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383) passed to write callback. |
| BT\_GATT\_PERM\_READ\_LESC | Attribute read permission with LE Secure Connection encryption.  If set, requires that LE Secure Connections is used for read access. |
| BT\_GATT\_PERM\_WRITE\_LESC | Attribute write permission with LE Secure Connection encryption.  If set, requires that LE Secure Connections is used for write access. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
