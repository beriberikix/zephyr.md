---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__le__past__received.html
original_path: doxygen/html/structbt__hci__evt__le__past__received.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_past\_received Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a1b2c229c99d06f44057b88458f168e7c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a1bdbaddb4003cea40738ee540ecb8789) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [service\_data](#adaa1e432db60a2529ad6266f16604e15) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_handle](#a2cea2f3b9d51ace91ddf63639e821328) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_sid](#a110c7cdd2ff1178d1ca686abaae92b05) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a3e368e95a6831f823d2efa0c0bc1ef51) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#aedb668e6f3232b1db9035ea89ccf1b71) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a41ea6099d3cca1caf37ff518a4e95492) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clock\_accuracy](#a00d570636a55c1d84723ad3bc5705d80) |

## Field Documentation

## [◆ ](#a3e368e95a6831f823d2efa0c0bc1ef51)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_past\_received::addr |
| --- |

## [◆ ](#a110c7cdd2ff1178d1ca686abaae92b05)adv\_sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received::adv\_sid |
| --- |

## [◆ ](#a00d570636a55c1d84723ad3bc5705d80)clock\_accuracy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received::clock\_accuracy |
| --- |

## [◆ ](#a1bdbaddb4003cea40738ee540ecb8789)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received::conn\_handle |
| --- |

## [◆ ](#a41ea6099d3cca1caf37ff518a4e95492)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received::interval |
| --- |

## [◆ ](#aedb668e6f3232b1db9035ea89ccf1b71)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received::phy |
| --- |

## [◆ ](#adaa1e432db60a2529ad6266f16604e15)service\_data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received::service\_data |
| --- |

## [◆ ](#a1b2c229c99d06f44057b88458f168e7c)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received::status |
| --- |

## [◆ ](#a2cea2f3b9d51ace91ddf63639e821328)sync\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received::sync\_handle |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_past\_received](structbt__hci__evt__le__past__received.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
