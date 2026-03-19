---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mcumgr__callback__api__settings__mgmt.html
original_path: doxygen/html/group__mcumgr__callback__api__settings__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr settings\_mgmt callback API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md)

MCUmgr settings\_mgmt callback API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [settings\_mgmt\_access](structsettings__mgmt__access.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0 "Callback when a setting is read/written/deleted.") notification callback: This callback function is used to notify the application about a pending setting read/write/delete/load/save/commit request and to authorise or deny it. [More...](structsettings__mgmt__access.md#details) |

| Enumerations | |
| --- | --- |
| enum | [settings\_mgmt\_access\_types](#ga40c179f978718409c7db43448efc8f47) {     [SETTINGS\_ACCESS\_READ](#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00) , [SETTINGS\_ACCESS\_WRITE](#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590) , [SETTINGS\_ACCESS\_DELETE](#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd) , [SETTINGS\_ACCESS\_COMMIT](#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de) ,     [SETTINGS\_ACCESS\_LOAD](#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce) , [SETTINGS\_ACCESS\_SAVE](#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)   } |

## Detailed Description

MCUmgr settings\_mgmt callback API.

## Enumeration Type Documentation

## [◆ ](#ga40c179f978718409c7db43448efc8f47)settings\_mgmt\_access\_types

| enum [settings\_mgmt\_access\_types](#ga40c179f978718409c7db43448efc8f47) |
| --- |

`#include <[settings_mgmt_callbacks.h](settings__mgmt__callbacks_8h.md)>`

| Enumerator | |
| --- | --- |
| SETTINGS\_ACCESS\_READ |  |
| SETTINGS\_ACCESS\_WRITE |  |
| SETTINGS\_ACCESS\_DELETE |  |
| SETTINGS\_ACCESS\_COMMIT |  |
| SETTINGS\_ACCESS\_LOAD |  |
| SETTINGS\_ACCESS\_SAVE |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
