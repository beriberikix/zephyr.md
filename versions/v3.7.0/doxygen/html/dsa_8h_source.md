---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dsa_8h_source.html
original_path: doxygen/html/dsa_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

25

26#define NET\_DSA\_PORT\_MAX\_COUNT 8

27#define DSA\_STATUS\_PERIOD\_MS K\_MSEC(1000)

28

29/\*

30 \* Size of the DSA TAG:

31 \* - KSZ8794 - 1 byte

32 \*/

33#if defined(CONFIG\_DSA\_KSZ8794) && defined(CONFIG\_DSA\_KSZ\_TAIL\_TAGGING)

34#define DSA\_TAG\_SIZE 1

35#else

36#define DSA\_TAG\_SIZE 0

37#endif

38

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

[ 57](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)int [dsa\_tx](group__DSA.md#ga381fae2a3cf652db81db6e64d9aea62a)(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

58

72typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa))(struct [net\_if](structnet__if.md) \*iface,

73 struct [net\_pkt](structnet__pkt.md) \*pkt);

74

[ 83](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)int [dsa\_register\_recv\_callback](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), [dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa) cb);

84

[ 93](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3)struct [net\_if](structnet__if.md) \*[dsa\_net\_recv](group__DSA.md#ga01a24efc07ef0aa4125b91781c3039f3)(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*\*pkt);

94

[ 98](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b)typedef int (\*[dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

99

[ 109](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)int [dsa\_register\_master\_tx](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), [dsa\_send\_t](group__DSA.md#gad9a6e0ad0e100914f6b932843908d42b) fn);

110

[ 119](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212)bool [dsa\_is\_port\_master](group__DSA.md#ga06ef38794a9ca3f7b8d3a32d2e1b2212)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

120

127

129struct dsa\_context {

131 struct [net\_if](structnet__if.md) \*iface\_slave[NET\_DSA\_PORT\_MAX\_COUNT];

132

134 struct [net\_if](structnet__if.md) \*iface\_master;

135

137 struct dsa\_api \*dapi;

138

140 struct [k\_work\_delayable](structk__work__delayable.md) dsa\_work;

141

143 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_slave\_ports;

144

146 bool link\_up[NET\_DSA\_PORT\_MAX\_COUNT];

147

149 void \*prv\_data;

150};

151

156struct dsa\_api {

158 struct net\_if \*(\*dsa\_get\_iface)(struct net\_if \*iface,

159 struct net\_pkt \*pkt);

160 /\*

161 \* Callbacks required for DSA switch initialization and configuration.

162 \*

163 \* Each switch instance (e.g. two KSZ8794 ICs) would have its own struct

164 \* dsa\_context.

165 \*/

167 int (\*switch\_read)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

168 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

170 int (\*switch\_write)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

171 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

172

174 int (\*switch\_set\_mac\_table\_entry)(const struct device \*dev,

175 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac,

176 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port,

177 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx,

178 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

179

181 int (\*switch\_get\_mac\_table\_entry)(const struct device \*dev,

182 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

183 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx);

184

185 /\*

186 \* DSA helper callbacks

187 \*/

188 struct net\_pkt \*(\*dsa\_xmit\_pkt)(struct net\_if \*iface,

189 struct net\_pkt \*pkt);

190};

191

195

[ 205](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13)struct [net\_if](structnet__if.md) \*[dsa\_get\_slave\_port](group__DSA.md#ga6ee72f05ee1192ceb3f691d0fe007e13)(struct [net\_if](structnet__if.md) \*iface, int slave\_num);

206

[ 216](group__DSA.md#ga131e095ddf546471952663e0ce836c59)int [dsa\_switch\_read](group__DSA.md#ga131e095ddf546471952663e0ce836c59)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

217

[ 227](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f)int [dsa\_switch\_write](group__DSA.md#gad6464601dcfccc77f06a0fed9ce80b0f)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

228

[ 240](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239)int [dsa\_switch\_set\_mac\_table\_entry](group__DSA.md#ga742d4531fc59bfd37a229c2f25c84239)(struct [net\_if](structnet__if.md) \*iface,

241 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac,

242 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port,

243 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx,

244 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

245

[ 255](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488)int [dsa\_switch\_get\_mac\_table\_entry](group__DSA.md#ga16767d0b80c684b32c33bbcc74d54488)(struct [net\_if](structnet__if.md) \*iface,

256 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

257 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx);

258

262

[ 263](structdsa__slave__config.md)struct [dsa\_slave\_config](structdsa__slave__config.md) {

[ 265](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mac\_addr](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854)[6];

266};

267

268#ifdef \_\_cplusplus

269}

270#endif

271

275#endif /\* ZEPHYR\_INCLUDE\_NET\_DSA\_H\_ \*/

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

[dsa\_register\_master\_tx](group__DSA.md#ga676bff9b468696e2158bf5b14211fd27)

int dsa\_register\_master\_tx(struct net\_if \*iface, dsa\_send\_t fn)

DSA helper function to register transmit function for master.

[dsa\_net\_recv\_cb\_t](group__DSA.md#ga6c40af9c2caefa7f855d225a41b43faa)

enum net\_verdict(\* dsa\_net\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

DSA (MGMT) Receive packet callback.

**Definition** dsa.h:72

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

**Definition** dsa.h:98

[dsa\_register\_recv\_callback](group__DSA.md#gaee78adf88b0598611097e42ff94e9c52)

int dsa\_register\_recv\_callback(struct net\_if \*iface, dsa\_net\_recv\_cb\_t cb)

Register DSA Rx callback functions.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

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

**Definition** device.h:403

[dsa\_slave\_config](structdsa__slave__config.md)

Structure to provide mac address for each LAN interface.

**Definition** dsa.h:263

[dsa\_slave\_config::mac\_addr](structdsa__slave__config.md#a1bdd6dc67a85170b4fa74358581dd854)

uint8\_t mac\_addr[6]

MAC address for each LAN{123.,} ports.

**Definition** dsa.h:265

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3908

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dsa.h](dsa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
