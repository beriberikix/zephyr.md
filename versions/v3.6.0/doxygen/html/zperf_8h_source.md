---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/zperf_8h_source.html
original_path: doxygen/html/zperf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

16

17#ifndef ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_

18#define ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_

19

20#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 26](group__zperf.md#ga073cc81d6fd201d09e7d1e712927f7cb)enum [zperf\_status](group__zperf.md#ga073cc81d6fd201d09e7d1e712927f7cb) {

[ 27](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba837674d9cb7309c80bf4dac2446667d8) [ZPERF\_SESSION\_STARTED](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba837674d9cb7309c80bf4dac2446667d8),

[ 28](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba230ffe541f46d28b19ce4ed66b5f9607) [ZPERF\_SESSION\_FINISHED](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba230ffe541f46d28b19ce4ed66b5f9607),

[ 29](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba6e2f47cdc1e2b67eede67a378ee5ed95) [ZPERF\_SESSION\_ERROR](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba6e2f47cdc1e2b67eede67a378ee5ed95)

30} \_\_packed;

31

[ 32](structzperf__upload__params.md)struct [zperf\_upload\_params](structzperf__upload__params.md) {

[ 33](structzperf__upload__params.md#a78307a038b6a4fb02c8d89387a20b29c) struct [sockaddr](structsockaddr.md) [peer\_addr](structzperf__upload__params.md#a78307a038b6a4fb02c8d89387a20b29c);

[ 34](structzperf__upload__params.md#ac6f7bb4aa70c20d70d8644d647ad5b0f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration\_ms](structzperf__upload__params.md#ac6f7bb4aa70c20d70d8644d647ad5b0f);

[ 35](structzperf__upload__params.md#ab639ac94ca20c742114fa5e7bb89df4b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rate\_kbps](structzperf__upload__params.md#ab639ac94ca20c742114fa5e7bb89df4b);

[ 36](structzperf__upload__params.md#a7815d9556cab97fb87742922663a5daf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [packet\_size](structzperf__upload__params.md#a7815d9556cab97fb87742922663a5daf);

37 struct {

[ 38](structzperf__upload__params.md#afe1767e2c82ffe7e014a75b4ad833cb0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tos](structzperf__upload__params.md#afe1767e2c82ffe7e014a75b4ad833cb0);

[ 39](structzperf__upload__params.md#a5a48be96c6b537c54dc500a28a3d307e) int [tcp\_nodelay](structzperf__upload__params.md#a5a48be96c6b537c54dc500a28a3d307e);

[ 40](structzperf__upload__params.md#a90ce9f0e4e2526104ea4dd2837bc059b) int [priority](structzperf__upload__params.md#a90ce9f0e4e2526104ea4dd2837bc059b);

[ 41](structzperf__upload__params.md#a7b453046c1c682941de34714cafc2fb6) } [options](structzperf__upload__params.md#a7b453046c1c682941de34714cafc2fb6);

42};

43

[ 44](structzperf__download__params.md)struct [zperf\_download\_params](structzperf__download__params.md) {

[ 45](structzperf__download__params.md#a0ea16f56e1d866f05f50935df2690f14) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port](structzperf__download__params.md#a0ea16f56e1d866f05f50935df2690f14);

[ 46](structzperf__download__params.md#a92e0a7d21f1a88933a9ec95fda71c84b) struct [sockaddr](structsockaddr.md) [addr](structzperf__download__params.md#a92e0a7d21f1a88933a9ec95fda71c84b);

47};

48

[ 49](structzperf__results.md)struct [zperf\_results](structzperf__results.md) {

[ 50](structzperf__results.md#adfd2738991c8bea53f20079421da6d96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_sent](structzperf__results.md#adfd2738991c8bea53f20079421da6d96);

[ 51](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_rcvd](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70);

[ 52](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_lost](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8);

[ 53](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_outorder](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1);

[ 54](structzperf__results.md#adf3ffbebe76def1730d2371307557d96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [total\_len](structzperf__results.md#adf3ffbebe76def1730d2371307557d96);

[ 55](structzperf__results.md#a03844123e3a1caf390f82cf924528c59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [time\_in\_us](structzperf__results.md#a03844123e3a1caf390f82cf924528c59);

[ 56](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [jitter\_in\_us](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2);

[ 57](structzperf__results.md#adc99d5b92704198b0a82fd6aad443d26) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [client\_time\_in\_us](structzperf__results.md#adc99d5b92704198b0a82fd6aad443d26);

[ 58](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [packet\_size](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28);

[ 59](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_packets\_errors](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8);

60};

61

[ 69](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b)typedef void (\*[zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b))(enum [zperf\_status](group__zperf.md#ga073cc81d6fd201d09e7d1e712927f7cb) status,

70 struct [zperf\_results](structzperf__results.md) \*result,

71 void \*user\_data);

72

[ 82](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e)int [zperf\_udp\_upload](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e)(const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param,

83 struct [zperf\_results](structzperf__results.md) \*result);

84

[ 94](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44)int [zperf\_tcp\_upload](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44)(const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param,

95 struct [zperf\_results](structzperf__results.md) \*result);

96

[ 109](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd)int [zperf\_udp\_upload\_async](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd)(const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param,

110 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

111

[ 124](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35)int [zperf\_tcp\_upload\_async](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35)(const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param,

125 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

126

[ 138](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a)int [zperf\_udp\_download](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a)(const struct [zperf\_download\_params](structzperf__download__params.md) \*param,

139 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

140

[ 152](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d)int [zperf\_tcp\_download](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d)(const struct [zperf\_download\_params](structzperf__download__params.md) \*param,

153 [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data);

154

[ 160](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf)int [zperf\_udp\_download\_stop](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf)(void);

161

[ 167](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a)int [zperf\_tcp\_download\_stop](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a)(void);

168

169#ifdef \_\_cplusplus

170}

171#endif

172

176

177#endif /\* ZEPHYR\_INCLUDE\_NET\_ZPERF\_H\_ \*/

[zperf\_status](group__zperf.md#ga073cc81d6fd201d09e7d1e712927f7cb)

zperf\_status

**Definition** zperf.h:26

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

**Definition** zperf.h:69

[ZPERF\_SESSION\_FINISHED](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba230ffe541f46d28b19ce4ed66b5f9607)

@ ZPERF\_SESSION\_FINISHED

**Definition** zperf.h:28

[ZPERF\_SESSION\_ERROR](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba6e2f47cdc1e2b67eede67a378ee5ed95)

@ ZPERF\_SESSION\_ERROR

**Definition** zperf.h:29

[ZPERF\_SESSION\_STARTED](group__zperf.md#gga073cc81d6fd201d09e7d1e712927f7cba837674d9cb7309c80bf4dac2446667d8)

@ ZPERF\_SESSION\_STARTED

**Definition** zperf.h:27

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[zperf\_download\_params](structzperf__download__params.md)

**Definition** zperf.h:44

[zperf\_download\_params::port](structzperf__download__params.md#a0ea16f56e1d866f05f50935df2690f14)

uint16\_t port

**Definition** zperf.h:45

[zperf\_download\_params::addr](structzperf__download__params.md#a92e0a7d21f1a88933a9ec95fda71c84b)

struct sockaddr addr

**Definition** zperf.h:46

[zperf\_results](structzperf__results.md)

**Definition** zperf.h:49

[zperf\_results::time\_in\_us](structzperf__results.md#a03844123e3a1caf390f82cf924528c59)

uint32\_t time\_in\_us

**Definition** zperf.h:55

[zperf\_results::nb\_packets\_errors](structzperf__results.md#a5fcccf6747c449418c246ac1d945a1f8)

uint32\_t nb\_packets\_errors

**Definition** zperf.h:59

[zperf\_results::packet\_size](structzperf__results.md#a8aedf97a8eeace1f4b9cda7e07e17e28)

uint32\_t packet\_size

**Definition** zperf.h:58

[zperf\_results::nb\_packets\_outorder](structzperf__results.md#aa1e3c86bcab447bc888bba0bbaa057d1)

uint32\_t nb\_packets\_outorder

**Definition** zperf.h:53

[zperf\_results::nb\_packets\_lost](structzperf__results.md#ac9ad68ef3b6081b64f290720ad9b5bc8)

uint32\_t nb\_packets\_lost

**Definition** zperf.h:52

[zperf\_results::nb\_packets\_rcvd](structzperf__results.md#acf312d831d8e6707f7e769da92f8eb70)

uint32\_t nb\_packets\_rcvd

**Definition** zperf.h:51

[zperf\_results::client\_time\_in\_us](structzperf__results.md#adc99d5b92704198b0a82fd6aad443d26)

uint32\_t client\_time\_in\_us

**Definition** zperf.h:57

[zperf\_results::total\_len](structzperf__results.md#adf3ffbebe76def1730d2371307557d96)

uint32\_t total\_len

**Definition** zperf.h:54

[zperf\_results::nb\_packets\_sent](structzperf__results.md#adfd2738991c8bea53f20079421da6d96)

uint32\_t nb\_packets\_sent

**Definition** zperf.h:50

[zperf\_results::jitter\_in\_us](structzperf__results.md#af4a5ce512fb37ddae8e2c12a0b67c3a2)

uint32\_t jitter\_in\_us

**Definition** zperf.h:56

[zperf\_upload\_params](structzperf__upload__params.md)

**Definition** zperf.h:32

[zperf\_upload\_params::tcp\_nodelay](structzperf__upload__params.md#a5a48be96c6b537c54dc500a28a3d307e)

int tcp\_nodelay

**Definition** zperf.h:39

[zperf\_upload\_params::packet\_size](structzperf__upload__params.md#a7815d9556cab97fb87742922663a5daf)

uint16\_t packet\_size

**Definition** zperf.h:36

[zperf\_upload\_params::peer\_addr](structzperf__upload__params.md#a78307a038b6a4fb02c8d89387a20b29c)

struct sockaddr peer\_addr

**Definition** zperf.h:33

[zperf\_upload\_params::options](structzperf__upload__params.md#a7b453046c1c682941de34714cafc2fb6)

struct zperf\_upload\_params::@360066372052226261354235375020002165114162105265 options

[zperf\_upload\_params::priority](structzperf__upload__params.md#a90ce9f0e4e2526104ea4dd2837bc059b)

int priority

**Definition** zperf.h:40

[zperf\_upload\_params::rate\_kbps](structzperf__upload__params.md#ab639ac94ca20c742114fa5e7bb89df4b)

uint32\_t rate\_kbps

**Definition** zperf.h:35

[zperf\_upload\_params::duration\_ms](structzperf__upload__params.md#ac6f7bb4aa70c20d70d8644d647ad5b0f)

uint32\_t duration\_ms

**Definition** zperf.h:34

[zperf\_upload\_params::tos](structzperf__upload__params.md#afe1767e2c82ffe7e014a75b4ad833cb0)

uint8\_t tos

**Definition** zperf.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [zperf.h](zperf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
