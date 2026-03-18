---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sparc_8h.html
original_path: doxygen/html/sparc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sparc.h File Reference

[Go to the source code of this file.](sparc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PSR\_VER\_BIT](#a3b6b8aa082ab1ef6344a85bdc761025c)   24 |
| #define | [PSR\_PIL\_BIT](#a5ee580d14f9c267d76dc0906fa0f6f69)   8 |
| #define | [PSR\_VER](#a6244f06da2bcc9c79499b354055c400e)   (0xf << [PSR\_VER\_BIT](#a3b6b8aa082ab1ef6344a85bdc761025c)) |
| #define | [PSR\_EF](#a49e2f0d06eb855c6797e2009736eac09)   (1 << 12) |
| #define | [PSR\_S](#adbf732343370fc1685ba4176db1db6bb)   (1 << 7) |
| #define | [PSR\_PS](#a2345b54dbade90ec8d3723229cb88dc0)   (1 << 6) |
| #define | [PSR\_ET](#ada37afa7445b2faaa141677c30d2378f)   (1 << 5) |
| #define | [PSR\_PIL](#af64517c44f7cf67c25602590b4b21fea)   (0xf << [PSR\_PIL\_BIT](#a5ee580d14f9c267d76dc0906fa0f6f69)) |
| #define | [PSR\_CWP](#a105dcd98b0429c955fdd858442104506)   0x1f |
| #define | [TBR\_TT\_BIT](#a5bfb42f867f7289edacc0f3ced61df2b)   4 |
| #define | [TBR\_TBA](#a86c8e0acfd7ed01269c4798f98abb8cb)   0xfffff000 |
| #define | [TBR\_TT](#a2653671b7568158f24260ea9e8faae7e)   0x00000ff0 |
| #define | [TT\_RESET](#a7d9ae67a7bb9cf93025c25ab95232e58)   0x00 |
| #define | [TT\_WINDOW\_OVERFLOW](#a3719eb7c4a6fd22df0479afe14e9cf88)   0x05 |
| #define | [TT\_WINDOW\_UNDERFLOW](#abf7f57c61c88ac4a7734d3f847c4f067)   0x06 |
| #define | [TT\_DATA\_ACCESS\_EXCEPTION](#a6e50cb2d56076ea595e9208ffca3f420)   0x09 |

## Macro Definition Documentation

## [◆ ](#a105dcd98b0429c955fdd858442104506)PSR\_CWP

| #define PSR\_CWP   0x1f |
| --- |

## [◆ ](#a49e2f0d06eb855c6797e2009736eac09)PSR\_EF

| #define PSR\_EF   (1 << 12) |
| --- |

## [◆ ](#ada37afa7445b2faaa141677c30d2378f)PSR\_ET

| #define PSR\_ET   (1 << 5) |
| --- |

## [◆ ](#af64517c44f7cf67c25602590b4b21fea)PSR\_PIL

| #define PSR\_PIL   (0xf << [PSR\_PIL\_BIT](#a5ee580d14f9c267d76dc0906fa0f6f69)) |
| --- |

## [◆ ](#a5ee580d14f9c267d76dc0906fa0f6f69)PSR\_PIL\_BIT

| #define PSR\_PIL\_BIT   8 |
| --- |

## [◆ ](#a2345b54dbade90ec8d3723229cb88dc0)PSR\_PS

| #define PSR\_PS   (1 << 6) |
| --- |

## [◆ ](#adbf732343370fc1685ba4176db1db6bb)PSR\_S

| #define PSR\_S   (1 << 7) |
| --- |

## [◆ ](#a6244f06da2bcc9c79499b354055c400e)PSR\_VER

| #define PSR\_VER   (0xf << [PSR\_VER\_BIT](#a3b6b8aa082ab1ef6344a85bdc761025c)) |
| --- |

## [◆ ](#a3b6b8aa082ab1ef6344a85bdc761025c)PSR\_VER\_BIT

| #define PSR\_VER\_BIT   24 |
| --- |

## [◆ ](#a86c8e0acfd7ed01269c4798f98abb8cb)TBR\_TBA

| #define TBR\_TBA   0xfffff000 |
| --- |

## [◆ ](#a2653671b7568158f24260ea9e8faae7e)TBR\_TT

| #define TBR\_TT   0x00000ff0 |
| --- |

## [◆ ](#a5bfb42f867f7289edacc0f3ced61df2b)TBR\_TT\_BIT

| #define TBR\_TT\_BIT   4 |
| --- |

## [◆ ](#a6e50cb2d56076ea595e9208ffca3f420)TT\_DATA\_ACCESS\_EXCEPTION

| #define TT\_DATA\_ACCESS\_EXCEPTION   0x09 |
| --- |

## [◆ ](#a7d9ae67a7bb9cf93025c25ab95232e58)TT\_RESET

| #define TT\_RESET   0x00 |
| --- |

## [◆ ](#a3719eb7c4a6fd22df0479afe14e9cf88)TT\_WINDOW\_OVERFLOW

| #define TT\_WINDOW\_OVERFLOW   0x05 |
| --- |

## [◆ ](#abf7f57c61c88ac4a7734d3f847c4f067)TT\_WINDOW\_UNDERFLOW

| #define TT\_WINDOW\_UNDERFLOW   0x06 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [sparc.h](sparc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
