---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__vreq__node.html
original_path: doxygen/html/structusbd__vreq__node.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_vreq\_node Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USBD vendor request node.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#a3c68346e2f871b22fb6c3b282ddfdccb) |
|  | Node information for the dlist. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [code](#a91fe4c5cf5ccad89e81380a332a8f955) |
|  | Vendor code (bRequest value). |
| int(\* | [to\_host](#a976d236a26a47cd17316c8174e2ad04a) )(const struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Vendor request callback for device-to-host direction. |
| int(\* | [to\_dev](#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3) )(const struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Vendor request callback for host-to-device direction. |

## Detailed Description

USBD vendor request node.

Vendor request node is identified by the vendor code and is used to register callbacks to handle the vendor request with the receiving device. When the device stack receives a request with type Vendor and recipient Device, and bRequest value equal to the vendor request code, it will call the vendor callbacks depending on the direction of the request.

Example callback code fragment:

static int foo\_to\_host\_cb(const struct [usbd\_context](structusbd__context.md) \*const ctx,

const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

struct [net\_buf](structnet__buf.md) \*const buf)

{

if (setup->[wIndex](structusb__setup__packet.md#a953c058f0e31481a3d59b404037be009) == WEBUSB\_REQ\_GET\_URL) {

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index = [USB\_GET\_DESCRIPTOR\_INDEX](usb__ch9_8h.md#a653a141a5084536362396149e81b6b9a)(setup->[wValue](structusb__setup__packet.md#a619fbc1b9b6452f4394da713bdbc6a89));

if (index != SAMPLE\_WEBUSB\_LANDING\_PAGE) {

return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

}

[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)(buf, &webusb\_origin\_url,

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)([net\_buf\_tailroom](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a)(buf), sizeof(webusb\_origin\_url)));

return 0;

}

return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

}

[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)

static void \* net\_buf\_add\_mem(struct net\_buf \*buf, const void \*mem, size\_t len)

Copies the given number of bytes to the end of the buffer.

**Definition** net\_buf.h:1622

[net\_buf\_tailroom](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a)

static size\_t net\_buf\_tailroom(const struct net\_buf \*buf)

Check buffer tailroom.

**Definition** net\_buf.h:2485

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:401

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:40

[usb\_setup\_packet::wValue](structusb__setup__packet.md#a619fbc1b9b6452f4394da713bdbc6a89)

uint16\_t wValue

**Definition** usb\_ch9.h:46

[usb\_setup\_packet::wIndex](structusb__setup__packet.md#a953c058f0e31481a3d59b404037be009)

uint16\_t wIndex

**Definition** usb\_ch9.h:47

[usbd\_context](structusbd__context.md)

USB device support runtime context.

**Definition** usbd.h:283

[USB\_GET\_DESCRIPTOR\_INDEX](usb__ch9_8h.md#a653a141a5084536362396149e81b6b9a)

#define USB\_GET\_DESCRIPTOR\_INDEX(wValue)

Macro to obtain descriptor index from USB\_SREQ\_GET\_DESCRIPTOR request.

**Definition** usb\_ch9.h:284

## Field Documentation

## [◆ ](#a91fe4c5cf5ccad89e81380a332a8f955)code

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_vreq\_node::code |
| --- |

Vendor code (bRequest value).

## [◆ ](#a3c68346e2f871b22fb6c3b282ddfdccb)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) usbd\_vreq\_node::node |
| --- |

Node information for the dlist.

## [◆ ](#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3)to\_dev

| int(\* usbd\_vreq\_node::to\_dev) (const struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

Vendor request callback for host-to-device direction.

## [◆ ](#a976d236a26a47cd17316c8174e2ad04a)to\_host

| int(\* usbd\_vreq\_node::to\_host) (const struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

Vendor request callback for device-to-host direction.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_vreq\_node](structusbd__vreq__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
