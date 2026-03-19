---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/other/float.html
original_path: kernel/services/other/float.html
---

# Floating Point Services

The kernel allows threads to use floating point registers on board
configurations that support these registers.

Note

Floating point services are currently available only for boards
based on ARM Cortex-M SoCs supporting the Floating Point Extension,
the Intel x86 architecture, the SPARC architecture and ARCv2 SoCs
supporting the Floating Point Extension. The services provided
are architecture specific.

The kernel does not support the use of floating point registers by ISRs.

## [Concepts](#id1)

The kernel can be configured to provide only the floating point services
required by an application. Three modes of operation are supported,
which are described below. In addition, the kernel’s support for the SSE
registers can be included or omitted, as desired.

### [No FP registers mode](#id2)

This mode is used when the application has no threads that use floating point
registers. It is the kernel’s default floating point services mode.

If a thread uses any floating point register,
the kernel generates a fatal error condition and aborts the thread.

### [Unshared FP registers mode](#id3)

This mode is used when the application has only a single thread
that uses floating point registers.

On x86 platforms, the kernel initializes the floating point registers so they can
be used by any thread (initialization in skipped on ARM Cortex-M platforms and
ARCv2 platforms). The floating point registers are left unchanged whenever a
context switch occurs.

Note

The behavior is undefined, if two or more threads attempt to use
the floating point registers, as the kernel does not attempt to detect
(or prevent) multiple threads from using these registers.

### [Shared FP registers mode](#id4)

This mode is used when the application has two or more threads that use
floating point registers. Depending upon the underlying CPU architecture,
the kernel supports one or more of the following thread sub-classes:

- non-user: A thread that cannot use any floating point registers
- FPU user: A thread that can use the standard floating point registers
- SSE user: A thread that can use both the standard floating point registers
  and SSE registers

The kernel initializes and enables access to the floating point registers,
so they can be used
by any thread, then saves and restores these registers during
context switches to ensure the computations performed by each FPU user
or SSE user are not impacted by the computations performed by the other users.

#### ARM Cortex-M architecture (with the Floating Point Extension)

Note

The Shared FP registers mode is the default Floating Point
Services mode in ARM Cortex-M.

On the ARM Cortex-M architecture with the Floating Point Extension, the kernel
treats *all* threads as FPU users when shared FP registers mode is enabled.
This means that any thread is allowed to access the floating point registers.
The ARM kernel automatically detects that a given thread is using the floating
point registers the first time the thread accesses them.

Pretag a thread that intends to use the FP registers by
using one of the techniques listed below.

- A statically-created ARM thread can be pretagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) option to [`K_THREAD_DEFINE`](../../../doxygen/html/group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2).
- A dynamically-created ARM thread can be pretagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) option to [`k_thread_create()`](../../../doxygen/html/group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367).

Pretagging a thread with the [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) option instructs the
MPU-based stack protection mechanism to properly configure the size of
the thread’s guard region to always guarantee stack overflow detection,
and enable lazy stacking for the given thread upon thread creation.

During thread context switching the ARM kernel saves the *callee-saved*
floating point registers, if the switched-out thread has been using them.
Additionally, the *caller-saved* floating point registers are saved on
the thread’s stack. If the switched-in thread has been using the floating
point registers, the kernel restores the *callee-saved* FP registers of
the switched-in thread and the *caller-saved* FP context is restored from
the thread’s stack. Thus, the kernel does not save or restore the FP
context of threads that are not using the FP registers.

Each thread that intends to use the floating point registers must provide
an extra 72 bytes of stack space where the callee-saved FP context can
be saved.

[Lazy Stacking](https://developer.arm.com/documentation/dai0298/a)
is currently enabled in Zephyr applications on ARM Cortex-M
architecture, minimizing interrupt latency, when the floating
point context is active.

When the MPU-based stack protection mechanism is not enabled, lazy stacking
is always active in the Zephyr application. When the MPU-based stack protection
is enabled, the following rules apply with respect to lazy stacking:

- Lazy stacking is activated by default on threads that are pretagged with
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951)
- Lazy stacking is activated dynamically on threads that are not pretagged with
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951), as soon as the kernel detects that they are using the
  floating point registers.

If an ARM thread does not require use of the floating point registers any
more, it can call [`k_float_disable()`](../../../doxygen/html/group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1). This instructs the kernel
not to save or restore its FP context during thread context switching.

