---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/threads/nothread.html
original_path: kernel/services/threads/nothread.html
---

# Operation without Threads

Thread support is not necessary in some applications:

- Bootloaders
- Simple event-driven applications
- Examples intended to demonstrate core functionality

Thread support can be disabled by setting
[`CONFIG_MULTITHREADING`](../../../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING") to `n`. Since this configuration has
a significant impact on Zephyr’s functionality and testing of it has
been limited, there are conditions on what can be expected to work in
this configuration.

## What Can be Expected to Work

These core capabilities shall function correctly when
[`CONFIG_MULTITHREADING`](../../../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING") is disabled:

- The [build system](../../../develop/application/index.md#application)
- The ability to boot the application to `main()`
- [Interrupt management](../interrupts.md#interrupts-v2)
- The system clock including [`k_uptime_get()`](../../../doxygen/html/group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69)
- Timers, i.e. `k_timer()`
- Non-sleeping delays e.g. [`k_busy_wait()`](../../../doxygen/html/group__thread__apis.md#ga550b642e071480323e589866abb99c22).
- Sleeping [`k_cpu_idle()`](../../../doxygen/html/group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356).
- Pre `main()` drivers and subsystems initialization e.g. [`SYS_INIT`](../../../doxygen/html/group__sys__init.md#gaf507cc0613add8113c41896bd631254f).
- [Memory Management](../index.md#kernel-memory-management-api)
- Specifically identified drivers in certain subsystems, listed below.

The expectations above affect selection of other features; for example
[`CONFIG_SYS_CLOCK_EXISTS`](../../../kconfig.md#CONFIG_SYS_CLOCK_EXISTS "CONFIG_SYS_CLOCK_EXISTS") cannot be set to `n`.

## What Cannot be Expected to Work

Functionality that will not work with [`CONFIG_MULTITHREADING`](../../../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING")
includes majority of the kernel API:

- [Threads](index.md#threads-v2)
- [Scheduling](../scheduling/index.md#scheduling-v2)
- [Workqueue Threads](workqueue.md#workqueues-v2)
- [Polling API](../polling.md#polling-v2)
- [Semaphores](../synchronization/semaphores.md#semaphores-v2)
- [Mutexes](../synchronization/mutexes.md#mutexes-v2)
- [Condition Variables](../synchronization/condvar.md#condvar)
- [Data Passing](../index.md#kernel-data-passing-api)

## Subsystem Behavior Without Thread Support

The sections below list driver and functional subsystems that are
expected to work to some degree when [`CONFIG_MULTITHREADING`](../../../kconfig.md#CONFIG_MULTITHREADING "CONFIG_MULTITHREADING") is
disabled. Subsystems that are not listed here should not be expected to
work.

Some existing drivers within the listed subsystems do not work when
threading is disabled, but are within scope based on their subsystem, or
may be sufficiently isolated that supporting them on a particular
platform is low-impact. Enhancements to add support to existing
capabilities that were not originally implemented to work with threads
disabled will be considered.

### Flash

The [Flash](../../../hardware/peripherals/flash.md#flash-api) is expected to work for all SoC flash peripheral
drivers. Bus-accessed devices like serial memories may not be
supported.

*List/table of supported drivers to go here*

### GPIO

The [General-Purpose Input/Output (GPIO)](../../../hardware/peripherals/gpio.md#gpio-api) is expected to work for all SoC GPIO peripheral
drivers. Bus-accessed devices like GPIO extenders may not be supported.

*List/table of supported drivers to go here*

### UART

A subset of the [Universal Asynchronous Receiver-Transmitter (UART)](../../../hardware/peripherals/uart.md#uart-api) is expected to work for all SoC UART
peripheral drivers.

- Applications that select [`CONFIG_UART_INTERRUPT_DRIVEN`](../../../kconfig.md#CONFIG_UART_INTERRUPT_DRIVEN "CONFIG_UART_INTERRUPT_DRIVEN") may
  work, depending on driver implementation.
- Applications that select [`CONFIG_UART_ASYNC_API`](../../../kconfig.md#CONFIG_UART_ASYNC_API "CONFIG_UART_ASYNC_API") may
  work, depending on driver implementation.
- Applications that do not select either [`CONFIG_UART_ASYNC_API`](../../../kconfig.md#CONFIG_UART_ASYNC_API "CONFIG_UART_ASYNC_API")
  or [`CONFIG_UART_INTERRUPT_DRIVEN`](../../../kconfig.md#CONFIG_UART_INTERRUPT_DRIVEN "CONFIG_UART_INTERRUPT_DRIVEN") are expected to work.

*List/table of supported drivers to go here, including which API options
are supported*
