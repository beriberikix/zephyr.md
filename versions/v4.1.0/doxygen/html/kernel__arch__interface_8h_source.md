---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/kernel__arch__interface_8h_source.html
original_path: doxygen/html/kernel__arch__interface_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

20#include <[zephyr/kernel.h](kernel_8h.md)>

21#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

22

23#ifndef \_ASMLANGUAGE

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

33#ifdef CONFIG\_ARCH\_HAS\_CUSTOM\_BUSY\_WAIT

[ 39](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f)void [arch\_busy\_wait](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait);

40#endif /\* CONFIG\_ARCH\_HAS\_CUSTOM\_BUSY\_WAIT \*/

41

43

49

[ 76](group__arch-threads.md#gade449838e445fa8201266e38215c616c)void [arch\_new\_thread](group__arch-threads.md#gade449838e445fa8201266e38215c616c)(struct [k\_thread](structk__thread.md) \*thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

77 char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry,

78 void \*p1, void \*p2, void \*p3);

79

80#ifdef CONFIG\_USE\_SWITCH

[ 131](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025)static inline void [arch\_switch](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025)(void \*switch\_to, void \*\*switched\_from);

132#endif /\* CONFIG\_USE\_SWITCH \*/

133

134#if !defined(CONFIG\_USE\_SWITCH) || defined(\_\_DOXYGEN\_\_)

135#if defined(\_\_DOXYGEN\_\_)

