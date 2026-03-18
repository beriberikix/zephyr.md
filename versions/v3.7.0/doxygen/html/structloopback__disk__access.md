---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structloopback__disk__access.html
original_path: doxygen/html/structloopback__disk__access.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loopback\_disk\_access Struct Reference

Context object for an active loopback disk device.
[More...](#details)

`#include <[loopback_disk.h](loopback__disk_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [disk\_info](structdisk__info.md) | [info](#a958b6ae459ade33487c01fa5e60c31b3) |
| const char \* | [file\_path](#ae34d1252cb853510aef1c173bb540fb2) |
| struct [fs\_file\_t](structfs__file__t.md) | [file](#ae290129bd48f42de5acd28876af95c3e) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_sectors](#a3e71921671d406734dd0125e3478abc2) |

## Detailed Description

Context object for an active loopback disk device.

## Field Documentation

## [◆ ](#ae290129bd48f42de5acd28876af95c3e)file

| struct [fs\_file\_t](structfs__file__t.md) loopback\_disk\_access::file |
| --- |

## [◆ ](#ae34d1252cb853510aef1c173bb540fb2)file\_path

| const char\* loopback\_disk\_access::file\_path |
| --- |

## [◆ ](#a958b6ae459ade33487c01fa5e60c31b3)info

| struct [disk\_info](structdisk__info.md) loopback\_disk\_access::info |
| --- |

## [◆ ](#a3e71921671d406734dd0125e3478abc2)num\_sectors

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) loopback\_disk\_access::num\_sectors |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[loopback\_disk.h](loopback__disk_8h_source.md)

- [loopback\_disk\_access](structloopback__disk__access.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
