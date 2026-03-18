---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/dns_resolve.html
original_path: connectivity/networking/api/dns_resolve.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[DNS resolve](../../../samples/net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")
:   Resolve an IP address for a given hostname.

[TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")
:   Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

*group* dns\_resolve
:   DNS resolving library.

    Defines

    DNS\_MAX\_NAME\_SIZE
    :   Max size of the resolved name.

    Typedefs

    typedef void (\*dns\_resolve\_cb\_t)(enum [dns\_resolve\_status](#c.dns_resolve_status) status, struct [dns\_addrinfo](#c.dns_addrinfo) \*info, void \*user\_data)
    :   DNS resolve callback.

        The DNS resolve callback is called after a successful DNS resolving. The resolver can call this callback multiple times, one for each resolved address.

        Param status:
        :   The status of the query: DNS\_EAI\_INPROGRESS returned for each resolved address DNS\_EAI\_ALLDONE mark end of the resolving, info is set to NULL in this case DNS\_EAI\_CANCELED if the query was canceled manually or timeout happened DNS\_EAI\_FAIL if the name cannot be resolved by the server DNS\_EAI\_NODATA if there is no such name other values means that an error happened.

        Param info:
        :   Query results are stored here.

        Param user\_data:
        :   The user data given in [dns\_resolve\_name()](#group__dns__resolve_1ga24f9bc24e2021b6b528bb15e4fcca49b) call.

    Enums

    enum dns\_query\_type
    :   DNS query type enum.

        *Values:*

        enumerator DNS\_QUERY\_TYPE\_A = 1
        :   IPv4 query.

        enumerator DNS\_QUERY\_TYPE\_AAAA = 28
        :   IPv6 query.

    enum dns\_resolve\_status
    :   Status values for the callback.

        *Values:*

        enumerator DNS\_EAI\_NONAME = -2
        :   Invalid value for `ai\_flags’ field \*/ DNS\_EAI\_BADFLAGS = -1, /\*\* NAME or SERVICE is unknown.

        enumerator DNS\_EAI\_AGAIN = -3
        :   Temporary failure in name resolution.

        enumerator DNS\_EAI\_FAIL = -4
        :   Non-recoverable failure in name res.

        enumerator DNS\_EAI\_NODATA = -5
        :   No address associated with NAME.

        enumerator DNS\_EAI\_ADDRFAMILY = -9
        :   `ai_family' not supported */ DNS_EAI_FAMILY = -6, /**` ai\_socktype’ not supported \*/ DNS\_EAI\_SOCKTYPE = -7, /\*\* SRV not supported for `ai\_socktype’ \*/ DNS\_EAI\_SERVICE = -8, /\*\* Address family for NAME not supported

        enumerator DNS\_EAI\_MEMORY = -10
        :   Memory allocation failure.

        enumerator DNS\_EAI\_OVERFLOW = -12
        :   System error returned in `errno’ \*/ DNS\_EAI\_SYSTEM = -11, /\*\* Argument buffer overflow.

        enumerator DNS\_EAI\_INPROGRESS = -100
        :   Processing request in progress.

        enumerator DNS\_EAI\_CANCELED = -101
        :   Request canceled.

        enumerator DNS\_EAI\_NOTCANCELED = -102
        :   Request not canceled.

        enumerator DNS\_EAI\_ALLDONE = -103
        :   All requests done.

        enumerator DNS\_EAI\_IDN\_ENCODE = -105
        :   IDN encoding failed.

    enum dns\_resolve\_context\_state
    :   *Values:*

        enumerator DNS\_RESOLVE\_CONTEXT\_ACTIVE

        enumerator DNS\_RESOLVE\_CONTEXT\_DEACTIVATING

        enumerator DNS\_RESOLVE\_CONTEXT\_INACTIVE

    Functions

    int dns\_resolve\_init(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx, const char \*dns\_servers\_str[], const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*dns\_servers\_sa[])
    :   Init DNS resolving context.

        This function sets the DNS server address and initializes the DNS context that is used by the actual resolver. DNS server addresses can be specified either in textual form, or as struct sockaddr (or both). Note that the recommended way to resolve DNS names is to use the [dns\_get\_addr\_info()](#group__dns__resolve_1gaf891d7e21bddc8fbd029209b4339c01d) API. In that case user does not need to call [dns\_resolve\_init()](#group__dns__resolve_1ga74e2be49894100fe5da641331ef083de) as the DNS servers are already setup by the system.

        Parameters:
        :   - **ctx** – DNS context. If the context variable is allocated from the stack, then the variable needs to be valid for the whole duration of the resolving. Caller does not need to fill the variable beforehand or edit the context afterwards.
            - **dns\_servers\_str** – DNS server addresses using textual strings. The array is NULL terminated. The port number can be given in the string. Syntax for the server addresses with or without port numbers: IPv4 : 10.0.9.1 IPv4 + port : 10.0.9.1:5353 IPv6 : 2001:db8::22:42 IPv6 + port : [2001:db8::22:42]:5353
            - **dns\_servers\_sa** – DNS server addresses as struct sockaddr. The array is NULL terminated. Port numbers are optional in struct sockaddr, the default will be used if set to 0.

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_init\_default(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx)
    :   Init DNS resolving context with default Kconfig options.

        Parameters:
        :   - **ctx** – DNS context.

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_close(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx)
    :   Close DNS resolving context.

        This releases DNS resolving context and marks the context unusable. Caller must call the [dns\_resolve\_init()](#group__dns__resolve_1ga74e2be49894100fe5da641331ef083de) again to make context usable.

        Parameters:
        :   - **ctx** – DNS context

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_reconfigure(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx, const char \*servers\_str[], const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*servers\_sa[])
    :   Reconfigure DNS resolving context.

        Reconfigures DNS context with new server list.

        Parameters:
        :   - **ctx** – DNS context
            - **servers\_str** – DNS server addresses using textual strings. The array is NULL terminated. The port number can be given in the string. Syntax for the server addresses with or without port numbers: IPv4 : 10.0.9.1 IPv4 + port : 10.0.9.1:5353 IPv6 : 2001:db8::22:42 IPv6 + port : [2001:db8::22:42]:5353
            - **servers\_sa** – DNS server addresses as struct sockaddr. The array is NULL terminated. Port numbers are optional in struct sockaddr, the default will be used if set to 0.

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_cancel(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx, uint16\_t dns\_id)
    :   Cancel a pending DNS query.

        This releases DNS resources used by a pending query.

        Parameters:
        :   - **ctx** – DNS context
            - **dns\_id** – DNS id of the pending query

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_cancel\_with\_name(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx, uint16\_t dns\_id, const char \*query\_name, enum [dns\_query\_type](#c.dns_query_type) query\_type)
    :   Cancel a pending DNS query using id, name and type.

        This releases DNS resources used by a pending query.

        Parameters:
        :   - **ctx** – DNS context
            - **dns\_id** – DNS id of the pending query
            - **query\_name** – Name of the resource we are trying to query (hostname)
            - **query\_type** – Type of the query (A or AAAA)

        Returns:
        :   0 if ok, <0 if error.

    int dns\_resolve\_name(struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx, const char \*query, enum [dns\_query\_type](#c.dns_query_type) type, uint16\_t \*dns\_id, [dns\_resolve\_cb\_t](#c.dns_resolve_cb_t) cb, void \*user\_data, int32\_t timeout)
    :   Resolve DNS name.

        This function can be used to resolve e.g., IPv4 or IPv6 address. Note that this is asynchronous call, the function will return immediately and system will call the callback after resolving has finished or timeout has occurred. We might send the query to multiple servers (if there are more than one server configured), but we only use the result of the first received response.

        Parameters:
        :   - **ctx** – DNS context
            - **query** – What the caller wants to resolve.
            - **type** – What kind of data the caller wants to get.
            - **dns\_id** – DNS id is returned to the caller. This is needed if one wishes to cancel the query. This can be set to NULL if there is no need to cancel the query.
            - **cb** – Callback to call after the resolving has finished or timeout has happened.
            - **user\_data** – The user data.
            - **timeout** – The timeout value for the query. Possible values: SYS\_FOREVER\_MS: the query is tried forever, user needs to cancel it manually if it takes too long time to finish >0: start the query and let the system timeout it after specified ms

        Returns:
        :   0 if resolving was started ok, < 0 otherwise

    struct [dns\_resolve\_context](#c.dns_resolve_context) \*dns\_resolve\_get\_default(void)
    :   Get default DNS context.

        The system level DNS context uses DNS servers that are defined in project config file. If no DNS servers are defined by the user, then resolving DNS names using default DNS context will do nothing. The configuration options are described in subsys/net/lib/dns/Kconfig file.

        Returns:
        :   Default DNS context.

    static inline int dns\_get\_addr\_info(const char \*query, enum [dns\_query\_type](#c.dns_query_type) type, uint16\_t \*dns\_id, [dns\_resolve\_cb\_t](#c.dns_resolve_cb_t) cb, void \*user\_data, int32\_t timeout)
    :   Get IP address info from DNS.

        This function can be used to resolve e.g., IPv4 or IPv6 address. Note that this is asynchronous call, the function will return immediately and system will call the callback after resolving has finished or timeout has occurred. We might send the query to multiple servers (if there are more than one server configured), but we only use the result of the first received response. This variant uses system wide DNS servers.

        Parameters:
        :   - **query** – What the caller wants to resolve.
            - **type** – What kind of data the caller wants to get.
            - **dns\_id** – DNS id is returned to the caller. This is needed if one wishes to cancel the query. This can be set to NULL if there is no need to cancel the query.
            - **cb** – Callback to call after the resolving has finished or timeout has happened.
            - **user\_data** – The user data.
            - **timeout** – The timeout value for the connection. Possible values: SYS\_FOREVER\_MS: the query is tried forever, user needs to cancel it manually if it takes too long time to finish >0: start the query and let the system timeout it after specified ms

        Returns:
        :   0 if resolving was started ok, < 0 otherwise

    static inline int dns\_cancel\_addr\_info(uint16\_t dns\_id)
    :   Cancel a pending DNS query.

        This releases DNS resources used by a pending query.

        Parameters:
        :   - **dns\_id** – DNS id of the pending query

        Returns:
        :   0 if ok, <0 if error.

    struct dns\_addrinfo
    :   *#include <dns\_resolve.h>*

        Address info struct is passed to callback that gets all the results.

    struct dns\_resolve\_context
    :   *#include <dns\_resolve.h>*

        DNS resolve context structure.

        Public Members

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") dns\_server
        :   DNS server information.

        struct net\_context \*net\_ctx
        :   Connection to the DNS server.

        uint8\_t is\_mdns
        :   Is this server mDNS one.

        uint8\_t is\_llmnr
        :   Is this server LLMNR one.

        struct [k\_mutex](../../../kernel/services/synchronization/mutexes.md#c.k_mutex "k_mutex") lock
        :   Prevent concurrent access.

        [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") buf\_timeout
        :   This timeout is also used when a buffer is required from the buffer pools.

        enum [dns\_resolve\_context\_state](#c.dns_resolve_context_state) state
        :   Is this context in use.

        struct dns\_pending\_query
        :   *#include <dns\_resolve.h>*

            Result callbacks.

            We have multiple callbacks here so that it is possible to do multiple queries at the same time.

            Contents of this structure can be inspected and changed only when the lock is held.

            Public Members

            struct [k\_work\_delayable](../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") timer
            :   Timeout timer.

            struct [dns\_resolve\_context](#c.dns_resolve_context) \*ctx
            :   Back pointer to ctx, needed in timeout handler.

            [dns\_resolve\_cb\_t](#c.dns_resolve_cb_t) cb
            :   Result callback.

                A null value indicates the slot is not in use.

            void \*user\_data
            :   User data.

            [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout
            :   TX timeout.

            const char \*query
            :   String containing the thing to resolve like www.example.com.

                This is set to a non-null value when the query is started, and is not used thereafter.

                If the query completed at a point where the work item was still pending the pointer is cleared to indicate that the query is complete, but release of the query slot will be deferred until a request for a slot determines that the work item has been released.

            enum [dns\_query\_type](#c.dns_query_type) query\_type
            :   Query type.

            uint16\_t id
            :   DNS id of this query.

            uint16\_t query\_hash
            :   Hash of the DNS name + query type we are querying.

                This hash is calculated so we can match the response that we are receiving. This is needed mainly for mDNS which is setting the DNS id to 0, which means that the id alone cannot be used to find correct pending query.
