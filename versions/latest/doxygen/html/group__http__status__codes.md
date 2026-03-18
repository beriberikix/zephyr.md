---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__http__status__codes.html
original_path: doxygen/html/group__http__status__codes.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HTTP response status codes

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

HTTP response status codes.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [http\_status](#gabc3b93f68c8bdd857ad32913628dfa8d) {     [HTTP\_100\_CONTINUE](#ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882) = 100 , [HTTP\_101\_SWITCHING\_PROTOCOLS](#ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5) = 101 , [HTTP\_102\_PROCESSING](#ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af) = 102 , [HTTP\_103\_EARLY\_HINTS](#ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0) = 103 ,     [HTTP\_200\_OK](#ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9) = 200 , [HTTP\_201\_CREATED](#ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a) = 201 , [HTTP\_202\_ACCEPTED](#ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9) = 202 , [HTTP\_203\_NON\_AUTHORITATIVE\_INFORMATION](#ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce) = 203 ,     [HTTP\_204\_NO\_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93) = 204 , [HTTP\_205\_RESET\_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255) = 205 , [HTTP\_206\_PARTIAL\_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2) = 206 , [HTTP\_207\_MULTI\_STATUS](#ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d) = 207 ,     [HTTP\_208\_ALREADY\_REPORTED](#ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f) = 208 , [HTTP\_226\_IM\_USED](#ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b) = 226 , [HTTP\_300\_MULTIPLE\_CHOICES](#ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435) = 300 , [HTTP\_301\_MOVED\_PERMANENTLY](#ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f) = 301 ,     [HTTP\_302\_FOUND](#ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc) = 302 , [HTTP\_303\_SEE\_OTHER](#ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51) = 303 , [HTTP\_304\_NOT\_MODIFIED](#ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8) = 304 , [HTTP\_305\_USE\_PROXY](#ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa) = 305 ,     [HTTP\_306\_UNUSED](#ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981) = 306 , [HTTP\_307\_TEMPORARY\_REDIRECT](#ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7) = 307 , [HTTP\_308\_PERMANENT\_REDIRECT](#ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416) = 308 , [HTTP\_400\_BAD\_REQUEST](#ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c) = 400 ,     [HTTP\_401\_UNAUTHORIZED](#ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113) = 401 , [HTTP\_402\_PAYMENT\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b) = 402 , [HTTP\_403\_FORBIDDEN](#ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00) = 403 , [HTTP\_404\_NOT\_FOUND](#ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875) = 404 ,     [HTTP\_405\_METHOD\_NOT\_ALLOWED](#ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163) = 405 , [HTTP\_406\_NOT\_ACCEPTABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0) = 406 , [HTTP\_407\_PROXY\_AUTHENTICATION\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4) = 407 , [HTTP\_408\_REQUEST\_TIMEOUT](#ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01) = 408 ,     [HTTP\_409\_CONFLICT](#ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50) = 409 , [HTTP\_410\_GONE](#ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444) = 410 , [HTTP\_411\_LENGTH\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93) = 411 , [HTTP\_412\_PRECONDITION\_FAILED](#ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5) = 412 ,     [HTTP\_413\_PAYLOAD\_TOO\_LARGE](#ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35) = 413 , [HTTP\_414\_URI\_TOO\_LONG](#ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807) = 414 , [HTTP\_415\_UNSUPPORTED\_MEDIA\_TYPE](#ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd) = 415 , [HTTP\_416\_RANGE\_NOT\_SATISFIABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095) = 416 ,     [HTTP\_417\_EXPECTATION\_FAILED](#ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae) = 417 , [HTTP\_418\_IM\_A\_TEAPOT](#ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762) = 418 , [HTTP\_421\_MISDIRECTED\_REQUEST](#ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b) = 421 , [HTTP\_422\_UNPROCESSABLE\_ENTITY](#ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8) = 422 ,     [HTTP\_423\_LOCKED](#ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7) = 423 , [HTTP\_424\_FAILED\_DEPENDENCY](#ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3) = 424 , [HTTP\_425\_TOO\_EARLY](#ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc) = 425 , [HTTP\_426\_UPGRADE\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2) = 426 ,     [HTTP\_428\_PRECONDITION\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98) = 428 , [HTTP\_429\_TOO\_MANY\_REQUESTS](#ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e) = 429 , [HTTP\_431\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE](#ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14) = 431 , [HTTP\_451\_UNAVAILABLE\_FOR\_LEGAL\_REASONS](#ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1) = 451 ,     [HTTP\_500\_INTERNAL\_SERVER\_ERROR](#ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4) = 500 , [HTTP\_501\_NOT\_IMPLEMENTED](#ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b) = 501 , [HTTP\_502\_BAD\_GATEWAY](#ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375) = 502 , [HTTP\_503\_SERVICE\_UNAVAILABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d) = 503 ,     [HTTP\_504\_GATEWAY\_TIMEOUT](#ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71) = 504 , [HTTP\_505\_HTTP\_VERSION\_NOT\_SUPPORTED](#ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419) = 505 , [HTTP\_506\_VARIANT\_ALSO\_NEGOTIATES](#ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e) = 506 , [HTTP\_507\_INSUFFICIENT\_STORAGE](#ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97) = 507 ,     [HTTP\_508\_LOOP\_DETECTED](#ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45) = 508 , [HTTP\_510\_NOT\_EXTENDED](#ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb) = 510 , [HTTP\_511\_NETWORK\_AUTHENTICATION\_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a) = 511   } |
|  | HTTP response status codes. [More...](#gabc3b93f68c8bdd857ad32913628dfa8d) |

## Detailed Description

HTTP response status codes.

## Enumeration Type Documentation

## [◆ ](#gabc3b93f68c8bdd857ad32913628dfa8d)http\_status

| enum [http\_status](#gabc3b93f68c8bdd857ad32913628dfa8d) |
| --- |

`#include <[status.h](status_8h.md)>`

HTTP response status codes.

Note
:   HTTP response status codes are subject to IANA approval.

See also
:   [Hypertext Transfer Protocol (HTTP) Status Code Registry](https://www.iana.org/assignments/http-status-codes)
:   [RFC9110](https://www.ietf.org/rfc/rfc9110.txt)
:   [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

| Enumerator | |
| --- | --- |
| HTTP\_100\_CONTINUE | Continue. |
| HTTP\_101\_SWITCHING\_PROTOCOLS | Switching Protocols. |
| HTTP\_102\_PROCESSING | Processing. |
| HTTP\_103\_EARLY\_HINTS | Early Hints. |
| HTTP\_200\_OK | OK. |
| HTTP\_201\_CREATED | Created. |
| HTTP\_202\_ACCEPTED | Accepted. |
| HTTP\_203\_NON\_AUTHORITATIVE\_INFORMATION | Non-Authoritative Information. |
| HTTP\_204\_NO\_CONTENT | No Content. |
| HTTP\_205\_RESET\_CONTENT | Reset Content. |
| HTTP\_206\_PARTIAL\_CONTENT | Partial Content. |
| HTTP\_207\_MULTI\_STATUS | Multi-Status. |
| HTTP\_208\_ALREADY\_REPORTED | Already Reported. |
| HTTP\_226\_IM\_USED | IM Used. |
| HTTP\_300\_MULTIPLE\_CHOICES | Multiple Choices. |
| HTTP\_301\_MOVED\_PERMANENTLY | Moved Permanently. |
| HTTP\_302\_FOUND | Found. |
| HTTP\_303\_SEE\_OTHER | See Other. |
| HTTP\_304\_NOT\_MODIFIED | Not Modified. |
| HTTP\_305\_USE\_PROXY | Use Proxy. |
| HTTP\_306\_UNUSED | unused |
| HTTP\_307\_TEMPORARY\_REDIRECT | Temporary Redirect. |
| HTTP\_308\_PERMANENT\_REDIRECT | Permanent Redirect. |
| HTTP\_400\_BAD\_REQUEST | Bad Request. |
| HTTP\_401\_UNAUTHORIZED | Unauthorized. |
| HTTP\_402\_PAYMENT\_REQUIRED | Payment Required. |
| HTTP\_403\_FORBIDDEN | Forbidden. |
| HTTP\_404\_NOT\_FOUND | Not Found. |
| HTTP\_405\_METHOD\_NOT\_ALLOWED | Method Not Allowed. |
| HTTP\_406\_NOT\_ACCEPTABLE | Not Acceptable. |
| HTTP\_407\_PROXY\_AUTHENTICATION\_REQUIRED | Proxy Authentication Required. |
| HTTP\_408\_REQUEST\_TIMEOUT | Request Timeout. |
| HTTP\_409\_CONFLICT | Conflict. |
| HTTP\_410\_GONE | Gone. |
| HTTP\_411\_LENGTH\_REQUIRED | Length Required. |
| HTTP\_412\_PRECONDITION\_FAILED | Precondition Failed. |
| HTTP\_413\_PAYLOAD\_TOO\_LARGE | Payload Too Large. |
| HTTP\_414\_URI\_TOO\_LONG | URI Too Long. |
| HTTP\_415\_UNSUPPORTED\_MEDIA\_TYPE | Unsupported Media Type. |
| HTTP\_416\_RANGE\_NOT\_SATISFIABLE | Range Not Satisfiable. |
| HTTP\_417\_EXPECTATION\_FAILED | Expectation Failed. |
| HTTP\_418\_IM\_A\_TEAPOT | I'm a teapot. |
| HTTP\_421\_MISDIRECTED\_REQUEST | Misdirected Request. |
| HTTP\_422\_UNPROCESSABLE\_ENTITY | Unprocessable Entity. |
| HTTP\_423\_LOCKED | Locked. |
| HTTP\_424\_FAILED\_DEPENDENCY | Failed Dependency. |
| HTTP\_425\_TOO\_EARLY | Too Early. |
| HTTP\_426\_UPGRADE\_REQUIRED | Upgrade Required. |
| HTTP\_428\_PRECONDITION\_REQUIRED | Precondition Required. |
| HTTP\_429\_TOO\_MANY\_REQUESTS | Too Many Requests. |
| HTTP\_431\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE | Request Header Fields Too Large. |
| HTTP\_451\_UNAVAILABLE\_FOR\_LEGAL\_REASONS | Unavailable For Legal Reasons. |
| HTTP\_500\_INTERNAL\_SERVER\_ERROR | Internal Server Error. |
| HTTP\_501\_NOT\_IMPLEMENTED | Not Implemented. |
| HTTP\_502\_BAD\_GATEWAY | Bad Gateway. |
| HTTP\_503\_SERVICE\_UNAVAILABLE | Service Unavailable. |
| HTTP\_504\_GATEWAY\_TIMEOUT | Gateway Timeout. |
| HTTP\_505\_HTTP\_VERSION\_NOT\_SUPPORTED | HTTP Version Not Supported. |
| HTTP\_506\_VARIANT\_ALSO\_NEGOTIATES | Variant Also Negotiates. |
| HTTP\_507\_INSUFFICIENT\_STORAGE | Insufficient Storage. |
| HTTP\_508\_LOOP\_DETECTED | Loop Detected. |
| HTTP\_510\_NOT\_EXTENDED | Not Extended. |
| HTTP\_511\_NETWORK\_AUTHENTICATION\_REQUIRED | Network Authentication Required. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
