---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html
original_path: doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h

[Go to the documentation of this file.](mgmt_2mcumgr_2smp_2smp_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

25

26#ifndef H\_SMP\_

27#define H\_SMP\_

28

29#include <[zephyr/net\_buf.h](net__buf_8h.md)>

30#include <[zephyr/mgmt/mcumgr/transport/smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>

31

32#include <zcbor\_common.h>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 39](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed)enum [smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed) {

[ 41](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33) [SMP\_MCUMGR\_VERSION\_1](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33) = 0,

42

[ 44](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a) [SMP\_MCUMGR\_VERSION\_2](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a),

45};

46

[ 47](structcbor__nb__reader.md)struct [cbor\_nb\_reader](structcbor__nb__reader.md) {

[ 48](structcbor__nb__reader.md#a1bfa99724cc6de5d93d88415e5231d09) struct [net\_buf](structnet__buf.md) \*[nb](structcbor__nb__reader.md#a1bfa99724cc6de5d93d88415e5231d09);

49 /\* CONFIG\_MCUMGR\_SMP\_CBOR\_MAX\_DECODING\_LEVELS + 2 translates to minimal

50 \* zcbor backup states.

51 \*/

[ 52](structcbor__nb__reader.md#a7cbec04a9c1fd8a1f8feed0de8d1be1d) zcbor\_state\_t [zs](structcbor__nb__reader.md#a7cbec04a9c1fd8a1f8feed0de8d1be1d)[CONFIG\_MCUMGR\_SMP\_CBOR\_MAX\_DECODING\_LEVELS + 2];

53};

54

[ 55](structcbor__nb__writer.md)struct [cbor\_nb\_writer](structcbor__nb__writer.md) {

[ 56](structcbor__nb__writer.md#af8832d941c69207bc80ed22def5e3125) struct [net\_buf](structnet__buf.md) \*[nb](structcbor__nb__writer.md#af8832d941c69207bc80ed22def5e3125);

[ 57](structcbor__nb__writer.md#a6aa71f361798e61f19e5f0c46cdf1ad5) zcbor\_state\_t [zs](structcbor__nb__writer.md#a6aa71f361798e61f19e5f0c46cdf1ad5)[CONFIG\_MCUMGR\_SMP\_CBOR\_MAX\_ENCODING\_LEVELS + 2];

58

59#if defined(CONFIG\_MCUMGR\_SMP\_SUPPORT\_ORIGINAL\_PROTOCOL)

60 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) error\_group;

61 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) error\_ret;

62#endif

63};

64

[ 71](mgmt_2mcumgr_2smp_2smp_8h.md#ac31c28afe322fb0e9ca49e8a1fb7002b)struct [net\_buf](structnet__buf.md) \*[smp\_packet\_alloc](mgmt_2mcumgr_2smp_2smp_8h.md#ac31c28afe322fb0e9ca49e8a1fb7002b)(void);

72

[ 78](mgmt_2mcumgr_2smp_2smp_8h.md#ad6b5e8c30760366c0e9d6c843605de93)void [smp\_packet\_free](mgmt_2mcumgr_2smp_2smp_8h.md#ad6b5e8c30760366c0e9d6c843605de93)(struct [net\_buf](structnet__buf.md) \*nb);

79

[ 83](structsmp__streamer.md)struct [smp\_streamer](structsmp__streamer.md) {

[ 84](structsmp__streamer.md#a478b0732071a888bd83ccd03bdd51e85) struct [smp\_transport](structsmp__transport.md) \*[smpt](structsmp__streamer.md#a478b0732071a888bd83ccd03bdd51e85);

[ 85](structsmp__streamer.md#ad5f6bcfcea32075ff61afc1b6c4972be) struct [cbor\_nb\_reader](structcbor__nb__reader.md) \*[reader](structsmp__streamer.md#ad5f6bcfcea32075ff61afc1b6c4972be);

[ 86](structsmp__streamer.md#a00f6b8731e1a789939eaec106d746daf) struct [cbor\_nb\_writer](structcbor__nb__writer.md) \*[writer](structsmp__streamer.md#a00f6b8731e1a789939eaec106d746daf);

87

88#ifdef CONFIG\_MCUMGR\_SMP\_VERBOSE\_ERR\_RESPONSE

89 const char \*rc\_rsn;

90#endif

91};

92

[ 107](mgmt_2mcumgr_2smp_2smp_8h.md#a6705014150cda88212d6eb6143d044d4)int [smp\_process\_request\_packet](mgmt_2mcumgr_2smp_2smp_8h.md#a6705014150cda88212d6eb6143d044d4)(struct [smp\_streamer](structsmp__streamer.md) \*streamer, void \*req);

108

[ 122](mgmt_2mcumgr_2smp_2smp_8h.md#a191eb8c8a5a531b158374a1071925ca7)bool [smp\_add\_cmd\_err](mgmt_2mcumgr_2smp_2smp_8h.md#a191eb8c8a5a531b158374a1071925ca7)(zcbor\_state\_t \*zse, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structgroup.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret);

123

124#if defined(CONFIG\_MCUMGR\_SMP\_SUPPORT\_ORIGINAL\_PROTOCOL)

132typedef int (\*smp\_translate\_error\_fn)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) err);

133#endif

134

135#ifdef \_\_cplusplus

136}

137#endif

138

139#endif /\* H\_SMP\_ \*/

[smp\_add\_cmd\_err](mgmt_2mcumgr_2smp_2smp_8h.md#a191eb8c8a5a531b158374a1071925ca7)

bool smp\_add\_cmd\_err(zcbor\_state\_t \*zse, uint16\_t group, uint16\_t ret)

Appends an "err" response.

[smp\_process\_request\_packet](mgmt_2mcumgr_2smp_2smp_8h.md#a6705014150cda88212d6eb6143d044d4)

int smp\_process\_request\_packet(struct smp\_streamer \*streamer, void \*req)

Processes a single SMP request packet and sends all corresponding responses.

[smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed)

smp\_mcumgr\_version\_t

SMP MCUmgr protocol version, part of the SMP header.

**Definition** smp.h:39

[SMP\_MCUMGR\_VERSION\_2](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a)

@ SMP\_MCUMGR\_VERSION\_2

Version 2: adds more detailed error reporting capabilities.

**Definition** smp.h:44

[SMP\_MCUMGR\_VERSION\_1](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33)

@ SMP\_MCUMGR\_VERSION\_1

Version 1: the original protocol.

**Definition** smp.h:41

[smp\_packet\_alloc](mgmt_2mcumgr_2smp_2smp_8h.md#ac31c28afe322fb0e9ca49e8a1fb7002b)

struct net\_buf \* smp\_packet\_alloc(void)

Allocates a net\_buf for holding an mcumgr request or response.

[smp\_packet\_free](mgmt_2mcumgr_2smp_2smp_8h.md#ad6b5e8c30760366c0e9d6c843605de93)

void smp\_packet\_free(struct net\_buf \*nb)

Frees an mcumgr net\_buf.

[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[cbor\_nb\_reader](structcbor__nb__reader.md)

**Definition** smp.h:47

[cbor\_nb\_reader::nb](structcbor__nb__reader.md#a1bfa99724cc6de5d93d88415e5231d09)

struct net\_buf \* nb

**Definition** smp.h:48

[cbor\_nb\_reader::zs](structcbor__nb__reader.md#a7cbec04a9c1fd8a1f8feed0de8d1be1d)

zcbor\_state\_t zs[CONFIG\_MCUMGR\_SMP\_CBOR\_MAX\_DECODING\_LEVELS+2]

**Definition** smp.h:52

[cbor\_nb\_writer](structcbor__nb__writer.md)

**Definition** smp.h:55

[cbor\_nb\_writer::zs](structcbor__nb__writer.md#a6aa71f361798e61f19e5f0c46cdf1ad5)

zcbor\_state\_t zs[CONFIG\_MCUMGR\_SMP\_CBOR\_MAX\_ENCODING\_LEVELS+2]

**Definition** smp.h:57

[cbor\_nb\_writer::nb](structcbor__nb__writer.md#af8832d941c69207bc80ed22def5e3125)

struct net\_buf \* nb

**Definition** smp.h:56

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[smp\_streamer](structsmp__streamer.md)

Decodes, encodes, and transmits SMP packets.

**Definition** smp.h:83

[smp\_streamer::writer](structsmp__streamer.md#a00f6b8731e1a789939eaec106d746daf)

struct cbor\_nb\_writer \* writer

**Definition** smp.h:86

[smp\_streamer::smpt](structsmp__streamer.md#a478b0732071a888bd83ccd03bdd51e85)

struct smp\_transport \* smpt

**Definition** smp.h:84

[smp\_streamer::reader](structsmp__streamer.md#ad5f6bcfcea32075ff61afc1b6c4972be)

struct cbor\_nb\_reader \* reader

**Definition** smp.h:85

[smp\_transport](structsmp__transport.md)

SMP transport object for sending SMP responses.

**Definition** smp.h:118

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [smp](dir_e62cfe388532d436a5daefec152a780b.md)
- [smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
