---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/intc__esp32_8h_source.html
original_path: doxygen/html/intc__esp32_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_esp32.h

[Go to the documentation of this file.](intc__esp32_8h.md)

1/\*

2 \* Copyright (c) 2021-2025 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

13/\*

14 \* Interrupt allocation flags - These flags can be used to specify

15 \* which interrupt qualities the code calling esp\_intr\_alloc\* needs.

16 \*

17 \*/

18

19/\* Keep the LEVELx values as they are here; they match up with (1<<level) \*/

[ 20](intc__esp32_8h.md#ab1ef5952bffcb1811d4f831b98ecf42a)#define ESP\_INTR\_FLAG\_LEVEL1 (1<<1) /\* Accept a Level 1 int vector, lowest priority \*/

[ 21](intc__esp32_8h.md#a8e4478d65d49a4f17fb77599764239e2)#define ESP\_INTR\_FLAG\_LEVEL2 (1<<2) /\* Accept a Level 2 int vector \*/

[ 22](intc__esp32_8h.md#a88ed1ea08351b07086a6e73a0487b0d8)#define ESP\_INTR\_FLAG\_LEVEL3 (1<<3) /\* Accept a Level 3 int vector \*/

[ 23](intc__esp32_8h.md#abb43226aa7d32763f17ee6a56090b322)#define ESP\_INTR\_FLAG\_LEVEL4 (1<<4) /\* Accept a Level 4 int vector \*/

[ 24](intc__esp32_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)#define ESP\_INTR\_FLAG\_LEVEL5 (1<<5) /\* Accept a Level 5 int vector \*/

[ 25](intc__esp32_8h.md#a8defb5130273462e32ed399dece67024)#define ESP\_INTR\_FLAG\_LEVEL6 (1<<6) /\* Accept a Level 6 int vector \*/

[ 26](intc__esp32_8h.md#a9e57c700cf362161d807657571280abe)#define ESP\_INTR\_FLAG\_NMI (1<<7) /\* Accept a Level 7 int vector, highest priority \*/

[ 27](intc__esp32_8h.md#afc7bfcea2e621d81336ea6dd23310363)#define ESP\_INTR\_FLAG\_SHARED (1<<8) /\* Interrupt can be shared between ISRs \*/

[ 28](intc__esp32_8h.md#a0ab957dd5055fe20725624db223f9535)#define ESP\_INTR\_FLAG\_EDGE (1<<9) /\* Edge-triggered interrupt \*/

[ 29](intc__esp32_8h.md#a3fb8d6fa8b5e33b3503e86917bc8367b)#define ESP\_INTR\_FLAG\_IRAM (1<<10) /\* ISR can be called if cache is disabled \*/

[ 30](intc__esp32_8h.md#a76d024609ecd48dc17b586b91e779b88)#define ESP\_INTR\_FLAG\_INTRDISABLED (1<<11) /\* Return with this interrupt disabled \*/

31

32/\* Low and medium prio interrupts. These can be handled in C. \*/

[ 33](intc__esp32_8h.md#a9b0bc1a2b5cc22b499e041742ae1b17b)#define ESP\_INTR\_FLAG\_LOWMED (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3)

34

35/\* High level interrupts. Need to be handled in assembly. \*/

[ 36](intc__esp32_8h.md#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)#define ESP\_INTR\_FLAG\_HIGH (ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

37 ESP\_INTR\_FLAG\_NMI)

38

39/\* Mask for all level flags \*/

[ 40](intc__esp32_8h.md#a610949ce2bf8d7adae528f816acc5725)#define ESP\_INTR\_FLAG\_LEVELMASK (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3| \

41 ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

42 ESP\_INTR\_FLAG\_NMI)

43

44/\*

45 \* Get the interrupt flags from the supplied priority.

46 \*/

[ 47](intc__esp32_8h.md#a447e94d9632ed5c38f1ea36cbc283c4a)#define ESP\_PRIO\_TO\_FLAGS(priority) \

48 ((priority) > 0 ? ((1 << (priority)) & ESP\_INTR\_FLAG\_LEVELMASK) : 0)

49

50/\*

51 \* Check interrupt flags from input and filter unallowed values.

52 \*/

[ 53](intc__esp32_8h.md#a4dac251442759ec39f07862b435e3dc1)#define ESP\_INT\_FLAGS\_CHECK(int\_flags) ((int\_flags) & ESP\_INTR\_FLAG\_SHARED)

54

55/\*

56 \* The esp\_intr\_alloc\* functions can allocate an int for all \*\_INTR\_SOURCE int sources that

57 \* are routed through the interrupt mux. Apart from these sources, each core also has some internal

58 \* sources that do not pass through the interrupt mux. To allocate an interrupt for these sources,

59 \* pass these pseudo-sources to the functions.

60 \*/

[ 61](intc__esp32_8h.md#a2ff354dc48600b4dcbce4569c5d15bc1)#define ETS\_INTERNAL\_TIMER0\_INTR\_SOURCE -1 /\* Xtensa timer 0 interrupt source \*/

[ 62](intc__esp32_8h.md#ad28849af2335d2c6d9e07949f8ea953d)#define ETS\_INTERNAL\_TIMER1\_INTR\_SOURCE -2 /\* Xtensa timer 1 interrupt source \*/

[ 63](intc__esp32_8h.md#ad94487ae3c0ae2b9e4bccad6ce26d761)#define ETS\_INTERNAL\_TIMER2\_INTR\_SOURCE -3 /\* Xtensa timer 2 interrupt source \*/

[ 64](intc__esp32_8h.md#a7cd02abe5015f1be30d77e1be15bd448)#define ETS\_INTERNAL\_SW0\_INTR\_SOURCE -4 /\* Software int source 1 \*/

[ 65](intc__esp32_8h.md#aa81d606c0199b91aba7633270ca314e6)#define ETS\_INTERNAL\_SW1\_INTR\_SOURCE -5 /\* Software int source 2 \*/

[ 66](intc__esp32_8h.md#a6cac8d828d3ec24b9bb58fe0cb3d59fc)#define ETS\_INTERNAL\_PROFILING\_INTR\_SOURCE -6 /\* Int source for profiling \*/

67

68/\* Function prototype for interrupt handler function \*/

[ 69](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2)typedef void (\*[intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2))(void \*arg);

70

71/\* Interrupt handler associated data structure \*/

[ 72](intc__esp32_8h.md#a3d8b814c26ba94933e16bc264bdbb7f8)typedef struct [intr\_handle\_data\_t](structintr__handle__data__t.md) [intr\_handle\_data\_t](structintr__handle__data__t.md);

73

74/\* Handle to an interrupt handler \*/

[ 75](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105)typedef [intr\_handle\_data\_t](structintr__handle__data__t.md) \*[intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105);

76

[ 77](structshared__vector__desc__t.md)struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) {

[ 78](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41) int [disabled](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41) : 1;

[ 79](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517) int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517) : 8;

[ 80](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[statusreg](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f);

[ 81](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [statusmask](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb);

[ 82](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84) [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) [isr](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84);

[ 83](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e) void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e);

[ 84](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[next](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605);

85};

86

87/\* Pack using bitfields for better memory use \*/

[ 88](structvector__desc__t.md)struct [vector\_desc\_t](structvector__desc__t.md) {

[ 89](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970) int [flags](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970) : 16; /\* OR of VECDESC\_FLAG\_\* defines \*/

[ 90](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9) unsigned int [cpu](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9) : 1;

[ 91](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77) unsigned int [intno](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77) : 5;

[ 92](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc) int [source](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc) : 8; /\* Int mux flags, used when not shared \*/

[ 93](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[shared\_vec\_info](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967); /\* used when VECDESC\_FL\_SHARED \*/

[ 94](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8) struct [vector\_desc\_t](structvector__desc__t.md) \*[next](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8);

95};

96

[ 98](structintr__handle__data__t.md)struct [intr\_handle\_data\_t](structintr__handle__data__t.md) {

[ 99](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036) struct [vector\_desc\_t](structvector__desc__t.md) \*[vector\_desc](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036);

[ 100](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e) struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \*[shared\_vector\_desc](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e);

101};

102

[ 118](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)int [esp\_intr\_mark\_shared](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)(int intno, int cpu, bool is\_in\_iram);

119

[ 132](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)int [esp\_intr\_reserve](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)(int intno, int cpu);

133

[ 167](intc__esp32_8h.md#a3ac390e382c675364bca9e7cb5e3c322)int [esp\_intr\_alloc](intc__esp32_8h.md#a3ac390e382c675364bca9e7cb5e3c322)(int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517),

168 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

169 [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) handler,

170 void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e),

171 [intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) \*ret\_handle);

172

173

[ 209](intc__esp32_8h.md#aab9a8a47e564d406fa9a36aa015a6831)int [esp\_intr\_alloc\_intrstatus](intc__esp32_8h.md#aab9a8a47e564d406fa9a36aa015a6831)(int [source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517),

210 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

211 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusreg,

212 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusmask,

213 [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) handler,

214 void \*[arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e),

215 [intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) \*ret\_handle);

216

217

[ 236](intc__esp32_8h.md#ac2f659fe4a54f1591e29ea4c1ce540e1)int [esp\_intr\_free](intc__esp32_8h.md#ac2f659fe4a54f1591e29ea4c1ce540e1)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle);

237

238

[ 246](intc__esp32_8h.md#a04d0b19e3d87390cb7a25c3cdd339141)int [esp\_intr\_get\_cpu](intc__esp32_8h.md#a04d0b19e3d87390cb7a25c3cdd339141)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle);

247

[ 255](intc__esp32_8h.md#a0f0269bcfe40a5ff90586c6848cf71cd)int [esp\_intr\_get\_intno](intc__esp32_8h.md#a0f0269bcfe40a5ff90586c6848cf71cd)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle);

256

[ 273](intc__esp32_8h.md#aa1a0dcb6bf0156f102e4db31f5e200c3)int [esp\_intr\_disable](intc__esp32_8h.md#aa1a0dcb6bf0156f102e4db31f5e200c3)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle);

274

[ 286](intc__esp32_8h.md#a703fcc25fcfd86afeb5097f527b1ebad)int [esp\_intr\_enable](intc__esp32_8h.md#a703fcc25fcfd86afeb5097f527b1ebad)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle);

287

[ 300](intc__esp32_8h.md#a0eb3aaaa35ed6fb4c8b1732025683d81)int [esp\_intr\_set\_in\_iram](intc__esp32_8h.md#a0eb3aaaa35ed6fb4c8b1732025683d81)([intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105) handle, bool is\_in\_iram);

301

[ 305](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)void [esp\_intr\_noniram\_disable](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)(void);

306

[ 310](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)void [esp\_intr\_noniram\_enable](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)(void);

311

312#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32\_H\_ \*/

[esp\_intr\_get\_cpu](intc__esp32_8h.md#a04d0b19e3d87390cb7a25c3cdd339141)

int esp\_intr\_get\_cpu(intr\_handle\_t handle)

Get CPU number an interrupt is tied to.

[esp\_intr\_set\_in\_iram](intc__esp32_8h.md#a0eb3aaaa35ed6fb4c8b1732025683d81)

int esp\_intr\_set\_in\_iram(intr\_handle\_t handle, bool is\_in\_iram)

Set the "in IRAM" status of the handler.

[esp\_intr\_get\_intno](intc__esp32_8h.md#a0f0269bcfe40a5ff90586c6848cf71cd)

int esp\_intr\_get\_intno(intr\_handle\_t handle)

Get the allocated interrupt for a certain handle.

[esp\_intr\_alloc](intc__esp32_8h.md#a3ac390e382c675364bca9e7cb5e3c322)

int esp\_intr\_alloc(int source, int flags, intr\_handler\_t handler, void \*arg, intr\_handle\_t \*ret\_handle)

Allocate an interrupt with the given parameters.

[esp\_intr\_noniram\_disable](intc__esp32_8h.md#a63263dc3bf78c25b514f739e6381ee64)

void esp\_intr\_noniram\_disable(void)

Disable interrupts that aren't specifically marked as running from IRAM.

[intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2)

void(\* intr\_handler\_t)(void \*arg)

**Definition** intc\_esp32.h:69

[esp\_intr\_enable](intc__esp32_8h.md#a703fcc25fcfd86afeb5097f527b1ebad)

int esp\_intr\_enable(intr\_handle\_t handle)

Enable the interrupt associated with the handle.

[esp\_intr\_noniram\_enable](intc__esp32_8h.md#a917f8af7f0c6af92dfbd1f7689c39cae)

void esp\_intr\_noniram\_enable(void)

Re-enable interrupts disabled by esp\_intr\_noniram\_disable.

[esp\_intr\_disable](intc__esp32_8h.md#aa1a0dcb6bf0156f102e4db31f5e200c3)

int esp\_intr\_disable(intr\_handle\_t handle)

Disable the interrupt associated with the handle.

[esp\_intr\_reserve](intc__esp32_8h.md#aa6eef593f8a838adec4d258346b087d0)

int esp\_intr\_reserve(int intno, int cpu)

Reserve an interrupt to be used outside of this framework.

[esp\_intr\_alloc\_intrstatus](intc__esp32_8h.md#aab9a8a47e564d406fa9a36aa015a6831)

int esp\_intr\_alloc\_intrstatus(int source, int flags, uint32\_t intrstatusreg, uint32\_t intrstatusmask, intr\_handler\_t handler, void \*arg, intr\_handle\_t \*ret\_handle)

Allocate an interrupt with the given parameters.

[esp\_intr\_mark\_shared](intc__esp32_8h.md#aafc6d38bb52a59bd024809efcb3b64f0)

int esp\_intr\_mark\_shared(int intno, int cpu, bool is\_in\_iram)

Mark an interrupt as a shared interrupt.

[intr\_handle\_t](intc__esp32_8h.md#ab011a236fc3c9318f38ae4cdb9a26105)

intr\_handle\_data\_t \* intr\_handle\_t

**Definition** intc\_esp32.h:75

[esp\_intr\_free](intc__esp32_8h.md#ac2f659fe4a54f1591e29ea4c1ce540e1)

int esp\_intr\_free(intr\_handle\_t handle)

Disable and free an interrupt.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intr\_handle\_data\_t](structintr__handle__data__t.md)

Interrupt handler associated data structure.

**Definition** intc\_esp32.h:98

[intr\_handle\_data\_t::vector\_desc](structintr__handle__data__t.md#a54ce22a2f0818180fbe25d0e9edf2036)

struct vector\_desc\_t \* vector\_desc

**Definition** intc\_esp32.h:99

[intr\_handle\_data\_t::shared\_vector\_desc](structintr__handle__data__t.md#a86785e459328fac2f0758d588159bf3e)

struct shared\_vector\_desc\_t \* shared\_vector\_desc

**Definition** intc\_esp32.h:100

[shared\_vector\_desc\_t](structshared__vector__desc__t.md)

**Definition** intc\_esp32.h:77

[shared\_vector\_desc\_t::disabled](structshared__vector__desc__t.md#a36afb23eff0489280549ac96fea0ee41)

int disabled

**Definition** intc\_esp32.h:78

[shared\_vector\_desc\_t::arg](structshared__vector__desc__t.md#a4ab5f28adbb5115ca6a37a3ab6c5328e)

void \* arg

**Definition** intc\_esp32.h:83

[shared\_vector\_desc\_t::statusmask](structshared__vector__desc__t.md#a9078649e1b33c0ad3ee624789fda95cb)

uint32\_t statusmask

**Definition** intc\_esp32.h:81

[shared\_vector\_desc\_t::isr](structshared__vector__desc__t.md#aa438daab7ce59980b664824142be8f84)

intr\_handler\_t isr

**Definition** intc\_esp32.h:82

[shared\_vector\_desc\_t::statusreg](structshared__vector__desc__t.md#acb593daeddd30515742759a73fc7838f)

volatile uint32\_t \* statusreg

**Definition** intc\_esp32.h:80

[shared\_vector\_desc\_t::next](structshared__vector__desc__t.md#aee24289457fcde842c2b557bce5cd605)

struct shared\_vector\_desc\_t \* next

**Definition** intc\_esp32.h:84

[shared\_vector\_desc\_t::source](structshared__vector__desc__t.md#af868d1b2bf579938907ef07f5b15d517)

int source

**Definition** intc\_esp32.h:79

[vector\_desc\_t](structvector__desc__t.md)

**Definition** intc\_esp32.h:88

[vector\_desc\_t::flags](structvector__desc__t.md#a08740a5225fef571398bbd91a42fc970)

int flags

**Definition** intc\_esp32.h:89

[vector\_desc\_t::next](structvector__desc__t.md#a4b3b6db584511e25407e187d4dbf6ac8)

struct vector\_desc\_t \* next

**Definition** intc\_esp32.h:94

[vector\_desc\_t::intno](structvector__desc__t.md#a74e81e89da2ca79df99911d0599e5f77)

unsigned int intno

**Definition** intc\_esp32.h:91

[vector\_desc\_t::cpu](structvector__desc__t.md#a853c50cd06725b9502fa14af262d76b9)

unsigned int cpu

**Definition** intc\_esp32.h:90

[vector\_desc\_t::source](structvector__desc__t.md#a8adcec0946b8790de75af65a6ae03ccc)

int source

**Definition** intc\_esp32.h:92

[vector\_desc\_t::shared\_vec\_info](structvector__desc__t.md#a9934f0a683b6f2145ce35a395a65b967)

struct shared\_vector\_desc\_t \* shared\_vec\_info

**Definition** intc\_esp32.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_esp32.h](intc__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
