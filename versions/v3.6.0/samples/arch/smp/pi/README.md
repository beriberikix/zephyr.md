---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/arch/smp/pi/README.html
original_path: samples/arch/smp/pi/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SMP Pi

## Overview

This sample application calculates Pi independently in many threads, and
demonstrates the benefit of multiple execution units (CPU cores)
when compute-intensive tasks can be run in parallel, with
no cross-dependencies or shared resources.

By changing the value of CONFIG\_MP\_MAX\_NUM\_CPUS on SMP systems, you
can see that using more cores takes almost linearly less time
to complete the computational task.

You can also edit the sample source code to change the
number of digits calculated (`DIGITS_NUM`), and the
number of threads to use (`THREADS_NUM`).

## Building and Running

This project outputs Pi values calculated by each thread and in the end total time
required for all the calculation to be done. It can be built and executed
on Synopsys ARC HSDK board as follows:

```shell
west build -b qemu_x86_64 samples/arch/smp/pi
west build -t run
```

### Sample Output

```shell
Calculate first 240 digits of Pi independently by 16 threads.
Pi value calculated by thread #0: 3141592653589793238462643383279502884197...
Pi value calculated by thread #1: 3141592653589793238462643383279502884197...
...
Pi value calculated by thread #14: 314159265358979323846264338327950288419...
Pi value calculated by thread #15: 314159265358979323846264338327950288419...
All 16 threads executed by 4 cores in 28 msec
```
