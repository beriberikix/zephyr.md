---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__extended__inquiry__result.html
original_path: doxygen/html/structbt__hci__evt__extended__inquiry__result.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_extended\_inquiry\_result Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_reports](#a76e4e82d1dedaee94bd730a4134d7d77) |
| [bt\_addr\_t](structbt__addr__t.md) | [addr](#a955a7d36736badfae1f39fa9eda61ebb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pscan\_rep\_mode](#aba4aac84e23ca9d283cb8af265dcaf0d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#ab6ec4b5efe058e225d173cbda9a16f2e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cod](#ab4ebcf09817827d1d10ddeee13832759) [3] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [clock\_offset](#a30c5586d954585006238e8c2b33a7601) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a21f7f48422bcfb867c9ca2e4411a2fbd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [eir](#a1eba2841941f7cdbb00f548ebf0485e9) [240] |

## Field Documentation

## [◆ ](#a955a7d36736badfae1f39fa9eda61ebb)addr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_extended\_inquiry\_result::addr |
| --- |

## [◆ ](#a30c5586d954585006238e8c2b33a7601)clock\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_extended\_inquiry\_result::clock\_offset |
| --- |

## [◆ ](#ab4ebcf09817827d1d10ddeee13832759)cod

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_extended\_inquiry\_result::cod[3] |
| --- |

## [◆ ](#a1eba2841941f7cdbb00f548ebf0485e9)eir

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_extended\_inquiry\_result::eir[240] |
| --- |

## [◆ ](#a76e4e82d1dedaee94bd730a4134d7d77)num\_reports

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_extended\_inquiry\_result::num\_reports |
| --- |

## [◆ ](#aba4aac84e23ca9d283cb8af265dcaf0d)pscan\_rep\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_extended\_inquiry\_result::pscan\_rep\_mode |
| --- |

## [◆ ](#ab6ec4b5efe058e225d173cbda9a16f2e)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_extended\_inquiry\_result::reserved |
| --- |

## [◆ ](#a21f7f48422bcfb867c9ca2e4411a2fbd)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_evt\_extended\_inquiry\_result::rssi |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_extended\_inquiry\_result](structbt__hci__evt__extended__inquiry__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
