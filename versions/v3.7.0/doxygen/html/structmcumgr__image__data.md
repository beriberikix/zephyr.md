---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmcumgr__image__data.html
original_path: doxygen/html/structmcumgr__image__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcumgr\_image\_data Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

Image list data.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [slot\_num](#a713cff86339e08b2f74b564dca4c521e) |
|  | Image slot num. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [img\_num](#ac394e1e5a0e0425b27926a3405d8bb2d) |
|  | Image number. |
| char | [hash](#a96a8216a5faa7095cec5907ef2117a41) [32] |
|  | Image SHA256 checksum. |
| char | [version](#aa75e38d37c9b12a2ccf32af6a47df814) [([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("255.255.65535.4294967295"))+1] |
|  | Image Version. |
| struct [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md) | [flags](#a24f83149d88a3709b4f58bc72ee932be) |
|  | Image Flags. |

## Detailed Description

Image list data.

## Field Documentation

## [◆ ](#a24f83149d88a3709b4f58bc72ee932be)flags

| struct [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md) mcumgr\_image\_data::flags |
| --- |

Image Flags.

## [◆ ](#a96a8216a5faa7095cec5907ef2117a41)hash

| char mcumgr\_image\_data::hash[32] |
| --- |

Image SHA256 checksum.

## [◆ ](#ac394e1e5a0e0425b27926a3405d8bb2d)img\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mcumgr\_image\_data::img\_num |
| --- |

Image number.

## [◆ ](#a713cff86339e08b2f74b564dca4c521e)slot\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mcumgr\_image\_data::slot\_num |
| --- |

Image slot num.

## [◆ ](#aa75e38d37c9b12a2ccf32af6a47df814)version

| char mcumgr\_image\_data::version[([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("255.255.65535.4294967295"))+1] |
| --- |

Image Version.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [mcumgr\_image\_data](structmcumgr__image__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
