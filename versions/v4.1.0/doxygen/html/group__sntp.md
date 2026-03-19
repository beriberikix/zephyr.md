---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__sntp.html
original_path: doxygen/html/group__sntp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SNTP

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Simple Network Time Protocol API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sntp\_time](structsntp__time.md) |
|  | Time as returned by SNTP API, fractional seconds since 1 Jan 1970. [More...](structsntp__time.md#details) |
| struct | [sntp\_ctx](structsntp__ctx.md) |
|  | SNTP context. [More...](structsntp__ctx.md#details) |

| Functions | |
| --- | --- |
| int | [sntp\_init](#ga945936e5164bbd959cfa666ceacdac13) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | Initialize SNTP context. |
| int | [sntp\_query](#ga25ef46cc74be71bbe2f76de7c30cbe45) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Perform SNTP query. |
| int | [sntp\_recv\_response](#ga8771cdc6e64ab1489b333cc0c1731e9f) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Attempt to receive an SNTP response after issuing a query. |
| void | [sntp\_close](#ga0cff25edb11ae944dd24a234450a2f3d) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx) |
|  | Release SNTP context. |
| int | [sntp\_simple](#ga25c894db6d24a5e729b4edcb8917ce9c) (const char \*server, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Convenience function to query SNTP in one-shot fashion. |
| int | [sntp\_simple\_addr](#ga75aaee9a8f8490c0cc826a0e9298cd88) (struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct. |

## Detailed Description

Simple Network Time Protocol API.

Since
:   1.10

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga0cff25edb11ae944dd24a234450a2f3d)sntp\_close()

| void sntp\_close | ( | struct [sntp\_ctx](structsntp__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sntp.h](sntp_8h.md)>`

Release SNTP context.

Parameters
:   | ctx | Address of sntp context. |
    | --- | --- |

## [◆ ](#ga945936e5164bbd959cfa666ceacdac13)sntp\_init()

| int sntp\_init | ( | struct [sntp\_ctx](structsntp__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len* ) |

`#include <[sntp.h](sntp_8h.md)>`

Initialize SNTP context.

Parameters
:   | ctx | Address of sntp context. |
    | --- | --- |
    | addr | IP address of NTP/SNTP server. |
    | addr\_len | IP address length of NTP/SNTP server. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga25ef46cc74be71bbe2f76de7c30cbe45)sntp\_query()

| int sntp\_query | ( | struct [sntp\_ctx](structsntp__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout*, |
|  |  | struct [sntp\_time](structsntp__time.md) \* | *ts* ) |

`#include <[sntp.h](sntp_8h.md)>`

Perform SNTP query.

Parameters
:   | ctx | Address of sntp context. |
    | --- | --- |
    | timeout | Timeout of waiting for sntp response (in milliseconds). |
    | ts | Timestamp including integer and fractional seconds since 1 Jan 1970 (output). |

Returns
:   0 if ok, <0 if error (-ETIMEDOUT if timeout).

## [◆ ](#ga8771cdc6e64ab1489b333cc0c1731e9f)sntp\_recv\_response()

| int sntp\_recv\_response | ( | struct [sntp\_ctx](structsntp__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout*, |
|  |  | struct [sntp\_time](structsntp__time.md) \* | *ts* ) |

`#include <[sntp.h](sntp_8h.md)>`

Attempt to receive an SNTP response after issuing a query.

Parameters
:   | ctx | Address of sntp context. |
    | --- | --- |
    | timeout | Timeout of waiting for sntp response (in milliseconds). |
    | ts | Timestamp including integer and fractional seconds since 1 Jan 1970 (output). |

Returns
:   0 if ok, <0 if error (-ETIMEDOUT if timeout).

## [◆ ](#ga25c894db6d24a5e729b4edcb8917ce9c)sntp\_simple()

| int sntp\_simple | ( | const char \* | *server*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout*, |
|  |  | struct [sntp\_time](structsntp__time.md) \* | *ts* ) |

`#include <[sntp.h](sntp_8h.md)>`

Convenience function to query SNTP in one-shot fashion.

Convenience wrapper which calls [getaddrinfo()](netdb_8h.md#adc9ea491d9008de7cd9e0a5b9147ca70), [sntp\_init()](#ga945936e5164bbd959cfa666ceacdac13), [sntp\_query()](#ga25ef46cc74be71bbe2f76de7c30cbe45), and [sntp\_close()](#ga0cff25edb11ae944dd24a234450a2f3d).

Parameters
:   | server | Address of server in format addr[:port] |
    | --- | --- |
    | timeout | Query timeout |
    | ts | Timestamp including integer and fractional seconds since 1 Jan 1970 (output). |

Returns
:   0 if ok, <0 if error (-ETIMEDOUT if timeout).

## [◆ ](#ga75aaee9a8f8490c0cc826a0e9298cd88)sntp\_simple\_addr()

| int sntp\_simple\_addr | ( | struct [sockaddr](structsockaddr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout*, |
|  |  | struct [sntp\_time](structsntp__time.md) \* | *ts* ) |

`#include <[sntp.h](sntp_8h.md)>`

Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct.

Convenience wrapper which calls [sntp\_init()](#ga945936e5164bbd959cfa666ceacdac13), [sntp\_query()](#ga25ef46cc74be71bbe2f76de7c30cbe45) and [sntp\_close()](#ga0cff25edb11ae944dd24a234450a2f3d).

Parameters
:   | addr | IP address of NTP/SNTP server. |
    | --- | --- |
    | addr\_len | IP address length of NTP/SNTP server. |
    | timeout | Query timeout |
    | ts | Timestamp including integer and fractional seconds since 1 Jan 1970 (output). |

Returns
:   0 if ok, <0 if error (-ETIMEDOUT if timeout).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
