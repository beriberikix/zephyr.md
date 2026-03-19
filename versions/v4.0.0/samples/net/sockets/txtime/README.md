---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/txtime/README.html
original_path: samples/net/sockets/txtime/README.html
---

# UDP sender using SO\_TXTIME

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/txtime/README.rst/..)

## Overview

This sample is a simple UDP sender/receiver which will set the
SO\_TXTIME socket option and expects the Ethernet driver to send
the data when the TX time is expected. The application requires
that the board has PTP clock support. A simulated PTP clock is
provided for qemu\_x86 board. Also frdm\_k64f and sam\_e70\_xplained/same70q21 boards
are supported. Other mcux or gmac Ethernet driver based boards should
work too.
User can control how long the application should wait between packets sent by
setting `CONFIG_NET_SAMPLE_PACKET_INTERVAL` option.
Also the TXTIME value can be specified in the config file by setting the
`CONFIG_NET_SAMPLE_PACKET_TXTIME` option. In this case the value is
used as an offset from the current time.

## Building and Running

When the application is run, it starts to send UDP packets. You can start
`echo-server` application from [net-tools](https://github.com/zephyrproject-rtos/net-tools) project to catch these and
send the data back to this application. Optionally you can set
`CONFIG_NET_SAMPLE_PACKET_SOCKET` option, which makes the application
to create an `AF_PACKET` type socket. In this case, the `echo-server`
application cannot be used as a peer.

This sample can be built and executed on qemu\_x86 board as
described in [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host).

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[Ethernet Support Functions](../../../../doxygen/html/group__ethernet.md)
