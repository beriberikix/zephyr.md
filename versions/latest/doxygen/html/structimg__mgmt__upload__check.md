---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structimg__mgmt__upload__check.html
original_path: doxygen/html/structimg__mgmt__upload__check.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_upload\_check Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c "Callback when a client sends a file upload chunk, data is img_mgmt_upload_check().") notification callback: This callback function is used to notify the application about a pending firmware upload packet from a client and authorise or deny it.
[More...](#details)

`#include <[img_mgmt_callbacks.h](img__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md) \* | [action](#aea96e650e2701e6064638dd4c384df55) |
|  | Action to take. |
| struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md) \* | [req](#ab8a3e937302b1def309508eace664793) |
|  | Upload request information. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c "Callback when a client sends a file upload chunk, data is img_mgmt_upload_check().") notification callback: This callback function is used to notify the application about a pending firmware upload packet from a client and authorise or deny it.

Upload will be allowed so long as all notification handlers return [MGMT\_ERR\_EOK](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f "No error (success)."), if one returns an error then the upload will be denied.

## Field Documentation

## [◆ ](#aea96e650e2701e6064638dd4c384df55)action

| struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md)\* img\_mgmt\_upload\_check::action |
| --- |

Action to take.

## [◆ ](#ab8a3e937302b1def309508eace664793)req

| struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md)\* img\_mgmt\_upload\_check::req |
| --- |

Upload request information.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h_source.md)

- [img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
