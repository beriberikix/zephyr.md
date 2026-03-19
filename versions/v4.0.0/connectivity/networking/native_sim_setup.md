---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/native_sim_setup.html
original_path: connectivity/networking/native_sim_setup.html
---

# Networking with native\_sim board

## [Using virtual/TAP Ethernet driver](#id1)

This paragraph describes how to set up a virtual network between a (Linux) host
and a Zephyr application running in a [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) board.

In this example, the [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") sample application from
the Zephyr source distribution is run in native\_sim board. The Zephyr
native\_sim board instance is connected to a Linux host using a tuntap device
which is modeled in Linux as an Ethernet network interface.

### [Prerequisites](#id2)

On the Linux Host, find the Zephyr [net-tools](https://github.com/zephyrproject-rtos/net-tools) project, which can either be
found in a Zephyr standard installation under the `tools/net-tools` directory
or installed stand alone from its own git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

### [Basic Setup](#id3)

For the steps below, you will need three terminal windows:

- Terminal #1 is terminal window with net-tools being the current
  directory (`cd net-tools`)
- Terminal #2 is your usual Zephyr development terminal,
  with the Zephyr environment initialized.
- Terminal #3 is the console to the running Zephyr native\_sim
  instance (optional).

#### Step 1 - Create Ethernet interface

Before starting native\_sim with network emulation, a network interface
should be created.

In terminal #1, type:

```shell
./net-setup.sh
```

You can tweak the behavior of the net-setup.sh script. See various options
by running `net-setup.sh` like this:

```shell
./net-setup.sh --help
```

#### Step 2 - Start app in native\_sim board

Build and start the `echo_server` sample application.

In terminal #2, type:

```shell
west build -b native_sim samples/net/sockets/echo_server
west build -t run
```

#### Step 3 - Connect to console (optional)

The console window should be launched automatically when the Zephyr instance is
started but if it does not show up, you can manually connect to the console.
The native\_sim board will print a string like this when it starts:

```shell
UART connected to pseudotty: /dev/pts/5
```

You can manually connect to it like this:

```shell
screen /dev/pts/5
```

## [Using offloaded sockets](#id4)

The main advantage over [Using virtual/TAP Ethernet driver](#using-virtual-tap-ethernet-driver) is not needing to
setup a virtual network interface on the host machine. This means that no
leveraged (root) privileges are needed.

### [Step 1 - Start app in native\_sim board](#id5)

Build and start the `echo_server` sample application:

```shell
west build -b native_sim samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-nsos.conf
west build -t run
```

### [Step 2 - run echo-client from net-tools](#id6)

On the Linux Host, find the Zephyr [net-tools](https://github.com/zephyrproject-rtos/net-tools) project, which can either be
found in a Zephyr standard installation under the `tools/net-tools` directory
or installed stand alone from its own git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

Note

Native Simulator with the offloaded sockets network driver is using the same
network interface/namespace as any other (Linux) application that uses BSD
sockets API. This means that [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and
`echo-client` applications will communicate over localhost/loopback
interface (address `127.0.0.1`).

To run UDP test, type:

```shell
./echo-client 127.0.0.1
```

For TCP test, type:

```shell
./echo-client -t 127.0.0.1
```

## [Setting interface name from command line](#id7)

By default the Ethernet interface name used by native\_sim is determined by
[`CONFIG_ETH_NATIVE_POSIX_DRV_NAME`](../../kconfig.md#CONFIG_ETH_NATIVE_POSIX_DRV_NAME "CONFIG_ETH_NATIVE_POSIX_DRV_NAME"), but is also possible
to set it from the command line using `--eth-if=<interface_name>`.
This can be useful if the application has to be
run in multiple instances and recompiling it for each instance would be
troublesome.

```shell
./zephyr.exe --eth-if=zeth2
```
