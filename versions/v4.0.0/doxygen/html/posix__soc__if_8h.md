---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix__soc__if_8h.html
original_path: doxygen/html/posix__soc__if_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_soc\_if.h File Reference

`#include <[zephyr/arch/posix/posix_trace.h](posix__trace_8h_source.md)>`  
`#include "soc_irq.h"`

[Go to the source code of this file.](posix__soc__if_8h_source.md)

| Functions | |
| --- | --- |
| void | [posix\_halt\_cpu](#a924db5712e0c7e6b3595dfc723281329) (void) |
| void | [posix\_atomic\_halt\_cpu](#a400f264c1c3a8838c589577b287d42a0) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int imask) |
| void | [posix\_irq\_enable](#a05199832c06ba854431bbdbfe2302918) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [posix\_irq\_disable](#a2d1cbc3efb24d49b151ad9506e1132c7) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [posix\_irq\_is\_enabled](#ad2d42fd9f28c04e0b37c4f34ed0dd711) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [posix\_irq\_lock](#a53106413853e29d1eeebbf1b5c4d36a5) (void) |
| void | [posix\_irq\_unlock](#abf80b27ff517e32514e952c53e6c67c6) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| void | [posix\_irq\_full\_unlock](#a18ad9bcd5676c282e5527e746550dfbb) (void) |
| int | [posix\_get\_current\_irq](#af6eefac1419bea5bca9a3c1ce48bcf0e) (void) |
| void | [posix\_sw\_set\_pending\_IRQ](#a8aa652da8beecd80c6036e1ad6f8fddd) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int IRQn) |
| void | [posix\_sw\_clear\_pending\_IRQ](#aa26107cfff573cc9028b321a62684c46) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int IRQn) |

## Function Documentation

## [◆ ](#a400f264c1c3a8838c589577b287d42a0)posix\_atomic\_halt\_cpu()

| void posix\_atomic\_halt\_cpu | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *imask* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af6eefac1419bea5bca9a3c1ce48bcf0e)posix\_get\_current\_irq()

| int posix\_get\_current\_irq | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a924db5712e0c7e6b3595dfc723281329)posix\_halt\_cpu()

| void posix\_halt\_cpu | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2d1cbc3efb24d49b151ad9506e1132c7)posix\_irq\_disable()

| void posix\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a05199832c06ba854431bbdbfe2302918)posix\_irq\_enable()

| void posix\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a18ad9bcd5676c282e5527e746550dfbb)posix\_irq\_full\_unlock()

| void posix\_irq\_full\_unlock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad2d42fd9f28c04e0b37c4f34ed0dd711)posix\_irq\_is\_enabled()

| int posix\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a53106413853e29d1eeebbf1b5c4d36a5)posix\_irq\_lock()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int posix\_irq\_lock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#abf80b27ff517e32514e952c53e6c67c6)posix\_irq\_unlock()

| void posix\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa26107cfff573cc9028b321a62684c46)posix\_sw\_clear\_pending\_IRQ()

| void posix\_sw\_clear\_pending\_IRQ | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *IRQn* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8aa652da8beecd80c6036e1ad6f8fddd)posix\_sw\_set\_pending\_IRQ()

| void posix\_sw\_set\_pending\_IRQ | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *IRQn* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [posix\_soc\_if.h](posix__soc__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
