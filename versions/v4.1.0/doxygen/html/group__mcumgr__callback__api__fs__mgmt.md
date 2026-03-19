---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html
original_path: doxygen/html/group__mcumgr__callback__api__fs__mgmt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr fs\_mgmt callback API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md)

MCUmgr fs\_mgmt callback API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [fs\_mgmt\_file\_access](structfs__mgmt__file__access.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3 "Callback when a file has been accessed, data is fs_mgmt_file_access().") notification callback: This callback function is used to notify the application about a pending file read/write request and to authorise or deny it. [More...](structfs__mgmt__file__access.md#details) |

| Enumerations | |
| --- | --- |
| enum | [fs\_mgmt\_file\_access\_types](#ga80e18873c1f4d97ea601a33042bc21f9) { [FS\_MGMT\_FILE\_ACCESS\_READ](#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a) , [FS\_MGMT\_FILE\_ACCESS\_WRITE](#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2) , [FS\_MGMT\_FILE\_ACCESS\_STATUS](#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2) , [FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM](#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c) } |
|  | The type of operation that is being requested for a given file access callback. [More...](#ga80e18873c1f4d97ea601a33042bc21f9) |

## Detailed Description

MCUmgr fs\_mgmt callback API.

## Enumeration Type Documentation

## [◆ ](#ga80e18873c1f4d97ea601a33042bc21f9)fs\_mgmt\_file\_access\_types

| enum [fs\_mgmt\_file\_access\_types](#ga80e18873c1f4d97ea601a33042bc21f9) |
| --- |

`#include <[fs_mgmt_callbacks.h](fs__mgmt__callbacks_8h.md)>`

The type of operation that is being requested for a given file access callback.

| Enumerator | |
| --- | --- |
| FS\_MGMT\_FILE\_ACCESS\_READ | Access to read file (file upload). |
| FS\_MGMT\_FILE\_ACCESS\_WRITE | Access to write file (file download). |
| FS\_MGMT\_FILE\_ACCESS\_STATUS | Access to get status of file. |
| FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM | Access to calculate hash or checksum of file. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
