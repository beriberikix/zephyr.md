---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html
original_path: doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h File Reference

Common definitions of the secure storage subsystem.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SECURE\_STORAGE\_ALL\_CREATE\_FLAGS](#ae07ad04cdb4e399b0751f58415d5e514) |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secure\_storage\_packed\_create\_flags\_t](#ac3c7c0ba918fe964b4c39ae0d8047bdd) |

## Detailed Description

Common definitions of the secure storage subsystem.

## Macro Definition Documentation

## [◆ ](#ae07ad04cdb4e399b0751f58415d5e514)SECURE\_STORAGE\_ALL\_CREATE\_FLAGS

| #define SECURE\_STORAGE\_ALL\_CREATE\_FLAGS |
| --- |

**Value:**

([PSA\_STORAGE\_FLAG\_NONE](storage__common_8h.md#a65299349e8643d466eeaeb5bb62cfb6e) | \

[PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd) | \

[PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY](storage__common_8h.md#ab3688fcb77630ebdb3774516560b5226) | \

[PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION](storage__common_8h.md#a5781482a6bea58c8f9acdb1da921efbe))

[PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd)

#define PSA\_STORAGE\_FLAG\_WRITE\_ONCE

The data associated with the UID will not be able to be modified or deleted.

**Definition** storage\_common.h:31

[PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION](storage__common_8h.md#a5781482a6bea58c8f9acdb1da921efbe)

#define PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION

The data associated with the UID does not require replay protection.

**Definition** storage\_common.h:35

[PSA\_STORAGE\_FLAG\_NONE](storage__common_8h.md#a65299349e8643d466eeaeb5bb62cfb6e)

#define PSA\_STORAGE\_FLAG\_NONE

No flag to pass.

**Definition** storage\_common.h:29

[PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY](storage__common_8h.md#ab3688fcb77630ebdb3774516560b5226)

#define PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY

The data associated with the UID is public, requiring only integrity.

**Definition** storage\_common.h:33

## Typedef Documentation

## [◆ ](#ac3c7c0ba918fe964b4c39ae0d8047bdd)secure\_storage\_packed\_create\_flags\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secure\_storage\_packed\_create\_flags\_t](#ac3c7c0ba918fe964b4c39ae0d8047bdd) |
| --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
