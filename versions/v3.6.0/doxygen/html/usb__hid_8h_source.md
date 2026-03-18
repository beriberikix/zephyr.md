---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb__hid_8h_source.html
original_path: doxygen/html/usb__hid_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_hid.h

[Go to the documentation of this file.](usb__hid_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \* Copyright (c) 2018,2021 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_USB\_HID\_CLASS\_DEVICE\_H\_

14#define ZEPHYR\_INCLUDE\_USB\_HID\_CLASS\_DEVICE\_H\_

15

16#include <[zephyr/usb/class/hid.h](hid_8h.md)>

17#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

34

[ 35](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee)typedef int (\*[hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee))(const struct [device](structdevice.md) \*dev,

36 struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*len,

37 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

[ 38](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0)typedef void (\*[hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0))(const struct [device](structdevice.md) \*dev);

[ 39](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7)typedef void (\*[hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol);

[ 40](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593)typedef void (\*[hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) report\_id);

41

[ 45](structhid__ops.md)struct [hid\_ops](structhid__ops.md) {

[ 46](structhid__ops.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652) [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) [get\_report](structhid__ops.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652);

[ 47](structhid__ops.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5) [hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee) [set\_report](structhid__ops.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5);

[ 48](structhid__ops.md#acc04ebec1deb335ef60bd3a01c6058d6) [hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7) [protocol\_change](structhid__ops.md#acc04ebec1deb335ef60bd3a01c6058d6);

[ 49](structhid__ops.md#a1acc7f77f6896d2925e63402f1b9ffdd) [hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593) [on\_idle](structhid__ops.md#a1acc7f77f6896d2925e63402f1b9ffdd);

50 /\*

51 \* int\_in\_ready is an optional callback that is called when

52 \* the current interrupt IN transfer has completed. This can

53 \* be used to wait for the endpoint to go idle or to trigger

54 \* the next transfer.

55 \*/

[ 56](structhid__ops.md#af1eda81d93e935f9560a26344076f65e) [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) [int\_in\_ready](structhid__ops.md#af1eda81d93e935f9560a26344076f65e);

57#ifdef CONFIG\_ENABLE\_HID\_INT\_OUT\_EP

58 [hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0) int\_out\_ready;

59#endif

60};

61

[ 70](group__usb__hid__device__api.md#ga8b08b633472ceb1323f09ef81176520f)void [usb\_hid\_register\_device](group__usb__hid__device__api.md#ga8b08b633472ceb1323f09ef81176520f)(const struct [device](structdevice.md) \*dev,

71 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*desc,

72 size\_t size,

73 const struct [hid\_ops](structhid__ops.md) \*op);

74

[ 85](group__usb__hid__device__api.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)int [hid\_int\_ep\_write](group__usb__hid__device__api.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)(const struct [device](structdevice.md) \*dev,

86 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

87 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len,

88 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret);

89

[ 102](group__usb__hid__device__api.md#ga7d1b97dd70c25c816a2c78447be13c84)int [hid\_int\_ep\_read](group__usb__hid__device__api.md#ga7d1b97dd70c25c816a2c78447be13c84)(const struct [device](structdevice.md) \*dev,

103 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

104 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len,

105 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes);

106

[ 117](group__usb__hid__device__api.md#gafb6073889bf17eb6a93bb8f182cd3f79)int [usb\_hid\_set\_proto\_code](group__usb__hid__device__api.md#gafb6073889bf17eb6a93bb8f182cd3f79)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proto\_code);

118

[ 126](group__usb__hid__device__api.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)int [usb\_hid\_init](group__usb__hid__device__api.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)(const struct [device](structdevice.md) \*dev);

127

131

135

136#ifdef \_\_cplusplus

137}

138#endif

139

140#endif /\* ZEPHYR\_INCLUDE\_USB\_HID\_CLASS\_DEVICE\_H\_ \*/

[hid\_cb\_t](group__usb__hid__device__api.md#ga04ec088255198d1597df8d70db6257ee)

int(\* hid\_cb\_t)(const struct device \*dev, struct usb\_setup\_packet \*setup, int32\_t \*len, uint8\_t \*\*data)

**Definition** usb\_hid.h:35

[hid\_idle\_cb\_t](group__usb__hid__device__api.md#ga61b4facfbfb729159135f5c7534ca593)

void(\* hid\_idle\_cb\_t)(const struct device \*dev, uint16\_t report\_id)

**Definition** usb\_hid.h:40

[hid\_int\_ep\_read](group__usb__hid__device__api.md#ga7d1b97dd70c25c816a2c78447be13c84)

int hid\_int\_ep\_read(const struct device \*dev, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*ret\_bytes)

Read from USB HID interrupt endpoint buffer.

[usb\_hid\_init](group__usb__hid__device__api.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)

int usb\_hid\_init(const struct device \*dev)

Initialize USB HID class support.

[usb\_hid\_register\_device](group__usb__hid__device__api.md#ga8b08b633472ceb1323f09ef81176520f)

void usb\_hid\_register\_device(const struct device \*dev, const uint8\_t \*desc, size\_t size, const struct hid\_ops \*op)

Register HID device.

[hid\_int\_ep\_write](group__usb__hid__device__api.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)

int hid\_int\_ep\_write(const struct device \*dev, const uint8\_t \*data, uint32\_t data\_len, uint32\_t \*bytes\_ret)

Write to USB HID interrupt endpoint buffer.

[hid\_protocol\_cb\_t](group__usb__hid__device__api.md#gae3d308c55f5594cc0c926b52aaa28fc7)

void(\* hid\_protocol\_cb\_t)(const struct device \*dev, uint8\_t protocol)

**Definition** usb\_hid.h:39

[hid\_int\_ready\_callback](group__usb__hid__device__api.md#gaed433e24f8487d4e451d9f9daa08c5b0)

void(\* hid\_int\_ready\_callback)(const struct device \*dev)

**Definition** usb\_hid.h:38

[usb\_hid\_set\_proto\_code](group__usb__hid__device__api.md#gafb6073889bf17eb6a93bb8f182cd3f79)

int usb\_hid\_set\_proto\_code(const struct device \*dev, uint8\_t proto\_code)

Set USB HID class Protocol Code.

[hid.h](hid_8h.md)

USB Human Interface Device (HID) common definitions header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[hid\_ops](structhid__ops.md)

USB HID device interface.

**Definition** usb\_hid.h:45

[hid\_ops::on\_idle](structhid__ops.md#a1acc7f77f6896d2925e63402f1b9ffdd)

hid\_idle\_cb\_t on\_idle

**Definition** usb\_hid.h:49

[hid\_ops::get\_report](structhid__ops.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652)

hid\_cb\_t get\_report

**Definition** usb\_hid.h:46

[hid\_ops::set\_report](structhid__ops.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5)

hid\_cb\_t set\_report

**Definition** usb\_hid.h:47

[hid\_ops::protocol\_change](structhid__ops.md#acc04ebec1deb335ef60bd3a01c6058d6)

hid\_protocol\_cb\_t protocol\_change

**Definition** usb\_hid.h:48

[hid\_ops::int\_in\_ready](structhid__ops.md#af1eda81d93e935f9560a26344076f65e)

hid\_int\_ready\_callback int\_in\_ready

**Definition** usb\_hid.h:56

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:39

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_hid.h](usb__hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
