---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/addresses_8h_source.html
original_path: doxygen/html/addresses_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

addresses.h

[Go to the documentation of this file.](addresses_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ADDRESSES\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ADDRESSES\_H\_

9

16

17#include <[stdint.h](stdint_8h.md)>

18

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/sys/util.h](sys_2util_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 27](group__i3c__addresses.md#gad516c48319d08db1886719645a682787)#define I3C\_BROADCAST\_ADDR 0x7E

28

[ 30](group__i3c__addresses.md#ga85a120abff94213b57ce4912f58d5ed8)#define I3C\_MAX\_ADDR 0x7F

31

32struct [i3c\_dev\_list](structi3c__dev__list.md);

33

[ 38](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0)enum [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) {

[ 40](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e) [I3C\_ADDR\_SLOT\_STATUS\_FREE](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e) = 0U,

41

[ 43](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45) [I3C\_ADDR\_SLOT\_STATUS\_RSVD](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45),

44

[ 46](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a) [I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a),

47

[ 49](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55) [I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55),

50

[ 52](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280) [I3C\_ADDR\_SLOT\_STATUS\_MASK](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280) = 0x03U,

53};

54

[ 58](structi3c__addr__slots.md)struct [i3c\_addr\_slots](structi3c__addr__slots.md) {

59 /\* 2 bits per slot \*/

[ 60](structi3c__addr__slots.md#a8117bc5c9b55bb074a845f8a4fe405fb) unsigned long [slots](structi3c__addr__slots.md#a8117bc5c9b55bb074a845f8a4fe405fb)[(([I3C\_MAX\_ADDR](group__i3c__addresses.md#ga85a120abff94213b57ce4912f58d5ed8) + 1) \* 2) / [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)];

61};

62

[ 74](group__i3c__addresses.md#gaf2be07d40d885f60997b5eb5edcf910f)int [i3c\_addr\_slots\_init](group__i3c__addresses.md#gaf2be07d40d885f60997b5eb5edcf910f)(const struct [device](structdevice.md) \*dev);

75

[ 83](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)void [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots,

84 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr,

85 enum [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) status);

86

[ 95](group__i3c__addresses.md#ga3dc021699fc489995b0bbe299753a33e)enum [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) [i3c\_addr\_slots\_status](group__i3c__addresses.md#ga3dc021699fc489995b0bbe299753a33e)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots,

96 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr);

97

[ 107](group__i3c__addresses.md#gadc2539a0b8793ec5b5ff34e57e68fb60)bool [i3c\_addr\_slots\_is\_free](group__i3c__addresses.md#gadc2539a0b8793ec5b5ff34e57e68fb60)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots,

108 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr);

109

[ 121](group__i3c__addresses.md#gad7eddb7aebf337a31f336ccf3f78cad1)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i3c\_addr\_slots\_next\_free\_find](group__i3c__addresses.md#gad7eddb7aebf337a31f336ccf3f78cad1)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr);

122

[ 129](group__i3c__addresses.md#gaf384836871625543aaa3f087e688f1b4)static inline void [i3c\_addr\_slots\_mark\_free](group__i3c__addresses.md#gaf384836871625543aaa3f087e688f1b4)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

130 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr)

131{

132 [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)(addr\_slots, addr,

133 [I3C\_ADDR\_SLOT\_STATUS\_FREE](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e));

134}

135

[ 142](group__i3c__addresses.md#gac976f542afb29d2360fc2c8d797dbac5)static inline void [i3c\_addr\_slots\_mark\_rsvd](group__i3c__addresses.md#gac976f542afb29d2360fc2c8d797dbac5)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

143 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr)

144{

145 [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)(addr\_slots, addr,

146 [I3C\_ADDR\_SLOT\_STATUS\_RSVD](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45));

147}

148

[ 155](group__i3c__addresses.md#gae10e6aba3335b78a2be728a5f495b436)static inline void [i3c\_addr\_slots\_mark\_i3c](group__i3c__addresses.md#gae10e6aba3335b78a2be728a5f495b436)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

156 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr)

157{

158 [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)(addr\_slots, addr,

159 [I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a));

160}

161

[ 168](group__i3c__addresses.md#gad5fc6b00171a4fdf76de20e6da3fbb32)static inline void [i3c\_addr\_slots\_mark\_i2c](group__i3c__addresses.md#gad5fc6b00171a4fdf76de20e6da3fbb32)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

169 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr)

170{

171 [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)(addr\_slots, addr,

172 [I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55));

173}

174

175#ifdef \_\_cplusplus

176}

177#endif

178

182

183#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ADDRESSES\_H\_ \*/

[device.h](device_8h.md)

[i3c\_addr\_slots\_status](group__i3c__addresses.md#ga3dc021699fc489995b0bbe299753a33e)

enum i3c\_addr\_slot\_status i3c\_addr\_slots\_status(struct i3c\_addr\_slots \*slots, uint8\_t dev\_addr)

Get the address status of a device.

[I3C\_MAX\_ADDR](group__i3c__addresses.md#ga85a120abff94213b57ce4912f58d5ed8)

#define I3C\_MAX\_ADDR

Maximum value of device addresses.

**Definition** addresses.h:30

[i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0)

i3c\_addr\_slot\_status

Enum to indicate whether an address is reserved, has I2C/I3C device attached, or no device attached.

**Definition** addresses.h:38

[i3c\_addr\_slots\_mark\_rsvd](group__i3c__addresses.md#gac976f542afb29d2360fc2c8d797dbac5)

static void i3c\_addr\_slots\_mark\_rsvd(struct i3c\_addr\_slots \*addr\_slots, uint8\_t addr)

Mark the address as reserved in device list.

**Definition** addresses.h:142

[i3c\_addr\_slots\_mark\_i2c](group__i3c__addresses.md#gad5fc6b00171a4fdf76de20e6da3fbb32)

static void i3c\_addr\_slots\_mark\_i2c(struct i3c\_addr\_slots \*addr\_slots, uint8\_t addr)

Mark the address as I2C device in device list.

**Definition** addresses.h:168

[i3c\_addr\_slots\_next\_free\_find](group__i3c__addresses.md#gad7eddb7aebf337a31f336ccf3f78cad1)

uint8\_t i3c\_addr\_slots\_next\_free\_find(struct i3c\_addr\_slots \*slots, uint8\_t start\_addr)

Find the next free address.

[i3c\_addr\_slots\_is\_free](group__i3c__addresses.md#gadc2539a0b8793ec5b5ff34e57e68fb60)

bool i3c\_addr\_slots\_is\_free(struct i3c\_addr\_slots \*slots, uint8\_t dev\_addr)

Check if the address is free.

[i3c\_addr\_slots\_mark\_i3c](group__i3c__addresses.md#gae10e6aba3335b78a2be728a5f495b436)

static void i3c\_addr\_slots\_mark\_i3c(struct i3c\_addr\_slots \*addr\_slots, uint8\_t addr)

Mark the address as I3C device in device list.

**Definition** addresses.h:155

[i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d)

void i3c\_addr\_slots\_set(struct i3c\_addr\_slots \*slots, uint8\_t dev\_addr, enum i3c\_addr\_slot\_status status)

Set the address status of a device.

[i3c\_addr\_slots\_init](group__i3c__addresses.md#gaf2be07d40d885f60997b5eb5edcf910f)

int i3c\_addr\_slots\_init(const struct device \*dev)

Initialize the I3C address slots struct.

[i3c\_addr\_slots\_mark\_free](group__i3c__addresses.md#gaf384836871625543aaa3f087e688f1b4)

static void i3c\_addr\_slots\_mark\_free(struct i3c\_addr\_slots \*addr\_slots, uint8\_t addr)

Mark the address as free (not used) in device list.

**Definition** addresses.h:129

[I3C\_ADDR\_SLOT\_STATUS\_RSVD](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45)

@ I3C\_ADDR\_SLOT\_STATUS\_RSVD

Address is reserved.

**Definition** addresses.h:43

[I3C\_ADDR\_SLOT\_STATUS\_MASK](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280)

@ I3C\_ADDR\_SLOT\_STATUS\_MASK

Bit masks used to filter status bits.

**Definition** addresses.h:52

[I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a)

@ I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV

Address is associated with an I3C device.

**Definition** addresses.h:46

[I3C\_ADDR\_SLOT\_STATUS\_FREE](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e)

@ I3C\_ADDR\_SLOT\_STATUS\_FREE

Address has not device attached.

**Definition** addresses.h:40

[I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55)

@ I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV

Address is associated with an I2C device.

**Definition** addresses.h:49

[BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)

#define BITS\_PER\_LONG

Number of bits in a long int.

**Definition** util.h:70

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[i3c\_addr\_slots](structi3c__addr__slots.md)

Structure to keep track of addresses on I3C bus.

**Definition** addresses.h:58

[i3c\_addr\_slots::slots](structi3c__addr__slots.md#a8117bc5c9b55bb074a845f8a4fe405fb)

unsigned long slots[((0x7F+1) \*2)/BITS\_PER\_LONG]

**Definition** addresses.h:60

[i3c\_dev\_list](structi3c__dev__list.md)

Structure for describing known devices for a controller.

**Definition** i3c.h:1163

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [addresses.h](addresses_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
