---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ubx_8h_source.html
original_path: doxygen/html/ubx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx.h

[Go to the documentation of this file.](ubx_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/kernel.h](kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

10

11#include <[zephyr/modem/pipe.h](pipe_8h.md)>

12

13#ifndef ZEPHYR\_MODEM\_UBX\_

14#define ZEPHYR\_MODEM\_UBX\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

26

[ 27](group__modem__ubx.md#ga703255ca4aee83952007115eb74aba50)#define UBX\_FRM\_HEADER\_SZ 6

[ 28](group__modem__ubx.md#ga36bcc1dda3daf89377b9cde87f642ecb)#define UBX\_FRM\_FOOTER\_SZ 2

[ 29](group__modem__ubx.md#ga76c616ef547947b5aed71cf516db69e9)#define UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD (UBX\_FRM\_HEADER\_SZ + UBX\_FRM\_FOOTER\_SZ)

[ 30](group__modem__ubx.md#ga658ec1be18701eeb8464e36690719ddf)#define UBX\_FRM\_SZ(payload\_size) (payload\_size + UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD)

31

[ 32](group__modem__ubx.md#ga1693f3584605a0197076cba71c79b0df)#define UBX\_PREAMBLE\_SYNC\_CHAR\_1 0xB5

[ 33](group__modem__ubx.md#gad8d6229db563db619d4f0a9f225fb640)#define UBX\_PREAMBLE\_SYNC\_CHAR\_2 0x62

34

[ 35](group__modem__ubx.md#ga56b16b79385bffdb4a46f1c09b80eb73)#define UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_1\_IDX 0

[ 36](group__modem__ubx.md#gaf72f72cd97e07540452342fdd1868dff)#define UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_2\_IDX 1

[ 37](group__modem__ubx.md#ga258a47c93ef596c2807aaf0e7b810cd0)#define UBX\_FRM\_MSG\_CLASS\_IDX 2

[ 38](group__modem__ubx.md#ga9c2428d2a7867b94638aa2108e23ec55)#define UBX\_FRM\_MSG\_ID\_IDX 3

[ 39](group__modem__ubx.md#ga500d87a31bc1a34cb50997b0d754bf91)#define UBX\_FRM\_PAYLOAD\_SZ\_L\_IDX 4

[ 40](group__modem__ubx.md#gaab0afee791670adfa80410bad0147482)#define UBX\_FRM\_PAYLOAD\_SZ\_H\_IDX 5

[ 41](group__modem__ubx.md#ga0fbb8dfbf14547637c9f5dd4ed9e9762)#define UBX\_FRM\_PAYLOAD\_IDX 6

[ 42](group__modem__ubx.md#gac5f7efa1d5c4bc4b7d9e48a41ad412a2)#define UBX\_FRM\_CHECKSUM\_START\_IDX 2

[ 43](group__modem__ubx.md#gab29f0a6e9d33f39c57b598a75695146f)#define UBX\_FRM\_CHECKSUM\_STOP\_IDX(frame\_len) (frame\_len - 2)

44

[ 45](group__modem__ubx.md#ga9c66cd27732153c56d0872339bc3deae)#define UBX\_PAYLOAD\_SZ\_MAX 256

[ 46](group__modem__ubx.md#gae3aeb2a4570fce67fda95961335ee30c)#define UBX\_FRM\_SZ\_MAX UBX\_FRM\_SZ(UBX\_PAYLOAD\_SZ\_MAX)

47

[ 48](structubx__frame.md)struct [ubx\_frame](structubx__frame.md) {

[ 49](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preamble\_sync\_char\_1](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1);

[ 50](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preamble\_sync\_char\_2](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d);

[ 51](structubx__frame.md#ab0e1094b79fa8ec4ad32a49d6eb58cd7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [message\_class](structubx__frame.md#ab0e1094b79fa8ec4ad32a49d6eb58cd7);

[ 52](structubx__frame.md#aca1010905f7286c6627379a3510ff4d8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [message\_id](structubx__frame.md#aca1010905f7286c6627379a3510ff4d8);

[ 53](structubx__frame.md#aa23a944475ce3926847c267e5463f17f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_size\_low](structubx__frame.md#aa23a944475ce3926847c267e5463f17f);

[ 54](structubx__frame.md#a2f3dda8dff68c4f26ad256453e0302d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_size\_high](structubx__frame.md#a2f3dda8dff68c4f26ad256453e0302d6);

[ 55](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)[];

56};

57

[ 58](structmodem__ubx__script.md)struct [modem\_ubx\_script](structmodem__ubx__script.md) {

[ 59](structmodem__ubx__script.md#adbcef30a46ef38184794e73759430ff8) struct [ubx\_frame](structubx__frame.md) \*[request](structmodem__ubx__script.md#adbcef30a46ef38184794e73759430ff8);

[ 60](structmodem__ubx__script.md#aacb2d50a577f3649d0d081b4b4f5989e) struct [ubx\_frame](structubx__frame.md) \*[response](structmodem__ubx__script.md#aacb2d50a577f3649d0d081b4b4f5989e);

[ 61](structmodem__ubx__script.md#af877497c20b2e67880a8a0051572088b) struct [ubx\_frame](structubx__frame.md) \*[match](structmodem__ubx__script.md#af877497c20b2e67880a8a0051572088b);

62

[ 63](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [retry\_count](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce);

[ 64](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11) [k\_timeout\_t](structk__timeout__t.md) [timeout](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11);

65};

66

[ 67](structmodem__ubx.md)struct [modem\_ubx](structmodem__ubx.md) {

[ 68](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849) void \*[user\_data](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849);

69

[ 70](structmodem__ubx.md#a6d07a9579a24e28b8c55133d9df4c8da) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structmodem__ubx.md#a6d07a9579a24e28b8c55133d9df4c8da);

71

[ 72](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac);

[ 73](structmodem__ubx.md#a4add513db024eb040de858e8901bc017) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__ubx.md#a4add513db024eb040de858e8901bc017);

74

[ 75](structmodem__ubx.md#aad1408bdba802cbf2c98e447c53299dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[work\_buf](structmodem__ubx.md#aad1408bdba802cbf2c98e447c53299dc);

[ 76](structmodem__ubx.md#a2197970808d4b5b5bda78d70d3669a38) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [work\_buf\_size](structmodem__ubx.md#a2197970808d4b5b5bda78d70d3669a38);

[ 77](structmodem__ubx.md#a9a4d782877f3b6e28ca385d438d00837) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [work\_buf\_len](structmodem__ubx.md#a9a4d782877f3b6e28ca385d438d00837);

[ 78](structmodem__ubx.md#a7ad137c9494039cdbc986af00b6e946b) bool [ubx\_preamble\_sync\_chars\_received](structmodem__ubx.md#a7ad137c9494039cdbc986af00b6e946b);

79

[ 80](structmodem__ubx.md#aa62a198023dcc02706f4a653e4eadbe5) const struct [modem\_ubx\_script](structmodem__ubx__script.md) \*[script](structmodem__ubx.md#aa62a198023dcc02706f4a653e4eadbe5);

81

[ 82](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c) struct modem\_pipe \*[pipe](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c);

83

[ 84](structmodem__ubx.md#aedbd81b987524f65c54838ea445bd8fd) struct [k\_work](structk__work.md) [send\_work](structmodem__ubx.md#aedbd81b987524f65c54838ea445bd8fd);

[ 85](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640) struct [k\_work](structk__work.md) [process\_work](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640);

[ 86](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe) struct k\_sem [script\_stopped\_sem](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe);

[ 87](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5) struct k\_sem [script\_running\_sem](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5);

88};

89

[ 90](structmodem__ubx__config.md)struct [modem\_ubx\_config](structmodem__ubx__config.md) {

[ 91](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e) void \*[user\_data](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e);

92

[ 93](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d);

[ 94](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e);

[ 95](structmodem__ubx__config.md#a2fbbde1b0deff7aced238ffe439c9621) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[work\_buf](structmodem__ubx__config.md#a2fbbde1b0deff7aced238ffe439c9621);

[ 96](structmodem__ubx__config.md#ac8504aa7e0154a628ca3ad0b58fa2091) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [work\_buf\_size](structmodem__ubx__config.md#ac8504aa7e0154a628ca3ad0b58fa2091);

97};

98

[ 108](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)int [modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe);

109

[ 115](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)void [modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)(struct [modem\_ubx](structmodem__ubx.md) \*ubx);

116

[ 123](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)int [modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config);

124

[ 152](group__modem__ubx.md#ga25319c784f0293c25c38b494cf9d2a53)int [modem\_ubx\_run\_script](group__modem__ubx.md#ga25319c784f0293c25c38b494cf9d2a53)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script);

153

[ 165](group__modem__ubx.md#ga5d6b36f127836c5b06cde37f098c8775)int [modem\_ubx\_create\_frame](group__modem__ubx.md#ga5d6b36f127836c5b06cde37f098c8775)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ubx\_frame](structubx__frame.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_frame\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_cls,

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_id, const void \*payload, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_size);

170

171#ifdef \_\_cplusplus

172}

173#endif

174

175#endif /\* ZEPHYR\_MODEM\_UBX\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[modem\_ubx\_run\_script](group__modem__ubx.md#ga25319c784f0293c25c38b494cf9d2a53)

int modem\_ubx\_run\_script(struct modem\_ubx \*ubx, const struct modem\_ubx\_script \*script)

Writes the ubx frame in script.request and reads back its response (if available).

[modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)

int modem\_ubx\_attach(struct modem\_ubx \*ubx, struct modem\_pipe \*pipe)

Attach pipe to Modem Ubx.

[modem\_ubx\_create\_frame](group__modem__ubx.md#ga5d6b36f127836c5b06cde37f098c8775)

int modem\_ubx\_create\_frame(uint8\_t \*ubx\_frame, uint16\_t ubx\_frame\_size, uint8\_t msg\_cls, uint8\_t msg\_id, const void \*payload, uint16\_t payload\_size)

Initialize ubx frame.

[modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)

void modem\_ubx\_release(struct modem\_ubx \*ubx)

Release pipe from Modem Ubx instance.

[modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)

int modem\_ubx\_init(struct modem\_ubx \*ubx, const struct modem\_ubx\_config \*config)

Initialize Modem Ubx instance.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[pipe.h](pipe_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3957

[modem\_ubx\_config](structmodem__ubx__config.md)

**Definition** ubx.h:90

[modem\_ubx\_config::work\_buf](structmodem__ubx__config.md#a2fbbde1b0deff7aced238ffe439c9621)

uint8\_t \* work\_buf

**Definition** ubx.h:95

[modem\_ubx\_config::receive\_buf\_size](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e)

uint16\_t receive\_buf\_size

**Definition** ubx.h:94

[modem\_ubx\_config::receive\_buf](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d)

uint8\_t \* receive\_buf

**Definition** ubx.h:93

[modem\_ubx\_config::work\_buf\_size](structmodem__ubx__config.md#ac8504aa7e0154a628ca3ad0b58fa2091)

uint16\_t work\_buf\_size

**Definition** ubx.h:96

[modem\_ubx\_config::user\_data](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e)

void \* user\_data

**Definition** ubx.h:91

[modem\_ubx\_script](structmodem__ubx__script.md)

**Definition** ubx.h:58

[modem\_ubx\_script::timeout](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11)

k\_timeout\_t timeout

**Definition** ubx.h:64

[modem\_ubx\_script::retry\_count](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce)

uint16\_t retry\_count

**Definition** ubx.h:63

[modem\_ubx\_script::response](structmodem__ubx__script.md#aacb2d50a577f3649d0d081b4b4f5989e)

struct ubx\_frame \* response

**Definition** ubx.h:60

[modem\_ubx\_script::request](structmodem__ubx__script.md#adbcef30a46ef38184794e73759430ff8)

struct ubx\_frame \* request

**Definition** ubx.h:59

[modem\_ubx\_script::match](structmodem__ubx__script.md#af877497c20b2e67880a8a0051572088b)

struct ubx\_frame \* match

**Definition** ubx.h:61

[modem\_ubx](structmodem__ubx.md)

**Definition** ubx.h:67

[modem\_ubx::script\_running\_sem](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5)

struct k\_sem script\_running\_sem

**Definition** ubx.h:87

[modem\_ubx::receive\_buf](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac)

uint8\_t \* receive\_buf

**Definition** ubx.h:72

[modem\_ubx::pipe](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c)

struct modem\_pipe \* pipe

**Definition** ubx.h:82

[modem\_ubx::work\_buf\_size](structmodem__ubx.md#a2197970808d4b5b5bda78d70d3669a38)

uint16\_t work\_buf\_size

**Definition** ubx.h:76

[modem\_ubx::receive\_buf\_size](structmodem__ubx.md#a4add513db024eb040de858e8901bc017)

uint16\_t receive\_buf\_size

**Definition** ubx.h:73

[modem\_ubx::state](structmodem__ubx.md#a6d07a9579a24e28b8c55133d9df4c8da)

atomic\_t state

**Definition** ubx.h:70

[modem\_ubx::ubx\_preamble\_sync\_chars\_received](structmodem__ubx.md#a7ad137c9494039cdbc986af00b6e946b)

bool ubx\_preamble\_sync\_chars\_received

**Definition** ubx.h:78

[modem\_ubx::work\_buf\_len](structmodem__ubx.md#a9a4d782877f3b6e28ca385d438d00837)

uint16\_t work\_buf\_len

**Definition** ubx.h:77

[modem\_ubx::script](structmodem__ubx.md#aa62a198023dcc02706f4a653e4eadbe5)

const struct modem\_ubx\_script \* script

**Definition** ubx.h:80

[modem\_ubx::work\_buf](structmodem__ubx.md#aad1408bdba802cbf2c98e447c53299dc)

uint8\_t \* work\_buf

**Definition** ubx.h:75

[modem\_ubx::user\_data](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849)

void \* user\_data

**Definition** ubx.h:68

[modem\_ubx::process\_work](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640)

struct k\_work process\_work

**Definition** ubx.h:85

[modem\_ubx::script\_stopped\_sem](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe)

struct k\_sem script\_stopped\_sem

**Definition** ubx.h:86

[modem\_ubx::send\_work](structmodem__ubx.md#aedbd81b987524f65c54838ea445bd8fd)

struct k\_work send\_work

**Definition** ubx.h:84

[ubx\_frame](structubx__frame.md)

**Definition** ubx.h:48

[ubx\_frame::payload\_size\_high](structubx__frame.md#a2f3dda8dff68c4f26ad256453e0302d6)

uint8\_t payload\_size\_high

**Definition** ubx.h:54

[ubx\_frame::payload\_and\_checksum](structubx__frame.md#a70c465b5bd1e9837c253d78fb210f4ce)

uint8\_t payload\_and\_checksum[]

**Definition** ubx.h:55

[ubx\_frame::payload\_size\_low](structubx__frame.md#aa23a944475ce3926847c267e5463f17f)

uint8\_t payload\_size\_low

**Definition** ubx.h:53

[ubx\_frame::message\_class](structubx__frame.md#ab0e1094b79fa8ec4ad32a49d6eb58cd7)

uint8\_t message\_class

**Definition** ubx.h:51

[ubx\_frame::preamble\_sync\_char\_2](structubx__frame.md#ac61fb72df7c1cd8a9bacb787071cb77d)

uint8\_t preamble\_sync\_char\_2

**Definition** ubx.h:50

[ubx\_frame::message\_id](structubx__frame.md#aca1010905f7286c6627379a3510ff4d8)

uint8\_t message\_id

**Definition** ubx.h:52

[ubx\_frame::preamble\_sync\_char\_1](structubx__frame.md#acf80f38e8f26bb32848ae2978a1f87a1)

uint8\_t preamble\_sync\_char\_1

**Definition** ubx.h:49

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx.h](ubx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
