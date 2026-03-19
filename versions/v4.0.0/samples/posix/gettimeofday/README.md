---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/posix/gettimeofday/README.html
original_path: samples/posix/gettimeofday/README.html
---

# gettimeofday() with clock initialization

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/posix/gettimeofday/README.rst/..)

## Overview

This sample application demonstrates using the POSIX [gettimeofday()](https://pubs.opengroup.org/onlinepubs/009604599/functions/gettimeofday.html) function to display the
absolute wall clock time and local time every second. At system startup, the current time is
queried using the SNTP networking protocol, enabled by setting the
[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](../../../kconfig.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT "CONFIG_NET_CONFIG_CLOCK_SNTP_INIT") and
[`CONFIG_NET_CONFIG_SNTP_INIT_SERVER`](../../../kconfig.md#CONFIG_NET_CONFIG_SNTP_INIT_SERVER "CONFIG_NET_CONFIG_SNTP_INIT_SERVER") options.

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)
- or, a board with hardware networking
- NAT/routing should be set up to allow connections to the Internet
- DNS server should be available on the host to resolve domain names

## Building and Running

This project outputs to the console. It can be built and executed on QEMU as follows:

```shell
west build -b qemu_x86 samples/posix/gettimeofday
west build -t run
```

For comparison, to build directly for your host OS if it is POSIX compliant (for ex. Linux):

```shell
cd samples/posix/gettimeofday
make -f Makefile.host
```

The make output file will be located in samples/posix/gettimeofday/build.
