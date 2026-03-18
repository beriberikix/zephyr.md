---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/led__strip_8h_source.html
original_path: doxygen/html/led__strip_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_strip.h

[Go to the documentation of this file.](led__strip_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_

17

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 38](structled__rgb.md)struct [led\_rgb](structled__rgb.md) {

39#ifdef CONFIG\_LED\_STRIP\_RGB\_SCRATCH

40 /\*

41 \* Pad/scratch space needed by some drivers. Users should

42 \* ignore.

43 \*/

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) scratch;

45#endif

[ 47](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33);

[ 49](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [g](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a);

[ 51](structled__rgb.md#abf071f86f224daa42b3b905071e550af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [b](structled__rgb.md#abf071f86f224daa42b3b905071e550af);

52};

53

[ 60](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151)typedef int (\*[led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151))(const struct [device](structdevice.md) \*dev,

61 struct [led\_rgb](structled__rgb.md) \*pixels,

62 size\_t num\_pixels);

63

[ 70](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501)typedef int (\*[led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501))(const struct [device](structdevice.md) \*dev,

71 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels,

72 size\_t num\_channels);

73

[ 79](structled__strip__driver__api.md)struct [led\_strip\_driver\_api](structled__strip__driver__api.md) {

[ 80](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425) [led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151) [update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425);

[ 81](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228) [led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501) [update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228);

82};

83

[ 99](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)static inline int [led\_strip\_update\_rgb](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)(const struct [device](structdevice.md) \*dev,

100 struct [led\_rgb](structled__rgb.md) \*pixels,

101 size\_t num\_pixels) {

102 const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*api =

103 (const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

104

105 return api->[update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425)(dev, pixels, num\_pixels);

106}

107

[ 125](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)static inline int [led\_strip\_update\_channels](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)(const struct [device](structdevice.md) \*dev,

126 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels,

127 size\_t num\_channels) {

128 const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*api =

129 (const struct [led\_strip\_driver\_api](structled__strip__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

130

131 return api->[update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228)(dev, channels, num\_channels);

132}

133

134#ifdef \_\_cplusplus

135}

136#endif

137

141

142#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_H\_ \*/

[device.h](device_8h.md)

[led\_strip\_update\_rgb](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67)

static int led\_strip\_update\_rgb(const struct device \*dev, struct led\_rgb \*pixels, size\_t num\_pixels)

Update an LED strip made of RGB pixels.

**Definition** led\_strip.h:99

[led\_strip\_update\_channels](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34)

static int led\_strip\_update\_channels(const struct device \*dev, uint8\_t \*channels, size\_t num\_channels)

Update an LED strip on a per-channel basis.

**Definition** led\_strip.h:125

[led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151)

int(\* led\_api\_update\_rgb)(const struct device \*dev, struct led\_rgb \*pixels, size\_t num\_pixels)

Callback API for updating an RGB LED strip.

**Definition** led\_strip.h:60

[led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501)

int(\* led\_api\_update\_channels)(const struct device \*dev, uint8\_t \*channels, size\_t num\_channels)

Callback API for updating channels without an RGB interpretation.

**Definition** led\_strip.h:70

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[led\_rgb](structled__rgb.md)

Color value for a single RGB LED.

**Definition** led\_strip.h:38

[led\_rgb::r](structled__rgb.md#a2b3072dbddc32f7a93b87b9ed01e1a33)

uint8\_t r

Red channel.

**Definition** led\_strip.h:47

[led\_rgb::g](structled__rgb.md#ab24a1948906fcb4c5978a84ac46b779a)

uint8\_t g

Green channel.

**Definition** led\_strip.h:49

[led\_rgb::b](structled__rgb.md#abf071f86f224daa42b3b905071e550af)

uint8\_t b

Blue channel.

**Definition** led\_strip.h:51

[led\_strip\_driver\_api](structled__strip__driver__api.md)

LED strip driver API.

**Definition** led\_strip.h:79

[led\_strip\_driver\_api::update\_channels](structled__strip__driver__api.md#ad5969b78c4b77d570669abd5143ec228)

led\_api\_update\_channels update\_channels

**Definition** led\_strip.h:81

[led\_strip\_driver\_api::update\_rgb](structled__strip__driver__api.md#af0f7a73d61589355b520f76073013425)

led\_api\_update\_rgb update\_rgb

**Definition** led\_strip.h:80

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led\_strip.h](led__strip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
