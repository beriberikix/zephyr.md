---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__mgmt__slot__info__slot.html
original_path: doxygen/html/structimg__mgmt__slot__info__slot.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_slot\_info\_slot Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0 "Callback when a slot list command outputs fields for a slot of an image, data is img_mgmt_slot_info_s...") notification callback: This callback function is called once per slot per image when the slot info command is used, it can be used to return additional information/fields in the response.
[More...](#details)

`#include <[img_mgmt_callbacks.h](img__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [image](#ab809efd89381e763f73a45b5c5e807d7) |
|  | The image that is currently being enumerated. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot](#a4fbfd8fb9135cc3fa2cc65f71ca2199e) |
|  | The slot that is currently being enumerated. |
| const struct [flash\_area](structflash__area.md) \* | [fa](#a53ef029264545a7caca289d61e7983a1) |
|  | Flash area of the slot that is current being enumerated. |
| zcbor\_state\_t \* | [zse](#a316d66379317f7a13be21cd242cdddda) |
|  | The zcbor encoder which is currently being used to output information, additional fields can be added using this. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0 "Callback when a slot list command outputs fields for a slot of an image, data is img_mgmt_slot_info_s...") notification callback: This callback function is called once per slot per image when the slot info command is used, it can be used to return additional information/fields in the response.

## Field Documentation

## [◆ ](#a53ef029264545a7caca289d61e7983a1)fa

| const struct [flash\_area](structflash__area.md)\* img\_mgmt\_slot\_info\_slot::fa |
| --- |

Flash area of the slot that is current being enumerated.

## [◆ ](#ab809efd89381e763f73a45b5c5e807d7)image

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_slot\_info\_slot::image |
| --- |

The image that is currently being enumerated.

## [◆ ](#a4fbfd8fb9135cc3fa2cc65f71ca2199e)slot

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_slot\_info\_slot::slot |
| --- |

The slot that is currently being enumerated.

## [◆ ](#a316d66379317f7a13be21cd242cdddda)zse

| zcbor\_state\_t\* img\_mgmt\_slot\_info\_slot::zse |
| --- |

The zcbor encoder which is currently being used to output information, additional fields can be added using this.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h_source.md)

- [img\_mgmt\_slot\_info\_slot](structimg__mgmt__slot__info__slot.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
