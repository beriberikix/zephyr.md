---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hci__cp__le__ext__create__conn.html
original_path: doxygen/html/structbt__hci__cp__le__ext__create__conn.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_ext\_create\_conn Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter\_policy](#a0561b446effa3f735a405c0b307466bf) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [own\_addr\_type](#a12a99044f54e3d5dae30a64392444cbf) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a79bc55d9f5b1d719de4fb404db9008f3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phys](#ae859ff0da5e9cdc872943fd74774ef7e) |
| struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) | [p](#acdb436d6bf2864745ec579622ae0d532) [0] |

## Field Documentation

## [◆ ](#a0561b446effa3f735a405c0b307466bf)filter\_policy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn::filter\_policy |
| --- |

## [◆ ](#a12a99044f54e3d5dae30a64392444cbf)own\_addr\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn::own\_addr\_type |
| --- |

## [◆ ](#acdb436d6bf2864745ec579622ae0d532)p

| struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) bt\_hci\_cp\_le\_ext\_create\_conn::p[0] |
| --- |

## [◆ ](#a79bc55d9f5b1d719de4fb404db9008f3)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_cp\_le\_ext\_create\_conn::peer\_addr |
| --- |

## [◆ ](#ae859ff0da5e9cdc872943fd74774ef7e)phys

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn::phys |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_ext\_create\_conn](structbt__hci__cp__le__ext__create__conn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
