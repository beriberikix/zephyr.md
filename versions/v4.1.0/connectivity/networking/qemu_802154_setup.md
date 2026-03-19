---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/qemu_802154_setup.html
original_path: connectivity/networking/qemu_802154_setup.html
---

# Networking with QEMU and IEEE 802.15.4

This page describes how to set up a virtual network between two QEMUs that
are connected together via UART and are running IEEE 802.15.4 link layer
between them. Note that this only works in Linux host.

## [Basic Setup](#id1)

For the steps below, you will need two terminal windows:

- Terminal #1 is terminal window with `echo-server` Zephyr sample application.
- Terminal #2 is terminal window with `echo-client` Zephyr sample application.

If you want to capture the transferred network data, you must compile the
`monitor_15_4` program in the `tools/net-tools` directory.

Open a terminal window and type:

```shell
cd $ZEPHYR_BASE/../tools/net-tools
make monitor_15_4
```

### [Step 1 - Compile and start echo-server](#id2)

In terminal #1, type:

```shell
west build -b qemu_x86 -d build/server samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-qemu_802154.conf
west build -t server -d build/server
```

If you want to capture the network traffic between the two QEMUs, type:

```shell
west build -b qemu_x86 -d build/server samples/net/sockets/echo_server -- -G'Unix Makefiles' -DEXTRA_CONF_FILE=overlay-qemu_802154.conf -DPCAP=capture.pcap
west build -t server -d build/server
```

Note that the `make` must be used for `server` target if packet capture
option is set in command line. The `build/server/capture.pcap` file will contain the
transferred data.

### [Step 2 - Compile and start echo-client](#id3)

In terminal #2, type:

```shell
west build -b qemu_x86 -d build/client samples/net/sockets/echo_client -- -DEXTRA_CONF_FILE=overlay-qemu_802154.conf
west build -t client -d build/client
```

You should see data passed between the two QEMUs.
Exit QEMU by pressing `CTRL+A` `x`.
