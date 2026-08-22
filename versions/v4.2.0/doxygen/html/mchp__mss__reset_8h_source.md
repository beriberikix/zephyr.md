---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mchp__mss__reset_8h_source.html
original_path: doxygen/html/mchp__mss__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp\_mss\_reset.h

[Go to the documentation of this file.](mchp__mss__reset_8h.md)

1/\*

2 \* Copyright (C) 2025 embedded brains GmbH & Co. KG

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_MCHP\_MSS\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_MCHP\_MSS\_RESET\_H\_

9

10/\*

11 \* The reset ID encodes the bit index of the SUBBLK\_CLOCK\_CR and SOFT\_RESET\_CR

12 \* registers associated with the device.

13 \*/

[ 14](mchp__mss__reset_8h.md#a18423a46750f38097775bef7841b1599)#define MSS\_RESET\_ID\_ENVM 0x0

[ 15](mchp__mss__reset_8h.md#abe15c7ece3ea1d9189079ea4926634d4)#define MSS\_RESET\_ID\_MAC0 0x1

[ 16](mchp__mss__reset_8h.md#a89a091748b5f3dc4d6aa61869033df6a)#define MSS\_RESET\_ID\_MAC1 0x2

[ 17](mchp__mss__reset_8h.md#ac02d74a88de02875c5a05ea66e73712e)#define MSS\_RESET\_ID\_MMC 0x3

[ 18](mchp__mss__reset_8h.md#ae858d82a6d9273797b7fbf5d29ab8720)#define MSS\_RESET\_ID\_TIMER 0x4

[ 19](mchp__mss__reset_8h.md#ab743db86468819ba1e6edc35324a13b7)#define MSS\_RESET\_ID\_MMUART0 0x5

[ 20](mchp__mss__reset_8h.md#ae3a4d2294c54e458825c717d5b5d7ad5)#define MSS\_RESET\_ID\_MMUART1 0x6

[ 21](mchp__mss__reset_8h.md#a2737e4fb004e6029594e40ae54b99566)#define MSS\_RESET\_ID\_MMUART2 0x7

[ 22](mchp__mss__reset_8h.md#a1da2931af9a378a4ab9aa345b759f797)#define MSS\_RESET\_ID\_MMUART3 0x8

[ 23](mchp__mss__reset_8h.md#ad7cd85ecba9a01342ce5a1f7240203c4)#define MSS\_RESET\_ID\_MMUART4 0x9

[ 24](mchp__mss__reset_8h.md#a1f535b6e7fe7bcde16a6361948efefaf)#define MSS\_RESET\_ID\_SPI0 0xa

[ 25](mchp__mss__reset_8h.md#a8bc6396ba5f953343ceddfd5ec01af3d)#define MSS\_RESET\_ID\_SPI1 0xb

[ 26](mchp__mss__reset_8h.md#a1b2d71457cb3db6910e36b1b69e41ac1)#define MSS\_RESET\_ID\_I2C0 0xc

[ 27](mchp__mss__reset_8h.md#ab3303ed0ce9afa29891ad1c7cdacb3fd)#define MSS\_RESET\_ID\_I2C1 0xd

[ 28](mchp__mss__reset_8h.md#a3133452e84c24d44ece177977d5cfda4)#define MSS\_RESET\_ID\_CAN0 0xe

[ 29](mchp__mss__reset_8h.md#afbc36dce6c281c34881f3e6bf5df8d07)#define MSS\_RESET\_ID\_CAN1 0xf

[ 30](mchp__mss__reset_8h.md#a7036754f68fe469be91cc3d362d5d766)#define MSS\_RESET\_ID\_USB 0x10

[ 31](mchp__mss__reset_8h.md#afb3ea0944f920f16d2de37f055279a9b)#define MSS\_RESET\_ID\_RSVD 0x11

[ 32](mchp__mss__reset_8h.md#a8b86bb9ba68bf6bbfe27a7d5a3213c32)#define MSS\_RESET\_ID\_RTC 0x12

[ 33](mchp__mss__reset_8h.md#a863d6829db645f239a0c39438ef4143a)#define MSS\_RESET\_ID\_QSPI 0x13

[ 34](mchp__mss__reset_8h.md#a8843d543f5b4ffeca0f16ed319b42cba)#define MSS\_RESET\_ID\_GPIO0 0x14

[ 35](mchp__mss__reset_8h.md#a50c9f48e475d0641bcf3f40263922594)#define MSS\_RESET\_ID\_GPIO1 0x15

[ 36](mchp__mss__reset_8h.md#a686ef85362a3ecfd055db68561a5fcd1)#define MSS\_RESET\_ID\_GPIO2 0x16

[ 37](mchp__mss__reset_8h.md#a16af4726a6b14da87e51463a88d243ac)#define MSS\_RESET\_ID\_DDRC 0x17

[ 38](mchp__mss__reset_8h.md#afda60022afd2f749483ac93d6789b831)#define MSS\_RESET\_ID\_FIC0 0x18

[ 39](mchp__mss__reset_8h.md#a4803d3ee18df0a678fd0b187354e7055)#define MSS\_RESET\_ID\_FIC1 0x19

[ 40](mchp__mss__reset_8h.md#a1bbb18c7528b33c1f8705a911ece1dc5)#define MSS\_RESET\_ID\_FIC2 0x1a

[ 41](mchp__mss__reset_8h.md#a6fb3ee9de4012c24980909025e65a236)#define MSS\_RESET\_ID\_FIC3 0x1b

[ 42](mchp__mss__reset_8h.md#a085f13b429cf39c99db1de6a60a95c36)#define MSS\_RESET\_ID\_ATHENA 0x1c

[ 43](mchp__mss__reset_8h.md#a4fa4d4e9cbac95ed3558cf2215e9180e)#define MSS\_RESET\_ID\_CFM 0x1d

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_MCHP\_MSS\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [mchp\_mss\_reset.h](mchp__mss__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