#### ARM64 architecture

Note

The Shared FP registers mode is the default Floating Point
Services mode on ARM64. The compiler is free to optimize code
using FP/SIMD registers, and library functions such as memcpy
are known to make use of them.

On the ARM64 (Aarch64) architecture the kernel treats each thread as a FPU
user on a case-by-case basis. A “lazy save” algorithm is used during context
switching which updates the floating point registers only when it is absolutely
necessary. For example, the registers are *not* saved when switching from an
FPU user to a non-user thread, and then back to the original FPU user.

FPU register usage by ISRs is supported although not recommended. When an
ISR uses floating point or SIMD registers, then the access is trapped, the
current FPU user context is saved in the thread object and the ISR is resumed
with interrupts disabled so to prevent another IRQ from interrupting the ISR
and potentially requesting FPU usage. Because ISR don’t have a persistent
register context, there are no provision for saving an ISR’s FPU context
either, hence the IRQ disabling.

Each thread object becomes 512 bytes larger when Shared FP registers mode
is enabled.

#### ARCv2 architecture

On the ARCv2 architecture, the kernel treats each thread as a non-user
or FPU user and the thread must be tagged by one of the
following techniques.

- A statically-created ARC thread can be tagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) option to [`K_THREAD_DEFINE`](../../../doxygen/html/group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2).
- A dynamically-created ARC thread can be tagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) to [`k_thread_create()`](../../../doxygen/html/group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367).

If an ARC thread does not require use of the floating point registers any
more, it can call [`k_float_disable()`](../../../doxygen/html/group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1). This instructs the kernel
not to save or restore its FP context during thread context switching.

During thread context switching the ARC kernel saves the *callee-saved*
floating point registers, if the switched-out thread has been using them.
Additionally, the *caller-saved* floating point registers are saved on
the thread’s stack. If the switched-in thread has been using the floating
point registers, the kernel restores the *callee-saved* FP registers of
the switched-in thread and the *caller-saved* FP context is restored from
the thread’s stack. Thus, the kernel does not save or restore the FP
context of threads that are not using the FP registers. An extra 16 bytes
(single floating point hardware) or 32 bytes (double floating point hardware)
of stack space is required to load and store floating point registers.

#### RISC-V architecture

On the RISC-V architecture the kernel treats each thread as an FPU
user on a case-by-case basis with the FPU access allocated on demand.
A “lazy save” algorithm is used during context switching which updates
the floating point registers only when it is absolutely necessary.
For example, the FPU registers are *not* saved when switching from an
FPU user to a non-user thread (or an FPU user that doesn’t touch the FPU
during its scheduling slot), and then back to the original FPU user.

FPU register usage by ISRs is supported although not recommended. When an
ISR uses floating point or SIMD registers, then the access is trapped, the
current FPU user context is saved in the thread object and the ISR is resumed
with interrupts disabled so to prevent another IRQ from interrupting the ISR
and potentially requesting FPU usage. Because ISR don’t have a persistent
register context, there are no provision for saving an ISR’s FPU context
either, hence the IRQ disabling.

As an optimization, the FPU context is preemptively restored upon scheduling
back an “active FPU user” thread that had its FPU context saved away due to
FPU usage by another thread. Active FPU users are so designated when they
make the FPU state “dirty” during their most recent scheduling slot before
being scheduled out. So if a thread doesn’t modify the FPU state within its
scheduling slot and another thread claims the FPU for itself afterwards then
that first thread will be subjected to the on-demand regime and won’t have
its FPU context restored until it attempts to access it again. But if that
thread does modify the FPU before being scheduled out then it is likely to
continue using it when scheduled back in and preemptively restoring its FPU
context saves on the exception trap overhead that would occur otherwise.

Each thread object becomes 136 bytes (single-precision floating point
hardware) or 264 bytes (double-precision floating point hardware) larger
when Shared FP registers mode is enabled.

#### SPARC architecture

On the SPARC architecture, the kernel treats each thread as a non-user
or FPU user and the thread must be tagged by one of the
following techniques:

- A statically-created thread can be tagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) option to [`K_THREAD_DEFINE`](../../../doxygen/html/group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2).
- A dynamically-created thread can be tagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) to [`k_thread_create()`](../../../doxygen/html/group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367).

