---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structimg__mgmt__state.html
original_path: doxygen/html/structimg__mgmt__state.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_state Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt API](group__mcumgr__img__mgmt.md)

Global state for upload in progress.
[More...](#details)

`#include <[img_mgmt.h](img__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [area\_id](#a4da29c0c4b525463cce3f0d3ffbed633) |
|  | Flash area being written; -1 if no upload in progress. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [off](#a965b6426ea57beac531af3bb9d2f0d0e) |
|  | Flash offset of next chunk. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a40619a325f216e1c27e45fd19ccd6db3) |
|  | Total size of image data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_sha\_len](#a6a3cbeb401f057fb1510e1acbdf7d71c) |
|  | Hash of image data; used for resumption of a partial upload. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_sha](#a1c357f22c420a310c234c96a9bc7143f) [32] |

## Detailed Description

Global state for upload in progress.

## Field Documentation

## [◆ ](#a4da29c0c4b525463cce3f0d3ffbed633)area\_id

| int img\_mgmt\_state::area\_id |
| --- |

Flash area being written; -1 if no upload in progress.

## [◆ ](#a1c357f22c420a310c234c96a9bc7143f)data\_sha

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_state::data\_sha[32] |
| --- |

## [◆ ](#a6a3cbeb401f057fb1510e1acbdf7d71c)data\_sha\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_state::data\_sha\_len |
| --- |

Hash of image data; used for resumption of a partial upload.

## [◆ ](#a965b6426ea57beac531af3bb9d2f0d0e)off

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_mgmt\_state::off |
| --- |

Flash offset of next chunk.

## [◆ ](#a40619a325f216e1c27e45fd19ccd6db3)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_mgmt\_state::size |
| --- |

Total size of image data.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt.h](img__mgmt_8h_source.md)

- [img\_mgmt\_state](structimg__mgmt__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
