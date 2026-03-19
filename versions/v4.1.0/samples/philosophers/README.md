---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/philosophers/README.html
original_path: samples/philosophers/README.html
---

# Dining Philosophers

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/philosophers/README.rst/..)

## Overview

An implementation of a solution to the Dining Philosophers problem (a classic multi-thread
synchronization problem). This particular implementation demonstrates the usage of multiple
preemptible and cooperative threads of differing priorities, as well as dynamic mutexes and thread
sleeping.

The philosopher always tries to get the lowest fork first (f1 then f2). When done, he will give
back the forks in the reverse order (f2 then f1). If he gets two forks, he is `EATING`.
Otherwise, he is `THINKING`. Transitional states are shown as well, such as `STARVING` when the
philosopher is hungry but the forks are not available, and `HOLDING ONE FORK` when a philosopher
is waiting for the second fork to be available.

Each Philosopher will randomly alternate between the `EATING` and `THINKING` states.

It is possible to run the demo in `coop-only` or `preempt-only` mode. To achieve this, set these
values for `CONFIG_NUM_COOP_PRIORITIES` and `CONFIG_NUM_PREEMPT_PRIORITIES` in `prj.conf`:

preempt-only
:   ```cfg
    CONFIG_NUM_PREEMPT_PRIORITIES=6
    CONFIG_NUM_COOP_PRIORITIES=0
    ```

coop-only
:   ```cfg
    CONFIG_NUM_PREEMPT_PRIORITIES=0
    CONFIG_NUM_COOP_PRIORITIES=6
    ```

In these cases, the philosopher threads will run with priorities 0 to 5 (preempt-only) and -7 to -2
(coop-only).

## Building and Running

This project outputs to the console. It can be built and executed on QEMU as follows:

```shell
west build -b qemu_x86 samples/philosophers
west build -t run
```

### Sample Output

```text
Philosopher 0 [P: 3]  HOLDING ONE FORK
Philosopher 1 [P: 2]  HOLDING ONE FORK
Philosopher 2 [P: 1]  EATING  [ 1900 ms ]
Philosopher 3 [P: 0]  THINKING [ 2500 ms ]
Philosopher 4 [C:-1]  THINKING [ 2200 ms ]
Philosopher 5 [C:-2]  THINKING [ 1700 ms ]
```

Exit QEMU by pressing `CTRL+A` `x`.

## Debug Threads

The philosophers sample by default enables [`CONFIG_DEBUG_THREAD_INFO`](../../kconfig.md#CONFIG_DEBUG_THREAD_INFO "CONFIG_DEBUG_THREAD_INFO"). This allows
tools like OpenOCD and J-link to inspect thread data using `info threads`.

```shell
west build -b <board_name> samples/philosophers
west debug
```

### OpenOCD Sample Output

```text
Thread 1 received signal SIGINT, Interrupt.
[Switching to Thread 537003160]
arch_cpu_idle () at zephyr/mainline/zephyr/arch/arm/core/cpu_idle.S:107
107          cpsie   i
(gdb) i threads
  Id   Target Id                                                  Frame
* 1    Thread 537003160 (Name: idle 00, prio:40,useropts:1)       arch_cpu_idle () at zephyr/mainline/zephyr/arch/arm/core/cpu_idle.S:107
Info : Getting thread 537002984 reg list
  2    Thread 537002984 (Name: Philosopher 5, prio:-2,useropts:4) 0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
Info : Getting thread 537002808 reg list
  3    Thread 537002808 (Name: Philosopher 4, prio:-1,useropts:4) 0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
Info : Getting thread 537002632 reg list
  4    Thread 537002632 (Name: Philosopher 3, prio:0,useropts:4)  0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
Info : Getting thread 537002456 reg list
  5    Thread 537002456 (Name: Philosopher 2, prio:1,useropts:4)  0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
Info : Getting thread 537002280 reg list
  6    Thread 537002280 (Name: Philosopher 1, prio:2,useropts:4)  0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
Info : Getting thread 537002104 reg list
  7    Thread 537002104 (Name: Philosopher 0, prio:3,useropts:4)  0x08001404 in arch_irq_unlock (key=0) at zephyr/mainline/zephyr/include/arch/arm/asm_inline_gcc.h:95
```

```text
Philosopher 0 [P: 3]        STARVING
Philosopher 1 [P: 2]    HOLDING ONE FORK
Philosopher 2 [P: 1]   EATING  [  400 ms ]
Philosopher 3 [P: 0]  THINKING [  525 ms ]
Philosopher 4 [C:-1]    HOLDING ONE FORK
Philosopher 5 [C:-2]   EATING  [  625 ms ]
```

### J-Link Sample Output

```text
Thread 2 received signal SIGTRAP, Trace/breakpoint trap.
[Switching to Thread 537920592]
arch_cpu_idle () at zephyr/mainline/zephyr/arch/arm/core/cpu_idle.S:107
107          cpsie   i
(gdb) i threads
  Id   Target Id                                           Frame
* 2    Thread 537920592 (idle 00 UNKNOWN PRIO 40)          arch_cpu_idle () at zephyr/mainline/zephyr/arch/arm/core/cpu_idle.S:107
  3    Thread 537919536 (Philosopher 0 PENDING PRIO 3)     arch_swap (key=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
  4    Thread 537919712 (Philosopher 1 SUSPENDED PRIO 2)   arch_swap (key=key@entry=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
  5    Thread 537919888 (Philosopher 2 SUSPENDED PRIO 1)   arch_swap (key=key@entry=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
  6    Thread 537920064 (Philosopher 3 SUSPENDED PRIO 0)   arch_swap (key=key@entry=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
  7    Thread 537920240 (Philosopher 4 PENDING PRIO 255)   arch_swap (key=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
  8    Thread 537920416 (Philosopher 5 SUSPENDED PRIO 254) arch_swap (key=key@entry=0) at zephyr/mainline/zephyr/arch/arm/core/swap.c:53
```

```text
Philosopher 0 [P: 3]        STARVING
Philosopher 1 [P: 2]   EATING  [  475 ms ]
Philosopher 2 [P: 1]  THINKING [  700 ms ]
Philosopher 3 [P: 0]  THINKING [  525 ms ]
Philosopher 4 [C:-1]    HOLDING ONE FORK
Philosopher 5 [C:-2]   EATING  [  625 ms ]
```

## See also

[Semaphore APIs](../../doxygen/html/group__semaphore__apis.md)

[Mutex APIs](../../doxygen/html/group__mutex__apis.md)

[Stack APIs](../../doxygen/html/group__stack__apis.md)

[Thread APIs](../../doxygen/html/group__thread__apis.md)

[FIFO APIs](../../doxygen/html/group__fifo__apis.md)

[LIFO APIs](../../doxygen/html/group__lifo__apis.md)
