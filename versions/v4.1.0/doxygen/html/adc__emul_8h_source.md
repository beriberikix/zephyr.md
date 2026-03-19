---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adc__emul_8h_source.html
original_path: doxygen/html/adc__emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_emul.h

[Go to the documentation of this file.](adc__emul_8h.md)

1

6

7/\*

8 \* Copyright 2021 Google LLC

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADC\_EMUL\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADC\_EMUL\_H\_

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[zephyr/drivers/adc.h](drivers_2adc_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

46

[ 59](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f)typedef int (\*[adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f))(const struct [device](structdevice.md) \*dev, unsigned int chan,

60 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result);

61

[ 72](group__adc__emul.md#ga564c588b71ec63aedb32f0c6221abd69)int [adc\_emul\_const\_value\_set](group__adc__emul.md#ga564c588b71ec63aedb32f0c6221abd69)(const struct [device](structdevice.md) \*dev, unsigned int chan,

73 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

74

[ 85](group__adc__emul.md#ga33dc3b494e7ac620c8cb35fd8324fd61)int [adc\_emul\_const\_raw\_value\_set](group__adc__emul.md#ga33dc3b494e7ac620c8cb35fd8324fd61)(const struct [device](structdevice.md) \*dev, unsigned int chan, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) raw\_value);

86

[ 99](group__adc__emul.md#gae5036c155341dd61d37558c311d3c554)int [adc\_emul\_value\_func\_set](group__adc__emul.md#gae5036c155341dd61d37558c311d3c554)(const struct [device](structdevice.md) \*dev, unsigned int chan,

100 [adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f) func, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

101

[ 114](group__adc__emul.md#ga9d3f19bd7812722d982f0ceda0418afa)int [adc\_emul\_raw\_value\_func\_set](group__adc__emul.md#ga9d3f19bd7812722d982f0ceda0418afa)(const struct [device](structdevice.md) \*dev, unsigned int chan,

115 [adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f) func, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

116

[ 127](group__adc__emul.md#ga53179798ec576b329927e5b6c845aa04)int [adc\_emul\_ref\_voltage\_set](group__adc__emul.md#ga53179798ec576b329927e5b6c845aa04)(const struct [device](structdevice.md) \*dev, enum [adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56) ref,

128 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

132

133#ifdef \_\_cplusplus

134}

135#endif

136

137#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADC\_EMUL\_H\_ \*/

[adc.h](drivers_2adc_8h.md)

ADC public API header file.

[adc\_emul\_const\_raw\_value\_set](group__adc__emul.md#ga33dc3b494e7ac620c8cb35fd8324fd61)

int adc\_emul\_const\_raw\_value\_set(const struct device \*dev, unsigned int chan, uint32\_t raw\_value)

Set constant raw value input for emulated ADC chan.

[adc\_emul\_ref\_voltage\_set](group__adc__emul.md#ga53179798ec576b329927e5b6c845aa04)

int adc\_emul\_ref\_voltage\_set(const struct device \*dev, enum adc\_reference ref, uint16\_t value)

Set reference voltage.

[adc\_emul\_const\_value\_set](group__adc__emul.md#ga564c588b71ec63aedb32f0c6221abd69)

int adc\_emul\_const\_value\_set(const struct device \*dev, unsigned int chan, uint32\_t value)

Set constant mV value input for emulated ADC chan.

[adc\_emul\_value\_func](group__adc__emul.md#ga8047a2a3700e085df84dc1dbc2ca155f)

int(\* adc\_emul\_value\_func)(const struct device \*dev, unsigned int chan, void \*data, uint32\_t \*result)

Type definition of the function which is used to obtain ADC mV input values.

**Definition** adc\_emul.h:59

[adc\_emul\_raw\_value\_func\_set](group__adc__emul.md#ga9d3f19bd7812722d982f0ceda0418afa)

int adc\_emul\_raw\_value\_func\_set(const struct device \*dev, unsigned int chan, adc\_emul\_value\_func func, void \*data)

Set function used to obtain voltage for raw input value of emulated ADC chan.

[adc\_emul\_value\_func\_set](group__adc__emul.md#gae5036c155341dd61d37558c311d3c554)

int adc\_emul\_value\_func\_set(const struct device \*dev, unsigned int chan, adc\_emul\_value\_func func, void \*data)

Set function used to obtain voltage for input of emulated ADC chan.

[adc\_reference](group__adc__interface.md#ga91b0f997d73739cf9f7349b7581e1f56)

adc\_reference

ADC references.

**Definition** adc.h:78

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [adc\_emul.h](adc__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
