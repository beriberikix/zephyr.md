---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/intc__rx__icu_8h_source.html
original_path: doxygen/html/intc__rx__icu_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_rx\_icu.h

[Go to the documentation of this file.](intc__rx__icu_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RX\_ICU\_H\_

7#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RX\_ICU\_H\_

8

[ 9](intc__rx__icu_8h.md#a1f2e0aab110d6ad50ca923d97b7a5569)#define IRQ\_CFG\_PCLK\_DIV1 (0)

[ 10](intc__rx__icu_8h.md#a886edc20620e3b7e376df37e90b81c1a)#define IRQ\_CFG\_PCLK\_DIV8 (1)

[ 11](intc__rx__icu_8h.md#adf9e7efaa66840f836a94ba6972b0dff)#define IRQ\_CFG\_PCLK\_DIV32 (2)

[ 12](intc__rx__icu_8h.md#a867e76951913679d9d1cd2ac5df79eda)#define IRQ\_CFG\_PCLK\_DIV64 (3)

13

[ 14](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e)enum [icu\_irq\_mode](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e) {

[ 15](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4) [ICU\_LOW\_LEVEL](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4),

[ 16](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432) [ICU\_FALLING](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432),

[ 17](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3) [ICU\_RISING](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3),

[ 18](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650) [ICU\_BOTH\_EDGE](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650),

[ 19](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8) [ICU\_MODE\_NONE](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8),

20};

21

[ 22](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431a)enum [icu\_dig\_filt](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431a) {

[ 23](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01) [DISENABLE\_DIG\_FILT](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01),

[ 24](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d) [ENABLE\_DIG\_FILT](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d),

25};

26

[ 27](structrx__irq__dig__filt__s.md)typedef struct [rx\_irq\_dig\_filt\_s](structrx__irq__dig__filt__s.md) {

[ 28](structrx__irq__dig__filt__s.md#a97fcdaa2ec47cb1714c48e5f67e4b069) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filt\_clk\_div](structrx__irq__dig__filt__s.md#a97fcdaa2ec47cb1714c48e5f67e4b069); /\* PCLK divisor setting for the input pin digital filter. \*/

[ 29](structrx__irq__dig__filt__s.md#a9338cdaf9596b591bc6ddd27a3a8cb97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filt\_enable](structrx__irq__dig__filt__s.md#a9338cdaf9596b591bc6ddd27a3a8cb97); /\* Filter enable setting for the input pin digital filter. \*/

[ 30](intc__rx__icu_8h.md#ae5e7618b4871363e4b9443cbe01ef86d)} [rx\_irq\_dig\_filt\_t](intc__rx__icu_8h.md#ae5e7618b4871363e4b9443cbe01ef86d);

31

[ 32](intc__rx__icu_8h.md#a03cc2d22194251dd8942e2d95c3b3451)extern void [rx\_icu\_clear\_ir\_flag](intc__rx__icu_8h.md#a03cc2d22194251dd8942e2d95c3b3451)(unsigned int irqn);

[ 33](intc__rx__icu_8h.md#a43836995901c04ab8c734f28c4e57e73)extern int [rx\_icu\_get\_ir\_flag](intc__rx__icu_8h.md#a43836995901c04ab8c734f28c4e57e73)(unsigned int irqn);

[ 34](intc__rx__icu_8h.md#a32aadebfbc450fa354d6d176289fec0d)extern int [rx\_icu\_set\_irq\_control](intc__rx__icu_8h.md#a32aadebfbc450fa354d6d176289fec0d)(unsigned int pin\_irqn, enum [icu\_irq\_mode](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e) mode);

[ 35](intc__rx__icu_8h.md#ac9bdc620911c67f607cf9ec5a49fd1b1)extern void [rx\_icu\_set\_irq\_dig\_filt](intc__rx__icu_8h.md#ac9bdc620911c67f607cf9ec5a49fd1b1)(unsigned int pin\_irqn, [rx\_irq\_dig\_filt\_t](intc__rx__icu_8h.md#ae5e7618b4871363e4b9443cbe01ef86d) dig\_filt);

36

37#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RX\_ICU\_H\_ \*/

[rx\_icu\_clear\_ir\_flag](intc__rx__icu_8h.md#a03cc2d22194251dd8942e2d95c3b3451)

void rx\_icu\_clear\_ir\_flag(unsigned int irqn)

[rx\_icu\_set\_irq\_control](intc__rx__icu_8h.md#a32aadebfbc450fa354d6d176289fec0d)

int rx\_icu\_set\_irq\_control(unsigned int pin\_irqn, enum icu\_irq\_mode mode)

[rx\_icu\_get\_ir\_flag](intc__rx__icu_8h.md#a43836995901c04ab8c734f28c4e57e73)

int rx\_icu\_get\_ir\_flag(unsigned int irqn)

[icu\_dig\_filt](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431a)

icu\_dig\_filt

**Definition** intc\_rx\_icu.h:22

[ENABLE\_DIG\_FILT](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d)

@ ENABLE\_DIG\_FILT

**Definition** intc\_rx\_icu.h:24

[DISENABLE\_DIG\_FILT](intc__rx__icu_8h.md#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01)

@ DISENABLE\_DIG\_FILT

**Definition** intc\_rx\_icu.h:23

[rx\_icu\_set\_irq\_dig\_filt](intc__rx__icu_8h.md#ac9bdc620911c67f607cf9ec5a49fd1b1)

void rx\_icu\_set\_irq\_dig\_filt(unsigned int pin\_irqn, rx\_irq\_dig\_filt\_t dig\_filt)

[rx\_irq\_dig\_filt\_t](intc__rx__icu_8h.md#ae5e7618b4871363e4b9443cbe01ef86d)

struct rx\_irq\_dig\_filt\_s rx\_irq\_dig\_filt\_t

[icu\_irq\_mode](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e)

icu\_irq\_mode

**Definition** intc\_rx\_icu.h:14

[ICU\_RISING](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3)

@ ICU\_RISING

**Definition** intc\_rx\_icu.h:17

[ICU\_BOTH\_EDGE](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650)

@ ICU\_BOTH\_EDGE

**Definition** intc\_rx\_icu.h:18

[ICU\_LOW\_LEVEL](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4)

@ ICU\_LOW\_LEVEL

**Definition** intc\_rx\_icu.h:15

[ICU\_FALLING](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432)

@ ICU\_FALLING

**Definition** intc\_rx\_icu.h:16

[ICU\_MODE\_NONE](intc__rx__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8)

@ ICU\_MODE\_NONE

**Definition** intc\_rx\_icu.h:19

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[rx\_irq\_dig\_filt\_s](structrx__irq__dig__filt__s.md)

**Definition** intc\_rx\_icu.h:27

[rx\_irq\_dig\_filt\_s::filt\_enable](structrx__irq__dig__filt__s.md#a9338cdaf9596b591bc6ddd27a3a8cb97)

uint8\_t filt\_enable

**Definition** intc\_rx\_icu.h:29

[rx\_irq\_dig\_filt\_s::filt\_clk\_div](structrx__irq__dig__filt__s.md#a97fcdaa2ec47cb1714c48e5f67e4b069)

uint8\_t filt\_clk\_div

**Definition** intc\_rx\_icu.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_rx\_icu.h](intc__rx__icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
