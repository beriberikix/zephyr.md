---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fake__comp_8h.html
original_path: doxygen/html/fake__comp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_comp.h File Reference

`#include <[zephyr/drivers/comparator.h](comparator_8h_source.md)>`  
`#include <[zephyr/fff.h](fff_8h_source.md)>`

[Go to the source code of this file.](fake__comp_8h_source.md)

| Functions | |
| --- | --- |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a2c5d4864a0a2f27f0e612eeb5021238a) (int, comp\_fake\_comp\_get\_output, const struct [device](structdevice.md) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a87eda8131b9665071bb533088704478c) (int, comp\_fake\_comp\_set\_trigger, const struct [device](structdevice.md) \*, enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a75a4f06e86d3ea886fd512c26c376dfa) (int, comp\_fake\_comp\_set\_trigger\_callback, const struct [device](structdevice.md) \*, [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31), void \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a3851a9b2f4fa854329cb7e43dc74323e) (int, comp\_fake\_comp\_trigger\_is\_pending, const struct [device](structdevice.md) \*) |

## Function Documentation

## [◆ ](#a2c5d4864a0a2f27f0e612eeb5021238a)DECLARE\_FAKE\_VALUE\_FUNC() [1/4]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | comp\_fake\_comp\_get\_output | , |
|  |  | const struct [device](structdevice.md) \* | ) |

## [◆ ](#a87eda8131b9665071bb533088704478c)DECLARE\_FAKE\_VALUE\_FUNC() [2/4]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | comp\_fake\_comp\_set\_trigger | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | enum | *comparator\_trigger* ) |

## [◆ ](#a75a4f06e86d3ea886fd512c26c376dfa)DECLARE\_FAKE\_VALUE\_FUNC() [3/4]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | comp\_fake\_comp\_set\_trigger\_callback | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31) | , |
|  |  | void \* | ) |

## [◆ ](#a3851a9b2f4fa854329cb7e43dc74323e)DECLARE\_FAKE\_VALUE\_FUNC() [4/4]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | comp\_fake\_comp\_trigger\_is\_pending | , |
|  |  | const struct [device](structdevice.md) \* | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [fake\_comp.h](fake__comp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
