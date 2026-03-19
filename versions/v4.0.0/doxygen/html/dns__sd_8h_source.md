---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dns__sd_8h_source.html
original_path: doxygen/html/dns__sd_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_sd.h

[Go to the documentation of this file.](dns__sd_8h.md)

1

4

5/\*

6 \* Copyright (c) 2020 Friedt Professional Engineering Services, Inc

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_DNS\_SD\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_DNS\_SD\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

16#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

38

[ 40](group__dns__sd.md#ga4d1f5462555d6051bdeaa21b02e7aa6e)#define DNS\_SD\_INSTANCE\_MIN\_SIZE 1

[ 42](group__dns__sd.md#ga5c0993b8bc21d47fa15f56acb313ac31)#define DNS\_SD\_INSTANCE\_MAX\_SIZE 63

[ 44](group__dns__sd.md#gacc652552aa567206ab7a4d7d070d1fbc)#define DNS\_SD\_SERVICE\_MIN\_SIZE 2

[ 46](group__dns__sd.md#gab4d208eac1491c45cb47e87c90a78c26)#define DNS\_SD\_SERVICE\_MAX\_SIZE 16

[ 48](group__dns__sd.md#ga81cac0a52e58142e492bad244ff97490)#define DNS\_SD\_SERVICE\_PREFIX '\_'

[ 50](group__dns__sd.md#gafb686ae445f5bd640176f59d62df2bdc)#define DNS\_SD\_PROTO\_SIZE 4

[ 52](group__dns__sd.md#ga19d655c1778143e2aed5d2d69a757422)#define DNS\_SD\_DOMAIN\_MIN\_SIZE 2

[ 54](group__dns__sd.md#gaa93b197f2b9a3b13c7ed8f3c455f11cb)#define DNS\_SD\_DOMAIN\_MAX\_SIZE 63

55

[ 70](group__dns__sd.md#gaeec792bc3111e1961eb2e21cd8bea80a)#define DNS\_SD\_MIN\_LABELS 3

[ 86](group__dns__sd.md#ga269e2f3bbf15a5ccd81a444749faa384)#define DNS\_SD\_MAX\_LABELS 4

87

[ 112](group__dns__sd.md#ga0c0060a680d5c4fe56f2815c920c3627)#define DNS\_SD\_REGISTER\_SERVICE(\_id, \_instance, \_service, \_proto, \

113 \_domain, \_text, \_port) \

114 static const STRUCT\_SECTION\_ITERABLE(dns\_sd\_rec, \_id) = { \

115 .instance = \_instance, \

116 .service = \_service, \

117 .proto = \_proto, \

118 .domain = \_domain, \

119 .text = (const char \*)\_text, \

120 .text\_size = sizeof(\_text) - 1, \

121 .port = \_port, \

122 }

123

[ 161](group__dns__sd.md#ga96abc525d755c138304f07cdd2d9e1c2)#define DNS\_SD\_REGISTER\_TCP\_SERVICE(id, instance, service, domain, text, \

162 port) \

163 static const uint16\_t id ## \_port = sys\_cpu\_to\_be16(port); \

164 DNS\_SD\_REGISTER\_SERVICE(id, instance, service, "\_tcp", domain, \

165 text, &id ## \_port)

166

[ 190](group__dns__sd.md#gaf8abe0968552213d46b49be16c1f21d6)#define DNS\_SD\_REGISTER\_UDP\_SERVICE(id, instance, service, domain, text, \

191 port) \

192 static const uint16\_t id ## \_port = sys\_cpu\_to\_be16(port); \

193 DNS\_SD\_REGISTER\_SERVICE(id, instance, service, "\_udp", domain, \

194 text, &id ## \_port)

195

[ 197](group__dns__sd.md#ga221216c5ffd142aa4c6cade4064d580f)#define DNS\_SD\_EMPTY\_TXT dns\_sd\_empty\_txt

198

[ 215](structdns__sd__rec.md)struct [dns\_sd\_rec](structdns__sd__rec.md) {

[ 217](structdns__sd__rec.md#a06a8d777d302f99a7ed8f4ddb7e3af7d) const char \*[instance](structdns__sd__rec.md#a06a8d777d302f99a7ed8f4ddb7e3af7d);

[ 219](structdns__sd__rec.md#ae944cbdafdaced49f7302292d23ea4f8) const char \*[service](structdns__sd__rec.md#ae944cbdafdaced49f7302292d23ea4f8);

[ 221](structdns__sd__rec.md#ad79c74e22f4546826b1de6c41402aa3e) const char \*[proto](structdns__sd__rec.md#ad79c74e22f4546826b1de6c41402aa3e);

[ 223](structdns__sd__rec.md#ad282799583cde5b60ae19d5f919c67fc) const char \*[domain](structdns__sd__rec.md#ad282799583cde5b60ae19d5f919c67fc);

[ 225](structdns__sd__rec.md#ae0585e5a0643a483d6ad12b7ff853323) const char \*[text](structdns__sd__rec.md#ae0585e5a0643a483d6ad12b7ff853323);

[ 227](structdns__sd__rec.md#a852f246f90d3608acd3b660f57a59dfb) size\_t [text\_size](structdns__sd__rec.md#a852f246f90d3608acd3b660f57a59dfb);

[ 229](structdns__sd__rec.md#a714f196f0d5297d511d97f88c18aa993) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[port](structdns__sd__rec.md#a714f196f0d5297d511d97f88c18aa993);

230};

231

233

239extern const char dns\_sd\_empty\_txt[1];

245extern const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_sd\_port\_zero;

246

248

[ 255](group__dns__sd.md#ga6d68e785607089df42d534c2f876c6d5)static inline size\_t [dns\_sd\_txt\_size](group__dns__sd.md#ga6d68e785607089df42d534c2f876c6d5)(const struct [dns\_sd\_rec](structdns__sd__rec.md) \*rec)

256{

257 return rec->[text\_size](structdns__sd__rec.md#a852f246f90d3608acd3b660f57a59dfb);

258}

259

[ 277](group__dns__sd.md#gaeba098fa6d159067c70588cb60056277)bool [dns\_sd\_is\_service\_type\_enumeration](group__dns__sd.md#gaeba098fa6d159067c70588cb60056277)(const struct [dns\_sd\_rec](structdns__sd__rec.md) \*rec);

278

[ 284](group__dns__sd.md#ga328d71e26411460b1b329db8f1ebd37b)void [dns\_sd\_create\_wildcard\_filter](group__dns__sd.md#ga328d71e26411460b1b329db8f1ebd37b)(struct [dns\_sd\_rec](structdns__sd__rec.md) \*filter);

285

289

290#ifdef \_\_cplusplus

291};

292#endif

293

294#endif /\* ZEPHYR\_INCLUDE\_NET\_DNS\_SD\_H\_ \*/

[dns\_sd\_create\_wildcard\_filter](group__dns__sd.md#ga328d71e26411460b1b329db8f1ebd37b)

void dns\_sd\_create\_wildcard\_filter(struct dns\_sd\_rec \*filter)

Create a wildcard filter for DNS-SD records.

[dns\_sd\_txt\_size](group__dns__sd.md#ga6d68e785607089df42d534c2f876c6d5)

static size\_t dns\_sd\_txt\_size(const struct dns\_sd\_rec \*rec)

Obtain the size of DNS-SD TXT data.

**Definition** dns\_sd.h:255

[dns\_sd\_is\_service\_type\_enumeration](group__dns__sd.md#gaeba098fa6d159067c70588cb60056277)

bool dns\_sd\_is\_service\_type\_enumeration(const struct dns\_sd\_rec \*rec)

Check if rec is a DNS-SD Service Type Enumeration.

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[dns\_sd\_rec](structdns__sd__rec.md)

DNS Service Discovery record.

**Definition** dns\_sd.h:215

[dns\_sd\_rec::instance](structdns__sd__rec.md#a06a8d777d302f99a7ed8f4ddb7e3af7d)

const char \* instance

"<Instance>" - e.g.

**Definition** dns\_sd.h:217

[dns\_sd\_rec::port](structdns__sd__rec.md#a714f196f0d5297d511d97f88c18aa993)

const uint16\_t \* port

A pointer to the port number used by the service.

**Definition** dns\_sd.h:229

[dns\_sd\_rec::text\_size](structdns__sd__rec.md#a852f246f90d3608acd3b660f57a59dfb)

size\_t text\_size

Size (in bytes) of the DNS TXT record.

**Definition** dns\_sd.h:227

[dns\_sd\_rec::domain](structdns__sd__rec.md#ad282799583cde5b60ae19d5f919c67fc)

const char \* domain

"<Domain>" such as "local" or "zephyrproject.org"

**Definition** dns\_sd.h:223

[dns\_sd\_rec::proto](structdns__sd__rec.md#ad79c74e22f4546826b1de6c41402aa3e)

const char \* proto

Bottom half of the "<Service>" "\_tcp" or "\_udp".

**Definition** dns\_sd.h:221

[dns\_sd\_rec::text](structdns__sd__rec.md#ae0585e5a0643a483d6ad12b7ff853323)

const char \* text

DNS TXT record.

**Definition** dns\_sd.h:225

[dns\_sd\_rec::service](structdns__sd__rec.md#ae944cbdafdaced49f7302292d23ea4f8)

const char \* service

Top half of the "<Service>" such as "\_http".

**Definition** dns\_sd.h:219

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_sd.h](dns__sd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
