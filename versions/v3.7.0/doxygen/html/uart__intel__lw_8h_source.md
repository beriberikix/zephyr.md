---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/uart__intel__lw_8h_source.html
original_path: doxygen/html/uart__intel__lw_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_intel\_lw.h

[Go to the documentation of this file.](uart__intel__lw_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_DRIVERS\_SERIAL\_UART\_INTEL\_LW\_H\_

12#define ZEPHYR\_DRIVERS\_SERIAL\_UART\_INTEL\_LW\_H\_

13

14/\* End of packet feature.

15 \* Driver will trigger interrupt upon receiving end of package character.

16 \* Please enable CONFIG\_UART\_INTEL\_LW\_EOP to use this feature.

17 \* Use the api: uart\_drv\_cmd with CMD\_ENABLE\_EOP to enable the feature.

18 \* This cmd will write the ip register and also set a flag to the driver.

19 \* The flag will modify uart\_irq\_callback\_user\_data\_set

20 \* to set call back function for eop interrupt.

21 \* Flag is cleared after uart\_irq\_callback\_user\_data\_set is called.

22 \*/

[ 23](uart__intel__lw_8h.md#acd0b56a568b2ee566e3749a07baa4ded)#define CMD\_ENABLE\_EOP 0x01

[ 24](uart__intel__lw_8h.md#adcc3a86b997151efa6970b2a12d4ecc2)#define CMD\_DISABLE\_EOP 0x02

25

26/\* Transmit break feature.

27 \* Use uart\_drv\_cmd with CMD\_TRBK\_EN to break ongoing transmit.

28 \* After this cmd, uart is unable to transmit any data.

29 \* Please use CMD\_TRBK\_DIS to resume normal operation.

30 \* Please also call uart\_intel\_lw\_err\_check, to clear the error caused

31 \* by transmit break.

32 \*/

[ 33](uart__intel__lw_8h.md#a6f9a2c319edecf29eeed485a84d408c3)#define CMD\_TRBK\_EN 0x03

[ 34](uart__intel__lw_8h.md#a492530b2df4cbb9771c2e068ed872173)#define CMD\_TRBK\_DIS 0x04

35

36/\* This driver supports interrupt driven api.

37 \* Polling for data under normal operation, might cause unexpected behaviour.

38 \* If users wish to poll for data, please use the api:

39 \* uart\_drv\_cmd with CMD\_POLL\_ASSERT\_RTS before polling out/in.

40 \* Then use CMD\_POLL\_DEASSERT\_RTS to resume normal operation after polling.

41 \*/

[ 42](uart__intel__lw_8h.md#a18ee5cdca3047268a54e9a228d5b4d16)#define CMD\_POLL\_ASSERT\_RTS 0x05

[ 43](uart__intel__lw_8h.md#af2d3ec81ffd531601140f0bbfd01d0af)#define CMD\_POLL\_DEASSERT\_RTS 0x06

44

45#endif /\* ZEPHYR\_DRIVERS\_SERIAL\_UART\_INTEL\_LW\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_intel\_lw.h](uart__intel__lw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
