---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/timestamp_8h.html
original_path: doxygen/html/timestamp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timestamp.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <zephyr/test_asm_inline_other.h>`

[Go to the source code of this file.](timestamp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TICK\_SYNCH](#a95c5be89ea7bce90d2a8a11472ebd2c6)() |
| #define | [OS\_GET\_TIME](#a1b4134f508183af47ef3deff07be4a54)() |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [TIME\_STAMP\_DELTA\_GET](#abb03327df49c0544f863a239a9af0086) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
| static void | [bench\_test\_init](#a7d2ae16b9d290b7ab914f71155c5e56d) (void) |
| static void | [bench\_test\_start](#ac476d41973f921a386c9a8341296dcfd) (void) |
| static int | [bench\_test\_end](#a6555ffaf6ca7b4f5b81477faa8f43f53) (void) |
| static int | [high\_timer\_overflow](#a54d527f8fde477822ad2044579a7edd3) (void) |

| Variables | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tm\_off](#a2503eba6a8f75337fe8c7ee84b0b3b21) |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [timestamp\_check](#a5a399603fca75f3004d45720f03f9d44) |

## Macro Definition Documentation

## [◆ ](#a1b4134f508183af47ef3deff07be4a54)OS\_GET\_TIME

| #define OS\_GET\_TIME | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)()

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)

static uint32\_t k\_cycle\_get\_32(void)

Read the hardware clock.

**Definition** kernel.h:1900

## [◆ ](#a95c5be89ea7bce90d2a8a11472ebd2c6)TICK\_SYNCH

| #define TICK\_SYNCH | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)([K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)(1))

[K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)

#define K\_TICKS(t)

Generate timeout delay from system ticks.

**Definition** kernel.h:1382

[k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657)

int32\_t k\_sleep(k\_timeout\_t timeout)

Put the current thread to sleep.

## Function Documentation

## [◆ ](#a6555ffaf6ca7b4f5b81477faa8f43f53)bench\_test\_end()

| | int bench\_test\_end | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7d2ae16b9d290b7ab914f71155c5e56d)bench\_test\_init()

| | void bench\_test\_init | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac476d41973f921a386c9a8341296dcfd)bench\_test\_start()

| | void bench\_test\_start | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a54d527f8fde477822ad2044579a7edd3)high\_timer\_overflow()

| | int high\_timer\_overflow | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#abb03327df49c0544f863a239a9af0086)TIME\_STAMP\_DELTA\_GET()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) TIME\_STAMP\_DELTA\_GET | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#a5a399603fca75f3004d45720f03f9d44)timestamp\_check

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) timestamp\_check | | --- | | static |
| --- | --- | --- |

## [◆ ](#a2503eba6a8f75337fe8c7ee84b0b3b21)tm\_off

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tm\_off | | --- | | extern |
| --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [timestamp.h](timestamp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
