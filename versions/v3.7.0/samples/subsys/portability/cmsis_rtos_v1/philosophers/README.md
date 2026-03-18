---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/portability/cmsis_rtos_v1/philosophers/README.html
original_path: samples/subsys/portability/cmsis_rtos_v1/philosophers/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Dining Philosophers (CMSIS RTOS V1 APIs)

## Overview

This sample implements a solution to the [Dining Philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem) (a classic
multi-thread synchronization problem) using CMSIS RTOS V1 APIs. This particular
implementation demonstrates the usage of multiple preemptible and cooperative
threads of differing priorities, as well as mutex/semaphore and thread sleeping
which uses CMSIS RTOS V1 API implementation in Zephyr.

The philosopher always tries to get the lowest fork first (f1 then f2). When
done, he will give back the forks in the reverse order (f2 then f1). If he
gets two forks, he is EATING. Otherwise, he is THINKING. Transitional states
are shown as well, such as STARVING when the philosopher is hungry but the
forks are not available, and HOLDING ONE FORK when a philosopher is waiting
for the second fork to be available.

Each Philosopher will randomly alternate between the EATING and THINKING state.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
west build -b qemu_x86 samples/philosophers
west build -t run
```

### Sample Output

```shell
Philosopher 0 [C:-2]  THINKING [  500 ms ]
Philosopher 1 [C:-1]  THINKING [  375 ms ]
Philosopher 2 [P: 0]  THINKING [  575 ms ]
Philosopher 3 [P: 1]   EATING  [  525 ms ]
Philosopher 4 [P: 2]  THINKING [  800 ms ]
Philosopher 5 [P: 3]   EATING  [  625 ms ]

Demo Description
----------------
An implementation of a solution to the Dining Philosophers
problem (a classic multi-thread synchronization problem) using
CMSIS RTOS V1 APIs. This particular implementation demonstrates the
usage of multiple preemptible threads of differing
priorities, as well as semaphores and thread sleeping.
```

Exit QEMU by pressing `CTRL+A` `x`.
