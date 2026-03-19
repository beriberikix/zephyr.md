---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/coap__client_8h_source.html
original_path: doxygen/html/coap__client_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_client.h

[Go to the documentation of this file.](coap__client_8h.md)

1

6

7/\*

8 \* Copyright (c) 2023 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_NET\_COAP\_CLIENT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_COAP\_CLIENT\_H\_

14

23

24#include <[zephyr/net/coap.h](coap_8h.md)>

25#include <[zephyr/kernel.h](kernel_8h.md)>

26

[ 28](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)#define MAX\_COAP\_MSG\_LEN (CONFIG\_COAP\_CLIENT\_MESSAGE\_HEADER\_SIZE + \

29 CONFIG\_COAP\_CLIENT\_MESSAGE\_SIZE)

30

[ 48](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0)typedef void (\*[coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0))([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) result\_code,

49 size\_t offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, size\_t len,

50 bool last\_block, void \*user\_data);

51

[ 55](structcoap__client__request.md)struct [coap\_client\_request](structcoap__client__request.md) {

[ 56](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791) enum [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) [method](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791);

[ 57](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18) bool [confirmable](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18);

[ 58](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd) const char \*[path](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd);

[ 59](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3) enum [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) [fmt](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3);

[ 60](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[payload](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632);

[ 61](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582) size\_t [len](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582);

[ 62](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a) [coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0) [cb](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a);

[ 63](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072) struct [coap\_client\_option](structcoap__client__option.md) \*[options](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072);

[ 64](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_options](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be);

[ 65](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4) void \*[user\_data](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4);

66};

67

[ 71](structcoap__client__option.md)struct [coap\_client\_option](structcoap__client__option.md) {

[ 73](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb);

74#if defined(CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN)

76 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

78 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN\_VALUE];

79#else

[ 81](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

[ 83](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[12];

84#endif

85};

86

88struct coap\_client\_internal\_request {

89 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_token[COAP\_TOKEN\_MAX\_LEN];

90 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset;

91 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) last\_id;

92 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tkl;

93 bool request\_ongoing;

94 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) in\_callback;

95 struct [coap\_block\_context](structcoap__block__context.md) recv\_blk\_ctx;

96 struct [coap\_block\_context](structcoap__block__context.md) send\_blk\_ctx;

97 struct [coap\_pending](structcoap__pending.md) pending;

98 struct [coap\_client\_request](structcoap__client__request.md) coap\_request;

99 struct [coap\_packet](structcoap__packet.md) request;

100 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tag[COAP\_TOKEN\_MAX\_LEN];

101

102 /\* For GETs with observe option set \*/

103 bool is\_observe;

104 int last\_response\_id;

105};

106

107struct coap\_client {

108 int fd;

109 struct sockaddr address;

110 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) socklen;

111 struct k\_mutex lock;

112 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) send\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

114 struct coap\_client\_internal\_request requests[CONFIG\_COAP\_CLIENT\_MAX\_REQUESTS];

115 struct coap\_option echo\_option;

116 bool send\_echo;

117};

119

[ 129](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)int [coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)(struct coap\_client \*client, const char \*info);

130

147