[ 148](group__arch-threads.md#ga05c03d97386bc973a403102f4c048444)int [arch\_swap](group__arch-threads.md#ga05c03d97386bc973a403102f4c048444)(unsigned int key);

149#endif /\* \_\_DOXYGEN\_\_ \*/

150

159static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void

[ 160](group__arch-threads.md#ga61b6981d7dd768fa01922c6c6ab9780f)[arch\_thread\_return\_value\_set](group__arch-threads.md#ga61b6981d7dd768fa01922c6c6ab9780f)(struct [k\_thread](structk__thread.md) \*thread, unsigned int value);

161#endif /\* !CONFIG\_USE\_SWITCH || \_\_DOXYGEN\_\_ \*/

162

163#ifdef CONFIG\_ARCH\_HAS\_CUSTOM\_SWAP\_TO\_MAIN

[ 174](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)void [arch\_switch\_to\_main\_thread](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)(struct [k\_thread](structk__thread.md) \*main\_thread, char \*stack\_ptr,

175 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) \_main);

176#endif /\* CONFIG\_ARCH\_HAS\_CUSTOM\_SWAP\_TO\_MAIN \*/

177

178#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

[ 192](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)int [arch\_float\_disable](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)(struct [k\_thread](structk__thread.md) \*thread);

193

[ 212](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18)int [arch\_float\_enable](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

213#endif /\* CONFIG\_FPU && CONFIG\_FPU\_SHARING \*/

214

215#if defined(CONFIG\_USERSPACE) && defined(CONFIG\_ARCH\_HAS\_THREAD\_PRIV\_STACK\_SPACE\_GET)

239int arch\_thread\_priv\_stack\_space\_get(const struct [k\_thread](structk__thread.md) \*thread, size\_t \*stack\_size,

240 size\_t \*unused\_ptr);

241#endif /\* CONFIG\_USERSPACE && CONFIG\_ARCH\_HAS\_THREAD\_PRIV\_STACK\_SPACE\_GET \*/

242

244

[ 251](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)FUNC\_NORETURN void [arch\_system\_halt](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)(unsigned int reason);

252

254

255

261

[ 270](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573)static inline bool [arch\_is\_in\_isr](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573)(void);

271

273

279

[ 316](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)void [arch\_mem\_map](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

317

[ 344](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)void [arch\_mem\_unmap](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)(void \*addr, size\_t size);

345

[ 367](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)int [arch\_page\_phys\_get](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys);

368

[ 379](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a)void [arch\_reserved\_pages\_update](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a)(void);

380

[ 400](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)void [arch\_mem\_page\_out](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

401

[ 419](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae)void [arch\_mem\_page\_in](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys);

420

[ 435](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1)void [arch\_mem\_scratch](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys);

436

[ 440](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b)enum [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) {

[ 442](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a) [ARCH\_PAGE\_LOCATION\_PAGED\_OUT](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a),

443

[ 445](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db) [ARCH\_PAGE\_LOCATION\_PAGED\_IN](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db),

446

[ 448](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9) [ARCH\_PAGE\_LOCATION\_BAD](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9)

449};

450

[ 478](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)enum [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) [arch\_page\_location\_get](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location);

479

489

500

508

515

[ 563](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c)[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_page\_info\_get](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c)(void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location,

564 bool clear\_accessed);

565

567

573

[ 590](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623)int [arch\_printk\_char\_out](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623)(int c);

591

592#ifdef CONFIG\_ARCH\_HAS\_THREAD\_NAME\_HOOK

605int arch\_thread\_name\_set(struct [k\_thread](structk__thread.md) \*thread, const char \*str);

606#endif /\* CONFIG\_ARCH\_HAS\_THREAD\_NAME\_HOOK \*/

607

[ 614](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5)static inline void [arch\_kernel\_init](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5)(void);

615

[ 617](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)static inline void [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)(void);

618

620

626

[ 634](group__arch-coredump.md#gae997cb3dc249bec6d5166145f37d9292)void [arch\_coredump\_info\_dump](group__arch-coredump.md#gae997cb3dc249bec6d5166145f37d9292)(const struct [arch\_esf](structarch__esf.md) \*esf);

635

[ 639](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [arch\_coredump\_tgt\_code\_get](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)(void);

640

641#if defined(CONFIG\_USERSPACE) || defined(\_\_DOXYGEN\_\_)

642

[ 650](group__arch-coredump.md#ga31bcb446604666c8f4d05ccfcbc00441)void [arch\_coredump\_priv\_stack\_dump](group__arch-coredump.md#ga31bcb446604666c8f4d05ccfcbc00441)(struct [k\_thread](structk__thread.md) \*thread);

651

652#endif /\* CONFIG\_USERSPACE || \_\_DOXYGEN\_\_ \*/

653

655

661

[ 672](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc)size\_t [arch\_tls\_stack\_setup](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc)(struct [k\_thread](structk__thread.md) \*new\_thread, char \*stack\_ptr);

673

675

676/\* Include arch-specific inline function implementation \*/

677#include <kernel\_arch\_func.h>

678

679#ifdef \_\_cplusplus

680}

681#endif

682

683#endif /\* \_ASMLANGUAGE \*/

684

685#endif /\* ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_ARCH\_INTERFACE\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:48

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[arch\_coredump\_tgt\_code\_get](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d)

uint16\_t arch\_coredump\_tgt\_code\_get(void)

Get the target code specified by the architecture.

[arch\_coredump\_priv\_stack\_dump](group__arch-coredump.md#ga31bcb446604666c8f4d05ccfcbc00441)

void arch\_coredump\_priv\_stack\_dump(struct k\_thread \*thread)

Architecture-specific handling of dumping privileged stack.

[arch\_coredump\_info\_dump](group__arch-coredump.md#gae997cb3dc249bec6d5166145f37d9292)

void arch\_coredump\_info\_dump(const struct arch\_esf \*esf)

Architecture-specific handling during coredump.

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

**Definition** kernel\_arch\_interface.h:440

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

**Definition** kernel\_arch\_interface.h:448

[ARCH\_PAGE\_LOCATION\_PAGED\_OUT](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a)

@ ARCH\_PAGE\_LOCATION\_PAGED\_OUT

The page has been evicted to the backing store.

**Definition** kernel\_arch\_interface.h:442

[ARCH\_PAGE\_LOCATION\_PAGED\_IN](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db)

@ ARCH\_PAGE\_LOCATION\_PAGED\_IN

The page is resident in memory.

**Definition** kernel\_arch\_interface.h:445

[arch\_system\_halt](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348)

FUNC\_NORETURN void arch\_system\_halt(unsigned int reason)

Halt the system, optionally propagating a reason code.

[arch\_swap](group__arch-threads.md#ga05c03d97386bc973a403102f4c048444)

int arch\_swap(unsigned int key)

Cooperatively context switch.

[arch\_switch\_to\_main\_thread](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269)

void arch\_switch\_to\_main\_thread(struct k\_thread \*main\_thread, char \*stack\_ptr, k\_thread\_entry\_t \_main)

Custom logic for entering main thread context at early boot.

[arch\_thread\_return\_value\_set](group__arch-threads.md#ga61b6981d7dd768fa01922c6c6ab9780f)

static ALWAYS\_INLINE void arch\_thread\_return\_value\_set(struct k\_thread \*thread, unsigned int value)

Set the return value for the specified thread.

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

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [kernel](dir_dc43877d82dd332f9fb2071fcca799d6.md)
- [include](dir_009f605b833ac4622acd6c3c0c26c0f0.md)
- [kernel\_arch\_interface.h](kernel__arch__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
