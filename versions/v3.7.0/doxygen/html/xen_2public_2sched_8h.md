---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/xen_2public_2sched_8h.html
original_path: doxygen/html/xen_2public_2sched_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched.h File Reference

`#include "[event_channel.h](event__channel_8h_source.md)"`

[Go to the source code of this file.](xen_2public_2sched_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sched\_shutdown](structsched__shutdown.md) |
| struct | [sched\_poll](structsched__poll.md) |
| struct | [sched\_remote\_shutdown](structsched__remote__shutdown.md) |
| struct | [sched\_watchdog](structsched__watchdog.md) |
| struct | [sched\_pin\_override](structsched__pin__override.md) |

| Macros | |
| --- | --- |
| #define | [SCHEDOP\_yield](#ac6729986fa8f1233fc665ff29e60d4fe)   0 |
| #define | [SCHEDOP\_block](#a566d14ea508950d32a5b1191642c7315)   1 |
| #define | [SCHEDOP\_shutdown](#ac5b250debc01324d7a41c7ae7d6a3b54)   2 |
| #define | [SCHEDOP\_poll](#aaf686f8f7b11629bf454d1610c2eb242)   3 |
| #define | [SCHEDOP\_remote\_shutdown](#a5d976e3048f113e09d37115c084bf5dc)   4 |
| #define | [SCHEDOP\_shutdown\_code](#a2cb33c474fb6d6f7063fde4d3ad06835)   5 |
| #define | [SCHEDOP\_watchdog](#a21298626bad1ba1ca03ed538f6b66677)   6 |
| #define | [SCHEDOP\_pin\_override](#a6ddcfa16b3a1af5c84360995a13d60ed)   7 |
| #define | [SHUTDOWN\_poweroff](#ab565461b915d7d8350fe4f21d8d7aceb)   0 |
| #define | [SHUTDOWN\_reboot](#a38df89b49d7eddfcabb9a73289ab8b2a)   1 |
| #define | [SHUTDOWN\_suspend](#a69edbb2f053d98cfc807a889b3fad958)   2 |
| #define | [SHUTDOWN\_crash](#addd2d09c78bbf469ebcd023207533088)   3 |
| #define | [SHUTDOWN\_watchdog](#a45cca8cb6eca9a48a63c12659edf02fd)   4 |
| #define | [SHUTDOWN\_soft\_reset](#a82ce3d9d9b48872947534b83820a0a37)   5 |
| #define | [SHUTDOWN\_MAX](#acc97d10d75325917d3bb3c47f26d99fe)   5 |

