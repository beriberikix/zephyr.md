---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel__arch__interface_8h.html
original_path: doxygen/html/kernel__arch__interface_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_arch\_interface.h File Reference

Internal kernel APIs implemented at the architecture layer.
[More...](#details)

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/arch_interface.h](arch__interface_8h_source.md)>`  
`#include <kernel_arch_func.h>`

[Go to the source code of this file.](kernel__arch__interface_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) { [ARCH\_PAGE\_LOCATION\_PAGED\_OUT](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bacf9e624eac380ea2bfa37632c4d17a3a) , [ARCH\_PAGE\_LOCATION\_PAGED\_IN](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0bae378a008f497ae10ab50cab06f8c36db) , [ARCH\_PAGE\_LOCATION\_BAD](group__arch-mmu.md#gga65e10c80055d7e695add000f2ccfbb0ba7ff70acdf02345b5fa4c42ed2b2adde9) } |
|  | Status of a particular page location. [More...](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) |

| Functions | |
| --- | --- |
| void | [arch\_busy\_wait](group__arch-timing.md#gaffc9f3013d53e72c25243ce4f972549f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait) |
|  | Architecture-specific implementation of busy-waiting. |
| void | [arch\_new\_thread](group__arch-threads.md#gade449838e445fa8201266e38215c616c) (struct [k\_thread](structk__thread.md) \*thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3) |
|  | Handle arch-specific logic for setting up new threads. |
| static void | [arch\_switch](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025) (void \*switch\_to, void \*\*switched\_from) |
|  | Cooperative context switch primitive. |
| void | [arch\_switch\_to\_main\_thread](group__arch-threads.md#ga3ddd51635018a2e0235d5599401f5269) (struct [k\_thread](structk__thread.md) \*main\_thread, char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) \_main) |
|  | Custom logic for entering main thread context at early boot. |
| int | [arch\_float\_disable](group__arch-threads.md#ga7c2f0ee0bee6f9de0bd23a0aa321a46d) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Disable floating point context preservation. |
| int | [arch\_float\_enable](group__arch-threads.md#gacd40e26783f3dbd8a658fc1af512fb18) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Enable floating point context preservation. |
| FUNC\_NORETURN void | [arch\_system\_halt](group__arch-pm.md#gada83bf3beb5004a39a1f9c8c7ce35348) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |
|  | Halt the system, optionally propagating a reason code. |
| static \_Bool | [arch\_is\_in\_isr](group__arch-irq.md#gaee3fe4c82d94c4d307ea3e1169eb9573) (void) |
|  | Test if the current context is in interrupt context. |
| void | [arch\_mem\_map](group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map physical memory into the virtual address space. |
| void | [arch\_mem\_unmap](group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Remove mappings for a provided virtual address range. |
| int | [arch\_page\_phys\_get](group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200) (void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys) |
|  | Get the mapped physical memory address from virtual address. |
| void | [arch\_reserved\_pages\_update](group__arch-mmu.md#ga229fa5699ad47951235af494f3d2a06a) (void) |
|  | Update page frame database with reserved pages. |
| void | [arch\_mem\_page\_out](group__arch-mmu.md#ga4c13ffab5b5a5f8c93971c4d3b51bd8f) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Update all page tables for a paged-out data page. |
| void | [arch\_mem\_page\_in](group__arch-mmu.md#ga3c446aea862e37d479a809582322b3ae) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Update all page tables for a paged-in data page. |
| void | [arch\_mem\_scratch](group__arch-mmu.md#gae4e82c3100b08bdfdcd9361d316735a1) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Update current page tables for a temporary mapping. |
| enum [arch\_page\_location](group__arch-mmu.md#ga65e10c80055d7e695add000f2ccfbb0b) | [arch\_page\_location\_get](group__arch-mmu.md#ga74b3ce1173b91a8f82c25ef89f9fbbc0) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location) |
|  | Fetch location information about a page at a particular address. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_page\_info\_get](group__arch-mmu.md#gae4db701524d0614d0104706dc2a03a6c) (void \*addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location, \_Bool clear\_accessed) |
|  | Retrieve page characteristics from the page table(s). |
| int | [arch\_printk\_char\_out](group__arch-misc.md#ga6860efc93b8ba35911cfb0afbe372623) (int c) |
|  | Early boot console output hook. |
| static void | [arch\_kernel\_init](group__arch-misc.md#ga62cc65268b396d2683e47c09c9b62af5) (void) |
|  | Architecture-specific kernel initialization hook. |
| static void | [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154) (void) |
|  | Do nothing and return. |
| void | [arch\_coredump\_info\_dump](group__arch-coredump.md#ga081b713e38ca635184f5f07bd7fd7a16) (const z\_arch\_esf\_t \*esf) |
|  | Architecture-specific handling during coredump. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [arch\_coredump\_tgt\_code\_get](group__arch-coredump.md#ga1d9b0c011a03434272ff9bec120f273d) (void) |
|  | Get the target code specified by the architecture. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_tls\_stack\_setup](group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc) (struct [k\_thread](structk__thread.md) \*new\_thread, char \*stack\_ptr) |
|  | Setup Architecture-specific TLS area in stack. |

## Detailed Description

Internal kernel APIs implemented at the architecture layer.

Not all architecture-specific defines are here, APIs that are used by public functions and macros are defined in include/sys/arch\_interface.h.

For all inline functions prototyped here, the implementation is expected to be provided by arch/ARCH/include/kernel\_arch\_func.h

- [kernel](dir_dc43877d82dd332f9fb2071fcca799d6.md)
- [include](dir_009f605b833ac4622acd6c3c0c26c0f0.md)
- [kernel\_arch\_interface.h](kernel__arch__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
