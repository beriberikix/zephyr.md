---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/swdp_8h_source.html
original_path: doxygen/html/swdp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

swdp.h

[Go to the documentation of this file.](swdp_8h.md)

1/\*

2 \* Copyright (c) 2019 PHYTEC Messtechnik GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SWDP\_H\_

13#define ZEPHYR\_INCLUDE\_SWDP\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21/\* SWDP packet request bits \*/

[ 22](swdp_8h.md#a8a41667b3516d49ad5785669a659fa0b)#define SWDP\_REQUEST\_APnDP BIT(0)

[ 23](swdp_8h.md#adc8522fcb5dd2d68b07d82b60d2324e3)#define SWDP\_REQUEST\_RnW BIT(1)

[ 24](swdp_8h.md#a2a48349320bd17c6495e96f53738645c)#define SWDP\_REQUEST\_A2 BIT(2)

[ 25](swdp_8h.md#a30ec6eccc9dc5f4254eceb887b33caf7)#define SWDP\_REQUEST\_A3 BIT(3)

26

27/\* SWDP acknowledge response bits \*/

[ 28](swdp_8h.md#accc95b6569bfdcb9969b62e49e4a7869)#define SWDP\_ACK\_OK BIT(0)

[ 29](swdp_8h.md#aaa8df6e1403dd7ca964acdfd3eba5c42)#define SWDP\_ACK\_WAIT BIT(1)

[ 30](swdp_8h.md#a6f67ce6246bda2a4f11fbef88de8050e)#define SWDP\_ACK\_FAULT BIT(2)

31

32/\* SWDP transfer or parity error \*/

[ 33](swdp_8h.md#a0c5587d14f0b68fa639558f768f24e90)#define SWDP\_TRANSFER\_ERROR BIT(3)

34

35/\* SWDP Interface pins \*/

[ 36](swdp_8h.md#a04d9dbfa1c6303adfbf22ea14c589a5d)#define SWDP\_SWCLK\_PIN 0U

[ 37](swdp_8h.md#af0d50f9d503900ad9a7e3dd0d40aae4e)#define SWDP\_SWDIO\_PIN 1U

[ 38](swdp_8h.md#a2cad01a3a938093f7b7ec2ddc0fcdc2d)#define SWDP\_nRESET\_PIN 7U

39

40/\*

41 \* Serial Wire Interface (SWDP) driver API.

42 \* This is the mandatory API any Serial Wire driver needs to expose.

43 \*/

[ 44](structswdp__api.md)struct [swdp\_api](structswdp__api.md) {

[ 53](structswdp__api.md#a4a4e268bc2e80b0fa3af76c8fb6d70c7) int (\*[swdp\_output\_sequence](structswdp__api.md#a4a4e268bc2e80b0fa3af76c8fb6d70c7))(const struct [device](structdevice.md) \*dev,

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count,

55 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

56

[ 65](structswdp__api.md#a0480ec7f5479382457ac2e9c264e46f4) int (\*[swdp\_input\_sequence](structswdp__api.md#a0480ec7f5479382457ac2e9c264e46f4))(const struct [device](structdevice.md) \*dev,

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count,

67 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

68

[ 79](structswdp__api.md#a3b2a89ee837aae3731ba0d2ba8c1c323) int (\*[swdp\_transfer](structswdp__api.md#a3b2a89ee837aae3731ba0d2ba8c1c323))(const struct [device](structdevice.md) \*dev,

80 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request,

81 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data,

82 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idle\_cycles,

83 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response);

84

[ 94](structswdp__api.md#af83ae99fb199d5506256c13aec92f1a7) int (\*[swdp\_set\_pins](structswdp__api.md#af83ae99fb199d5506256c13aec92f1a7))(const struct [device](structdevice.md) \*dev,

95 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pins, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

96

[ 105](structswdp__api.md#ac0e08f227a18d087fa98894caa277282) int (\*[swdp\_get\_pins](structswdp__api.md#ac0e08f227a18d087fa98894caa277282))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

106

[ 114](structswdp__api.md#aba201f47bb6037334b3da19d17ea7349) int (\*[swdp\_set\_clock](structswdp__api.md#aba201f47bb6037334b3da19d17ea7349))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clock);

115

[ 124](structswdp__api.md#a62b5b2285bdec6d9e6069f1671ad1bc3) int (\*[swdp\_configure](structswdp__api.md#a62b5b2285bdec6d9e6069f1671ad1bc3))(const struct [device](structdevice.md) \*dev,

125 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) turnaround,

126 bool data\_phase);

127

[ 136](structswdp__api.md#a642cd297ace3437669be092ca4061911) int (\*[swdp\_port\_on](structswdp__api.md#a642cd297ace3437669be092ca4061911))(const struct [device](structdevice.md) \*dev);

137

[ 144](structswdp__api.md#aa7e408b542b1bd9134b86f2a257cf004) int (\*[swdp\_port\_off](structswdp__api.md#aa7e408b542b1bd9134b86f2a257cf004))(const struct [device](structdevice.md) \*dev);

145};

146

147#ifdef \_\_cplusplus

148}

149#endif

150

151#endif /\* ZEPHYR\_INCLUDE\_SWDP\_H\_ \*/

[device.h](device_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[swdp\_api](structswdp__api.md)

**Definition** swdp.h:44

[swdp\_api::swdp\_input\_sequence](structswdp__api.md#a0480ec7f5479382457ac2e9c264e46f4)

int(\* swdp\_input\_sequence)(const struct device \*dev, uint32\_t count, uint8\_t \*data)

Read count bits from SWDIO into data LSB first.

**Definition** swdp.h:65

[swdp\_api::swdp\_transfer](structswdp__api.md#a3b2a89ee837aae3731ba0d2ba8c1c323)

int(\* swdp\_transfer)(const struct device \*dev, uint8\_t request, uint32\_t \*data, uint8\_t idle\_cycles, uint8\_t \*response)

Perform SWDP transfer and store response.

**Definition** swdp.h:79

[swdp\_api::swdp\_output\_sequence](structswdp__api.md#a4a4e268bc2e80b0fa3af76c8fb6d70c7)

int(\* swdp\_output\_sequence)(const struct device \*dev, uint32\_t count, const uint8\_t \*data)

Write count bits to SWDIO from data LSB first.

**Definition** swdp.h:53

[swdp\_api::swdp\_configure](structswdp__api.md#a62b5b2285bdec6d9e6069f1671ad1bc3)

int(\* swdp\_configure)(const struct device \*dev, uint8\_t turnaround, bool data\_phase)

Configure SWDP interface.

**Definition** swdp.h:124

[swdp\_api::swdp\_port\_on](structswdp__api.md#a642cd297ace3437669be092ca4061911)

int(\* swdp\_port\_on)(const struct device \*dev)

Enable interface, set pins to default state.

**Definition** swdp.h:136

[swdp\_api::swdp\_port\_off](structswdp__api.md#aa7e408b542b1bd9134b86f2a257cf004)

int(\* swdp\_port\_off)(const struct device \*dev)

Disable interface, set pins to High-Z mode.

**Definition** swdp.h:144

[swdp\_api::swdp\_set\_clock](structswdp__api.md#aba201f47bb6037334b3da19d17ea7349)

int(\* swdp\_set\_clock)(const struct device \*dev, uint32\_t clock)

Set SWDP clock frequency.

**Definition** swdp.h:114

[swdp\_api::swdp\_get\_pins](structswdp__api.md#ac0e08f227a18d087fa98894caa277282)

int(\* swdp\_get\_pins)(const struct device \*dev, uint8\_t \*state)

Get SWCLK, SWDPIO, and nRESET pins state.

**Definition** swdp.h:105

[swdp\_api::swdp\_set\_pins](structswdp__api.md#af83ae99fb199d5506256c13aec92f1a7)

int(\* swdp\_set\_pins)(const struct device \*dev, uint8\_t pins, uint8\_t value)

Set SWCLK, SWDPIO, and nRESET pins state.

**Definition** swdp.h:94

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [swdp.h](swdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
