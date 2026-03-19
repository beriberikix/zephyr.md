---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/sockets/coap_download/README.html
original_path: samples/net/sockets/coap_download/README.html
---

# CoAP download

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_download/README.rst/..)

## Overview

This sample demonstrates the use of the CoAP client API to make GET requests to
a CoAP server. If the data to be fetched is larger than a single CoAP packet,
a blockwise transfer will be used to receive the data.

Once the transfer is complete, the sample prints the amount of data received
and the time taken.

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host), [Networking with native\_sim board](../../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim)
- or, a board with hardware networking (tested on nucleo\_h753zi)
- Network connection between the board and host running a CoAP server

## Build and Running

Build the CoAP download sample application like this:

```shell
west build -b <board to use> samples/net/sockets/coap_download -- -DCONF_FILE=<config file to use>
```

The easiest way to run this sample application is to build and run it as a
native\_sim application. Some setup is required as described in
[Networking with native\_sim board](../../../../connectivity/networking/native_sim_setup.md#networking-with-native-sim).

Download a CoAP server application, for example [aiocoap](https://github.com/chrysn/aiocoap) (Python), or
[Eclipse Californium](https://github.com/eclipse-californium/californium) (Java) has a demo [Simple File Server](https://github.com/eclipse-californium/californium/tree/main/demo-apps/cf-simplefile-server) application.

Using `aiocoap`:

```shell
python -m pip install "aiocoap[all]"
mkdir file_root
echo "some test data" > file_root/test.txt
aiocoap-fileserver file_root
```

You can also change the name of the CoAP resource to request via Kconfig:

```cfg
CONFIG_NET_SAMPLE_COAP_RESOURCE_PATH="resource_name_to_request"
```

Launch **net-setup.sh** in net-tools:

```shell
./net-setup.sh
```

Build and run the coap\_download sample application for native\_sim like this:

```shell
west build -b native_sim samples/net/sockets/coap_download
west build -t run
```

### Sample output

```shell
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> coap_download: Network L4 is connected
[00:00:00.110,000] <inf> coap_download: Starting CoAP download using IPv4
[00:00:00.180,000] <inf> coap_download: CoAP response, result_code=69, offset=0, len=100
[00:00:00.180,000] <inf> coap_download: CoAP download done, got 100 bytes in 70 ms
[00:00:00.180,000] <inf> coap_download: Starting CoAP download using IPv6
[00:00:00.300,000] <inf> coap_download: CoAP response, result_code=69, offset=0, len=100
[00:00:00.300,000] <inf> coap_download: CoAP download done, got 100 bytes in 120 ms
```

## See also

[COAP Library](../../../../doxygen/html/group__coap.md)
