---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/sntp_client/README.html
original_path: samples/net/sockets/sntp_client/README.html
---

# SNTP client

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/sntp_client/README.rst/..)

## Overview

This sample is a simple SNTP client showing how to retrieve the current
time in seconds since 1st January 1970.

This demo assumes that the platform of choice has networking support,
some adjustments to the configuration may be needed. It also assumes
SNTP server is running on the host.

## Building and Running

When the application runs, it issues an SNTP request to the host and waits
for a response. When the response is received, the current epoch time, in
seconds, as well as the status code of the response (0 on success), is
printed.

See the [net-tools](https://github.com/zephyrproject-rtos/net-tools) project for more details.

This sample can be built and executed on QEMU or native\_sim board as
described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

### Wi-Fi

The IPv4 Wi-Fi support can be enabled in the sample with
[Wi-Fi snippet](../../../../snippets/wifi-ipv4/README.md#snippet-wifi-ipv4).

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[SNTP](../../../../doxygen/html/group__sntp.md)
