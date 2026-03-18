---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structinput__kbd__matrix__common__config.html
original_path: doxygen/html/structinput__kbd__matrix__common__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_kbd\_matrix\_common\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Keyboard Matrix API](group__input__kbd__matrix.md)

Common keyboard matrix config.
[More...](#details)

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md) \* | [api](#ace0bafa079826819b7df7950cb3e8212) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [row\_size](#af3c4f2bcddf50dc2dbf0ad0e54230565) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [col\_size](#adfb2b978f1d41bdff28acca17cc4ed3d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [poll\_period\_us](#a34ce838e3ed4a5cb19c8ce961a9da947) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [poll\_timeout\_ms](#a81ccf8e0a1f49361f55737e0149bd656) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [debounce\_down\_us](#a004cb35eede1e58b27730a46155540e9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [debounce\_up\_us](#a545fba8a03ced44a95d7bb7f345d763f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [settle\_time\_us](#a13374b57becd9314ea726ae888f1702a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ghostkey\_check](#a2377a3c7cbd195bb6da3d4dfaf1f5972) |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \* | [actual\_key\_mask](#ac2343c08359099f383f154655b371cf6) |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \* | [matrix\_stable\_state](#aafb384043bed6593b696e11fd34e0f97) |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \* | [matrix\_unstable\_state](#a47d4177495c1e17b76c1f616720a3aa6) |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \* | [matrix\_previous\_state](#a361fd7c63b2ca643e4b957a6c1c85ae4) |
| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) \* | [matrix\_new\_state](#a5da560d28d8bfc527d60c10e4aa29ffb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [scan\_cycle\_idx](#a0fbc6d10c2f15f3a0126e0c229ec9686) |

## Detailed Description

Common keyboard matrix config.

This structure **must** be placed first in the driver's config structure.

## Field Documentation

## [◆ ](#ac2343c08359099f383f154655b371cf6)actual\_key\_mask

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)\* input\_kbd\_matrix\_common\_config::actual\_key\_mask |
| --- |

## [◆ ](#ace0bafa079826819b7df7950cb3e8212)api

| const struct [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md)\* input\_kbd\_matrix\_common\_config::api |
| --- |

## [◆ ](#adfb2b978f1d41bdff28acca17cc4ed3d)col\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_kbd\_matrix\_common\_config::col\_size |
| --- |

## [◆ ](#a004cb35eede1e58b27730a46155540e9)debounce\_down\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_config::debounce\_down\_us |
| --- |

## [◆ ](#a545fba8a03ced44a95d7bb7f345d763f)debounce\_up\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_config::debounce\_up\_us |
| --- |

## [◆ ](#a2377a3c7cbd195bb6da3d4dfaf1f5972)ghostkey\_check

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) input\_kbd\_matrix\_common\_config::ghostkey\_check |
| --- |

## [◆ ](#a5da560d28d8bfc527d60c10e4aa29ffb)matrix\_new\_state

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)\* input\_kbd\_matrix\_common\_config::matrix\_new\_state |
| --- |

## [◆ ](#a361fd7c63b2ca643e4b957a6c1c85ae4)matrix\_previous\_state

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)\* input\_kbd\_matrix\_common\_config::matrix\_previous\_state |
| --- |

## [◆ ](#aafb384043bed6593b696e11fd34e0f97)matrix\_stable\_state

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)\* input\_kbd\_matrix\_common\_config::matrix\_stable\_state |
| --- |

## [◆ ](#a47d4177495c1e17b76c1f616720a3aa6)matrix\_unstable\_state

| [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)\* input\_kbd\_matrix\_common\_config::matrix\_unstable\_state |
| --- |

## [◆ ](#a34ce838e3ed4a5cb19c8ce961a9da947)poll\_period\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_config::poll\_period\_us |
| --- |

## [◆ ](#a81ccf8e0a1f49361f55737e0149bd656)poll\_timeout\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_config::poll\_timeout\_ms |
| --- |

## [◆ ](#af3c4f2bcddf50dc2dbf0ad0e54230565)row\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) input\_kbd\_matrix\_common\_config::row\_size |
| --- |

## [◆ ](#a0fbc6d10c2f15f3a0126e0c229ec9686)scan\_cycle\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* input\_kbd\_matrix\_common\_config::scan\_cycle\_idx |
| --- |

## [◆ ](#a13374b57becd9314ea726ae888f1702a)settle\_time\_us

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_kbd\_matrix\_common\_config::settle\_time\_us |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input\_kbd\_matrix.h](input__kbd__matrix_8h_source.md)

- [input\_kbd\_matrix\_common\_config](structinput__kbd__matrix__common__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
