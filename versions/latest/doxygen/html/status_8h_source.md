---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/status_8h_source.html
original_path: doxygen/html/status_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

status.h

[Go to the documentation of this file.](status_8h.md)

1

4

5/\*

6 \* Copyright (c) 2022 Meta

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_STATUS\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_HTTP\_STATUS\_H\_

13

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 34](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d)enum [http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d) {

[ 35](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882) [HTTP\_100\_CONTINUE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882) = 100,

[ 36](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5) [HTTP\_101\_SWITCHING\_PROTOCOLS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5) = 101,

[ 37](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af) [HTTP\_102\_PROCESSING](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af) = 102,

[ 38](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0) [HTTP\_103\_EARLY\_HINTS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0) = 103,

[ 39](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9) [HTTP\_200\_OK](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9) = 200,

[ 40](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a) [HTTP\_201\_CREATED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a) = 201,

[ 41](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9) [HTTP\_202\_ACCEPTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9) = 202,

[ 42](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce) [HTTP\_203\_NON\_AUTHORITATIVE\_INFORMATION](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce) = 203,

[ 43](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93) [HTTP\_204\_NO\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93) = 204,

[ 44](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255) [HTTP\_205\_RESET\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255) = 205,

[ 45](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2) [HTTP\_206\_PARTIAL\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2) = 206,

[ 46](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d) [HTTP\_207\_MULTI\_STATUS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d) = 207,

[ 47](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f) [HTTP\_208\_ALREADY\_REPORTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f) = 208,

[ 48](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b) [HTTP\_226\_IM\_USED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b) = 226,

[ 49](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435) [HTTP\_300\_MULTIPLE\_CHOICES](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435) = 300,

[ 50](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f) [HTTP\_301\_MOVED\_PERMANENTLY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f) = 301,

[ 51](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc) [HTTP\_302\_FOUND](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc) = 302,

[ 52](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51) [HTTP\_303\_SEE\_OTHER](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51) = 303,

[ 53](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8) [HTTP\_304\_NOT\_MODIFIED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8) = 304,

[ 54](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa) [HTTP\_305\_USE\_PROXY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa) = 305,

[ 55](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981) [HTTP\_306\_UNUSED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981) = 306,

[ 56](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7) [HTTP\_307\_TEMPORARY\_REDIRECT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7) = 307,

[ 57](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416) [HTTP\_308\_PERMANENT\_REDIRECT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416) = 308,

[ 58](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c) [HTTP\_400\_BAD\_REQUEST](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c) = 400,

[ 59](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113) [HTTP\_401\_UNAUTHORIZED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113) = 401,

[ 60](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b) [HTTP\_402\_PAYMENT\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b) = 402,

[ 61](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00) [HTTP\_403\_FORBIDDEN](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00) = 403,

[ 62](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875) [HTTP\_404\_NOT\_FOUND](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875) = 404,

[ 63](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163) [HTTP\_405\_METHOD\_NOT\_ALLOWED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163) = 405,

[ 64](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0) [HTTP\_406\_NOT\_ACCEPTABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0) = 406,

[ 65](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4) [HTTP\_407\_PROXY\_AUTHENTICATION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4) = 407,

[ 66](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01) [HTTP\_408\_REQUEST\_TIMEOUT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01) = 408,

[ 67](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50) [HTTP\_409\_CONFLICT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50) = 409,

[ 68](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444) [HTTP\_410\_GONE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444) = 410,

[ 69](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93) [HTTP\_411\_LENGTH\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93) = 411,

[ 70](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5) [HTTP\_412\_PRECONDITION\_FAILED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5) = 412,

[ 71](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35) [HTTP\_413\_PAYLOAD\_TOO\_LARGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35) = 413,

[ 72](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807) [HTTP\_414\_URI\_TOO\_LONG](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807) = 414,

[ 73](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd) [HTTP\_415\_UNSUPPORTED\_MEDIA\_TYPE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd) = 415,

[ 74](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095) [HTTP\_416\_RANGE\_NOT\_SATISFIABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095) = 416,

[ 75](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae) [HTTP\_417\_EXPECTATION\_FAILED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae) = 417,

[ 76](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762) [HTTP\_418\_IM\_A\_TEAPOT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762) = 418,

[ 77](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b) [HTTP\_421\_MISDIRECTED\_REQUEST](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b) = 421,

[ 78](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8) [HTTP\_422\_UNPROCESSABLE\_ENTITY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8) = 422,

[ 79](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7) [HTTP\_423\_LOCKED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7) = 423,

[ 80](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3) [HTTP\_424\_FAILED\_DEPENDENCY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3) = 424,

[ 81](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc) [HTTP\_425\_TOO\_EARLY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc) = 425,

[ 82](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2) [HTTP\_426\_UPGRADE\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2) = 426,

[ 83](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98) [HTTP\_428\_PRECONDITION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98) = 428,

[ 84](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e) [HTTP\_429\_TOO\_MANY\_REQUESTS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e) = 429,

[ 85](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14) [HTTP\_431\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14) = 431,

[ 86](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1) [HTTP\_451\_UNAVAILABLE\_FOR\_LEGAL\_REASONS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1) = 451,

[ 87](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4) [HTTP\_500\_INTERNAL\_SERVER\_ERROR](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4) = 500,

[ 88](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b) [HTTP\_501\_NOT\_IMPLEMENTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b) = 501,

[ 89](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375) [HTTP\_502\_BAD\_GATEWAY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375) = 502,

[ 90](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d) [HTTP\_503\_SERVICE\_UNAVAILABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d) = 503,

[ 91](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71) [HTTP\_504\_GATEWAY\_TIMEOUT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71) = 504,

[ 92](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419) [HTTP\_505\_HTTP\_VERSION\_NOT\_SUPPORTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419) = 505,

[ 93](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e) [HTTP\_506\_VARIANT\_ALSO\_NEGOTIATES](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e) = 506,

[ 94](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97) [HTTP\_507\_INSUFFICIENT\_STORAGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97) = 507,

[ 95](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45) [HTTP\_508\_LOOP\_DETECTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45) = 508,

[ 96](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb) [HTTP\_510\_NOT\_EXTENDED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb) = 510,

[ 97](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a) [HTTP\_511\_NETWORK\_AUTHENTICATION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a) = 511,

98};

