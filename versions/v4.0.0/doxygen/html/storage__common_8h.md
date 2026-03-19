---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/storage__common_8h.html
original_path: doxygen/html/storage__common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

storage\_common.h File Reference

[Operating System Services](group__os__services.md) » [PSA Secure Storage API](group__psa__secure__storage.md)

Common definitions of the PSA Secure Storage API.
[More...](#details)

`#include <[psa/error.h](subsys_2secure__storage_2include_2psa_2error_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](storage__common_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [psa\_storage\_info\_t](structpsa__storage__info__t.md) |
|  | Metadata associated with a specific entry. [More...](structpsa__storage__info__t.md#details) |
| #define | [PSA\_STORAGE\_FLAG\_NONE](#a65299349e8643d466eeaeb5bb62cfb6e)   0u |
|  | No flag to pass. |
| #define | [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](#a15dbec8d862073de6024924bf015dcdd)   (1u << 0) |
|  | The data associated with the UID will not be able to be modified or deleted. |
| #define | [PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY](#ab3688fcb77630ebdb3774516560b5226)   (1u << 1) |
|  | The data associated with the UID is public, requiring only integrity. |
| #define | [PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION](#a5781482a6bea58c8f9acdb1da921efbe)   (1u << 2) |
|  | The data associated with the UID does not require replay protection. |
| #define | [PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED](#ad9f16fc478036752ffb2ce9e50b2a710)   (1u << 0) |
|  | Flag indicating that [psa\_ps\_create()](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508 "psa_ps_create()") and [psa\_ps\_set\_extended()](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a "psa_ps_set_extended()") are supported. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [psa\_storage\_uid\_t](#ae9154910f4f350c3b467b55d541a21a6) |
|  | UID type for identifying entries. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [psa\_storage\_create\_flags\_t](#a1f53bd4fd1ba72bd88e9d7d9eb7da211) |
|  | Flags used when creating an entry. |

## Detailed Description

Common definitions of the PSA Secure Storage API.

## Macro Definition Documentation

## [◆ ](#ab3688fcb77630ebdb3774516560b5226)PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY

| #define PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY   (1u << 1) |
| --- |

The data associated with the UID is public, requiring only integrity.

## [◆ ](#a5781482a6bea58c8f9acdb1da921efbe)PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION

| #define PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION   (1u << 2) |
| --- |

The data associated with the UID does not require replay protection.

## [◆ ](#a65299349e8643d466eeaeb5bb62cfb6e)PSA\_STORAGE\_FLAG\_NONE

| #define PSA\_STORAGE\_FLAG\_NONE   0u |
| --- |

No flag to pass.

## [◆ ](#a15dbec8d862073de6024924bf015dcdd)PSA\_STORAGE\_FLAG\_WRITE\_ONCE

| #define PSA\_STORAGE\_FLAG\_WRITE\_ONCE   (1u << 0) |
| --- |

The data associated with the UID will not be able to be modified or deleted.

## [◆ ](#ad9f16fc478036752ffb2ce9e50b2a710)PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED

| #define PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED   (1u << 0) |
| --- |

Flag indicating that [psa\_ps\_create()](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508 "psa_ps_create()") and [psa\_ps\_set\_extended()](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a "psa_ps_set_extended()") are supported.

## Typedef Documentation

## [◆ ](#a1f53bd4fd1ba72bd88e9d7d9eb7da211)psa\_storage\_create\_flags\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psa\_storage\_create\_flags\_t](#a1f53bd4fd1ba72bd88e9d7d9eb7da211) |
| --- |

Flags used when creating an entry.

## [◆ ](#ae9154910f4f350c3b467b55d541a21a6)psa\_storage\_uid\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [psa\_storage\_uid\_t](#ae9154910f4f350c3b467b55d541a21a6) |
| --- |

UID type for identifying entries.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [storage\_common.h](storage__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
