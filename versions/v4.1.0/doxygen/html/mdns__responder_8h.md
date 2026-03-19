---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mdns__responder_8h.html
original_path: doxygen/html/mdns__responder_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdns\_responder.h File Reference

mDNS responder API
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/net/dns_sd.h](dns__sd_8h_source.md)>`

[Go to the source code of this file.](mdns__responder_8h_source.md)

| Functions | |
| --- | --- |
| int | [mdns\_responder\_set\_ext\_records](#a4682ee30bf3e739790dbcaede5485777) (const struct [dns\_sd\_rec](structdns__sd__rec.md) \*records, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Register continuous memory of [dns\_sd\_rec](structdns__sd__rec.md "dns_sd_rec") records. |

## Detailed Description

mDNS responder API

This file contains the mDNS responder API. These APIs are used by the to register mDNS records.

## Function Documentation

## [◆ ](#a4682ee30bf3e739790dbcaede5485777)mdns\_responder\_set\_ext\_records()

| int mdns\_responder\_set\_ext\_records | ( | const struct [dns\_sd\_rec](structdns__sd__rec.md) \* | *records*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

Register continuous memory of [dns\_sd\_rec](structdns__sd__rec.md "dns_sd_rec") records.

mDNS responder will start with iteration over mDNS records registered using [DNS\_SD\_REGISTER\_SERVICE](group__dns__sd.md#ga0c0060a680d5c4fe56f2815c920c3627 "DNS_SD_REGISTER_SERVICE") (if any) and then go over external records.

Parameters
:   | records | A pointer to an array of mDNS records. It is stored internally without copying the content so it must be kept valid. It can be set to NULL, e.g. before freeing the memory block. |
    | --- | --- |
    | count | The number of elements |

Returns
:   0 for OK; -EINVAL for invalid parameters.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mdns\_responder.h](mdns__responder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