99

100#ifdef \_\_cplusplus

101}

102#endif

103

107

108#endif

[http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d)

http\_status

HTTP response status codes.

**Definition** status.h:34

[HTTP\_403\_FORBIDDEN](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00)

@ HTTP\_403\_FORBIDDEN

Forbidden.

**Definition** status.h:61

[HTTP\_201\_CREATED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a)

@ HTTP\_201\_CREATED

Created.

**Definition** status.h:40

[HTTP\_423\_LOCKED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7)

@ HTTP\_423\_LOCKED

Locked.

**Definition** status.h:79

[HTTP\_406\_NOT\_ACCEPTABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0)

@ HTTP\_406\_NOT\_ACCEPTABLE

Not Acceptable.

**Definition** status.h:64

[HTTP\_424\_FAILED\_DEPENDENCY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3)

@ HTTP\_424\_FAILED\_DEPENDENCY

Failed Dependency.

**Definition** status.h:80

[HTTP\_305\_USE\_PROXY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa)

@ HTTP\_305\_USE\_PROXY

Use Proxy.

**Definition** status.h:54

[HTTP\_207\_MULTI\_STATUS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d)

@ HTTP\_207\_MULTI\_STATUS

Multi-Status.

**Definition** status.h:46

[HTTP\_409\_CONFLICT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50)

@ HTTP\_409\_CONFLICT

Conflict.

**Definition** status.h:67

[HTTP\_431\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14)

@ HTTP\_431\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE

Request Header Fields Too Large.

**Definition** status.h:85

[HTTP\_413\_PAYLOAD\_TOO\_LARGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35)

@ HTTP\_413\_PAYLOAD\_TOO\_LARGE

Payload Too Large.

**Definition** status.h:71

[HTTP\_203\_NON\_AUTHORITATIVE\_INFORMATION](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce)

@ HTTP\_203\_NON\_AUTHORITATIVE\_INFORMATION

Non-Authoritative Information.

**Definition** status.h:42

[HTTP\_408\_REQUEST\_TIMEOUT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01)

@ HTTP\_408\_REQUEST\_TIMEOUT

Request Timeout.

**Definition** status.h:66

[HTTP\_102\_PROCESSING](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af)

@ HTTP\_102\_PROCESSING

Processing.

**Definition** status.h:37

[HTTP\_307\_TEMPORARY\_REDIRECT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7)

@ HTTP\_307\_TEMPORARY\_REDIRECT

Temporary Redirect.

