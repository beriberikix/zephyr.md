---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__esp32_8h_source.html
original_path: doxygen/html/intc__esp32_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_esp32.h

[Go to the documentation of this file.](intc__esp32_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ESP\_INTR\_ALLOC\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ESP\_INTR\_ALLOC\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

13/\* number of possible interrupts per core \*/

[ 14](intc__esp32_8h.md#a1bc4233beade6702b76413dd4ee6497f)#define ESP\_INTC\_INTS\_NUM (32)

15

16/\*

17 \* Interrupt allocation flags - These flags can be used to specify

18 \* which interrupt qualities the code calling esp\_intr\_alloc\* needs.

19 \*

20 \*/

21

22/\* Keep the LEVELx values as they are here; they match up with (1<<level) \*/

[ 23](intc__esp32_8h.md#ab1ef5952bffcb1811d4f831b98ecf42a)#define ESP\_INTR\_FLAG\_LEVEL1 (1<<1) /\* Accept a Level 1 int vector, lowest priority \*/

[ 24](intc__esp32_8h.md#a8e4478d65d49a4f17fb77599764239e2)#define ESP\_INTR\_FLAG\_LEVEL2 (1<<2) /\* Accept a Level 2 int vector \*/

[ 25](intc__esp32_8h.md#a88ed1ea08351b07086a6e73a0487b0d8)#define ESP\_INTR\_FLAG\_LEVEL3 (1<<3) /\* Accept a Level 3 int vector \*/

[ 26](intc__esp32_8h.md#abb43226aa7d32763f17ee6a56090b322)#define ESP\_INTR\_FLAG\_LEVEL4 (1<<4) /\* Accept a Level 4 int vector \*/

[ 27](intc__esp32_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)#define ESP\_INTR\_FLAG\_LEVEL5 (1<<5) /\* Accept a Level 5 int vector \*/

[ 28](intc__esp32_8h.md#a8defb5130273462e32ed399dece67024)#define ESP\_INTR\_FLAG\_LEVEL6 (1<<6) /\* Accept a Level 6 int vector \*/

[ 29](intc__esp32_8h.md#a9e57c700cf362161d807657571280abe)#define ESP\_INTR\_FLAG\_NMI (1<<7) /\* Accept a Level 7 int vector, highest priority \*/

[ 30](intc__esp32_8h.md#afc7bfcea2e621d81336ea6dd23310363)#define ESP\_INTR\_FLAG\_SHARED (1<<8) /\* Interrupt can be shared between ISRs \*/

[ 31](intc__esp32_8h.md#a0ab957dd5055fe20725624db223f9535)#define ESP\_INTR\_FLAG\_EDGE (1<<9) /\* Edge-triggered interrupt \*/

[ 32](intc__esp32_8h.md#a3fb8d6fa8b5e33b3503e86917bc8367b)#define ESP\_INTR\_FLAG\_IRAM (1<<10) /\* ISR can be called if cache is disabled \*/

[ 33](intc__esp32_8h.md#a76d024609ecd48dc17b586b91e779b88)#define ESP\_INTR\_FLAG\_INTRDISABLED (1<<11) /\* Return with this interrupt disabled \*/

34

35/\* Low and medium prio interrupts. These can be handled in C. \*/

[ 36](intc__esp32_8h.md#a9b0bc1a2b5cc22b499e041742ae1b17b)#define ESP\_INTR\_FLAG\_LOWMED (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3)

37

38/\* High level interrupts. Need to be handled in assembly. \*/

[ 39](intc__esp32_8h.md#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)#define ESP\_INTR\_FLAG\_HIGH (ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

40 ESP\_INTR\_FLAG\_NMI)

41

42/\* Mask for all level flags \*/

[ 43](intc__esp32_8h.md#a610949ce2bf8d7adae528f816acc5725)#define ESP\_INTR\_FLAG\_LEVELMASK (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3| \

44 ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

45 ESP\_INTR\_FLAG\_NMI)

46

47/\*

48 \* The esp\_intr\_alloc\* functions can allocate an int for all \*\_INTR\_SOURCE int sources that

49 \* are routed through the interrupt mux. Apart from these sources, each core also has some internal

50 \* sources that do not pass through the interrupt mux. To allocate an interrupt for these sources,

51 \* pass these pseudo-sources to the functions.

52 \*/

[ 53](intc__esp32_8h.md#a2ff354dc48600b4dcbce4569c5d15bc1)#define ETS\_INTERNAL\_TIMER0\_INTR\_SOURCE -1 /\* Xtensa timer 0 interrupt source \*/

[ 54](intc__esp32_8h.md#ad28849af2335d2c6d9e07949f8ea953d)#define ETS\_INTERNAL\_TIMER1\_INTR\_SOURCE -2 /\* Xtensa timer 1 interrupt source \*/

[ 55](intc__esp32_8h.md#ad94487ae3c0ae2b9e4bccad6ce26d761)#define ETS\_INTERNAL\_TIMER2\_INTR\_SOURCE -3 /\* Xtensa timer 2 interrupt source \*/

[ 56](intc__esp32_8h.md#a7cd02abe5015f1be30d77e1be15bd448)#define ETS\_INTERNAL\_SW0\_INTR\_SOURCE -4 /\* Software int source 1 \*/

[ 57](intc__esp32_8h.md#aa81d606c0199b91aba7633270ca314e6)#define ETS\_INTERNAL\_SW1\_INTR\_SOURCE -5 /\* Software int source 2 \*/

[ 58](intc__esp32_8h.md#a6cac8d828d3ec24b9bb58fe0cb3d59fc)#define ETS\_INTERNAL\_PROFILING\_INTR\_SOURCE -6 /\* Int source for profiling \*/

59

60/\* Function prototype for interrupt handler function \*/

[ 61](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2)typedef void (\*[intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2))(void \*arg);

62

[ 63](structshared__vector__desc__t.md)struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) {

[ 64](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41) int [disabled](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41) : 1;

[ 65](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517) int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517) : 8;

[ 66](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[statusreg](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f);

[ 67](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [statusmask](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb);

[ 68](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84) [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) [isr](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84);

[ 69](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e) void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e);

[ 70](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[next](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605);

71};

72

73/\* Pack using bitfields for better memory use \*/

[ 74](structvector__desc__t.md)struct [vector\_desc\_t](structvector__desc__t.md) {

[ 75](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970) int [flags](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970) : 16; /\* OR of VECDESC\_FLAG\_\* defines \*/

[ 76](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9) unsigned int [cpu](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9) : 1;

[ 77](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77) unsigned int [intno](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77) : 5;

[ 78](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc) int [source](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc) : 8; /\* Int mux flags, used when not shared \*/

[ 79](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[shared\_vec\_info](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967); /\* used when VECDESC\_FL\_SHARED \*/

[ 80](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8) struct [vector\_desc\_t](structvector__desc__t.md) \*[next](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8);

81};

82

[ 84](structintr__handle__data__t.md)struct [intr\_handle\_data\_t](structintr__handle__data__t.md) {

[ 85](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036) struct [vector\_desc\_t](structvector__desc__t.md) \*[vector\_desc](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036);

[ 86](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[shared\_vector\_desc](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e);

87};

88

[ 92](intc__esp32_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)void [esp\_intr\_initialize](intc__esp32_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)(void);

93

[ 109](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)int [esp\_intr\_mark\_shared](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)(int intno, int cpu, bool is\_in\_iram);

110

[ 123](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)int [esp\_intr\_reserve](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)(int intno, int cpu);

124

[ 158](intc__esp32_8h.md#a480a4405ea151074f2ce4ffbab1265ea)int [esp\_intr\_alloc](intc__esp32_8h.md#a480a4405ea151074f2ce4ffbab1265ea)(int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517),

159 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

160 [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) handler,

161 void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e),

162 struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\*ret\_handle);

163

164

[ 200](intc__esp32_8h.md#a8659159ab9a4fea92d989068bb6d6f7b)int [esp\_intr\_alloc\_intrstatus](intc__esp32_8h.md#a8659159ab9a4fea92d989068bb6d6f7b)(int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517),

201 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

202 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusreg,

203 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusmask,

204 [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) handler,

205 void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e),

206 struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\*ret\_handle);

207

208

[ 227](intc__esp32_8h.md#a90993df0cbd038640609df8c3e1957d3)int [esp\_intr\_free](intc__esp32_8h.md#a90993df0cbd038640609df8c3e1957d3)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle);

228

229

[ 237](intc__esp32_8h.md#a6c399aafeab8bff0a49bc2b127445e10)int [esp\_intr\_get\_cpu](intc__esp32_8h.md#a6c399aafeab8bff0a49bc2b127445e10)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle);

238

[ 246](intc__esp32_8h.md#a5261fac231a9d1428b4131da33f1ef90)int [esp\_intr\_get\_intno](intc__esp32_8h.md#a5261fac231a9d1428b4131da33f1ef90)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle);

247

[ 264](intc__esp32_8h.md#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6)int [esp\_intr\_disable](intc__esp32_8h.md#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle);

265

[ 277](intc__esp32_8h.md#a3a9ed282687252cd3a8e5c18284257ff)int [esp\_intr\_enable](intc__esp32_8h.md#a3a9ed282687252cd3a8e5c18284257ff)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle);

278

[ 291](intc__esp32_8h.md#af1417d7a4a9faba280ac4e17c9ee60ab)int [esp\_intr\_set\_in\_iram](intc__esp32_8h.md#af1417d7a4a9faba280ac4e17c9ee60ab)(struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle, bool is\_in\_iram);

292

[ 296](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)void [esp\_intr\_noniram\_disable](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)(void);

297

298

[ 302](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)void [esp\_intr\_noniram\_enable](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)(void);

303

304#endif

[esp\_intr\_enable](intc__esp32_8h.md#a3a9ed282687252cd3a8e5c18284257ff)

int esp\_intr\_enable(struct intr\_handle\_data\_t \*handle)

Enable the interrupt associated with the handle.

[esp\_intr\_disable](intc__esp32_8h.md#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6)

int esp\_intr\_disable(struct intr\_handle\_data\_t \*handle)

Disable the interrupt associated with the handle.

[esp\_intr\_alloc](intc__esp32_8h.md#a480a4405ea151074f2ce4ffbab1265ea)

int esp\_intr\_alloc(int source, int flags, intr\_handler\_t handler, void \*arg, struct intr\_handle\_data\_t \*\*ret\_handle)

Allocate an interrupt with the given parameters.

[esp\_intr\_get\_intno](intc__esp32_8h.md#a5261fac231a9d1428b4131da33f1ef90)

int esp\_intr\_get\_intno(struct intr\_handle\_data\_t \*handle)

Get the allocated interrupt for a certain handle.

[esp\_intr\_noniram\_disable](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)

void esp\_intr\_noniram\_disable(void)

Disable interrupts that aren't specifically marked as running from IRAM.

[intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2)

void(\* intr\_handler\_t)(void \*arg)

**Definition** intc\_esp32.h:61

[esp\_intr\_get\_cpu](intc__esp32_8h.md#a6c399aafeab8bff0a49bc2b127445e10)

int esp\_intr\_get\_cpu(struct intr\_handle\_data\_t \*handle)

Get CPU number an interrupt is tied to.

[esp\_intr\_alloc\_intrstatus](intc__esp32_8h.md#a8659159ab9a4fea92d989068bb6d6f7b)

int esp\_intr\_alloc\_intrstatus(int source, int flags, uint32\_t intrstatusreg, uint32\_t intrstatusmask, intr\_handler\_t handler, void \*arg, struct intr\_handle\_data\_t \*\*ret\_handle)

Allocate an interrupt with the given parameters.

[esp\_intr\_free](intc__esp32_8h.md#a90993df0cbd038640609df8c3e1957d3)

int esp\_intr\_free(struct intr\_handle\_data\_t \*handle)

Disable and free an interrupt.

[esp\_intr\_noniram\_enable](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)

void esp\_intr\_noniram\_enable(void)

Re-enable interrupts disabled by esp\_intr\_noniram\_disable.

[esp\_intr\_reserve](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)

int esp\_intr\_reserve(int intno, int cpu)

Reserve an interrupt to be used outside of this framework.

[esp\_intr\_mark\_shared](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)

int esp\_intr\_mark\_shared(int intno, int cpu, bool is\_in\_iram)

Mark an interrupt as a shared interrupt.

[esp\_intr\_initialize](intc__esp32_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)

void esp\_intr\_initialize(void)

Initializes interrupt table to its defaults.

[esp\_intr\_set\_in\_iram](intc__esp32_8h.md#af1417d7a4a9faba280ac4e17c9ee60ab)

int esp\_intr\_set\_in\_iram(struct intr\_handle\_data\_t \*handle, bool is\_in\_iram)

Set the "in IRAM" status of the handler.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intr\_handle\_data\_t](structintr__handle__data__t.md)

Interrupt handler associated data structure.

**Definition** intc\_esp32.h:84

[intr\_handle\_data\_t::vector\_desc](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036)

struct vector\_desc\_t \* vector\_desc

**Definition** intc\_esp32.h:85

[intr\_handle\_data\_t::shared\_vector\_desc](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e)

struct shared\_vector\_desc\_t \* shared\_vector\_desc

**Definition** intc\_esp32.h:86

[shared\_vector\_desc\_t](structshared__vector__desc__t.md)

**Definition** intc\_esp32.h:63

[shared\_vector\_desc\_t::disabled](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41)

int disabled

**Definition** intc\_esp32.h:64

[shared\_vector\_desc\_t::arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e)

void \* arg

**Definition** intc\_esp32.h:69

[shared\_vector\_desc\_t::statusmask](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb)

uint32\_t statusmask

**Definition** intc\_esp32.h:67

[shared\_vector\_desc\_t::isr](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84)

intr\_handler\_t isr

**Definition** intc\_esp32.h:68

[shared\_vector\_desc\_t::statusreg](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f)

volatile uint32\_t \* statusreg

**Definition** intc\_esp32.h:66

[shared\_vector\_desc\_t::next](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605)

struct shared\_vector\_desc\_t \* next

**Definition** intc\_esp32.h:70

[shared\_vector\_desc\_t::source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517)

int source

**Definition** intc\_esp32.h:65

[vector\_desc\_t](structvector__desc__t.md)

**Definition** intc\_esp32.h:74

[vector\_desc\_t::flags](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970)

int flags

**Definition** intc\_esp32.h:75

[vector\_desc\_t::next](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8)

struct vector\_desc\_t \* next

**Definition** intc\_esp32.h:80

[vector\_desc\_t::intno](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77)

unsigned int intno

**Definition** intc\_esp32.h:77

[vector\_desc\_t::cpu](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9)

unsigned int cpu

**Definition** intc\_esp32.h:76

[vector\_desc\_t::source](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc)

int source

**Definition** intc\_esp32.h:78

[vector\_desc\_t::shared\_vec\_info](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967)

struct shared\_vector\_desc\_t \* shared\_vec\_info

**Definition** intc\_esp32.h:79

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_esp32.h](intc__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
