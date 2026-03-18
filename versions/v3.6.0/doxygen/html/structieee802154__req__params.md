---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__req__params.html
original_path: doxygen/html/structieee802154__req__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_req\_params Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Net Management](group__ieee802154__mgmt.md)

Scanning parameters.
[More...](#details)

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [channel\_set](#ad49071ae3c35a548f6894d32be017ad7) |
|  | The set of channels to scan, use above macros to manage it. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [duration](#a75b3e1658829dfa4970cef7267250c9b) |
|  | Duration of scan, per-channel, in milliseconds. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [channel](#a78c9f6b62c7cfc51f514df09a2719441) |
|  | Current channel in use as a result. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pan\_id](#abde2cf05ea51cd0e024552aaf2414c86) |
|  | Current pan\_id in use as a result. |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [short\_addr](#a9cafc55c59dc4eff07bdf03e60da07ec) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [addr](#aa1b2ea9ffb009a1b6255a9e57ddef9f7) [8] |  |
| }; |  |
|  | Result address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a8c63caa3ae260f4c6f9bebe71677673b) |
|  | length of address |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [lqi](#af08c2fa32367340c54c8d8bf9c46f34a) |
|  | Link quality information, between 0 and 255. |

## Detailed Description

Scanning parameters.

Used to request a scan and get results as well, see section 8.2.11.2

## Field Documentation

## [◆ ](#a591ec123b8009042260d51a6c134a11d)[union]

| union { ... } [ieee802154\_req\_params](structieee802154__req__params.md) |
| --- |

Result address.

## [◆ ](#aa1b2ea9ffb009a1b6255a9e57ddef9f7)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_req\_params::addr[8] |
| --- |

## [◆ ](#a78c9f6b62c7cfc51f514df09a2719441)channel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_req\_params::channel |
| --- |

Current channel in use as a result.

## [◆ ](#ad49071ae3c35a548f6894d32be017ad7)channel\_set

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_req\_params::channel\_set |
| --- |

The set of channels to scan, use above macros to manage it.

## [◆ ](#a75b3e1658829dfa4970cef7267250c9b)duration

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_req\_params::duration |
| --- |

Duration of scan, per-channel, in milliseconds.

## [◆ ](#a8c63caa3ae260f4c6f9bebe71677673b)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_req\_params::len |
| --- |

length of address

## [◆ ](#af08c2fa32367340c54c8d8bf9c46f34a)lqi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_req\_params::lqi |
| --- |

Link quality information, between 0 and 255.

## [◆ ](#abde2cf05ea51cd0e024552aaf2414c86)pan\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_req\_params::pan\_id |
| --- |

Current pan\_id in use as a result.

## [◆ ](#a9cafc55c59dc4eff07bdf03e60da07ec)short\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_req\_params::short\_addr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_mgmt.h](ieee802154__mgmt_8h_source.md)

- [ieee802154\_req\_params](structieee802154__req__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
