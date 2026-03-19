---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__mgmt__slot__info__image.html
original_path: doxygen/html/structimg__mgmt__slot__info__image.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_slot\_info\_image Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3 "Callback when a slot list command outputs fields for an image, data is img_mgmt_slot_info_image().") notification callback: This callback function is called once per image when the slot info command is used, it can be used to return additional information/fields in the response.
[More...](#details)

`#include <[img_mgmt_callbacks.h](img__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [image](#a2456d0f9cc29a5cb56d5e8fb45f149d7) |
|  | The image that is currently being enumerated. |
| zcbor\_state\_t \* | [zse](#af19f99ee4e86a586177b014c364be94c) |
|  | The zcbor encoder which is currently being used to output information, additional fields can be added using this. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3 "Callback when a slot list command outputs fields for an image, data is img_mgmt_slot_info_image().") notification callback: This callback function is called once per image when the slot info command is used, it can be used to return additional information/fields in the response.

## Field Documentation

## [◆ ](#a2456d0f9cc29a5cb56d5e8fb45f149d7)image

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_slot\_info\_image::image |
| --- |

The image that is currently being enumerated.

## [◆ ](#af19f99ee4e86a586177b014c364be94c)zse

| zcbor\_state\_t\* img\_mgmt\_slot\_info\_image::zse |
| --- |

The zcbor encoder which is currently being used to output information, additional fields can be added using this.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h_source.md)

- [img\_mgmt\_slot\_info\_image](structimg__mgmt__slot__info__image.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
