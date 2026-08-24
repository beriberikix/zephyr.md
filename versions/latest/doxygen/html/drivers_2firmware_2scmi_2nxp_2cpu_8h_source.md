---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html
original_path: doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](drivers_2firmware_2scmi_2nxp_2cpu_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CPU\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CPU\_H\_

14

15#include <[zephyr/drivers/firmware/scmi/protocol.h](drivers_2firmware_2scmi_2protocol_8h.md)>

16#if \_\_has\_include("scmi\_cpu\_soc.h")

17#include <scmi\_cpu\_soc.h>

18#endif

19

[ 20](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#af2b7e2beb6bf8c54aafd42bda71a0374)#define SCMI\_CPU\_SLEEP\_FLAG\_IRQ\_MUX 0x1U

21

[ 22](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a893e63347e801f01f1da912ed7dccc64)#define SCMI\_PROTOCOL\_CPU\_DOMAIN 130

23

[ 30](structscmi__cpu__sleep__mode__config.md)struct [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md) {

[ 31](structscmi__cpu__sleep__mode__config.md#ab14413f0c5cdd1a061235a750df316e0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cpu\_id](structscmi__cpu__sleep__mode__config.md#ab14413f0c5cdd1a061235a750df316e0);

[ 32](structscmi__cpu__sleep__mode__config.md#ab11fddc7614f03706180cf12151d5e7d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structscmi__cpu__sleep__mode__config.md#ab11fddc7614f03706180cf12151d5e7d);

[ 33](structscmi__cpu__sleep__mode__config.md#a29781dcbdbaf3fd2e6aa840e78f26615) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sleep\_mode](structscmi__cpu__sleep__mode__config.md#a29781dcbdbaf3fd2e6aa840e78f26615);

34};

35

[ 39](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672)enum [scmi\_cpu\_domain\_message](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672) {

[ 40](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a4f38f51833761413a69fc9c0832c184a) [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a4f38f51833761413a69fc9c0832c184a) = 0x0,

[ 41](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a23078d9d4a3f2c6f8764fae8bbc1e29f) [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a23078d9d4a3f2c6f8764fae8bbc1e29f) = 0x1,

[ 42](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ace67a725f9f6692139fecdfe7bc0f610) [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ace67a725f9f6692139fecdfe7bc0f610) = 0x2,

[ 43](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a81c78cfa362e3b9be276a6dccf971a77) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_DOMAIN\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a81c78cfa362e3b9be276a6dccf971a77) = 0x3,

[ 44](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a2e35dbcb409b234c41b435e373095b69) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_START](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a2e35dbcb409b234c41b435e373095b69) = 0x4,

[ 45](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a31df2a02066ffdec65b7c3f42c382961) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_STOP](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a31df2a02066ffdec65b7c3f42c382961) = 0x5,

[ 46](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aca337c082e8717d4bcbfd63826914328) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_RESET\_VECTOR\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aca337c082e8717d4bcbfd63826914328) = 0x6,

[ 47](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a829fe5849691731336da95eeff60d481) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_SLEEP\_MODE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a829fe5849691731336da95eeff60d481) = 0x7,

[ 48](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a34dedf8a4ea9686eeec89c6fd118aebe) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_IRQ\_WAKE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a34dedf8a4ea9686eeec89c6fd118aebe) = 0x8,

[ 49](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a8fa78652734f276abc4af0b955299b78) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_NON\_IRQ\_WAKE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a8fa78652734f276abc4af0b955299b78) = 0x9,

[ 50](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a0b40038d48738f6685686c4f9f1576f9) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PD\_LPM\_CONFIG\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a0b40038d48738f6685686c4f9f1576f9) = 0xA,

[ 51](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aa9076f4531ca885a3c58ef060cfa304b) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PER\_LPM\_CONFIG\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aa9076f4531ca885a3c58ef060cfa304b) = 0xB,

[ 52](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ac47a18fb60f00abfbdcf0c3fd1fee4d7) [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_INFO\_GET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ac47a18fb60f00abfbdcf0c3fd1fee4d7) = 0xC,

[ 53](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a9de9b4d325a02bff24cfb9b9a0d6b3a7) [SCMI\_CPU\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a9de9b4d325a02bff24cfb9b9a0d6b3a7) = 0x10,

