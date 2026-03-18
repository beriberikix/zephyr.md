---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/led__strip_8h_source.html
original_path: doxygen/html/led__strip_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_strip.h

[Go to the documentation of this file.](led__strip_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \* Copyright (c) 2024 Jamie McCrae

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_

18

25

26#include <[errno.h](errno_8h.md)>

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 40](structled__rgb.md)struct [led\_rgb](structled__rgb.md) {

41#ifdef CONFIG\_LED\_STRIP\_RGB\_SCRATCH

42 /\*

43 \* Pad/scratch space needed by some drivers. Users should

44 \* ignore.

45 \*/

46 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) scratch;

47#endif

[ 49](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33);

[ 51](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [g](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a);

[ 53](structled__rgb.md#abf071f86f224daa42b3b905071e550af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [b](structled__rgb.md#abf071f86f224daa42b3b905071e550af);

54};

55

[ 62](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151)typedef int (\*[led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151))(const struct [device](structdevice.md) \*dev,

63 struct [led\_rgb](structled__rgb.md) \*pixels,

64 size\_t num\_pixels);

65

[ 72](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501)typedef int (\*[led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501))(const struct [device](structdevice.md) \*dev,

73 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels,

74 size\_t num\_channels);

75

[ 82](group__led__strip__interface.md#ga3487e5d4a339898f88a225bb3678776b)typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*[led\_api\_length](group__led__strip__interface.md#ga3487e5d4a339898f88a225bb3678776b))(const struct [device](structdevice.md) \*dev);

83

[ 89](structled__strip__driver__api.md)\_\_subsystem struct [led\_strip\_driver\_api](structled__strip__driver__api.md) {

[ 90](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425) [led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151) [update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425);

[ 91](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228) [led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501) [update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228);

[ 92](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671) [led\_api\_length](group__led__strip__interface.md#ga3487e5d4a339898f88a225bb3678776b) [length](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671);

93};

94

[ 107](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)static inline int [led\_strip\_update\_rgb](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)(const struct [device](structdevice.md) \*dev,

108 struct [led\_rgb](structled__rgb.md) \*pixels,

109 size\_t num\_pixels)

110{

111 const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*api =

112 (const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

113

114 /\* Allow for out-of-tree drivers that do not have this function for 2 Zephyr releases

115 \* until making it mandatory, function added after Zephyr 3.6

116 \*/

117 if (api->[length](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671) != NULL) {

118 /\* Ensure supplied pixel size is valid for this device \*/

119 if (api->[length](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671)(dev) < num\_pixels) {

120 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

121 }

122 }

123

124 return api->[update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425)(dev, pixels, num\_pixels);

125}

126

[ 142](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)static inline int [led\_strip\_update\_channels](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)(const struct [device](structdevice.md) \*dev,

143 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels,

144 size\_t num\_channels)

145{

146 const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*api =

147 (const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

148

149 if (api->[update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228) == NULL) {

150 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

151 }

152

153 return api->[update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228)(dev, channels, num\_channels);

154}

155

[ 163](group__led__strip__interface.md#ga7f94eab0b357a81cccb5f0ea1575714a)static inline size\_t [led\_strip\_length](group__led__strip__interface.md#ga7f94eab0b357a81cccb5f0ea1575714a)(const struct [device](structdevice.md) \*dev)

164{

165 const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*api =

166 (const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

167

168 return api->[length](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671)(dev);

169}

170

171#ifdef \_\_cplusplus

172}

173#endif

174

178

179#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[led\_api\_length](group__led__strip__interface.md#ga3487e5d4a339898f88a225bb3678776b)

size\_t(\* led\_api\_length)(const struct device \*dev)

Callback API for getting length of an LED strip.

**Definition** led\_strip.h:82

[led\_strip\_update\_rgb](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)

static int led\_strip\_update\_rgb(const struct device \*dev, struct led\_rgb \*pixels, size\_t num\_pixels)

Mandatory function to update an LED strip with the given RGB array.

**Definition** led\_strip.h:107

[led\_strip\_length](group__led__strip__interface.md#ga7f94eab0b357a81cccb5f0ea1575714a)

static size\_t led\_strip\_length(const struct device \*dev)

Mandatory function to get chain length (in pixels) of an LED strip device.

**Definition** led\_strip.h:163

[led\_strip\_update\_channels](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)

static int led\_strip\_update\_channels(const struct device \*dev, uint8\_t \*channels, size\_t num\_channels)

Optional function to update an LED strip with the given channel array (each channel byte correspondin...

**Definition** led\_strip.h:142

[led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151)

int(\* led\_api\_update\_rgb)(const struct device \*dev, struct led\_rgb \*pixels, size\_t num\_pixels)

Callback API for updating an RGB LED strip.

**Definition** led\_strip.h:62

[led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501)

int(\* led\_api\_update\_channels)(const struct device \*dev, uint8\_t \*channels, size\_t num\_channels)

Callback API for updating channels without an RGB interpretation.

**Definition** led\_strip.h:72

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:72

[types.h](include_2zephyr_2types_8h.md)

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[led\_rgb](structled__rgb.md)

Color value for a single RGB LED.

**Definition** led\_strip.h:40

[led\_rgb::r](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33)

uint8\_t r

Red channel.

**Definition** led\_strip.h:49

[led\_rgb::g](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a)

uint8\_t g

Green channel.

**Definition** led\_strip.h:51

[led\_rgb::b](structled__rgb.md#abf071f86f224daa42b3b905071e550af)

uint8\_t b

Blue channel.

**Definition** led\_strip.h:53

[led\_strip\_driver\_api](structled__strip__driver__api.md)

LED strip driver API.

**Definition** led\_strip.h:89

[led\_strip\_driver\_api::length](structled__strip__driver__api.md#a083406f6a5b5ce034268315b7075d671)

led\_api\_length length

**Definition** led\_strip.h:92

[led\_strip\_driver\_api::update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228)

led\_api\_update\_channels update\_channels

**Definition** led\_strip.h:91

[led\_strip\_driver\_api::update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425)

led\_api\_update\_rgb update\_rgb

**Definition** led\_strip.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led\_strip.h](led__strip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
