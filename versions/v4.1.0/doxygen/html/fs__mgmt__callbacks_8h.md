---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fs__mgmt__callbacks_8h.html
original_path: doxygen/html/fs__mgmt__callbacks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_callbacks.h File Reference

[Go to the source code of this file.](fs__mgmt__callbacks_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fs\_mgmt\_file\_access](structfs__mgmt__file__access.md) |
|  | Structure provided in the [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3 "Callback when a file has been accessed, data is fs_mgmt_file_access().") notification callback: This callback function is used to notify the application about a pending file read/write request and to authorise or deny it. [More...](structfs__mgmt__file__access.md#details) |

| Enumerations | |
| --- | --- |
| enum | [fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) { [FS\_MGMT\_FILE\_ACCESS\_READ](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a) , [FS\_MGMT\_FILE\_ACCESS\_WRITE](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2) , [FS\_MGMT\_FILE\_ACCESS\_STATUS](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2) , [FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM](group__mcumgr__callback__api__fs__mgmt.md#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c) } |
|  | The type of operation that is being requested for a given file access callback. [More...](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [fs\_mgmt](dir_c1d9e91ec7be14b6f800d54e568d432d.md)
- [fs\_mgmt\_callbacks.h](fs__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
