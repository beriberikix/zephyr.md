---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wuc__ite__it8xxx2_8h_source.html
original_path: doxygen/html/wuc__ite__it8xxx2_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wuc\_ite\_it8xxx2.h

[Go to the documentation of this file.](wuc__ite__it8xxx2_8h.md)

1/\*

2 \* Copyright (c) 2022 ITE Corporation. All Rights Reserved

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_

8#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[stdint.h](stdint_8h.md)>

12

[ 20](wuc__ite__it8xxx2_8h.md#a12abd49530eee59cb3d9670c35c307b1)void [it8xxx2\_wuc\_enable](wuc__ite__it8xxx2_8h.md#a12abd49530eee59cb3d9670c35c307b1)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

21

[ 29](wuc__ite__it8xxx2_8h.md#af707d0b461010aea4fcfbfbeb82d0b2b)void [it8xxx2\_wuc\_disable](wuc__ite__it8xxx2_8h.md#af707d0b461010aea4fcfbfbeb82d0b2b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

30

[ 38](wuc__ite__it8xxx2_8h.md#ad48382e2c3fd0d12c3a1334d863a9065)void [it8xxx2\_wuc\_clear\_status](wuc__ite__it8xxx2_8h.md#ad48382e2c3fd0d12c3a1334d863a9065)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

39

[ 47](wuc__ite__it8xxx2_8h.md#ab589f992436176f288056e219ead7972)void [it8xxx2\_wuc\_set\_polarity](wuc__ite__it8xxx2_8h.md#ab589f992436176f288056e219ead7972)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

49

50#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT8XXX2\_WUC\_H\_ \*/

[device.h](device_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[it8xxx2\_wuc\_enable](wuc__ite__it8xxx2_8h.md#a12abd49530eee59cb3d9670c35c307b1)

void it8xxx2\_wuc\_enable(const struct device \*dev, uint8\_t mask)

A trigger condition on the corresponding input generates a wake-up signal to the power management con...

[it8xxx2\_wuc\_set\_polarity](wuc__ite__it8xxx2_8h.md#ab589f992436176f288056e219ead7972)

void it8xxx2\_wuc\_set\_polarity(const struct device \*dev, uint8\_t mask, uint32\_t flags)

Select the trigger edge mode on the corresponding input.

[it8xxx2\_wuc\_clear\_status](wuc__ite__it8xxx2_8h.md#ad48382e2c3fd0d12c3a1334d863a9065)

void it8xxx2\_wuc\_clear\_status(const struct device \*dev, uint8\_t mask)

Write-1-clear a trigger condition that occurs on the corresponding input.

[it8xxx2\_wuc\_disable](wuc__ite__it8xxx2_8h.md#af707d0b461010aea4fcfbfbeb82d0b2b)

void it8xxx2\_wuc\_disable(const struct device \*dev, uint8\_t mask)

A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pendin...

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wuc\_ite\_it8xxx2.h](wuc__ite__it8xxx2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