| Typedefs | |
| --- | --- |
| typedef struct [sched\_shutdown](structsched__shutdown.md) | [sched\_shutdown\_t](#ab7dec9bb2853d145f6e8035e81aacea9) |
| typedef struct [sched\_poll](structsched__poll.md) | [sched\_poll\_t](#aa4cc6a09419667548c61ee024a693b23) |
| typedef struct [sched\_remote\_shutdown](structsched__remote__shutdown.md) | [sched\_remote\_shutdown\_t](#ad9999189885b0556a19dadaa47ae8729) |
| typedef struct [sched\_watchdog](structsched__watchdog.md) | [sched\_watchdog\_t](#a220e31e99c5aded3f4fa30417d949c0a) |
| typedef struct [sched\_pin\_override](structsched__pin__override.md) | [sched\_pin\_override\_t](#a008552edd0a746a38e426e70a3f8bc1b) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#add69380a2fa2c48d1b3d0a2fc9d4c48d) ([sched\_shutdown\_t](#ab7dec9bb2853d145f6e8035e81aacea9)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a5dbec2ec7d18d52cae3a5fb79749650d) ([sched\_poll\_t](#aa4cc6a09419667548c61ee024a693b23)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#ac011ae6dd03db79f31eaf664ef337bd9) ([sched\_remote\_shutdown\_t](#ad9999189885b0556a19dadaa47ae8729)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a071598f2732280a61e9ed949691f5745) ([sched\_watchdog\_t](#a220e31e99c5aded3f4fa30417d949c0a)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a1b124f173597b5ae2ee426cd762234e9) ([sched\_pin\_override\_t](#a008552edd0a746a38e426e70a3f8bc1b)) |

## Macro Definition Documentation

## [◆ ](#a566d14ea508950d32a5b1191642c7315)SCHEDOP\_block

| #define SCHEDOP\_block   1 |
| --- |

## [◆ ](#a6ddcfa16b3a1af5c84360995a13d60ed)SCHEDOP\_pin\_override

| #define SCHEDOP\_pin\_override   7 |
| --- |

## [◆ ](#aaf686f8f7b11629bf454d1610c2eb242)SCHEDOP\_poll

| #define SCHEDOP\_poll   3 |
| --- |

## [◆ ](#a5d976e3048f113e09d37115c084bf5dc)SCHEDOP\_remote\_shutdown

| #define SCHEDOP\_remote\_shutdown   4 |
| --- |

## [◆ ](#ac5b250debc01324d7a41c7ae7d6a3b54)SCHEDOP\_shutdown

| #define SCHEDOP\_shutdown   2 |
| --- |

## [◆ ](#a2cb33c474fb6d6f7063fde4d3ad06835)SCHEDOP\_shutdown\_code

| #define SCHEDOP\_shutdown\_code   5 |
| --- |

## [◆ ](#a21298626bad1ba1ca03ed538f6b66677)SCHEDOP\_watchdog

| #define SCHEDOP\_watchdog   6 |
| --- |

## [◆ ](#ac6729986fa8f1233fc665ff29e60d4fe)SCHEDOP\_yield

| #define SCHEDOP\_yield   0 |
| --- |

## [◆ ](#addd2d09c78bbf469ebcd023207533088)SHUTDOWN\_crash

| #define SHUTDOWN\_crash   3 |
| --- |

## [◆ ](#acc97d10d75325917d3bb3c47f26d99fe)SHUTDOWN\_MAX

| #define SHUTDOWN\_MAX   5 |
| --- |

## [◆ ](#ab565461b915d7d8350fe4f21d8d7aceb)SHUTDOWN\_poweroff

| #define SHUTDOWN\_poweroff   0 |
| --- |

## [◆ ](#a38df89b49d7eddfcabb9a73289ab8b2a)SHUTDOWN\_reboot

| #define SHUTDOWN\_reboot   1 |
| --- |

## [◆ ](#a82ce3d9d9b48872947534b83820a0a37)SHUTDOWN\_soft\_reset

| #define SHUTDOWN\_soft\_reset   5 |
| --- |

## [◆ ](#a69edbb2f053d98cfc807a889b3fad958)SHUTDOWN\_suspend

| #define SHUTDOWN\_suspend   2 |
| --- |

## [◆ ](#a45cca8cb6eca9a48a63c12659edf02fd)SHUTDOWN\_watchdog

| #define SHUTDOWN\_watchdog   4 |
| --- |

## Typedef Documentation

## [◆ ](#a008552edd0a746a38e426e70a3f8bc1b)sched\_pin\_override\_t

| typedef struct [sched\_pin\_override](structsched__pin__override.md) [sched\_pin\_override\_t](#a008552edd0a746a38e426e70a3f8bc1b) |
| --- |

## [◆ ](#aa4cc6a09419667548c61ee024a693b23)sched\_poll\_t

| typedef struct [sched\_poll](structsched__poll.md) [sched\_poll\_t](#aa4cc6a09419667548c61ee024a693b23) |
| --- |

## [◆ ](#ad9999189885b0556a19dadaa47ae8729)sched\_remote\_shutdown\_t

| typedef struct [sched\_remote\_shutdown](structsched__remote__shutdown.md) [sched\_remote\_shutdown\_t](#ad9999189885b0556a19dadaa47ae8729) |
| --- |

## [◆ ](#ab7dec9bb2853d145f6e8035e81aacea9)sched\_shutdown\_t

| typedef struct [sched\_shutdown](structsched__shutdown.md) [sched\_shutdown\_t](#ab7dec9bb2853d145f6e8035e81aacea9) |
| --- |

## [◆ ](#a220e31e99c5aded3f4fa30417d949c0a)sched\_watchdog\_t

| typedef struct [sched\_watchdog](structsched__watchdog.md) [sched\_watchdog\_t](#a220e31e99c5aded3f4fa30417d949c0a) |
| --- |

## Function Documentation

## [◆ ](#a1b124f173597b5ae2ee426cd762234e9)DEFINE\_XEN\_GUEST\_HANDLE() [1/5]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [sched\_pin\_override\_t](#a008552edd0a746a38e426e70a3f8bc1b) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5dbec2ec7d18d52cae3a5fb79749650d)DEFINE\_XEN\_GUEST\_HANDLE() [2/5]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [sched\_poll\_t](#aa4cc6a09419667548c61ee024a693b23) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac011ae6dd03db79f31eaf664ef337bd9)DEFINE\_XEN\_GUEST\_HANDLE() [3/5]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [sched\_remote\_shutdown\_t](#ad9999189885b0556a19dadaa47ae8729) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#add69380a2fa2c48d1b3d0a2fc9d4c48d)DEFINE\_XEN\_GUEST\_HANDLE() [4/5]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [sched\_shutdown\_t](#ab7dec9bb2853d145f6e8035e81aacea9) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a071598f2732280a61e9ed949691f5745)DEFINE\_XEN\_GUEST\_HANDLE() [5/5]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [sched\_watchdog\_t](#a220e31e99c5aded3f4fa30417d949c0a) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [sched.h](xen_2public_2sched_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
