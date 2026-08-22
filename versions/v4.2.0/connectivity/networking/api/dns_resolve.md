---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/connectivity/networking/api/dns_resolve.html
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

DNS-based service discovery queries described in
[IETF RFC6763](https://datatracker.ietf.org/doc/html/rfc6763)
can be done by [`dns_resolve_service()`](../../../doxygen/html/group__dns__resolve.md#gaf28f6f8baa97d0b2341e1bdc02b6cb8c) API.
The returned service descriptions are passed to user supplied callback
and the API sets the address family to [`AF_LOCAL`](../../../doxygen/html/group__ip__4__6.md#gae24f1f9ea44fcce3affcb2137f593dc1) to indicate that
the value is not an IPv4 or IPv6 address but a service description.

Example:

```c
#include <zephyr/net/dns_resolve.h>

#define MAX_STR_LEN CONFIG_DNS_RESOLVER_MAX_NAME_LEN

static void dns_result_cb(enum dns_resolve_status status,
                          struct dns_addrinfo *info,
                          void *user_data)
{
     if (status == DNS_EAI_CANCELED) {
             /* dns: Timeout while resolving name */
             return;
     }

     if (status == DNS_EAI_INPROGRESS && info) {
             char str[MAX_STR_LEN + 1];

             if (info->ai_family == AF_INET) {
                     net_addr_ntop(AF_INET,
                                   &net_sin(&info->ai_addr)->sin_addr,
                                   str, NET_IPV4_ADDR_LEN);
             } else if (info->ai_family == AF_INET6) {
                     net_addr_ntop(AF_INET6,
                                   &net_sin6(&info->ai_addr)->sin6_addr,
                                   str, NET_IPV6_ADDR_LEN);
             } else if (info->ai_family == AF_LOCAL) {
                     /* service discovery */
                     memset(str, 0, MAX_STR_LEN);
                     memcpy(str, info->ai_canonname,
                            MIN(info->ai_addrlen, MAX_STR_LEN));
             } else {
                     strncpy(str, "Invalid proto family", MAX_STR_LEN + 1);
             }

             str[MAX_STR_LEN] = '\0';

             printk("dns: %s\n", str);
             return;
     }

     if (status == DNS_EAI_ALLDONE) {
             printk("dns: All results received\n");
             return;
     }

     if (status == DNS_EAI_FAIL) {
             printk("dns: No such name found.\n");
             return;
     }

     printk("dns: Unhandled status %d received (errno %d)\n", status, errno);
}

#define DNS_TIMEOUT (MSEC_PER_SEC * 5) /* in ms */

static void discover_service(void)
{
     int ret = dns_resolve_service(dns_resolve_get_default(),
                                   "_http._tcp.dns-sd.org",
                                   NULL, dns_result_cb,
                                   NULL, DNS_TIMEOUT);
     ...
}
```

The above query would return output like this:

As the service discovery query could return long strings and the packet size could
be large, you might need to adjust following Kconfig options:

- [`CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE`](../../../kconfig.md#CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE "CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE"). This tells the maximum size of the
  answer, typical value for this option could be 1024. The default size for this option is
  512 bytes.
- [`CONFIG_DNS_RESOLVER_MAX_NAME_LEN`](../../../kconfig.md#CONFIG_DNS_RESOLVER_MAX_NAME_LEN "CONFIG_DNS_RESOLVER_MAX_NAME_LEN"). This tells the maximum length of the
  returned name. The value depends on your expected data size, typical value might be 128 bytes.

## [Sample usage](#id2)

See [DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.") sample application for details.

## [API Reference](#id3)

[DNS Resolve Library](../../../doxygen/html/group__dns__resolve.md)

Related code samples

- [AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")Resolve an IP address for a given hostname.
- [TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.
