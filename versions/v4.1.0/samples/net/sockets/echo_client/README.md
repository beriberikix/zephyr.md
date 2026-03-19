---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/net/sockets/echo_client/README.html
original_path: samples/net/sockets/echo_client/README.html
---

# Echo client (advanced)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_client/README.rst/..)

## Overview

The echo-client sample application for Zephyr implements a UDP/TCP client
that will send IPv4 or IPv6 packets, wait for the data to be sent back,
and then verify it matches the data that was sent.

The source code for this sample application can be found at:
[samples/net/sockets/echo\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_client).

## Requirements

- [Networking with the host system](../../../../connectivity/networking/networking_with_host.md#networking-with-host)

## Building and Running

There are multiple ways to use this application. One of the most common
usage scenario is to run echo-client application inside QEMU. This is
described in [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu).

There are configuration files for different boards and setups in the
echo-client directory:

- `prj.conf`
  Generic config file, normally you should use this.
- `overlay-ot.conf`
  This overlay config enables support for OpenThread.
- `overlay-802154.conf`
  This overlay config enables support for native IEEE 802.15.4 connectivity.
  Note, that by default IEEE 802.15.4 L2 uses unacknowledged communication. To
  improve connection reliability, acknowledgments can be enabled with shell
  command: `ieee802154 ack set`.
- `overlay-qemu_802154.conf`
  This overlay config enables support for two QEMU’s when simulating
  IEEE 802.15.4 network that are connected together.
- `overlay-tls.conf`
  This overlay config enables support for TLS.

Build echo-client sample application like this:

```shell
west build -b <board to use> samples/net/sockets/echo_client -- -DCONF_FILE=<config file to use>
```

Example building for the nrf52840dk/nrf52840 with OpenThread support:

```shell
west build -b nrf52840dk/nrf52840 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot.conf"
west build -t run
```

Example building for the IEEE 802.15.4 RF2XX transceiver:

```shell
west build -b [samr21_xpro | sam4s_xplained | sam_v71_xult/samv71q21] samples/net/sockets/echo_client -- -DEXTRA_CONF_FILE=overlay-802154.conf
west flash
```

In a terminal window you can check if communication is happen:

```shell
$ minicom -D /dev/ttyACM1
```

### Enabling TLS support

Enable TLS support in the sample by building the project with the
`overlay-tls.conf` overlay file enabled, for example, using these commands:

```shell
west build -b qemu_x86 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

An alternative way is to specify `-DEXTRA_CONF_FILE=overlay-tls.conf` when
running `west build` or `cmake`.

The certificate and private key used by the sample can be found in the sample’s
`src` directory. The default certificates used by Socket Echo Client and
[Echo server (advanced)](../echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") enable establishing a secure connection
between the samples.

### SOCKS5 proxy support

It is also possible to connect to the echo-server through a SOCKS5 proxy.
To enable it, use `-DEXTRA_CONF_FILE=overlay-socks5.conf` when running `west
build` or `cmake`.

By default, to make the testing easier, the proxy is expected to run on the
same host as the echo-server in Linux host.

To start a proxy server, for example a builtin SOCKS server support in ssh
can be used (-D option). Use the following command to run it on your host
with the default port:

For IPv4 proxy server:

```shell
$ ssh -N -D 0.0.0.0:1080 localhost
```

For IPv6 proxy server:

```shell
$ ssh -N -D [::]:1080 localhost
```

Run both commands if you are testing IPv4 and IPv6.

To connect to a proxy server that is not running under the same IP as the
echo-server or uses a different port number, modify the following values
in echo\_client/src/tcp.c.

```c
#define SOCKS5_PROXY_V4_ADDR IPV4_ADDR
#define SOCKS5_PROXY_V6_ADDR IPV6_ADDR
#define SOCKS5_PROXY_PORT    1080
```

### Running echo-server in Linux Host

There is one useful testing scenario that can be used with Linux host.
Here echo-client is run in QEMU and echo-server is run in Linux host.

To use QEMU for testing, follow the [Networking with QEMU](../../../../connectivity/networking/qemu_setup.md#networking-with-qemu) guide.

In a terminal window:

```shell
$ sudo ./echo-server -i tap0
```

Run echo-client application in QEMU:

```shell
west build -b qemu_x86 samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-linux.conf"
west build -t run
```

Note that echo-server must be running in the Linux host terminal window
before you start the echo-client application in QEMU.
Exit QEMU by pressing `CTRL+A` `x`.

You can verify TLS communication with a Linux host as well. See
[https://github.com/zephyrproject-rtos/net-tools](https://github.com/zephyrproject-rtos/net-tools) documentation for information
on how to test TLS with Linux host samples.

See the [Echo server (advanced)](../echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") documentation for an alternate
way of running, with the echo-client on the Linux host and the echo-server
in QEMU.

### OpenThread RCP+Zephyr HOST (SPINEL connection via UART)

#### Prerequisites:

- Build `echo-server` for HOST PC (x86\_64)
  ([https://github.com/zephyrproject-rtos/net-tools](https://github.com/zephyrproject-rtos/net-tools)) SHA1:1c4fdba

```shell
$ make echo-server
```

- Program nRF RCP from Nordic nrf SDK (v2.7.0):

```shell
(v2.7.0) ~/ncs$ west build -p always -b nrf21540dk/nrf52840 -S logging nrf/samples/openthread/coprocessor
```

- Build mimxrt1020\_evk HOST (Zephyr):

```shell
west build -b mimxrt1020_evk samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-uart.conf"
```

And flash

```shell
$ west flash -r pyocd -i 0226000047784e4500439004d9170013e56100009796990
```

- Connect the nRF RCP with IMXRT1020 (HOST) via UART

```c
/*
 * imxrt1020_evk -> HOST
 * nRF21540-DK   -> RCP (nrf/samples/openthread/coprocessor)
 * LPUART2 used for communication:
 *  nRF21540 (P6) P0.08 RXD -> IMXRT1020-EVK (J17) D1 (GPIO B1 08) (TXD)
 *  nRF21540 (P6) P0.07 CTS -> IMXRT1020-EVK (J19) D8 (GPIO B1 07) (RTS)
 *  nRF21540 (P6) P0.06 TXD -> IMXRT1020-EVK (J17) D0 (GPIO B1 09) (RXD)
 *  nRF21540 (P6) P0.05 RTS -> IMXRT1020-EVK (J17) D7 (GPIO B1 06) (CTS)
 */
```

- Install the OTBR (OpenThread Border Router) docker container on your HOST PC (x86\_64)
  Follow steps from [https://docs.nordicsemi.com/bundle/ncs-2.5.1/page/nrf/protocols/thread/tools.html#running\_otbr\_using\_docker](https://docs.nordicsemi.com/bundle/ncs-2.5.1/page/nrf/protocols/thread/tools.html#running_otbr_using_docker)

**Most notable ones:**

> 1. Create `otbr0` network bridge to have access to OT network from HOST
>    Linux PC
>
> ```shell
> sudo docker network create --ipv6 --subnet fd11:db8:1::/64 -o com.docker.network.bridge.name=otbr0 otbr
> ```
>
> 2. Pull docker container for OTBR:
>
> ```shell
> docker pull nrfconnect/otbr:84c6aff
> ```
>
> 3. Start the docker image:
>
> ```shell
> sudo modprobe ip6table_filter
> sudo docker run -it --rm --privileged --name otbr --network otbr -p 8080:80 --sysctl "net.ipv6.conf.all.disable_ipv6=0 net.ipv4.conf.all.forwarding=1 net.ipv6.conf.all.forwarding=1" --volume /dev/ttyACM5:/dev/radio nrfconnect/otbr:84c6aff --radio-url spinel+hdlc+uart:///dev/radio?uart-baudrate=1000000
> ```
>
> 4. Add proper routing (`fd11:22::/64` are the IPv6 addresses - On-Mesh - which allow accessing the OT devices) on HOST PC (x86\_64)
>
> ```shell
> sudo ip -6 route add fd11:22::/64 dev otbr0 via fd11:db8:1::2
> ```
>
> And the output for on-OT address:
>
> ```shell
> ip route get fd11:22:0:0:5188:1678:d0c0:6893
> fd11:22::5188:1678:d0c0:6893 from :: via fd11:db8:1::2 dev otbr0 src fd11:db8:1::1 metric 1024 pref medium
> ```
>
> 5. Start the console to the docker image:
>
> ```shell
> sudo docker exec -it otbr /bin/bash
> ```
>
> Test with e.g.
>
> ```shell
> ot-ctl router table
> ot-ctl ipaddr
> ```

#### Configure OTBR

On the HOST PC’s webbrowser: [http://localhost:8080/](http://localhost:8080/)

Go to `Form` and leave default values - e.g:

> - Network Key: `00112233445566778899aabbccddeeff`
> - On-Mesh Prefix: `fd11:22::`
> - Channel: `15`

to “FORM” the OT network.

*Note:*
The “On-Mesh Prefix” shall match the one setup in `otbr0` routing.

#### Configure RCP (nRF21540-DK) + OT HOST (mimxrt1020)

```shell
ot factoryreset
ot dataset networkkey 00112233445566778899aabbccddeeff
ot ifconfig up
```

In the HOST PC www webpage interface please:
Commission -> Joiner PSKd\* set to `J01NME` -> START COMMISSION

```shell
ot joiner start J01NME
ot thread start
```

The `ot ipaddr` shall show IPv6 address starting from `fd11:22:0:0:`.
This one can be accessed from HOST’s PC network (via e.g.
`ping -6 fd11:22:0:0:e8bf:266b:63ca:eff4`).

#### Start `echo-server` on HOST PC (x86-64)

```shell
./echo-server -i otbr0
```

## See also

[BSD Sockets compatible API](../../../../doxygen/html/group__bsd__sockets.md)

[TLS credentials management](../../../../doxygen/html/group__tls__credentials.md)