54};

55

[ 65](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#ac62bef1626449da2f816a2be755b762d)int [scmi\_cpu\_sleep\_mode\_set](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#ac62bef1626449da2f816a2be755b762d)(struct [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md) \*cfg);

66

67#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_CPU\_H\_ \*/

[scmi\_cpu\_domain\_message](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672)

scmi\_cpu\_domain\_message

CPU domain protocol command message IDs.

**Definition** cpu.h:39

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PD\_LPM\_CONFIG\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a0b40038d48738f6685686c4f9f1576f9)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PD\_LPM\_CONFIG\_SET

**Definition** cpu.h:50

[SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a23078d9d4a3f2c6f8764fae8bbc1e29f)

@ SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES

**Definition** cpu.h:41

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_START](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a2e35dbcb409b234c41b435e373095b69)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_START

**Definition** cpu.h:44

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_STOP](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a31df2a02066ffdec65b7c3f42c382961)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_STOP

**Definition** cpu.h:45

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_IRQ\_WAKE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a34dedf8a4ea9686eeec89c6fd118aebe)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_IRQ\_WAKE\_SET

**Definition** cpu.h:48

[SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a4f38f51833761413a69fc9c0832c184a)

@ SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_VERSION

**Definition** cpu.h:40

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_DOMAIN\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a81c78cfa362e3b9be276a6dccf971a77)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_DOMAIN\_ATTRIBUTES

**Definition** cpu.h:43

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_SLEEP\_MODE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a829fe5849691731336da95eeff60d481)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_SLEEP\_MODE\_SET

**Definition** cpu.h:47

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_NON\_IRQ\_WAKE\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a8fa78652734f276abc4af0b955299b78)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_NON\_IRQ\_WAKE\_SET

**Definition** cpu.h:49

[SCMI\_CPU\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672a9de9b4d325a02bff24cfb9b9a0d6b3a7)

@ SCMI\_CPU\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION

**Definition** cpu.h:53

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PER\_LPM\_CONFIG\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aa9076f4531ca885a3c58ef060cfa304b)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PER\_LPM\_CONFIG\_SET

**Definition** cpu.h:51

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_INFO\_GET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ac47a18fb60f00abfbdcf0c3fd1fee4d7)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_INFO\_GET

**Definition** cpu.h:52

[SCMI\_CPU\_DOMAIN\_MSG\_CPU\_RESET\_VECTOR\_SET](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672aca337c082e8717d4bcbfd63826914328)

@ SCMI\_CPU\_DOMAIN\_MSG\_CPU\_RESET\_VECTOR\_SET

**Definition** cpu.h:46

[SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#a8b569d6a08f7eb1779c62ca886fb4672ace67a725f9f6692139fecdfe7bc0f610)

@ SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES

**Definition** cpu.h:42

[scmi\_cpu\_sleep\_mode\_set](drivers_2firmware_2scmi_2nxp_2cpu_8h.md#ac62bef1626449da2f816a2be755b762d)

int scmi\_cpu\_sleep\_mode\_set(struct scmi\_cpu\_sleep\_mode\_config \*cfg)

Send the CPU\_SLEEP\_MODE\_SET command and get its reply.

[protocol.h](drivers_2firmware_2scmi_2protocol_8h.md)

SCMI protocol generic functions and structures.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md)

Describes the parameters for the CPU\_STATE\_SET command.

**Definition** cpu.h:30

[scmi\_cpu\_sleep\_mode\_config::sleep\_mode](structscmi__cpu__sleep__mode__config.md#a29781dcbdbaf3fd2e6aa840e78f26615)

uint32\_t sleep\_mode

**Definition** cpu.h:33

[scmi\_cpu\_sleep\_mode\_config::flags](structscmi__cpu__sleep__mode__config.md#ab11fddc7614f03706180cf12151d5e7d)

uint32\_t flags

**Definition** cpu.h:32

[scmi\_cpu\_sleep\_mode\_config::cpu\_id](structscmi__cpu__sleep__mode__config.md#ab14413f0c5cdd1a061235a750df316e0)

uint32\_t cpu\_id

**Definition** cpu.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [nxp](dir_bc3d371a8d44c42990f11f40d55980ed.md)
- [cpu.h](drivers_2firmware_2scmi_2nxp_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
