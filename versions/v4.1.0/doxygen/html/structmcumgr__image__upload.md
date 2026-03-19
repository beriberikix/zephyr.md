---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmcumgr__image__upload.html
original_path: doxygen/html/structmcumgr__image__upload.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcumgr\_image\_upload Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

MCUmgr Image upload response.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) | [status](#a5522d2958df295c72fd00212155c7eee) |
|  | Status. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [image\_upload\_offset](#ade29d2b559d9709b7372874e993e267c) |
|  | Reported image offset. |

## Detailed Description

MCUmgr Image upload response.

## Field Documentation

## [◆ ](#ade29d2b559d9709b7372874e993e267c)image\_upload\_offset

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mcumgr\_image\_upload::image\_upload\_offset |
| --- |

Reported image offset.

## [◆ ](#a5522d2958df295c72fd00212155c7eee)status

| enum [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) mcumgr\_image\_upload::status |
| --- |

Status.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [mcumgr\_image\_upload](structmcumgr__image__upload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
