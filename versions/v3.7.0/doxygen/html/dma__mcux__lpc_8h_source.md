---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dma__mcux__lpc_8h_source.html
original_path: doxygen/html/dma__mcux__lpc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_lpc.h

[Go to the documentation of this file.](dma__mcux__lpc_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_DMA\_MCUX\_LPC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_DMA\_MCUX\_LPC\_H\_

9

10/\*

11 \* LPC DMA engine channel hardware trigger attributes.

12 \* These attributes can be set to the "dma\_slot" field

13 \* in a dma\_config structure to configure a channel for

14 \* hardware triggering.

15 \*/

16

17/\* Peripheral request enable. When set, the peripheral

18 \* request line associated with this channel is used to pace DMA transfers.

19 \*/

[ 20](dma__mcux__lpc_8h.md#a4d1f2a9bd076336bce0fd5e535cfc580)#define LPC\_DMA\_PERIPH\_REQ\_EN BIT(0)

21

22/\* Hardware trigger enable. When set, the hardware trigger connected to this

23 \* channel via INPUTMUX can be used to trigger a transfer

24 \*/

[ 25](dma__mcux__lpc_8h.md#a738b7a640e92bd64a95172b236f10544)#define LPC\_DMA\_HWTRIG\_EN BIT(1)

26

27/\* HW trigger polarity. When this bit is set, the trigger will be active

28 \* high or rising edge triggered, based on TRIG\_TYPE selection

29 \*/

[ 30](dma__mcux__lpc_8h.md#a6c9492c7479a678b11a54e28f7bc3df8)#define LPC\_DMA\_TRIGPOL\_HIGH\_RISING BIT(2)

31

32/\* HW trigger type. When this bit is set, the trigger will be level triggered.

33 \* When it is cleared, the hardware trigger will be edge triggered.

34 \*/

[ 35](dma__mcux__lpc_8h.md#a0f5ed8f5fbe87d13e4f21e0a3018ab64)#define LPC\_DMA\_TRIGTYPE\_LEVEL BIT(3)

36

37/\* HW trigger burst mode. When set, the hardware trigger will cause a burst

38 \* transfer to occur, the length of which is determined by BURST\_POWER.

39 \* When cleared, a single transfer (of the width selected by XFERCFG register)

40 \* will occur.

41 \*/

[ 42](dma__mcux__lpc_8h.md#a4d9e1928d741d1950384f7ab83600ee2)#define LPC\_DMA\_TRIGBURST BIT(4)

43

44/\* HW trigger burst power. Note that due to the size limit of the dma\_slot

45 \* field, the maximum transfer burst possible is 128. The hardware supports

46 \* up to 1024 transfers in BURSTPOWER. The value set here will result in

47 \* 2^BURSTPOWER transfers occurring. So for BURSTPOWER=3, 8 transfers would

48 \* occur.

49 \*/

[ 50](dma__mcux__lpc_8h.md#acfa31048d38fa62b9cb3681886472609)#define LPC\_DMA\_BURSTPOWER(pwr) (((pwr) & 0x7) << 5)

51

52

53/\* Used by driver to extract burstpower setting \*/

[ 54](dma__mcux__lpc_8h.md#a0e9624882342df7556aa29a8f7ee74f3)#define LPC\_DMA\_GET\_BURSTPOWER(slot) (((slot) & 0xE0) >> 5)

55

56#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_DMA\_MCUX\_LPC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_lpc.h](dma__mcux__lpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
