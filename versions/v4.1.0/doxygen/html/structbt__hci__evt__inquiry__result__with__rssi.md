---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__inquiry__result__with__rssi.html
original_path: doxygen/html/structbt__hci__evt__inquiry__result__with__rssi.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_inquiry\_result\_with\_rssi Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_t](structbt__addr__t.md) | [addr](#af955dd1660f83e41e6d1b2b5aecf8133) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pscan\_rep\_mode](#a0a5c188d0d40b4259cbeb613c0dd12cf) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#a09914ee9998c0b59cb35ed74d08aa4f2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cod](#ad9b4920e2864ed8350de038dffe64574) [3] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [clock\_offset](#a1ee08f85103581994a88345cc94d7494) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a6d19e6400d7015db7122516e570d7989) |

## Field Documentation

## [◆ ](#af955dd1660f83e41e6d1b2b5aecf8133)addr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_inquiry\_result\_with\_rssi::addr |
| --- |

## [◆ ](#a1ee08f85103581994a88345cc94d7494)clock\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_inquiry\_result\_with\_rssi::clock\_offset |
| --- |

## [◆ ](#ad9b4920e2864ed8350de038dffe64574)cod

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_inquiry\_result\_with\_rssi::cod[3] |
| --- |

## [◆ ](#a0a5c188d0d40b4259cbeb613c0dd12cf)pscan\_rep\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_inquiry\_result\_with\_rssi::pscan\_rep\_mode |
| --- |

## [◆ ](#a09914ee9998c0b59cb35ed74d08aa4f2)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_inquiry\_result\_with\_rssi::reserved |
| --- |

## [◆ ](#a6d19e6400d7015db7122516e570d7989)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_evt\_inquiry\_result\_with\_rssi::rssi |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_inquiry\_result\_with\_rssi](structbt__hci__evt__inquiry__result__with__rssi.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
