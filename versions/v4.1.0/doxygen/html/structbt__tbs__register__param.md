---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__tbs__register__param.html
original_path: doxygen/html/structbt__tbs__register__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tbs\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Telephone Bearer Service (TBS)](group__bt__tbs.md)

Parameters for registering a Telephone Bearer Service.
[More...](#details)

`#include <[tbs.h](tbs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [provider\_name](#a8cf7713269e8bb193c61be01d6971922) |
|  | The name of the provider, for example a cellular service provider. |
| char \* | [uci](#ab7a0dc41a9e4c898ffd1afaffdfae51d) |
|  | The Uniform Caller Identifier of the bearer. |
| char \* | [uri\_schemes\_supported](#a4ffe59cd6d00b9b45db304b17efa22b0) |
|  | The Uniform Resource Identifiers schemes supported by this bearer as an UTF-8 string. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gtbs](#aa38a646b7121b555846f7acea9bc9365) |
|  | Whether this bearer shall be registered as a Generic Telephone Bearer server. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [authorization\_required](#af88bfd0ac0e83f94e9e467064b4c6c32) |
|  | Whether the application will need to authorize changes to calls. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [technology](#a248601152be83c807671e2ed635a36a7) |
|  | The technology of the bearer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [supported\_features](#a3539dcc4f088a643634aef39a0783726) |
|  | The optional supported features of the bearer. |

## Detailed Description

Parameters for registering a Telephone Bearer Service.

## Field Documentation

## [◆ ](#af88bfd0ac0e83f94e9e467064b4c6c32)authorization\_required

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_tbs\_register\_param::authorization\_required |
| --- |

Whether the application will need to authorize changes to calls.

If set to false then the service will automatically accept write requests from clients.

## [◆ ](#aa38a646b7121b555846f7acea9bc9365)gtbs

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_tbs\_register\_param::gtbs |
| --- |

Whether this bearer shall be registered as a Generic Telephone Bearer server.

A GTBS shall be registered before any non-GTBS services. There can only be a single GTBS registered.

## [◆ ](#a8cf7713269e8bb193c61be01d6971922)provider\_name

| char\* bt\_tbs\_register\_param::provider\_name |
| --- |

The name of the provider, for example a cellular service provider.

## [◆ ](#a3539dcc4f088a643634aef39a0783726)supported\_features

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_tbs\_register\_param::supported\_features |
| --- |

The optional supported features of the bearer.

See the BT\_TBS\_FEATURE\_\* values.

## [◆ ](#a248601152be83c807671e2ed635a36a7)technology

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_tbs\_register\_param::technology |
| --- |

The technology of the bearer.

See the BT\_TBS\_TECHNOLOGY\_\* values.

## [◆ ](#ab7a0dc41a9e4c898ffd1afaffdfae51d)uci

| char\* bt\_tbs\_register\_param::uci |
| --- |

The Uniform Caller Identifier of the bearer.

See the Uniform Caller Identifiers table in Bluetooth Assigned Numbers

## [◆ ](#a4ffe59cd6d00b9b45db304b17efa22b0)uri\_schemes\_supported

| char\* bt\_tbs\_register\_param::uri\_schemes\_supported |
| --- |

The Uniform Resource Identifiers schemes supported by this bearer as an UTF-8 string.

See [https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) for possible values. If multiple values are used, these shall be comma separated, e.g. "tel,skype".

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tbs.h](tbs_8h_source.md)

- [bt\_tbs\_register\_param](structbt__tbs__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
