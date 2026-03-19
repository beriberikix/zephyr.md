---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structimg__gr__upload.html
original_path: doxygen/html/structimg__gr__upload.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_gr\_upload Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt\_client API](group__mcumgr__img__mgmt__client.md)

IMG mgmt client upload structure.
[More...](#details)

`#include <[img_mgmt_client.h](img__mgmt__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [sha256](#a773dfcf2f4ceccb771020f29f2e44c92) [32] |
|  | Image 256-bit hash. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [hash\_initialized](#af71ec58c3a2c39e1549c41f7692b1319) |
|  | True when Hash is configured, false when not. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [image\_size](#a093b1897e492545ab5b92d91bde727fb) |
|  | Image size. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [offset](#a71736f17ef73d50d0e61049d356e2ce2) |
|  | Image upload offset state. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [upload\_header\_size](#ae5245e6622c991cbd207b3f69f7548f3) |
|  | Worst case init upload message size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [image\_num](#a457e54010e9980b96bc970f6d43bd127) |
|  | Image slot num. |

## Detailed Description

IMG mgmt client upload structure.

Structure is used internally by the client

## Field Documentation

## [◆ ](#af71ec58c3a2c39e1549c41f7692b1319)hash\_initialized

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) img\_gr\_upload::hash\_initialized |
| --- |

True when Hash is configured, false when not.

## [◆ ](#a457e54010e9980b96bc970f6d43bd127)image\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_gr\_upload::image\_num |
| --- |

Image slot num.

## [◆ ](#a093b1897e492545ab5b92d91bde727fb)image\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_gr\_upload::image\_size |
| --- |

Image size.

## [◆ ](#a71736f17ef73d50d0e61049d356e2ce2)offset

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_gr\_upload::offset |
| --- |

Image upload offset state.

## [◆ ](#a773dfcf2f4ceccb771020f29f2e44c92)sha256

| char img\_gr\_upload::sha256[32] |
| --- |

Image 256-bit hash.

## [◆ ](#ae5245e6622c991cbd207b3f69f7548f3)upload\_header\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_gr\_upload::upload\_header\_size |
| --- |

Worst case init upload message size.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt\_client.h](img__mgmt__client_8h_source.md)

- [img\_gr\_upload](structimg__gr__upload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
