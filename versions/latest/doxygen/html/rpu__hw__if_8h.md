---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpu__hw__if_8h.html
original_path: doxygen/html/rpu__hw__if_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpu\_hw\_if.h File Reference

`#include <[stdio.h](stdio_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](rpu__hw__if_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | {     [SYSBUS](#a0af5845199daa5a85fbaf31347ca07b2a5644bd46a26ffff652d489a25edc2ac8) = 0 , [EXT\_SYS\_BUS](#a0af5845199daa5a85fbaf31347ca07b2ae3adc4be123a7ab371aec7b8abcd0e6b) , [PBUS](#a0af5845199daa5a85fbaf31347ca07b2a7ebc7c586fe6170492012ff4b58136c1) , [PKTRAM](#a0af5845199daa5a85fbaf31347ca07b2a866f21bcbbd021916d9f400c36a53aa9) ,     [GRAM](#a0af5845199daa5a85fbaf31347ca07b2a56b26140695810b82c8d01a40b68c0ef) , [LMAC\_ROM](#a0af5845199daa5a85fbaf31347ca07b2abc6bad5f17cb51c69c21add8460a5e98) , [LMAC\_RET\_RAM](#a0af5845199daa5a85fbaf31347ca07b2a565f9ead2860aa9a47a22d8ca5a60450) , [LMAC\_SRC\_RAM](#a0af5845199daa5a85fbaf31347ca07b2a8c55a703a4d80b31c60811a0ac19e1d5) ,     [UMAC\_ROM](#a0af5845199daa5a85fbaf31347ca07b2a561e00cb2ad96150cd6b2a7f20d30df4) , [UMAC\_RET\_RAM](#a0af5845199daa5a85fbaf31347ca07b2a1e5ff995ea0e46ecd2016f9df793b7c4) , [UMAC\_SRC\_RAM](#a0af5845199daa5a85fbaf31347ca07b2a9b5f609c6e3434c3299aa0f56b93e951) , [NUM\_MEM\_BLOCKS](#a0af5845199daa5a85fbaf31347ca07b2a80b0c0944a12f69321f94debfdd6f07e)   } |
|  | Header containing common functions for RPU hardware interaction using QSPI and SPI that can be invoked by shell or the driver. [More...](#a0af5845199daa5a85fbaf31347ca07b2) |

| Functions | |
| --- | --- |
| int | [rpu\_read](#aa39ecf94ad3ed404126e4c0fe66a04b4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| int | [rpu\_write](#a99ac77ce9469d38d350ea30dc6f536bd) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, const void \*data, int len) |
| int | [rpu\_sleep](#a924554f26c08d92df4b546724c306060) (void) |
| int | [rpu\_wakeup](#aafebdcea8e3a35c04aaafc99651212f7) (void) |
| int | [rpu\_sleep\_status](#ab2709308f3b368e9c857bc09002edf1d) (void) |
| void | [rpu\_get\_sleep\_stats](#a3e1cf31f4c9109698015c8eb431b2c06) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wrd\_len) |
| int | [rpu\_irq\_config](#a4d1faf319f268a1ebd53eb7fece4d440) (struct [gpio\_callback](structgpio__callback.md) \*irq\_callback\_data, void(\*irq\_handler)()) |
| int | [rpu\_irq\_remove](#a1504f397d4d4fed2d2fd05d52df52cd1) (struct [gpio\_callback](structgpio__callback.md) \*irq\_callback\_data) |
| int | [rpu\_wrsr2](#a2ad297eb9009726b7d230b703fc4995f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
| int | [rpu\_rdsr2](#a50dc1376a8c0df466dfa0c032faad2bc) (void) |
| int | [rpu\_rdsr1](#a6b878d1b2ee5c0de940df28e98a712b4) (void) |
| int | [rpu\_clks\_on](#a1f8f3322380bc92987b06681fc6cdb06) (void) |
| int | [rpu\_init](#af8092922568e145249ab6e8ff205ebf9) (void) |
| int | [rpu\_enable](#af1c9e5d15446c5d106d9fade62791163) (void) |
| int | [rpu\_disable](#af5b1afbcf46396a6c7d225b2699f3080) (void) |

| Variables | |
| --- | --- |
| char | [blk\_name](#adeeb0a092efcba75f774110aa59de589) [][15] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rpu\_7002\_memmap](#afcb709e46416f4955669ef57cb1fea94) [][3] |

## Enumeration Type Documentation

## [◆ ](#a0af5845199daa5a85fbaf31347ca07b2)anonymous enum

| anonymous enum |
| --- |

Header containing common functions for RPU hardware interaction using QSPI and SPI that can be invoked by shell or the driver.

| Enumerator | |
| --- | --- |
| SYSBUS |  |
| EXT\_SYS\_BUS |  |
| PBUS |  |
| PKTRAM |  |
| GRAM |  |
| LMAC\_ROM |  |
| LMAC\_RET\_RAM |  |
| LMAC\_SRC\_RAM |  |
| UMAC\_ROM |  |
| UMAC\_RET\_RAM |  |
| UMAC\_SRC\_RAM |  |
| NUM\_MEM\_BLOCKS |  |

## Function Documentation

## [◆ ](#a1f8f3322380bc92987b06681fc6cdb06)rpu\_clks\_on()

| int rpu\_clks\_on | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af5b1afbcf46396a6c7d225b2699f3080)rpu\_disable()

| int rpu\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af1c9e5d15446c5d106d9fade62791163)rpu\_enable()

| int rpu\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3e1cf31f4c9109698015c8eb431b2c06)rpu\_get\_sleep\_stats()

| void rpu\_get\_sleep\_stats | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buff*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *wrd\_len* ) |

## [◆ ](#af8092922568e145249ab6e8ff205ebf9)rpu\_init()

| int rpu\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4d1faf319f268a1ebd53eb7fece4d440)rpu\_irq\_config()

| int rpu\_irq\_config | ( | struct [gpio\_callback](structgpio__callback.md) \* | *irq\_callback\_data*, |
| --- | --- | --- | --- |
|  |  | void(\* | *irq\_handler*)() ) |

## [◆ ](#a1504f397d4d4fed2d2fd05d52df52cd1)rpu\_irq\_remove()

| int rpu\_irq\_remove | ( | struct [gpio\_callback](structgpio__callback.md) \* | *irq\_callback\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a6b878d1b2ee5c0de940df28e98a712b4)rpu\_rdsr1()

| int rpu\_rdsr1 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a50dc1376a8c0df466dfa0c032faad2bc)rpu\_rdsr2()

| int rpu\_rdsr2 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa39ecf94ad3ed404126e4c0fe66a04b4)rpu\_read()

| int rpu\_read | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *addr*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | int | *len* ) |

## [◆ ](#a924554f26c08d92df4b546724c306060)rpu\_sleep()

| int rpu\_sleep | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab2709308f3b368e9c857bc09002edf1d)rpu\_sleep\_status()

| int rpu\_sleep\_status | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aafebdcea8e3a35c04aaafc99651212f7)rpu\_wakeup()

| int rpu\_wakeup | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a99ac77ce9469d38d350ea30dc6f536bd)rpu\_write()

| int rpu\_write | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *addr*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | int | *len* ) |

## [◆ ](#a2ad297eb9009726b7d230b703fc4995f)rpu\_wrsr2()

| int rpu\_wrsr2 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#adeeb0a092efcba75f774110aa59de589)blk\_name

| | char blk\_name[][15] | | --- | | extern |
| --- | --- | --- |

## [◆ ](#afcb709e46416f4955669ef57cb1fea94)rpu\_7002\_memmap

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rpu\_7002\_memmap[][3] | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrf\_wifi](dir_827a5ceb820ded32f2709b259acb2436.md)
- [bus](dir_a8af871e2af95a2ae463c0a62cb13e77.md)
- [rpu\_hw\_if.h](rpu__hw__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
