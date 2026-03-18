---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dsa_8h_source.html
original_path: doxygen/html/dsa_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa.h

[Go to the documentation of this file.](dsa_8h.md)

1/\*

2 \* Copyright (c) 2020 DENX Software Engineering GmbH

3 \* Lukasz Majewski <lukma@denx.de>

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_DSA\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_DSA\_H\_

13

14#include <[zephyr/device.h](device_8h.md)>

15#include <[zephyr/net/net\_if.h](net__if_8h.md)>

16

23

[ 24](group__DSA.md#ga55b8be4fd4fad75fe1a9156c41b80b4b)#define NET\_DSA\_PORT\_MAX\_COUNT 8

[ 25](group__DSA.md#ga4ff957832aeb0c69e0ba92516eaa4c59)#define DSA\_STATUS\_PERIOD\_MS K\_MSEC(1000)

26

27/\*

28 \* Size of the DSA TAG:

29 \* - KSZ8794 - 1 byte

30 \*/

31#if defined(CONFIG\_DSA\_KSZ8794) && defined(CONFIG\_DSA\_KSZ\_TAIL\_TAGGING)

32#define DSA\_TAG\_SIZE 1

33#else

[ 34](group__DSA.md#ga0e30a4c4996c11eaa86df3ef00a26e61)#define DSA\_TAG\_SIZE 0

35#endif

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

[ 53](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)int [dsa\_tx](group__DSA.md#ga381fae2a3cf652db81db6e64d9aea62a)(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

54

68typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa))(struct [net\_if](structnet__if.md) \*iface,

69 struct [net\_pkt](structnet__pkt.md) \*pkt);

70

[ 79](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)int [dsa\_register\_recv\_callback](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa) cb);

80

[ 89](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3)struct [net\_if](structnet__if.md) \*[dsa\_net\_recv](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*\*pkt);

90

[ 94](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)typedef int (\*[dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

95

[ 105](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)int [dsa\_register\_master\_tx](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b) fn);

106

[ 115](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212)bool [dsa\_is\_port\_master](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

116

123

125struct dsa\_context {

127 struct [net\_if](structnet__if.md) \*iface\_slave[[NET\_DSA\_PORT\_MAX\_COUNT](group__DSA.md#ga55b8be4fd4fad75fe1a9156c41b80b4b)];

128

130 struct [net\_if](structnet__if.md) \*iface\_master;

131

133 struct dsa\_api \*dapi;

134

136 struct [k\_work\_delayable](structk__work__delayable.md) dsa\_work;

137

139 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_slave\_ports;

140

142 bool link\_up[[NET\_DSA\_PORT\_MAX\_COUNT](group__DSA.md#ga55b8be4fd4fad75fe1a9156c41b80b4b)];

143

145 void \*prv\_data;

146};

147

152struct dsa\_api {

154 struct net\_if \*(\*dsa\_get\_iface)(struct net\_if \*iface,

155 struct net\_pkt \*pkt);

156 /\*

157 \* Callbacks required for DSA switch initialization and configuration.

158 \*

159 \* Each switch instance (e.g. two KSZ8794 ICs) would have its own struct

160 \* dsa\_context.

161 \*/

163 int (\*switch\_read)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

164 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

166 int (\*switch\_write)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

167 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

168

170 int (\*switch\_set\_mac\_table\_entry)(const struct device \*dev,

171 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac,

172 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port,

173 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx,

174 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

175

177 int (\*switch\_get\_mac\_table\_entry)(const struct device \*dev,

178 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

179 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx);

180

181 /\*

182 \* DSA helper callbacks

183 \*/

184 struct net\_pkt \*(\*dsa\_xmit\_pkt)(struct net\_if \*iface,

185 struct net\_pkt \*pkt);

186};

187

191

[ 201](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13)struct [net\_if](structnet__if.md) \*[dsa\_get\_slave\_port](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13)(struct [net\_if](structnet__if.md) \*iface, int slave\_num);

202

[ 212](group__DSA.md#ga131e095ddf546471952663e0ce836c59)int [dsa\_switch\_read](group__DSA.md#ga131e095ddf546471952663e0ce836c59)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

213

[ 223](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f)int [dsa\_switch\_write](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

224

[ 236](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239)int [dsa\_switch\_set\_mac\_table\_entry](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239)(struct [net\_if](structnet__if.md) \*iface,

237 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac,

238 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port,

239 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx,

240 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

241

[ 251](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488)int [dsa\_switch\_get\_mac\_table\_entry](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488)(struct [net\_if](structnet__if.md) \*iface,

252 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

253 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx);

254

258

[ 259](structdsa__slave__config.md)struct [dsa\_slave\_config](structdsa__slave__config.md) {

[ 261](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_addr](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854)[6];

262};

263

264#ifdef \_\_cplusplus

265}

266#endif

267

271#endif /\* ZEPHYR\_INCLUDE\_NET\_DSA\_H\_ \*/

[device.h](device_8h.md)

[dsa\_net\_recv](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3)

struct net\_if \* dsa\_net\_recv(struct net\_if \*iface, struct net\_pkt \*\*pkt)

Set DSA interface to packet.

[dsa\_is\_port\_master](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212)

bool dsa\_is\_port\_master(struct net\_if \*iface)

DSA helper function to check if port is master.

[dsa\_switch\_read](group__DSA.md#ga131e095ddf546471952663e0ce836c59)

int dsa\_switch\_read(struct net\_if \*iface, uint16\_t reg\_addr, uint8\_t \*value)

Read from DSA switch register.

[dsa\_switch\_get\_mac\_table\_entry](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488)

int dsa\_switch\_get\_mac\_table\_entry(struct net\_if \*iface, uint8\_t \*buf, uint16\_t tbl\_entry\_idx)

Read static MAC table entry.

[dsa\_tx](group__DSA.md#ga381fae2a3cf652db81db6e64d9aea62a)

int dsa\_tx(const struct device \*dev, struct net\_pkt \*pkt)

DSA generic transmit function.

[NET\_DSA\_PORT\_MAX\_COUNT](group__DSA.md#ga55b8be4fd4fad75fe1a9156c41b80b4b)

#define NET\_DSA\_PORT\_MAX\_COUNT

**Definition** dsa.h:24

[dsa\_register\_master\_tx](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)

int dsa\_register\_master\_tx(struct net\_if \*iface, dsa\_send\_t fn)

DSA helper function to register transmit function for master.

[dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)

enum net\_verdict(\* dsa\_net\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

DSA (MGMT) Receive packet callback.

**Definition** dsa.h:68

[dsa\_get\_slave\_port](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13)

struct net\_if \* dsa\_get\_slave\_port(struct net\_if \*iface, int slave\_num)

Get network interface of a slave port.

[dsa\_switch\_set\_mac\_table\_entry](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239)

int dsa\_switch\_set\_mac\_table\_entry(struct net\_if \*iface, const uint8\_t \*mac, uint8\_t fw\_port, uint16\_t tbl\_entry\_idx, uint16\_t flags)

Write static MAC table entry.

[dsa\_switch\_write](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f)

int dsa\_switch\_write(struct net\_if \*iface, uint16\_t reg\_addr, uint8\_t value)

Write to DSA switch.

[dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)

int(\* dsa\_send\_t)(const struct device \*dev, struct net\_pkt \*pkt)

Pointer to master interface send function.

**Definition** dsa.h:94

[dsa\_register\_recv\_callback](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)

int dsa\_register\_recv\_callback(struct net\_if \*iface, dsa\_net\_recv\_cb\_t cb)

Register DSA Rx callback functions.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:98

[net\_if.h](net__if_8h.md)

Public API for network interface.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[dsa\_slave\_config](structdsa__slave__config.md)

Structure to provide mac address for each LAN interface.

**Definition** dsa.h:259

[dsa\_slave\_config::mac\_addr](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854)

uint8\_t mac\_addr[6]

MAC address for each LAN{123.,} ports.

**Definition** dsa.h:261

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:86

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dsa.h](dsa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
