---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbd__uac2_8h_source.html
original_path: doxygen/html/usbd__uac2_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_uac2.h

[Go to the documentation of this file.](usbd__uac2_8h.md)

1/\*

2 \* Copyright (c) 2023-2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UAC2\_H\_

18#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UAC2\_H\_

19

20#include <[zephyr/device.h](device_8h.md)>

21

[ 22](usbd__uac2_8h.md#aa35265e83d894896806fcca28feb84a3)#define UAC2\_ENTITY\_ID(node) \

23 ({ \

24 BUILD\_ASSERT(DT\_NODE\_HAS\_COMPAT(DT\_PARENT(node), zephyr\_uac2)); \

25 UTIL\_INC(DT\_NODE\_CHILD\_IDX(node)); \

26 })

27

[ 31](structuac2__ops.md)struct [uac2\_ops](structuac2__ops.md) {

[ 40](structuac2__ops.md#a76e31b01dc6ce52793735b70301e8470) void (\*[sof\_cb](structuac2__ops.md#a76e31b01dc6ce52793735b70301e8470))(const struct [device](structdevice.md) \*dev, void \*user\_data);

[ 52](structuac2__ops.md#ae938633dcf6eb6f120ca458bf8a2142f) void (\*[terminal\_update\_cb](structuac2__ops.md#ae938633dcf6eb6f120ca458bf8a2142f))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

53 bool enabled, bool microframes,

54 void \*user\_data);

[ 68](structuac2__ops.md#ab41274aadc39d39cbcbfe0047a56f24b) void \*(\*get\_recv\_buf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

69 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data);

[ 82](structuac2__ops.md#abb973db8018d09ba34f508c4e8aff573) void (\*[data\_recv\_cb](structuac2__ops.md#abb973db8018d09ba34f508c4e8aff573))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

83 void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, void \*user\_data);

[ 95](structuac2__ops.md#aa934f5ecee8f8e67e2165735a6dd2bca) void (\*[buf\_release\_cb](structuac2__ops.md#aa934f5ecee8f8e67e2165735a6dd2bca))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

96 void \*buf, void \*user\_data);

[ 112](structuac2__ops.md#ad427ec3534c8c2b1fe097a7eb83a2e87) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[feedback\_cb](structuac2__ops.md#ad427ec3534c8c2b1fe097a7eb83a2e87))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

113 void \*user\_data);

114};

115

[ 123](usbd__uac2_8h.md#a802a727c1a201c26a3bd74f0e7f0900c)void [usbd\_uac2\_set\_ops](usbd__uac2_8h.md#a802a727c1a201c26a3bd74f0e7f0900c)(const struct [device](structdevice.md) \*dev,

124 const struct [uac2\_ops](structuac2__ops.md) \*ops, void \*user\_data);

125

[ 136](usbd__uac2_8h.md#ae899d75d786f5b1df86db48de88d1254)int [usbd\_uac2\_send](usbd__uac2_8h.md#ae899d75d786f5b1df86db48de88d1254)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal,

137 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size);

138

139#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UAC2\_H\_ \*/

[device.h](device_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[uac2\_ops](structuac2__ops.md)

USB Audio 2 application event handlers.

**Definition** usbd\_uac2.h:31

[uac2\_ops::sof\_cb](structuac2__ops.md#a76e31b01dc6ce52793735b70301e8470)

void(\* sof\_cb)(const struct device \*dev, void \*user\_data)

Start of Frame callback.

**Definition** usbd\_uac2.h:40

[uac2\_ops::buf\_release\_cb](structuac2__ops.md#aa934f5ecee8f8e67e2165735a6dd2bca)

void(\* buf\_release\_cb)(const struct device \*dev, uint8\_t terminal, void \*buf, void \*user\_data)

Transmit buffer release callback.

**Definition** usbd\_uac2.h:95

[uac2\_ops::data\_recv\_cb](structuac2__ops.md#abb973db8018d09ba34f508c4e8aff573)

void(\* data\_recv\_cb)(const struct device \*dev, uint8\_t terminal, void \*buf, uint16\_t size, void \*user\_data)

Data received.

**Definition** usbd\_uac2.h:82

[uac2\_ops::feedback\_cb](structuac2__ops.md#ad427ec3534c8c2b1fe097a7eb83a2e87)

uint32\_t(\* feedback\_cb)(const struct device \*dev, uint8\_t terminal, void \*user\_data)

Get Explicit Feedback value.

**Definition** usbd\_uac2.h:112

[uac2\_ops::terminal\_update\_cb](structuac2__ops.md#ae938633dcf6eb6f120ca458bf8a2142f)

void(\* terminal\_update\_cb)(const struct device \*dev, uint8\_t terminal, bool enabled, bool microframes, void \*user\_data)

Terminal update callback.

**Definition** usbd\_uac2.h:52

[usbd\_uac2\_set\_ops](usbd__uac2_8h.md#a802a727c1a201c26a3bd74f0e7f0900c)

void usbd\_uac2\_set\_ops(const struct device \*dev, const struct uac2\_ops \*ops, void \*user\_data)

Register USB Audio 2 application callbacks.

[usbd\_uac2\_send](usbd__uac2_8h.md#ae899d75d786f5b1df86db48de88d1254)

int usbd\_uac2\_send(const struct device \*dev, uint8\_t terminal, void \*data, uint16\_t size)

Send audio data to output terminal.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_uac2.h](usbd__uac2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
