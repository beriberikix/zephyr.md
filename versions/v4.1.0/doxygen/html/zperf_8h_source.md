---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zperf_8h_source.html
original_path: doxygen/html/zperf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zperf.h

[Go to the documentation of this file.](zperf_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \* Copyright (c) 2022 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

18

19#ifndef ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_

20#define ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_

21

22#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

23#include <[zephyr/net/socket.h](net_2socket_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

30

31enum zperf\_status {

32 ZPERF\_SESSION\_STARTED,

33 ZPERF\_SESSION\_PERIODIC\_RESULT,

34 ZPERF\_SESSION\_FINISHED,

35 ZPERF\_SESSION\_ERROR

36} \_\_packed;

37

38struct zperf\_upload\_params {

39 struct sockaddr peer\_addr;

40 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) duration\_ms;

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rate\_kbps;

42 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) packet\_size;

43 char if\_name[[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)];

44 struct {

45 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tos;

46 int tcp\_nodelay;

47 int priority;

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) report\_interval\_ms;

49 } options;

50};

51

52struct zperf\_download\_params {

53 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port;

54 struct sockaddr addr;

55 char if\_name[[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)];

56};

57

59

[ 61](structzperf__results.md)struct [zperf\_results](structzperf__results.md) {

[ 62](structzperf__results.md#adfd2738991c8bea53f20079421da6d96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_sent](structzperf__results.md#adfd2738991c8bea53f20079421da6d96);

[ 63](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_rcvd](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70);

[ 64](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_lost](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8);

[ 65](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_outorder](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1);

[ 66](structzperf__results.md#a517ba180a6414a2f2d1484e698d57650) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [total\_len](structzperf__results.md#a517ba180a6414a2f2d1484e698d57650);

[ 67](structzperf__results.md#aafb7f2c221c91c59ab0d6936ebc6ce2a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [time\_in\_us](structzperf__results.md#aafb7f2c221c91c59ab0d6936ebc6ce2a);

[ 68](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [jitter\_in\_us](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2);

[ 69](structzperf__results.md#a550158fd641799c2a6b2d25617ac9a6c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [client\_time\_in\_us](structzperf__results.md#a550158fd641799c2a6b2d25617ac9a6c);

[ 70](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [packet\_size](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28);

[ 71](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_errors](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8);

72};

73

[ 81](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b)typedef void (\*[zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b))(enum zperf\_status status,

82 struct [zperf\_results](structzperf__results.md) \*result,

83 void \*user\_data);

84

[ 94](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e)int [zperf\_udp\_upload](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e)(const struct zperf\_upload\_params \*param,

95 struct [zperf\_results](structzperf__results.md) \*result);

96

[ 106](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44)int [zperf\_tcp\_upload](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44)(const struct zperf\_upload\_params \*param,

107 struct [zperf\_results](structzperf__results.md) \*result);

108

[ 121](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd)int [zperf\_udp\_upload\_async](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd)(const struct zperf\_upload\_params \*param,

122 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

123

[ 136](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35)int [zperf\_tcp\_upload\_async](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35)(const struct zperf\_upload\_params \*param,

137 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

138

[ 150](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a)int [zperf\_udp\_download](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a)(const struct zperf\_download\_params \*param,

151 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

152

[ 164](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d)int [zperf\_tcp\_download](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d)(const struct zperf\_download\_params \*param,

165 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

166

[ 172](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf)int [zperf\_udp\_download\_stop](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf)(void);

173

[ 179](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a)int [zperf\_tcp\_download\_stop](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a)(void);

180

181#ifdef \_\_cplusplus

182}

183#endif

184

188

189#endif /\* ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_ \*/

[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)

#define IFNAMSIZ

Network interface name length.

**Definition** socket.h:815

[zperf\_tcp\_upload\_async](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35)

int zperf\_tcp\_upload\_async(const struct zperf\_upload\_params \*param, zperf\_callback callback, void \*user\_data)

Asynchronous TCP upload operation.

[zperf\_tcp\_upload](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44)

int zperf\_tcp\_upload(const struct zperf\_upload\_params \*param, struct zperf\_results \*result)

Synchronous TCP upload operation.

[zperf\_udp\_download\_stop](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf)

int zperf\_udp\_download\_stop(void)

Stop UDP server.

[zperf\_udp\_upload](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e)

int zperf\_udp\_upload(const struct zperf\_upload\_params \*param, struct zperf\_results \*result)

Synchronous UDP upload operation.

[zperf\_tcp\_download](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d)

int zperf\_tcp\_download(const struct zperf\_download\_params \*param, zperf\_callback callback, void \*user\_data)

Start TCP server.

[zperf\_udp\_download](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a)

int zperf\_udp\_download(const struct zperf\_download\_params \*param, zperf\_callback callback, void \*user\_data)

Start UDP server.

[zperf\_tcp\_download\_stop](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a)

int zperf\_tcp\_download\_stop(void)

Stop TCP server.

[zperf\_udp\_upload\_async](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd)

int zperf\_udp\_upload\_async(const struct zperf\_upload\_params \*param, zperf\_callback callback, void \*user\_data)

Asynchronous UDP upload operation.

[zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b)

void(\* zperf\_callback)(enum zperf\_status status, struct zperf\_results \*result, void \*user\_data)

Zperf callback function used for asynchronous operations.

**Definition** zperf.h:81

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[zperf\_results](structzperf__results.md)

Performance results.

**Definition** zperf.h:61

[zperf\_results::total\_len](structzperf__results.md#a517ba180a6414a2f2d1484e698d57650)

uint64\_t total\_len

Total length of the transferred data.

**Definition** zperf.h:66

[zperf\_results::client\_time\_in\_us](structzperf__results.md#a550158fd641799c2a6b2d25617ac9a6c)

uint64\_t client\_time\_in\_us

Client connection time in microseconds.

**Definition** zperf.h:69

[zperf\_results::nb\_packets\_errors](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8)

uint32\_t nb\_packets\_errors

Number of packet errors.

**Definition** zperf.h:71

[zperf\_results::packet\_size](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28)

uint32\_t packet\_size

Packet size.

**Definition** zperf.h:70

[zperf\_results::nb\_packets\_outorder](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1)

uint32\_t nb\_packets\_outorder

Number of packets out of order.

**Definition** zperf.h:65

[zperf\_results::time\_in\_us](structzperf__results.md#aafb7f2c221c91c59ab0d6936ebc6ce2a)

uint64\_t time\_in\_us

Total time of the transfer in microseconds.

**Definition** zperf.h:67

[zperf\_results::nb\_packets\_lost](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8)

uint32\_t nb\_packets\_lost

Number of packets lost.

**Definition** zperf.h:64

[zperf\_results::nb\_packets\_rcvd](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70)

uint32\_t nb\_packets\_rcvd

Number of packets received.

**Definition** zperf.h:63

[zperf\_results::nb\_packets\_sent](structzperf__results.md#adfd2738991c8bea53f20079421da6d96)

uint32\_t nb\_packets\_sent

Number of packets sent.

**Definition** zperf.h:62

[zperf\_results::jitter\_in\_us](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2)

uint32\_t jitter\_in\_us

Jitter in microseconds.

**Definition** zperf.h:68

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [zperf.h](zperf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
