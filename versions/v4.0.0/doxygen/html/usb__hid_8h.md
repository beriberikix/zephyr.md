---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usb__hid_8h.html
original_path: doxygen/html/usb__hid_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_hid.h File Reference

USB HID Class device API header.
[More...](#details)

`#include <[zephyr/usb/class/hid.h](hid_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`

[Go to the source code of this file.](usb__hid_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hid\_ops](structhid__ops.md) |
|  | USB HID device interface. [More...](structhid__ops.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee)) (const struct [device](structdevice.md) \*dev, struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
| typedef void(\* | [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0)) (const struct [device](structdevice.md) \*dev) |
| typedef void(\* | [hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
| typedef void(\* | [hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) report\_id) |

| Functions | |
| --- | --- |
| void | [usb\_hid\_register\_device](group__usb__hid__device__api.md#ga8b08b633472ceb1323f09ef81176520f) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*desc, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const struct [hid\_ops](structhid__ops.md) \*op) |
|  | Register HID device. |
| int | [hid\_int\_ep\_write](group__usb__hid__device__api.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret) |
|  | Write to USB HID interrupt endpoint buffer. |
| int | [hid\_int\_ep\_read](group__usb__hid__device__api.md#ga7d1b97dd70c25c816a2c78447be13c84) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes) |
|  | Read from USB HID interrupt endpoint buffer. |
| int | [usb\_hid\_set\_proto\_code](group__usb__hid__device__api.md#gafb6073889bf17eb6a93bb8f182cd3f79) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto\_code) |
|  | Set USB HID class Protocol Code. |
| int | [usb\_hid\_init](group__usb__hid__device__api.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b) (const struct [device](structdevice.md) \*dev) |
|  | Initialize USB HID class support. |

## Detailed Description

USB HID Class device API header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_hid.h](usb__hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
