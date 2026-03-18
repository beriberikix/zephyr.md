---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structgptp__phase__dis__cb.html
original_path: doxygen/html/structgptp__phase__dis__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp\_phase\_dis\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [gPTP support](group__gptp.md)

Phase discontinuity callback structure.
[More...](#details)

`#include <[gptp.h](gptp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a9801de29992ae2f23bbe89c417d58fe3) |
|  | Node information for the slist. |
| [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b) | [cb](#a8294a9abac55d1f4406923ea4e8ed144) |
|  | Phase discontinuity callback. |

## Detailed Description

Phase discontinuity callback structure.

Stores the phase discontinuity callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

## Field Documentation

## [◆ ](#a8294a9abac55d1f4406923ea4e8ed144)cb

| [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b) gptp\_phase\_dis\_cb::cb |
| --- |

Phase discontinuity callback.

## [◆ ](#a9801de29992ae2f23bbe89c417d58fe3)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) gptp\_phase\_dis\_cb::node |
| --- |

Node information for the slist.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[gptp.h](gptp_8h_source.md)

- [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
