---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch__interface_8h.html
original_path: doxygen/html/arch__interface_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_interface.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/irq_offload.h](irq__offload_8h_source.md)>`  
`#include <[zephyr/arch/syscall.h](arch_2syscall_8h_source.md)>`  
`#include <[zephyr/timing/types.h](include_2zephyr_2timing_2types_8h_source.md)>`  
`#include <[zephyr/arch/arch_inlines.h](arch__inlines_8h_source.md)>`

[Go to the source code of this file.](arch__interface_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef struct z\_thread\_stack\_element | [k\_thread\_stack\_t](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) |
|  | Typedef of struct z\_thread\_stack\_element. |
| typedef void(\* | [k\_thread\_entry\_t](#a3707e886593b0a8b4995309e4230b717)) (void \*p1, void \*p2, void \*p3) |
|  | Thread entry point function type. |
| typedef void(\* | [arch\_cpustart\_t](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)) (void \*data) |
|  | Per-cpu entry function. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844)) (void \*cookie, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long addr) |
|  | [stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844 "stack_trace_callback_fn - Callback for arch_stack_walk") - Callback for [arch\_stack\_walk](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2 "arch_stack_walk") |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e) (void) |
|  | Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971) (void) |
|  | As for [arch\_k\_cycle\_get\_32()](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e "Obtain the current cycle count, in units specified by CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC."), but with a 64 bit return value. |
| void | [arch\_cpu\_idle](group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48) (void) |
|  | Power save idle routine. |
| void | [arch\_cpu\_atomic\_idle](group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Atomically re-enable interrupts and enter low power mode. |
| void | [arch\_cpu\_start](group__arch-smp.md#ga32b7e543ce51498200c368c39c900bc8) (int cpu\_num, [k\_thread\_stack\_t](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, int sz, [arch\_cpustart\_t](group__arch-smp.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2) fn, void \*arg) |
|  | Start a numbered CPU on a MP-capable system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cpu\_active](group__arch-smp.md#ga5a7f0198ee061551c300129bffe64717) (int cpu\_num) |
|  | Return CPU power status. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38) (void) |
|  | Lock interrupts on the current CPU. |
| static void | [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Unlock interrupts on the current CPU. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](group__arch-irq.md#ga1b827afafc622d412962f568b78726dc) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Test if calling [arch\_irq\_unlock()](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05 "Unlock interrupts on the current CPU.") with this key would unlock irqs. |
| void | [arch\_irq\_disable](group__arch-irq.md#ga216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Disable the specified interrupt line. |
| void | [arch\_irq\_enable](group__arch-irq.md#gaa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Enable the specified interrupt line. |
| int | [arch\_irq\_is\_enabled](group__arch-irq.md#ga3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Test if an interrupt line is enabled. |
| int | [arch\_irq\_connect\_dynamic](group__arch-irq.md#gaa4d733913e12a12e104dc4781cca7308) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Arch-specific hook to install a dynamic interrupt. |
| int | [arch\_irq\_disconnect\_dynamic](group__arch-irq.md#ga41483a9fc1090d96d066e107a74ee38c) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Arch-specific hook to dynamically uninstall a shared interrupt. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_allocate](group__arch-irq.md#gaac8f60e7dfc5ce3222372798e96316ae) (void) |
|  | Arch-specific hook for allocating IRQs. |
| void | [arch\_irq\_set\_used](group__arch-irq.md#ga5f0942bd035c50c9d2d91ada472f37c4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Arch-specific hook for declaring an IRQ being used. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_is\_used](group__arch-irq.md#ga5c85d7bf54a83190ed27587dc5a01de5) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Arch-specific hook for checking if an IRQ is being used already. |
| static struct \_cpu \* | [arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2) (void) |
|  | Return the CPU struct for the currently executing CPU. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_proc\_id](group__arch-smp.md#gad628c89816128546501e3c26eaaf9dea) (void) |
|  | Processor hardware ID. |
| void | [arch\_sched\_broadcast\_ipi](group__arch-smp.md#ga8fe90cec57c56993df14c0d545106ca3) (void) |
|  | Broadcast an interrupt to all CPUs. |
| void | [arch\_sched\_directed\_ipi](group__arch-smp.md#gadebac82c1ed0a8a08adb297738d2633e) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cpu\_bitmap) |
|  | Direct IPIs to the specified CPUs. |
| int | [arch\_smp\_init](group__arch-smp.md#ga6ffc01f86f4541d1092ee4b277a07ac6) (void) |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_num\_cpus](group__arch-smp.md#ga078e9bf1a4a557d1321ddc4848092cbe) (void) |
|  | Returns the number of CPUs. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke0](group__arch-userspace.md#ga5e9ab24b9c980e327903fbe3f5bd97f3) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 0 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke1](group__arch-userspace.md#ga4cfb3b2b38e5afca889e8b9765d6c3df) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 1 argument. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke2](group__arch-userspace.md#ga1e78f1022aaf10e88727b142b56d4ef0) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 2 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke3](group__arch-userspace.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 3 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke4](group__arch-userspace.md#ga0ba3ae2290827385b226ebdbf3de3b53) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 4 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke5](group__arch-userspace.md#ga9971c78bc8f579a0dadf84225dc0c3ff) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 5 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke6](group__arch-userspace.md#gac6cae2197637993a86b6ec6803b5742b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 6 arguments. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_is\_user\_context](group__arch-userspace.md#ga89ab53a218add419e37f89c1f5fd955f) (void) |
|  | Indicate whether we are currently running in user mode. |
| int | [arch\_mem\_domain\_max\_partitions\_get](group__arch-userspace.md#ga71542fcc679a94ad9ea60d7ac46da361) (void) |
|  | Get the maximum number of partitions for a memory domain. |
| int | [arch\_buffer\_validate](group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16) (const void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int write) |
|  | Check memory region permissions. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_virt\_region\_align](group__arch-userspace.md#ga48be2412ba65ec550ded63e2f1a0470f) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Get the optimal virtual region alignment to optimize the MMU table layout. |
| FUNC\_NORETURN void | [arch\_user\_mode\_enter](group__arch-userspace.md#ga447daa0454a90a7a3a247de01e522567) ([k\_thread\_entry\_t](#a3707e886593b0a8b4995309e4230b717) user\_entry, void \*p1, void \*p2, void \*p3) |
|  | Perform a one-way transition from supervisor to user mode. |
| FUNC\_NORETURN void | [arch\_syscall\_oops](group__arch-userspace.md#gad53908f229d7e2c333574b009493644b) (void \*ssf) |
|  | Induce a kernel oops that appears to come from a specific location. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_user\_string\_nlen](group__arch-userspace.md#ga174c4f356fe315c523cefbf513858c9c) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxsize, int \*err) |
|  | Safely take the length of a potentially bad string. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_mem\_coherent](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f) (void \*ptr) |
|  | Detect memory coherence type. |
| static void | [arch\_cohere\_stacks](group__arch-userspace.md#ga306e9d0e5f8094cb75686f1c43d068a9) (struct [k\_thread](structk__thread.md) \*old\_thread, void \*old\_switch\_handle, struct [k\_thread](structk__thread.md) \*new\_thread) |
|  | Ensure cache coherence prior to context switch. |
| void | [arch\_gdb\_init](group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726) (void) |
|  | Architecture layer debug start. |
| void | [arch\_gdb\_continue](group__arch-gdbstub.md#ga9c130421feeee919651828511743b346) (void) |
|  | Continue running program. |
| void | [arch\_gdb\_step](group__arch-gdbstub.md#ga2aa577d5e55c8b739e2be6187336aaf0) (void) |
|  | Continue with one step. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_readall](group__arch-gdbstub.md#ga5317106a8022bea2a0d42af0789cc016) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Read all registers, and outputs as hexadecimal string. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_writeall](group__arch-gdbstub.md#ga0ef78d7e193e98549d9665632e53d5ca) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen) |
|  | Take a hexadecimal string and update all registers. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_readone](group__arch-gdbstub.md#gaa3216e9f381f974c374a6399af5cdba5) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno) |
|  | Read one register, and outputs as hexadecimal string. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_writeone](group__arch-gdbstub.md#gad717b520d774294bbda78a56cddcaeff) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno) |
|  | Take a hexadecimal string and update one register. |
| int | [arch\_gdb\_add\_breakpoint](group__arch-gdbstub.md#gab6f42110cf2340132bf2b3916810c01d) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind) |
|  | Add breakpoint or watchpoint. |
| int | [arch\_gdb\_remove\_breakpoint](group__arch-gdbstub.md#ga734041433f69030ad98439d10ef56ad6) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind) |
|  | Remove breakpoint or watchpoint. |
| void | [arch\_timing\_init](group__timing__api__arch.md#ga5d9923569b40437c28879ff4b3ff77c2) (void) |
|  | Initialize the timing subsystem. |
| void | [arch\_timing\_start](group__timing__api__arch.md#gaf8cd88e81c2104b5eb0fbe42967b7834) (void) |
|  | Signal the start of the timing information gathering. |
| void | [arch\_timing\_stop](group__timing__api__arch.md#ga566483c64f5c5d2f0465e3f969303fd3) (void) |
|  | Signal the end of the timing information gathering. |
| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [arch\_timing\_counter\_get](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd) (void) |
|  | Return timing counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_get](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_freq\_get](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2) (void) |
|  | Get frequency of counter used (in Hz). |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_to\_ns](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_to\_ns\_avg](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_timing\_freq\_get\_mhz](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb) (void) |
|  | Get frequency of counter used (in MHz). |
| void | [arch\_spin\_relax](#a9932b29bc0c3b86e4f8cbd6708ef5d9c) (void) |
|  | Perform architecture specific processing within spin loops. |
| void | [arch\_stack\_walk](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2) ([stack\_trace\_callback\_fn](group__arch-stackwalk.md#gaec9949df614728aa6d677f9f1fafd844) callback\_fn, void \*cookie, const struct [k\_thread](structk__thread.md) \*thread, const struct [arch\_esf](structarch__esf.md) \*esf) |
|  | Architecture-specific function to walk the stack. |

## Typedef Documentation

## [◆ ](#a3707e886593b0a8b4995309e4230b717)k\_thread\_entry\_t

| typedef void(\* k\_thread\_entry\_t) (void \*p1, void \*p2, void \*p3) |
| --- |

Thread entry point function type.

A thread's entry point function is invoked when the thread starts executing. Up to 3 argument values can be passed to the function.

The thread terminates execution permanently if the entry point function returns. The thread is responsible for releasing any shared resources it may own (such as mutexes and dynamically allocated memory), prior to returning.

Parameters
:   | p1 | First argument. |
    | --- | --- |
    | p2 | Second argument. |
    | p3 | Third argument. |

## [◆ ](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)k\_thread\_stack\_t

| typedef struct z\_thread\_stack\_element [k\_thread\_stack\_t](#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) |
| --- |

Typedef of struct z\_thread\_stack\_element.

See also
:   z\_thread\_stack\_element

## Function Documentation

## [◆ ](#a9932b29bc0c3b86e4f8cbd6708ef5d9c)arch\_spin\_relax()

| void arch\_spin\_relax | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Perform architecture specific processing within spin loops.

This is invoked from busy loops with IRQs disabled such as the contended spinlock loop. The default implementation is a weak function that calls [arch\_nop()](group__arch-misc.md#gabb087b9e158824121212d65646ae4154 "Do nothing and return."). Architectures may implement this function to perform extra checks or power management tricks if needed.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arch\_interface.h](arch__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
