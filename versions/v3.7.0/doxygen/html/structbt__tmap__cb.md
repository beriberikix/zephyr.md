---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__tmap__cb.html
original_path: doxygen/html/structbt__tmap__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tmap\_cb Struct Reference

TMAP callback structure.
[More...](#details)

`#include <[tmap.h](tmap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discovery\_complete](#a22ee1b605448a3707d8086de30572def) )(enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) role, struct bt\_conn \*conn, int err) |
|  | TMAP discovery complete callback. |

## Detailed Description

TMAP callback structure.

## Field Documentation

## [◆ ](#a22ee1b605448a3707d8086de30572def)discovery\_complete

| void(\* bt\_tmap\_cb::discovery\_complete) (enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) role, struct bt\_conn \*conn, int err) |
| --- |

TMAP discovery complete callback.

This callback notifies the application about the value of the TMAP Role characteristic on the peer.

Parameters
:   | role | Peer TMAP role(s). |
    | --- | --- |
    | conn | Pointer to the connection |
    | err | 0 if success, ATT error received from server otherwise. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tmap.h](tmap_8h_source.md)

- [bt\_tmap\_cb](structbt__tmap__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
