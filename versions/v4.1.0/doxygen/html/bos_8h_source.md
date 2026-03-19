---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bos_8h_source.html
original_path: doxygen/html/bos_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bos.h

[Go to the documentation of this file.](bos_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_USB\_BOS\_H\_

9#define ZEPHYR\_INCLUDE\_USB\_BOS\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12

21

[ 23](structusb__bos__descriptor.md)struct [usb\_bos\_descriptor](structusb__bos__descriptor.md) {

[ 24](structusb__bos__descriptor.md#aa3a661440a4b6d6a2ecf27da740c4121) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__bos__descriptor.md#aa3a661440a4b6d6a2ecf27da740c4121);

[ 25](structusb__bos__descriptor.md#afd74417a44821690051d50cd5ffdd581) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__bos__descriptor.md#afd74417a44821690051d50cd5ffdd581);

[ 26](structusb__bos__descriptor.md#ab45b26a3249589469a53b2cfb99ddd1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTotalLength](structusb__bos__descriptor.md#ab45b26a3249589469a53b2cfb99ddd1d);

[ 27](structusb__bos__descriptor.md#a2c0e68a49d6904d32413f3b3598bb926) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bNumDeviceCaps](structusb__bos__descriptor.md#a2c0e68a49d6904d32413f3b3598bb926);

28} \_\_packed;

29

[ 31](group__usb__bos.md#ga0bddefd6b9373068cd4ff8e6fc47950d)enum [usb\_bos\_capability\_types](group__usb__bos.md#ga0bddefd6b9373068cd4ff8e6fc47950d) {

[ 32](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862) [USB\_BOS\_CAPABILITY\_EXTENSION](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862) = 0x02,

[ 33](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b) [USB\_BOS\_CAPABILITY\_PLATFORM](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b) = 0x05,

34};

35

[ 37](structusb__bos__capability__lpm.md)struct [usb\_bos\_capability\_lpm](structusb__bos__capability__lpm.md) {

[ 38](structusb__bos__capability__lpm.md#a09ec679e05e7b848800ab63220109bef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__bos__capability__lpm.md#a09ec679e05e7b848800ab63220109bef);

[ 39](structusb__bos__capability__lpm.md#a880b1f6efecf7d1e8e9076680c74f9c2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__bos__capability__lpm.md#a880b1f6efecf7d1e8e9076680c74f9c2);

[ 40](structusb__bos__capability__lpm.md#a1ceea07e81970d684a6c1586364a0c90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDevCapabilityType](structusb__bos__capability__lpm.md#a1ceea07e81970d684a6c1586364a0c90);

[ 41](structusb__bos__capability__lpm.md#a8a643af1e99eafdecc006cf714cb0af7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bmAttributes](structusb__bos__capability__lpm.md#a8a643af1e99eafdecc006cf714cb0af7);

42} \_\_packed;

43

[ 45](structusb__bos__platform__descriptor.md)struct [usb\_bos\_platform\_descriptor](structusb__bos__platform__descriptor.md) {

[ 46](structusb__bos__platform__descriptor.md#a477ab8e85845e8809ff7f4bd1bcc0f8a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__bos__platform__descriptor.md#a477ab8e85845e8809ff7f4bd1bcc0f8a);

[ 47](structusb__bos__platform__descriptor.md#a26a748945b0223d369a05ad06a2c6d05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__bos__platform__descriptor.md#a26a748945b0223d369a05ad06a2c6d05);

[ 48](structusb__bos__platform__descriptor.md#a8e8e95a1648e6bba7568c519158de917) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDevCapabilityType](structusb__bos__platform__descriptor.md#a8e8e95a1648e6bba7568c519158de917);

[ 49](structusb__bos__platform__descriptor.md#a477719191468cec83d2a92a5d6f1231d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bReserved](structusb__bos__platform__descriptor.md#a477719191468cec83d2a92a5d6f1231d);

[ 50](structusb__bos__platform__descriptor.md#a09f10af1f29bccdd300be504cd2dda10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [PlatformCapabilityUUID](structusb__bos__platform__descriptor.md#a09f10af1f29bccdd300be504cd2dda10)[16];

51} \_\_packed;

52

[ 54](structusb__bos__capability__webusb.md)struct [usb\_bos\_capability\_webusb](structusb__bos__capability__webusb.md) {

[ 55](structusb__bos__capability__webusb.md#a1ebbfa1bdca4ad783000c67419552e54) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdVersion](structusb__bos__capability__webusb.md#a1ebbfa1bdca4ad783000c67419552e54);

[ 56](structusb__bos__capability__webusb.md#a3ae4aada1ab7b28d9bac6294467e93ff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bVendorCode](structusb__bos__capability__webusb.md#a3ae4aada1ab7b28d9bac6294467e93ff);

[ 57](structusb__bos__capability__webusb.md#a068861c7ee1abfdb03e52b8269db30b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iLandingPage](structusb__bos__capability__webusb.md#a068861c7ee1abfdb03e52b8269db30b5);

58} \_\_packed;

59

[ 61](structusb__bos__capability__msos.md)struct [usb\_bos\_capability\_msos](structusb__bos__capability__msos.md) {

[ 62](structusb__bos__capability__msos.md#a5e10aed83d93d2ddc1278245aab9cb0a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dwWindowsVersion](structusb__bos__capability__msos.md#a5e10aed83d93d2ddc1278245aab9cb0a);

[ 63](structusb__bos__capability__msos.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wMSOSDescriptorSetTotalLength](structusb__bos__capability__msos.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5);

[ 64](structusb__bos__capability__msos.md#a4da7539d3bc58fe1da48e3d4d8c965e2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bMS\_VendorCode](structusb__bos__capability__msos.md#a4da7539d3bc58fe1da48e3d4d8c965e2);

[ 65](structusb__bos__capability__msos.md#a0945c68d9e7911add0c0586b000c90d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bAltEnumCode](structusb__bos__capability__msos.md#a0945c68d9e7911add0c0586b000c90d3);

66} \_\_packed;

67

71

72#endif /\* ZEPHYR\_INCLUDE\_USB\_BOS\_H\_ \*/

[usb\_bos\_capability\_types](group__usb__bos.md#ga0bddefd6b9373068cd4ff8e6fc47950d)

usb\_bos\_capability\_types

Device capability type codes.

**Definition** bos.h:31

[USB\_BOS\_CAPABILITY\_EXTENSION](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862)

@ USB\_BOS\_CAPABILITY\_EXTENSION

**Definition** bos.h:32

[USB\_BOS\_CAPABILITY\_PLATFORM](group__usb__bos.md#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b)

@ USB\_BOS\_CAPABILITY\_PLATFORM

**Definition** bos.h:33

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[usb\_bos\_capability\_lpm](structusb__bos__capability__lpm.md)

BOS USB 2.0 extension capability descriptor.

**Definition** bos.h:37

[usb\_bos\_capability\_lpm::bLength](structusb__bos__capability__lpm.md#a09ec679e05e7b848800ab63220109bef)

uint8\_t bLength

**Definition** bos.h:38

[usb\_bos\_capability\_lpm::bDevCapabilityType](structusb__bos__capability__lpm.md#a1ceea07e81970d684a6c1586364a0c90)

uint8\_t bDevCapabilityType

**Definition** bos.h:40

[usb\_bos\_capability\_lpm::bDescriptorType](structusb__bos__capability__lpm.md#a880b1f6efecf7d1e8e9076680c74f9c2)

uint8\_t bDescriptorType

**Definition** bos.h:39

[usb\_bos\_capability\_lpm::bmAttributes](structusb__bos__capability__lpm.md#a8a643af1e99eafdecc006cf714cb0af7)

uint32\_t bmAttributes

**Definition** bos.h:41

[usb\_bos\_capability\_msos](structusb__bos__capability__msos.md)

Microsoft OS 2.0 descriptor specific part of platform capability descriptor.

**Definition** bos.h:61

[usb\_bos\_capability\_msos::bAltEnumCode](structusb__bos__capability__msos.md#a0945c68d9e7911add0c0586b000c90d3)

uint8\_t bAltEnumCode

**Definition** bos.h:65

[usb\_bos\_capability\_msos::bMS\_VendorCode](structusb__bos__capability__msos.md#a4da7539d3bc58fe1da48e3d4d8c965e2)

uint8\_t bMS\_VendorCode

**Definition** bos.h:64

[usb\_bos\_capability\_msos::dwWindowsVersion](structusb__bos__capability__msos.md#a5e10aed83d93d2ddc1278245aab9cb0a)

uint32\_t dwWindowsVersion

**Definition** bos.h:62

[usb\_bos\_capability\_msos::wMSOSDescriptorSetTotalLength](structusb__bos__capability__msos.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5)

uint16\_t wMSOSDescriptorSetTotalLength

**Definition** bos.h:63

[usb\_bos\_capability\_webusb](structusb__bos__capability__webusb.md)

WebUSB specific part of platform capability descriptor.

**Definition** bos.h:54

[usb\_bos\_capability\_webusb::iLandingPage](structusb__bos__capability__webusb.md#a068861c7ee1abfdb03e52b8269db30b5)

uint8\_t iLandingPage

**Definition** bos.h:57

[usb\_bos\_capability\_webusb::bcdVersion](structusb__bos__capability__webusb.md#a1ebbfa1bdca4ad783000c67419552e54)

uint16\_t bcdVersion

**Definition** bos.h:55

[usb\_bos\_capability\_webusb::bVendorCode](structusb__bos__capability__webusb.md#a3ae4aada1ab7b28d9bac6294467e93ff)

uint8\_t bVendorCode

**Definition** bos.h:56

[usb\_bos\_descriptor](structusb__bos__descriptor.md)

Root BOS Descriptor.

**Definition** bos.h:23

[usb\_bos\_descriptor::bNumDeviceCaps](structusb__bos__descriptor.md#a2c0e68a49d6904d32413f3b3598bb926)

uint8\_t bNumDeviceCaps

**Definition** bos.h:27

[usb\_bos\_descriptor::bLength](structusb__bos__descriptor.md#aa3a661440a4b6d6a2ecf27da740c4121)

uint8\_t bLength

**Definition** bos.h:24

[usb\_bos\_descriptor::wTotalLength](structusb__bos__descriptor.md#ab45b26a3249589469a53b2cfb99ddd1d)

uint16\_t wTotalLength

**Definition** bos.h:26

[usb\_bos\_descriptor::bDescriptorType](structusb__bos__descriptor.md#afd74417a44821690051d50cd5ffdd581)

uint8\_t bDescriptorType

**Definition** bos.h:25

[usb\_bos\_platform\_descriptor](structusb__bos__platform__descriptor.md)

BOS platform capability descriptor.

**Definition** bos.h:45

[usb\_bos\_platform\_descriptor::PlatformCapabilityUUID](structusb__bos__platform__descriptor.md#a09f10af1f29bccdd300be504cd2dda10)

uint8\_t PlatformCapabilityUUID[16]

**Definition** bos.h:50

[usb\_bos\_platform\_descriptor::bDescriptorType](structusb__bos__platform__descriptor.md#a26a748945b0223d369a05ad06a2c6d05)

uint8\_t bDescriptorType

**Definition** bos.h:47

[usb\_bos\_platform\_descriptor::bReserved](structusb__bos__platform__descriptor.md#a477719191468cec83d2a92a5d6f1231d)

uint8\_t bReserved

**Definition** bos.h:49

[usb\_bos\_platform\_descriptor::bLength](structusb__bos__platform__descriptor.md#a477ab8e85845e8809ff7f4bd1bcc0f8a)

uint8\_t bLength

**Definition** bos.h:46

[usb\_bos\_platform\_descriptor::bDevCapabilityType](structusb__bos__platform__descriptor.md#a8e8e95a1648e6bba7568c519158de917)

uint8\_t bDevCapabilityType

**Definition** bos.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [bos.h](bos_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
