---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__if__link__cb.html
original_path: doxygen/html/structnet__if__link__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_link\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Link callback handler struct.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#accae7945a802c5b7fc36948b12a365ef) |
|  | Node information for the slist. |
| [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) | [cb](#a66092a22cba3dd69ac1a91c3522240bb) |
|  | Link callback. |

## Detailed Description

Link callback handler struct.

Stores the link callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

## Field Documentation

## [◆ ](#a66092a22cba3dd69ac1a91c3522240bb)cb

| [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) net\_if\_link\_cb::cb |
| --- |

Link callback.

## [◆ ](#accae7945a802c5b7fc36948b12a365ef)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_if\_link\_cb::node |
| --- |

Node information for the slist.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_link\_cb](structnet__if__link__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
