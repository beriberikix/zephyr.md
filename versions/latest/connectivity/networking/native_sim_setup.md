---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/native_sim_setup.html
original_path: connectivity/networking/native_sim_setup.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Networking with native\_sim board

This page describes how to set up a virtual network between a (Linux) host
and a Zephyr application running in a [native\_sim](../../boards/posix/native_sim/doc/index.md#native-sim) board.

In this example, the [Echo server (advanced)](../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") sample application from
the Zephyr source distribution is run in native\_sim board. The Zephyr
native\_sim board instance is connected to a Linux host using a tuntap device
which is modeled in Linux as an Ethernet network interface.

## [Prerequisites](#id1)

On the Linux Host, fetch the Zephyr `net-tools` project, which is located
in a separate Git repository:

```shell
git clone https://github.com/zephyrproject-rtos/net-tools
```

## [Basic Setup](#id2)

For the steps below, you will need three terminal windows:

- Terminal #1 is terminal window with net-tools being the current
  directory (`cd net-tools`)
- Terminal #2 is your usual Zephyr development terminal,
  with the Zephyr environment initialized.
- Terminal #3 is the console to the running Zephyr native\_sim
  instance (optional).

### [Step 1 - Create Ethernet interface](#id3)

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

### [Step 2 - Start app in native\_sim board](#id4)

Build and start the `echo_server` sample application.

In terminal #2, type:

```shell
west build -b native_sim samples/net/sockets/echo_server
west build -t run
```

### [Step 3 - Connect to console (optional)](#id5)

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
