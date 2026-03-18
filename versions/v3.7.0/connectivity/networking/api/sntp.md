---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/sntp.html
original_path: connectivity/networking/api/sntp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Simple Network Time Protocol Library

## [Overview](#id1)

The SNTP library implements
[IETF RFC4330 (Simple Network Time Protocol v4)](https://tools.ietf.org/html/rfc4330).

SNTP provides a way to synchronize clocks in computer networks.

## [API Reference](#id2)

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[SNTP client](../../../samples/net/sockets/sntp_client/README.md#sntp-client "Use SNTP to get the current time from the host.")
:   Use SNTP to get the current time from the host.

*group* SNTP
:   Simple Network Time Protocol API.

    Functions

    int sntp\_init(struct [sntp\_ctx](#c.sntp_ctx) \*ctx, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len)
    :   Initialize SNTP context.

        Parameters:
        :   - **ctx** – Address of sntp context.
            - **addr** – IP address of NTP/SNTP server.
            - **addr\_len** – IP address length of NTP/SNTP server.

        Returns:
        :   0 if ok, <0 if error.

    int sntp\_query(struct [sntp\_ctx](#c.sntp_ctx) \*ctx, uint32\_t timeout, struct [sntp\_time](#c.sntp_time) \*time)
    :   Perform SNTP query.

        Parameters:
        :   - **ctx** – Address of sntp context.
            - **timeout** – Timeout of waiting for sntp response (in milliseconds).
            - **time** – Timestamp including integer and fractional seconds since 1 Jan 1970 (output).

        Returns:
        :   0 if ok, <0 if error (-ETIMEDOUT if timeout).

    void sntp\_close(struct [sntp\_ctx](#c.sntp_ctx) \*ctx)
    :   Release SNTP context.

        Parameters:
        :   - **ctx** – Address of sntp context.

    int sntp\_simple(const char \*server, uint32\_t timeout, struct [sntp\_time](#c.sntp_time) \*ts)
    :   Convenience function to query SNTP in one-shot fashion.

        Convenience wrapper which calls [getaddrinfo()](sockets.md#group__bsd__sockets_1ga08be4218900930dcc3add7e03173a83c), [sntp\_init()](#group__sntp_1ga945936e5164bbd959cfa666ceacdac13), [sntp\_query()](#group__sntp_1ga8a32571c1706fbe50d4e58e1cb7f38f6), and [sntp\_close()](#group__sntp_1ga0cff25edb11ae944dd24a234450a2f3d).

        Parameters:
        :   - **server** – Address of server in format addr[:port]
            - **timeout** – Query timeout
            - **ts** – Timestamp including integer and fractional seconds since 1 Jan 1970 (output).

        Returns:
        :   0 if ok, <0 if error (-ETIMEDOUT if timeout).

    int sntp\_simple\_addr(struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len, uint32\_t timeout, struct [sntp\_time](#c.sntp_time) \*ts)
    :   Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct.

        Convenience wrapper which calls [sntp\_init()](#group__sntp_1ga945936e5164bbd959cfa666ceacdac13), [sntp\_query()](#group__sntp_1ga8a32571c1706fbe50d4e58e1cb7f38f6) and [sntp\_close()](#group__sntp_1ga0cff25edb11ae944dd24a234450a2f3d).

        Parameters:
        :   - **addr** – IP address of NTP/SNTP server.
            - **addr\_len** – IP address length of NTP/SNTP server.
            - **timeout** – Query timeout
            - **ts** – Timestamp including integer and fractional seconds since 1 Jan 1970 (output).

        Returns:
        :   0 if ok, <0 if error (-ETIMEDOUT if timeout).

    struct sntp\_time
    :   *#include <sntp.h>*

        Time as returned by SNTP API, fractional seconds since 1 Jan 1970.

        Public Members

        uint64\_t seconds
        :   Second value.

        uint32\_t fraction
        :   Fractional seconds value.

    struct sntp\_ctx
    :   *#include <sntp.h>*

        SNTP context.

        Public Members

        struct [sntp\_time](#c.sntp_time) expected\_orig\_ts
        :   Timestamp when the request was sent from client to server.

            This is used to check if the originated timestamp in the server reply matches the one in client request.
