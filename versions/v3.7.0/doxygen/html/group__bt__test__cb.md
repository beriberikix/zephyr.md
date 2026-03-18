---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__test__cb.html
original_path: doxygen/html/group__bt__test__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth testing callbacks

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth testing.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_test\_cb](structbt__test__cb.md) |
|  | Bluetooth Testing callbacks structure. [More...](structbt__test__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_test\_cb\_register](#ga79979505bd3809ea401d5db4b0c13cd6) (struct [bt\_test\_cb](structbt__test__cb.md) \*cb) |
|  | Register callbacks for Bluetooth testing purposes. |
| void | [bt\_test\_cb\_unregister](#ga2d2c1085532ce33175e20bf6ef48329c) (struct [bt\_test\_cb](structbt__test__cb.md) \*cb) |
|  | Unregister callbacks for Bluetooth testing purposes. |
| int | [bt\_test\_mesh\_lpn\_group\_add](#gad0590321fdc43ee71b10a9a1d260bb92) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group) |
|  | Send Friend Subscription List Add message. |
| int | [bt\_test\_mesh\_lpn\_group\_remove](#gaa33faa58edd5a8bf286815309571baf7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*groups, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) groups\_count) |
|  | Send Friend Subscription List Remove message. |
| int | [bt\_test\_mesh\_rpl\_clear](#ga02e2d32cec7115970a4278d733df1879) (void) |
|  | Clear replay protection list cache. |

## Detailed Description

Bluetooth testing.

## Function Documentation

## [◆ ](#ga79979505bd3809ea401d5db4b0c13cd6)bt\_test\_cb\_register()

| int bt\_test\_cb\_register | ( | struct [bt\_test\_cb](structbt__test__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[testing.h](testing_8h.md)>`

Register callbacks for Bluetooth testing purposes.

Parameters
:   | cb | [bt\_test\_cb](structbt__test__cb.md "Bluetooth Testing callbacks structure.") callback structure |
    | --- | --- |

Return values
:   | 0 | Success. |
    | --- | --- |
    | -EEXIST | if `cb` was already registered. |

## [◆ ](#ga2d2c1085532ce33175e20bf6ef48329c)bt\_test\_cb\_unregister()

| void bt\_test\_cb\_unregister | ( | struct [bt\_test\_cb](structbt__test__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[testing.h](testing_8h.md)>`

Unregister callbacks for Bluetooth testing purposes.

Parameters
:   | cb | [bt\_test\_cb](structbt__test__cb.md "Bluetooth Testing callbacks structure.") callback structure |
    | --- | --- |

## [◆ ](#gad0590321fdc43ee71b10a9a1d260bb92)bt\_test\_mesh\_lpn\_group\_add()

| int bt\_test\_mesh\_lpn\_group\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *group* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[testing.h](testing_8h.md)>`

Send Friend Subscription List Add message.

Used by Low Power node to send the group address for which messages are to be stored by Friend node.

Parameters
:   | group | Group address |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaa33faa58edd5a8bf286815309571baf7)bt\_test\_mesh\_lpn\_group\_remove()

| int bt\_test\_mesh\_lpn\_group\_remove | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *groups*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *groups\_count* ) |

`#include <[testing.h](testing_8h.md)>`

Send Friend Subscription List Remove message.

Used by Low Power node to remove the group addresses from Friend node subscription list. Messages sent to those addresses will not be stored by Friend node.

Parameters
:   | groups | Group addresses |
    | --- | --- |
    | groups\_count | Group addresses count |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga02e2d32cec7115970a4278d733df1879)bt\_test\_mesh\_rpl\_clear()

| int bt\_test\_mesh\_rpl\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[testing.h](testing_8h.md)>`

Clear replay protection list cache.

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
