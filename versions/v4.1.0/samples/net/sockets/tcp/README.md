---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/tcp/README.html
original_path: samples/net/sockets/tcp/README.html
---

# TCP sample for TTCN-3 based sanity check

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/tcp/README.rst/..)

## Overview

This application is used together with the TTCN-3 based sanity check
to validate the functionality of the TCP.

## Building, Running and executing TTCN-3 based Sanity Check for TCP

Compile and start the [net-test-tools](https://github.com/intel/net-test-tools):

```shell
./autogen.sh
make
./loop-slipcat.sh
```

Build the TCP sample app:

```shell
cd samples/net/sockets/tcp
mkdir build && cd build
cmake -DBOARD=qemu_x86 -DEXTRA_CONF_FILE="overlay-slip.conf" ..
make run
```

Compile and run the TCP sanity check [net-test-suites](https://github.com/intel/net-test-suites):

```shell
. titan-install.sh
. titan-env.sh
cd src
. make.sh
ttcn3_start test_suite tcp2_check_3_runs.cfg
```

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)
