---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__mgmt__client.html
original_path: doxygen/html/structimg__mgmt__client.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_client Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

IMG mgmt client object.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [smp\_client\_object](structsmp__client__object.md) \* | [smp\_client](#a36abd266bbd1ea35849423708f9e816d) |
|  | SMP client object. |
| struct [img\_gr\_upload](structimg__gr__upload.md) | [upload](#a77559218adc5f7873366c56f9a02750e) |
|  | Image Upload state data for client internal use. |
| int | [image\_list\_length](#a2a2097f05111d6242d623a68959ecca9) |
|  | Client image list buffer size. |
| struct [mcumgr\_image\_data](structmcumgr__image__data.md) \* | [image\_list](#a654c94fafac9cd72465a413de8266005) |
|  | Image list buffer. |
| int | [status](#a4fb8d168a6faf48c32903b71fc8c8097) |
|  | Command status. |

## Detailed Description

IMG mgmt client object.

## Field Documentation

## [◆ ](#a654c94fafac9cd72465a413de8266005)image\_list

| struct [mcumgr\_image\_data](structmcumgr__image__data.md)\* img\_mgmt\_client::image\_list |
| --- |

Image list buffer.

## [◆ ](#a2a2097f05111d6242d623a68959ecca9)image\_list\_length

| int img\_mgmt\_client::image\_list\_length |
| --- |

Client image list buffer size.

## [◆ ](#a36abd266bbd1ea35849423708f9e816d)smp\_client

| struct [smp\_client\_object](structsmp__client__object.md)\* img\_mgmt\_client::smp\_client |
| --- |

SMP client object.

## [◆ ](#a4fb8d168a6faf48c32903b71fc8c8097)status

| int img\_mgmt\_client::status |
| --- |

Command status.

## [◆ ](#a77559218adc5f7873366c56f9a02750e)upload

| struct [img\_gr\_upload](structimg__gr__upload.md) img\_mgmt\_client::upload |
| --- |

Image Upload state data for client internal use.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [img\_mgmt\_client](structimg__mgmt__client.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