**Definition** status.h:56

[HTTP\_502\_BAD\_GATEWAY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375)

@ HTTP\_502\_BAD\_GATEWAY

Bad Gateway.

**Definition** status.h:89

[HTTP\_412\_PRECONDITION\_FAILED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5)

@ HTTP\_412\_PRECONDITION\_FAILED

Precondition Failed.

**Definition** status.h:70

[HTTP\_308\_PERMANENT\_REDIRECT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416)

@ HTTP\_308\_PERMANENT\_REDIRECT

Permanent Redirect.

**Definition** status.h:57

[HTTP\_510\_NOT\_EXTENDED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb)

@ HTTP\_510\_NOT\_EXTENDED

Not Extended.

**Definition** status.h:96

[HTTP\_426\_UPGRADE\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2)

@ HTTP\_426\_UPGRADE\_REQUIRED

Upgrade Required.

**Definition** status.h:82

[HTTP\_400\_BAD\_REQUEST](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c)

@ HTTP\_400\_BAD\_REQUEST

Bad Request.

**Definition** status.h:58

[HTTP\_418\_IM\_A\_TEAPOT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762)

@ HTTP\_418\_IM\_A\_TEAPOT

I'm a teapot.

**Definition** status.h:76

[HTTP\_501\_NOT\_IMPLEMENTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b)

@ HTTP\_501\_NOT\_IMPLEMENTED

Not Implemented.

**Definition** status.h:88

[HTTP\_422\_UNPROCESSABLE\_ENTITY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8)

@ HTTP\_422\_UNPROCESSABLE\_ENTITY

Unprocessable Entity.

**Definition** status.h:78

[HTTP\_416\_RANGE\_NOT\_SATISFIABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095)

@ HTTP\_416\_RANGE\_NOT\_SATISFIABLE

Range Not Satisfiable.

**Definition** status.h:74

[HTTP\_204\_NO\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93)

@ HTTP\_204\_NO\_CONTENT

No Content.

**Definition** status.h:43

[HTTP\_410\_GONE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444)

@ HTTP\_410\_GONE

Gone.

**Definition** status.h:68

[HTTP\_504\_GATEWAY\_TIMEOUT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71)

@ HTTP\_504\_GATEWAY\_TIMEOUT

Gateway Timeout.

**Definition** status.h:91

[HTTP\_101\_SWITCHING\_PROTOCOLS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5)

@ HTTP\_101\_SWITCHING\_PROTOCOLS

Switching Protocols.

**Definition** status.h:36

[HTTP\_202\_ACCEPTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9)

@ HTTP\_202\_ACCEPTED

Accepted.

**Definition** status.h:41

[HTTP\_304\_NOT\_MODIFIED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8)

@ HTTP\_304\_NOT\_MODIFIED

Not Modified.

**Definition** status.h:53

[HTTP\_429\_TOO\_MANY\_REQUESTS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e)

@ HTTP\_429\_TOO\_MANY\_REQUESTS

Too Many Requests.

**Definition** status.h:84

[HTTP\_206\_PARTIAL\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2)

@ HTTP\_206\_PARTIAL\_CONTENT

Partial Content.

**Definition** status.h:45

[HTTP\_503\_SERVICE\_UNAVAILABLE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d)

@ HTTP\_503\_SERVICE\_UNAVAILABLE

Service Unavailable.

**Definition** status.h:90

[HTTP\_405\_METHOD\_NOT\_ALLOWED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163)

@ HTTP\_405\_METHOD\_NOT\_ALLOWED

Method Not Allowed.

**Definition** status.h:63

[HTTP\_306\_UNUSED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981)

@ HTTP\_306\_UNUSED

unused

**Definition** status.h:55

[HTTP\_226\_IM\_USED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b)

@ HTTP\_226\_IM\_USED

IM Used.

**Definition** status.h:48

[HTTP\_200\_OK](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9)

@ HTTP\_200\_OK

OK.

**Definition** status.h:39

[HTTP\_508\_LOOP\_DETECTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45)

@ HTTP\_508\_LOOP\_DETECTED

Loop Detected.

**Definition** status.h:95

[HTTP\_421\_MISDIRECTED\_REQUEST](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b)

@ HTTP\_421\_MISDIRECTED\_REQUEST

Misdirected Request.

**Definition** status.h:77

[HTTP\_505\_HTTP\_VERSION\_NOT\_SUPPORTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419)

