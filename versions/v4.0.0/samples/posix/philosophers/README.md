---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/posix/philosophers/README.html
original_path: samples/posix/philosophers/README.html
---

# POSIX Philosophers

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/posix/philosophers/README.rst/..)

## Overview

This sample implements Zephyr’s [Dining Philosophers](../../philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.") sample using the
[POSIX API](../../../services/portability/posix/index.md#posix-support). The source code for this sample can be found under
`samples/posix/philosophers`.

## Building and Running

This project outputs to the console. It can be built and executed on QEMU as follows:

```shell
west build -b qemu_riscv64 samples/posix/philosophers
west build -t run
```

### Sample Output

```shell
Philosopher 0 [P: 3]  HOLDING ONE FORK
Philosopher 1 [P: 2]  HOLDING ONE FORK
Philosopher 2 [P: 1]  EATING  [ 1900 ms ]
Philosopher 3 [P: 0]  THINKING [ 2500 ms ]
Philosopher 4 [C:-1]  THINKING [ 2200 ms ]
Philosopher 5 [C:-2]  THINKING [ 1700 ms ]
```

Exit QEMU by pressing `CTRL`+`A` `x`.

## Debugging

Like the original philosophers sample, the POSIX variant also enables
[`CONFIG_DEBUG_THREAD_INFO`](../../../kconfig.md#CONFIG_DEBUG_THREAD_INFO "CONFIG_DEBUG_THREAD_INFO") by default.

```shell
west build -b <board_name> samples/philosophers
west debug
```

## Additional Information

For additional information, please refer to the [Dining Philosophers](../../philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.") sample.
