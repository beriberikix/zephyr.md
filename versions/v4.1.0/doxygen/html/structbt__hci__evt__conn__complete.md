---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__conn__complete.html
original_path: doxygen/html/structbt__hci__evt__conn__complete.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_conn\_complete Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a3dbf4fef53279003b7304ffee4a55e56) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#ad8877912008ea7445a67abc43aab5021) |
| [bt\_addr\_t](structbt__addr__t.md) | [bdaddr](#a60a2ca6a8f16e4562c12b369685efa9b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [link\_type](#afd9a21adf7d35205fb7e222c2e9e0328) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [encr\_enabled](#a975617e8b568675a3ed8883cbe411557) |

## Field Documentation

## [◆ ](#a60a2ca6a8f16e4562c12b369685efa9b)bdaddr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_conn\_complete::bdaddr |
| --- |

## [◆ ](#a975617e8b568675a3ed8883cbe411557)encr\_enabled

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_conn\_complete::encr\_enabled |
| --- |

## [◆ ](#ad8877912008ea7445a67abc43aab5021)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_conn\_complete::handle |
| --- |

## [◆ ](#afd9a21adf7d35205fb7e222c2e9e0328)link\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_conn\_complete::link\_type |
| --- |

## [◆ ](#a3dbf4fef53279003b7304ffee4a55e56)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_conn\_complete::status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_conn\_complete](structbt__hci__evt__conn__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
