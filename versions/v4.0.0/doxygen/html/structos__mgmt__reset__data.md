---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structos__mgmt__reset__data.html
original_path: doxygen/html/structos__mgmt__reset__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_reset\_data Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr os\_mgmt callback API](group__mcumgr__callback__api__os__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52 "Callback when a reset command has been received, data is os_mgmt_reset_data.") notification callback: This callback function is used to notify the application about a pending device reboot request and to authorise or deny it.
[More...](#details)

`#include <[os_mgmt_callbacks.h](os__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [force](#aa9defc41c1e9aff601b5c98cb307bc01) |
|  | Contains the value of the force parameter. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52 "Callback when a reset command has been received, data is os_mgmt_reset_data.") notification callback: This callback function is used to notify the application about a pending device reboot request and to authorise or deny it.

## Field Documentation

## [◆ ](#aa9defc41c1e9aff601b5c98cb307bc01)force

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) os\_mgmt\_reset\_data::force |
| --- |

Contains the value of the force parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/os\_mgmt/[os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h_source.md)

- [os\_mgmt\_reset\_data](structos__mgmt__reset__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
