---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2mbox_8h.html
original_path: doxygen/html/drivers_2mbox_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox.h File Reference

Generic low-level multi-channel inter-processor mailbox communication API.
[More...](#details)

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h_source.md)>`  
`#include <syscalls/mbox.h>`

[Go to the source code of this file.](drivers_2mbox_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mbox\_msg](structmbox__msg.md) |
|  | Message struct (to hold data and its size). [More...](structmbox__msg.md#details) |
| struct | [mbox\_channel](structmbox__channel.md) |
|  | Provides a type to hold an MBOX channel. [More...](structmbox__channel.md#details) |
| struct | [mbox\_driver\_api](structmbox__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [MBOX\_DT\_CHANNEL\_GET](group__mbox__interface.md#ga9e02e3a523a63ff564ce2bb42c03aa1f)(node\_id, name) |
|  | Structure initializer for [mbox\_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.") from devicetree. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, void \*user\_data, struct [mbox\_msg](structmbox__msg.md) \*data) |
|  | Callback API for incoming MBOX messages. |
| typedef int(\* | [mbox\_send\_t](group__mbox__interface.md#gaaecf1d595053c6ea282abb0bbe637beb)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Callback API to send MBOX messages. |
| typedef int(\* | [mbox\_mtu\_get\_t](group__mbox__interface.md#gadce4d6561407c2d8d7bc54a0b7350297)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get maximum data size. |
| typedef int(\* | [mbox\_register\_callback\_t](group__mbox__interface.md#gac8959349175e67d0e02f98252a52647b)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8) cb, void \*user\_data) |
|  | Callback API upon registration. |
| typedef int(\* | [mbox\_set\_enabled\_t](group__mbox__interface.md#ga64dad0e5a73903e3a55d619838f53176)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Callback API upon enablement of interrupts. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [mbox\_max\_channels\_get\_t](group__mbox__interface.md#ga822c7691cdd429f18f2e5e922102ef1c)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get maximum number of channels. |

| Functions | |
| --- | --- |
| static void | [mbox\_init\_channel](group__mbox__interface.md#ga70253c432c8064a2760731f1d237f2b7) (struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ch\_id) |
|  | Initialize a channel struct. |
| int | [mbox\_send](group__mbox__interface.md#ga18828e5c28201ad838ed9ba7c0afabfe) (const struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device. |
| static int | [mbox\_register\_callback](group__mbox__interface.md#gad48e48c984e70348336a896bb2835c77) (const struct [mbox\_channel](structmbox__channel.md) \*channel, [mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8) cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages. |
| int | [mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| int | [mbox\_set\_enabled](group__mbox__interface.md#ga563c6c0e2199b0608b2cd0606c46fc81) (const struct [mbox\_channel](structmbox__channel.md) \*channel, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable (disable) interrupts and callbacks for inbound channels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of channels. |

## Detailed Description

Generic low-level multi-channel inter-processor mailbox communication API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mbox.h](drivers_2mbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
