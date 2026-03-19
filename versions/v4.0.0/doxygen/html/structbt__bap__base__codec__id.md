---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__base__codec__id.html
original_path: doxygen/html/structbt__bap__base__codec__id.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_base\_codec\_id Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md)

Codec ID structure for a Broadcast Audio Source Endpoint (BASE).
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a9031aaf6a3f6e0acf68f1bfaed39b819) |
|  | Codec ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a0aadd7e53f72efd8c0e33dd9a8eca177) |
|  | Codec Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#a49802819cc3129a993320b95472f2262) |
|  | Codec Company Vendor ID. |

## Detailed Description

Codec ID structure for a Broadcast Audio Source Endpoint (BASE).

## Field Documentation

## [◆ ](#a0aadd7e53f72efd8c0e33dd9a8eca177)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_base\_codec\_id::cid |
| --- |

Codec Company ID.

## [◆ ](#a9031aaf6a3f6e0acf68f1bfaed39b819)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_base\_codec\_id::id |
| --- |

Codec ID.

## [◆ ](#a49802819cc3129a993320b95472f2262)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_base\_codec\_id::vid |
| --- |

Codec Company Vendor ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
