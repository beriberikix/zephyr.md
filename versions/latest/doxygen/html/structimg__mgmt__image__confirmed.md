---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__mgmt__image__confirmed.html
original_path: doxygen/html/structimg__mgmt__image__confirmed.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_image\_confirmed Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb "Callback when an image has been confirmed.") notification callback: This callback function is used to notify the application about an image confirmation being executed successfully.
[More...](#details)

`#include <[img_mgmt_callbacks.h](img__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [image](#a2cd305cbe1446fd26b97a25cacad0e5c) |
|  | Image number which has been confirmed. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb "Callback when an image has been confirmed.") notification callback: This callback function is used to notify the application about an image confirmation being executed successfully.

## Field Documentation

## [◆ ](#a2cd305cbe1446fd26b97a25cacad0e5c)image

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_image\_confirmed::image |
| --- |

Image number which has been confirmed.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h_source.md)

- [img\_mgmt\_image\_confirmed](structimg__mgmt__image__confirmed.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
