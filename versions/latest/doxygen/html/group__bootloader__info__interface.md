---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bootloader__info__interface.html
original_path: doxygen/html/group__bootloader__info__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bootloader info interface

[Operating System Services](group__os__services.md) » [Retention API](group__retention__api.md)

Bootloader info interface.
[More...](#details)

| Functions | |
| --- | --- |
| int | [blinfo\_lookup](#ga7b172c65244678070c9b6ca6e24cee0f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key, char \*val, int val\_len\_max) |
|  | Returns bootinfo information. |

## Detailed Description

Bootloader info interface.

## Function Documentation

## [◆ ](#ga7b172c65244678070c9b6ca6e24cee0f)blinfo\_lookup()

| int blinfo\_lookup | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key*, |
| --- | --- | --- | --- |
|  |  | char \* | *val*, |
|  |  | int | *val\_len\_max* ) |

`#include <[blinfo.h](blinfo_8h.md)>`

Returns bootinfo information.

Parameters
:   | key | The information to return (for MCUboot: minor TLV). |
    | --- | --- |
    | val | Where the return information will be placed. |
    | val\_len\_max | The maximum size of the provided buffer. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EOVERFLOW | If the data is too large to fit the supplied buffer. |
    | -EIO | If the requested key was not found. |
    | -errno | Error code. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
