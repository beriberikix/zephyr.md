---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structstat.html
original_path: doxygen/html/structstat.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat Struct Reference

`#include <[stat.h](stat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) | [st\_dev](#ac5b90090ae323741ae4c9e4f3683a29f) |
| [ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c) | [st\_ino](#a9769ed8f0d4c5a9f329c32bc92479d56) |
| [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | [st\_mode](#a5cbdd829011af82ba61e83773bbcbc7d) |
| [nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e) | [st\_nlink](#a0ed9092fa6c77a3251b9b9a4738ef84f) |
| [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) | [st\_uid](#a4a8708a3d18be60ee7b2f06c4cab0c70) |
| [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) | [st\_gid](#ab864f16f436cec370f0ced585d897698) |
| [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) | [st\_rdev](#aa61e6c1a8a91c69f1d26f6700a0546cb) |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [st\_size](#a040e19c8b9766f841fde8786ce9297bf) |
| struct [timespec](structtimespec.md) | [st\_atim](#a8447c545451bec2b95f9d67787404934) |
| struct [timespec](structtimespec.md) | [st\_mtim](#a78eca07da5a8a88b1c3dd8be5a32821e) |
| struct [timespec](structtimespec.md) | [st\_ctim](#a8fcf65727b775d92b773776ed1210c8b) |
| [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b) | [st\_blksize](#a38d474e1ae3cf6fbdde89ac3c3e308f1) |
| [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347) | [st\_blocks](#a42dd716b2f9234f961d949fc9500eefb) |
| long | [st\_spare4](#a3715a60e75816e25a52d150e1893af76) [2] |

## Field Documentation

## [◆ ](#a8447c545451bec2b95f9d67787404934)st\_atim

| struct [timespec](structtimespec.md) stat::st\_atim |
| --- |

## [◆ ](#a38d474e1ae3cf6fbdde89ac3c3e308f1)st\_blksize

| [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b) stat::st\_blksize |
| --- |

## [◆ ](#a42dd716b2f9234f961d949fc9500eefb)st\_blocks

| [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347) stat::st\_blocks |
| --- |

## [◆ ](#a8fcf65727b775d92b773776ed1210c8b)st\_ctim

| struct [timespec](structtimespec.md) stat::st\_ctim |
| --- |

## [◆ ](#ac5b90090ae323741ae4c9e4f3683a29f)st\_dev

| [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) stat::st\_dev |
| --- |

## [◆ ](#ab864f16f436cec370f0ced585d897698)st\_gid

| [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) stat::st\_gid |
| --- |

## [◆ ](#a9769ed8f0d4c5a9f329c32bc92479d56)st\_ino

| [ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c) stat::st\_ino |
| --- |

## [◆ ](#a5cbdd829011af82ba61e83773bbcbc7d)st\_mode

| [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) stat::st\_mode |
| --- |

## [◆ ](#a78eca07da5a8a88b1c3dd8be5a32821e)st\_mtim

| struct [timespec](structtimespec.md) stat::st\_mtim |
| --- |

## [◆ ](#a0ed9092fa6c77a3251b9b9a4738ef84f)st\_nlink

| [nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e) stat::st\_nlink |
| --- |

## [◆ ](#aa61e6c1a8a91c69f1d26f6700a0546cb)st\_rdev

| [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) stat::st\_rdev |
| --- |

## [◆ ](#a040e19c8b9766f841fde8786ce9297bf)st\_size

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) stat::st\_size |
| --- |

## [◆ ](#a3715a60e75816e25a52d150e1893af76)st\_spare4

| long stat::st\_spare4[2] |
| --- |

## [◆ ](#a4a8708a3d18be60ee7b2f06c4cab0c70)st\_uid

| [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) stat::st\_uid |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/sys/[stat.h](stat_8h_source.md)

- [stat](structstat.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
