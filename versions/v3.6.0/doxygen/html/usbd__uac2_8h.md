---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbd__uac2_8h.html
original_path: doxygen/html/usbd__uac2_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_uac2.h File Reference

USB Audio Class 2 device public header.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](usbd__uac2_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uac2\_ops](structuac2__ops.md) |
|  | USB Audio 2 application event handlers. [More...](structuac2__ops.md#details) |

| Macros | |
| --- | --- |
| #define | [UAC2\_ENTITY\_ID](#aa35265e83d894896806fcca28feb84a3)(node) |

| Functions | |
| --- | --- |
| void | [usbd\_uac2\_set\_ops](#a802a727c1a201c26a3bd74f0e7f0900c) (const struct [device](structdevice.md) \*dev, const struct [uac2\_ops](structuac2__ops.md) \*ops, void \*user\_data) |
|  | Register USB Audio 2 application callbacks. |
| int | [usbd\_uac2\_send](#ae899d75d786f5b1df86db48de88d1254) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Send audio data to output terminal. |

## Detailed Description

USB Audio Class 2 device public header.

This header describes only class API interaction with application. The audio device itself is modelled with devicetree zephyr,uac2 compatible.

This API is currently considered experimental.

## Macro Definition Documentation

## [◆ ](#aa35265e83d894896806fcca28feb84a3)UAC2\_ENTITY\_ID

| #define UAC2\_ENTITY\_ID | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

BUILD\_ASSERT([DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node), zephyr\_uac2)); \

UTIL\_INC([DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)(node)); \

})

[DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)

#define DT\_NODE\_HAS\_COMPAT(node\_id, compat)

Does a devicetree node match a compatible?

**Definition** devicetree.h:3252

[DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)

#define DT\_NODE\_CHILD\_IDX(node\_id)

Get a devicetree node's index into its parent's list of children.

**Definition** devicetree.h:550

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:359

## Function Documentation

## [◆ ](#ae899d75d786f5b1df86db48de88d1254)usbd\_uac2\_send()

| int usbd\_uac2\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *terminal*, |
|  |  | void \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *size* ) |

Send audio data to output terminal.

Parameters
:   | dev | USB Audio 2 device |
    | --- | --- |
    | terminal | Output Terminal ID linked to AudioStreaming interface |
    | data | Buffer containing outgoing data |
    | size | Number of bytes to send |

Returns
:   0 on success, negative value on error

## [◆ ](#a802a727c1a201c26a3bd74f0e7f0900c)usbd\_uac2\_set\_ops()

| void usbd\_uac2\_set\_ops | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [uac2\_ops](structuac2__ops.md) \* | *ops*, |
|  |  | void \* | *user\_data* ) |

Register USB Audio 2 application callbacks.

Parameters
:   | dev | USB Audio 2 device instance |
    | --- | --- |
    | ops | USB Audio 2 callback structure |
    | user\_data | Opaque user data to pass to ops callbacks |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_uac2.h](usbd__uac2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
