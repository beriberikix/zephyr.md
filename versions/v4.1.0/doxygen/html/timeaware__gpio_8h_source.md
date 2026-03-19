---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/timeaware__gpio_8h_source.html
original_path: doxygen/html/timeaware__gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeaware\_gpio.h

[Go to the documentation of this file.](timeaware__gpio_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_DRIVERS\_MISC\_TIMEAWARE\_GPIO\_TIMEAWARE\_GPIO

12#define ZEPHYR\_DRIVERS\_MISC\_TIMEAWARE\_GPIO\_TIMEAWARE\_GPIO

13

22

23#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

24#include <[zephyr/sys/slist.h](slist_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <stddef.h>

28#include <[zephyr/device.h](device_8h.md)>

29#include <[zephyr/internal/syscall\_handler.h](syscall__handler_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 38](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c)enum [tgpio\_pin\_polarity](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c) {

[ 39](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) [TGPIO\_RISING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) = 0,

[ 40](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98) [TGPIO\_FALLING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98),

[ 41](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9) [TGPIO\_TOGGLE\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9),

42};

43

51

52\_\_subsystem struct tgpio\_driver\_api {

53 int (\*pin\_disable)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin);

54 int (\*get\_time)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time);

55 int (\*cyc\_per\_sec)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles);

56 int (\*set\_perout)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time,

57 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval, bool periodic\_enable);

58 int (\*config\_ext\_ts)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity);

59 int (\*read\_ts\_ec)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp,

60 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count);

61};

62

66

[ 76](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)\_\_syscall int [tgpio\_port\_get\_time](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time);

77

78static inline int z\_impl\_tgpio\_port\_get\_time(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time)

79{

80 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

81

82 return api->get\_time(dev, current\_time);

83}

84

[ 93](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da)\_\_syscall int [tgpio\_port\_get\_cycles\_per\_second](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles);

94

95static inline int z\_impl\_tgpio\_port\_get\_cycles\_per\_second(const struct [device](structdevice.md) \*dev,

96 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles)

97{

98 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

99

100 return api->cyc\_per\_sec(dev, cycles);

101}

102

[ 111](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879)\_\_syscall int [tgpio\_pin\_disable](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin);

112

113static inline int z\_impl\_tgpio\_pin\_disable(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin)

114{

115 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

116

117 return api->pin\_disable(dev, pin);

118}

119

[ 129](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e)\_\_syscall int [tgpio\_pin\_config\_ext\_timestamp](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

130 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity);

131

132static inline int z\_impl\_tgpio\_pin\_config\_ext\_timestamp(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

133 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity)

134{

135 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

136

137 return api->config\_ext\_ts(dev, pin, event\_polarity);

138}

139

[ 151](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)\_\_syscall int [tgpio\_pin\_periodic\_output](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

152 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval,

153 bool periodic\_enable);

154

155static inline int z\_impl\_tgpio\_pin\_periodic\_output(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

156 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval,

157 bool periodic\_enable)

158{

159 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

160

161 return api->set\_perout(dev, pin, start\_time, repeat\_interval, periodic\_enable);

162}

163

[ 174](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)\_\_syscall int [tgpio\_pin\_read\_ts\_ec](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp,

175 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count);

176

177static inline int z\_impl\_tgpio\_pin\_read\_ts\_ec(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

178 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count)

179{

180 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

181

182 return api->read\_ts\_ec(dev, pin, timestamp, event\_count);

183}

184

188

189#ifdef \_\_cplusplus

190}

191#endif

192

193#include <zephyr/syscalls/timeaware\_gpio.h>

194

195#endif /\* ZEPHYR\_DRIVERS\_MISC\_TIMEAWARE\_GPIO\_TIMEAWARE\_GPIO \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[tgpio\_pin\_read\_ts\_ec](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)

int tgpio\_pin\_read\_ts\_ec(const struct device \*dev, uint32\_t pin, uint64\_t \*timestamp, uint64\_t \*event\_count)

Read timestamp and event counter from TGPIO.

[tgpio\_pin\_config\_ext\_timestamp](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e)

int tgpio\_pin\_config\_ext\_timestamp(const struct device \*dev, uint32\_t pin, uint32\_t event\_polarity)

Enable/Continue operation on pin.

[tgpio\_pin\_disable](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879)

int tgpio\_pin\_disable(const struct device \*dev, uint32\_t pin)

Disable operation on pin.

[tgpio\_port\_get\_time](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)

int tgpio\_port\_get\_time(const struct device \*dev, uint64\_t \*current\_time)

Get time from ART timer.

[tgpio\_port\_get\_cycles\_per\_second](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da)

int tgpio\_port\_get\_cycles\_per\_second(const struct device \*dev, uint32\_t \*cycles)

Get current running rate.

[tgpio\_pin\_polarity](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c)

tgpio\_pin\_polarity

Event polarity.

**Definition** timeaware\_gpio.h:38

[tgpio\_pin\_periodic\_output](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)

int tgpio\_pin\_periodic\_output(const struct device \*dev, uint32\_t pin, uint64\_t start\_time, uint64\_t repeat\_interval, bool periodic\_enable)

Enable periodic pulse generation on a pin.

[TGPIO\_TOGGLE\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9)

@ TGPIO\_TOGGLE\_EDGE

**Definition** timeaware\_gpio.h:41

[TGPIO\_RISING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df)

@ TGPIO\_RISING\_EDGE

**Definition** timeaware\_gpio.h:39

[TGPIO\_FALLING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98)

@ TGPIO\_FALLING\_EDGE

**Definition** timeaware\_gpio.h:40

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[syscall\_handler.h](syscall__handler_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [timeaware\_gpio](dir_6bb0264ea02bd365c18848a4d9878330.md)
- [timeaware\_gpio.h](timeaware__gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
