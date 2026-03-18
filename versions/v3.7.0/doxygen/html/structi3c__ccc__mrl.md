---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__ccc__mrl.html
original_path: doxygen/html/structi3c__ccc__mrl.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_mrl Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a381d52439049c6a13d232e4e94d17335) |
|  | Maximum Read Length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ibi\_len](#a7480df4486c9eb8a11581e42ff3b6b67) |
|  | Optional IBI Payload Size. |

## Detailed Description

Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length).

Note
:   For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

## Field Documentation

## [◆ ](#a7480df4486c9eb8a11581e42ff3b6b67)ibi\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_mrl::ibi\_len |
| --- |

Optional IBI Payload Size.

## [◆ ](#a381d52439049c6a13d232e4e94d17335)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_mrl::len |
| --- |

Maximum Read Length.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_mrl](structi3c__ccc__mrl.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
