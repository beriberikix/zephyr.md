---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpu__hw__if_8h_source.html
original_path: doxygen/html/rpu__hw__if_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpu\_hw\_if.h

[Go to the documentation of this file.](rpu__hw__if_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_\_RPU\_HW\_IF\_H\_

13#define \_\_RPU\_HW\_IF\_H\_

14

15#include <[stdio.h](stdio_8h.md)>

16#include <[stdlib.h](stdlib_8h.md)>

17#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

18

19enum {

[ 20](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a5644bd46a26ffff652d489a25edc2ac8) [SYSBUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a5644bd46a26ffff652d489a25edc2ac8) = 0,

[ 21](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2ae3adc4be123a7ab371aec7b8abcd0e6b) [EXT\_SYS\_BUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2ae3adc4be123a7ab371aec7b8abcd0e6b),

[ 22](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a7ebc7c586fe6170492012ff4b58136c1) [PBUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a7ebc7c586fe6170492012ff4b58136c1),

[ 23](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a866f21bcbbd021916d9f400c36a53aa9) [PKTRAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a866f21bcbbd021916d9f400c36a53aa9),

[ 24](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a56b26140695810b82c8d01a40b68c0ef) [GRAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a56b26140695810b82c8d01a40b68c0ef),

[ 25](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2abc6bad5f17cb51c69c21add8460a5e98) [LMAC\_ROM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2abc6bad5f17cb51c69c21add8460a5e98),

[ 26](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a565f9ead2860aa9a47a22d8ca5a60450) [LMAC\_RET\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a565f9ead2860aa9a47a22d8ca5a60450),

[ 27](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a8c55a703a4d80b31c60811a0ac19e1d5) [LMAC\_SRC\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a8c55a703a4d80b31c60811a0ac19e1d5),

[ 28](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a561e00cb2ad96150cd6b2a7f20d30df4) [UMAC\_ROM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a561e00cb2ad96150cd6b2a7f20d30df4),

[ 29](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a1e5ff995ea0e46ecd2016f9df793b7c4) [UMAC\_RET\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a1e5ff995ea0e46ecd2016f9df793b7c4),

[ 30](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a9b5f609c6e3434c3299aa0f56b93e951) [UMAC\_SRC\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a9b5f609c6e3434c3299aa0f56b93e951),

[ 31](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a80b0c0944a12f69321f94debfdd6f07e) [NUM\_MEM\_BLOCKS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a80b0c0944a12f69321f94debfdd6f07e)

32};

33

34extern char [blk\_name](rpu__hw__if_8h.md#adeeb0a092efcba75f774110aa59de589)[][15];

35extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rpu\_7002\_memmap](rpu__hw__if_8h.md#afcb709e46416f4955669ef57cb1fea94)[][3];

36

[ 37](rpu__hw__if_8h.md#aa39ecf94ad3ed404126e4c0fe66a04b4)int [rpu\_read](rpu__hw__if_8h.md#aa39ecf94ad3ed404126e4c0fe66a04b4)(unsigned int addr, void \*data, int len);

[ 38](rpu__hw__if_8h.md#a99ac77ce9469d38d350ea30dc6f536bd)int [rpu\_write](rpu__hw__if_8h.md#a99ac77ce9469d38d350ea30dc6f536bd)(unsigned int addr, const void \*data, int len);

39

[ 40](rpu__hw__if_8h.md#a924554f26c08d92df4b546724c306060)int [rpu\_sleep](rpu__hw__if_8h.md#a924554f26c08d92df4b546724c306060)(void);

[ 41](rpu__hw__if_8h.md#aafebdcea8e3a35c04aaafc99651212f7)int [rpu\_wakeup](rpu__hw__if_8h.md#aafebdcea8e3a35c04aaafc99651212f7)(void);

[ 42](rpu__hw__if_8h.md#ab2709308f3b368e9c857bc09002edf1d)int [rpu\_sleep\_status](rpu__hw__if_8h.md#ab2709308f3b368e9c857bc09002edf1d)(void);

[ 43](rpu__hw__if_8h.md#a3e1cf31f4c9109698015c8eb431b2c06)void [rpu\_get\_sleep\_stats](rpu__hw__if_8h.md#a3e1cf31f4c9109698015c8eb431b2c06)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wrd\_len);

[ 44](rpu__hw__if_8h.md#a4d1faf319f268a1ebd53eb7fece4d440)int [rpu\_irq\_config](rpu__hw__if_8h.md#a4d1faf319f268a1ebd53eb7fece4d440)(struct [gpio\_callback](structgpio__callback.md) \*irq\_callback\_data, void (\*irq\_handler)());

[ 45](rpu__hw__if_8h.md#a1504f397d4d4fed2d2fd05d52df52cd1)int [rpu\_irq\_remove](rpu__hw__if_8h.md#a1504f397d4d4fed2d2fd05d52df52cd1)(struct [gpio\_callback](structgpio__callback.md) \*irq\_callback\_data);

46

[ 47](rpu__hw__if_8h.md#a2ad297eb9009726b7d230b703fc4995f)int [rpu\_wrsr2](rpu__hw__if_8h.md#a2ad297eb9009726b7d230b703fc4995f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

[ 48](rpu__hw__if_8h.md#a50dc1376a8c0df466dfa0c032faad2bc)int [rpu\_rdsr2](rpu__hw__if_8h.md#a50dc1376a8c0df466dfa0c032faad2bc)(void);

[ 49](rpu__hw__if_8h.md#a6b878d1b2ee5c0de940df28e98a712b4)int [rpu\_rdsr1](rpu__hw__if_8h.md#a6b878d1b2ee5c0de940df28e98a712b4)(void);

[ 50](rpu__hw__if_8h.md#a1f8f3322380bc92987b06681fc6cdb06)int [rpu\_clks\_on](rpu__hw__if_8h.md#a1f8f3322380bc92987b06681fc6cdb06)(void);

51

[ 52](rpu__hw__if_8h.md#af8092922568e145249ab6e8ff205ebf9)int [rpu\_init](rpu__hw__if_8h.md#af8092922568e145249ab6e8ff205ebf9)(void);

[ 53](rpu__hw__if_8h.md#af1c9e5d15446c5d106d9fade62791163)int [rpu\_enable](rpu__hw__if_8h.md#af1c9e5d15446c5d106d9fade62791163)(void);

[ 54](rpu__hw__if_8h.md#af5b1afbcf46396a6c7d225b2699f3080)int [rpu\_disable](rpu__hw__if_8h.md#af5b1afbcf46396a6c7d225b2699f3080)(void);

55

56#ifdef CONFIG\_NRF70\_SR\_COEX\_RF\_SWITCH

57int sr\_ant\_switch(unsigned int ant\_switch);

58int sr\_gpio\_remove(void);

59int sr\_gpio\_config(void);

60#endif /\* CONFIG\_NRF70\_SR\_COEX\_RF\_SWITCH \*/

61#endif /\* \_\_RPU\_HW\_IF\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[UMAC\_RET\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a1e5ff995ea0e46ecd2016f9df793b7c4)

@ UMAC\_RET\_RAM

**Definition** rpu\_hw\_if.h:29

[UMAC\_ROM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a561e00cb2ad96150cd6b2a7f20d30df4)

@ UMAC\_ROM

**Definition** rpu\_hw\_if.h:28

[SYSBUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a5644bd46a26ffff652d489a25edc2ac8)

@ SYSBUS

**Definition** rpu\_hw\_if.h:20

[LMAC\_RET\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a565f9ead2860aa9a47a22d8ca5a60450)

@ LMAC\_RET\_RAM

**Definition** rpu\_hw\_if.h:26

[GRAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a56b26140695810b82c8d01a40b68c0ef)

@ GRAM

**Definition** rpu\_hw\_if.h:24

[PBUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a7ebc7c586fe6170492012ff4b58136c1)

@ PBUS

**Definition** rpu\_hw\_if.h:22

[NUM\_MEM\_BLOCKS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a80b0c0944a12f69321f94debfdd6f07e)

@ NUM\_MEM\_BLOCKS

**Definition** rpu\_hw\_if.h:31

[PKTRAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a866f21bcbbd021916d9f400c36a53aa9)

@ PKTRAM

**Definition** rpu\_hw\_if.h:23

[LMAC\_SRC\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a8c55a703a4d80b31c60811a0ac19e1d5)

@ LMAC\_SRC\_RAM

**Definition** rpu\_hw\_if.h:27

[UMAC\_SRC\_RAM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2a9b5f609c6e3434c3299aa0f56b93e951)

@ UMAC\_SRC\_RAM

**Definition** rpu\_hw\_if.h:30

[LMAC\_ROM](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2abc6bad5f17cb51c69c21add8460a5e98)

@ LMAC\_ROM

**Definition** rpu\_hw\_if.h:25

[EXT\_SYS\_BUS](rpu__hw__if_8h.md#a0af5845199daa5a85fbaf31347ca07b2ae3adc4be123a7ab371aec7b8abcd0e6b)

@ EXT\_SYS\_BUS

**Definition** rpu\_hw\_if.h:21

[rpu\_irq\_remove](rpu__hw__if_8h.md#a1504f397d4d4fed2d2fd05d52df52cd1)

int rpu\_irq\_remove(struct gpio\_callback \*irq\_callback\_data)

[rpu\_clks\_on](rpu__hw__if_8h.md#a1f8f3322380bc92987b06681fc6cdb06)

int rpu\_clks\_on(void)

[rpu\_wrsr2](rpu__hw__if_8h.md#a2ad297eb9009726b7d230b703fc4995f)

int rpu\_wrsr2(uint8\_t data)

[rpu\_get\_sleep\_stats](rpu__hw__if_8h.md#a3e1cf31f4c9109698015c8eb431b2c06)

void rpu\_get\_sleep\_stats(uint32\_t addr, uint32\_t \*buff, uint32\_t wrd\_len)

[rpu\_irq\_config](rpu__hw__if_8h.md#a4d1faf319f268a1ebd53eb7fece4d440)

int rpu\_irq\_config(struct gpio\_callback \*irq\_callback\_data, void(\*irq\_handler)())

[rpu\_rdsr2](rpu__hw__if_8h.md#a50dc1376a8c0df466dfa0c032faad2bc)

int rpu\_rdsr2(void)

[rpu\_rdsr1](rpu__hw__if_8h.md#a6b878d1b2ee5c0de940df28e98a712b4)

int rpu\_rdsr1(void)

[rpu\_sleep](rpu__hw__if_8h.md#a924554f26c08d92df4b546724c306060)

int rpu\_sleep(void)

[rpu\_write](rpu__hw__if_8h.md#a99ac77ce9469d38d350ea30dc6f536bd)

int rpu\_write(unsigned int addr, const void \*data, int len)

[rpu\_read](rpu__hw__if_8h.md#aa39ecf94ad3ed404126e4c0fe66a04b4)

int rpu\_read(unsigned int addr, void \*data, int len)

[rpu\_wakeup](rpu__hw__if_8h.md#aafebdcea8e3a35c04aaafc99651212f7)

int rpu\_wakeup(void)

[rpu\_sleep\_status](rpu__hw__if_8h.md#ab2709308f3b368e9c857bc09002edf1d)

int rpu\_sleep\_status(void)

[blk\_name](rpu__hw__if_8h.md#adeeb0a092efcba75f774110aa59de589)

char blk\_name[][15]

[rpu\_enable](rpu__hw__if_8h.md#af1c9e5d15446c5d106d9fade62791163)

int rpu\_enable(void)

[rpu\_disable](rpu__hw__if_8h.md#af5b1afbcf46396a6c7d225b2699f3080)

int rpu\_disable(void)

[rpu\_init](rpu__hw__if_8h.md#af8092922568e145249ab6e8ff205ebf9)

int rpu\_init(void)

[rpu\_7002\_memmap](rpu__hw__if_8h.md#afcb709e46416f4955669ef57cb1fea94)

uint32\_t rpu\_7002\_memmap[][3]

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[stdio.h](stdio_8h.md)

[stdlib.h](stdlib_8h.md)

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrf\_wifi](dir_827a5ceb820ded32f2709b259acb2436.md)
- [bus](dir_a8af871e2af95a2ae463c0a62cb13e77.md)
- [rpu\_hw\_if.h](rpu__hw__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
