---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structimg__mgmt__upload__req.html
original_path: doxygen/html/structimg__mgmt__upload__req.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_upload\_req Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr img\_mgmt API](group__mcumgr__img__mgmt.md)

Represents an individual upload request.
[More...](#details)

`#include <[img_mgmt.h](img__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [image](#ad61f8c732f0b2150bd252e47eb539bb1) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [off](#ae9c67210faa7dfc55a73f66defc00195) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a25cdcd55c77cde43af1a9ec9b414cecb) |
| struct zcbor\_string | [img\_data](#ade363ed09134ff2f3a1fcb20a6305cfa) |
| struct zcbor\_string | [data\_sha](#ae30c1fc9257f04c88216ba92f8453dac) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [upgrade](#a439504202c945a1dd74b75c35a1a8017) |

## Detailed Description

Represents an individual upload request.

## Field Documentation

## [◆ ](#ae30c1fc9257f04c88216ba92f8453dac)data\_sha

| struct zcbor\_string img\_mgmt\_upload\_req::data\_sha |
| --- |

## [◆ ](#ad61f8c732f0b2150bd252e47eb539bb1)image

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_mgmt\_upload\_req::image |
| --- |

## [◆ ](#ade363ed09134ff2f3a1fcb20a6305cfa)img\_data

| struct zcbor\_string img\_mgmt\_upload\_req::img\_data |
| --- |

## [◆ ](#ae9c67210faa7dfc55a73f66defc00195)off

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_mgmt\_upload\_req::off |
| --- |

## [◆ ](#a25cdcd55c77cde43af1a9ec9b414cecb)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) img\_mgmt\_upload\_req::size |
| --- |

## [◆ ](#a439504202c945a1dd74b75c35a1a8017)upgrade

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) img\_mgmt\_upload\_req::upgrade |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/img\_mgmt/[img\_mgmt.h](img__mgmt_8h_source.md)

- [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
