---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/coap__client_8h_source.html
original_path: doxygen/html/coap__client_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

24

25

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

[ 70](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb);

71#if defined(CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN)

72 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

73 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN\_VALUE];

74#else

[ 75](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5);

[ 76](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)[12];

77#endif

78};

79

81struct coap\_client\_internal\_request {

82 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_token[[COAP\_TOKEN\_MAX\_LEN](group__coap.md#ga69fbb7a145ce60fc4f3765c590e4808c)];

83 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset;

84 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) last\_id;

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tkl;

86 bool request\_ongoing;

87 struct [coap\_block\_context](structcoap__block__context.md) recv\_blk\_ctx;

88 struct [coap\_block\_context](structcoap__block__context.md) send\_blk\_ctx;

89 struct [coap\_pending](structcoap__pending.md) pending;

90 struct [coap\_client\_request](structcoap__client__request.md) coap\_request;

91 struct [coap\_packet](structcoap__packet.md) request;

92 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request\_tag[[COAP\_TOKEN\_MAX\_LEN](group__coap.md#ga69fbb7a145ce60fc4f3765c590e4808c)];

93};

94

95struct coap\_client {

96 int fd;

97 struct sockaddr address;

98 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) socklen;

99 bool response\_ready;

100 struct k\_mutex send\_mutex;

101 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) send\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

102 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_buf[[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)];

103 struct coap\_client\_internal\_request requests[CONFIG\_COAP\_CLIENT\_MAX\_REQUESTS];

104 struct coap\_option echo\_option;

105 bool send\_echo;

106};

108

[ 118](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)int [coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)(struct coap\_client \*client, const char \*info);

119

136

[ 137](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)int [coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)(struct coap\_client \*client, int sock, const struct [sockaddr](structsockaddr.md) \*addr,

138 struct [coap\_client\_request](structcoap__client__request.md) \*req, struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

139

143

144#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_CLIENT\_H\_ \*/

[coap.h](coap_8h.md)

CoAP implementation for Zephyr.

[coap\_client\_req](group__coap__client.md#ga028ebc6d75d98868599bca8b6ae56308)

int coap\_client\_req(struct coap\_client \*client, int sock, const struct sockaddr \*addr, struct coap\_client\_request \*req, struct coap\_transmission\_parameters \*params)

Send CoAP request.

[coap\_client\_response\_cb\_t](group__coap__client.md#ga0a33095a309016ddb4ff00206cfd4bb0)

void(\* coap\_client\_response\_cb\_t)(int16\_t result\_code, size\_t offset, const uint8\_t \*payload, size\_t len, bool last\_block, void \*user\_data)

Callback for CoAP request.

**Definition** coap\_client.h:46

[MAX\_COAP\_MSG\_LEN](group__coap__client.md#ga53c57dcb241786b6e0213a7198667bd0)

#define MAX\_COAP\_MSG\_LEN

**Definition** coap\_client.h:26

[coap\_client\_init](group__coap__client.md#gac85c4bcbc129b5d2be6a74f9024c84d9)

int coap\_client\_init(struct coap\_client \*client, const char \*info)

Initialize the CoAP client.

[COAP\_TOKEN\_MAX\_LEN](group__coap.md#ga69fbb7a145ce60fc4f3765c590e4808c)

#define COAP\_TOKEN\_MAX\_LEN

**Definition** coap.h:194

[coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7)

coap\_method

Available request methods.

**Definition** coap.h:73

[coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73)

coap\_content\_format

Set of Content-Format option values for CoAP.

**Definition** coap.h:201

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[kernel.h](include_2zephyr_2kernel_8h.md)

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

**Definition** coap.h:698

[coap\_client\_option](structcoap__client__option.md)

Representation of extra options for the CoAP client request.

**Definition** coap\_client.h:69

[coap\_client\_option::code](structcoap__client__option.md#a3b0c23802edd7cbb162bff6cfb745bfb)

uint16\_t code

**Definition** coap\_client.h:70

[coap\_client\_option::value](structcoap__client__option.md#ac1f5a38dad7ea227e19a96a3799329c6)

uint8\_t value[12]

**Definition** coap\_client.h:76

[coap\_client\_option::len](structcoap__client__option.md#aebc27705f851af910757f0bb2a73bbe5)

uint8\_t len

**Definition** coap\_client.h:75

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

**Definition** coap.h:270

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:327

[coap\_transmission\_parameters](structcoap__transmission__parameters.md)

CoAP transmission parameters.

**Definition** coap.h:315

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_client.h](coap__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