@ HTTP\_505\_HTTP\_VERSION\_NOT\_SUPPORTED

HTTP Version Not Supported.

**Definition** status.h:92

[HTTP\_301\_MOVED\_PERMANENTLY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f)

@ HTTP\_301\_MOVED\_PERMANENTLY

Moved Permanently.

**Definition** status.h:50

[HTTP\_404\_NOT\_FOUND](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875)

@ HTTP\_404\_NOT\_FOUND

Not Found.

**Definition** status.h:62

[HTTP\_208\_ALREADY\_REPORTED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f)

@ HTTP\_208\_ALREADY\_REPORTED

Already Reported.

**Definition** status.h:47

[HTTP\_103\_EARLY\_HINTS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0)

@ HTTP\_103\_EARLY\_HINTS

Early Hints.

**Definition** status.h:38

[HTTP\_417\_EXPECTATION\_FAILED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae)

@ HTTP\_417\_EXPECTATION\_FAILED

Expectation Failed.

**Definition** status.h:75

[HTTP\_302\_FOUND](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc)

@ HTTP\_302\_FOUND

Found.

**Definition** status.h:51

[HTTP\_428\_PRECONDITION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98)

@ HTTP\_428\_PRECONDITION\_REQUIRED

Precondition Required.

**Definition** status.h:83

[HTTP\_506\_VARIANT\_ALSO\_NEGOTIATES](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e)

@ HTTP\_506\_VARIANT\_ALSO\_NEGOTIATES

Variant Also Negotiates.

**Definition** status.h:93

[HTTP\_300\_MULTIPLE\_CHOICES](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435)

@ HTTP\_300\_MULTIPLE\_CHOICES

Multiple Choices.

**Definition** status.h:49

[HTTP\_425\_TOO\_EARLY](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc)

@ HTTP\_425\_TOO\_EARLY

Too Early.

**Definition** status.h:81

[HTTP\_507\_INSUFFICIENT\_STORAGE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97)

@ HTTP\_507\_INSUFFICIENT\_STORAGE

Insufficient Storage.

**Definition** status.h:94

[HTTP\_407\_PROXY\_AUTHENTICATION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4)

@ HTTP\_407\_PROXY\_AUTHENTICATION\_REQUIRED

Proxy Authentication Required.

**Definition** status.h:65

[HTTP\_100\_CONTINUE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882)

@ HTTP\_100\_CONTINUE

Continue.

**Definition** status.h:35

[HTTP\_303\_SEE\_OTHER](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51)

@ HTTP\_303\_SEE\_OTHER

See Other.

**Definition** status.h:52

[HTTP\_511\_NETWORK\_AUTHENTICATION\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a)

@ HTTP\_511\_NETWORK\_AUTHENTICATION\_REQUIRED

Network Authentication Required.

**Definition** status.h:97

[HTTP\_414\_URI\_TOO\_LONG](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807)

@ HTTP\_414\_URI\_TOO\_LONG

URI Too Long.

**Definition** status.h:72

[HTTP\_415\_UNSUPPORTED\_MEDIA\_TYPE](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd)

@ HTTP\_415\_UNSUPPORTED\_MEDIA\_TYPE

Unsupported Media Type.

**Definition** status.h:73

[HTTP\_411\_LENGTH\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93)

@ HTTP\_411\_LENGTH\_REQUIRED

Length Required.

**Definition** status.h:69

[HTTP\_500\_INTERNAL\_SERVER\_ERROR](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4)

@ HTTP\_500\_INTERNAL\_SERVER\_ERROR

Internal Server Error.

**Definition** status.h:87

[HTTP\_205\_RESET\_CONTENT](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255)

@ HTTP\_205\_RESET\_CONTENT

Reset Content.

**Definition** status.h:44

[HTTP\_401\_UNAUTHORIZED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113)

@ HTTP\_401\_UNAUTHORIZED

Unauthorized.

**Definition** status.h:59

[HTTP\_402\_PAYMENT\_REQUIRED](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b)

@ HTTP\_402\_PAYMENT\_REQUIRED

Payment Required.

**Definition** status.h:60

[HTTP\_451\_UNAVAILABLE\_FOR\_LEGAL\_REASONS](group__http__status__codes.md#ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1)

@ HTTP\_451\_UNAVAILABLE\_FOR\_LEGAL\_REASONS

Unavailable For Legal Reasons.

**Definition** status.h:86

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [status.h](status_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
