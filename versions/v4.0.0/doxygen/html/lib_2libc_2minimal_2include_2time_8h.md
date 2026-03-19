---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html
original_path: doxygen/html/lib_2libc_2minimal_2include_2time_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[sys/_types.h](__types_8h_source.md)>`  
`#include <[sys/_timespec.h](__timespec_8h_source.md)>`

[Go to the source code of this file.](lib_2libc_2minimal_2include_2time_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tm](structtm.md) |

| Functions | |
| --- | --- |
| struct [tm](structtm.md) \* | [gmtime](#a4bc4ff58d4ac838a36ba939747e5833e) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*timep) |
| struct [tm](structtm.md) \* | [gmtime\_r](#aee41f7a79e9f6ec34cdf7096fd597dbd) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timep, struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result) |
| char \* | [asctime](#a068d11e0d50eab73920a3162d2ac9202) (const struct [tm](structtm.md) \*timeptr) |
| struct [tm](structtm.md) \* | [localtime](#a47dad42d50a51f3ba4033320084c833b) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*timer) |
| char \* | [ctime](#a185521f2c273b9697eb1e536a37912fb) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*clock) |
| char \* | [asctime\_r](#a86ed062bf74f495209b11b650631e2f2) (const struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) tp, char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) buf) |
| char \* | [ctime\_r](#abb5334ac0f38a87278861e6edab616db) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*clock, char \*buf) |
| struct [tm](structtm.md) \* | [localtime\_r](#a3d8015c8bf5fadc92389635bd977e880) (const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timer, struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) result) |
| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) | [time](#a99ef1cb2c789827dd5db3886dccf9067) ([time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*tloc) |

## Function Documentation

## [◆ ](#a068d11e0d50eab73920a3162d2ac9202)asctime()

| char \* asctime | ( | const struct [tm](structtm.md) \* | *timeptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a86ed062bf74f495209b11b650631e2f2)asctime\_r()

| char \* asctime\_r | ( | const struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *tp*, |
| --- | --- | --- | --- |
|  |  | char \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *buf* ) |

## [◆ ](#a185521f2c273b9697eb1e536a37912fb)ctime()

| char \* ctime | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *clock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#abb5334ac0f38a87278861e6edab616db)ctime\_r()

| char \* ctime\_r | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *clock*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf* ) |

## [◆ ](#a4bc4ff58d4ac838a36ba939747e5833e)gmtime()

| struct [tm](structtm.md) \* gmtime | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *timep* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aee41f7a79e9f6ec34cdf7096fd597dbd)gmtime\_r()

| struct [tm](structtm.md) \* gmtime\_r | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *timep*, |
| --- | --- | --- | --- |
|  |  | struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *result* ) |

## [◆ ](#a47dad42d50a51f3ba4033320084c833b)localtime()

| struct [tm](structtm.md) \* localtime | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3d8015c8bf5fadc92389635bd977e880)localtime\_r()

| struct [tm](structtm.md) \* localtime\_r | ( | const [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *timer*, |
| --- | --- | --- | --- |
|  |  | struct [tm](structtm.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *result* ) |

## [◆ ](#a99ef1cb2c789827dd5db3886dccf9067)time()

| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) time | ( | [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *tloc* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [time.h](lib_2libc_2minimal_2include_2time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
