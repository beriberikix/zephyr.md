---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/ppp.html
original_path: connectivity/networking/api/ppp.html
---

# Point-to-Point Protocol (PPP) Support

## [Overview](#id1)

[Point-to-Point Protocol](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) (PPP) is a data link
layer (layer 2) communications protocol used to establish a direct connection
between two nodes. PPP is used over many types of serial links since IP packets
cannot be transmitted over a modem line on their own, without some data link
protocol.

In Zephyr, each individual PPP link is modelled as a network interface. This
is similar to how Linux implements PPP.

PPP support must be enabled at compile time by setting option
[`CONFIG_NET_L2_PPP`](../../../kconfig.md#CONFIG_NET_L2_PPP "CONFIG_NET_L2_PPP").
The PPP implementation supports only these protocols:

- LCP (Link Control Protocol,
  [RFC1661](https://tools.ietf.org/html/rfc1661))
- HDLC (High-level data link control,
  [RFC1662](https://tools.ietf.org/html/rfc1662))
- IPCP (IP Control Protocol,
  [RFC1332](https://tools.ietf.org/html/rfc1332))
- IPV6CP (IPv6 Control Protocol,
  [RFC5072](https://tools.ietf.org/html/rfc5072))

For using PPP with a cellular modem, see [Cellular modem](../../../samples/net/cellular_modem/README.md#cellular-modem "Use a cellular modem to communicate with a UDP server.") sample
for additional information.

## [Testing](#id2)

See the [net-tools README](https://github.com/zephyrproject-rtos/net-tools/blob/master/README.md#ppp-connectivity) file for more details on how to test the Zephyr PPP
against pppd running in Linux.
