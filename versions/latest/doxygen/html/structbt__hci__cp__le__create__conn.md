---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__cp__le__create__conn.html
original_path: doxygen/html/structbt__hci__cp__le__create__conn.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_create\_conn Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [scan\_interval](#a1a830a0f6cd961d534c338031b2b691b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [scan\_window](#abf61e67f5e20adc44b5b9314ed43bccc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter\_policy](#a2ca5063f5082a0f330676e56253a21c7) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#aa51da7602eb2b44528964c8b706bb043) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [own\_addr\_type](#a63c7f9e89528105e484a60e41eeb8a30) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_interval\_min](#a988cf154b0df1ff9af8d34ce73a920dd) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_interval\_max](#aa009d54866d9c675c2785412bdbd182f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_latency](#a5a9d5c1d44adac876680a517b1fad63f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supervision\_timeout](#ae8e0ad70a3b23ac035c237db0d57adc4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_ce\_len](#a476501ccd209f3a52082decf906ca8f0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_ce\_len](#a5b329aa8b48e03998e969b2436d35ab5) |

## Field Documentation

## [◆ ](#aa009d54866d9c675c2785412bdbd182f)conn\_interval\_max

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::conn\_interval\_max |
| --- |

## [◆ ](#a988cf154b0df1ff9af8d34ce73a920dd)conn\_interval\_min

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::conn\_interval\_min |
| --- |

## [◆ ](#a5a9d5c1d44adac876680a517b1fad63f)conn\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::conn\_latency |
| --- |

## [◆ ](#a2ca5063f5082a0f330676e56253a21c7)filter\_policy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_create\_conn::filter\_policy |
| --- |

## [◆ ](#a5b329aa8b48e03998e969b2436d35ab5)max\_ce\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::max\_ce\_len |
| --- |

## [◆ ](#a476501ccd209f3a52082decf906ca8f0)min\_ce\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::min\_ce\_len |
| --- |

## [◆ ](#a63c7f9e89528105e484a60e41eeb8a30)own\_addr\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_create\_conn::own\_addr\_type |
| --- |

## [◆ ](#aa51da7602eb2b44528964c8b706bb043)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_cp\_le\_create\_conn::peer\_addr |
| --- |

## [◆ ](#a1a830a0f6cd961d534c338031b2b691b)scan\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::scan\_interval |
| --- |

## [◆ ](#abf61e67f5e20adc44b5b9314ed43bccc)scan\_window

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::scan\_window |
| --- |

## [◆ ](#ae8e0ad70a3b23ac035c237db0d57adc4)supervision\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_create\_conn::supervision\_timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_create\_conn](structbt__hci__cp__le__create__conn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
