---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ad559x_8h_source.html
original_path: doxygen/html/ad559x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ad559x.h

[Go to the documentation of this file.](ad559x_8h.md)

1/\*

2 \* Copyright (c) 2023 Grinn

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD559X\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD559X\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/device.h](device_8h.md)>

14

[ 15](ad559x_8h.md#ade40e7e134b45f33b22758fed430d786)#define AD559X\_REG\_SEQ\_ADC 0x02U

[ 16](ad559x_8h.md#a7a588e6ec9e98cd0530a55414fcc63de)#define AD559X\_REG\_ADC\_CONFIG 0x04U

[ 17](ad559x_8h.md#a513c0ed1982f51edb294ce3c07d92c8f)#define AD559X\_REG\_LDAC\_EN 0x05U

[ 18](ad559x_8h.md#a843ed93d660cfe363f4b682bd6a574a2)#define AD559X\_REG\_GPIO\_PULLDOWN 0x06U

[ 19](ad559x_8h.md#a9f90d05e96f8bf8170d2d461019f71b4)#define AD559X\_REG\_READ\_AND\_LDAC 0x07U

[ 20](ad559x_8h.md#a55717b95bfb5f4d6218dcaa22ce597f8)#define AD559X\_REG\_GPIO\_OUTPUT\_EN 0x08U

[ 21](ad559x_8h.md#a257a2ffecc969740e9a15231e05c74d4)#define AD559X\_REG\_GPIO\_SET 0x09U

[ 22](ad559x_8h.md#a1b1049f7ab7e768d286e3b599a72745d)#define AD559X\_REG\_GPIO\_INPUT\_EN 0x0AU

[ 23](ad559x_8h.md#a79a840afe34154908a59e64e7c8526de)#define AD559X\_REG\_PD\_REF\_CTRL 0x0BU

24

[ 25](ad559x_8h.md#a8db6c5c634f572cfca2bcb2e2f2cdb73)#define AD559X\_EN\_REF BIT(9)

26

[ 27](ad559x_8h.md#a24da8b1b01da9473bcf1b953727ead1e)#define AD559X\_PIN\_MAX 8U

28

34

[ 42](group__mdf__interface__ad559x.md#ga9280bf8cdaf3011a53073d189840e58f)bool [mfd\_ad559x\_has\_pointer\_byte\_map](group__mdf__interface__ad559x.md#ga9280bf8cdaf3011a53073d189840e58f)(const struct [device](structdevice.md) \*dev);

43

[ 54](group__mdf__interface__ad559x.md#ga60a3bef4d69b2e5dcde5f15ab10ee607)int [mfd\_ad559x\_read\_raw](group__mdf__interface__ad559x.md#ga60a3bef4d69b2e5dcde5f15ab10ee607)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val, size\_t len);

55

[ 66](group__mdf__interface__ad559x.md#ga0b9f70e3c85e17cd9f556f5cb98baf59)int [mfd\_ad559x\_write\_raw](group__mdf__interface__ad559x.md#ga0b9f70e3c85e17cd9f556f5cb98baf59)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val, size\_t len);

67

[ 79](group__mdf__interface__ad559x.md#ga896686606e114e223ee5afe40518356f)int [mfd\_ad559x\_read\_reg](group__mdf__interface__ad559x.md#ga896686606e114e223ee5afe40518356f)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val);

80

[ 91](group__mdf__interface__ad559x.md#gac91730fd6126260bc60da7c2637d7ccb)int [mfd\_ad559x\_write\_reg](group__mdf__interface__ad559x.md#gac91730fd6126260bc60da7c2637d7ccb)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

92

[ 103](group__mdf__interface__ad559x.md#gace77752024305f468412262f063e2c2a)int [mfd\_ad559x\_read\_adc\_chan](group__mdf__interface__ad559x.md#gace77752024305f468412262f063e2c2a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result);

104

[ 115](group__mdf__interface__ad559x.md#ga9a07f9de00ca00e19daa56ac1fc923bc)int [mfd\_ad559x\_write\_dac\_chan](group__mdf__interface__ad559x.md#ga9a07f9de00ca00e19daa56ac1fc923bc)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

116

[ 127](group__mdf__interface__ad559x.md#gacf88f29f46db4293e97f7fbb7a3edeb7)int [mfd\_ad559x\_gpio\_port\_get\_raw](group__mdf__interface__ad559x.md#gacf88f29f46db4293e97f7fbb7a3edeb7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value);

131

132#ifdef \_\_cplusplus

133}

134#endif

135

136#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD559X\_H\_ \*/

[device.h](device_8h.md)

[mfd\_ad559x\_write\_raw](group__mdf__interface__ad559x.md#ga0b9f70e3c85e17cd9f556f5cb98baf59)

int mfd\_ad559x\_write\_raw(const struct device \*dev, uint8\_t \*val, size\_t len)

Write raw data to chip.

[mfd\_ad559x\_read\_raw](group__mdf__interface__ad559x.md#ga60a3bef4d69b2e5dcde5f15ab10ee607)

int mfd\_ad559x\_read\_raw(const struct device \*dev, uint8\_t \*val, size\_t len)

Read raw data from the chip.

[mfd\_ad559x\_read\_reg](group__mdf__interface__ad559x.md#ga896686606e114e223ee5afe40518356f)

int mfd\_ad559x\_read\_reg(const struct device \*dev, uint8\_t reg, uint8\_t reg\_data, uint16\_t \*val)

Read data from provided register.

[mfd\_ad559x\_has\_pointer\_byte\_map](group__mdf__interface__ad559x.md#ga9280bf8cdaf3011a53073d189840e58f)

bool mfd\_ad559x\_has\_pointer\_byte\_map(const struct device \*dev)

Check if the chip has a pointer byte map.

[mfd\_ad559x\_write\_dac\_chan](group__mdf__interface__ad559x.md#ga9a07f9de00ca00e19daa56ac1fc923bc)

int mfd\_ad559x\_write\_dac\_chan(const struct device \*dev, uint8\_t channel, uint16\_t value)

Write ADC channel data to the chip.

[mfd\_ad559x\_write\_reg](group__mdf__interface__ad559x.md#gac91730fd6126260bc60da7c2637d7ccb)

int mfd\_ad559x\_write\_reg(const struct device \*dev, uint8\_t reg, uint16\_t val)

Write data to provided register.

[mfd\_ad559x\_read\_adc\_chan](group__mdf__interface__ad559x.md#gace77752024305f468412262f063e2c2a)

int mfd\_ad559x\_read\_adc\_chan(const struct device \*dev, uint8\_t channel, uint16\_t \*result)

Read ADC channel data from the chip.

[mfd\_ad559x\_gpio\_port\_get\_raw](group__mdf__interface__ad559x.md#gacf88f29f46db4293e97f7fbb7a3edeb7)

int mfd\_ad559x\_gpio\_port\_get\_raw(const struct device \*dev, uint8\_t gpio, uint16\_t \*value)

Read GPIO port from the chip.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [ad559x.h](ad559x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
