---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gic_8h.html
original_path: doxygen/html/gic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gic.h File Reference

Driver for ARM Generic Interrupt Controller.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](gic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651)   [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_gic), 0) |
| #define | [GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)   [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_gic), 1) |
| #define | [GICD\_CTLR](#a00f17ebce4b31e38e18375340fdf3826)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x0) |
| #define | [GICD\_TYPER](#a1b97217a477f13f173ff4a22c0aeeef6)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x4) |
| #define | [GICD\_IIDR](#a88abd454e14abb10903e32cc83649e07)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x8) |
| #define | [GICD\_IGROUPRn](#a1080fbe96176a41ccf2bd2387ff0db63)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x80) |
| #define | [GICD\_ISENABLERn](#a310ab6442912860cc32c4728323aa77d)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x100) |
| #define | [GICD\_ICENABLERn](#a5c3d3ec71773c06de84fae6e9a4e0a09)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x180) |
| #define | [GICD\_ISPENDRn](#a6f6edc1558ef636d46f09b68b7abe025)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x200) |
| #define | [GICD\_ICPENDRn](#aeb43e488b1b2f321aa04973b92f55fde)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x280) |
| #define | [GICD\_ISACTIVERn](#a166410e3d61c7b967df532db8b541bf6)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x300) |
| #define | [GICD\_IPRIORITYRn](#ac55442a1b5748b8fcc46a9630ecf1645)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x400) |
| #define | [GICD\_ITARGETSRn](#a9b05ed54bb00c209d8774edea5368d5d)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x800) |
| #define | [GICD\_ICFGRn](#a4683149b0af23adbf4b1c149be5d9fe5)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0xc00) |
| #define | [GICD\_SGIR](#a5125b5f77951f0e882e002aac406beec)   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0xf00) |
| #define | [GICC\_CTLR](#a11871e15a62cbfcc1e54f3dd2ce21e74)   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x0) |
| #define | [GICC\_PMR](#a8d72b8216b091c1d148b5812bc46e7d4)   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x4) |
| #define | [GICC\_BPR](#acef579bca73eb22cc132808fcfede353)   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x8) |
| #define | [GICC\_IAR](#a61672c3cde5301e076793c2ad904cdb9)   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0xc) |
| #define | [GICC\_EOIR](#af92519fe60b0cf2183a6100bea15dd43)   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x10) |
| #define | [GICC\_CTLR\_ENABLEGRP0](#a518810ec411ebf4fb128a86c3e256333)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [GICC\_CTLR\_ENABLEGRP1](#a692e86e4ede5319e7480a358fe75172b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [GICC\_CTLR\_ENABLE\_MASK](#ad3403f63efc5ce1dc9f257602f2ff0ae)   ([GICC\_CTLR\_ENABLEGRP0](#a518810ec411ebf4fb128a86c3e256333) | [GICC\_CTLR\_ENABLEGRP1](#a692e86e4ede5319e7480a358fe75172b)) |
| #define | [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(x) |
| #define | [GICD\_SGIR\_TGTFILT\_CPULIST](#a907207ff57799c57a6b84a928738d205)   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b00) |
| #define | [GICD\_SGIR\_TGTFILT\_ALLBUTREQ](#a64b98ce10603ac8cb7bb356fa162a344)   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b01) |
| #define | [GICD\_SGIR\_TGTFILT\_REQONLY](#ae759ef6f311a7279db5e7ccd68c80863)   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b10) |
| #define | [GICD\_SGIR\_CPULIST](#a4dff39b6ec90ed14dea04fdd25abc1ce)(x) |
| #define | [GICD\_SGIR\_CPULIST\_CPU](#a124b8c93f6902e9166447dd735f5dc1a)(n) |
| #define | [GICD\_SGIR\_CPULIST\_MASK](#a011479af47f54dfc94330092191aaac5)   0xff |
| #define | [GICD\_SGIR\_NSATT](#a041824e4a8176f8bbbdac5bafe06fae7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [GICD\_SGIR\_SGIINTID](#ae388207ec492448a22511cee6dcecedc)(x) |
| #define | [GICD\_ICFGR\_MASK](#a44b5b4941c426cd73350eeea005beb8a)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(2) |
| #define | [GICD\_ICFGR\_TYPE](#a11ed86dd29db285527ff4474958ade81)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [GICD\_TYPER\_ITLINESNUM\_MASK](#a74cbf9f2c19fb1a09f8936958b02503a)   0x1f |
| #define | [GICD\_TYPER\_IDBITS](#a62397b69dbb93be1a404d14c195cdb2f)(typer) |
| #define | [GIC\_SGI\_INT\_BASE](#a87acbf5e0124561ba231e95cca1bbc7a)   0 |
| #define | [GIC\_PPI\_INT\_BASE](#a63bca268593477e8c0b6bc58aa3ee85c)   16 |
| #define | [GIC\_IS\_SGI](#a9bb04de2bd1f9d4e304ecdbea6a63a85)(intid) |
| #define | [GIC\_SPI\_INT\_BASE](#ad9e9ba1264c9e57922cc0b8ad2e4dfba)   32 |
| #define | [GIC\_SPI\_MAX\_INTID](#a1deeb13c2ac681cb120c06b18dee2b91)   1019 |
| #define | [GIC\_IS\_SPI](#aa2672b14cfaa1a943bf1633e208ba288)(intid) |
| #define | [GIC\_NUM\_INTR\_PER\_REG](#aed0af65dd3212045aeb0906d2d937ad5)   32 |
| #define | [GIC\_NUM\_CFG\_PER\_REG](#ad563564c4794a65475474fd8c19f7b41)   16 |
| #define | [GIC\_NUM\_PRI\_PER\_REG](#abb00f7fda87b16903a1fbcdd85d660bf)   4 |
| #define | [GIC\_IDLE\_PRIO](#ae29667ceb670f4fabfc442350e8d4152)   0xff |
| #define | [GIC\_PRI\_MASK](#aaa5afc14eff8f002060b52030783cc47)   0xff |
| #define | [GIC\_INT\_DEF\_PRI\_X4](#a94e122b157b3e50259581bd1d2f319a1)   0xa0a0a0a0 |
| #define | [GIC\_INTID\_SPURIOUS](#a6ac20d04f13472d5dd915197af39aaf3)   1023 |
| #define | [GIC\_NUM\_CPU\_IF](#a24a62a86eb885f9f47e8bfdc430e8292)   CONFIG\_MP\_MAX\_NUM\_CPUS |

