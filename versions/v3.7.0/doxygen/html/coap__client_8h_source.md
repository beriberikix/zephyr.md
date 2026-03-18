---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/coap__client_8h_source.html
original_path: doxygen/html/coap__client_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

21

22#include <[zephyr/net/coap.h](coap_8h.md)>

23#include <[zephyr/kernel.h](kernel_8h.md)>

24

[ 26](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)#define MAX\_COAP\_MSG\_LEN (CONFIG\_COAP\_CLIENT\_MESSAGE\_HEADER\_SIZE + \

27 CONFIG\_COAP\_CLIENT\_MESSAGE\_SIZE)

28

[ 46](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0)typedef void (\*[coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0))([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) result\_code,

47 size\_t offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, size\_t len,

48 bool last\_block, void \*user\_data);

49

[ 53](structcoap__client__request.md)struct [coap\_client\_request](structcoap__client__request.md) {

[ 54](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791) enum [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) [method](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791);

[ 55](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18) bool [confirmable](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18);

[ 56](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd) const char \*[path](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd);

[ 57](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3) enum [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) [fmt](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3);

[ 58](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[payload](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632);

[ 59](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582) size\_t [len](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582);

[ 60](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a) [coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0) [cb](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a);

[ 61](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072) struct [coap\_client\_option](structcoap__client__option.md) \*[options](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072);

[ 62](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_options](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be);

[ 63](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4) void \*[user\_data](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4);

64};

65

[ 69](structcoap__client__option.md)struct [coap\_client\_option](structcoap__client__option.md) {

[ 71](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb);

72#if defined(CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN)

74 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

76 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN\_VALUE];

77#else

[ 79](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

[ 81](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[12];

82#endif

83};

84

86struct coap\_client\_internal\_request {

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_token[COAP\_TOKEN\_MAX\_LEN];

88 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset;

89 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) last\_id;

90 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tkl;

91 bool request\_ongoing;

92 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) in\_callback;

93 struct [coap\_block\_context](structcoap__block__context.md) recv\_blk\_ctx;

94 struct [coap\_block\_context](structcoap__block__context.md) send\_blk\_ctx;

95 struct [coap\_pending](structcoap__pending.md) pending;

96 struct [coap\_client\_request](structcoap__client__request.md) coap\_request;

97 struct [coap\_packet](structcoap__packet.md) request;

98 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tag[COAP\_TOKEN\_MAX\_LEN];

99

100 /\* For GETs with observe option set \*/

101 bool is\_observe;

102 int last\_response\_id;

103};

104

105struct coap\_client {

106 int fd;

107 struct sockaddr address;

108 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) socklen;

109 bool response\_ready;

110 struct k\_mutex send\_mutex;

111 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) send\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

112 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

113 struct coap\_client\_internal\_request requests[CONFIG\_COAP\_CLIENT\_MAX\_REQUESTS];

114 struct coap\_option echo\_option;

115 bool send\_echo;

116};

118

[ 128](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)int [coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)(struct coap\_client \*client, const char \*info);

129

146

[ 147](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)int [coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)(struct coap\_client \*client, int sock, const struct [sockaddr](structsockaddr.md) \*addr,

148 struct [coap\_client\_request](structcoap__client__request.md) \*req, struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

149

[ 158](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)void [coap\_client\_cancel\_requests](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)(struct coap\_client \*client);

159

163

164#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_CLIENT\_H\_ \*/

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

**Definition** coap\_client.h:46

[coap\_client\_cancel\_requests](group__coap__client.md#ga3f511d4df22bece05c1ac97ff4d09a80)

void coap\_client\_cancel\_requests(struct coap\_client \*client)

Cancel all current requests.

[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)

#define MAX\_COAP\_MSG\_LEN

Maximum size of a CoAP message.

**Definition** coap\_client.h:26

[coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)

int coap\_client\_init(struct coap\_client \*client, const char \*info)

Initialize the CoAP client.

[coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7)

coap\_method

Available request methods.

**Definition** coap.h:75

[coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73)

coap\_content\_format

Set of Content-Format option values for CoAP.

**Definition** coap.h:213

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

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

**Definition** coap.h:750

[coap\_client\_option](structcoap__client__option.md)

Representation of extra options for the CoAP client request.

**Definition** coap\_client.h:69

[coap\_client\_option::code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb)

uint16\_t code

Option code.

**Definition** coap\_client.h:71

[coap\_client\_option::value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)

uint8\_t value[12]

Buffer for the length.

**Definition** coap\_client.h:81

[coap\_client\_option::len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5)

uint8\_t len

Option len.

**Definition** coap\_client.h:79

[coap\_client\_request](structcoap__client__request.md)

Representation of a CoAP client request.

**Definition** coap\_client.h:53

[coap\_client\_request::num\_options](structcoap__client__request.md#a03f9aec935feab0352254f2d425c59be)

uint8\_t num\_options

Number of extra options.

**Definition** coap\_client.h:62

[coap\_client\_request::len](structcoap__client__request.md#a04e7fd6614e0a4b0a0e78f5420019582)

size\_t len

Length of the payload.

**Definition** coap\_client.h:59

[coap\_client\_request::method](structcoap__client__request.md#a308709b298a7449d32492ee1170a6791)

enum coap\_method method

Method of the request.

**Definition** coap\_client.h:54

[coap\_client\_request::confirmable](structcoap__client__request.md#a4db33f53cd9723d5c073d379578e5a18)

bool confirmable

CoAP Confirmable/Non-confirmable message.

**Definition** coap\_client.h:55

[coap\_client\_request::path](structcoap__client__request.md#a51dfca3516d01d3881e80615456e05bd)

const char \* path

Path of the requested resource.

**Definition** coap\_client.h:56

[coap\_client\_request::options](structcoap__client__request.md#ab2f777b35287169c3510fdd5be19d072)

struct coap\_client\_option \* options

Extra options to be added to request.

**Definition** coap\_client.h:61

[coap\_client\_request::user\_data](structcoap__client__request.md#ad725d95c1745d19e74d3ed39710b10b4)

void \* user\_data

User provided context.

**Definition** coap\_client.h:63

[coap\_client\_request::fmt](structcoap__client__request.md#ae0a506b0baef3133f8665a5c8799e8d3)

enum coap\_content\_format fmt

Content format to be used.

**Definition** coap\_client.h:57

[coap\_client\_request::payload](structcoap__client__request.md#aeda75b6fe9e523f7f3847d4c469b0632)

uint8\_t \* payload

User allocated buffer for send request.

**Definition** coap\_client.h:58

[coap\_client\_request::cb](structcoap__client__request.md#aefc85ec14f031aabe5ed0830d819069a)

coap\_client\_response\_cb\_t cb

Callback when response received.

**Definition** coap\_client.h:60

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:295

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:352

[coap\_transmission\_parameters](structcoap__transmission__parameters.md)

CoAP transmission parameters.

**Definition** coap.h:340

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_client.h](coap__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
