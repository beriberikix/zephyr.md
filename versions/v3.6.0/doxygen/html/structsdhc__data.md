---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsdhc__data.html
original_path: doxygen/html/structsdhc__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

SD host controller data structure.
[More...](#details)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [block\_addr](#aad1e8462d94b4243c981147eab6c962d) |
|  | Block to start read from. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [block\_size](#a20b0ca14adadcdb8d3681240faf5e7b6) |
|  | Block size. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [blocks](#a47b378d455167bb8d7d05d2f058977fa) |
|  | Number of blocks. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [bytes\_xfered](#ae68f1e7f1fbff14c24bd42fa300f9e15) |
|  | populated with number of bytes sent by SDHC |
| void \* | [data](#a0f656d093a5cdf3bd09ffee279ad452d) |
|  | Data to transfer or receive. |
| int | [timeout\_ms](#afcf3942de27cd164b6da8dfefa864a8a) |
|  | data timeout in milliseconds |

## Detailed Description

SD host controller data structure.

This command structure is used to send data transfer requests to an SD host controller, which will be sent to SD devices.

## Field Documentation

## [◆ ](#aad1e8462d94b4243c981147eab6c962d)block\_addr

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_data::block\_addr |
| --- |

Block to start read from.

## [◆ ](#a20b0ca14adadcdb8d3681240faf5e7b6)block\_size

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_data::block\_size |
| --- |

Block size.

## [◆ ](#a47b378d455167bb8d7d05d2f058977fa)blocks

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_data::blocks |
| --- |

Number of blocks.

## [◆ ](#ae68f1e7f1fbff14c24bd42fa300f9e15)bytes\_xfered

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_data::bytes\_xfered |
| --- |

populated with number of bytes sent by SDHC

## [◆ ](#a0f656d093a5cdf3bd09ffee279ad452d)data

| void\* sdhc\_data::data |
| --- |

Data to transfer or receive.

## [◆ ](#afcf3942de27cd164b6da8dfefa864a8a)timeout\_ms

| int sdhc\_data::timeout\_ms |
| --- |

data timeout in milliseconds

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_data](structsdhc__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
