---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/posix/eventfd/README.html
original_path: samples/posix/eventfd/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# POSIX eventfd()

## Overview

This sample application demonstrates using the POSIX eventfd() function to create a file descriptor,
which can be used for event notification. The returned file descriptor is used with write/read calls
and write/read values are output to the console.

## Building and Running

This project outputs to the console. It can be built and executed on QEMU as follows:

```shell
west build -b qemu_x86 samples/posix/eventfd
west build -t run
```

For comparison, to build directly for your host OS if it is POSIX compliant (for ex. Linux):

```shell
cd samples/posix/eventfd
make -f Makefile.host
```

The make output file will be located in samples/posix/eventfd/build.

### Sample Output

```shell
Writing 1 to efd
Writing 2 to efd
Writing 3 to efd
Writing 4 to efd
Completed write loop
About to read
Read 10 (0xa) from efd
Finished
```
