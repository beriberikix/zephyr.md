---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmcumgr__image__list__flags.html
original_path: doxygen/html/structmcumgr__image__list__flags.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcumgr\_image\_list\_flags Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

Image list flags.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bootable](#acb12d5ae0c75e9dac48874e542784bd3): 1 |
|  | Bootable image. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pending](#a744597f98d3092de161512d0817bb1a2): 1 |
|  | Pending update state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [confirmed](#ad3ff9c0acbcf2ebbb5f6820b38705bff): 1 |
|  | Confirmed image. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [active](#ade2a01aeeede96070bcdf33ce2d949fb): 1 |
|  | Active image. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [permanent](#af7c7b565ef02ea95c7486949a29164c1): 1 |
|  | Permanent image state. |

## Detailed Description

Image list flags.

## Field Documentation

## [◆ ](#ade2a01aeeede96070bcdf33ce2d949fb)active

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mcumgr\_image\_list\_flags::active |
| --- |

Active image.

## [◆ ](#acb12d5ae0c75e9dac48874e542784bd3)bootable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mcumgr\_image\_list\_flags::bootable |
| --- |

Bootable image.

## [◆ ](#ad3ff9c0acbcf2ebbb5f6820b38705bff)confirmed

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mcumgr\_image\_list\_flags::confirmed |
| --- |

Confirmed image.

## [◆ ](#a744597f98d3092de161512d0817bb1a2)pending

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mcumgr\_image\_list\_flags::pending |
| --- |

Pending update state.

## [◆ ](#af7c7b565ef02ea95c7486949a29164c1)permanent

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mcumgr\_image\_list\_flags::permanent |
| --- |

Permanent image state.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
