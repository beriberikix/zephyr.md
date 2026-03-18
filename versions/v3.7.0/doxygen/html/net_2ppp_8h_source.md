---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net_2ppp_8h_source.html
original_path: doxygen/html/net_2ppp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp.h

[Go to the documentation of this file.](net_2ppp_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_PPP\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_PPP\_H\_

14

15#include <[zephyr/net/net\_if.h](net__if_8h.md)>

16#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

17#include <[zephyr/net/net\_stats.h](net__stats_8h.md)>

18#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

30

[ 32](group__ppp.md#gaec050624f0693600196068d8f5413e6f)#define PPP\_MRU CONFIG\_NET\_PPP\_MTU\_MRU

33

[ 35](group__ppp.md#gacc51e91347721a8255ae891ddc43636b)#define PPP\_MTU PPP\_MRU

36

[ 38](group__ppp.md#ga2e5d0ae66bf076123cb29effc0a8e894)#define PPP\_MAX\_TERMINATE\_REASON\_LEN 32

39

[ 41](group__ppp.md#gaad7380b3a502f4b649348b733124f21a)#define PPP\_INTERFACE\_IDENTIFIER\_LEN 8

42

[ 44](structppp__api.md)struct [ppp\_api](structppp__api.md) {

[ 49](structppp__api.md#acc4e82fbaa8b933040b0a77da8a3cae0) struct net\_if\_api [iface\_api](structppp__api.md#acc4e82fbaa8b933040b0a77da8a3cae0);

50

[ 52](structppp__api.md#ab85010475c4f03a48ad7629ed4947626) int (\*[start](structppp__api.md#ab85010475c4f03a48ad7629ed4947626))(const struct [device](structdevice.md) \*dev);

53

[ 55](structppp__api.md#a42576f1d58920f48a0d0adf888f99006) int (\*[stop](structppp__api.md#a42576f1d58920f48a0d0adf888f99006))(const struct [device](structdevice.md) \*dev);

56

[ 58](structppp__api.md#aa0ec35e57f22674ef06f8cc3bc09987f) int (\*[send](structppp__api.md#aa0ec35e57f22674ef06f8cc3bc09987f))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

59

60#if defined(CONFIG\_NET\_STATISTICS\_PPP)

65 struct [net\_stats\_ppp](structnet__stats__ppp.md) \*(\*get\_stats)(const struct [device](structdevice.md) \*dev);

66#endif

67};

68

69/\* Make sure that the network interface API is properly setup inside

70 \* PPP API struct (it is the first one).

71 \*/

72BUILD\_ASSERT(offsetof(struct [ppp\_api](structppp__api.md), iface\_api) == 0);

73

[ 79](group__ppp.md#ga8ad7cc0d142a6e7ea82c45bec2cc3670)enum [ppp\_protocol\_type](group__ppp.md#ga8ad7cc0d142a6e7ea82c45bec2cc3670) {

[ 80](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6) [PPP\_IP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6) = 0x0021,

[ 81](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe) [PPP\_IPV6](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe) = 0x0057,

[ 82](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21) [PPP\_IPCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21) = 0x8021,

[ 83](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44) [PPP\_ECP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44) = 0x8053,

[ 84](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0) [PPP\_IPV6CP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0) = 0x8057,

[ 85](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b) [PPP\_CCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b) = 0x80FD,

[ 86](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9) [PPP\_LCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9) = 0xc021,

[ 87](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206) [PPP\_PAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206) = 0xc023,

[ 88](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25) [PPP\_CHAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25) = 0xc223,

[ 89](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2) [PPP\_EAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2) = 0xc227,

90};

91

[ 95](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b)enum [ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) {

[ 97](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d) [PPP\_DEAD](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d),

[ 99](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4) [PPP\_ESTABLISH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4),

[ 101](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a) [PPP\_AUTH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a),

[ 103](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af) [PPP\_NETWORK](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af),

[ 105](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7) [PPP\_RUNNING](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7),

[ 107](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7) [PPP\_TERMINATE](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7),

108};

109

111

115enum ppp\_state {

116 PPP\_INITIAL,

117 PPP\_STARTING,

118 PPP\_CLOSED,

119 PPP\_STOPPED,

120 PPP\_CLOSING,

121 PPP\_STOPPING,

122 PPP\_REQUEST\_SENT,

123 PPP\_ACK\_RECEIVED,

124 PPP\_ACK\_SENT,

125 PPP\_OPENED

126};

127

131enum ppp\_packet\_type {

132 PPP\_CONFIGURE\_REQ = 1,

133 PPP\_CONFIGURE\_ACK = 2,

134 PPP\_CONFIGURE\_NACK = 3,

135 PPP\_CONFIGURE\_REJ = 4,

136 PPP\_TERMINATE\_REQ = 5,

137 PPP\_TERMINATE\_ACK = 6,

138 PPP\_CODE\_REJ = 7,

139 PPP\_PROTOCOL\_REJ = 8,

140 PPP\_ECHO\_REQ = 9,

141 PPP\_ECHO\_REPLY = 10,

142 PPP\_DISCARD\_REQ = 11

143};

144

146

[ 150](group__ppp.md#gac8f3d915c930d61831bcb13d6201b15c)enum [lcp\_option\_type](group__ppp.md#gac8f3d915c930d61831bcb13d6201b15c) {

[ 152](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3) [LCP\_OPTION\_RESERVED](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3) = 0,

153

[ 155](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe) [LCP\_OPTION\_MRU](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe) = 1,

156

[ 158](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef) [LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef) = 2,

159

[ 161](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743) [LCP\_OPTION\_AUTH\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743) = 3,

162

[ 164](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9) [LCP\_OPTION\_QUALITY\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9) = 4,

165

[ 167](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8) [LCP\_OPTION\_MAGIC\_NUMBER](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8) = 5,

168

[ 170](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4) [LCP\_OPTION\_PROTO\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4) = 7,

171

[ 173](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524) [LCP\_OPTION\_ADDR\_CTRL\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524) = 8

174} \_\_packed;

175

[ 179](group__ppp.md#ga1064e3d8c6aa3d3161e399d6937162b6)enum [ipcp\_option\_type](group__ppp.md#ga1064e3d8c6aa3d3161e399d6937162b6) {

[ 181](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b) [IPCP\_OPTION\_RESERVED](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b) = 0,

182

[ 184](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b) [IPCP\_OPTION\_IP\_ADDRESSES](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b) = 1,

185

[ 187](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6) [IPCP\_OPTION\_IP\_COMP\_PROTO](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6) = 2,

188

[ 190](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9) [IPCP\_OPTION\_IP\_ADDRESS](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9) = 3,

191

192 /\* RFC 1877 \*/

193

[ 195](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931) [IPCP\_OPTION\_DNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931) = 129,

196

[ 198](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552) [IPCP\_OPTION\_NBNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552) = 130,

199

[ 201](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964) [IPCP\_OPTION\_DNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964) = 131,

202

[ 204](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad) [IPCP\_OPTION\_NBNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad) = 132,

205} \_\_packed;

206

[ 210](group__ppp.md#gaf30172a9fead40463d129a5afeaf1ac3)enum [ipv6cp\_option\_type](group__ppp.md#gaf30172a9fead40463d129a5afeaf1ac3) {

[ 212](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858) [IPV6CP\_OPTION\_RESERVED](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858) = 0,

213

[ 215](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7) [IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7) = 1,

216} \_\_packed;

217

[ 226](group__ppp.md#ga15afa05abc0446201c912c75644306bf)typedef void (\*[net\_ppp\_lcp\_echo\_reply\_cb\_t](group__ppp.md#ga15afa05abc0446201c912c75644306bf))(void \*user\_data,

227 size\_t user\_data\_len);

228

229struct ppp\_my\_option\_data;

230struct ppp\_my\_option\_info;

231

[ 235](structppp__fsm.md)struct [ppp\_fsm](structppp__fsm.md) {

[ 237](structppp__fsm.md#ae033ee41d66ec568dc4244115730114a) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structppp__fsm.md#ae033ee41d66ec568dc4244115730114a);

238

240 struct {

[ 242](structppp__fsm.md#a42bb4a40d88893d461d93202c4ad8e2a) int (\*[config\_info\_ack](structppp__fsm.md#a42bb4a40d88893d461d93202c4ad8e2a))(struct [ppp\_fsm](structppp__fsm.md) \*fsm,

243 struct [net\_pkt](structnet__pkt.md) \*pkt,

244 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

245

247 struct [net\_pkt](structnet__pkt.md) \*(\*config\_info\_add)(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

248

[ 250](structppp__fsm.md#a099cc834fc5e2d062ee4410a1de729c2) int (\*[config\_info\_len](structppp__fsm.md#a099cc834fc5e2d062ee4410a1de729c2))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

251

[ 253](structppp__fsm.md#ad0967edee7fee72368732876ca6bc5e7) int (\*[config\_info\_nack](structppp__fsm.md#ad0967edee7fee72368732876ca6bc5e7))(struct [ppp\_fsm](structppp__fsm.md) \*fsm,

254 struct [net\_pkt](structnet__pkt.md) \*pkt,

255 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

256 bool rejected);

257

[ 259](structppp__fsm.md#ab430e0240f35718f6eaf8f9052a4edde) int (\*[config\_info\_req](structppp__fsm.md#ab430e0240f35718f6eaf8f9052a4edde))(struct [ppp\_fsm](structppp__fsm.md) \*fsm,

260 struct [net\_pkt](structnet__pkt.md) \*pkt,

261 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

262 struct [net\_pkt](structnet__pkt.md) \*ret\_pkt);

263

[ 265](structppp__fsm.md#a90dad2f780b4573559c76e6a67e44f4c) int (\*[config\_info\_rej](structppp__fsm.md#a90dad2f780b4573559c76e6a67e44f4c))(struct [ppp\_fsm](structppp__fsm.md) \*fsm,

266 struct [net\_pkt](structnet__pkt.md) \*pkt,

267 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

268

[ 270](structppp__fsm.md#afb0296b0d8e9b60594781cfd5f8acee3) void (\*[config\_info\_reset](structppp__fsm.md#afb0296b0d8e9b60594781cfd5f8acee3))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

271

[ 273](structppp__fsm.md#aa1ca37605ab7934c16a5260d531efa00) void (\*[up](structppp__fsm.md#aa1ca37605ab7934c16a5260d531efa00))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

274

[ 276](structppp__fsm.md#a2ba52396156dd1ec63d67dc6ae0a2d5a) void (\*[down](structppp__fsm.md#a2ba52396156dd1ec63d67dc6ae0a2d5a))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

277

[ 279](structppp__fsm.md#ad7f2d5d09acb298d29ebc60b4f748478) void (\*[starting](structppp__fsm.md#ad7f2d5d09acb298d29ebc60b4f748478))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

280

[ 282](structppp__fsm.md#aecdcdfa2f7264c7b1b2202a23327fa3b) void (\*[finished](structppp__fsm.md#aecdcdfa2f7264c7b1b2202a23327fa3b))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

283

[ 285](structppp__fsm.md#ae4f68c11709ab03445b853c12c11c787) void (\*[proto\_reject](structppp__fsm.md#ae4f68c11709ab03445b853c12c11c787))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

286

[ 288](structppp__fsm.md#aa302cfe79c73fe081d2642cf54d1d3cf) void (\*[retransmit](structppp__fsm.md#ae0c0b33d5e51a01a63b5afbf5012c0f5))(struct [ppp\_fsm](structppp__fsm.md) \*fsm);

289

293 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[proto\_extension](structppp__fsm.md#aa302cfe79c73fe081d2642cf54d1d3cf))(struct [ppp\_fsm](structppp__fsm.md) \*fsm,

294 enum ppp\_packet\_type code,

295 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structppp__fsm.md#a844c8747b299d3614e5ccff892b45d5c),

296 struct [net\_pkt](structnet__pkt.md) \*pkt);

[ 297](structppp__fsm.md#a0e3cd20db2e06d6d0e85478c013e36db) } [cb](structppp__fsm.md#a0e3cd20db2e06d6d0e85478c013e36db);

298

300 struct {

[ 302](structppp__fsm.md#a117a5df8fed62b57a59580a2513fc1c3) const struct ppp\_my\_option\_info \*[info](structppp__fsm.md#a117a5df8fed62b57a59580a2513fc1c3);

303

[ 305](structppp__fsm.md#a64330e89597eac2b8b841d0f95389473) struct ppp\_my\_option\_data \*[data](structppp__fsm.md#a64330e89597eac2b8b841d0f95389473);

306

[ 308](structppp__fsm.md#a7e125f9011a9377d18dc523b1f84964f) size\_t [count](structppp__fsm.md#a7e125f9011a9377d18dc523b1f84964f);

[ 309](structppp__fsm.md#a39a7d8b02a0c905ea27565445295c4f2) } [my\_options](structppp__fsm.md#a39a7d8b02a0c905ea27565445295c4f2);

310

[ 312](structppp__fsm.md#a489c2d992e03e126ba2d1bbfe7a71b85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structppp__fsm.md#a489c2d992e03e126ba2d1bbfe7a71b85);

313;

[ 315](structppp__fsm.md#a31d84f3fa6246bd70d664dbae6845c4b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [retransmits](structppp__fsm.md#a31d84f3fa6246bd70d664dbae6845c4b);

316

[ 318](structppp__fsm.md#a0a0523fe16fe45a756615b62e8673828) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nack\_loops](structppp__fsm.md#a0a0523fe16fe45a756615b62e8673828);

319

[ 321](structppp__fsm.md#a55c0fe60eb84f33386ec90691ee0f707) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [recv\_nack\_loops](structppp__fsm.md#a55c0fe60eb84f33386ec90691ee0f707);

322

[ 324](structppp__fsm.md#a054fd1e61e667072a552eadf54634ffc) char [terminate\_reason](structppp__fsm.md#a054fd1e61e667072a552eadf54634ffc)[[PPP\_MAX\_TERMINATE\_REASON\_LEN](group__ppp.md#ga2e5d0ae66bf076123cb29effc0a8e894)];

325

[ 327](structppp__fsm.md#a2032a922d2e356155c5a4c86cf48ff3d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [protocol](structppp__fsm.md#a2032a922d2e356155c5a4c86cf48ff3d);

328

[ 330](structppp__fsm.md#ab955d11b75231e94ec1613d5c8c027e1) enum ppp\_state [state](structppp__fsm.md#ab955d11b75231e94ec1613d5c8c027e1);

331

[ 333](structppp__fsm.md#a9192c71ef82436c519ac3b8ccd38a089) const char \*[name](structppp__fsm.md#a9192c71ef82436c519ac3b8ccd38a089);

334

[ 336](structppp__fsm.md#a844c8747b299d3614e5ccff892b45d5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structppp__fsm.md#a844c8747b299d3614e5ccff892b45d5c);

337

[ 339](structppp__fsm.md#a8fe52ffe2a17c03ff0432e36c9d43578) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [req\_id](structppp__fsm.md#a8fe52ffe2a17c03ff0432e36c9d43578);

340

[ 342](structppp__fsm.md#a42777bc7c5f904cbac6bb0b16615fb02) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ack\_received](structppp__fsm.md#a42777bc7c5f904cbac6bb0b16615fb02) : 1;

343};

344

346

347#define PPP\_MY\_OPTION\_ACKED BIT(0)

348#define PPP\_MY\_OPTION\_REJECTED BIT(1)

349

350struct ppp\_my\_option\_data {

351 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

352};

353

354#define IPCP\_NUM\_MY\_OPTIONS 3

355#define IPV6CP\_NUM\_MY\_OPTIONS 1

356

357enum ppp\_flags {

358 PPP\_CARRIER\_UP,

359};

360

362

[ 364](structlcp__options.md)struct [lcp\_options](structlcp__options.md) {

[ 366](structlcp__options.md#a68d9f004596bfac6dea9b14bd22e9dda) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [magic](structlcp__options.md#a68d9f004596bfac6dea9b14bd22e9dda);

367

[ 369](structlcp__options.md#a2672e1374c25aac1571adccadda5283e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [async\_map](structlcp__options.md#a2672e1374c25aac1571adccadda5283e);

370

[ 372](structlcp__options.md#a028da648c4b8cdd9330d9195a161e847) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mru](structlcp__options.md#a028da648c4b8cdd9330d9195a161e847);

373

[ 375](structlcp__options.md#a560d009cb642fff99ef83a9e6c056c6b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [auth\_proto](structlcp__options.md#a560d009cb642fff99ef83a9e6c056c6b);

376};

377

378#if defined(CONFIG\_NET\_L2\_PPP\_OPTION\_MRU)

379#define LCP\_NUM\_MY\_OPTIONS 1

380#endif

381

[ 383](structipcp__options.md)struct [ipcp\_options](structipcp__options.md) {

[ 385](structipcp__options.md#a2d4a41b74c4a319551c003210c1e6f3d) struct [in\_addr](structin__addr.md) [address](structipcp__options.md#a2d4a41b74c4a319551c003210c1e6f3d);

386

[ 388](structipcp__options.md#a5c2b153ee9103393159a7090357df5a1) struct [in\_addr](structin__addr.md) [dns1\_address](structipcp__options.md#a5c2b153ee9103393159a7090357df5a1);

389

[ 391](structipcp__options.md#a4e9825d9c161fa318cb538ebc231dd44) struct [in\_addr](structin__addr.md) [dns2\_address](structipcp__options.md#a4e9825d9c161fa318cb538ebc231dd44);

392};

393

[ 395](structipv6cp__options.md)struct [ipv6cp\_options](structipv6cp__options.md) {

[ 397](structipv6cp__options.md#a4962f03fcf645257306ceeb95116ddce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iid](structipv6cp__options.md#a4962f03fcf645257306ceeb95116ddce)[[PPP\_INTERFACE\_IDENTIFIER\_LEN](group__ppp.md#gaad7380b3a502f4b649348b733124f21a)];

398};

399

[ 401](structppp__context.md)struct [ppp\_context](structppp__context.md) {

[ 405](structppp__context.md#a6b327cafe07a0807163589471a9bdae8) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](structppp__context.md#a6b327cafe07a0807163589471a9bdae8);

406

[ 408](structppp__context.md#a5671d7ba465c424004f0460e5ed0d3ba) struct [k\_work\_delayable](structk__work__delayable.md) [startup](structppp__context.md#a5671d7ba465c424004f0460e5ed0d3ba);

409

411 struct {

[ 413](structppp__context.md#ac555024228a1e1d830c915a098428bc5) struct [ppp\_fsm](structppp__fsm.md) [fsm](structppp__context.md#ac555024228a1e1d830c915a098428bc5);

414

[ 416](structppp__context.md#a37f609192ee6b739d7018d5a07ce179f) struct [lcp\_options](structlcp__options.md) [my\_options](structppp__context.md#a37f609192ee6b739d7018d5a07ce179f);

417

[ 419](structppp__context.md#a80fffd30b145b0842e36299ac78d5da8) struct [lcp\_options](structlcp__options.md) [peer\_options](structppp__context.md#a80fffd30b145b0842e36299ac78d5da8);

420

[ 422](structppp__context.md#a4d91bf9e6e36415b13be02ccf03d3e40) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [magic](structppp__context.md#a4d91bf9e6e36415b13be02ccf03d3e40);

423#if defined(CONFIG\_NET\_L2\_PPP\_OPTION\_MRU)

424 struct ppp\_my\_option\_data my\_options\_data[LCP\_NUM\_MY\_OPTIONS];

425#endif

[ 426](structppp__context.md#a7705aedba900cf1de66b02ad488b7161) } [lcp](structppp__context.md#a7705aedba900cf1de66b02ad488b7161);

427

428#if defined(CONFIG\_NET\_IPV4)

430 struct {

432 struct [ppp\_fsm](structppp__fsm.md) fsm;

433

435 struct [ipcp\_options](structipcp__options.md) my\_options;

436

438 struct [ipcp\_options](structipcp__options.md) peer\_options;

439

441 struct ppp\_my\_option\_data my\_options\_data[IPCP\_NUM\_MY\_OPTIONS];

442 } ipcp;

443#endif

444

445#if defined(CONFIG\_NET\_IPV6)

447 struct {

449 struct ppp\_fsm fsm;

450

452 struct ipv6cp\_options my\_options;

453

455 struct ipv6cp\_options peer\_options;

456

458 struct ppp\_my\_option\_data my\_options\_data[IPV6CP\_NUM\_MY\_OPTIONS];

459 } ipv6cp;

460#endif

461

462#if defined(CONFIG\_NET\_L2\_PPP\_PAP)

464 struct {

466 struct ppp\_fsm fsm;

467 } pap;

468#endif

469

470#if defined(CONFIG\_NET\_SHELL)

472 struct {

474 struct {

477 [net\_ppp\_lcp\_echo\_reply\_cb\_t](group__ppp.md#ga15afa05abc0446201c912c75644306bf) cb;

478

480 void \*user\_data;

481

483 size\_t user\_data\_len;

484 } echo\_reply;

485

487 struct k\_sem wait\_echo\_reply;

488

490 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) echo\_req\_data;

491

493 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) echo\_reply\_data;

494 } shell;

495#endif

496

[ 498](structppp__context.md#a3b0bfb9c3ceece34565b282efa74390e) struct [net\_if](structnet__if.md) \*[iface](structppp__context.md#a3b0bfb9c3ceece34565b282efa74390e);

499

[ 501](structppp__context.md#a141cb0b4f4b99313de63a5bff2b7cafc) struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) [mgmt\_evt\_cb](structppp__context.md#a141cb0b4f4b99313de63a5bff2b7cafc);

502

[ 504](structppp__context.md#a6afb964ef87696fdadb5cb0c714bd841) enum [ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) [phase](structppp__context.md#a6afb964ef87696fdadb5cb0c714bd841);

505

[ 507](structppp__context.md#a1afa42c99b098407f8bba11e50178c84) struct k\_sem [wait\_ppp\_link\_terminated](structppp__context.md#a1afa42c99b098407f8bba11e50178c84);

508

[ 510](structppp__context.md#ae784688e2d78f7427c6672583e326d94) struct k\_sem [wait\_ppp\_link\_down](structppp__context.md#ae784688e2d78f7427c6672583e326d94);

511

[ 513](structppp__context.md#a1c6674bad19047abcc3097bf5ff5f31d) enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [ppp\_l2\_flags](structppp__context.md#a1c6674bad19047abcc3097bf5ff5f31d);

514

[ 516](structppp__context.md#a2e04c6e411fe5b07d9d2cda1a61db57f) int [network\_protos\_open](structppp__context.md#a2e04c6e411fe5b07d9d2cda1a61db57f);

517

[ 519](structppp__context.md#a9dd6e156897c53d488344bbbe05d4ae1) int [network\_protos\_up](structppp__context.md#a9dd6e156897c53d488344bbbe05d4ae1);

520

[ 522](structppp__context.md#a3d97c93b183ca455daf0e3bc2b9c25e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_ready\_to\_serve](structppp__context.md#a3d97c93b183ca455daf0e3bc2b9c25e1) : 1;

523

[ 525](structppp__context.md#a7f103857c7412a6ee9471b6c67baea71) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_enabled](structppp__context.md#a7f103857c7412a6ee9471b6c67baea71) : 1;

526

[ 528](structppp__context.md#acdee16f229cb6aa0672630de1d3ee39b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_enable\_done](structppp__context.md#acdee16f229cb6aa0672630de1d3ee39b) : 1;

529

[ 531](structppp__context.md#a861216f943c5af5d5db58f10ba4263ac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_ipcp\_up](structppp__context.md#a861216f943c5af5d5db58f10ba4263ac) : 1;

532

[ 534](structppp__context.md#a7ef9ac6bb1f86ea417032fe93fc7e8a0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_ipcp\_open](structppp__context.md#a7ef9ac6bb1f86ea417032fe93fc7e8a0) : 1;

535

[ 537](structppp__context.md#a7b4ee6988626cb69c012a0b58c27bef5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_ipv6cp\_up](structppp__context.md#a7b4ee6988626cb69c012a0b58c27bef5) : 1;

538

[ 540](structppp__context.md#ab139c8d6f1d16c702cb9ca92a7f82178) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_ipv6cp\_open](structppp__context.md#ab139c8d6f1d16c702cb9ca92a7f82178) : 1;

541

[ 543](structppp__context.md#a52227a05ce8a63f3a4f7535e60fdf979) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_pap\_up](structppp__context.md#a52227a05ce8a63f3a4f7535e60fdf979) : 1;

544

[ 546](structppp__context.md#a80c2c3248c47fac7fce8d463cfbc0c9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [is\_pap\_open](structppp__context.md#a80c2c3248c47fac7fce8d463cfbc0c9f) : 1;

547};

548

[ 554](group__ppp.md#gaabf883cfefc9910b9b9d8931e68b320c)void [net\_ppp\_init](group__ppp.md#gaabf883cfefc9910b9b9d8931e68b320c)(struct [net\_if](structnet__if.md) \*iface);

555

556/\* Management API for PPP \*/

557

559

560#define PPP\_L2\_CTX\_TYPE struct ppp\_context

561

562#define \_NET\_PPP\_LAYER NET\_MGMT\_LAYER\_L2

563#define \_NET\_PPP\_CODE 0x209

564#define \_NET\_PPP\_BASE (NET\_MGMT\_IFACE\_BIT | \

565 NET\_MGMT\_LAYER(\_NET\_PPP\_LAYER) | \

566 NET\_MGMT\_LAYER\_CODE(\_NET\_PPP\_CODE))

567#define \_NET\_PPP\_EVENT (\_NET\_PPP\_BASE | NET\_MGMT\_EVENT\_BIT)

568

569enum net\_event\_ppp\_cmd {

570 NET\_EVENT\_PPP\_CMD\_CARRIER\_ON = 1,

571 NET\_EVENT\_PPP\_CMD\_CARRIER\_OFF,

572 NET\_EVENT\_PPP\_CMD\_PHASE\_RUNNING,

573 NET\_EVENT\_PPP\_CMD\_PHASE\_DEAD,

574};

575

576struct [net\_if](structnet__if.md);

577

579

[ 581](group__ppp.md#ga17c4e8cc92e0e9261d0b2dcc704b2f93)#define NET\_EVENT\_PPP\_CARRIER\_ON \

582 (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_ON)

583

[ 585](group__ppp.md#ga2b3c11bbdc7b36d4381811b210340e45)#define NET\_EVENT\_PPP\_CARRIER\_OFF \

586 (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_OFF)

587

[ 589](group__ppp.md#ga4853534532ac4875321785a70c5a1b19)#define NET\_EVENT\_PPP\_PHASE\_RUNNING \

590 (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_RUNNING)

591

[ 593](group__ppp.md#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)#define NET\_EVENT\_PPP\_PHASE\_DEAD \

594 (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_DEAD)

595

601#if defined(CONFIG\_NET\_L2\_PPP\_MGMT)

602void [ppp\_mgmt\_raise\_carrier\_on\_event](group__ppp.md#ga1436cf5cfcb6752e41c9e06a0ee30030)(struct [net\_if](structnet__if.md) \*iface);

603#else

[ 604](group__ppp.md#ga1436cf5cfcb6752e41c9e06a0ee30030)static inline void [ppp\_mgmt\_raise\_carrier\_on\_event](group__ppp.md#ga1436cf5cfcb6752e41c9e06a0ee30030)(struct [net\_if](structnet__if.md) \*iface)

605{

606 ARG\_UNUSED(iface);

607}

608#endif

609

615#if defined(CONFIG\_NET\_L2\_PPP\_MGMT)

616void [ppp\_mgmt\_raise\_carrier\_off\_event](group__ppp.md#gad96b2c77cf6a066d55d78c5d63cb9bd0)(struct [net\_if](structnet__if.md) \*iface);

617#else

[ 618](group__ppp.md#gad96b2c77cf6a066d55d78c5d63cb9bd0)static inline void [ppp\_mgmt\_raise\_carrier\_off\_event](group__ppp.md#gad96b2c77cf6a066d55d78c5d63cb9bd0)(struct [net\_if](structnet__if.md) \*iface)

619{

620 ARG\_UNUSED(iface);

621}

622#endif

623

629#if defined(CONFIG\_NET\_L2\_PPP\_MGMT)

630void [ppp\_mgmt\_raise\_phase\_running\_event](group__ppp.md#ga74e94e9fcae30bc386c5e3d951ed5882)(struct [net\_if](structnet__if.md) \*iface);

631#else

[ 632](group__ppp.md#ga74e94e9fcae30bc386c5e3d951ed5882)static inline void [ppp\_mgmt\_raise\_phase\_running\_event](group__ppp.md#ga74e94e9fcae30bc386c5e3d951ed5882)(struct [net\_if](structnet__if.md) \*iface)

633{

634 ARG\_UNUSED(iface);

635}

636#endif

637

643#if defined(CONFIG\_NET\_L2\_PPP\_MGMT)

644void [ppp\_mgmt\_raise\_phase\_dead\_event](group__ppp.md#gad7f41d9012098ed1a04f897e252cc32d)(struct [net\_if](structnet__if.md) \*iface);

645#else

[ 646](group__ppp.md#gad7f41d9012098ed1a04f897e252cc32d)static inline void [ppp\_mgmt\_raise\_phase\_dead\_event](group__ppp.md#gad7f41d9012098ed1a04f897e252cc32d)(struct [net\_if](structnet__if.md) \*iface)

647{

648 ARG\_UNUSED(iface);

649}

650#endif

651

662#if defined(CONFIG\_NET\_L2\_PPP)

663int [net\_ppp\_ping](group__ppp.md#ga9893a7c93b3d23b96b4d83aa1204c500)(int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

664#else

[ 665](group__ppp.md#ga9893a7c93b3d23b96b4d83aa1204c500)static inline int [net\_ppp\_ping](group__ppp.md#ga9893a7c93b3d23b96b4d83aa1204c500)(int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

666{

667 ARG\_UNUSED(idx);

668 ARG\_UNUSED(timeout);

669

670 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

671}

672#endif

673

682#if defined(CONFIG\_NET\_L2\_PPP) && defined(CONFIG\_NET\_SHELL)

683struct [ppp\_context](structppp__context.md) \*[net\_ppp\_context\_get](group__ppp.md#ga4f6104cff735f9829762b6552a7346bf)(int idx);

684#else

[ 685](group__ppp.md#ga4f6104cff735f9829762b6552a7346bf)static inline struct [ppp\_context](structppp__context.md) \*[net\_ppp\_context\_get](group__ppp.md#ga4f6104cff735f9829762b6552a7346bf)(int idx)

686{

687 ARG\_UNUSED(idx);

688

689 return NULL;

690}

691#endif

692

693#ifdef \_\_cplusplus

694}

695#endif

696

700

701#endif /\* ZEPHYR\_INCLUDE\_NET\_PPP\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:34

[ipcp\_option\_type](group__ppp.md#ga1064e3d8c6aa3d3161e399d6937162b6)

ipcp\_option\_type

IPCP option types from RFC 1332.

**Definition** ppp.h:179

[ppp\_mgmt\_raise\_carrier\_on\_event](group__ppp.md#ga1436cf5cfcb6752e41c9e06a0ee30030)

static void ppp\_mgmt\_raise\_carrier\_on\_event(struct net\_if \*iface)

Raise CARRIER\_ON event when PPP is connected.

**Definition** ppp.h:604

[net\_ppp\_lcp\_echo\_reply\_cb\_t](group__ppp.md#ga15afa05abc0446201c912c75644306bf)

void(\* net\_ppp\_lcp\_echo\_reply\_cb\_t)(void \*user\_data, size\_t user\_data\_len)

A callback function that can be called if a Echo-Reply needs to be received.

**Definition** ppp.h:226

[ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b)

ppp\_phase

PPP phases.

**Definition** ppp.h:95

[PPP\_MAX\_TERMINATE\_REASON\_LEN](group__ppp.md#ga2e5d0ae66bf076123cb29effc0a8e894)

#define PPP\_MAX\_TERMINATE\_REASON\_LEN

Max length of terminate description string.

**Definition** ppp.h:38

[net\_ppp\_context\_get](group__ppp.md#ga4f6104cff735f9829762b6552a7346bf)

static struct ppp\_context \* net\_ppp\_context\_get(int idx)

Get PPP context information.

**Definition** ppp.h:685

[ppp\_mgmt\_raise\_phase\_running\_event](group__ppp.md#ga74e94e9fcae30bc386c5e3d951ed5882)

static void ppp\_mgmt\_raise\_phase\_running\_event(struct net\_if \*iface)

Raise PHASE\_RUNNING event when PPP reaching RUNNING phase.

**Definition** ppp.h:632

[ppp\_protocol\_type](group__ppp.md#ga8ad7cc0d142a6e7ea82c45bec2cc3670)

ppp\_protocol\_type

PPP protocol types.

**Definition** ppp.h:79

[net\_ppp\_ping](group__ppp.md#ga9893a7c93b3d23b96b4d83aa1204c500)

static int net\_ppp\_ping(int idx, int32\_t timeout)

Send PPP Echo-Request to peer.

**Definition** ppp.h:665

[net\_ppp\_init](group__ppp.md#gaabf883cfefc9910b9b9d8931e68b320c)

void net\_ppp\_init(struct net\_if \*iface)

Initialize PPP L2 stack for a given interface.

[PPP\_INTERFACE\_IDENTIFIER\_LEN](group__ppp.md#gaad7380b3a502f4b649348b733124f21a)

#define PPP\_INTERFACE\_IDENTIFIER\_LEN

Length of network interface identifier.

**Definition** ppp.h:41

[lcp\_option\_type](group__ppp.md#gac8f3d915c930d61831bcb13d6201b15c)

lcp\_option\_type

LCP option types from RFC 1661 ch.

**Definition** ppp.h:150

[ppp\_mgmt\_raise\_phase\_dead\_event](group__ppp.md#gad7f41d9012098ed1a04f897e252cc32d)

static void ppp\_mgmt\_raise\_phase\_dead\_event(struct net\_if \*iface)

Raise PHASE\_DEAD event when PPP reaching DEAD phase.

**Definition** ppp.h:646

[ppp\_mgmt\_raise\_carrier\_off\_event](group__ppp.md#gad96b2c77cf6a066d55d78c5d63cb9bd0)

static void ppp\_mgmt\_raise\_carrier\_off\_event(struct net\_if \*iface)

Raise CARRIER\_OFF event when PPP is disconnected.

**Definition** ppp.h:618

[ipv6cp\_option\_type](group__ppp.md#gaf30172a9fead40463d129a5afeaf1ac3)

ipv6cp\_option\_type

IPV6CP option types from RFC 5072.

**Definition** ppp.h:210

[IPCP\_OPTION\_IP\_ADDRESS](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9)

@ IPCP\_OPTION\_IP\_ADDRESS

IP Address.

**Definition** ppp.h:190

[IPCP\_OPTION\_DNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964)

@ IPCP\_OPTION\_DNS2

Secondary DNS Server Address.

**Definition** ppp.h:201

[IPCP\_OPTION\_IP\_COMP\_PROTO](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6)

@ IPCP\_OPTION\_IP\_COMP\_PROTO

IP Compression Protocol.

**Definition** ppp.h:187

[IPCP\_OPTION\_NBNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad)

@ IPCP\_OPTION\_NBNS2

Secondary NBNS Server Address.

**Definition** ppp.h:204

[IPCP\_OPTION\_RESERVED](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b)

@ IPCP\_OPTION\_RESERVED

Reserved IPCP option value (do not use).

**Definition** ppp.h:181

[IPCP\_OPTION\_NBNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552)

@ IPCP\_OPTION\_NBNS1

Primary NBNS Server Address.

**Definition** ppp.h:198

[IPCP\_OPTION\_IP\_ADDRESSES](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b)

@ IPCP\_OPTION\_IP\_ADDRESSES

IP Addresses.

**Definition** ppp.h:184

[IPCP\_OPTION\_DNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931)

@ IPCP\_OPTION\_DNS1

Primary DNS Server Address.

**Definition** ppp.h:195

[PPP\_AUTH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a)

@ PPP\_AUTH

Link authentication with peer.

**Definition** ppp.h:101

[PPP\_RUNNING](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7)

@ PPP\_RUNNING

Network running.

**Definition** ppp.h:105

[PPP\_NETWORK](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af)

@ PPP\_NETWORK

Network connection establishment.

**Definition** ppp.h:103

[PPP\_ESTABLISH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4)

@ PPP\_ESTABLISH

Link is being established.

**Definition** ppp.h:99

[PPP\_DEAD](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d)

@ PPP\_DEAD

Physical-layer not ready.

**Definition** ppp.h:97

[PPP\_TERMINATE](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)

@ PPP\_TERMINATE

Link termination.

**Definition** ppp.h:107

[PPP\_IPV6](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe)

@ PPP\_IPV6

RFC 5072.

**Definition** ppp.h:81

[PPP\_IP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6)

@ PPP\_IP

RFC 1332.

**Definition** ppp.h:80

[PPP\_CHAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25)

@ PPP\_CHAP

RFC 1334.

**Definition** ppp.h:88

[PPP\_LCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9)

@ PPP\_LCP

RFC 1661.

**Definition** ppp.h:86

[PPP\_IPCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21)

@ PPP\_IPCP

RFC 1332.

**Definition** ppp.h:82

[PPP\_ECP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44)

@ PPP\_ECP

RFC 1968.

**Definition** ppp.h:83

[PPP\_CCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b)

@ PPP\_CCP

RFC 1962.

**Definition** ppp.h:85

[PPP\_EAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2)

@ PPP\_EAP

RFC 2284.

**Definition** ppp.h:89

[PPP\_IPV6CP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0)

@ PPP\_IPV6CP

RFC 5072.

**Definition** ppp.h:84

[PPP\_PAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206)

@ PPP\_PAP

RFC 1334.

**Definition** ppp.h:87

[LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef)

@ LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP

Async-Control-Character-Map.

**Definition** ppp.h:158

[LCP\_OPTION\_ADDR\_CTRL\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524)

@ LCP\_OPTION\_ADDR\_CTRL\_COMPRESS

Address-and-Control-Field-Compression.

**Definition** ppp.h:173

[LCP\_OPTION\_QUALITY\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9)

@ LCP\_OPTION\_QUALITY\_PROTO

Quality-Protocol.

**Definition** ppp.h:164

[LCP\_OPTION\_MAGIC\_NUMBER](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8)

@ LCP\_OPTION\_MAGIC\_NUMBER

Magic-Number.

**Definition** ppp.h:167

[LCP\_OPTION\_RESERVED](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3)

@ LCP\_OPTION\_RESERVED

Reserved option value (do not use).

**Definition** ppp.h:152

[LCP\_OPTION\_PROTO\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4)

@ LCP\_OPTION\_PROTO\_COMPRESS

Protocol-Field-Compression.

**Definition** ppp.h:170

[LCP\_OPTION\_MRU](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe)

@ LCP\_OPTION\_MRU

Maximum-Receive-Unit.

**Definition** ppp.h:155

[LCP\_OPTION\_AUTH\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743)

@ LCP\_OPTION\_AUTH\_PROTO

Authentication-Protocol.

**Definition** ppp.h:161

[IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7)

@ IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER

Interface identifier.

**Definition** ppp.h:215

[IPV6CP\_OPTION\_RESERVED](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858)

@ IPV6CP\_OPTION\_RESERVED

Reserved IPV6CP option value (do not use).

**Definition** ppp.h:212

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[net\_stats.h](net__stats_8h.md)

Network statistics.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[ipcp\_options](structipcp__options.md)

IPv4 control protocol options.

**Definition** ppp.h:383

[ipcp\_options::address](structipcp__options.md#a2d4a41b74c4a319551c003210c1e6f3d)

struct in\_addr address

IPv4 address.

**Definition** ppp.h:385

[ipcp\_options::dns2\_address](structipcp__options.md#a4e9825d9c161fa318cb538ebc231dd44)

struct in\_addr dns2\_address

Secondary DNS server address.

**Definition** ppp.h:391

[ipcp\_options::dns1\_address](structipcp__options.md#a5c2b153ee9103393159a7090357df5a1)

struct in\_addr dns1\_address

Primary DNS server address.

**Definition** ppp.h:388

[ipv6cp\_options](structipv6cp__options.md)

IPv6 control protocol options.

**Definition** ppp.h:395

[ipv6cp\_options::iid](structipv6cp__options.md#a4962f03fcf645257306ceeb95116ddce)

uint8\_t iid[8]

Interface identifier.

**Definition** ppp.h:397

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3908

[lcp\_options](structlcp__options.md)

Link control protocol options.

**Definition** ppp.h:364

[lcp\_options::mru](structlcp__options.md#a028da648c4b8cdd9330d9195a161e847)

uint16\_t mru

Maximum Receive Unit value.

**Definition** ppp.h:372

[lcp\_options::async\_map](structlcp__options.md#a2672e1374c25aac1571adccadda5283e)

uint32\_t async\_map

Async char map.

**Definition** ppp.h:369

[lcp\_options::auth\_proto](structlcp__options.md#a560d009cb642fff99ef83a9e6c056c6b)

uint16\_t auth\_proto

Which authentication protocol was negotiated (0 means none).

**Definition** ppp.h:375

[lcp\_options::magic](structlcp__options.md#a68d9f004596bfac6dea9b14bd22e9dda)

uint32\_t magic

Magic number.

**Definition** ppp.h:366

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)

Network Management event callback structure Used to register a callback into the network management e...

**Definition** net\_mgmt.h:143

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_stats\_ppp](structnet__stats__ppp.md)

All PPP specific statistics.

**Definition** net\_stats.h:575

[ppp\_api](structppp__api.md)

PPP L2 API.

**Definition** ppp.h:44

[ppp\_api::stop](structppp__api.md#a42576f1d58920f48a0d0adf888f99006)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** ppp.h:55

[ppp\_api::send](structppp__api.md#aa0ec35e57f22674ef06f8cc3bc09987f)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

Send a network packet.

**Definition** ppp.h:58

[ppp\_api::start](structppp__api.md#ab85010475c4f03a48ad7629ed4947626)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** ppp.h:52

[ppp\_api::iface\_api](structppp__api.md#acc4e82fbaa8b933040b0a77da8a3cae0)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** ppp.h:49

[ppp\_context](structppp__context.md)

PPP L2 context specific to certain network interface.

**Definition** ppp.h:401

[ppp\_context::mgmt\_evt\_cb](structppp__context.md#a141cb0b4f4b99313de63a5bff2b7cafc)

struct net\_mgmt\_event\_callback mgmt\_evt\_cb

Network management callback structure.

**Definition** ppp.h:501

[ppp\_context::wait\_ppp\_link\_terminated](structppp__context.md#a1afa42c99b098407f8bba11e50178c84)

struct k\_sem wait\_ppp\_link\_terminated

Signal when PPP link is terminated.

**Definition** ppp.h:507

[ppp\_context::ppp\_l2\_flags](structppp__context.md#a1c6674bad19047abcc3097bf5ff5f31d)

enum net\_l2\_flags ppp\_l2\_flags

This tells what features the PPP supports.

**Definition** ppp.h:513

[ppp\_context::network\_protos\_open](structppp__context.md#a2e04c6e411fe5b07d9d2cda1a61db57f)

int network\_protos\_open

This tells how many network protocols are open.

**Definition** ppp.h:516

[ppp\_context::my\_options](structppp__context.md#a37f609192ee6b739d7018d5a07ce179f)

struct lcp\_options my\_options

Options that we want to request.

**Definition** ppp.h:416

[ppp\_context::iface](structppp__context.md#a3b0bfb9c3ceece34565b282efa74390e)

struct net\_if \* iface

Network interface related to this PPP connection.

**Definition** ppp.h:498

[ppp\_context::is\_ready\_to\_serve](structppp__context.md#a3d97c93b183ca455daf0e3bc2b9c25e1)

uint16\_t is\_ready\_to\_serve

Is PPP ready to receive packets.

**Definition** ppp.h:522

[ppp\_context::magic](structppp__context.md#a4d91bf9e6e36415b13be02ccf03d3e40)

uint32\_t magic

Magic-Number value.

**Definition** ppp.h:422

[ppp\_context::is\_pap\_up](structppp__context.md#a52227a05ce8a63f3a4f7535e60fdf979)

uint16\_t is\_pap\_up

PAP status (up / down).

**Definition** ppp.h:543

[ppp\_context::startup](structppp__context.md#a5671d7ba465c424004f0460e5ed0d3ba)

struct k\_work\_delayable startup

PPP startup worker.

**Definition** ppp.h:408

[ppp\_context::phase](structppp__context.md#a6afb964ef87696fdadb5cb0c714bd841)

enum ppp\_phase phase

Current phase of PPP link.

**Definition** ppp.h:504

[ppp\_context::flags](structppp__context.md#a6b327cafe07a0807163589471a9bdae8)

atomic\_t flags

Flags representing PPP state, which are accessed from multiple threads.

**Definition** ppp.h:405

[ppp\_context::lcp](structppp__context.md#a7705aedba900cf1de66b02ad488b7161)

struct ppp\_context::@107044235232120325226013173232044313172073104354 lcp

LCP options.

[ppp\_context::is\_ipv6cp\_up](structppp__context.md#a7b4ee6988626cb69c012a0b58c27bef5)

uint16\_t is\_ipv6cp\_up

IPV6CP status (up / down).

**Definition** ppp.h:537

[ppp\_context::is\_ipcp\_open](structppp__context.md#a7ef9ac6bb1f86ea417032fe93fc7e8a0)

uint16\_t is\_ipcp\_open

IPCP open status (open / closed).

**Definition** ppp.h:534

[ppp\_context::is\_enabled](structppp__context.md#a7f103857c7412a6ee9471b6c67baea71)

uint16\_t is\_enabled

Is PPP L2 enabled or not.

**Definition** ppp.h:525

[ppp\_context::is\_pap\_open](structppp__context.md#a80c2c3248c47fac7fce8d463cfbc0c9f)

uint16\_t is\_pap\_open

PAP open status (open / closed).

**Definition** ppp.h:546

[ppp\_context::peer\_options](structppp__context.md#a80fffd30b145b0842e36299ac78d5da8)

struct lcp\_options peer\_options

Options that peer want to request.

**Definition** ppp.h:419

[ppp\_context::is\_ipcp\_up](structppp__context.md#a861216f943c5af5d5db58f10ba4263ac)

uint16\_t is\_ipcp\_up

IPCP status (up / down).

**Definition** ppp.h:531

[ppp\_context::network\_protos\_up](structppp__context.md#a9dd6e156897c53d488344bbbe05d4ae1)

int network\_protos\_up

This tells how many network protocols are up.

**Definition** ppp.h:519

[ppp\_context::is\_ipv6cp\_open](structppp__context.md#ab139c8d6f1d16c702cb9ca92a7f82178)

uint16\_t is\_ipv6cp\_open

IPV6CP open status (open / closed).

**Definition** ppp.h:540

[ppp\_context::fsm](structppp__context.md#ac555024228a1e1d830c915a098428bc5)

struct ppp\_fsm fsm

Finite state machine for LCP.

**Definition** ppp.h:413

[ppp\_context::is\_enable\_done](structppp__context.md#acdee16f229cb6aa0672630de1d3ee39b)

uint16\_t is\_enable\_done

PPP enable pending.

**Definition** ppp.h:528

[ppp\_context::wait\_ppp\_link\_down](structppp__context.md#ae784688e2d78f7427c6672583e326d94)

struct k\_sem wait\_ppp\_link\_down

Signal when PPP link is down.

**Definition** ppp.h:510

[ppp\_fsm](structppp__fsm.md)

Generic PPP Finite State Machine.

**Definition** ppp.h:235

[ppp\_fsm::terminate\_reason](structppp__fsm.md#a054fd1e61e667072a552eadf54634ffc)

char terminate\_reason[32]

Reason for closing protocol.

**Definition** ppp.h:324

[ppp\_fsm::config\_info\_len](structppp__fsm.md#a099cc834fc5e2d062ee4410a1de729c2)

int(\* config\_info\_len)(struct ppp\_fsm \*fsm)

Length of Configuration Information.

**Definition** ppp.h:250

[ppp\_fsm::nack\_loops](structppp__fsm.md#a0a0523fe16fe45a756615b62e8673828)

uint32\_t nack\_loops

Number of NACK loops since last ACK.

**Definition** ppp.h:318

[ppp\_fsm::cb](structppp__fsm.md#a0e3cd20db2e06d6d0e85478c013e36db)

struct ppp\_fsm::@052004163371367320103113371230205042101145245273 cb

FSM callbacks.

[ppp\_fsm::info](structppp__fsm.md#a117a5df8fed62b57a59580a2513fc1c3)

const struct ppp\_my\_option\_info \* info

Options information.

**Definition** ppp.h:302

[ppp\_fsm::protocol](structppp__fsm.md#a2032a922d2e356155c5a4c86cf48ff3d)

uint16\_t protocol

PPP protocol number for this FSM.

**Definition** ppp.h:327

[ppp\_fsm::down](structppp__fsm.md#a2ba52396156dd1ec63d67dc6ae0a2d5a)

void(\* down)(struct ppp\_fsm \*fsm)

FSM leaves OPENED state.

**Definition** ppp.h:276

[ppp\_fsm::retransmits](structppp__fsm.md#a31d84f3fa6246bd70d664dbae6845c4b)

uint32\_t retransmits

Number of re-transmissions left.

**Definition** ppp.h:315

[ppp\_fsm::my\_options](structppp__fsm.md#a39a7d8b02a0c905ea27565445295c4f2)

struct ppp\_fsm::@036065054042057125263035255322050022074300066337 my\_options

My options.

[ppp\_fsm::ack\_received](structppp__fsm.md#a42777bc7c5f904cbac6bb0b16615fb02)

uint8\_t ack\_received

Have received valid Ack, Nack or Reject to a Request.

**Definition** ppp.h:342

[ppp\_fsm::config\_info\_ack](structppp__fsm.md#a42bb4a40d88893d461d93202c4ad8e2a)

int(\* config\_info\_ack)(struct ppp\_fsm \*fsm, struct net\_pkt \*pkt, uint16\_t length)

Acknowledge Configuration Information.

**Definition** ppp.h:242

[ppp\_fsm::flags](structppp__fsm.md#a489c2d992e03e126ba2d1bbfe7a71b85)

uint32\_t flags

Option bits.

**Definition** ppp.h:312

[ppp\_fsm::recv\_nack\_loops](structppp__fsm.md#a55c0fe60eb84f33386ec90691ee0f707)

uint32\_t recv\_nack\_loops

Number of NACKs received.

**Definition** ppp.h:321

[ppp\_fsm::data](structppp__fsm.md#a64330e89597eac2b8b841d0f95389473)

struct ppp\_my\_option\_data \* data

Options negotiation data.

**Definition** ppp.h:305

[ppp\_fsm::count](structppp__fsm.md#a7e125f9011a9377d18dc523b1f84964f)

size\_t count

Number of negotiated options.

**Definition** ppp.h:308

[ppp\_fsm::id](structppp__fsm.md#a844c8747b299d3614e5ccff892b45d5c)

uint8\_t id

Current id.

**Definition** ppp.h:336

[ppp\_fsm::req\_id](structppp__fsm.md#a8fe52ffe2a17c03ff0432e36c9d43578)

uint8\_t req\_id

Current request id.

**Definition** ppp.h:339

[ppp\_fsm::config\_info\_rej](structppp__fsm.md#a90dad2f780b4573559c76e6a67e44f4c)

int(\* config\_info\_rej)(struct ppp\_fsm \*fsm, struct net\_pkt \*pkt, uint16\_t length)

Reject Configuration Information.

**Definition** ppp.h:265

[ppp\_fsm::name](structppp__fsm.md#a9192c71ef82436c519ac3b8ccd38a089)

const char \* name

Protocol/layer name of this FSM (for debugging).

**Definition** ppp.h:333

[ppp\_fsm::up](structppp__fsm.md#aa1ca37605ab7934c16a5260d531efa00)

void(\* up)(struct ppp\_fsm \*fsm)

FSM goes to OPENED state.

**Definition** ppp.h:273

[ppp\_fsm::proto\_extension](structppp__fsm.md#aa302cfe79c73fe081d2642cf54d1d3cf)

enum net\_verdict(\* proto\_extension)(struct ppp\_fsm \*fsm, enum ppp\_packet\_type code, uint8\_t id, struct net\_pkt \*pkt)

Any code that is not understood by PPP is passed to this FSM for further processing.

**Definition** ppp.h:293

[ppp\_fsm::config\_info\_req](structppp__fsm.md#ab430e0240f35718f6eaf8f9052a4edde)

int(\* config\_info\_req)(struct ppp\_fsm \*fsm, struct net\_pkt \*pkt, uint16\_t length, struct net\_pkt \*ret\_pkt)

Request peer's Configuration Information.

**Definition** ppp.h:259

[ppp\_fsm::state](structppp__fsm.md#ab955d11b75231e94ec1613d5c8c027e1)

enum ppp\_state state

Current state of PPP link.

**Definition** ppp.h:330

[ppp\_fsm::config\_info\_nack](structppp__fsm.md#ad0967edee7fee72368732876ca6bc5e7)

int(\* config\_info\_nack)(struct ppp\_fsm \*fsm, struct net\_pkt \*pkt, uint16\_t length, bool rejected)

Negative Acknowledge Configuration Information.

**Definition** ppp.h:253

[ppp\_fsm::starting](structppp__fsm.md#ad7f2d5d09acb298d29ebc60b4f748478)

void(\* starting)(struct ppp\_fsm \*fsm)

Starting this protocol.

**Definition** ppp.h:279

[ppp\_fsm::timer](structppp__fsm.md#ae033ee41d66ec568dc4244115730114a)

struct k\_work\_delayable timer

Timeout timer.

**Definition** ppp.h:237

[ppp\_fsm::retransmit](structppp__fsm.md#ae0c0b33d5e51a01a63b5afbf5012c0f5)

void(\* retransmit)(struct ppp\_fsm \*fsm)

Retransmit.

**Definition** ppp.h:288

[ppp\_fsm::proto\_reject](structppp__fsm.md#ae4f68c11709ab03445b853c12c11c787)

void(\* proto\_reject)(struct ppp\_fsm \*fsm)

We received Protocol-Reject.

**Definition** ppp.h:285

[ppp\_fsm::finished](structppp__fsm.md#aecdcdfa2f7264c7b1b2202a23327fa3b)

void(\* finished)(struct ppp\_fsm \*fsm)

Quitting this protocol.

**Definition** ppp.h:282

[ppp\_fsm::config\_info\_reset](structppp__fsm.md#afb0296b0d8e9b60594781cfd5f8acee3)

void(\* config\_info\_reset)(struct ppp\_fsm \*fsm)

Reset Configuration Information.

**Definition** ppp.h:270

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ppp.h](net_2ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