[ 148](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)int [coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)(struct coap\_client \*client, int sock, const struct [sockaddr](structsockaddr.md) \*addr,

149 struct [coap\_client\_request](structcoap__client__request.md) \*req, struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

150

[ 159](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)void [coap\_client\_cancel\_requests](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)(struct coap\_client \*client);

160

[ 172](group__coap__client.md#gabbd785c47f2efedc3ae1d76b97ef7d31)static inline struct [coap\_client\_option](structcoap__client__option.md) [coap\_client\_option\_initial\_block2](group__coap__client.md#gabbd785c47f2efedc3ae1d76b97ef7d31)(void)

173{

174 struct [coap\_client\_option](structcoap__client__option.md) block2 = {

175 .code = [COAP\_OPTION\_BLOCK2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972),

176 .len = 1,

177 .value[0] = [coap\_bytes\_to\_block\_size](group__coap.md#ga27e3008b8511333e0c0115ba928017f3)(CONFIG\_COAP\_CLIENT\_BLOCK\_SIZE),

178 };

179

180 return block2;

181}

182

186

187#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_CLIENT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[coap.h](coap_8h.md)

CoAP implementation for Zephyr.

[coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)

int coap\_client\_req(struct coap\_client \*client, int sock, const struct sockaddr \*addr, struct coap\_client\_request \*req, struct coap\_transmission\_parameters \*params)

Send CoAP request.

[coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0)

void(\* coap\_client\_response\_cb\_t)(int16\_t result\_code, size\_t offset, const uint8\_t \*payload, size\_t len, bool last\_block, void \*user\_data)

Callback for CoAP request.

**Definition** coap\_client.h:48

[coap\_client\_cancel\_requests](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)

void coap\_client\_cancel\_requests(struct coap\_client \*client)

Cancel all current requests.

[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)

#define MAX\_COAP\_MSG\_LEN

Maximum size of a CoAP message.

**Definition** coap\_client.h:28

[coap\_client\_option\_initial\_block2](group__coap__client.md#gabbd785c47f2efedc3ae1d76b97ef7d31)

static struct coap\_client\_option coap\_client\_option\_initial\_block2(void)

Initialise a Block2 option to be added to a request.

**Definition** coap\_client.h:172

[coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)

int coap\_client\_init(struct coap\_client \*client, const char \*info)

Initialize the CoAP client.

[coap\_bytes\_to\_block\_size](group__coap.md#ga27e3008b8511333e0c0115ba928017f3)

static enum coap\_block\_size coap\_bytes\_to\_block\_size(uint16\_t bytes)

Helper for converting block size in bytes to enumeration.

**Definition** coap.h:773

[coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7)

coap\_method

Available request methods.

**Definition** coap.h:76

[coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73)

coap\_content\_format

Set of Content-Format option values for CoAP.

**Definition** coap.h:214

[COAP\_OPTION\_BLOCK2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972)

@ COAP\_OPTION\_BLOCK2

Block2 (RFC 7959).

**Definition** coap.h:60

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[coap\_block\_context](structcoap__block__context.md)

Represents the current state of a block-wise transaction.

**Definition** coap.h:789

[coap\_client\_option](structcoap__client__option.md)

Representation of extra options for the CoAP client request.

**Definition** coap\_client.h:71

[coap\_client\_option::code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb)

uint16\_t code

Option code.

**Definition** coap\_client.h:73

[coap\_client\_option::value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)

uint8\_t value[12]

Buffer for the length.

**Definition** coap\_client.h:83

[coap\_client\_option::len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5)

uint8\_t len

Option len.

**Definition** coap\_client.h:81

[coap\_client\_request](structcoap__client__request.md)

Representation of a CoAP client request.

**Definition** coap\_client.h:55

[coap\_client\_request::num\_options](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be)

uint8\_t num\_options

Number of extra options.

**Definition** coap\_client.h:64

[coap\_client\_request::len](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582)

size\_t len

Length of the payload.

**Definition** coap\_client.h:61

[coap\_client\_request::method](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791)

enum coap\_method method

Method of the request.

**Definition** coap\_client.h:56

[coap\_client\_request::confirmable](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18)

bool confirmable

CoAP Confirmable/Non-confirmable message.

**Definition** coap\_client.h:57

[coap\_client\_request::path](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd)

const char \* path

Path of the requested resource.

**Definition** coap\_client.h:58

[coap\_client\_request::options](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072)

struct coap\_client\_option \* options

Extra options to be added to request.

**Definition** coap\_client.h:63

[coap\_client\_request::user\_data](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4)

void \* user\_data

User provided context.

**Definition** coap\_client.h:65

[coap\_client\_request::fmt](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3)

enum coap\_content\_format fmt

Content format to be used.

**Definition** coap\_client.h:59

[coap\_client\_request::payload](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632)

uint8\_t \* payload

User allocated buffer for send request.

**Definition** coap\_client.h:60

[coap\_client\_request::cb](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a)

coap\_client\_response\_cb\_t cb

Callback when response received.

**Definition** coap\_client.h:62

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:312

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:376

[coap\_transmission\_parameters](structcoap__transmission__parameters.md)

CoAP transmission parameters.

**Definition** coap.h:357

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_client.h](coap__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
