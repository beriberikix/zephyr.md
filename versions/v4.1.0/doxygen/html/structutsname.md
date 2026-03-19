---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structutsname.html
original_path: doxygen/html/structutsname.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utsname Struct Reference

`#include <[utsname.h](utsname_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [sysname](#a8bfca811eed8101b2310200a96e9757e) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("Zephyr")] |
| char | [nodename](#afc4ee8a38fc0d85ac4f8fe1b669c3f74) [[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1] |
| char | [release](#afcc31cc768b481d10c887dcf56d64a1c) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("99.99.99-rc1")] |
| char | [version](#abe146e9be86c55a25881e6c58ba3ddf0) [[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1] |
| char | [machine](#a708b512fcd536a51fa7266899eec3964) [[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(CONFIG\_ARCH)] |

## Field Documentation

## [◆ ](#a708b512fcd536a51fa7266899eec3964)machine

| char utsname::machine[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(CONFIG\_ARCH)] |
| --- |

## [◆ ](#afc4ee8a38fc0d85ac4f8fe1b669c3f74)nodename

| char utsname::nodename[[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1] |
| --- |

## [◆ ](#afcc31cc768b481d10c887dcf56d64a1c)release

| char utsname::release[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("99.99.99-rc1")] |
| --- |

## [◆ ](#a8bfca811eed8101b2310200a96e9757e)sysname

| char utsname::sysname[[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("Zephyr")] |
| --- |

## [◆ ](#abe146e9be86c55a25881e6c58ba3ddf0)version

| char utsname::version[[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/sys/[utsname.h](utsname_8h_source.md)

- [utsname](structutsname.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
