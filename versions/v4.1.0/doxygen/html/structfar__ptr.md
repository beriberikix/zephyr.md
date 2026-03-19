---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfar__ptr.html
original_path: doxygen/html/structfar__ptr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

far\_ptr Struct Reference

`#include <[segmentation.h](segmentation_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [offset](#a348a66049c5a1cf56e86743c03ce568b) |
|  | Far pointer offset, unused when invoking a task. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sel](#a756bf5b1059a1d637556aadbf687df31) |
|  | Far pointer segment/gate selector. |

## Field Documentation

## [◆ ](#a348a66049c5a1cf56e86743c03ce568b)offset

| void\* far\_ptr::offset |
| --- |

Far pointer offset, unused when invoking a task.

## [◆ ](#a756bf5b1059a1d637556aadbf687df31)sel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) far\_ptr::sel |
| --- |

Far pointer segment/gate selector.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[segmentation.h](segmentation_8h_source.md)

- [far\_ptr](structfar__ptr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
