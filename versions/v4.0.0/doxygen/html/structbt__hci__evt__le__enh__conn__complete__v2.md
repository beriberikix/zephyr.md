---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__le__enh__conn__complete__v2.html
original_path: doxygen/html/structbt__hci__evt__le__enh__conn__complete__v2.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_enh\_conn\_complete\_v2 Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#ad72ba07d766135a94474a9d004da1a66) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#affe2dba0634e0215579fb13d77016a8c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [role](#a3343de57a24fa2ebdccf9411f388817d) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a7df28c9ddec607d5a84572bb421b7f5a) |
| [bt\_addr\_t](structbt__addr__t.md) | [local\_rpa](#a10a1cbf0e9e21bc127dc64adadd53773) |
| [bt\_addr\_t](structbt__addr__t.md) | [peer\_rpa](#a014e8bf891684c4cd9e5ec53d986d412) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a237b8313970cc63b7e57c0ce4913392e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#a3daa32ac19c4eda4a49bebb64f3145be) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supv\_timeout](#a2b2ac4890eb9604a3f5cd40f55c2c066) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clock\_accuracy](#a7bb168061803d1122e8ee47dc8af3ae9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_handle](#a883ba3aed9aed00ec0ce425999d97180) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_handle](#a81dca94a6f2a8ea3da7a5a316daa5941) |

## Field Documentation

## [◆ ](#a883ba3aed9aed00ec0ce425999d97180)adv\_handle

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::adv\_handle |
| --- |

## [◆ ](#a7bb168061803d1122e8ee47dc8af3ae9)clock\_accuracy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::clock\_accuracy |
| --- |

## [◆ ](#affe2dba0634e0215579fb13d77016a8c)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::handle |
| --- |

## [◆ ](#a237b8313970cc63b7e57c0ce4913392e)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::interval |
| --- |

## [◆ ](#a3daa32ac19c4eda4a49bebb64f3145be)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::latency |
| --- |

## [◆ ](#a10a1cbf0e9e21bc127dc64adadd53773)local\_rpa

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::local\_rpa |
| --- |

## [◆ ](#a7df28c9ddec607d5a84572bb421b7f5a)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_addr |
| --- |

## [◆ ](#a014e8bf891684c4cd9e5ec53d986d412)peer\_rpa

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::peer\_rpa |
| --- |

## [◆ ](#a3343de57a24fa2ebdccf9411f388817d)role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::role |
| --- |

## [◆ ](#ad72ba07d766135a94474a9d004da1a66)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::status |
| --- |

## [◆ ](#a2b2ac4890eb9604a3f5cd40f55c2c066)supv\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::supv\_timeout |
| --- |

## [◆ ](#a81dca94a6f2a8ea3da7a5a316daa5941)sync\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete\_v2::sync\_handle |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_enh\_conn\_complete\_v2](structbt__hci__evt__le__enh__conn__complete__v2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
