---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mcumgr__callback__api__img__mgmt.html
original_path: doxygen/html/group__mcumgr__callback__api__img__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr img\_mgmt callback API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md)

MCUmgr img\_mgmt callback API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c "Callback when a client sends a file upload chunk, data is img_mgmt_upload_check().") notification callback: This callback function is used to notify the application about a pending firmware upload packet from a client and authorise or deny it. [More...](structimg__mgmt__upload__check.md#details) |
| struct | [img\_mgmt\_state\_slot\_encode](structimg__mgmt__state__slot__encode.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7 "Callback when an image slot's state is encoded for a response.") notification callback: This callback function is used to allow applications or modules append custom fields to the image slot state response. [More...](structimg__mgmt__state__slot__encode.md#details) |
| struct | [img\_mgmt\_slot\_info\_image](structimg__mgmt__slot__info__image.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3 "Callback when an slot list command outputs fields for an image.") notification callback: This callback function is called once per image when the slot info command is used, it can be used to return additional information/fields in the response. [More...](structimg__mgmt__slot__info__image.md#details) |
| struct | [img\_mgmt\_slot\_info\_slot](structimg__mgmt__slot__info__slot.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0 "Callback when an slot list command outputs fields for a slot of an image.") notification callback: This callback function is called once per slot per image when the slot info command is used, it can be used to return additional information/fields in the response. [More...](structimg__mgmt__slot__info__slot.md#details) |

## Detailed Description

MCUmgr img\_mgmt callback API.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
