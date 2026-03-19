---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/comparator_8h.html
original_path: doxygen/html/comparator_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

comparator.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <zephyr/syscalls/comparator.h>`

[Go to the source code of this file.](comparator_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Comparator callback template. |

| Enumerations | |
| --- | --- |
| enum | [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) { [COMPARATOR\_TRIGGER\_NONE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674aef8abb95e06470906323eb67a84274ab) = 0 , [COMPARATOR\_TRIGGER\_RISING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a2bd8d1afb67a68a0bbc6737d434d6b89) , [COMPARATOR\_TRIGGER\_FALLING\_EDGE](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a762c9ea031595a909d2b70128adf9734) , [COMPARATOR\_TRIGGER\_BOTH\_EDGES](group__comparator__interface.md#ggab02743771baf02ee0105aa1303931674a65cb9e6aa70639b15d0ca3cf16777f97) } |
|  | Comparator trigger enumerations. [More...](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) |

| Functions | |
| --- | --- |
| int | [comparator\_get\_output](group__comparator__interface.md#ga89ea48c5d4a9d8c8ec44ee4c987309f3) (const struct [device](structdevice.md) \*dev) |
|  | Get comparator's output state. |
| int | [comparator\_set\_trigger](group__comparator__interface.md#ga964fab6458e020d8717ee7c47a84c1d0) (const struct [device](structdevice.md) \*dev, enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674) trigger) |
|  | Set comparator's trigger. |
| static int | [comparator\_set\_trigger\_callback](group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509) (const struct [device](structdevice.md) \*dev, [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31) callback, void \*user\_data) |
|  | Set comparator's trigger callback. |
| int | [comparator\_trigger\_is\_pending](group__comparator__interface.md#ga28aa27594c7c3cf5cd7306d47ebf53f9) (const struct [device](structdevice.md) \*dev) |
|  | Check if comparator's trigger is pending and clear it. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator.h](comparator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
