---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hrs_8h.html
original_path: doxygen/html/hrs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hrs.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](hrs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hrs\_cb](structbt__hrs__cb.md) |
|  | Heart rate service callback structure. [More...](structbt__hrs__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_hrs\_cb\_register](group__bt__hrs.md#ga4b250a12dc6e975589f21ca1391c5b38) (struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb) |
|  | Heart rate service callback register. |
| int | [bt\_hrs\_cb\_unregister](group__bt__hrs.md#gad725bf460319ca796c166a5f91e38bb6) (struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb) |
|  | Heart rate service callback unregister. |
| int | [bt\_hrs\_notify](group__bt__hrs.md#ga0e3d298d984e2504957ca655f142e45b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) heartrate) |
|  | Notify heart rate measurement. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [hrs.h](hrs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
