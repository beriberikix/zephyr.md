---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structimg__mgmt__upload__action.html
original_path: doxygen/html/structimg__mgmt__upload__action.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_upload\_action Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt API](group__mcumgr__img__mgmt.md)

Describes what to do during processing of an upload request.
[More...](#details)

`#include <[img_mgmt.h](img__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long | [size](#a4b1d3625ade4e4392094ace41ec4aa01) |
|  | The total size of the image. |
| int | [write\_bytes](#aac493000e6989735531492f15edb6108) |
|  | The number of image bytes to write to flash. |
| int | [area\_id](#a6c9248e3c21325ed99ff8cf765f3ac82) |
|  | The flash area to write to. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [proceed](#a7661db4343ebf6f7d040e3e87d3611aa) |
|  | Whether to process the request; false if offset is wrong. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [erase](#abe9c3503c6d58cf3b7ad637cd4fec852) |
|  | Whether to erase the destination flash area. |

## Detailed Description

Describes what to do during processing of an upload request.

## Field Documentation

## [◆ ](#a6c9248e3c21325ed99ff8cf765f3ac82)area\_id

| int img\_mgmt\_upload\_action::area\_id |
| --- |

The flash area to write to.

## [◆ ](#abe9c3503c6d58cf3b7ad637cd4fec852)erase

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) img\_mgmt\_upload\_action::erase |
| --- |

Whether to erase the destination flash area.

## [◆ ](#a7661db4343ebf6f7d040e3e87d3611aa)proceed

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) img\_mgmt\_upload\_action::proceed |
| --- |

Whether to process the request; false if offset is wrong.

## [◆ ](#a4b1d3625ade4e4392094ace41ec4aa01)size

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long img\_mgmt\_upload\_action::size |
| --- |

The total size of the image.

## [◆ ](#aac493000e6989735531492f15edb6108)write\_bytes

| int img\_mgmt\_upload\_action::write\_bytes |
| --- |

The number of image bytes to write to flash.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt.h](img__mgmt_8h_source.md)

- [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
