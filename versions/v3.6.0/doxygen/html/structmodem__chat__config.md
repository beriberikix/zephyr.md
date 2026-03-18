---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmodem__chat__config.html
original_path: doxygen/html/structmodem__chat__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_chat\_config Struct Reference

Chat configuration.
[More...](#details)

`#include <[chat.h](chat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [user\_data](#ac002d9f43309db8c3c35826127d94194) |
|  | Free to use user data passed with modem match callbacks. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#a295de98c2e8866059e7194c57d0502b7) |
|  | Receive buffer used to store parsed arguments. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a76f85951f5750f0d07b1253af118ec6f) |
|  | Size of receive buffer should be longest line + longest match. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [delimiter](#ab3adfaddd56884553a57467c762bdf98) |
|  | Delimiter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [delimiter\_size](#aa30ccfd372c47c64e2a7b7c840405499) |
|  | Size of delimiter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [filter](#af6646dee93b3279429eb95c87426168b) |
|  | Bytes which are discarded by parser. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter\_size](#af762b783d33e192ef45647e0b2e2d70b) |
|  | Size of filter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | [argv](#ae2afa6465bfad9c83dd57498165888b4) |
|  | Array of pointers used to point to parsed arguments. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [argv\_size](#a2cf551a0946459b2825595026ebc7490) |
|  | Elements in array of pointers. |
| const struct [modem\_chat\_match](structmodem__chat__match.md) \* | [unsol\_matches](#a661d96b8a7031b17e6f660c6e0e4be11) |
|  | Array of unsolicited matches. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [unsol\_matches\_size](#addfa7cacc676190d9e29c451d47ea3bd) |
|  | Elements in array of unsolicited matches. |

## Detailed Description

Chat configuration.

## Field Documentation

## [◆ ](#ae2afa6465bfad9c83dd57498165888b4)argv

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\*\* modem\_chat\_config::argv |
| --- |

Array of pointers used to point to parsed arguments.

## [◆ ](#a2cf551a0946459b2825595026ebc7490)argv\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_config::argv\_size |
| --- |

Elements in array of pointers.

## [◆ ](#ab3adfaddd56884553a57467c762bdf98)delimiter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_config::delimiter |
| --- |

Delimiter.

## [◆ ](#aa30ccfd372c47c64e2a7b7c840405499)delimiter\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_config::delimiter\_size |
| --- |

Size of delimiter.

## [◆ ](#af6646dee93b3279429eb95c87426168b)filter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_config::filter |
| --- |

Bytes which are discarded by parser.

## [◆ ](#af762b783d33e192ef45647e0b2e2d70b)filter\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_config::filter\_size |
| --- |

Size of filter.

## [◆ ](#a295de98c2e8866059e7194c57d0502b7)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_config::receive\_buf |
| --- |

Receive buffer used to store parsed arguments.

## [◆ ](#a76f85951f5750f0d07b1253af118ec6f)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_config::receive\_buf\_size |
| --- |

Size of receive buffer should be longest line + longest match.

## [◆ ](#a661d96b8a7031b17e6f660c6e0e4be11)unsol\_matches

| const struct [modem\_chat\_match](structmodem__chat__match.md)\* modem\_chat\_config::unsol\_matches |
| --- |

Array of unsolicited matches.

## [◆ ](#addfa7cacc676190d9e29c451d47ea3bd)unsol\_matches\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_config::unsol\_matches\_size |
| --- |

Elements in array of unsolicited matches.

## [◆ ](#ac002d9f43309db8c3c35826127d94194)user\_data

| void\* modem\_chat\_config::user\_data |
| --- |

Free to use user data passed with modem match callbacks.

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[chat.h](chat_8h_source.md)

- [modem\_chat\_config](structmodem__chat__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
