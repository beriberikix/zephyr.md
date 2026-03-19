---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__cs__test__cb.html
original_path: doxygen/html/structbt__le__cs__test__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_test\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

Callbacks for CS Test.
[More...](#details)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [le\_cs\_test\_subevent\_data\_available](#a2a3ca580a3c3d55aa2f2323a318827f9) )(struct [bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md) \*data) |
|  | CS Test Subevent data. |
| void(\* | [le\_cs\_test\_end\_complete](#a7da5731fb2ae9e7fc3cece78a7468663) )(void) |
|  | CS Test End Complete. |

## Detailed Description

Callbacks for CS Test.

## Field Documentation

## [◆ ](#a7da5731fb2ae9e7fc3cece78a7468663)le\_cs\_test\_end\_complete

| void(\* bt\_le\_cs\_test\_cb::le\_cs\_test\_end\_complete) (void) |
| --- |

CS Test End Complete.

## [◆ ](#a2a3ca580a3c3d55aa2f2323a318827f9)le\_cs\_test\_subevent\_data\_available

| void(\* bt\_le\_cs\_test\_cb::le\_cs\_test\_subevent\_data\_available) (struct [bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md) \*data) |
| --- |

CS Test Subevent data.

Parameters
:   | [in] | Subevent | results. |
    | --- | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_test\_cb](structbt__le__cs__test__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
