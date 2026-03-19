---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__le__cs__step__data__mode__0__initiator.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__mode__0__initiator.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator Struct Reference

Subevent result step data format: Mode 0 Initiator.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_bit\_errors](#a339252cacafd05e85c0fb19776343e17): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_aa\_check](#a811eb38a04e63b12be9e25291126ccc1): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_rssi](#a11edf6e1c1da5d24aa1136521a249f52) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_antenna](#ad9a2193cbe5381d30494dbf6f8d84482) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [measured\_freq\_offset](#a48fc1fd87869d4ca2b70c42d5c4e1d75) |

## Detailed Description

Subevent result step data format: Mode 0 Initiator.

## Field Documentation

## [◆ ](#a48fc1fd87869d4ca2b70c42d5c4e1d75)measured\_freq\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::measured\_freq\_offset |
| --- |

## [◆ ](#ad9a2193cbe5381d30494dbf6f8d84482)packet\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_antenna |
| --- |

## [◆ ](#a811eb38a04e63b12be9e25291126ccc1)packet\_quality\_aa\_check

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_quality\_aa\_check |
| --- |

## [◆ ](#a339252cacafd05e85c0fb19776343e17)packet\_quality\_bit\_errors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_quality\_bit\_errors |
| --- |

## [◆ ](#a11edf6e1c1da5d24aa1136521a249f52)packet\_rssi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator::packet\_rssi |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator](structbt__hci__le__cs__step__data__mode__0__initiator.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
