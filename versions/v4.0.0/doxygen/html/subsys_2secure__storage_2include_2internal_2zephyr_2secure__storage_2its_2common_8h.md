---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html
original_path: doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h File Reference

Common definitions of the secure storage subsystem's ITS APIs.
[More...](#details)

`#include "[../common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.md)"`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[psa/storage_common.h](storage__common_8h_source.md)>`

[Go to the source code of this file.](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) |
|  | The UID (caller + entry IDs) of an ITS entry. [More...](structsecure__storage__its__uid__t.md#details) |

| Enumerations | |
| --- | --- |
| enum | [secure\_storage\_its\_caller\_id\_t](#a2369ff303bf323cb4e57f1b970093d2b) { [SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS](#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd) , [SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS](#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d) , [SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS](#a2369ff303bf323cb4e57f1b970093d2ba22e2c3976fbb36461f6587372ce9314b) } |
|  | The ID of the caller from which the ITS API call originates. [More...](#a2369ff303bf323cb4e57f1b970093d2b) |

## Detailed Description

Common definitions of the secure storage subsystem's ITS APIs.

## Enumeration Type Documentation

## [◆ ](#a2369ff303bf323cb4e57f1b970093d2b)secure\_storage\_its\_caller\_id\_t

| enum [secure\_storage\_its\_caller\_id\_t](#a2369ff303bf323cb4e57f1b970093d2b) |
| --- |

The ID of the caller from which the ITS API call originates.

This is used to prevent ID collisions between different callers that are not aware of each other and so might use the same numerical IDs, e.g. PSA Crypto and PSA ITS.

| Enumerator | |
| --- | --- |
| SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS |  |
| SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS |  |
| SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS |  |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
