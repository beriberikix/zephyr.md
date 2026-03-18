---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__usb__hid__device__api.html
original_path: doxygen/html/group__usb__hid__device__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HID class USB specific definitions

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB HID class API](group__usb__hid__class.md)

| Data Structures | |
| --- | --- |
| struct | [hid\_ops](structhid__ops.md) |
|  | USB HID device interface. [More...](structhid__ops.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hid\_cb\_t](#ga04ec088255198d1597df8d70db6257ee)) (const struct [device](structdevice.md) \*dev, struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
| typedef void(\* | [hid\_int\_ready\_callback](#gaed433e24f8487d4e451d9f9daa08c5b0)) (const struct [device](structdevice.md) \*dev) |
| typedef void(\* | [hid\_protocol\_cb\_t](#gae3d308c55f5594cc0c926b52aaa28fc7)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
| typedef void(\* | [hid\_idle\_cb\_t](#ga61b4facfbfb729159135f5c7534ca593)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) report\_id) |

| Functions | |
| --- | --- |
| void | [usb\_hid\_register\_device](#ga8b08b633472ceb1323f09ef81176520f) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*desc, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const struct [hid\_ops](structhid__ops.md) \*op) |
|  | Register HID device. |
| int | [hid\_int\_ep\_write](#ga9d82d48c9c6c94ad90e01f44c1f0e72b) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret) |
|  | Write to USB HID interrupt endpoint buffer. |
| int | [hid\_int\_ep\_read](#ga7d1b97dd70c25c816a2c78447be13c84) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes) |
|  | Read from USB HID interrupt endpoint buffer. |
| int | [usb\_hid\_set\_proto\_code](#gafb6073889bf17eb6a93bb8f182cd3f79) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto\_code) |
|  | Set USB HID class Protocol Code. |
| int | [usb\_hid\_init](#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b) (const struct [device](structdevice.md) \*dev) |
|  | Initialize USB HID class support. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga04ec088255198d1597df8d70db6257ee)hid\_cb\_t

| typedef int(\* hid\_cb\_t) (const struct [device](structdevice.md) \*dev, struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
| --- |

`#include <[usb_hid.h](usb__hid_8h.md)>`

## [◆ ](#ga61b4facfbfb729159135f5c7534ca593)hid\_idle\_cb\_t

| typedef void(\* hid\_idle\_cb\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) report\_id) |
| --- |

`#include <[usb_hid.h](usb__hid_8h.md)>`

## [◆ ](#gaed433e24f8487d4e451d9f9daa08c5b0)hid\_int\_ready\_callback

| typedef void(\* hid\_int\_ready\_callback) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[usb_hid.h](usb__hid_8h.md)>`

## [◆ ](#gae3d308c55f5594cc0c926b52aaa28fc7)hid\_protocol\_cb\_t

| typedef void(\* hid\_protocol\_cb\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
| --- |

`#include <[usb_hid.h](usb__hid_8h.md)>`

## Function Documentation

## [◆ ](#ga7d1b97dd70c25c816a2c78447be13c84)hid\_int\_ep\_read()

| int hid\_int\_ep\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *ret\_bytes* ) |

`#include <[usb_hid.h](usb__hid_8h.md)>`

Read from USB HID interrupt endpoint buffer.

Parameters
:   | [in] | dev | Pointer to USB HID device |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer |
    | [in] | max\_data\_len | Max length of data to copy |
    | [out] | ret\_bytes | Number of bytes to copy. If data is NULL and max\_data\_len is 0 the number of bytes available in the buffer will be returned. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga9d82d48c9c6c94ad90e01f44c1f0e72b)hid\_int\_ep\_write()

| int hid\_int\_ep\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *bytes\_ret* ) |

`#include <[usb_hid.h](usb__hid_8h.md)>`

Write to USB HID interrupt endpoint buffer.

Parameters
:   | [in] | dev | Pointer to USB HID device |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer |
    | [in] | data\_len | Length of data to copy |
    | [out] | bytes\_ret | Bytes written to the EP buffer. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)usb\_hid\_init()

| int usb\_hid\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_hid.h](usb__hid_8h.md)>`

Initialize USB HID class support.

Parameters
:   | [in] | dev | Pointer to USB HID device |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga8b08b633472ceb1323f09ef81176520f)usb\_hid\_register\_device()

| void usb\_hid\_register\_device | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *desc*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const struct [hid\_ops](structhid__ops.md) \* | *op* ) |

`#include <[usb_hid.h](usb__hid_8h.md)>`

Register HID device.

Parameters
:   | [in] | dev | Pointer to USB HID device |
    | --- | --- | --- |
    | [in] | desc | Pointer to HID report descriptor |
    | [in] | size | Size of HID report descriptor |
    | [in] | op | Pointer to USB HID device interrupt struct |

## [◆ ](#gafb6073889bf17eb6a93bb8f182cd3f79)usb\_hid\_set\_proto\_code()

| int usb\_hid\_set\_proto\_code | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proto\_code* ) |

`#include <[usb_hid.h](usb__hid_8h.md)>`

Set USB HID class Protocol Code.

Should be called before [usb\_hid\_init()](#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b).

Parameters
:   | [in] | dev | Pointer to USB HID device |
    | --- | --- | --- |
    | [in] | proto\_code | Protocol Code to be used for bInterfaceProtocol |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
