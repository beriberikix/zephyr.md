---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__mgmt__state__slot__encode.html
original_path: doxygen/html/structimg__mgmt__state__slot__encode.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_state\_slot\_encode Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7 "Callback when an image slot's state is encoded for a response, data is img_mgmt_state_slot_encode().") notification callback: This callback function is used to allow applications or modules append custom fields to the image slot state response.
[More...](#details)

`#include <[img_mgmt_callbacks.h](img__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | [ok](#a9279018722b20380da6e48046787d220) |
| zcbor\_state\_t \* | [zse](#a62157cb9a3288806f4ec11e5c2ef20ac) |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [slot](#ad669d8c2062f90d008f715dee206c687) |
| const char \* | [version](#aa4bf77897519408786c1ee28029342dd) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [hash](#a5c2486f75743eb44133819b5f35d97cb) |
| const int | [flags](#a9e53ce9a8a88b76e035b02cd2289fb07) |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7 "Callback when an image slot's state is encoded for a response, data is img_mgmt_state_slot_encode().") notification callback: This callback function is used to allow applications or modules append custom fields to the image slot state response.

## Field Documentation

## [◆ ](#a9e53ce9a8a88b76e035b02cd2289fb07)flags

| const int img\_mgmt\_state\_slot\_encode::flags |
| --- |

## [◆ ](#a5c2486f75743eb44133819b5f35d97cb)hash

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* img\_mgmt\_state\_slot\_encode::hash |
| --- |

## [◆ ](#a9279018722b20380da6e48046787d220)ok

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)\* img\_mgmt\_state\_slot\_encode::ok |
| --- |

## [◆ ](#ad669d8c2062f90d008f715dee206c687)slot

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_mgmt\_state\_slot\_encode::slot |
| --- |

## [◆ ](#aa4bf77897519408786c1ee28029342dd)version

| const char\* img\_mgmt\_state\_slot\_encode::version |
| --- |

## [◆ ](#a62157cb9a3288806f4ec11e5c2ef20ac)zse

| zcbor\_state\_t\* img\_mgmt\_state\_slot\_encode::zse |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h_source.md)

- [img\_mgmt\_state\_slot\_encode](structimg__mgmt__state__slot__encode.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
