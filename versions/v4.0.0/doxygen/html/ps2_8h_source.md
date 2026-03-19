---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ps2_8h_source.html
original_path: doxygen/html/ps2_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ps2.h

[Go to the documentation of this file.](ps2_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PS2\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_PS2\_H\_

16

17#include <[errno.h](errno_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <stddef.h>

20#include <[zephyr/device.h](device_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

32

[ 39](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f)typedef void (\*[ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

40

48typedef int (\*ps2\_config\_t)(const struct [device](structdevice.md) \*dev,

49 [ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f) callback\_isr);

50typedef int (\*ps2\_read\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

51typedef int (\*ps2\_write\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

52typedef int (\*ps2\_disable\_callback\_t)(const struct [device](structdevice.md) \*dev);

53typedef int (\*ps2\_enable\_callback\_t)(const struct [device](structdevice.md) \*dev);

54

55\_\_subsystem struct ps2\_driver\_api {

56 ps2\_config\_t config;

57 ps2\_read\_t read;

58 ps2\_write\_t write;

59 ps2\_disable\_callback\_t disable\_callback;

60 ps2\_enable\_callback\_t enable\_callback;

61};

65

[ 76](group__ps2__interface.md#ga8d6da9b966432defb0cd482003c11f15)\_\_syscall int [ps2\_config](group__ps2__interface.md#ga8d6da9b966432defb0cd482003c11f15)(const struct [device](structdevice.md) \*dev,

77 [ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f) callback\_isr);

78

79static inline int z\_impl\_ps2\_config(const struct [device](structdevice.md) \*dev,

80 [ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f) callback\_isr)

81{

82 const struct ps2\_driver\_api \*api =

83 (struct ps2\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

84

85 return api->config(dev, callback\_isr);

86}

87

[ 97](group__ps2__interface.md#gae291cb991ae9525552fdb52c2fa4ac5e)\_\_syscall int [ps2\_write](group__ps2__interface.md#gae291cb991ae9525552fdb52c2fa4ac5e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

98

99static inline int z\_impl\_ps2\_write(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

100{

101 const struct ps2\_driver\_api \*api =

102 (const struct ps2\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

103

104 return api->write(dev, value);

105}

106

[ 115](group__ps2__interface.md#gab91b1efe1f07d409607922f4eb87b221)\_\_syscall int [ps2\_read](group__ps2__interface.md#gab91b1efe1f07d409607922f4eb87b221)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

116

117static inline int z\_impl\_ps2\_read(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

118{

119 const struct ps2\_driver\_api \*api =

120 (const struct ps2\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

121

122 return api->read(dev, value);

123}

124

[ 132](group__ps2__interface.md#ga9568487018f4ef972eb463ea2098e254)\_\_syscall int [ps2\_enable\_callback](group__ps2__interface.md#ga9568487018f4ef972eb463ea2098e254)(const struct [device](structdevice.md) \*dev);

133

134static inline int z\_impl\_ps2\_enable\_callback(const struct [device](structdevice.md) \*dev)

135{

136 const struct ps2\_driver\_api \*api =

137 (const struct ps2\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

138

139 if (api->enable\_callback == NULL) {

140 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

141 }

142

143 return api->enable\_callback(dev);

144}

145

[ 153](group__ps2__interface.md#gade1a470c3583e465d6a8f24a28611397)\_\_syscall int [ps2\_disable\_callback](group__ps2__interface.md#gade1a470c3583e465d6a8f24a28611397)(const struct [device](structdevice.md) \*dev);

154

155static inline int z\_impl\_ps2\_disable\_callback(const struct [device](structdevice.md) \*dev)

156{

157 const struct ps2\_driver\_api \*api =

158 (const struct ps2\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

159

160 if (api->disable\_callback == NULL) {

161 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

162 }

163

164 return api->disable\_callback(dev);

165}

166

167#ifdef \_\_cplusplus

168}

169#endif

170

174

175#include <zephyr/syscalls/ps2.h>

176

177#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PS2\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[ps2\_config](group__ps2__interface.md#ga8d6da9b966432defb0cd482003c11f15)

int ps2\_config(const struct device \*dev, ps2\_callback\_t callback\_isr)

Configure a ps2 instance.

[ps2\_enable\_callback](group__ps2__interface.md#ga9568487018f4ef972eb463ea2098e254)

int ps2\_enable\_callback(const struct device \*dev)

Enables callback.

[ps2\_read](group__ps2__interface.md#gab91b1efe1f07d409607922f4eb87b221)

int ps2\_read(const struct device \*dev, uint8\_t \*value)

Read slave-to-host values from PS/2 device.

[ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f)

void(\* ps2\_callback\_t)(const struct device \*dev, uint8\_t data)

PS/2 callback called when user types or click a mouse.

**Definition** ps2.h:39

[ps2\_disable\_callback](group__ps2__interface.md#gade1a470c3583e465d6a8f24a28611397)

int ps2\_disable\_callback(const struct device \*dev)

Disables callback.

[ps2\_write](group__ps2__interface.md#gae291cb991ae9525552fdb52c2fa4ac5e)

int ps2\_write(const struct device \*dev, uint8\_t value)

Write to PS/2 device.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ps2.h](ps2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
