---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__dfu_8h.html
original_path: doxygen/html/usb__dfu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_dfu.h File Reference

USB Device Firmware Upgrade (DFU) public header.
[More...](#details)

`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`

[Go to the source code of this file.](usb__dfu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dfu\_runtime\_descriptor](structdfu__runtime__descriptor.md) |
|  | Run-Time Functional Descriptor. [More...](structdfu__runtime__descriptor.md#details) |

| Macros | |
| --- | --- |
| #define | [DFU\_SUBCLASS](#a86d100d1016e44b1a57d72f87394f49b)   0x01 |
|  | DFU Class Subclass. |
| #define | [DFU\_RT\_PROTOCOL](#a6da8cdd5028653f5008ae62371d68049)   0x01 |
|  | DFU Class runtime Protocol. |
| #define | [DFU\_MODE\_PROTOCOL](#ad44791964357de89e8f051a0eeff7b6c)   0x02 |
|  | DFU Class DFU mode Protocol. |
| #define | [DFU\_DETACH](#a1dbfcd9de4badc68f1a79720113dfa3d)   0x00 |
|  | DFU Class Specific Requests. |
| #define | [DFU\_DNLOAD](#aaf8b2bc0fa447ec925a47cee00916e4a)   0x01 |
| #define | [DFU\_UPLOAD](#a9ec42539a3b1d7a1fcb47383e5ae73b7)   0x02 |
| #define | [DFU\_GETSTATUS](#af45d9250c3e5dfb12a217bc08828cc06)   0x03 |
| #define | [DFU\_CLRSTATUS](#aff6ab40ddfc07a8e873aa4c8dde99fc8)   0x04 |
| #define | [DFU\_GETSTATE](#a41912ad6c650bf2df2b730f3d6d07849)   0x05 |
| #define | [DFU\_ABORT](#a9f0bb6811ae976a2cd8a7b42c19a8390)   0x06 |
| #define | [DFU\_FUNC\_DESC](#a2d6a59039cf1e8f97ba0443e7d20fd1c)   0x21 |
|  | DFU FUNCTIONAL descriptor type. |
| #define | [DFU\_ATTR\_WILL\_DETACH](#a8f41515182d31b45f06523deb89a0b6d)   0x08 |
|  | DFU attributes DFU Functional Descriptor. |
| #define | [DFU\_ATTR\_MANIFESTATION\_TOLERANT](#a9426f19a5d9970da8b7479e6f341e26c)   0x04 |
| #define | [DFU\_ATTR\_CAN\_UPLOAD](#a0fe01b636c7e5224a7cbd0ddcd3ac3e7)   0x02 |
| #define | [DFU\_ATTR\_CAN\_DNLOAD](#a07cbf2381d03bafb4d844cd00fd95079)   0x01 |
| #define | [DFU\_VERSION](#a7f333dc5f69079381f912b9b3ab9d202)   0x0110 |
|  | DFU Specification release. |

| Enumerations | |
| --- | --- |
| enum | [dfu\_status](#abcf2757cf1c6281a06a8a6f25ff2aa31) {     [statusOK](#abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19) , [errTARGET](#abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d) , [errFILE](#abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e) , [errWRITE](#abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1) ,     [errERASE](#abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54) , [errCHECK\_ERASED](#abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be) , [errPROG](#abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8) , [errVERIFY](#abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff) ,     [errADDRESS](#abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902) , [errNOTDONE](#abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998) , [errFIRMWARE](#abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb) , [errVENDOR](#abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210) ,     [errUSB](#abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947) , [errPOR](#abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb) , [errUNKNOWN](#abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471) , [errSTALLEDPKT](#abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788)   } |
|  | bStatus values for the DFU\_GETSTATUS response [More...](#abcf2757cf1c6281a06a8a6f25ff2aa31) |
| enum | [dfu\_state](#a3f025bde53c777c5e0493ef54bbeb143) {     [appIDLE](#a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa) , [appDETACH](#a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1) , [dfuIDLE](#a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c) , [dfuDNLOAD\_SYNC](#a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f) ,     [dfuDNBUSY](#a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e) , [dfuDNLOAD\_IDLE](#a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff) , [dfuMANIFEST\_SYNC](#a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c) , [dfuMANIFEST](#a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6) ,     [dfuMANIFEST\_WAIT\_RST](#a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8) , [dfuUPLOAD\_IDLE](#a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2) , [dfuERROR](#a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd)   } |
|  | bState values for the DFU\_GETSTATUS response [More...](#a3f025bde53c777c5e0493ef54bbeb143) |

| Functions | |
| --- | --- |
| void | [wait\_for\_usb\_dfu](#a892959f521c403e4ec295c252e75e5dc) ([k\_timeout\_t](structk__timeout__t.md) delay) |

## Detailed Description

USB Device Firmware Upgrade (DFU) public header.

Header follows the Device Class Specification for Device Firmware Upgrade Version 1.1

## Macro Definition Documentation

## [◆ ](#a9f0bb6811ae976a2cd8a7b42c19a8390)DFU\_ABORT

| #define DFU\_ABORT   0x06 |
| --- |

## [◆ ](#a07cbf2381d03bafb4d844cd00fd95079)DFU\_ATTR\_CAN\_DNLOAD

| #define DFU\_ATTR\_CAN\_DNLOAD   0x01 |
| --- |

## [◆ ](#a0fe01b636c7e5224a7cbd0ddcd3ac3e7)DFU\_ATTR\_CAN\_UPLOAD

| #define DFU\_ATTR\_CAN\_UPLOAD   0x02 |
| --- |

## [◆ ](#a9426f19a5d9970da8b7479e6f341e26c)DFU\_ATTR\_MANIFESTATION\_TOLERANT

| #define DFU\_ATTR\_MANIFESTATION\_TOLERANT   0x04 |
| --- |

## [◆ ](#a8f41515182d31b45f06523deb89a0b6d)DFU\_ATTR\_WILL\_DETACH

| #define DFU\_ATTR\_WILL\_DETACH   0x08 |
| --- |

DFU attributes DFU Functional Descriptor.

## [◆ ](#aff6ab40ddfc07a8e873aa4c8dde99fc8)DFU\_CLRSTATUS

| #define DFU\_CLRSTATUS   0x04 |
| --- |

## [◆ ](#a1dbfcd9de4badc68f1a79720113dfa3d)DFU\_DETACH

| #define DFU\_DETACH   0x00 |
| --- |

DFU Class Specific Requests.

## [◆ ](#aaf8b2bc0fa447ec925a47cee00916e4a)DFU\_DNLOAD

| #define DFU\_DNLOAD   0x01 |
| --- |

## [◆ ](#a2d6a59039cf1e8f97ba0443e7d20fd1c)DFU\_FUNC\_DESC

| #define DFU\_FUNC\_DESC   0x21 |
| --- |

DFU FUNCTIONAL descriptor type.

## [◆ ](#a41912ad6c650bf2df2b730f3d6d07849)DFU\_GETSTATE

| #define DFU\_GETSTATE   0x05 |
| --- |

## [◆ ](#af45d9250c3e5dfb12a217bc08828cc06)DFU\_GETSTATUS

| #define DFU\_GETSTATUS   0x03 |
| --- |

## [◆ ](#ad44791964357de89e8f051a0eeff7b6c)DFU\_MODE\_PROTOCOL

| #define DFU\_MODE\_PROTOCOL   0x02 |
| --- |

DFU Class DFU mode Protocol.

## [◆ ](#a6da8cdd5028653f5008ae62371d68049)DFU\_RT\_PROTOCOL

| #define DFU\_RT\_PROTOCOL   0x01 |
| --- |

DFU Class runtime Protocol.

## [◆ ](#a86d100d1016e44b1a57d72f87394f49b)DFU\_SUBCLASS

| #define DFU\_SUBCLASS   0x01 |
| --- |

DFU Class Subclass.

## [◆ ](#a9ec42539a3b1d7a1fcb47383e5ae73b7)DFU\_UPLOAD

| #define DFU\_UPLOAD   0x02 |
| --- |

## [◆ ](#a7f333dc5f69079381f912b9b3ab9d202)DFU\_VERSION

| #define DFU\_VERSION   0x0110 |
| --- |

DFU Specification release.

## Enumeration Type Documentation

## [◆ ](#a3f025bde53c777c5e0493ef54bbeb143)dfu\_state

| enum [dfu\_state](#a3f025bde53c777c5e0493ef54bbeb143) |
| --- |

bState values for the DFU\_GETSTATUS response

| Enumerator | |
| --- | --- |
| appIDLE |  |
| appDETACH |  |
| dfuIDLE |  |
| dfuDNLOAD\_SYNC |  |
| dfuDNBUSY |  |
| dfuDNLOAD\_IDLE |  |
| dfuMANIFEST\_SYNC |  |
| dfuMANIFEST |  |
| dfuMANIFEST\_WAIT\_RST |  |
| dfuUPLOAD\_IDLE |  |
| dfuERROR |  |

## [◆ ](#abcf2757cf1c6281a06a8a6f25ff2aa31)dfu\_status

| enum [dfu\_status](#abcf2757cf1c6281a06a8a6f25ff2aa31) |
| --- |

bStatus values for the DFU\_GETSTATUS response

| Enumerator | |
| --- | --- |
| statusOK |  |
| errTARGET |  |
| errFILE |  |
| errWRITE |  |
| errERASE |  |
| errCHECK\_ERASED |  |
| errPROG |  |
| errVERIFY |  |
| errADDRESS |  |
| errNOTDONE |  |
| errFIRMWARE |  |
| errVENDOR |  |
| errUSB |  |
| errPOR |  |
| errUNKNOWN |  |
| errSTALLEDPKT |  |

## Function Documentation

## [◆ ](#a892959f521c403e4ec295c252e75e5dc)wait\_for\_usb\_dfu()

| void wait\_for\_usb\_dfu | ( | [k\_timeout\_t](structk__timeout__t.md) | *delay* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_dfu.h](usb__dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
