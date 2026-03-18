---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hci__evt__sync__conn__complete.html
original_path: doxygen/html/structbt__hci__evt__sync__conn__complete.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_sync\_conn\_complete Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#accd17a95f35ab1988122df7584830f60) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#aa48aa29ff73e93e8d961013f066c1b5e) |
| [bt\_addr\_t](structbt__addr__t.md) | [bdaddr](#a78f5560783400f1d1a63b2c9d69fa7ed) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [link\_type](#aacf9919945e9b755913da145f0fe78ae) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_interval](#a4b93873ad6f5388657511d87fc0a8c85) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retansmission\_window](#a68a31880c8aab9245be043c1719464d3) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_pkt\_length](#a6a455f56da4666cb602e6c05157e166d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_pkt\_length](#ab4d4106d5120f10e8300834db12740d8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [air\_mode](#a5f6068569bf649bcd1d13928f56f9703) |

## Field Documentation

## [◆ ](#a5f6068569bf649bcd1d13928f56f9703)air\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_sync\_conn\_complete::air\_mode |
| --- |

## [◆ ](#a78f5560783400f1d1a63b2c9d69fa7ed)bdaddr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_sync\_conn\_complete::bdaddr |
| --- |

## [◆ ](#aa48aa29ff73e93e8d961013f066c1b5e)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_sync\_conn\_complete::handle |
| --- |

## [◆ ](#aacf9919945e9b755913da145f0fe78ae)link\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_sync\_conn\_complete::link\_type |
| --- |

## [◆ ](#a68a31880c8aab9245be043c1719464d3)retansmission\_window

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_sync\_conn\_complete::retansmission\_window |
| --- |

## [◆ ](#a6a455f56da4666cb602e6c05157e166d)rx\_pkt\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_sync\_conn\_complete::rx\_pkt\_length |
| --- |

## [◆ ](#accd17a95f35ab1988122df7584830f60)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_sync\_conn\_complete::status |
| --- |

## [◆ ](#a4b93873ad6f5388657511d87fc0a8c85)tx\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_sync\_conn\_complete::tx\_interval |
| --- |

## [◆ ](#ab4d4106d5120f10e8300834db12740d8)tx\_pkt\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_sync\_conn\_complete::tx\_pkt\_length |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_sync\_conn\_complete](structbt__hci__evt__sync__conn__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
