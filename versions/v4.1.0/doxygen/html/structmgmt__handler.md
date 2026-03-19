---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmgmt__handler.html
original_path: doxygen/html/structmgmt__handler.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_handler Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr mgmt API](group__mcumgr__mgmt__api.md)

Read handler and write handler for a single command ID.
[More...](#details)

`#include <[mgmt.h](mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) | [mh\_read](#a7cc4917fa24afef79f1a8de8549a21e4) |
| [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) | [mh\_write](#a1bc6b52645f6eb1d0e0b0c695d972c15) |

## Detailed Description

Read handler and write handler for a single command ID.

Set use\_custom\_payload to true when using a user defined payload type

## Field Documentation

## [◆ ](#a7cc4917fa24afef79f1a8de8549a21e4)mh\_read

| [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) mgmt\_handler::mh\_read |
| --- |

## [◆ ](#a1bc6b52645f6eb1d0e0b0c695d972c15)mh\_write

| [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) mgmt\_handler::mh\_write |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/mgmt/[mgmt.h](mgmt_8h_source.md)

- [mgmt\_handler](structmgmt__handler.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
