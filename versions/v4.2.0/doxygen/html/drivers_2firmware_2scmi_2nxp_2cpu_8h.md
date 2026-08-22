---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html
original_path: doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h File Reference

SCMI power domain protocol helpers.
[More...](#details)

`#include <[zephyr/drivers/firmware/scmi/protocol.h](drivers_2firmware_2scmi_2protocol_8h_source.md)>`

[Go to the source code of this file.](drivers_2firmware_2scmi_2nxp_2cpu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md) |
|  | Describes the parameters for the CPU\_STATE\_SET command. [More...](structscmi__cpu__sleep__mode__config.md#details) |

| Macros | |
| --- | --- |
| #define | [SCMI\_CPU\_SLEEP\_FLAG\_IRQ\_MUX](#af2b7e2beb6bf8c54aafd42bda71a0374)   0x1U |
| #define | [SCMI\_PROTOCOL\_CPU\_DOMAIN](#a893e63347e801f01f1da912ed7dccc64)   130 |

| Enumerations | |
| --- | --- |
| enum | [scmi\_cpu\_domain\_message](#a8b569d6a08f7eb1779c62ca886fb4672) {     [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_VERSION](#a8b569d6a08f7eb1779c62ca886fb4672a4f38f51833761413a69fc9c0832c184a) = 0x0 , [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](#a8b569d6a08f7eb1779c62ca886fb4672a23078d9d4a3f2c6f8764fae8bbc1e29f) = 0x1 , [SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](#a8b569d6a08f7eb1779c62ca886fb4672ace67a725f9f6692139fecdfe7bc0f610) = 0x2 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_DOMAIN\_ATTRIBUTES](#a8b569d6a08f7eb1779c62ca886fb4672a81c78cfa362e3b9be276a6dccf971a77) = 0x3 ,     [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_START](#a8b569d6a08f7eb1779c62ca886fb4672a2e35dbcb409b234c41b435e373095b69) = 0x4 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_STOP](#a8b569d6a08f7eb1779c62ca886fb4672a31df2a02066ffdec65b7c3f42c382961) = 0x5 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_RESET\_VECTOR\_SET](#a8b569d6a08f7eb1779c62ca886fb4672aca337c082e8717d4bcbfd63826914328) = 0x6 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_SLEEP\_MODE\_SET](#a8b569d6a08f7eb1779c62ca886fb4672a829fe5849691731336da95eeff60d481) = 0x7 ,     [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_IRQ\_WAKE\_SET](#a8b569d6a08f7eb1779c62ca886fb4672a34dedf8a4ea9686eeec89c6fd118aebe) = 0x8 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_NON\_IRQ\_WAKE\_SET](#a8b569d6a08f7eb1779c62ca886fb4672a8fa78652734f276abc4af0b955299b78) = 0x9 , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PD\_LPM\_CONFIG\_SET](#a8b569d6a08f7eb1779c62ca886fb4672a0b40038d48738f6685686c4f9f1576f9) = 0xA , [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PER\_LPM\_CONFIG\_SET](#a8b569d6a08f7eb1779c62ca886fb4672aa9076f4531ca885a3c58ef060cfa304b) = 0xB ,     [SCMI\_CPU\_DOMAIN\_MSG\_CPU\_INFO\_GET](#a8b569d6a08f7eb1779c62ca886fb4672ac47a18fb60f00abfbdcf0c3fd1fee4d7) = 0xC , [SCMI\_CPU\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](#a8b569d6a08f7eb1779c62ca886fb4672a9de9b4d325a02bff24cfb9b9a0d6b3a7) = 0x10   } |
|  | CPU domain protocol command message IDs. [More...](#a8b569d6a08f7eb1779c62ca886fb4672) |

| Functions | |
| --- | --- |
| int | [scmi\_cpu\_sleep\_mode\_set](#ac62bef1626449da2f816a2be755b762d) (struct [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md) \*cfg) |
|  | Send the CPU\_SLEEP\_MODE\_SET command and get its reply. |

## Detailed Description

SCMI power domain protocol helpers.

## Macro Definition Documentation

## [◆ ](#af2b7e2beb6bf8c54aafd42bda71a0374)SCMI\_CPU\_SLEEP\_FLAG\_IRQ\_MUX

| #define SCMI\_CPU\_SLEEP\_FLAG\_IRQ\_MUX   0x1U |
| --- |

## [◆ ](#a893e63347e801f01f1da912ed7dccc64)SCMI\_PROTOCOL\_CPU\_DOMAIN

| #define SCMI\_PROTOCOL\_CPU\_DOMAIN   130 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a8b569d6a08f7eb1779c62ca886fb4672)scmi\_cpu\_domain\_message

| enum [scmi\_cpu\_domain\_message](#a8b569d6a08f7eb1779c62ca886fb4672) |
| --- |

CPU domain protocol command message IDs.

| Enumerator | |
| --- | --- |
| SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_VERSION |  |
| SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES |  |
| SCMI\_CPU\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_DOMAIN\_ATTRIBUTES |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_START |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_STOP |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_RESET\_VECTOR\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_SLEEP\_MODE\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_IRQ\_WAKE\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_NON\_IRQ\_WAKE\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PD\_LPM\_CONFIG\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_PER\_LPM\_CONFIG\_SET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_CPU\_INFO\_GET |  |
| SCMI\_CPU\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION |  |

## Function Documentation

## [◆ ](#ac62bef1626449da2f816a2be755b762d)scmi\_cpu\_sleep\_mode\_set()

| int scmi\_cpu\_sleep\_mode\_set | ( | struct [scmi\_cpu\_sleep\_mode\_config](structscmi__cpu__sleep__mode__config.md) \* | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

Send the CPU\_SLEEP\_MODE\_SET command and get its reply.

Parameters
:   | cfg | pointer to structure containing configuration to be set |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [nxp](dir_bc3d371a8d44c42990f11f40d55980ed.md)
- [cpu.h](drivers_2firmware_2scmi_2nxp_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
