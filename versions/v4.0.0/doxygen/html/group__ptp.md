---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ptp.html
original_path: doxygen/html/group__ptp.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PTP support

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Precision Time Protocol (PTP) support.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [PTP\_MAJOR\_VERSION](#ga7ee0c8e25e85663efbaaa12eac6bee7b)   2 |
|  | Major PTP Version. |
| #define | [PTP\_MINOR\_VERSION](#ga45adf4966a9012e08dbfbbccf2b806d0)   1 |
|  | Minor PTP Version. |
| #define | [PTP\_VERSION](#ga19395e019e5a96c94ac021bd788c6b55)   ([PTP\_MINOR\_VERSION](#ga45adf4966a9012e08dbfbbccf2b806d0) << 4 | [PTP\_MAJOR\_VERSION](#ga7ee0c8e25e85663efbaaa12eac6bee7b)) |
|  | PTP version IEEE-1588:2019. |

## Detailed Description

Precision Time Protocol (PTP) support.

Since
:   3.7

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga7ee0c8e25e85663efbaaa12eac6bee7b)PTP\_MAJOR\_VERSION

| #define PTP\_MAJOR\_VERSION   2 |
| --- |

`#include <[ptp.h](ptp_8h.md)>`

Major PTP Version.

## [◆ ](#ga45adf4966a9012e08dbfbbccf2b806d0)PTP\_MINOR\_VERSION

| #define PTP\_MINOR\_VERSION   1 |
| --- |

`#include <[ptp.h](ptp_8h.md)>`

Minor PTP Version.

## [◆ ](#ga19395e019e5a96c94ac021bd788c6b55)PTP\_VERSION

| #define PTP\_VERSION   ([PTP\_MINOR\_VERSION](#ga45adf4966a9012e08dbfbbccf2b806d0) << 4 | [PTP\_MAJOR\_VERSION](#ga7ee0c8e25e85663efbaaa12eac6bee7b)) |
| --- |

`#include <[ptp.h](ptp_8h.md)>`

PTP version IEEE-1588:2019.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
