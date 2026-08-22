---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dsa__core_8h_source.html
original_path: doxygen/html/dsa__core_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_core.h

[Go to the documentation of this file.](dsa__core_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

9

10#ifndef ZEPHYR\_INCLUDE\_NET\_DSA\_CORE\_H\_

11#define ZEPHYR\_INCLUDE\_NET\_DSA\_CORE\_H\_

12

13#include <[errno.h](errno_8h.md)>

14#include <[zephyr/device.h](device_8h.md)>

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16#include <[zephyr/net/net\_if.h](net__if_8h.md)>

17#include <[zephyr/net/phy.h](phy_8h.md)>

18

27

29

30#if defined(CONFIG\_DSA\_PORT\_MAX\_COUNT)

31#define DSA\_PORT\_MAX\_COUNT CONFIG\_DSA\_PORT\_MAX\_COUNT

32#else

33#define DSA\_PORT\_MAX\_COUNT 0

34#endif

35

36#if defined(CONFIG\_DSA\_TAG\_SIZE)

37#define DSA\_TAG\_SIZE CONFIG\_DSA\_TAG\_SIZE

38#else

39#define DSA\_TAG\_SIZE 0

40#endif

41

43

44#ifdef \_\_cplusplus

45extern "C" {

46#endif

47

[ 55](group__dsa__core.md#ga012eeda4facb67b5c387b74878b53188)#define DSA\_PORT\_INST\_INIT(port, n, cfg) \

56 NET\_DEVICE\_INIT\_INSTANCE(CONCAT(dsa\_, n, port), DEVICE\_DT\_NAME(port), DT\_REG\_ADDR(port), \

57 dsa\_port\_initialize, NULL, &dsa\_switch\_context\_##n, cfg, \

58 CONFIG\_ETH\_INIT\_PRIORITY, &dsa\_eth\_api, ETHERNET\_L2, \

59 NET\_L2\_GET\_CTX\_TYPE(ETHERNET\_L2), NET\_ETH\_MTU);

60

[ 69](group__dsa__core.md#gaa7665e4b96cbc40cbae6de621f773aa4)#define DSA\_SWITCH\_INST\_INIT(n, \_dapi, data, fn) \

70 struct dsa\_switch\_context dsa\_switch\_context\_##n = { \

71 .dapi = \_dapi, \

72 .prv\_data = data, \

73 .init\_ports = 0, \

74 .num\_ports = DT\_INST\_CHILD\_NUM\_STATUS\_OKAY(n), \

75 }; \

76 DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(n, fn, n);

77

[ 79](structdsa__switch__context.md)struct [dsa\_switch\_context](structdsa__switch__context.md) {

[ 81](structdsa__switch__context.md#ad6670b8743639c7837b9188a9e8a70eb) struct [net\_if](structnet__if.md) \*[iface\_user](structdsa__switch__context.md#ad6670b8743639c7837b9188a9e8a70eb)[DSA\_PORT\_MAX\_COUNT];

82

[ 84](structdsa__switch__context.md#a227551d262998fb83dcd06ebfccdb4d7) struct [net\_if](structnet__if.md) \*[iface\_conduit](structdsa__switch__context.md#a227551d262998fb83dcd06ebfccdb4d7);

85

[ 87](structdsa__switch__context.md#a4ca4e815b96c29cb26aef7ff02d8b03c) struct [dsa\_api](structdsa__api.md) \*[dapi](structdsa__switch__context.md#a4ca4e815b96c29cb26aef7ff02d8b03c);

88

[ 90](structdsa__switch__context.md#a0eb8ee97a922eaefdaed00cf75ec5a26) void \*[prv\_data](structdsa__switch__context.md#a0eb8ee97a922eaefdaed00cf75ec5a26);

91

[ 93](structdsa__switch__context.md#ae9437d8ef21a64cdb297623096cd77f3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ports](structdsa__switch__context.md#ae9437d8ef21a64cdb297623096cd77f3);

94

[ 96](structdsa__switch__context.md#a68a619b3db141ba6127ccc4577f2edf5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_ports](structdsa__switch__context.md#a68a619b3db141ba6127ccc4577f2edf5);

97};

98

[ 103](structdsa__api.md)struct [dsa\_api](structdsa__api.md) {

105

107 struct [net\_if](structnet__if.md) \*(\*recv)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

108

110 struct [net\_pkt](structnet__pkt.md) \*(\*xmit)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

111

[ 113](structdsa__api.md#a5117a72ebe047a23f18e168282b74a30) int (\*[port\_init](structdsa__api.md#a5117a72ebe047a23f18e168282b74a30))(const struct [device](structdevice.md) \*dev);

114

[ 116](structdsa__api.md#a170af07de55d93fbdf82c89d2976d9ea) void (\*[port\_phylink\_change](structdsa__api.md#a170af07de55d93fbdf82c89d2976d9ea))(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

117 void \*user\_data);

118

[ 120](structdsa__api.md#a40cc66f48a287011ef61a0767eceda5c) void (\*[port\_generate\_random\_mac](structdsa__api.md#a40cc66f48a287011ef61a0767eceda5c))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac\_addr);

121

[ 123](structdsa__api.md#a3ad664182c5cee8786600d4dcd9bae1a) int (\*[switch\_setup](structdsa__api.md#a3ad664182c5cee8786600d4dcd9bae1a))(const struct [dsa\_switch\_context](structdsa__switch__context.md) \*dsa\_switch\_ctx);

124};

125

[ 129](structdsa__port__config.md)struct [dsa\_port\_config](structdsa__port__config.md) {

[ 131](structdsa__port__config.md#a96b55ad5f534ae4837236c0ef6f2d75b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_addr](structdsa__port__config.md#a96b55ad5f534ae4837236c0ef6f2d75b)[6];

[ 133](structdsa__port__config.md#a1ce3b39d25b2321984d91b4f311581ba) const bool [use\_random\_mac\_addr](structdsa__port__config.md#a1ce3b39d25b2321984d91b4f311581ba);

[ 135](structdsa__port__config.md#a521f8ad8298fce309f80785b850f6eef) const int [port\_idx](structdsa__port__config.md#a521f8ad8298fce309f80785b850f6eef);

[ 137](structdsa__port__config.md#acebba6797230c65baac4403b578e1cbb) const struct [device](structdevice.md) \*[phy\_dev](structdsa__port__config.md#acebba6797230c65baac4403b578e1cbb);

[ 139](structdsa__port__config.md#a8eac549c19d9f9999b95c95fa112ff97) const char \*[phy\_mode](structdsa__port__config.md#a8eac549c19d9f9999b95c95fa112ff97);

[ 141](structdsa__port__config.md#a97138eca5243d1564badfe89fd04bbd4) const struct [device](structdevice.md) \*[ethernet\_connection](structdsa__port__config.md#a97138eca5243d1564badfe89fd04bbd4);

[ 143](structdsa__port__config.md#a3ab024894788e956b545d6b3114e8739) void \*[prv\_config](structdsa__port__config.md#a3ab024894788e956b545d6b3114e8739);

144};

145

147

148enum dsa\_port\_type {

149 NON\_DSA\_PORT,

150 DSA\_CONDUIT\_PORT,

151 DSA\_USER\_PORT,

152 DSA\_CPU\_PORT,

153 DSA\_PORT,

154};

155

156/\*

157 \* DSA port init

158 \*

159 \* Returns:

160 \* - 0 if ok, < 0 if error

161 \*/

162int dsa\_port\_initialize(const struct [device](structdevice.md) \*dev);

163

164/\*

165 \* DSA transmit function

166 \*

167 \* param dev: Port device to transmit

168 \* param pkt: Network packet

169 \*

170 \* Returns:

171 \* - 0 if ok, < 0 if error

172 \*/

173int dsa\_xmit(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

174

175/\*

176 \* DSA receive function

177 \*

178 \* param iface: Interface of conduit port

179 \* param pkt: Network packet

180 \*

181 \* Returns:

182 \* - Interface to redirect

183 \*/

184struct [net\_if](structnet__if.md) \*dsa\_recv(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

185

186/\*

187 \* DSA ethernet init function to handle flags

188 \*

189 \* param iface: Interface of port

190 \*

191 \* Returns:

192 \* - 0 if ok, < 0 if error

193 \*/

194int dsa\_eth\_init(struct [net\_if](structnet__if.md) \*iface);

195

196/\* Ethernet APIs definition for switch ports \*/

197extern const struct [ethernet\_api](structethernet__api.md) dsa\_eth\_api;

198

200

[ 210](group__dsa__core.md#ga16d03129d1e4c39f8662dae4b35598d9)struct [net\_if](structnet__if.md) \*[dsa\_user\_get\_iface](group__dsa__core.md#ga16d03129d1e4c39f8662dae4b35598d9)(struct [net\_if](structnet__if.md) \*iface, int port\_idx);

211

212#ifdef \_\_cplusplus

213}

214#endif

215

219#endif /\* ZEPHYR\_INCLUDE\_NET\_DSA\_CORE\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[dsa\_user\_get\_iface](group__dsa__core.md#ga16d03129d1e4c39f8662dae4b35598d9)

struct net\_if \* dsa\_user\_get\_iface(struct net\_if \*iface, int port\_idx)

Get network interface of a user port.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[phy.h](phy_8h.md)

Public APIs for Ethernet PHY drivers.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[dsa\_api](structdsa__api.md)

Structure to provide DSA switch api callbacks - it is an augmented struct ethernet\_api.

**Definition** dsa\_core.h:103

[dsa\_api::port\_phylink\_change](structdsa__api.md#a170af07de55d93fbdf82c89d2976d9ea)

void(\* port\_phylink\_change)(const struct device \*dev, struct phy\_link\_state \*state, void \*user\_data)

Port link change.

**Definition** dsa\_core.h:116

[dsa\_api::switch\_setup](structdsa__api.md#a3ad664182c5cee8786600d4dcd9bae1a)

int(\* switch\_setup)(const struct dsa\_switch\_context \*dsa\_switch\_ctx)

Switch setup.

**Definition** dsa\_core.h:123

[dsa\_api::port\_generate\_random\_mac](structdsa__api.md#a40cc66f48a287011ef61a0767eceda5c)

void(\* port\_generate\_random\_mac)(uint8\_t \*mac\_addr)

Port generates random mac address.

**Definition** dsa\_core.h:120

[dsa\_api::port\_init](structdsa__api.md#a5117a72ebe047a23f18e168282b74a30)

int(\* port\_init)(const struct device \*dev)

Port init.

**Definition** dsa\_core.h:113

[dsa\_port\_config](structdsa__port__config.md)

Structure of DSA port configuration.

**Definition** dsa\_core.h:129

[dsa\_port\_config::use\_random\_mac\_addr](structdsa__port__config.md#a1ce3b39d25b2321984d91b4f311581ba)

const bool use\_random\_mac\_addr

Use random mac address or not.

**Definition** dsa\_core.h:133

[dsa\_port\_config::prv\_config](structdsa__port__config.md#a3ab024894788e956b545d6b3114e8739)

void \* prv\_config

Instance specific config.

**Definition** dsa\_core.h:143

[dsa\_port\_config::port\_idx](structdsa__port__config.md#a521f8ad8298fce309f80785b850f6eef)

const int port\_idx

Port index.

**Definition** dsa\_core.h:135

[dsa\_port\_config::phy\_mode](structdsa__port__config.md#a8eac549c19d9f9999b95c95fa112ff97)

const char \* phy\_mode

PHY mode.

**Definition** dsa\_core.h:139

[dsa\_port\_config::mac\_addr](structdsa__port__config.md#a96b55ad5f534ae4837236c0ef6f2d75b)

uint8\_t mac\_addr[6]

Port mac address.

**Definition** dsa\_core.h:131

[dsa\_port\_config::ethernet\_connection](structdsa__port__config.md#a97138eca5243d1564badfe89fd04bbd4)

const struct device \* ethernet\_connection

Ethernet device connected to the port.

**Definition** dsa\_core.h:141

[dsa\_port\_config::phy\_dev](structdsa__port__config.md#acebba6797230c65baac4403b578e1cbb)

const struct device \* phy\_dev

PHY device.

**Definition** dsa\_core.h:137

[dsa\_switch\_context](structdsa__switch__context.md)

DSA switch context data.

**Definition** dsa\_core.h:79

[dsa\_switch\_context::prv\_data](structdsa__switch__context.md#a0eb8ee97a922eaefdaed00cf75ec5a26)

void \* prv\_data

Instance specific data.

**Definition** dsa\_core.h:90

[dsa\_switch\_context::iface\_conduit](structdsa__switch__context.md#a227551d262998fb83dcd06ebfccdb4d7)

struct net\_if \* iface\_conduit

Pointer to DSA conduit network interface.

**Definition** dsa\_core.h:84

[dsa\_switch\_context::dapi](structdsa__switch__context.md#a4ca4e815b96c29cb26aef7ff02d8b03c)

struct dsa\_api \* dapi

DSA specific API callbacks.

**Definition** dsa\_core.h:87

[dsa\_switch\_context::init\_ports](structdsa__switch__context.md#a68a619b3db141ba6127ccc4577f2edf5)

uint8\_t init\_ports

Number of initialized ports in the DSA switch.

**Definition** dsa\_core.h:96

[dsa\_switch\_context::iface\_user](structdsa__switch__context.md#ad6670b8743639c7837b9188a9e8a70eb)

struct net\_if \* iface\_user[DSA\_PORT\_MAX\_COUNT]

Pointers to all DSA user network interfaces.

**Definition** dsa\_core.h:81

[dsa\_switch\_context::num\_ports](structdsa__switch__context.md#ae9437d8ef21a64cdb297623096cd77f3)

uint8\_t num\_ports

Number of ports in the DSA switch.

**Definition** dsa\_core.h:93

[ethernet\_api](structethernet__api.md)

Ethernet L2 API operations.

**Definition** ethernet.h:518

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[phy\_link\_state](structphy__link__state.md)

Link state.

**Definition** phy.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dsa\_core.h](dsa__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
