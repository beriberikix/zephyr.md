---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/qemu_eth_setup.html
original_path: connectivity/networking/qemu_eth_setup.html
---

# Networking with QEMU Ethernet

This page describes how to set up a virtual network between a (Linux) host
and a Zephyr application running in QEMU.

In this example, the [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") sample application from
the Zephyr source distribution is run in QEMU. The Zephyr instance is
connected to a Linux host using a tuntap device which is modeled in Linux as
an Ethernet network interface.

## [Prerequisites](#id1)

On the Linux Host, find the Zephyr [net-tools](https://github.com/zephyrproject-rtos/net-tools) project, which can either be
found in a Zephyr standard installation under the `tools/net-tools` directory
or installed stand alone from its own git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

## [Basic Setup](#id2)

For the steps below, you will need two terminal windows:

- Terminal #1 is terminal window with net-tools being the current
  directory (`cd net-tools`)
- Terminal #2 is your usual Zephyr development terminal,
  with the Zephyr environment initialized.

When configuring the Zephyr instance, you must select the correct Ethernet
driver for QEMU connectivity:

- For `qemu_x86`, select `Intel(R) PRO/1000 Gigabit Ethernet driver`
  Ethernet driver. Driver is called `e1000` in Zephyr source tree.
- For `qemu_cortex_m3`, select `TI Stellaris MCU family ethernet driver`
  Ethernet driver. Driver is called `stellaris` in Zephyr source tree.
- For `mps2_an385`, select `SMSC911x/9220 Ethernet driver` Ethernet driver.
  Driver is called `smsc911x` in Zephyr source tree.
- For `qemu_cortex_a53`, `Intel(R) PRO/1000 Gigabit Ethernet driver`
  Ethernet driver is selected by default.

### [Step 1 - Create Ethernet interface](#id3)

Before starting QEMU with network connectivity, a network interface
should be created in the host system.

In terminal #1, type:

```shell
./net-setup.sh
```

You can tweak the behavior of the `net-setup.sh` script. See various options
by running `net-setup.sh` like this:

```shell
./net-setup.sh --help
```

### [Step 2 - Start app in QEMU board](#id4)

Build and start the [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") sample application.
In this example, the qemu\_x86 board is used.

In terminal #2, type:

```shell
west build -b qemu_x86 samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-e1000.conf
west build -t run
```

Exit QEMU by pressing `CTRL+A` `x`.
