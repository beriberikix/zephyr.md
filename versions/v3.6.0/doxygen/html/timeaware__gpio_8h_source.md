---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/timeaware__gpio_8h_source.html
original_path: doxygen/html/timeaware__gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

20

21#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

22#include <[zephyr/sys/slist.h](slist_8h.md)>

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <stddef.h>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/internal/syscall\_handler.h](syscall__handler_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 36](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c)enum [tgpio\_pin\_polarity](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c) {

[ 37](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) [TGPIO\_RISING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) = 0,

[ 38](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98) [TGPIO\_FALLING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98),

[ 39](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9) [TGPIO\_TOGGLE\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9),

40};

41

49

50\_\_subsystem struct tgpio\_driver\_api {

51 int (\*pin\_disable)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin);

52 int (\*get\_time)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time);

53 int (\*cyc\_per\_sec)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles);

54 int (\*set\_perout)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time,

55 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval, bool periodic\_enable);

56 int (\*config\_ext\_ts)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity);

57 int (\*read\_ts\_ec)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp,

58 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count);

59};

60

64

[ 74](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)\_\_syscall int [tgpio\_port\_get\_time](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time);

75

76static inline int z\_impl\_tgpio\_port\_get\_time(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time)

77{

78 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

79

80 return api->get\_time(dev, current\_time);

81}

82

[ 91](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da)\_\_syscall int [tgpio\_port\_get\_cycles\_per\_second](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles);

92

93static inline int z\_impl\_tgpio\_port\_get\_cycles\_per\_second(const struct [device](structdevice.md) \*dev,

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles)

95{

96 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

97

98 return api->cyc\_per\_sec(dev, cycles);

99}

100

[ 109](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879)\_\_syscall int [tgpio\_pin\_disable](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin);

110

111static inline int z\_impl\_tgpio\_pin\_disable(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin)

112{

113 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

114

115 return api->pin\_disable(dev, pin);

116}

117

[ 127](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e)\_\_syscall int [tgpio\_pin\_config\_ext\_timestamp](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

128 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity);

129

130static inline int z\_impl\_tgpio\_pin\_config\_ext\_timestamp(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

131 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity)

132{

133 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

134

135 return api->config\_ext\_ts(dev, pin, event\_polarity);

136}

137

[ 149](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)\_\_syscall int [tgpio\_pin\_periodic\_output](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

150 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval,

151 bool periodic\_enable);

152

153static inline int z\_impl\_tgpio\_pin\_periodic\_output(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

154 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval,

155 bool periodic\_enable)

156{

157 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

158

159 return api->set\_perout(dev, pin, start\_time, repeat\_interval, periodic\_enable);

160}

161

[ 172](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)\_\_syscall int [tgpio\_pin\_read\_ts\_ec](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp,

173 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count);

174

175static inline int z\_impl\_tgpio\_pin\_read\_ts\_ec(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin,

176 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count)

177{

178 const struct tgpio\_driver\_api \*api = (const struct tgpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

179

180 return api->read\_ts\_ec(dev, pin, timestamp, event\_count);

181}

182

186

187#ifdef \_\_cplusplus

188}

189#endif

190

191#include <syscalls/timeaware\_gpio.h>

192

193#endif /\* ZEPHYR\_DRIVERS\_MISC\_TIMEAWARE\_GPIO\_TIMEAWARE\_GPIO \*/

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

**Definition** timeaware\_gpio.h:36

[tgpio\_pin\_periodic\_output](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301)

int tgpio\_pin\_periodic\_output(const struct device \*dev, uint32\_t pin, uint64\_t start\_time, uint64\_t repeat\_interval, bool periodic\_enable)

Enable periodic pulse generation on a pin.

[TGPIO\_TOGGLE\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9)

@ TGPIO\_TOGGLE\_EDGE

**Definition** timeaware\_gpio.h:39

[TGPIO\_RISING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df)

@ TGPIO\_RISING\_EDGE

**Definition** timeaware\_gpio.h:37

[TGPIO\_FALLING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98)

@ TGPIO\_FALLING\_EDGE

**Definition** timeaware\_gpio.h:38

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[syscall\_handler.h](syscall__handler_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [timeaware\_gpio](dir_6bb0264ea02bd365c18848a4d9878330.md)
- [timeaware\_gpio.h](timeaware__gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
