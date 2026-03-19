---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/img__mgmt__callbacks_8h.html
original_path: doxygen/html/img__mgmt__callbacks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_callbacks.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <zcbor_common.h>`

[Go to the source code of this file.](img__mgmt__callbacks_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c "Callback when a client sends a file upload chunk, data is img_mgmt_upload_check().") notification callback: This callback function is used to notify the application about a pending firmware upload packet from a client and authorise or deny it. [More...](structimg__mgmt__upload__check.md#details) |
| struct | [img\_mgmt\_image\_confirmed](structimg__mgmt__image__confirmed.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb "Callback when an image has been confirmed.") notification callback: This callback function is used to notify the application about an image confirmation being executed successfully. [More...](structimg__mgmt__image__confirmed.md#details) |
| struct | [img\_mgmt\_state\_slot\_encode](structimg__mgmt__state__slot__encode.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7 "Callback when an image slot's state is encoded for a response, data is img_mgmt_state_slot_encode().") notification callback: This callback function is used to allow applications or modules append custom fields to the image slot state response. [More...](structimg__mgmt__state__slot__encode.md#details) |
| struct | [img\_mgmt\_slot\_info\_image](structimg__mgmt__slot__info__image.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3 "Callback when a slot list command outputs fields for an image, data is img_mgmt_slot_info_image().") notification callback: This callback function is called once per image when the slot info command is used, it can be used to return additional information/fields in the response. [More...](structimg__mgmt__slot__info__image.md#details) |
| struct | [img\_mgmt\_slot\_info\_slot](structimg__mgmt__slot__info__slot.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0 "Callback when a slot list command outputs fields for a slot of an image, data is img_mgmt_slot_info_s...") notification callback: This callback function is called once per slot per image when the slot info command is used, it can be used to return additional information/fields in the response. [More...](structimg__mgmt__slot__info__slot.md#details) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