During thread context switch at exit from interrupt handler, the SPARC
kernel saves *all* floating point registers, if the FPU was enabled in
the switched-out thread. Floating point registers are saved on the thread’s
stack. Floating point registers are restored when a thread context is restored
iff they were saved at the context save. Saving and restoring of the floating
point registers is synchronous and thus not lazy. The FPU is always disabled
when an ISR is called (independent of [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING")).

Floating point disabling with [`k_float_disable()`](../../../doxygen/html/group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1) is not implemented.

When [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING") is used, then 136 bytes of stack space
is required for each FPU user thread to load and store floating point
registers. No extra stack is required if [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING") is
not used.

#### x86 architecture

On the x86 architecture the kernel treats each thread as a non-user,
FPU user or SSE user on a case-by-case basis. A “lazy save” algorithm is used
during context switching which updates the floating point registers only when
it is absolutely necessary. For example, the registers are *not* saved when
switching from an FPU user to a non-user thread, and then back to the original
FPU user. The following table indicates the amount of additional stack space a
thread must provide so the registers can be saved properly.

| Thread type | FP register use | Extra stack space required |
| --- | --- | --- |
| cooperative | any | 0 bytes |
| preemptive | none | 0 bytes |
| preemptive | FPU | 108 bytes |
| preemptive | SSE | 464 bytes |

The x86 kernel automatically detects that a given thread is using
the floating point registers the first time the thread accesses them.
The thread is tagged as an SSE user if the kernel has been configured
to support the SSE registers, or as an FPU user if the SSE registers are
not supported. If this would result in a thread that is an FPU user being
tagged as an SSE user, or if the application wants to avoid the exception
handling overhead involved in auto-tagging threads, it is possible to
pretag a thread using one of the techniques listed below.

- A statically-created x86 thread can be pretagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) or [`K_SSE_REGS`](../../../doxygen/html/group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7) option to
  [`K_THREAD_DEFINE`](../../../doxygen/html/group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2).
- A dynamically-created x86 thread can be pretagged by passing the
  [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) or [`K_SSE_REGS`](../../../doxygen/html/group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7) option to
  [`k_thread_create()`](../../../doxygen/html/group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367).
- An already-created x86 thread can pretag itself once it has started
  by passing the [`K_FP_REGS`](../../../doxygen/html/group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951) or [`K_SSE_REGS`](../../../doxygen/html/group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7) option to
  [`k_float_enable()`](../../../doxygen/html/group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77).

If an x86 thread uses the floating point registers infrequently it can call
[`k_float_disable()`](../../../doxygen/html/group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1) to remove its tagging as an FPU user or SSE user.
This eliminates the need for the kernel to take steps to preserve
the contents of the floating point registers during context switches
when there is no need to do so.
When the thread again needs to use the floating point registers it can re-tag
itself as an FPU user or SSE user by calling [`k_float_enable()`](../../../doxygen/html/group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77).

## [Implementation](#id5)

### [Performing Floating Point Arithmetic](#id6)

No special coding is required for a thread to use floating point arithmetic
if the kernel is properly configured.

The following code shows how a routine can use floating point arithmetic
to avoid overflow issues when computing the average of a series of integer
values.

```c
int average(int *values, int num_values)
{
    double sum;
    int i;

    sum = 0.0;

    for (i = 0; i < num_values; i++) {
        sum += *values;
        values++;
    }

    return (int)((sum / num_values) + 0.5);
}
```

## [Suggested Uses](#id7)

Use the kernel floating point services when an application needs to
perform floating point operations.

## [Configuration Options](#id8)

To configure unshared FP registers mode, enable the [`CONFIG_FPU`](../../../kconfig.md#CONFIG_FPU "CONFIG_FPU")
configuration option and leave the [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING") configuration
option disabled.

To configure shared FP registers mode, enable both the [`CONFIG_FPU`](../../../kconfig.md#CONFIG_FPU "CONFIG_FPU")
configuration option and the [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING") configuration option.
Also, ensure that any thread that uses the floating point registers has
sufficient added stack space for saving floating point register values
during context switches, as described above.

For x86, use the [`CONFIG_X86_SSE`](../../../kconfig.md#CONFIG_X86_SSE "CONFIG_X86_SSE") configuration option to enable
support for SSEx instructions.

## [API Reference](#id9)

[Floating Point APIs](../../../doxygen/html/group__float__apis.md)
