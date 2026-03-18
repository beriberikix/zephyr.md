---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/testing_8h.html
original_path: doxygen/html/testing_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

testing.h File Reference

Internal API for Bluetooth testing.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](testing_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_test\_cb](structbt__test__cb.md) |
|  | Bluetooth Testing callbacks structure. [More...](structbt__test__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_test\_cb\_register](group__bt__test__cb.md#ga79979505bd3809ea401d5db4b0c13cd6) (struct [bt\_test\_cb](structbt__test__cb.md) \*cb) |
|  | Register callbacks for Bluetooth testing purposes. |
| void | [bt\_test\_cb\_unregister](group__bt__test__cb.md#ga2d2c1085532ce33175e20bf6ef48329c) (struct [bt\_test\_cb](structbt__test__cb.md) \*cb) |
|  | Unregister callbacks for Bluetooth testing purposes. |
| int | [bt\_test\_mesh\_lpn\_group\_add](group__bt__test__cb.md#gad0590321fdc43ee71b10a9a1d260bb92) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group) |
|  | Send Friend Subscription List Add message. |
| int | [bt\_test\_mesh\_lpn\_group\_remove](group__bt__test__cb.md#gaa33faa58edd5a8bf286815309571baf7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*groups, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) groups\_count) |
|  | Send Friend Subscription List Remove message. |
| int | [bt\_test\_mesh\_rpl\_clear](group__bt__test__cb.md#ga02e2d32cec7115970a4278d733df1879) (void) |
|  | Clear replay protection list cache. |

## Detailed Description

Internal API for Bluetooth testing.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [testing.h](testing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
