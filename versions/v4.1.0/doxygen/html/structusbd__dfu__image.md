---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__dfu__image.html
original_path: doxygen/html/structusbd__dfu__image.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_dfu\_image Struct Reference

`#include <[usbd_dfu.h](usbd__dfu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a3e2d6339752919988f3c113ca87a543e) |
| struct [usb\_if\_descriptor](structusb__if__descriptor.md) \*const | [if\_desc](#a4df9017274c5094ed49fd8e6964b4379) |
| void \*const | [priv](#a2aade79d72faef1fe8a6fe846189daf0) |
| struct [usbd\_desc\_node](structusbd__desc__node.md) \*const | [sd\_nd](#aff741ab9145292e9b7a30fe3a93a4615) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [next\_cb](#a2202146c73e3b2300200f04eff05c888) )(void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) next) |
| int(\* | [read\_cb](#a03ee7685c90ac7ec8c2c4d87a6389e62) )(void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]) |
| int(\* | [write\_cb](#aad9a4efbf3649373328b6b6b12fa1922) )(void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]) |

## Field Documentation

## [◆ ](#a4df9017274c5094ed49fd8e6964b4379)if\_desc

| struct [usb\_if\_descriptor](structusb__if__descriptor.md)\* const usbd\_dfu\_image::if\_desc |
| --- |

## [◆ ](#a3e2d6339752919988f3c113ca87a543e)name

| const char\* usbd\_dfu\_image::name |
| --- |

## [◆ ](#a2202146c73e3b2300200f04eff05c888)next\_cb

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* usbd\_dfu\_image::next\_cb) (void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) next) |
| --- |

## [◆ ](#a2aade79d72faef1fe8a6fe846189daf0)priv

| void\* const usbd\_dfu\_image::priv |
| --- |

## [◆ ](#a03ee7685c90ac7ec8c2c4d87a6389e62)read\_cb

| int(\* usbd\_dfu\_image::read\_cb) (void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]) |
| --- |

## [◆ ](#aff741ab9145292e9b7a30fe3a93a4615)sd\_nd

| struct [usbd\_desc\_node](structusbd__desc__node.md)\* const usbd\_dfu\_image::sd\_nd |
| --- |

## [◆ ](#aad9a4efbf3649373328b6b6b12fa1922)write\_cb

| int(\* usbd\_dfu\_image::write\_cb) (void \*const [priv](#a2aade79d72faef1fe8a6fe846189daf0), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usbd\_dfu.h](usbd__dfu_8h_source.md)

- [usbd\_dfu\_image](structusbd__dfu__image.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
