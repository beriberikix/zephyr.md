---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2mbox_8h.html
original_path: doxygen/html/drivers_2mbox_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <zephyr/syscalls/mbox.h>`

[Go to the source code of this file.](drivers_2mbox_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mbox\_msg](structmbox__msg.md) |
|  | Message struct (to hold data and its size). [More...](structmbox__msg.md#details) |
| struct | [mbox\_dt\_spec](structmbox__dt__spec.md) |
|  | MBOX specification from DT. [More...](structmbox__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [MBOX\_DT\_SPEC\_GET](group__mbox__interface.md#gadd0a5b06ab4b208460cf49952a2b4b43)(node\_id, name) |
|  | Structure initializer for struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") from devicetree. |
| #define | [MBOX\_DT\_SPEC\_INST\_GET](group__mbox__interface.md#gafb05876cbac7967d93d9ffccbd4761a5)(inst, name) |
|  | Instance version of MBOX\_DT\_CHANNEL\_GET(). |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) |
|  | Type for MBOX channel identifiers. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mbox\_is\_ready\_dt](group__mbox__interface.md#gab1bea02e9f49442b7454706fb434f5f2) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Validate if MBOX device instance from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") is ready. |
| int | [mbox\_send](group__mbox__interface.md#gaf4d02fb3a3ed788ba28a58783209d359) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device. |
| static int | [mbox\_send\_dt](group__mbox__interface.md#ga8f737ce94afac19dd8924526d48c68ba) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| static int | [mbox\_register\_callback](group__mbox__interface.md#gac1cc65cc54b9c7e6cf2639152a4d6a7a) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, mbox\_callback\_t cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages. |
| static int | [mbox\_register\_callback\_dt](group__mbox__interface.md#ga9cda3048389f4f57d425eac8257048a7) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, mbox\_callback\_t cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| int | [mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| static int | [mbox\_mtu\_get\_dt](group__mbox__interface.md#ga9565933b282fe8e5fd057fbb238e00b9) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Return the maximum number of bytes possible in an outbound message from struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| int | [mbox\_set\_enabled](group__mbox__interface.md#ga9eea4b9501751919125cd6124f9e9868) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enable (disable) interrupts and callbacks for inbound channels. |
| static int | [mbox\_set\_enabled\_dt](group__mbox__interface.md#ga50282848e03481fe8b6f5caa900892d3) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enable (disable) interrupts and callbacks for inbound channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of channels. |
| static int | [mbox\_max\_channels\_get\_dt](group__mbox__interface.md#gad9321777457f958e9291ded26e4ed5c6) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Return the maximum number of channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mbox.h](drivers_2mbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
