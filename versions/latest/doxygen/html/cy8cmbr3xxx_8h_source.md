---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cy8cmbr3xxx_8h_source.html
original_path: doxygen/html/cy8cmbr3xxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cy8cmbr3xxx.h

[Go to the documentation of this file.](cy8cmbr3xxx_8h.md)

1/\*

2 \* Copyright (c) 2025 Basalte bv

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_INPUT\_CY8CMBR3XXX\_H\_

7#define ZEPHYR\_INCLUDE\_INPUT\_CY8CMBR3XXX\_H\_

8

9#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

10

[ 11](cy8cmbr3xxx_8h.md#a0d8534cc7dc74a6b17cf30ecb4ac1bfd)#define CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE 128

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif /\* \_\_cplusplus \*/

16

[ 17](structcy8cmbr3xxx__config__data.md)struct [cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md) {

[ 18](structcy8cmbr3xxx__config__data.md#aadacd16ce180b86d1c80c8e56b5dc4da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcy8cmbr3xxx__config__data.md#aadacd16ce180b86d1c80c8e56b5dc4da)[[CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE](cy8cmbr3xxx_8h.md#a0d8534cc7dc74a6b17cf30ecb4ac1bfd)];

19};

20

[ 30](cy8cmbr3xxx_8h.md#a26da2ccc3ff92bc2c29021f66f184448)int [cy8cmbr3xxx\_configure](cy8cmbr3xxx_8h.md#a26da2ccc3ff92bc2c29021f66f184448)(const struct [device](structdevice.md) \*dev,

31 const struct [cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md) \*config\_data);

32

33#ifdef \_\_cplusplus

34}

35#endif /\* \_\_cplusplus \*/

36

37#endif /\* ZEPHYR\_INCLUDE\_INPUT\_CY8CMBR3XXX\_H\_ \*/

[CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE](cy8cmbr3xxx_8h.md#a0d8534cc7dc74a6b17cf30ecb4ac1bfd)

#define CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE

**Definition** cy8cmbr3xxx.h:11

[cy8cmbr3xxx\_configure](cy8cmbr3xxx_8h.md#a26da2ccc3ff92bc2c29021f66f184448)

int cy8cmbr3xxx\_configure(const struct device \*dev, const struct cy8cmbr3xxx\_config\_data \*config\_data)

Configure the CY8CMBR3xxx device with an EZ-Click generated configuration.

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md)

**Definition** cy8cmbr3xxx.h:17

[cy8cmbr3xxx\_config\_data::data](structcy8cmbr3xxx__config__data.md#aadacd16ce180b86d1c80c8e56b5dc4da)

uint8\_t data[128]

**Definition** cy8cmbr3xxx.h:18

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [cy8cmbr3xxx.h](cy8cmbr3xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
