---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmcumgr__image__state.html
original_path: doxygen/html/structmcumgr__image__state.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcumgr\_image\_state Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

MCUmgr Image list response.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) | [status](#a4ec39c59f3cfe789dabf7fc361ff86ac) |
|  | Status. |
| int | [image\_list\_length](#afd36103c373d709733ee928326c50343) |
|  | Length of image\_list. |
| struct [mcumgr\_image\_data](structmcumgr__image__data.md) \* | [image\_list](#af7bd52b3a18ad190e0159c5e928b857e) |
|  | Image list pointer. |

## Detailed Description

MCUmgr Image list response.

## Field Documentation

## [◆ ](#af7bd52b3a18ad190e0159c5e928b857e)image\_list

| struct [mcumgr\_image\_data](structmcumgr__image__data.md)\* mcumgr\_image\_state::image\_list |
| --- |

Image list pointer.

## [◆ ](#afd36103c373d709733ee928326c50343)image\_list\_length

| int mcumgr\_image\_state::image\_list\_length |
| --- |

Length of image\_list.

## [◆ ](#a4ec39c59f3cfe789dabf7fc361ff86ac)status

| enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) mcumgr\_image\_state::status |
| --- |

Status.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [mcumgr\_image\_state](structmcumgr__image__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
