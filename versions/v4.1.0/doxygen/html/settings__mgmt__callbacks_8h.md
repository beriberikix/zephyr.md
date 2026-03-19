---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/settings__mgmt__callbacks_8h.html
original_path: doxygen/html/settings__mgmt__callbacks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_mgmt\_callbacks.h File Reference

[Go to the source code of this file.](settings__mgmt__callbacks_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [settings\_mgmt\_access](structsettings__mgmt__access.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0 "Callback when a setting is read/written/deleted.") notification callback: This callback function is used to notify the application about a pending setting read/write/delete/load/save/commit request and to authorise or deny it. [More...](structsettings__mgmt__access.md#details) |

| Enumerations | |
| --- | --- |
| enum | [settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47) {     [SETTINGS\_ACCESS\_READ](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47aea0d3b2628423306fbb4d52718d7af00) , [SETTINGS\_ACCESS\_WRITE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a614d170f1bdd53361576fd7c73b7c590) , [SETTINGS\_ACCESS\_DELETE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a1d4e86a55ad3d9869b0185cc0b4d9dbd) , [SETTINGS\_ACCESS\_COMMIT](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a377d59e22e96f09348df99cd62fad4de) ,     [SETTINGS\_ACCESS\_LOAD](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47acc68c6153dcb7c7b0c7182fd6eb525ce) , [SETTINGS\_ACCESS\_SAVE](group__mcumgr__callback__api__settings__mgmt.md#gga40c179f978718409c7db43448efc8f47a37c25f343771851dab3aa4f99c97e543)   } |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [settings\_mgmt](dir_f7c37d3a1c1d534b483feb4fbb3dbf95.md)
- [settings\_mgmt\_callbacks.h](settings__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
