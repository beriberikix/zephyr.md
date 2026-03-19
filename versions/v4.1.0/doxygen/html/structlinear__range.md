---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlinear__range.html
original_path: doxygen/html/structlinear__range.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linear\_range Struct Reference

[Utilities](group__utilities.md) » [Linear Range](group__linear__range.md)

Linear range.
[More...](#details)

`#include <[linear_range.h](linear__range_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [min](#a4523369fa49fa1d6aa58f0d2634eb41d) |
|  | Minimum value. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [step](#a963889c27dd8541f7cd6528ac82401b3) |
|  | Step value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_idx](#a705275f156fc4bcf5bb111be01aff6ef) |
|  | Minimum index (must be <= maximum index). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_idx](#a84af63957a1b3e829cf1d53fa6342982) |
|  | Maximum index (must be >= minimum index). |

## Detailed Description

Linear range.

## Field Documentation

## [◆ ](#a84af63957a1b3e829cf1d53fa6342982)max\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) linear\_range::max\_idx |
| --- |

Maximum index (must be >= minimum index).

## [◆ ](#a4523369fa49fa1d6aa58f0d2634eb41d)min

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) linear\_range::min |
| --- |

Minimum value.

## [◆ ](#a705275f156fc4bcf5bb111be01aff6ef)min\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) linear\_range::min\_idx |
| --- |

Minimum index (must be <= maximum index).

## [◆ ](#a963889c27dd8541f7cd6528ac82401b3)step

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) linear\_range::step |
| --- |

Step value.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[linear\_range.h](linear__range_8h_source.md)

- [linear\_range](structlinear__range.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
