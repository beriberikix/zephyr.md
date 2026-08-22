---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/connectivity/networking/api/thread.html
original_path: connectivity/networking/api/thread.html
---

# Thread protocol

## [Overview](#id1)

Thread is a low-power mesh networking technology, designed specifically for home
automation applications. It is an IPv6-based standard, which uses 6LoWPAN
technology over IEEE 802.15.4 protocol. IP connectivity lets you easily connect
a Thread mesh network to the internet with a Thread Border Router.

The Thread specification provides a high level of network security. Mesh networks
built with Thread are secure - only authenticated devices can join the network
and all communications within the mesh are encrypted. More information about
Thread protocol can be found at
[Thread Group website](https://www.threadgroup.org).

Zephyr integrates an open source Thread protocol implementation called OpenThread,
documented on the [OpenThread website](https://openthread.io/).

## [Internet connectivity](#id2)

A Thread Border Router is required to connect mesh network to the internet.
An open source implementation of Thread Border Router is provided by the OpenThread
community. See
[OpenThread Border Router guide](https://openthread.io/guides/border-router)
for instructions on how to set up a Border Router.

## [Sample usage](#id3)

You can try using OpenThread with the Zephyr Echo server and Echo client samples,
which provide out-of-the-box configuration for OpenThread. To enable OpenThread
support in these samples, build them with `overlay-ot.conf` overlay config file.
See [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
samples for details.

Zephyr also provides an [OpenThread shell](../../../samples/net/openthread/shell/README.md#openthread-shell "Test Thread and IEEE 802.15.4 using the OpenThread shell."), which is useful for
testing and debugging Thread and its underlying IEEE 802.15.4 drivers.

## [Thread related APIs](#id4)

### [OpenThread Driver API](#id5)

OpenThread L2 uses Zephyr’s protocol agnostic IEEE 802.15.4 driver API
internally. This API is of interest to **driver developers** that want to
support OpenThread.

The driver API is part of the [IEEE 802.15.4 Driver API](ieee802154.md#ieee802154-driver-api) subsystem and
documented there.

### [OpenThread L2 Adaptation Layer API](#id6)

Zephyr’s OpenThread L2 platform adaptation layer glues the external OpenThread
stack together with Zephyr’s IEEE 802.15.4 protocol agnostic driver API. This
API is of interest to OpenThread L2 **subsystem contributors** only.

### [OpenThread Platform API](#id7)

The OpenThread platform API is defined by the OpenThread stack and implemented in Zephyr as an
OpenThread module. Applications can use this implementation directly, or access it through the
OpenThread L2 adaptation layer.

#### Using the OpenThread L2 Adaptation Layer API

To use the OpenThread platform API via the OpenThread L2 adaptation layer, enable both the
[`CONFIG_NET_L2_OPENTHREAD`](../../../kconfig.md#CONFIG_NET_L2_OPENTHREAD "CONFIG_NET_L2_OPENTHREAD") and [`CONFIG_NETWORKING`](../../../kconfig.md#CONFIG_NETWORKING "CONFIG_NETWORKING") Kconfig options
by setting them to `y`. The adaptation layer will use the OpenThread radio API implementation
found in `modules/openthread/platform/radio.c`. In this setup, the OpenThread stack is
initialized and managed by the adaptation layer.

#### Using the OpenThread Platform API Directly

You can also use the OpenThread platform API directly, bypassing the OpenThread L2 adaptation
layer. However, this approach requires you to provide your own implementation of the OpenThread
radio API that is compatible with your specific radio driver.

To use the OpenThread platform API directly, set the [`CONFIG_OPENTHREAD`](../../../kconfig.md#CONFIG_OPENTHREAD "CONFIG_OPENTHREAD") Kconfig
option to `y`, and do **not** set [`CONFIG_NET_L2_OPENTHREAD`](../../../kconfig.md#CONFIG_NET_L2_OPENTHREAD "CONFIG_NET_L2_OPENTHREAD"). In this case, you
must implement the following functions from the [OpenThread radio API](https://openthread.io/reference/group/radio-config) using your own radio driver:

- `otPlatRadioGetPromiscuous`
- `otPlatRadioGetCcaEnergyDetectThreshold`
- `otPlatRadioGetTransmitPower`
- `otPlatRadioGetIeeeEui64`
- `otPlatRadioSetPromiscuous`
- `otPlatRadioGetCaps`
- `otPlatRadioGetTransmitBuffer`
- `otPlatRadioSetPanId`
- `otPlatRadioEnable`
- `otPlatRadioDisable`
- `otPlatRadioReceive`
- `otPlatRadioGetRssi`
- `otPlatRadioGetReceiveSensitivity`
- `otPlatRadioEnergyScan`
- `otPlatRadioSetExtendedAddress`
- `otPlatRadioSetShortAddress`
- `otPlatRadioAddSrcMatchExtEntry`
- `otPlatRadioTransmit`
- `otPlatRadioClearSrcMatchShortEntries`
- `otPlatRadioClearSrcMatchExtEntries`
- `otPlatRadioEnableSrcMatch`
- `otPlatRadioAddSrcMatchShortEntry`
- `otPlatRadioClearSrcMatchShortEntry`
- `otPlatRadioClearSrcMatchExtEntry`

Additionally, you must implement the following functions from the OpenThread radio API (see
[include/zephyr/net/openthread.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/openthread.h)) to handle radio initialization and event processing:

- `platformRadioInit()`
- `platformRadioProcess()`

To initialize the OpenThread stack in this approach, either call the `ot_platform_init()`
function in your application, or enable the [`CONFIG_OPENTHREAD_SYS_INIT`](../../../kconfig.md#CONFIG_OPENTHREAD_SYS_INIT "CONFIG_OPENTHREAD_SYS_INIT") Kconfig
option to automatically initialize OpenThread during system startup. You can set the
initialization priority using the [`CONFIG_OPENTHREAD_SYS_INIT_PRIORITY`](../../../kconfig.md#CONFIG_OPENTHREAD_SYS_INIT_PRIORITY "CONFIG_OPENTHREAD_SYS_INIT_PRIORITY") Kconfig
option.

[OpenThread stack](../../../doxygen/html/group__openthread.md)

Related code samples

- [OpenThread co-processor](../../../samples/net/openthread/coprocessor/README.md#openthread-coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")Build a Thread border-router using OpenThread's co-processor designs.
- [OpenThread CoAP client and server application](../../../samples/net/openthread/coap/README.md#ot-coap "Build a Full Thread Device (FTD) CoAP server and client.")Build a Full Thread Device (FTD) CoAP server and client.
