---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__stat.html
original_path: doxygen/html/group__bt__mesh__stat.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Statistic

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Statistic.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_statistic](structbt__mesh__statistic.md) |
|  | The structure that keeps statistics of mesh frames handling. [More...](structbt__mesh__statistic.md#details) |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_stat\_get](#ga8c1e9de2f323111ee95d0903b5ecb2fd) (struct [bt\_mesh\_statistic](structbt__mesh__statistic.md) \*st) |
|  | Get mesh frame handling statistic. |
| void | [bt\_mesh\_stat\_reset](#gabe8c893466f24e9b75fe51ae5ea65132) (void) |
|  | Reset mesh frame handling statistic. |

## Detailed Description

Statistic.

## Function Documentation

## [◆ ](#ga8c1e9de2f323111ee95d0903b5ecb2fd)bt\_mesh\_stat\_get()

| void bt\_mesh\_stat\_get | ( | struct [bt\_mesh\_statistic](structbt__mesh__statistic.md) \* | *st* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[statistic.h](statistic_8h.md)>`

Get mesh frame handling statistic.

Parameters
:   | st | BLE mesh statistic. |
    | --- | --- |

## [◆ ](#gabe8c893466f24e9b75fe51ae5ea65132)bt\_mesh\_stat\_reset()

| void bt\_mesh\_stat\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[statistic.h](statistic_8h.md)>`

Reset mesh frame handling statistic.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
