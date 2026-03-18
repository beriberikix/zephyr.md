---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ias_8h.html
original_path: doxygen/html/ias_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ias.h File Reference

`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](ias_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_ias\_cb](structbt__ias__cb.md) |
|  | Immediate Alert Service callback structure. [More...](structbt__ias__cb.md#details) |
| struct | [bt\_ias\_client\_cb](structbt__ias__client__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_IAS\_CB\_DEFINE](group__bt__ias.md#ga5dee0ec206e8ddbb9bc33c8df824fcb0)(\_name) |
|  | Register a callback structure for immediate alert events. |

| Enumerations | |
| --- | --- |
| enum | [bt\_ias\_alert\_lvl](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0) { [BT\_IAS\_ALERT\_LVL\_NO\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997) , [BT\_IAS\_ALERT\_LVL\_MILD\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd) , [BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653) } |

| Functions | |
| --- | --- |
| int | [bt\_ias\_local\_alert\_stop](group__bt__ias.md#gad810c9d74701dc48c12e4545bded95a4) (void) |
|  | Method for stopping alert locally. |
| int | [bt\_ias\_client\_alert\_write](group__bt__ias.md#ga040ef37207ddca54edb9839c721ca2f2) (struct bt\_conn \*conn, enum [bt\_ias\_alert\_lvl](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0)) |
|  | Set alert level. |
| int | [bt\_ias\_discover](group__bt__ias.md#ga2628386523390e044e4a32fb2cf3e7b5) (struct bt\_conn \*conn) |
|  | Discover Immediate Alert Service. |
| int | [bt\_ias\_client\_cb\_register](group__bt__ias.md#ga481a20cbe9b3f128f8737f75535d2bfe) (const struct [bt\_ias\_client\_cb](structbt__ias__client__cb.md) \*cb) |
|  | Register Immediate Alert Client callbacks. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [ias.h](ias_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
