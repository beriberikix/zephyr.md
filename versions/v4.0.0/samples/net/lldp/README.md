---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/lldp/README.html
original_path: samples/net/lldp/README.html
---

# Link Layer Discovery Protocol (LLDP)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/lldp/README.rst/..)

## Overview

The Link Layer Discovery Protocol sample application for Zephyr will enable
LLDP support and setup VLANs if needed.

The source code for this sample application can be found at:
[samples/net/lldp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lldp).

## Requirements

- [Networking with the host system](../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

A good way to run this sample LLDP application is inside QEMU,
as described in [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) or with embedded device like
FRDM-K64F. Note that LLDP is only supported for boards that have an ethernet
port.

Follow these steps to build the LLDP sample application:

```shell
west build -b <board to use> samples/net/lldp -- -DCONF_FILE=prj.conf
```

### Setting up Linux Host

If you need VLAN support in your network, then the
[samples/net/vlan/vlan-setup-linux.sh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/vlan/vlan-setup-linux.sh) provides a script that can be
executed on the Linux host. It creates two VLANs on the Linux host and creates
routes to Zephyr.

## See also

[Link Layer Discovery Protocol definitions and helpers](../../../doxygen/html/group__lldp.md)

[Network L2 Abstraction Layer](../../../doxygen/html/group__net__l2.md)
