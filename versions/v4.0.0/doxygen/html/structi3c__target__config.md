---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__target__config.html
original_path: doxygen/html/structi3c__target__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_target\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Target Device API](group__i3c__target__device.md)

Structure describing a device that supports the I3C target API.
[More...](#details)

`#include <[target_device.h](target__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a4e0fc180a85b4ec2f9fc5d3f3b8e030b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#ae27fb5be1c29a3f7a38955d5954f1bf6) |
|  | Flags for the target device defined by I3C\_TARGET\_FLAGS\_\* constants. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [address](#a89b7f8bd52beec7dd733ab6dd1111758) |
|  | Address for this target device. |
| const struct [i3c\_target\_callbacks](structi3c__target__callbacks.md) \* | [callbacks](#a43ed9a3679d54f7bb91dade34a5897b6) |
|  | Callback functions. |

## Detailed Description

Structure describing a device that supports the I3C target API.

Instances of this are passed to the [i3c\_target\_register()](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42 "Registers the provided config as target device of a controller.") and [i3c\_target\_unregister()](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4 "Unregisters the provided config as target device.") functions to indicate addition and removal of a target device, respective.

Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to [i3c\_target\_register()](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42 "Registers the provided config as target device of a controller.").

## Field Documentation

## [◆ ](#a89b7f8bd52beec7dd733ab6dd1111758)address

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_target\_config::address |
| --- |

Address for this target device.

## [◆ ](#a43ed9a3679d54f7bb91dade34a5897b6)callbacks

| const struct [i3c\_target\_callbacks](structi3c__target__callbacks.md)\* i3c\_target\_config::callbacks |
| --- |

Callback functions.

## [◆ ](#ae27fb5be1c29a3f7a38955d5954f1bf6)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_target\_config::flags |
| --- |

Flags for the target device defined by I3C\_TARGET\_FLAGS\_\* constants.

## [◆ ](#a4e0fc180a85b4ec2f9fc5d3f3b8e030b)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i3c\_target\_config::node |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[target\_device.h](target__device_8h_source.md)

- [i3c\_target\_config](structi3c__target__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
