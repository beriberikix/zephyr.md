---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structutsname.html
original_path: doxygen/html/structutsname.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utsname Struct Reference

`#include <[utsname.h](utsname_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [sysname](#a8bfca811eed8101b2310200a96e9757e) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("Zephyr")] |
| char | [nodename](#adb9b79651cf171e090b5e9cf12804320) [CONFIG\_POSIX\_UNAME\_NODENAME\_LEN+1] |
| char | [release](#afcc31cc768b481d10c887dcf56d64a1c) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("99.99.99-rc1")] |
| char | [version](#a5fdfa66e563e8112c517d3cd95133eaf) [CONFIG\_POSIX\_UNAME\_VERSION\_LEN+1] |
| char | [machine](#a708b512fcd536a51fa7266899eec3964) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(CONFIG\_ARCH)] |

## Field Documentation

## [◆ ](#a708b512fcd536a51fa7266899eec3964)machine

| char utsname::machine[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(CONFIG\_ARCH)] |
| --- |

## [◆ ](#adb9b79651cf171e090b5e9cf12804320)nodename

| char utsname::nodename[CONFIG\_POSIX\_UNAME\_NODENAME\_LEN+1] |
| --- |

## [◆ ](#afcc31cc768b481d10c887dcf56d64a1c)release

| char utsname::release[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("99.99.99-rc1")] |
| --- |

## [◆ ](#a8bfca811eed8101b2310200a96e9757e)sysname

| char utsname::sysname[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("Zephyr")] |
| --- |

## [◆ ](#a5fdfa66e563e8112c517d3cd95133eaf)version

| char utsname::version[CONFIG\_POSIX\_UNAME\_VERSION\_LEN+1] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/sys/[utsname.h](utsname_8h_source.md)

- [utsname](structutsname.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
