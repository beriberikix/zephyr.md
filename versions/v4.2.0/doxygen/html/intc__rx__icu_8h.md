---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/intc__rx__icu_8h.html
original_path: doxygen/html/intc__rx__icu_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_rx\_icu.h File Reference

[Go to the source code of this file.](intc__rx__icu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rx\_irq\_dig\_filt\_s](structrx__irq__dig__filt__s.md) |

| Macros | |
| --- | --- |
| #define | [IRQ\_CFG\_PCLK\_DIV1](#a1f2e0aab110d6ad50ca923d97b7a5569)   (0) |
| #define | [IRQ\_CFG\_PCLK\_DIV8](#a886edc20620e3b7e376df37e90b81c1a)   (1) |
| #define | [IRQ\_CFG\_PCLK\_DIV32](#adf9e7efaa66840f836a94ba6972b0dff)   (2) |
| #define | [IRQ\_CFG\_PCLK\_DIV64](#a867e76951913679d9d1cd2ac5df79eda)   (3) |

| Typedefs | |
| --- | --- |
| typedef struct [rx\_irq\_dig\_filt\_s](structrx__irq__dig__filt__s.md) | [rx\_irq\_dig\_filt\_t](#ae5e7618b4871363e4b9443cbe01ef86d) |

| Enumerations | |
| --- | --- |
| enum | [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) {     [ICU\_LOW\_LEVEL](#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4) , [ICU\_FALLING](#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432) , [ICU\_RISING](#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3) , [ICU\_BOTH\_EDGE](#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650) ,     [ICU\_MODE\_NONE](#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8)   } |
| enum | [icu\_dig\_filt](#a4b89ff23dc526521af51a61f6d34431a) { [DISENABLE\_DIG\_FILT](#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01) , [ENABLE\_DIG\_FILT](#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d) } |

| Functions | |
| --- | --- |
| void | [rx\_icu\_clear\_ir\_flag](#a03cc2d22194251dd8942e2d95c3b3451) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irqn) |
| int | [rx\_icu\_get\_ir\_flag](#a43836995901c04ab8c734f28c4e57e73) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irqn) |
| int | [rx\_icu\_set\_irq\_control](#a32aadebfbc450fa354d6d176289fec0d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int pin\_irqn, enum [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) mode) |
| void | [rx\_icu\_set\_irq\_dig\_filt](#ac9bdc620911c67f607cf9ec5a49fd1b1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int pin\_irqn, [rx\_irq\_dig\_filt\_t](#ae5e7618b4871363e4b9443cbe01ef86d) dig\_filt) |

## Macro Definition Documentation

## [◆ ](#a1f2e0aab110d6ad50ca923d97b7a5569)IRQ\_CFG\_PCLK\_DIV1

| #define IRQ\_CFG\_PCLK\_DIV1   (0) |
| --- |

## [◆ ](#adf9e7efaa66840f836a94ba6972b0dff)IRQ\_CFG\_PCLK\_DIV32

| #define IRQ\_CFG\_PCLK\_DIV32   (2) |
| --- |

## [◆ ](#a867e76951913679d9d1cd2ac5df79eda)IRQ\_CFG\_PCLK\_DIV64

| #define IRQ\_CFG\_PCLK\_DIV64   (3) |
| --- |

## [◆ ](#a886edc20620e3b7e376df37e90b81c1a)IRQ\_CFG\_PCLK\_DIV8

| #define IRQ\_CFG\_PCLK\_DIV8   (1) |
| --- |

## Typedef Documentation

## [◆ ](#ae5e7618b4871363e4b9443cbe01ef86d)rx\_irq\_dig\_filt\_t

| typedef struct [rx\_irq\_dig\_filt\_s](structrx__irq__dig__filt__s.md) [rx\_irq\_dig\_filt\_t](#ae5e7618b4871363e4b9443cbe01ef86d) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a4b89ff23dc526521af51a61f6d34431a)icu\_dig\_filt

| enum [icu\_dig\_filt](#a4b89ff23dc526521af51a61f6d34431a) |
| --- |

| Enumerator | |
| --- | --- |
| DISENABLE\_DIG\_FILT |  |
| ENABLE\_DIG\_FILT |  |

## [◆ ](#aea25818bb1e7cf4bc3d1a6fce309207e)icu\_irq\_mode

| enum [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) |
| --- |

| Enumerator | |
| --- | --- |
| ICU\_LOW\_LEVEL |  |
| ICU\_FALLING |  |
| ICU\_RISING |  |
| ICU\_BOTH\_EDGE |  |
| ICU\_MODE\_NONE |  |

## Function Documentation

## [◆ ](#a03cc2d22194251dd8942e2d95c3b3451)rx\_icu\_clear\_ir\_flag()

| | void rx\_icu\_clear\_ir\_flag | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irqn* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a43836995901c04ab8c734f28c4e57e73)rx\_icu\_get\_ir\_flag()

| | int rx\_icu\_get\_ir\_flag | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irqn* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a32aadebfbc450fa354d6d176289fec0d)rx\_icu\_set\_irq\_control()

| | int rx\_icu\_set\_irq\_control | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *pin\_irqn*, | | --- | --- | --- | --- | |  |  | enum [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) | *mode* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac9bdc620911c67f607cf9ec5a49fd1b1)rx\_icu\_set\_irq\_dig\_filt()

| | void rx\_icu\_set\_irq\_dig\_filt | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *pin\_irqn*, | | --- | --- | --- | --- | |  |  | [rx\_irq\_dig\_filt\_t](#ae5e7618b4871363e4b9443cbe01ef86d) | *dig\_filt* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_rx\_icu.h](intc__rx__icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
