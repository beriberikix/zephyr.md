---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dac_8h_source.html
original_path: doxygen/html/dac_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dac.h

[Go to the documentation of this file.](dac_8h.md)

1/\*

2 \* Copyright (c) 2020 Libre Solar Technologies GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 31](structdac__channel__cfg.md)struct [dac\_channel\_cfg](structdac__channel__cfg.md) {

[ 33](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_id](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3);

[ 35](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resolution](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3);

[ 40](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96) bool [buffered](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96);

41};

42

48

49/\*

50 \* Type definition of DAC API function for configuring a channel.

51 \* See dac\_channel\_setup() for argument descriptions.

52 \*/

53typedef int (\*dac\_api\_channel\_setup)(const struct [device](structdevice.md) \*dev,

54 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg);

55

56/\*

57 \* Type definition of DAC API function for setting a write request.

58 \* See dac\_write\_value() for argument descriptions.

59 \*/

60typedef int (\*dac\_api\_write\_value)(const struct [device](structdevice.md) \*dev,

61 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

62

63/\*

64 \* DAC driver API

65 \*

66 \* This is the mandatory API any DAC driver needs to expose.

67 \*/

68\_\_subsystem struct dac\_driver\_api {

69 dac\_api\_channel\_setup channel\_setup;

70 dac\_api\_write\_value write\_value;

71};

72

76

[ 90](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56)\_\_syscall int [dac\_channel\_setup](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56)(const struct [device](structdevice.md) \*dev,

91 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg);

92

93static inline int z\_impl\_dac\_channel\_setup(const struct [device](structdevice.md) \*dev,

94 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg)

95{

96 const struct dac\_driver\_api \*api =

97 (const struct dac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

98

99 return api->channel\_setup(dev, channel\_cfg);

100}

101

[ 112](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e)\_\_syscall int [dac\_write\_value](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

113 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

114

115static inline int z\_impl\_dac\_write\_value(const struct [device](structdevice.md) \*dev,

116 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

117{

118 const struct dac\_driver\_api \*api =

119 (const struct dac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

120

121 return api->write\_value(dev, channel, value);

122}

123

127

128#ifdef \_\_cplusplus

129}

130#endif

131

132#include <syscalls/dac.h>

133

134#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_H\_ \*/

[device.h](device_8h.md)

[dac\_write\_value](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e)

int dac\_write\_value(const struct device \*dev, uint8\_t channel, uint32\_t value)

Write a single value to a DAC channel.

[dac\_channel\_setup](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56)

int dac\_channel\_setup(const struct device \*dev, const struct dac\_channel\_cfg \*channel\_cfg)

Configure a DAC channel.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[dac\_channel\_cfg](structdac__channel__cfg.md)

Structure for specifying the configuration of a DAC channel.

**Definition** dac.h:31

[dac\_channel\_cfg::buffered](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96)

bool buffered

Enable output buffer for this channel.

**Definition** dac.h:40

[dac\_channel\_cfg::channel\_id](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3)

uint8\_t channel\_id

Channel identifier of the DAC that should be configured.

**Definition** dac.h:33

[dac\_channel\_cfg::resolution](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3)

uint8\_t resolution

Desired resolution of the DAC (depends on device capabilities).

**Definition** dac.h:35

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dac.h](dac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
