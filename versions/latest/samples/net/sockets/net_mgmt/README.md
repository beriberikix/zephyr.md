---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/net/sockets/net_mgmt/README.html
original_path: samples/net/sockets/net_mgmt/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Network management socket

## Overview

The net-mgmt-socket sample application for Zephyr implements a listener
for network management events that the networking subsystem is sending.

The source code for this sample application can be found at:
[samples/net/sockets/net\_mgmt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/net_mgmt).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

There are multiple ways to use this application. One of the most common
usage scenario is to run echo-server application inside QEMU. This is
described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

Build net-mgmt socket sample application like this:

```shell
west build -b <board to use> samples/net/sockets/net_mgmt -- -DCONF_FILE=<config file to use>
```

Example building for the native\_sim board:

```shell
west build -b native_sim samples/net/sockets/net_mgmt -- -DCONF_FILE=prj.conf
west build -t run
```
