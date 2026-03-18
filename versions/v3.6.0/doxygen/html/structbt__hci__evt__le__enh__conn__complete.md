---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__evt__le__enh__conn__complete.html
original_path: doxygen/html/structbt__hci__evt__le__enh__conn__complete.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_enh\_conn\_complete Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#ae26575416658bf285c45f57ddf426eb2) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#a13ceff445de6a89f6ea0e832e8b3fba9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [role](#af24298f8c1d58882b4962a14086fc5c7) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a4906d6991489e95f8c74aacf5ad8c22e) |
| [bt\_addr\_t](structbt__addr__t.md) | [local\_rpa](#ab275bcb4a3dd09525b446c01e4e5fdad) |
| [bt\_addr\_t](structbt__addr__t.md) | [peer\_rpa](#a4ece4379733f1ab404fa03f4794192a4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#ac0565ecf0c459275d147933bbdaa9fbc) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#a7276bf433c21ffcd3582463492af107b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supv\_timeout](#aa99df131f3fb0330ff8051015d2b78dc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clock\_accuracy](#a5641e5cb17df4613cd85f5ad3ba8541c) |

## Field Documentation

## [◆ ](#a5641e5cb17df4613cd85f5ad3ba8541c)clock\_accuracy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete::clock\_accuracy |
| --- |

## [◆ ](#a13ceff445de6a89f6ea0e832e8b3fba9)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete::handle |
| --- |

## [◆ ](#ac0565ecf0c459275d147933bbdaa9fbc)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete::interval |
| --- |

## [◆ ](#a7276bf433c21ffcd3582463492af107b)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete::latency |
| --- |

## [◆ ](#ab275bcb4a3dd09525b446c01e4e5fdad)local\_rpa

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete::local\_rpa |
| --- |

## [◆ ](#a4906d6991489e95f8c74aacf5ad8c22e)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_addr |
| --- |

## [◆ ](#a4ece4379733f1ab404fa03f4794192a4)peer\_rpa

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_evt\_le\_enh\_conn\_complete::peer\_rpa |
| --- |

## [◆ ](#af24298f8c1d58882b4962a14086fc5c7)role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete::role |
| --- |

## [◆ ](#ae26575416658bf285c45f57ddf426eb2)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_enh\_conn\_complete::status |
| --- |

## [◆ ](#aa99df131f3fb0330ff8051015d2b78dc)supv\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_enh\_conn\_complete::supv\_timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_enh\_conn\_complete](structbt__hci__evt__le__enh__conn__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