| Functions | |
| --- | --- |
| void | [arm\_gic\_irq\_enable](#a585b5b22a16dab6999ab94dae30f4e71) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Enable interrupt. |
| void | [arm\_gic\_irq\_disable](#a3f5ec5c6b16fbac66cd02459d6045742) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Disable interrupt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arm\_gic\_irq\_is\_enabled](#acfa77cdcf46cad1181476bc3b974b58e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Check if an interrupt is enabled. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arm\_gic\_irq\_is\_pending](#ad0cc0929cc6e0336448d45ebd27a45bd) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Check if an interrupt is pending. |
| void | [arm\_gic\_irq\_clear\_pending](#a2980cdb020c9d8a886bf9d4fd485121b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Clear the pending irq. |
| void | [arm\_gic\_irq\_set\_priority](#ad5eb3fc988f7077dc9600e62d768b076) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int prio, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set interrupt priority. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arm\_gic\_get\_active](#ae545623722c1b45fda2b58155f3fd0ed) (void) |
|  | Get active interrupt ID. |
| void | [arm\_gic\_eoi](#a4bfb597ef68cc7f83d86ba52e099e3b4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Signal end-of-interrupt. |
| void | [arm\_gic\_secondary\_init](#a3c2d3adf07e2d48bdf863d8142a685aa) (void) |
|  | Initialize GIC of secondary cores. |
| void | [gic\_raise\_sgi](#a08291705f002f01687cf507abbb410dc) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sgi\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_aff, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) target\_list) |
|  | raise SGI to target cores |

## Detailed Description

Driver for ARM Generic Interrupt Controller.

The Generic Interrupt Controller (GIC) is the default interrupt controller for the ARM A and R profile cores. This driver is used by the ARM arch implementation to handle interrupts.

## Macro Definition Documentation

## [◆ ](#a855f96fbf6e3c5645d7e4d610eb98664)GIC\_CPU\_BASE

| #define GIC\_CPU\_BASE   [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_gic), 1) |
| --- |

## [◆ ](#adb371115c787d786755ca23eedc6a651)GIC\_DIST\_BASE

| #define GIC\_DIST\_BASE   [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_gic), 0) |
| --- |

## [◆ ](#ae29667ceb670f4fabfc442350e8d4152)GIC\_IDLE\_PRIO

| #define GIC\_IDLE\_PRIO   0xff |
| --- |

## [◆ ](#a94e122b157b3e50259581bd1d2f319a1)GIC\_INT\_DEF\_PRI\_X4

| #define GIC\_INT\_DEF\_PRI\_X4   0xa0a0a0a0 |
| --- |

## [◆ ](#a6ac20d04f13472d5dd915197af39aaf3)GIC\_INTID\_SPURIOUS

| #define GIC\_INTID\_SPURIOUS   1023 |
| --- |

## [◆ ](#a9bb04de2bd1f9d4e304ecdbea6a63a85)GIC\_IS\_SGI

| #define GIC\_IS\_SGI | ( |  | *intid* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((intid) >= [GIC\_SGI\_INT\_BASE](#a87acbf5e0124561ba231e95cca1bbc7a)) && \

((intid) < [GIC\_PPI\_INT\_BASE](#a63bca268593477e8c0b6bc58aa3ee85c)))

[GIC\_PPI\_INT\_BASE](#a63bca268593477e8c0b6bc58aa3ee85c)

#define GIC\_PPI\_INT\_BASE

**Definition** gic.h:226

[GIC\_SGI\_INT\_BASE](#a87acbf5e0124561ba231e95cca1bbc7a)

#define GIC\_SGI\_INT\_BASE

**Definition** gic.h:225

## [◆ ](#aa2672b14cfaa1a943bf1633e208ba288)GIC\_IS\_SPI

| #define GIC\_IS\_SPI | ( |  | *intid* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((intid) >= [GIC\_SPI\_INT\_BASE](#ad9e9ba1264c9e57922cc0b8ad2e4dfba)) && \

((intid) <= [GIC\_SPI\_MAX\_INTID](#a1deeb13c2ac681cb120c06b18dee2b91)))

[GIC\_SPI\_MAX\_INTID](#a1deeb13c2ac681cb120c06b18dee2b91)

#define GIC\_SPI\_MAX\_INTID

**Definition** gic.h:234

[GIC\_SPI\_INT\_BASE](#ad9e9ba1264c9e57922cc0b8ad2e4dfba)

#define GIC\_SPI\_INT\_BASE

**Definition** gic.h:232

## [◆ ](#ad563564c4794a65475474fd8c19f7b41)GIC\_NUM\_CFG\_PER\_REG

| #define GIC\_NUM\_CFG\_PER\_REG   16 |
| --- |

## [◆ ](#a24a62a86eb885f9f47e8bfdc430e8292)GIC\_NUM\_CPU\_IF

| #define GIC\_NUM\_CPU\_IF   CONFIG\_MP\_MAX\_NUM\_CPUS |
| --- |

## [◆ ](#aed0af65dd3212045aeb0906d2d937ad5)GIC\_NUM\_INTR\_PER\_REG

| #define GIC\_NUM\_INTR\_PER\_REG   32 |
| --- |

## [◆ ](#abb00f7fda87b16903a1fbcdd85d660bf)GIC\_NUM\_PRI\_PER\_REG

| #define GIC\_NUM\_PRI\_PER\_REG   4 |
| --- |

## [◆ ](#a63bca268593477e8c0b6bc58aa3ee85c)GIC\_PPI\_INT\_BASE

| #define GIC\_PPI\_INT\_BASE   16 |
| --- |

## [◆ ](#aaa5afc14eff8f002060b52030783cc47)GIC\_PRI\_MASK

| #define GIC\_PRI\_MASK   0xff |
| --- |

## [◆ ](#a87acbf5e0124561ba231e95cca1bbc7a)GIC\_SGI\_INT\_BASE

| #define GIC\_SGI\_INT\_BASE   0 |
| --- |

## [◆ ](#ad9e9ba1264c9e57922cc0b8ad2e4dfba)GIC\_SPI\_INT\_BASE

| #define GIC\_SPI\_INT\_BASE   32 |
| --- |

## [◆ ](#a1deeb13c2ac681cb120c06b18dee2b91)GIC\_SPI\_MAX\_INTID

| #define GIC\_SPI\_MAX\_INTID   1019 |
| --- |

## [◆ ](#acef579bca73eb22cc132808fcfede353)GICC\_BPR

| #define GICC\_BPR   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x8) |
| --- |

## [◆ ](#a11871e15a62cbfcc1e54f3dd2ce21e74)GICC\_CTLR

| #define GICC\_CTLR   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x0) |
| --- |

## [◆ ](#ad3403f63efc5ce1dc9f257602f2ff0ae)GICC\_CTLR\_ENABLE\_MASK

| #define GICC\_CTLR\_ENABLE\_MASK   ([GICC\_CTLR\_ENABLEGRP0](#a518810ec411ebf4fb128a86c3e256333) | [GICC\_CTLR\_ENABLEGRP1](#a692e86e4ede5319e7480a358fe75172b)) |
| --- |

## [◆ ](#a518810ec411ebf4fb128a86c3e256333)GICC\_CTLR\_ENABLEGRP0

| #define GICC\_CTLR\_ENABLEGRP0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a692e86e4ede5319e7480a358fe75172b)GICC\_CTLR\_ENABLEGRP1

| #define GICC\_CTLR\_ENABLEGRP1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#af92519fe60b0cf2183a6100bea15dd43)GICC\_EOIR

| #define GICC\_EOIR   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x10) |
| --- |

## [◆ ](#a61672c3cde5301e076793c2ad904cdb9)GICC\_IAR

| #define GICC\_IAR   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0xc) |
| --- |

## [◆ ](#a8d72b8216b091c1d148b5812bc46e7d4)GICC\_PMR

| #define GICC\_PMR   ([GIC\_CPU\_BASE](#a855f96fbf6e3c5645d7e4d610eb98664) + 0x4) |
| --- |

## [◆ ](#a00f17ebce4b31e38e18375340fdf3826)GICD\_CTLR

| #define GICD\_CTLR   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x0) |
| --- |

## [◆ ](#a5c3d3ec71773c06de84fae6e9a4e0a09)GICD\_ICENABLERn

| #define GICD\_ICENABLERn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x180) |
| --- |

## [◆ ](#a44b5b4941c426cd73350eeea005beb8a)GICD\_ICFGR\_MASK

| #define GICD\_ICFGR\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(2) |
| --- |

## [◆ ](#a11ed86dd29db285527ff4474958ade81)GICD\_ICFGR\_TYPE

| #define GICD\_ICFGR\_TYPE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4683149b0af23adbf4b1c149be5d9fe5)GICD\_ICFGRn

| #define GICD\_ICFGRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0xc00) |
| --- |

## [◆ ](#aeb43e488b1b2f321aa04973b92f55fde)GICD\_ICPENDRn

| #define GICD\_ICPENDRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x280) |
| --- |

## [◆ ](#a1080fbe96176a41ccf2bd2387ff0db63)GICD\_IGROUPRn

| #define GICD\_IGROUPRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x80) |
| --- |

## [◆ ](#a88abd454e14abb10903e32cc83649e07)GICD\_IIDR

| #define GICD\_IIDR   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x8) |
| --- |

## [◆ ](#ac55442a1b5748b8fcc46a9630ecf1645)GICD\_IPRIORITYRn

| #define GICD\_IPRIORITYRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x400) |
| --- |

## [◆ ](#a166410e3d61c7b967df532db8b541bf6)GICD\_ISACTIVERn

| #define GICD\_ISACTIVERn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x300) |
| --- |

## [◆ ](#a310ab6442912860cc32c4728323aa77d)GICD\_ISENABLERn

| #define GICD\_ISENABLERn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x100) |
| --- |

## [◆ ](#a6f6edc1558ef636d46f09b68b7abe025)GICD\_ISPENDRn

| #define GICD\_ISPENDRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x200) |
| --- |

## [◆ ](#a9b05ed54bb00c209d8774edea5368d5d)GICD\_ITARGETSRn

| #define GICD\_ITARGETSRn   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x800) |
| --- |

## [◆ ](#a5125b5f77951f0e882e002aac406beec)GICD\_SGIR

| #define GICD\_SGIR   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0xf00) |
| --- |

## [◆ ](#a4dff39b6ec90ed14dea04fdd25abc1ce)GICD\_SGIR\_CPULIST

| #define GICD\_SGIR\_CPULIST | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << 16)

## [◆ ](#a124b8c93f6902e9166447dd735f5dc1a)GICD\_SGIR\_CPULIST\_CPU

| #define GICD\_SGIR\_CPULIST\_CPU | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[GICD\_SGIR\_CPULIST](#a4dff39b6ec90ed14dea04fdd25abc1ce)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(n))

[GICD\_SGIR\_CPULIST](#a4dff39b6ec90ed14dea04fdd25abc1ce)

#define GICD\_SGIR\_CPULIST(x)

**Definition** gic.h:201

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#a011479af47f54dfc94330092191aaac5)GICD\_SGIR\_CPULIST\_MASK

| #define GICD\_SGIR\_CPULIST\_MASK   0xff |
| --- |

## [◆ ](#a041824e4a8176f8bbbdac5bafe06fae7)GICD\_SGIR\_NSATT

| #define GICD\_SGIR\_NSATT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#ae388207ec492448a22511cee6dcecedc)GICD\_SGIR\_SGIINTID

| #define GICD\_SGIR\_SGIINTID | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x)

## [◆ ](#abb0a8279fd1bafe13b5b79ec7aeb3f90)GICD\_SGIR\_TGTFILT

| #define GICD\_SGIR\_TGTFILT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << 24)

## [◆ ](#a64b98ce10603ac8cb7bb356fa162a344)GICD\_SGIR\_TGTFILT\_ALLBUTREQ

| #define GICD\_SGIR\_TGTFILT\_ALLBUTREQ   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b01) |
| --- |

## [◆ ](#a907207ff57799c57a6b84a928738d205)GICD\_SGIR\_TGTFILT\_CPULIST

| #define GICD\_SGIR\_TGTFILT\_CPULIST   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b00) |
| --- |

## [◆ ](#ae759ef6f311a7279db5e7ccd68c80863)GICD\_SGIR\_TGTFILT\_REQONLY

| #define GICD\_SGIR\_TGTFILT\_REQONLY   [GICD\_SGIR\_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)(0b10) |
| --- |

## [◆ ](#a1b97217a477f13f173ff4a22c0aeeef6)GICD\_TYPER

| #define GICD\_TYPER   ([GIC\_DIST\_BASE](#adb371115c787d786755ca23eedc6a651) + 0x4) |
| --- |

## [◆ ](#a62397b69dbb93be1a404d14c195cdb2f)GICD\_TYPER\_IDBITS

| #define GICD\_TYPER\_IDBITS | ( |  | *typer* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((typer) >> 19) & 0x1f) + 1)

## [◆ ](#a74cbf9f2c19fb1a09f8936958b02503a)GICD\_TYPER\_ITLINESNUM\_MASK

| #define GICD\_TYPER\_ITLINESNUM\_MASK   0x1f |
| --- |

## Function Documentation

## [◆ ](#a4bfb597ef68cc7f83d86ba52e099e3b4)arm\_gic\_eoi()

| void arm\_gic\_eoi | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Signal end-of-interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#ae545623722c1b45fda2b58155f3fd0ed)arm\_gic\_get\_active()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arm\_gic\_get\_active | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get active interrupt ID.

Returns
:   Returns the ID of an active interrupt

## [◆ ](#a2980cdb020c9d8a886bf9d4fd485121b)arm\_gic\_irq\_clear\_pending()

| void arm\_gic\_irq\_clear\_pending | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear the pending irq.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#a3f5ec5c6b16fbac66cd02459d6045742)arm\_gic\_irq\_disable()

| void arm\_gic\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#a585b5b22a16dab6999ab94dae30f4e71)arm\_gic\_irq\_enable()

| void arm\_gic\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#acfa77cdcf46cad1181476bc3b974b58e)arm\_gic\_irq\_is\_enabled()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arm\_gic\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Check if an interrupt is enabled.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

Returns
:   Returns true if interrupt is enabled, false otherwise

## [◆ ](#ad0cc0929cc6e0336448d45ebd27a45bd)arm\_gic\_irq\_is\_pending()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arm\_gic\_irq\_is\_pending | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Check if an interrupt is pending.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

Returns
:   Returns true if interrupt is pending, false otherwise

## [◆ ](#ad5eb3fc988f7077dc9600e62d768b076)arm\_gic\_irq\_set\_priority()

| void arm\_gic\_irq\_set\_priority | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *prio*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *flags* ) |

Set interrupt priority.

Parameters
:   | irq | interrupt ID |
    | --- | --- |
    | prio | interrupt priority |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | interrupt flags |

## [◆ ](#a3c2d3adf07e2d48bdf863d8142a685aa)arm\_gic\_secondary\_init()

| void arm\_gic\_secondary\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize GIC of secondary cores.

## [◆ ](#a08291705f002f01687cf507abbb410dc)gic\_raise\_sgi()

| void gic\_raise\_sgi | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *sgi\_id*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *target\_aff*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *target\_list* ) |

raise SGI to target cores

Parameters
:   | sgi\_id | SGI ID 0 to 15 |
    | --- | --- |
    | target\_aff | target affinity in mpidr form. Aff level 1 2 3 will be extracted by api. |
    | target\_list | bitmask of target cores |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gic.h](gic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
