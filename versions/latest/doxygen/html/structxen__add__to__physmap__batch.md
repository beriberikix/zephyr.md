---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__add__to__physmap__batch.html
original_path: doxygen/html/structxen__add__to__physmap__batch.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_add\_to\_physmap\_batch Struct Reference

`#include <[memory.h](public_2memory_8h_source.md)>`

| Public Member Functions | |
| --- | --- |
|  | [XEN\_GUEST\_HANDLE](#ae21559560d005afcadcb4e63306ea5ed) ([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) idxs |
|  | [XEN\_GUEST\_HANDLE](#acd92848c32fd218aa28a8544db8bf780) ([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)) gpfns |
|  | [XEN\_GUEST\_HANDLE](#ac3dcc0adb6f94a4c040658f3366bf098) (int) errs |

| Data Fields | |
| --- | --- |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [domid](#a9e7325563f39256e35fbada075bc1e4c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [space](#a2d0bd5efa6e425e4c583c1fb8e028fe5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [size](#a47f58749bd833fc81f4ac7e714530a4b) |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [foreign\_domid](#aeba66d4e050258147caf95828c3fa1d4) |

## Member Function Documentation

## [◆ ](#ac3dcc0adb6f94a4c040658f3366bf098)XEN\_GUEST\_HANDLE() [1/3]

| xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE | ( | int |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#acd92848c32fd218aa28a8544db8bf780)XEN\_GUEST\_HANDLE() [2/3]

| xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE | ( | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae21559560d005afcadcb4e63306ea5ed)XEN\_GUEST\_HANDLE() [3/3]

| xen\_add\_to\_physmap\_batch::XEN\_GUEST\_HANDLE | ( | [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Field Documentation

## [◆ ](#a9e7325563f39256e35fbada075bc1e4c)domid

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) xen\_add\_to\_physmap\_batch::domid |
| --- |

## [◆ ](#aeba66d4e050258147caf95828c3fa1d4)foreign\_domid

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) xen\_add\_to\_physmap\_batch::foreign\_domid |
| --- |

## [◆ ](#a47f58749bd833fc81f4ac7e714530a4b)size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xen\_add\_to\_physmap\_batch::size |
| --- |

## [◆ ](#a2d0bd5efa6e425e4c583c1fb8e028fe5)space

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xen\_add\_to\_physmap\_batch::space |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[memory.h](public_2memory_8h_source.md)

- [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
