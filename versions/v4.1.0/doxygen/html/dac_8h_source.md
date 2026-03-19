---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dac_8h_source.html
original_path: doxygen/html/dac_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

29

[ 34](group__dac__interface.md#gabeb2cf325aec36624a013ee91a377b35)#define DAC\_CHANNEL\_BROADCAST 0xFF

35

[ 39](structdac__channel__cfg.md)struct [dac\_channel\_cfg](structdac__channel__cfg.md) {

[ 41](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_id](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3);

[ 43](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resolution](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3);

[ 48](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96) bool [buffered](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96): 1;

53 bool internal: 1;

54};

55

61

62/\*

63 \* Type definition of DAC API function for configuring a channel.

64 \* See dac\_channel\_setup() for argument descriptions.

65 \*/

66typedef int (\*dac\_api\_channel\_setup)(const struct [device](structdevice.md) \*dev,

67 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg);

68

69/\*

70 \* Type definition of DAC API function for setting a write request.

71 \* See dac\_write\_value() for argument descriptions.

72 \*/

73typedef int (\*dac\_api\_write\_value)(const struct [device](structdevice.md) \*dev,

74 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

75

76/\*

77 \* DAC driver API

78 \*

79 \* This is the mandatory API any DAC driver needs to expose.

80 \*/

81\_\_subsystem struct dac\_driver\_api {

82 dac\_api\_channel\_setup channel\_setup;

83 dac\_api\_write\_value write\_value;

84};

85

89

[ 103](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56)\_\_syscall int [dac\_channel\_setup](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56)(const struct [device](structdevice.md) \*dev,

104 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg);

105

106static inline int z\_impl\_dac\_channel\_setup(const struct [device](structdevice.md) \*dev,

107 const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg)

108{

109 const struct dac\_driver\_api \*api =

110 (const struct dac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

111

112 return api->channel\_setup(dev, channel\_cfg);

113}

114

[ 125](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e)\_\_syscall int [dac\_write\_value](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

126 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

127

128static inline int z\_impl\_dac\_write\_value(const struct [device](structdevice.md) \*dev,

129 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

130{

131 const struct dac\_driver\_api \*api =

132 (const struct dac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

133

134 return api->write\_value(dev, channel, value);

135}

136

140

141#ifdef \_\_cplusplus

142}

143#endif

144

145#include <zephyr/syscalls/dac.h>

146

147#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_H\_ \*/

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

**Definition** dac.h:39

[dac\_channel\_cfg::buffered](structdac__channel__cfg.md#a31df5ad55f40cb89819fac3acd6b4d96)

bool buffered

Enable output buffer for this channel.

**Definition** dac.h:48

[dac\_channel\_cfg::channel\_id](structdac__channel__cfg.md#a41a1708aa81b2a808556ec976ce303f3)

uint8\_t channel\_id

Channel identifier of the DAC that should be configured.

**Definition** dac.h:41

[dac\_channel\_cfg::resolution](structdac__channel__cfg.md#a4ba4f6dde3e4525e0a0e71fea5aeaef3)

uint8\_t resolution

Desired resolution of the DAC (depends on device capabilities).

**Definition** dac.h:43

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dac.h](dac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
