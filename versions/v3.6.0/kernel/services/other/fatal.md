---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/other/fatal.html
original_path: kernel/services/other/fatal.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Fatal Errors

## Software Errors Triggered in Source Code

Zephyr provides several methods for inducing fatal error conditions through
either build-time checks, conditionally compiled assertions, or deliberately
invoked panic or oops conditions.

### Runtime Assertions

Zephyr provides some macros to perform runtime assertions which may be
conditionally compiled. Their definitions may be found in
[include/zephyr/sys/\_\_assert.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/__assert.h).

Assertions are enabled by setting the `__ASSERT_ON` preprocessor symbol to a
non-zero value. There are two ways to do this:

- Use the [`CONFIG_ASSERT`](../../../kconfig.md#CONFIG_ASSERT "CONFIG_ASSERT") and [`CONFIG_ASSERT_LEVEL`](../../../kconfig.md#CONFIG_ASSERT_LEVEL "CONFIG_ASSERT_LEVEL") kconfig
  options.
- Add `-D__ASSERT_ON=<level>` to the project’s CFLAGS, either on the
  build command line or in a CMakeLists.txt.

The `__ASSERT_ON` method takes precedence over the kconfig option if both are
used.

Specifying an assertion level of 1 causes the compiler to issue warnings that
the kernel contains debug-type `__ASSERT()` statements; this reminder is
issued since assertion code is not normally present in a final product.
Specifying assertion level 2 suppresses these warnings.

Assertions are enabled by default when running Zephyr test cases, as
configured by the [`CONFIG_TEST`](../../../kconfig.md#CONFIG_TEST "CONFIG_TEST") option.

The policy for what to do when encountering a failed assertion is controlled
by the implementation of `assert_post_action()`. Zephyr provides
a default implementation with weak linkage which invokes a kernel oops if
the thread that failed the assertion was running in user mode, and a kernel
panic otherwise.

#### \_\_ASSERT()

The `__ASSERT()` macro can be used inside kernel and application code to
perform optional runtime checks which will induce a fatal error if the
check does not pass. The macro takes a string message which will be printed
to provide context to the assertion. In addition, the kernel will print
a text representation of the expression code that was evaluated, and the
file and line number where the assertion can be found.

For example:

```c
__ASSERT(foo == 0xF0CACC1A, "Invalid value of foo, got 0x%x", foo);
```

If at runtime `foo` had some unexpected value, the error produced may
look like the following:

```text
ASSERTION FAIL [foo == 0xF0CACC1A] @ ZEPHYR_BASE/tests/kernel/fatal/src/main.c:367
        Invalid value of foo, got 0xdeadbeef
[00:00:00.000,000] <err> os: r0/a1:  0x00000004  r1/a2:  0x0000016f  r2/a3:  0x00000000
[00:00:00.000,000] <err> os: r3/a4:  0x00000000 r12/ip:  0x00000000 r14/lr:  0x00000a6d
[00:00:00.000,000] <err> os:  xpsr:  0x61000000
[00:00:00.000,000] <err> os: Faulting instruction address (r15/pc): 0x00009fe4
[00:00:00.000,000] <err> os: >>> ZEPHYR FATAL ERROR 4: Kernel panic
[00:00:00.000,000] <err> os: Current thread: 0x20000414 (main)
[00:00:00.000,000] <err> os: Halting system
```

#### \_\_ASSERT\_EVAL()

The `__ASSERT_EVAL()` macro can also be used inside kernel and application
code, with special semantics for the evaluation of its arguments.

It makes use of the `__ASSERT()` macro, but has some extra flexibility. It
allows the developer to specify different actions depending whether the
`__ASSERT()` macro is enabled or not. This can be particularly useful to
prevent the compiler from generating comments (errors, warnings or remarks)
about variables that are only used with `__ASSERT()` being assigned a value,
but otherwise unused when the `__ASSERT()` macro is disabled.

Consider the following example:

```c
int x;
x = foo();
__ASSERT(x != 0, "foo() returned zero!");
```

If `__ASSERT()` is disabled, then ‘x’ is assigned a value, but never used.
This type of situation can be resolved using the \_\_ASSERT\_EVAL() macro.

```c
__ASSERT_EVAL ((void) foo(),
               int x = foo(),
               x != 0,
               "foo() returned zero!");
```

The first parameter tells `__ASSERT_EVAL()` what to do if `__ASSERT()` is
disabled. The second parameter tells `__ASSERT_EVAL()` what to do if
`__ASSERT()` is enabled. The third and fourth parameters are the parameters
it passes to `__ASSERT()`.

#### \_\_ASSERT\_NO\_MSG()

The `__ASSERT_NO_MSG()` macro can be used to perform an assertion that
reports the failed test and its location, but lacks additional debugging
information provided to assist the user in diagnosing the problem; its use is
discouraged.

### Build Assertions

Zephyr provides two macros for performing build-time assertion checks.
These are evaluated completely at compile-time, and are always checked.

#### BUILD\_ASSERT()

This has the same semantics as C’s `_Static_assert` or C++’s
`static_assert`. If the evaluation fails, a build error will be generated by
the compiler. If the compiler supports it, the provided message will be printed
to provide further context.

Unlike `__ASSERT()`, the message must be a static string, without
`printf()`-like format codes or extra arguments.

For example, suppose this check fails:

```c
BUILD_ASSERT(FOO == 2000, "Invalid value of FOO");
```

With GCC, the output resembles:

```text
tests/kernel/fatal/src/main.c: In function 'test_main':
include/toolchain/gcc.h:28:37: error: static assertion failed: "Invalid value of FOO"
 #define BUILD_ASSERT(EXPR, MSG) _Static_assert(EXPR, "" MSG)
                                 ^~~~~~~~~~~~~~
tests/kernel/fatal/src/main.c:370:2: note: in expansion of macro 'BUILD_ASSERT'
  BUILD_ASSERT(FOO == 2000,
  ^~~~~~~~~~~~~~~~
```

### Kernel Oops

A kernel oops is a software triggered fatal error invoked by
`k_oops()`. This should be used to indicate an unrecoverable condition
in application logic.

The fatal error reason code generated will be `K_ERR_KERNEL_OOPS`.

### Kernel Panic

A kernel error is a software triggered fatal error invoked by
`k_panic()`. This should be used to indicate that the Zephyr kernel is
in an unrecoverable state. Implementations of
[`k_sys_fatal_error_handler()`](#c.k_sys_fatal_error_handler) should not return if the kernel
encounters a panic condition, as the entire system needs to be reset.

Threads running in user mode are not permitted to invoke `k_panic()`,
and doing so will generate a kernel oops instead. Otherwise, the fatal error
reason code generated will be `K_ERR_KERNEL_PANIC`.

## Exceptions

### Spurious Interrupts

If the CPU receives a hardware interrupt on an interrupt line that has not had
a handler installed with `IRQ_CONNECT()` or [`irq_connect_dynamic()`](../interrupts.md#c.irq_connect_dynamic "irq_connect_dynamic"),
then the kernel will generate a fatal error with the reason code
`K_ERR_SPURIOUS_IRQ()`.

### Stack Overflows

In the event that a thread pushes more data onto its execution stack than its
stack buffer provides, the kernel may be able to detect this situation and
generate a fatal error with a reason code of `K_ERR_STACK_CHK_FAIL`.

If a thread is running in user mode, then stack overflows are always caught,
as the thread will simply not have permission to write to adjacent memory
addresses outside of the stack buffer. Because this is enforced by the
memory protection hardware, there is no risk of data corruption to memory
that the thread would not otherwise be able to write to.

If a thread is running in supervisor mode, or if [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is
not enabled, depending on configuration stack overflows may or may not be
caught. [`CONFIG_HW_STACK_PROTECTION`](../../../kconfig.md#CONFIG_HW_STACK_PROTECTION "CONFIG_HW_STACK_PROTECTION") is supported on some
architectures and will catch stack overflows in supervisor mode, including
when handling a system call on behalf of a user thread. Typically this is
implemented via dedicated CPU features, or read-only MMU/MPU guard regions
placed immediately adjacent to the stack buffer. Stack overflows caught in this
way can detect the overflow, but cannot guarantee against data corruption and
should be treated as a very serious condition impacting the health of the
entire system.

If a platform lacks memory management hardware support,
[`CONFIG_STACK_SENTINEL`](../../../kconfig.md#CONFIG_STACK_SENTINEL "CONFIG_STACK_SENTINEL") is a software-only stack overflow detection
feature which periodically checks if a sentinel value at the end of the stack
buffer has been corrupted. It does not require hardware support, but provides
no protection against data corruption. Since the checks are typically done at
interrupt exit, the overflow may be detected a nontrivial amount of time after
the stack actually overflowed.

Finally, Zephyr supports GCC compiler stack canaries via
[`CONFIG_STACK_CANARIES`](../../../kconfig.md#CONFIG_STACK_CANARIES "CONFIG_STACK_CANARIES"). If enabled, the compiler will insert a canary
value randomly generated at boot into function stack frames, checking that the
canary has not been overwritten at function exit. If the check fails, the
compiler invokes `__stack_chk_fail()`, whose Zephyr implementation
invokes a fatal stack overflow error. An error in this case does not indicate
that the entire stack buffer has overflowed, but instead that the current
function stack frame has been corrupted. See the compiler documentation for
more details.

### Other Exceptions

Any other type of unhandled CPU exception will generate an error code of
`K_ERR_CPU_EXCEPTION`.

## Fatal Error Handling

The policy for what to do when encountering a fatal error is determined by the
implementation of the [`k_sys_fatal_error_handler()`](#c.k_sys_fatal_error_handler) function. This
function has a default implementation with weak linkage that calls
`LOG_PANIC()` to dump all pending logging messages and then unconditionally
halts the system with [`k_fatal_halt()`](#c.k_fatal_halt).

Applications are free to implement their own error handling policy by
overriding the implementation of [`k_sys_fatal_error_handler()`](#c.k_sys_fatal_error_handler).
If the implementation returns, the faulting thread will be aborted and
the system will otherwise continue to function. See the documentation for
this function for additional details and constraints.

## API Reference

*group* fatal\_apis
:   Functions

    FUNC\_NORETURN void k\_fatal\_halt(unsigned int reason)
    :   Halt the system on a fatal error.

        Invokes architecture-specific code to power off or halt the system in a low power state. Lacking that, lock interrupts and sit in an idle loop.

        Parameters:
        :   - **reason** – Fatal exception reason code

    void k\_sys\_fatal\_error\_handler(unsigned int reason, const z\_arch\_esf\_t \*esf)
    :   Fatal error policy handler.

        This function is not invoked by application code, but is declared as a weak symbol so that applications may introduce their own policy.

        The default implementation of this function halts the system unconditionally. Depending on architecture support, this may be a simple infinite loop, power off the hardware, or exit an emulator.

        If this function returns, then the currently executing thread will be aborted.

        A few notes for custom implementations:

        - If the error is determined to be unrecoverable, [LOG\_PANIC()](../../../services/logging/index.md#group__log__ctrl_1ga9ee5a99e0487e3f1e6d289b12c19ad5a) should be invoked to flush any pending logging buffers.
        - K\_ERR\_KERNEL\_PANIC indicates a severe unrecoverable error in the kernel itself, and should not be considered recoverable. There is an assertion in z\_fatal\_error() to enforce this.
        - Even outside of a kernel panic, unless the fault occurred in user mode, the kernel itself may be in an inconsistent state, with API calls to kernel objects possibly exhibiting undefined behavior or triggering another exception.

        Parameters:
        :   - **reason** – The reason for the fatal error
            - **esf** – Exception context, with details and partial or full register state when the error occurred. May in some cases be NULL.
