---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usbd__dfu.html
original_path: doxygen/html/group__usbd__dfu.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB DFU device update API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB DFU device update API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [USBD\_DFU\_DEFINE\_IMG](#ga24229d3b70d2e61bb1658c35f0be5070)(id, iname, ipriv, iread, iwrite, inext) |
|  | Define USB DFU image. |

## Detailed Description

USB DFU device update API.

## Macro Definition Documentation

## [◆ ](#ga24229d3b70d2e61bb1658c35f0be5070)USBD\_DFU\_DEFINE\_IMG

| #define USBD\_DFU\_DEFINE\_IMG | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *iname*, |
|  |  |  | *ipriv*, |
|  |  |  | *iread*, |
|  |  |  | *iwrite*, |
|  |  |  | *inext* ) |

`#include <[usbd_dfu.h](usbd__dfu_8h.md)>`

**Value:**

static \_\_noinit struct [usb\_if\_descriptor](structusb__if__descriptor.md) usbd\_dfu\_iface\_##id; \

\

USBD\_DESC\_STRING\_DEFINE(usbd\_dfu\_str\_##id, iname, USBD\_DUT\_STRING\_INTERFACE); \

\

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbd\_dfu\_image](structusbd__dfu__image.md), usbd\_dfu\_image\_##id) = { \

.name = iname, \

.if\_desc = &usbd\_dfu\_iface\_##id, \

.priv = ipriv, \

.sd\_nd = &usbd\_dfu\_str\_##id, \

.read\_cb = iread, \

.write\_cb = iwrite, \

.next\_cb = inext, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usb\_if\_descriptor](structusb__if__descriptor.md)

USB Standard Interface Descriptor defined in spec.

**Definition** usb\_ch9.h:193

[usbd\_dfu\_image](structusbd__dfu__image.md)

**Definition** usbd\_dfu.h:95

Define USB DFU image.

Use this macro to create USB DFU image

The callbacks must be in form:

static int read(void \*const priv, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE])

{

int len;

return len;

}

static int write(void \*const priv, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE])

{

return 0;

}

static bool next(void \*const priv,

const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) next)

{

return true;

}

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e)

usb\_dfu\_state

**Definition** usbd\_dfu.h:80

Parameters
:   | id | Identifier by which the linker sorts registered images |
    | --- | --- |
    | iname | Image name as used in interface descriptor |
    | iread | Image read callback |
    | iwrite | Image write callback |
    | inext | Notify/confirm next state |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
