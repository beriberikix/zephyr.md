---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input__analog__axis_8h_source.html
original_path: doxygen/html/input__analog__axis_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_analog\_axis.h

[Go to the documentation of this file.](input__analog__axis_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12

19

[ 27](structanalog__axis__calibration.md)struct [analog\_axis\_calibration](structanalog__axis__calibration.md) {

[ 29](structanalog__axis__calibration.md#a2a0b2c3ec62b66c05b187411a8b3e4db) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [in\_min](structanalog__axis__calibration.md#a2a0b2c3ec62b66c05b187411a8b3e4db);

[ 31](structanalog__axis__calibration.md#a67a595a038b2a244d16e759aecf5856a) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [in\_max](structanalog__axis__calibration.md#a67a595a038b2a244d16e759aecf5856a);

[ 33](structanalog__axis__calibration.md#a8c583137a2605d7ba48da2291de46590) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [in\_deadzone](structanalog__axis__calibration.md#a8c583137a2605d7ba48da2291de46590);

34};

35

[ 43](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64)typedef void (\*[analog\_axis\_raw\_data\_t](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64))(const struct [device](structdevice.md) \*dev,

44 int channel, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) raw\_val);

45

[ 56](group__input__analog__axis.md#ga645237cdb40113e4253a24e902091f3e)void [analog\_axis\_set\_raw\_data\_cb](group__input__analog__axis.md#ga645237cdb40113e4253a24e902091f3e)(const struct [device](structdevice.md) \*dev, [analog\_axis\_raw\_data\_t](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64) cb);

57

[ 63](group__input__analog__axis.md#ga99dd3b96a43f115a8c90859e7eed24d4)int [analog\_axis\_num\_axes](group__input__analog__axis.md#ga99dd3b96a43f115a8c90859e7eed24d4)(const struct [device](structdevice.md) \*dev);

64

[ 76](group__input__analog__axis.md#gad359f00fa9c46219a55a218d26d0407a)int [analog\_axis\_calibration\_get](group__input__analog__axis.md#gad359f00fa9c46219a55a218d26d0407a)(const struct [device](structdevice.md) \*dev,

77 int channel,

78 struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal);

79

[ 91](group__input__analog__axis.md#gaae496bde41a58d92521b0a24f762caeb)int [analog\_axis\_calibration\_set](group__input__analog__axis.md#gaae496bde41a58d92521b0a24f762caeb)(const struct [device](structdevice.md) \*dev,

92 int channel,

93 struct [analog\_axis\_calibration](structanalog__axis__calibration.md) \*cal);

94

96

97#endif /\* ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_H\_ \*/

[device.h](device_8h.md)

[analog\_axis\_raw\_data\_t](group__input__analog__axis.md#ga384e901afe29ae91e01c44b458034d64)

void(\* analog\_axis\_raw\_data\_t)(const struct device \*dev, int channel, int16\_t raw\_val)

Analog axis raw data callback.

**Definition** input\_analog\_axis.h:43

[analog\_axis\_set\_raw\_data\_cb](group__input__analog__axis.md#ga645237cdb40113e4253a24e902091f3e)

void analog\_axis\_set\_raw\_data\_cb(const struct device \*dev, analog\_axis\_raw\_data\_t cb)

Set a raw data callback.

[analog\_axis\_num\_axes](group__input__analog__axis.md#ga99dd3b96a43f115a8c90859e7eed24d4)

int analog\_axis\_num\_axes(const struct device \*dev)

Get the number of defined axes.

[analog\_axis\_calibration\_set](group__input__analog__axis.md#gaae496bde41a58d92521b0a24f762caeb)

int analog\_axis\_calibration\_set(const struct device \*dev, int channel, struct analog\_axis\_calibration \*cal)

Set the axis calibration data.

[analog\_axis\_calibration\_get](group__input__analog__axis.md#gad359f00fa9c46219a55a218d26d0407a)

int analog\_axis\_calibration\_get(const struct device \*dev, int channel, struct analog\_axis\_calibration \*cal)

Get the axis calibration data.

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[analog\_axis\_calibration](structanalog__axis__calibration.md)

Analog axis calibration data structure.

**Definition** input\_analog\_axis.h:27

[analog\_axis\_calibration::in\_min](structanalog__axis__calibration.md#a2a0b2c3ec62b66c05b187411a8b3e4db)

int16\_t in\_min

Input value that corresponds to the minimum output value.

**Definition** input\_analog\_axis.h:29

[analog\_axis\_calibration::in\_max](structanalog__axis__calibration.md#a67a595a038b2a244d16e759aecf5856a)

int16\_t in\_max

Input value that corresponds to the maximum output value.

**Definition** input\_analog\_axis.h:31

[analog\_axis\_calibration::in\_deadzone](structanalog__axis__calibration.md#a8c583137a2605d7ba48da2291de46590)

uint16\_t in\_deadzone

Input value center deadzone.

**Definition** input\_analog\_axis.h:33

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_analog\_axis.h](input__analog__axis_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
