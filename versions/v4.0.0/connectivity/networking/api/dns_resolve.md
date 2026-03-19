---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/dns_resolve.html
original_path: connectivity/networking/api/dns_resolve.html
---

# DNS Resolve

## [Overview](#id1)

The DNS resolver implements a basic DNS resolver according
to [IETF RFC1035 on Domain Implementation and Specification](https://tools.ietf.org/html/rfc1035).
Supported DNS answers are IPv4/IPv6 addresses and CNAME.

If a CNAME is received, the DNS resolver will create another DNS query.
The number of additional queries is controlled by the
[`CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES`](../../../kconfig.md#CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES "CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES") Kconfig variable.

The multicast DNS (mDNS) client resolver support can be enabled by setting
[`CONFIG_MDNS_RESOLVER`](../../../kconfig.md#CONFIG_MDNS_RESOLVER "CONFIG_MDNS_RESOLVER") Kconfig option.
See [IETF RFC6762](https://tools.ietf.org/html/rfc6762) for more details
about mDNS.

The link-local multicast name resolution (LLMNR) client resolver support can be
enabled by setting the [`CONFIG_LLMNR_RESOLVER`](../../../kconfig.md#CONFIG_LLMNR_RESOLVER "CONFIG_LLMNR_RESOLVER") Kconfig variable.
See [IETF RFC4795](https://tools.ietf.org/html/rfc4795) for more details
about LLMNR.

For more information about DNS configuration variables, see:
[subsys/net/lib/dns/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig). The DNS resolver API can be found at
[include/zephyr/net/dns\_resolve.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/dns_resolve.h).

## [Sample usage](#id2)

See [DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.") sample application for details.

## [API Reference](#id3)

[DNS Resolve Library](../../../doxygen/html/group__dns__resolve.md)

Related code samples

- [AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")Resolve an IP address for a given hostname.
- [TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.
