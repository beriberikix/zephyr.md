---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rp2350__reset_8h_source.html
original_path: doxygen/html/rp2350__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rp2350\_reset.h

[Go to the documentation of this file.](rp2350__reset_8h.md)

1/\*

2 \* Copyright (c) 2024 Andrew Featherstone

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_RP2350\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_RP2350\_RESET\_H\_

9

[ 10](rp2350__reset_8h.md#abac5947197d81eb0dfb2e4490b191ff1)#define RPI\_PICO\_RESETS\_RESET\_ADC 0

[ 11](rp2350__reset_8h.md#a8d9aed2655b0d64f8b33bfe49fa41570)#define RPI\_PICO\_RESETS\_RESET\_BUSCTRL 1

[ 12](rp2350__reset_8h.md#a99b09965f0053aefad10961d95dac77c)#define RPI\_PICO\_RESETS\_RESET\_DMA 2

[ 13](rp2350__reset_8h.md#a165f80e4f4570e2d373a84eb212574c7)#define RPI\_PICO\_RESETS\_RESET\_HSTX 3

[ 14](rp2350__reset_8h.md#a335daf7797415719654796cd15ccd37b)#define RPI\_PICO\_RESETS\_RESET\_I2C0 4

[ 15](rp2350__reset_8h.md#a30a4199460568314ccbf3cdda6427db0)#define RPI\_PICO\_RESETS\_RESET\_I2C1 5

[ 16](rp2350__reset_8h.md#af8ac1ce17d197cd09f41dab48ca9fec1)#define RPI\_PICO\_RESETS\_RESET\_IO\_BANK0 6

[ 17](rp2350__reset_8h.md#a349d905a5e3de42a9626b4d81059992b)#define RPI\_PICO\_RESETS\_RESET\_IO\_QSPI 7

[ 18](rp2350__reset_8h.md#aec1f55ee581b899f9325fefb9aacf68e)#define RPI\_PICO\_RESETS\_RESET\_JTAG 8

[ 19](rp2350__reset_8h.md#a6d45f135f543c9b5168f5244842b6af1)#define RPI\_PICO\_RESETS\_RESET\_PADS\_BANK0 9

[ 20](rp2350__reset_8h.md#a6cc676793d5c937a693be6fe8b2862bf)#define RPI\_PICO\_RESETS\_RESET\_PADS\_QSPI 10

[ 21](rp2350__reset_8h.md#adc3511168398819c01afba241f866fb3)#define RPI\_PICO\_RESETS\_RESET\_PIO0 11

[ 22](rp2350__reset_8h.md#a18fa1392f3eb00a15288460610113671)#define RPI\_PICO\_RESETS\_RESET\_PIO1 12

[ 23](rp2350__reset_8h.md#a9c9447b5f3674917ac4778b3f2fa9742)#define RPI\_PICO\_RESETS\_RESET\_PIO2 13

[ 24](rp2350__reset_8h.md#ad6664574a797fa6a2aeabb63755bcb7e)#define RPI\_PICO\_RESETS\_RESET\_PLL\_SYS 14

[ 25](rp2350__reset_8h.md#ae791233ea824b3adf783479cdd0f3288)#define RPI\_PICO\_RESETS\_RESET\_PLL\_USB 15

[ 26](rp2350__reset_8h.md#a140922f8bd5886b14b7b5ea21ba9d64b)#define RPI\_PICO\_RESETS\_RESET\_PWM 16

[ 27](rp2350__reset_8h.md#a62ad14e6a73e63e355415bfd998ccbfa)#define RPI\_PICO\_RESETS\_RESET\_SHA256 17

[ 28](rp2350__reset_8h.md#a3217125ff2d9e231a658a7510caa5b6e)#define RPI\_PICO\_RESETS\_RESET\_SPI0 18

[ 29](rp2350__reset_8h.md#a3f539a0ea496367c61b3deb7bf614fec)#define RPI\_PICO\_RESETS\_RESET\_SPI1 19

[ 30](rp2350__reset_8h.md#a6960ebc2988d20452a21e8d2e704494d)#define RPI\_PICO\_RESETS\_RESET\_SYSCFG 20

[ 31](rp2350__reset_8h.md#afe5cf6cc92248efac38cb79a057f4ebe)#define RPI\_PICO\_RESETS\_RESET\_SYSINFO 21

[ 32](rp2350__reset_8h.md#a526ba5a9f743922cdcc921ce5f767330)#define RPI\_PICO\_RESETS\_RESET\_TBMAN 22

[ 33](rp2350__reset_8h.md#a95ff7d8603885b874462eb80b6688898)#define RPI\_PICO\_RESETS\_RESET\_TIMER0 23

[ 34](rp2350__reset_8h.md#a0f82b7d3351a9852e1017d1f958484d6)#define RPI\_PICO\_RESETS\_RESET\_TIMER1 24

[ 35](rp2350__reset_8h.md#a2395c9a17abf14b7ee15422d6897e13f)#define RPI\_PICO\_RESETS\_RESET\_TRNG 25

[ 36](rp2350__reset_8h.md#a518638c89ac3f52e0c5fdf3bd5cc3612)#define RPI\_PICO\_RESETS\_RESET\_UART0 26

[ 37](rp2350__reset_8h.md#a832e0aabb3bdca804e610e2386c9f835)#define RPI\_PICO\_RESETS\_RESET\_UART1 27

[ 38](rp2350__reset_8h.md#acf3cd72b20163e803165f8950b343fdc)#define RPI\_PICO\_RESETS\_RESET\_USBCTRL 28

39

40#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_RP2350\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [rp2350\_reset.h](rp2350__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
