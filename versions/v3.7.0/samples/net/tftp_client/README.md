---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/net/tftp_client/README.html
original_path: samples/net/tftp_client/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# TFTP client

## Overview

Trivial File Transfer Protocol (TFTP) is a simple lockstep File Transfer Protocol
based on UDP, and is designed to get a file from or put a file onto a remote host.

This TFTP client sample application for Zephyr implements the TFTP client library
and establishes a connection to a TFTP server on standard port 69.

The source code for this sample application can be found at:
[samples/net/tftp\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client).

## Requirements

- [Networking with QEMU Ethernet](../../../connectivity/networking/qemu_eth_setup.md#networking-with-eth-qemu), [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) or [Networking with native\_sim board](../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim)
- Linux machine

## Building and Running

There are configuration files for various setups in the
samples/net/tftp\_client directory:

- `prj.conf`
  This is the standard default config.

Build the tftp-client sample application like this:

```shell
west build -b <board to use> samples/net/tftp_client -- -DCONF_FILE=<config file to use>
```

The easiest way to setup this sample application is to build and run it
as a native\_sim application or as a QEMU target using the default configuration `prj.conf`.
This requires a small amount of setup described in [Networking with QEMU Ethernet](../../../connectivity/networking/qemu_eth_setup.md#networking-with-eth-qemu), [Networking with QEMU](../../../connectivity/networking/qemu_setup.md#networking-with-qemu) and [Networking with native\_sim board](../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim).

Build the tftp-client sample application for [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) like this:

```shell
west build -b native_sim samples/net/tftp_client
west build -t run
```

Download and run a TFTP server (like TFTPd), then create file1.bin (with data) and newfile.bin.

Please note that default IP server address is 192.0.2.2 and default port is 69.
To specify an IP server address and/or port, change these configurations in `prj.conf`:

```cfg
CONFIG_TFTP_APP_SERVER="10.0.0.10"
CONFIG_TFTP_APP_PORT="70"
```

To connect to server using hostname, enable DNS resolver by changing these two
configurations in `prj.conf`:

```cfg
CONFIG_DNS_RESOLVER=y
CONFIG_TFTP_APP_SERVER="my-tftp-server.org"
```

### Sample output

This sample can be run on [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) while running a TFTP server on the host
machine.

Launch **net-setup.sh** in net-tools:

```shell
net-setup.sh
```

```shell
<inf> net_config: Initializing network
<inf> net_config: IPv4 address: 192.0.2.1
<inf> net_tftp_client_app: Run TFTP client
<inf> net_tftp_client_app: Received data:
        74 65 73 74 74 66 74 70  66 6f 72 7a 65 70 68 79 |testtftp forzephy
        72 0a                                            |r.
<inf> net_tftp_client_app: TFTP client get done
<inf> net_tftp_client_app: TFTP client put done
```
