---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/posix/env/README.html
original_path: samples/posix/env/README.html
---

# Environment Variables

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/posix/env/README.rst/..)

## Overview

In this sample application, the POSIX `setenv()`, function is used to populate several environment
variables in C. Then, all environment variables are then printed.

If the user sets a new value for the `ALERT` environment variable, it is printed to standard
output, and then cleared via `unsetenv()`.

## Building and Running

This project outputs to the console. It can be built and executed on QEMU as follows:

```shell
west build -b qemu_riscv32 samples/posix/env
west build -t run
```

### Sample Output

The program below shows sample output for a specific Zephyr build.

```shell
BOARD=qemu_riscv32
BUILD_VERSION=zephyr-v3.5.0-5372-g3a46f2d052c7
ALERT=
```

### Setting Environment Variables

The shell command below shows how to create a new environment variable or update the value
associated with an existing environment variable.

The C code that is part of this sample application displays the value associated with the
`ALERT` environment variable and then immediately unsets it.

```shell
uart:~$ posix env set ALERT="Happy Friday!"
uart:~$ ALERT="Happy Friday!"
uart:~$ posix env set HOME="127.0.0.1"
uart:~$
```

### Getting Environment Variables

The shell command below may be used to display the value associated with one environment variable.

```shell
uart:~$ posix env get BOARD
qemu_riscv32
```

The shell command below may be used to display all environment variables and their associated
values.

```shell
uart:~$ posix env get
BOARD=qemu_riscv32
BUILD_VERSION=zephyr-v3.5.0-5372-g3a46f2d052c7
ALERT=
```

### Unsetting Environment Variables

The shell command below may be used to unset environment variables.

```shell
uart:~$ posix env unset BOARD
```
