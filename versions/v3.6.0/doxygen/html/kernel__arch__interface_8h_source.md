---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel__arch__interface_8h_source.html
original_path: doxygen/html/kernel__arch__interface_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_arch\_interface.h

[Go to the documentation of this file.](kernel__arch__interface_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

17#ifndef ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_ARCH\_INTERFACE\_H\_

18#define ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_ARCH\_INTERFACE\_H\_

19

20#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

21#include <[zephyr/sys/arch\_interface.h](arch__interface_8h.md)>

22

23#ifndef \_ASMLANGUAGE

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

33#ifdef CONFIG\_ARCH\_HAS\_CUSTOM\_BUSY\_WAIT

[ 39](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f)void [arch\_busy\_wait](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait);

40#endif

41

43

49

[ 76](group__arch-threads.md#gade449838e445fa8201266e38215c616c)void [arch\_new\_thread](group__arch-threads.md#gade449838e445fa8201266e38215c616c)(struct [k\_thread](structk__thread.md) \*thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

77 char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry,

78 void \*p1, void \*p2, void \*p3);

79

80#ifdef CONFIG\_USE\_SWITCH

[ 131](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025)static inline void [arch\_switch](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025)(void \*switch\_to, void \*\*switched\_from);

132#else

145int arch\_swap(unsigned int key);

146

155static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void

156arch\_thread\_return\_value\_set(struct [k\_thread](structk__thread.md) \*thread, unsigned int value);

157#endif /\* CONFIG\_USE\_SWITCH i\*/

158

159#ifdef CONFIG\_ARCH\_HAS\_CUSTOM\_SWAP\_TO\_MAIN

[ 170](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)void [arch\_switch\_to\_main\_thread](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)(struct [k\_thread](structk__thread.md) \*main\_thread, char \*stack\_ptr,

171 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) \_main);

172#endif /\* CONFIG\_ARCH\_HAS\_CUSTOM\_SWAP\_TO\_MAIN \*/

173

174#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

[ 188](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)int [arch\_float\_disable](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)(struct [k\_thread](structk__thread.md) \*thread);

189

