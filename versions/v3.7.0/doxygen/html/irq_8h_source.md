---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/irq_8h_source.html
original_path: doxygen/html/irq_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](irq_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_IRQ\_H\_

12#define ZEPHYR\_INCLUDE\_IRQ\_H\_

13

14/\* Pull in the arch-specific implementations \*/

15#include <[zephyr/arch/cpu.h](cpu_8h.md)>

16

17#ifndef \_ASMLANGUAGE

18#include <[zephyr/toolchain.h](toolchain_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

30

[ 48](group__isr__apis.md#ga131739d1faf501a15590053817aba984)#define IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

49 ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

50

64static inline int

[ 65](group__isr__apis.md#ga4e9915b92b09df49b99bc449f0cc31a1)[irq\_connect\_dynamic](group__isr__apis.md#ga4e9915b92b09df49b99bc449f0cc31a1)(unsigned int irq, unsigned int priority,

66 void (\*routine)(const void \*parameter),

67 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

68{

69 return [arch\_irq\_connect\_dynamic](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308)(irq, priority, routine, parameter,

70 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

71}

72

89static inline int

[ 90](group__isr__apis.md#gabdab7745edc1e15862e1772d8673fc00)[irq\_disconnect\_dynamic](group__isr__apis.md#gabdab7745edc1e15862e1772d8673fc00)(unsigned int irq, unsigned int priority,

91 void (\*routine)(const void \*parameter),

92 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

93{

94 return [arch\_irq\_disconnect\_dynamic](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c)(irq, priority, routine,

95 parameter, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

96}

97

[ 136](group__isr__apis.md#gac6c8746ac28da6ce02b24714f4144ff3)#define IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

137 ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p)

138

[ 146](group__isr__apis.md#ga1ab99dbeb50b228001e1fca808cbaeea)#define ISR\_DIRECT\_HEADER() ARCH\_ISR\_DIRECT\_HEADER()

147

[ 163](group__isr__apis.md#ga31581157c9dbacf935f0e6a8dd456335)#define ISR\_DIRECT\_FOOTER(check\_reschedule) \

164 ARCH\_ISR\_DIRECT\_FOOTER(check\_reschedule)

165

[ 174](group__isr__apis.md#ga3c1327551dfca7818975e3fbf1470227)#define ISR\_DIRECT\_PM() ARCH\_ISR\_DIRECT\_PM()

175

[ 205](group__isr__apis.md#gaf86866cd07fd37f381d98866f8874ebf)#define ISR\_DIRECT\_DECLARE(name) ARCH\_ISR\_DIRECT\_DECLARE(name)

206

248#ifdef CONFIG\_SMP

249unsigned int z\_smp\_global\_lock(void);

[ 250](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228)#define irq\_lock() z\_smp\_global\_lock()

251#else

252#define irq\_lock() arch\_irq\_lock()

253#endif

254

276#ifdef CONFIG\_SMP

277void z\_smp\_global\_unlock(unsigned int key);

[ 278](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57)#define irq\_unlock(key) z\_smp\_global\_unlock(key)

279#else

280#define irq\_unlock(key) arch\_irq\_unlock(key)

281#endif

282

[ 290](group__isr__apis.md#ga7ea700ee31e4ff036c997a554dbedfeb)#define irq\_enable(irq) arch\_irq\_enable(irq)

291

[ 299](group__isr__apis.md#ga82c3a15d812f58e0f6525f358d031e6d)#define irq\_disable(irq) arch\_irq\_disable(irq)

300

[ 310](group__isr__apis.md#ga71fef3867ba9818cf0a5baf8410a6354)#define irq\_is\_enabled(irq) arch\_irq\_is\_enabled(irq)

311

315

316#ifdef \_\_cplusplus

317}

318#endif

319

320#endif /\* ASMLANGUAGE \*/

321#endif /\* ZEPHYR\_INCLUDE\_IRQ\_H\_ \*/

[cpu.h](cpu_8h.md)

[arch\_irq\_disconnect\_dynamic](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c)

int arch\_irq\_disconnect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Arch-specific hook to dynamically uninstall a shared interrupt.

[arch\_irq\_connect\_dynamic](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308)

int arch\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Arch-specific hook to install a dynamic interrupt.

[irq\_connect\_dynamic](group__isr__apis.md#ga4e9915b92b09df49b99bc449f0cc31a1)

static int irq\_connect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Configure a dynamic interrupt.

**Definition** irq.h:65

[irq\_disconnect\_dynamic](group__isr__apis.md#gabdab7745edc1e15862e1772d8673fc00)

static int irq\_disconnect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Disconnect a dynamic interrupt.

**Definition** irq.h:90

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq.h](irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
