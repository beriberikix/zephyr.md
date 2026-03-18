---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/zperf_8h.html
original_path: doxygen/html/zperf_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zperf.h File Reference

Zperf API.
[More...](#details)

`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](zperf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [zperf\_results](structzperf__results.md) |
|  | Performance results. [More...](structzperf__results.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b)) (enum zperf\_status status, struct [zperf\_results](structzperf__results.md) \*result, void \*user\_data) |
|  | Zperf callback function used for asynchronous operations. |

| Functions | |
| --- | --- |
| int | [zperf\_udp\_upload](group__zperf.md#ga6f2704914a9a577dac119a11f98c0e8e) (const struct zperf\_upload\_params \*param, struct [zperf\_results](structzperf__results.md) \*result) |
|  | Synchronous UDP upload operation. |
| int | [zperf\_tcp\_upload](group__zperf.md#ga24c061ea0dcd44b94c2ad79dfa264e44) (const struct zperf\_upload\_params \*param, struct [zperf\_results](structzperf__results.md) \*result) |
|  | Synchronous TCP upload operation. |
| int | [zperf\_udp\_upload\_async](group__zperf.md#gacf57dcebd09cae8ecf61b553baf6b2cd) (const struct zperf\_upload\_params \*param, [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Asynchronous UDP upload operation. |
| int | [zperf\_tcp\_upload\_async](group__zperf.md#ga07704e0bd701c0f2da2b74b9a83d6b35) (const struct zperf\_upload\_params \*param, [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Asynchronous TCP upload operation. |
| int | [zperf\_udp\_download](group__zperf.md#gaae9e5669a76da0cde7454bbd7b491a4a) (const struct zperf\_download\_params \*param, [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Start UDP server. |
| int | [zperf\_tcp\_download](group__zperf.md#ga9ac136e27fc87f85ddb66cbd2f78256d) (const struct zperf\_download\_params \*param, [zperf\_callback](group__zperf.md#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Start TCP server. |
| int | [zperf\_udp\_download\_stop](group__zperf.md#ga394e3a10550cf9d0a435f5d217dfbbdf) (void) |
|  | Stop UDP server. |
| int | [zperf\_tcp\_download\_stop](group__zperf.md#gac29193fb02ccb159b7adc3c8de64895a) (void) |
|  | Stop TCP server. |

## Detailed Description

Zperf API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [zperf.h](zperf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