[ 208](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18)int [arch\_float\_enable](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

209#endif /\* CONFIG\_FPU && CONFIG\_FPU\_SHARING \*/

210

212

[ 219](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)FUNC\_NORETURN void [arch\_system\_halt](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)(unsigned int reason);

220

222

223

229

[ 238](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573)static inline bool [arch\_is\_in\_isr](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573)(void);

239

241

247

[ 284](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)void [arch\_mem\_map](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

285

[ 312](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)void [arch\_mem\_unmap](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)(void \*addr, size\_t size);

313

[ 335](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)int [arch\_page\_phys\_get](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys);

336

[ 347](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a)void [arch\_reserved\_pages\_update](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a)(void);

348

[ 368](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)void [arch\_mem\_page\_out](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

369

[ 387](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae)void [arch\_mem\_page\_in](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys);

388

[ 403](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1)void [arch\_mem\_scratch](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys);

404

[ 408](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b)enum [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) {

[ 410](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a) [ARCH\_PAGE\_LOCATION\_PAGED\_OUT](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a),

411

[ 413](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db) [ARCH\_PAGE\_LOCATION\_PAGED\_IN](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db),

414

[ 416](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9) [ARCH\_PAGE\_LOCATION\_BAD](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)

417};

418

[ 446](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)enum [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) [arch\_page\_location\_get](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location);

447

457

468

476

483

[ 531](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c)[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_page\_info\_get](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location,

532 bool clear\_accessed);

533

535

541

[ 558](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623)int [arch\_printk\_char\_out](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623)(int c);

559

[ 566](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5)static inline void [arch\_kernel\_init](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5)(void);

567

[ 569](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)static inline void [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)(void);

570

572

578

[ 586](group__arch-coredump.md#ga081b713e38ca635184f5f07bd7fd7a16)void [arch\_coredump\_info\_dump](group__arch-coredump.md#ga081b713e38ca635184f5f07bd7fd7a16)(const z\_arch\_esf\_t \*esf);

587

[ 591](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [arch\_coredump\_tgt\_code\_get](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)(void);

592

594

600

[ 611](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc)size\_t [arch\_tls\_stack\_setup](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc)(struct [k\_thread](structk__thread.md) \*new\_thread, char \*stack\_ptr);

612

614

615/\* Include arch-specific inline function implementation \*/

616#include <kernel\_arch\_func.h>

617

618#ifdef \_\_cplusplus

619}

620#endif

621

622#endif /\* \_ASMLANGUAGE \*/

623

624#endif /\* ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_ARCH\_INTERFACE\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:47

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:45

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[arch\_coredump\_info\_dump](group__arch-coredump.md#ga081b713e38ca635184f5f07bd7fd7a16)

void arch\_coredump\_info\_dump(const z\_arch\_esf\_t \*esf)

Architecture-specific handling during coredump.

[arch\_coredump\_tgt\_code\_get](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)

uint16\_t arch\_coredump\_tgt\_code\_get(void)

Get the target code specified by the architecture.

[arch\_is\_in\_isr](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573)

static \_Bool arch\_is\_in\_isr(void)

Test if the current context is in interrupt context.

[arch\_kernel\_init](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5)

static void arch\_kernel\_init(void)

Architecture-specific kernel initialization hook.

[arch\_printk\_char\_out](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623)

int arch\_printk\_char\_out(int c)

Early boot console output hook.

[arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)

static void arch\_nop(void)

Do nothing and return.

[arch\_reserved\_pages\_update](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a)

void arch\_reserved\_pages\_update(void)

Update page frame database with reserved pages.

[arch\_mem\_page\_in](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae)

void arch\_mem\_page\_in(void \*addr, uintptr\_t phys)

Update all page tables for a paged-in data page.

[arch\_mem\_page\_out](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)

void arch\_mem\_page\_out(void \*addr, uintptr\_t location)

Update all page tables for a paged-out data page.

[arch\_mem\_map](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)

void arch\_mem\_map(void \*virt, uintptr\_t phys, size\_t size, uint32\_t flags)

Map physical memory into the virtual address space.

[arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b)

arch\_page\_location

Status of a particular page location.

**Definition** kernel\_arch\_interface.h:408

[arch\_page\_location\_get](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)

enum arch\_page\_location arch\_page\_location\_get(void \*addr, uintptr\_t \*location)

Fetch location information about a page at a particular address.

[arch\_mem\_unmap](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)

void arch\_mem\_unmap(void \*addr, size\_t size)

Remove mappings for a provided virtual address range.

[arch\_page\_phys\_get](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)

int arch\_page\_phys\_get(void \*virt, uintptr\_t \*phys)

Get the mapped physical memory address from virtual address.

[arch\_page\_info\_get](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c)

uintptr\_t arch\_page\_info\_get(void \*addr, uintptr\_t \*location, \_Bool clear\_accessed)

Retrieve page characteristics from the page table(s).

[arch\_mem\_scratch](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1)

void arch\_mem\_scratch(uintptr\_t phys)

Update current page tables for a temporary mapping.

[ARCH\_PAGE\_LOCATION\_BAD](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)

@ ARCH\_PAGE\_LOCATION\_BAD

The page is not mapped.

**Definition** kernel\_arch\_interface.h:416

[ARCH\_PAGE\_LOCATION\_PAGED\_OUT](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a)

@ ARCH\_PAGE\_LOCATION\_PAGED\_OUT

The page has been evicted to the backing store.

**Definition** kernel\_arch\_interface.h:410

[ARCH\_PAGE\_LOCATION\_PAGED\_IN](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db)

@ ARCH\_PAGE\_LOCATION\_PAGED\_IN

The page is resident in memory.

**Definition** kernel\_arch\_interface.h:413

[arch\_system\_halt](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)

FUNC\_NORETURN void arch\_system\_halt(unsigned int reason)

Halt the system, optionally propagating a reason code.

[arch\_switch\_to\_main\_thread](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)

void arch\_switch\_to\_main\_thread(struct k\_thread \*main\_thread, char \*stack\_ptr, k\_thread\_entry\_t \_main)

Custom logic for entering main thread context at early boot.

[arch\_float\_disable](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)

int arch\_float\_disable(struct k\_thread \*thread)

Disable floating point context preservation.

[arch\_switch](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025)

static void arch\_switch(void \*switch\_to, void \*\*switched\_from)

Cooperative context switch primitive.

[arch\_float\_enable](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18)

int arch\_float\_enable(struct k\_thread \*thread, unsigned int options)

Enable floating point context preservation.

[arch\_new\_thread](group__arch-threads.md#gade449838e445fa8201266e38215c616c)

void arch\_new\_thread(struct k\_thread \*thread, k\_thread\_stack\_t \*stack, char \*stack\_ptr, k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3)

Handle arch-specific logic for setting up new threads.

[arch\_busy\_wait](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f)

void arch\_busy\_wait(uint32\_t usec\_to\_wait)

Architecture-specific implementation of busy-waiting.

[arch\_tls\_stack\_setup](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc)

size\_t arch\_tls\_stack\_setup(struct k\_thread \*new\_thread, char \*stack\_ptr)

Setup Architecture-specific TLS area in stack.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

- [kernel](dir_dc43877d82dd332f9fb2071fcca799d6.md)
- [include](dir_009f605b833ac4622acd6c3c0c26c0f0.md)
- [kernel\_arch\_interface.h](kernel__arch__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
