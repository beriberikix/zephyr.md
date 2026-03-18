---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/coap.html
original_path: connectivity/networking/api/coap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# CoAP

## [Overview](#id2)

The Constrained Application Protocol (CoAP) is a specialized web transfer
protocol for use with constrained nodes and constrained (e.g., low-power,
lossy) networks. It provides a convenient API for RESTful Web services
that support CoAP’s features. For more information about the protocol
itself, see [IETF RFC7252 The Constrained Application Protocol](https://tools.ietf.org/html/rfc7252).

Zephyr provides a CoAP library which supports client and server roles.
The library can be enabled with [`CONFIG_COAP`](../../../kconfig.md#CONFIG_COAP "CONFIG_COAP") Kconfig option and
is configurable as per user needs. The Zephyr CoAP library
is implemented using plain buffers. Users of the API create sockets
for communication and pass the buffer to the library for parsing and other
purposes. The library itself doesn’t create any sockets for users.

On top of CoAP, Zephyr has support for LWM2M “Lightweight Machine 2 Machine”
protocol, a simple, low-cost remote management and service enablement mechanism.
See [Lightweight M2M (LWM2M)](lwm2m.md#lwm2m-interface) for more information.

Supported RFCs:

- [RFC7252: The Constrained Application Protocol (CoAP)](https://tools.ietf.org/html/rfc7252)
- [RFC6690: Constrained RESTful Environments (CoRE) Link Format](https://tools.ietf.org/html/rfc6690)
- [RFC7959: Block-Wise Transfers in the Constrained Application Protocol (CoAP)](https://tools.ietf.org/html/rfc7959)
- [RFC7641: Observing Resources in the Constrained Application Protocol (CoAP)](https://tools.ietf.org/html/rfc7641)

Note

Not all parts of these RFCs are supported. Features are supported based on Zephyr requirements.

## [Sample Usage](#id3)

### [CoAP Server](#id4)

Note

A [CoAP server](coap_server.md#coap-server-interface) subsystem is available, the following is for creating a custom
server implementation.

To create a CoAP server, resources for the server need to be defined.
The `.well-known/core` resource should be added before all other
resources that should be included in the responses of the `.well-known/core`
resource.

```c
static struct coap_resource resources[] = {
    { .get = well_known_core_get,
      .path = COAP_WELL_KNOWN_CORE_PATH,
    },
    { .get  = sample_get,
      .post = sample_post,
      .del  = sample_del,
      .put  = sample_put,
      .path = sample_path
    },
    { },
};
```

An application reads data from the socket and passes the buffer to the CoAP library
to parse the message. If the CoAP message is proper, the library uses the buffer
along with resources defined above to call the correct callback function
to handle the CoAP request from the client. It’s the callback function’s
responsibility to either reply or act according to CoAP request.

```c
coap_packet_parse(&request, data, data_len, options, opt_num);
...
coap_handle_request(&request, resources, options, opt_num,
                    client_addr, client_addr_len);
```

If [`CONFIG_COAP_URI_WILDCARD`](../../../kconfig.md#CONFIG_COAP_URI_WILDCARD "CONFIG_COAP_URI_WILDCARD") enabled, server may accept multiple resources
using MQTT-like wildcard style:

- the plus symbol represents a single-level wild card in the path;
- the hash symbol represents the multi-level wild card in the path.

```c
static const char * const led_set[] = { "led","+","set", NULL };
static const char * const btn_get[] = { "button","#", NULL };
static const char * const no_wc[] = { "test","+1", NULL };
```

It accepts /led/0/set, led/1234/set, led/any/set, /button/door/1, /test/+1,
but returns -ENOENT for /led/1, /test/21, /test/1.

This option is enabled by default, disable it to avoid unexpected behaviour
with resource path like ‘/some\_resource/+/#’.

### [CoAP Client](#id5)

Note

A [CoAP client](coap_client.md#coap-client-interface) subsystem is available, the following is for creating a custom
client implementation.

If the CoAP client knows about resources in the CoAP server, the client can start
prepare CoAP requests and wait for responses. If the client doesn’t know
about resources in the CoAP server, it can request resources through
the `.well-known/core` CoAP message.

```c
/* Initialize the CoAP message */
char *path = "test";
struct coap_packet request;
uint8_t data[100];
uint8_t payload[20];

coap_packet_init(&request, data, sizeof(data),
                 1, COAP_TYPE_CON, 8, coap_next_token(),
                 COAP_METHOD_GET, coap_next_id());

/* Append options */
coap_packet_append_option(&request, COAP_OPTION_URI_PATH,
                          path, strlen(path));

/* Append Payload marker if you are going to add payload */
coap_packet_append_payload_marker(&request);

/* Append payload */
coap_packet_append_payload(&request, (uint8_t *)payload,
                           sizeof(payload) - 1);

/* send over sockets */
```

## [Testing](#id6)

There are various ways to test Zephyr CoAP library.

### [libcoap](#id7)

libcoap implements a lightweight application-protocol for devices that are
resource constrained, such as by computing power, RF range, memory, bandwidth,
or network packet sizes. Sources can be found here [libcoap](https://github.com/obgm/libcoap).
libcoap has a script (`examples/etsi_coaptest.sh`) to test coap-server functionality
in Zephyr.

See the [net-tools](https://github.com/zephyrproject-rtos/net-tools) project for more details

The [CoAP service](../../../samples/net/sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.") sample can be built and executed on QEMU as described
in [Networking with QEMU](../qemu_setup.md#networking-with-qemu).

Use this command on the host to run the libcoap implementation of
the ETSI test cases:

```shell
sudo ./libcoap/examples/etsi_coaptest.sh -i tap0 2001:db8::1
```

### [TTCN3](#id8)

Eclipse has TTCN3 based tests to run against CoAP implementations.

Install eclipse-titan and set symbolic links for titan tools

```shell
sudo apt-get install eclipse-titan

cd /usr/share/titan

sudo ln -s /usr/bin bin
sudo ln /usr/bin/titanver bin
sudo ln -s /usr/bin/mctr_cli bin
sudo ln -s /usr/include/titan include
sudo ln -s /usr/lib/titan lib

export TTCN3_DIR=/usr/share/titan

git clone https://gitlab.eclipse.org/eclipse/titan/titan.misc.git

cd titan.misc
```

Follow the instruction to setup CoAP test suite from here:

- [https://gitlab.eclipse.org/eclipse/titan/titan.misc](https://gitlab.eclipse.org/eclipse/titan/titan.misc)
- [https://gitlab.eclipse.org/eclipse/titan/titan.misc/-/tree/master/CoAP\_Conf](https://gitlab.eclipse.org/eclipse/titan/titan.misc/-/tree/master/CoAP_Conf)

After the build is complete, the [CoAP service](../../../samples/net/sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.") sample can be built
and executed on QEMU as described in [Networking with QEMU](../qemu_setup.md#networking-with-qemu).

Change the client (test suite) and server (Zephyr coap-server sample) addresses
in coap.cfg file as per your setup.

Execute the test cases with following command.

```shell
ttcn3_start coaptests coap.cfg
```

Sample output of ttcn3 tests looks like this.

```shell
Verdict statistics: 0 none (0.00 %), 10 pass (100.00 %), 0 inconc (0.00 %), 0 fail (0.00 %), 0 error (0.00 %).
Test execution summary: 10 test cases were executed. Overall verdict: pass
```

## [API Reference](#id9)

Related code samples

[CoAP client](../../../samples/net/sockets/coap_client/README.md#coap-client "Use the CoAP library to implement a client that fetches a resource.")
:   Use the CoAP library to implement a client that fetches a resource.

[CoAP service](../../../samples/net/sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.")
:   Use the CoAP server subsystem to register CoAP resources.

*group* COAP Library
:   COAP library.

    **Since**
    :   1.10

    **Version**
    :   0.8.0

    Defines

    COAP\_MAKE\_RESPONSE\_CODE(class, det)
    :   Utility macro to create a CoAP response code.

        Parameters:
        :   - **class** – Class of the response code (ex. 2, 4, 5, …)
            - **det** – Detail of the response code

        Returns:
        :   Response code literal

    COAP\_WELL\_KNOWN\_CORE\_PATH
    :   This resource should be added before all other resources that should be included in the responses of the .well-known/core resource if is to be used with coap\_well\_known\_core\_get.

    Typedefs

    typedef int (\*coap\_method\_t)(struct [coap\_resource](#c.coap_resource) \*resource, struct [coap\_packet](#c.coap_packet) \*request, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len)
    :   Type of the callback being called when a resource’s method is invoked by the remote entity.

    typedef void (\*coap\_notify\_t)(struct [coap\_resource](#c.coap_resource) \*resource, struct [coap\_observer](#c.coap_observer) \*observer)
    :   Type of the callback being called when a resource’s has observers to be informed when an update happens.

    typedef int (\*coap\_reply\_t)(const struct [coap\_packet](#c.coap_packet) \*response, struct [coap\_reply](#c.coap_reply) \*reply, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*from)
    :   Helper function to be called when a response matches the a pending request.

        When sending blocks, the callback is only executed when the reply of the last block is received. i.e. it is not called when the code of the reply is ‘continue’ (2.31).

    Enums

    enum coap\_option\_num
    :   Set of CoAP packet options we are aware of.

        Users may add options other than these to their packets, provided they know how to format them correctly. The only restriction is that all options must be added to a packet in numeric order.

        Refer to RFC 7252, section 12.2 for more information.

        *Values:*

        enumerator COAP\_OPTION\_IF\_MATCH = 1
        :   If-Match.

        enumerator COAP\_OPTION\_URI\_HOST = 3
        :   Uri-Host.

        enumerator COAP\_OPTION\_ETAG = 4
        :   ETag.

        enumerator COAP\_OPTION\_IF\_NONE\_MATCH = 5
        :   If-None-Match.

        enumerator COAP\_OPTION\_OBSERVE = 6
        :   Observe (RFC 7641).

        enumerator COAP\_OPTION\_URI\_PORT = 7
        :   Uri-Port.

        enumerator COAP\_OPTION\_LOCATION\_PATH = 8
        :   Location-Path.

        enumerator COAP\_OPTION\_URI\_PATH = 11
        :   Uri-Path.

        enumerator COAP\_OPTION\_CONTENT\_FORMAT = 12
        :   Content-Format.

        enumerator COAP\_OPTION\_MAX\_AGE = 14
        :   Max-Age.

        enumerator COAP\_OPTION\_URI\_QUERY = 15
        :   Uri-Query.

        enumerator COAP\_OPTION\_ACCEPT = 17
        :   Accept.

        enumerator COAP\_OPTION\_LOCATION\_QUERY = 20
        :   Location-Query.

        enumerator COAP\_OPTION\_BLOCK2 = 23
        :   Block2 (RFC 7959).

        enumerator COAP\_OPTION\_BLOCK1 = 27
        :   Block1 (RFC 7959).

        enumerator COAP\_OPTION\_SIZE2 = 28
        :   Size2 (RFC 7959).

        enumerator COAP\_OPTION\_PROXY\_URI = 35
        :   Proxy-Uri.

        enumerator COAP\_OPTION\_PROXY\_SCHEME = 39
        :   Proxy-Scheme.

        enumerator COAP\_OPTION\_SIZE1 = 60
        :   Size1.

        enumerator COAP\_OPTION\_ECHO = 252
        :   Echo (RFC 9175).

        enumerator COAP\_OPTION\_REQUEST\_TAG = 292
        :   Request-Tag (RFC 9175).

    enum coap\_method
    :   Available request methods.

        To be used when creating a request or a response.

        *Values:*

        enumerator COAP\_METHOD\_GET = 1
        :   GET.

        enumerator COAP\_METHOD\_POST = 2
        :   POST.

        enumerator COAP\_METHOD\_PUT = 3
        :   PUT.

        enumerator COAP\_METHOD\_DELETE = 4
        :   DELETE.

        enumerator COAP\_METHOD\_FETCH = 5
        :   FETCH.

        enumerator COAP\_METHOD\_PATCH = 6
        :   PATCH.

        enumerator COAP\_METHOD\_IPATCH = 7
        :   IPATCH.

    enum coap\_msgtype
    :   CoAP packets may be of one of these types.

        *Values:*

        enumerator COAP\_TYPE\_CON = 0
        :   Confirmable message.

            The packet is a request or response the destination end-point must acknowledge.

        enumerator COAP\_TYPE\_NON\_CON = 1
        :   Non-confirmable message.

            The packet is a request or response that doesn’t require acknowledgements.

        enumerator COAP\_TYPE\_ACK = 2
        :   Acknowledge.

            Response to a confirmable message.

        enumerator COAP\_TYPE\_RESET = 3
        :   Reset.

            Rejecting a packet for any reason is done by sending a message of this type.

    enum coap\_response\_code
    :   Set of response codes available for a response packet.

        To be used when creating a response.

        *Values:*

        enumerator COAP\_RESPONSE\_CODE\_OK = ((2 << 5) | (0))
        :   2.00 - OK

        enumerator COAP\_RESPONSE\_CODE\_CREATED = ((2 << 5) | (1))
        :   2.01 - Created

        enumerator COAP\_RESPONSE\_CODE\_DELETED = ((2 << 5) | (2))
        :   2.02 - Deleted

        enumerator COAP\_RESPONSE\_CODE\_VALID = ((2 << 5) | (3))
        :   2.03 - Valid

        enumerator COAP\_RESPONSE\_CODE\_CHANGED = ((2 << 5) | (4))
        :   2.04 - Changed

        enumerator COAP\_RESPONSE\_CODE\_CONTENT = ((2 << 5) | (5))
        :   2.05 - Content

        enumerator COAP\_RESPONSE\_CODE\_CONTINUE = ((2 << 5) | (31))
        :   2.31 - Continue

        enumerator COAP\_RESPONSE\_CODE\_BAD\_REQUEST = ((4 << 5) | (0))
        :   4.00 - Bad Request

        enumerator COAP\_RESPONSE\_CODE\_UNAUTHORIZED = ((4 << 5) | (1))
        :   4.01 - Unauthorized

        enumerator COAP\_RESPONSE\_CODE\_BAD\_OPTION = ((4 << 5) | (2))
        :   4.02 - Bad Option

        enumerator COAP\_RESPONSE\_CODE\_FORBIDDEN = ((4 << 5) | (3))
        :   4.03 - Forbidden

        enumerator COAP\_RESPONSE\_CODE\_NOT\_FOUND = ((4 << 5) | (4))
        :   4.04 - Not Found

        enumerator COAP\_RESPONSE\_CODE\_NOT\_ALLOWED = ((4 << 5) | (5))
        :   4.05 - Method Not Allowed

        enumerator COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE = ((4 << 5) | (6))
        :   4.06 - Not Acceptable

        enumerator COAP\_RESPONSE\_CODE\_INCOMPLETE = ((4 << 5) | (8))
        :   4.08 - Request Entity Incomplete

        enumerator COAP\_RESPONSE\_CODE\_CONFLICT = ((4 << 5) | (9))
        :   4.12 - Precondition Failed

        enumerator COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED = ((4 << 5) | (12))
        :   4.12 - Precondition Failed

        enumerator COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE = ((4 << 5) | (13))
        :   4.13 - Request Entity Too Large

        enumerator COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT = ((4 << 5) | (15))
        :   4.15 - Unsupported Content-Format

        enumerator COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY = ((4 << 5) | (22))
        :   4.22 - Unprocessable Entity

        enumerator COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS = ((4 << 5) | (29))
        :   4.29 - Too Many Requests

        enumerator COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR = ((5 << 5) | (0))
        :   5.00 - Internal Server Error

        enumerator COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED = ((5 << 5) | (1))
        :   5.01 - Not Implemented

        enumerator COAP\_RESPONSE\_CODE\_BAD\_GATEWAY = ((5 << 5) | (2))
        :   5.02 - Bad Gateway

        enumerator COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE = ((5 << 5) | (3))
        :   5.03 - Service Unavailable

        enumerator COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT = ((5 << 5) | (4))
        :   5.04 - Gateway Timeout

        enumerator COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED = ((5 << 5) | (5))
        :   5.05 - Proxying Not Supported

    enum coap\_content\_format
    :   Set of Content-Format option values for CoAP.

        To be used when encoding or decoding a Content-Format option.

        *Values:*

        enumerator COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN = 0
        :   text/plain;charset=utf-8

        enumerator COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT = 40
        :   application/link-format

        enumerator COAP\_CONTENT\_FORMAT\_APP\_XML = 41
        :   application/xml

        enumerator COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM = 42
        :   application/octet-stream

        enumerator COAP\_CONTENT\_FORMAT\_APP\_EXI = 47
        :   application/exi

        enumerator COAP\_CONTENT\_FORMAT\_APP\_JSON = 50
        :   application/json

        enumerator COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON = 51
        :   application/json-patch+json

        enumerator COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON = 52
        :   application/merge-patch+json

        enumerator COAP\_CONTENT\_FORMAT\_APP\_CBOR = 60
        :   application/cbor

    enum coap\_block\_size
    :   Represents the size of each block that will be transferred using block-wise transfers [RFC7959]:

        Each entry maps directly to the value that is used in the wire.

        [https://tools.ietf.org/html/rfc7959](https://tools.ietf.org/html/rfc7959)

        *Values:*

        enumerator COAP\_BLOCK\_16
        :   16-byte block size

        enumerator COAP\_BLOCK\_32
        :   32-byte block size

        enumerator COAP\_BLOCK\_64
        :   64-byte block size

        enumerator COAP\_BLOCK\_128
        :   128-byte block size

        enumerator COAP\_BLOCK\_256
        :   256-byte block size

        enumerator COAP\_BLOCK\_512
        :   512-byte block size

        enumerator COAP\_BLOCK\_1024
        :   1024-byte block size

    Functions

    uint8\_t coap\_header\_get\_version(const struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Returns the version present in a CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation

        Returns:
        :   the CoAP version in packet

    uint8\_t coap\_header\_get\_type(const struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Returns the type of the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation

        Returns:
        :   the type of the packet

    uint8\_t coap\_header\_get\_token(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint8\_t \*token)
    :   Returns the token (if any) in the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation
            - **token** – Where to store the token, must point to a buffer containing at least COAP\_TOKEN\_MAX\_LEN bytes

        Returns:
        :   Token length in the CoAP packet (0 - COAP\_TOKEN\_MAX\_LEN).

    uint8\_t coap\_header\_get\_code(const struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Returns the code of the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation

        Returns:
        :   the code present in the packet

    int coap\_header\_set\_code(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint8\_t code)
    :   Modifies the code of the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation
            - **code** – CoAP code

        Returns:
        :   0 on success, -EINVAL on failure

    uint16\_t coap\_header\_get\_id(const struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Returns the message id associated with the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation

        Returns:
        :   the message id present in the packet

    const uint8\_t \*coap\_packet\_get\_payload(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t \*len)
    :   Returns the data pointer and length of the CoAP packet.

        Parameters:
        :   - **cpkt** – CoAP packet representation
            - **len** – Total length of CoAP payload

        Returns:
        :   data pointer and length if payload exists NULL pointer and length set to 0 in case there is no payload

    bool coap\_uri\_path\_match(const char \*const \*path, struct [coap\_option](#c.coap_option) \*options, uint8\_t opt\_num)
    :   Verify if CoAP URI path matches with provided options.

        Parameters:
        :   - **path** – Null-terminated array of strings.
            - **options** – Parsed options from [coap\_packet\_parse()](#group__coap_1ga27a58a69f632551aa7a2394ae2badacf)
            - **opt\_num** – Number of options

        Returns:
        :   true if the CoAP URI path matches, false otherwise.

    int coap\_packet\_parse(struct [coap\_packet](#c.coap_packet) \*cpkt, uint8\_t \*data, uint16\_t len, struct [coap\_option](#c.coap_option) \*options, uint8\_t opt\_num)
    :   Parses the CoAP packet in data, validating it and initializing *cpkt*.

        *data* must remain valid while *cpkt* is used.

        Parameters:
        :   - **cpkt** – Packet to be initialized from received *data*.
            - **data** – Data containing a CoAP packet, its *data* pointer is positioned on the start of the CoAP packet.
            - **len** – Length of the data
            - **options** – Parse options and cache its details.
            - **opt\_num** – Number of options

        Return values:
        :   - **0** – in case of success.
            - **-EINVAL** – in case of invalid input args.
            - **-EBADMSG** – in case of malformed coap packet header.
            - **-EILSEQ** – in case of malformed coap options.

    int coap\_packet\_set\_path(struct [coap\_packet](#c.coap_packet) \*cpkt, const char \*path)
    :   Parses provided coap path (with/without query) or query and appends that as options to the *cpkt*.

        Parameters:
        :   - **cpkt** – Packet to append path and query options for.
            - **path** – Null-terminated string of coap path, query or both.

        Return values:
        :   **0** – in case of success or negative in case of error.

    int coap\_packet\_init(struct [coap\_packet](#c.coap_packet) \*cpkt, uint8\_t \*data, uint16\_t max\_len, uint8\_t ver, uint8\_t type, uint8\_t token\_len, const uint8\_t \*token, uint8\_t code, uint16\_t id)
    :   Creates a new CoAP Packet from input data.

        Parameters:
        :   - **cpkt** – New packet to be initialized using the storage from *data*.
            - **data** – Data that will contain a CoAP packet information
            - **max\_len** – Maximum allowable length of data
            - **ver** – CoAP header version
            - **type** – CoAP header type
            - **token\_len** – CoAP header token length
            - **token** – CoAP header token
            - **code** – CoAP header code
            - **id** – CoAP header message id

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_ack\_init(struct [coap\_packet](#c.coap_packet) \*cpkt, const struct [coap\_packet](#c.coap_packet) \*req, uint8\_t \*data, uint16\_t max\_len, uint8\_t code)
    :   Create a new CoAP Acknowledgment message for given request.

        This function works like [coap\_packet\_init](#group__coap_1ga90e6aab174f8977f0a3b5fbe1a20297c), filling CoAP header type, CoAP header token, and CoAP header message id fields according to acknowledgment rules.

        Parameters:
        :   - **cpkt** – New packet to be initialized using the storage from *data*.
            - **req** – CoAP request packet that is being acknowledged
            - **data** – Data that will contain a CoAP packet information
            - **max\_len** – Maximum allowable length of data
            - **code** – CoAP header code

        Returns:
        :   0 in case of success or negative in case of error.

    uint8\_t \*coap\_next\_token(void)
    :   Returns a randomly generated array of 8 bytes, that can be used as a message’s token.

        Returns:
        :   a 8-byte pseudo-random token.

    uint16\_t coap\_next\_id(void)
    :   Helper to generate message ids.

        Returns:
        :   a new message id

    int coap\_find\_options(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t code, struct [coap\_option](#c.coap_option) \*options, uint16\_t veclen)
    :   Return the values associated with the option of value *code*.

        Parameters:
        :   - **cpkt** – CoAP packet representation
            - **code** – Option number to look for
            - **options** – Array of [coap\_option](#structcoap__option) where to store the value of the options found
            - **veclen** – Number of elements in the options array

        Returns:
        :   The number of options found in packet matching code, negative on error.

    int coap\_packet\_append\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t code, const uint8\_t \*value, uint16\_t len)
    :   Appends an option to the packet.

        Note: options can be added out of numeric order of their codes. But it’s more efficient to add them in order.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **code** – Option code to add to the packet, see [coap\_option\_num](#group__coap_1ga7b8b3041e2f4ae26e663ff7431a6e6e3)
            - **value** – Pointer to the value of the option, will be copied to the packet
            - **len** – Size of the data to be added

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_packet\_remove\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t code)
    :   Remove an option from the packet.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **code** – Option code to remove from the packet, see [coap\_option\_num](#group__coap_1ga7b8b3041e2f4ae26e663ff7431a6e6e3)

        Returns:
        :   0 in case of success or negative in case of error.

    unsigned int coap\_option\_value\_to\_int(const struct [coap\_option](#c.coap_option) \*option)
    :   Converts an option to its integer representation.

        Assumes that the number is encoded in the network byte order in the option.

        Parameters:
        :   - **option** – Pointer to the option value, retrieved by [coap\_find\_options()](#group__coap_1gaf006c8048ed7b863e70dbdd64bc3d608)

        Returns:
        :   The integer representation of the option

    int coap\_append\_option\_int(struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t code, unsigned int val)
    :   Appends an integer value option to the packet.

        The option must be added in numeric order of their codes, and the least amount of bytes will be used to encode the value.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **code** – Option code to add to the packet, see [coap\_option\_num](#group__coap_1ga7b8b3041e2f4ae26e663ff7431a6e6e3)
            - **val** – Integer value to be added

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_packet\_append\_payload\_marker(struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Append payload marker to CoAP packet.

        Parameters:
        :   - **cpkt** – Packet to append the payload marker (0xFF)

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_packet\_append\_payload(struct [coap\_packet](#c.coap_packet) \*cpkt, const uint8\_t \*payload, uint16\_t payload\_len)
    :   Append payload to CoAP packet.

        Parameters:
        :   - **cpkt** – Packet to append the payload
            - **payload** – CoAP packet payload
            - **payload\_len** – CoAP packet payload len

        Returns:
        :   0 in case of success or negative in case of error.

    bool coap\_packet\_is\_request(const struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Check if a CoAP packet is a CoAP request.

        Parameters:
        :   - **cpkt** – Packet to be checked.

        Returns:
        :   true if the packet is a request, false otherwise.

    int coap\_handle\_request\_len(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_resource](#c.coap_resource) \*resources, size\_t resources\_len, struct [coap\_option](#c.coap_option) \*options, uint8\_t opt\_num, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len)
    :   When a request is received, call the appropriate methods of the matching resources.

        Parameters:
        :   - **cpkt** – Packet received
            - **resources** – Array of known resources
            - **resources\_len** – Number of resources in the array
            - **options** – Parsed options from [coap\_packet\_parse()](#group__coap_1ga27a58a69f632551aa7a2394ae2badacf)
            - **opt\_num** – Number of options
            - **addr** – Peer address
            - **addr\_len** – Peer address length

        Return values:
        :   - **>=** – 0 in case of success.
            - **-ENOTSUP** – in case of invalid request code.
            - **-EPERM** – in case resource handler is not implemented.
            - **-ENOENT** – in case the resource is not found.

    int coap\_handle\_request(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_resource](#c.coap_resource) \*resources, struct [coap\_option](#c.coap_option) \*options, uint8\_t opt\_num, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len)
    :   When a request is received, call the appropriate methods of the matching resources.

        Parameters:
        :   - **cpkt** – Packet received
            - **resources** – Array of known resources (terminated with empty resource)
            - **options** – Parsed options from [coap\_packet\_parse()](#group__coap_1ga27a58a69f632551aa7a2394ae2badacf)
            - **opt\_num** – Number of options
            - **addr** – Peer address
            - **addr\_len** – Peer address length

        Return values:
        :   - **>=** – 0 in case of success.
            - **-ENOTSUP** – in case of invalid request code.
            - **-EPERM** – in case resource handler is not implemented.
            - **-ENOENT** – in case the resource is not found.

    static inline uint16\_t coap\_block\_size\_to\_bytes(enum [coap\_block\_size](#c.coap_block_size) block\_size)
    :   Helper for converting the enumeration to the size expressed in bytes.

        Parameters:
        :   - **block\_size** – The block size to be converted

        Returns:
        :   The size in bytes that the block\_size represents

    static inline enum [coap\_block\_size](#c.coap_block_size) coap\_bytes\_to\_block\_size(uint16\_t bytes)
    :   Helper for converting block size in bytes to enumeration.

        NOTE: Only valid CoAP block sizes map correctly.

        Parameters:
        :   - **bytes** – CoAP block size in bytes.

        Returns:
        :   enum [coap\_block\_size](#group__coap_1ga712c1468f936a3af7dc39a86a5961922)

    int coap\_block\_transfer\_init(struct [coap\_block\_context](#c.coap_block_context) \*ctx, enum [coap\_block\_size](#c.coap_block_size) block\_size, size\_t total\_size)
    :   Initializes the context of a block-wise transfer.

        Parameters:
        :   - **ctx** – The context to be initialized
            - **block\_size** – The size of the block
            - **total\_size** – The total size of the transfer, if known

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_append\_descriptive\_block\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Append BLOCK1 or BLOCK2 option to the packet.

        If the CoAP packet is a request then BLOCK1 is appended otherwise BLOCK2 is appended.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **ctx** – Block context from which to retrieve the information for the block option

        Returns:
        :   0 in case of success or negative in case of error.

    bool coap\_has\_descriptive\_block\_option(struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Check if a descriptive block option is set in the packet.

        If the CoAP packet is a request then an available BLOCK1 option would be checked otherwise a BLOCK2 option would be checked.

        Parameters:
        :   - **cpkt** – Packet to be checked.

        Returns:
        :   true if the corresponding block option is set, false otherwise.

    int coap\_remove\_descriptive\_block\_option(struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Remove BLOCK1 or BLOCK2 option from the packet.

        If the CoAP packet is a request then BLOCK1 is removed otherwise BLOCK2 is removed.

        Parameters:
        :   - **cpkt** – Packet to be updated.

        Returns:
        :   0 in case of success or negative in case of error.

    bool coap\_block\_has\_more(struct [coap\_packet](#c.coap_packet) \*cpkt)
    :   Check if BLOCK1 or BLOCK2 option has more flag set.

        Parameters:
        :   - **cpkt** – Packet to be checked.

        Returns:
        :   true If more flag is set in BLOCK1 or BLOCK2

        Returns:
        :   false If MORE flag is not set or BLOCK header not found.

    int coap\_append\_block1\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Append BLOCK1 option to the packet.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **ctx** – Block context from which to retrieve the information for the Block1 option

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_append\_block2\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Append BLOCK2 option to the packet.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **ctx** – Block context from which to retrieve the information for the Block2 option

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_append\_size1\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Append SIZE1 option to the packet.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **ctx** – Block context from which to retrieve the information for the Size1 option

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_append\_size2\_option(struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Append SIZE2 option to the packet.

        Parameters:
        :   - **cpkt** – Packet to be updated
            - **ctx** – Block context from which to retrieve the information for the Size2 option

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_get\_option\_int(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint16\_t code)
    :   Get the integer representation of a CoAP option.

        Parameters:
        :   - **cpkt** – Packet to be inspected
            - **code** – CoAP option code

        Returns:
        :   Integer value >= 0 in case of success or negative in case of error.

    int coap\_get\_block1\_option(const struct [coap\_packet](#c.coap_packet) \*cpkt, bool \*has\_more, uint8\_t \*block\_number)
    :   Get the block size, more flag and block number from the CoAP block1 option.

        Parameters:
        :   - **cpkt** – Packet to be inspected
            - **has\_more** – Is set to the value of the more flag
            - **block\_number** – Is set to the number of the block

        Returns:
        :   Integer value of the block size in case of success or negative in case of error.

    int coap\_get\_block2\_option(const struct [coap\_packet](#c.coap_packet) \*cpkt, uint8\_t \*block\_number)
    :   Get values from CoAP block2 option.

        Decode block number and block size from option. Ignore the has\_more flag as it should always be zero on queries.

        Parameters:
        :   - **cpkt** – Packet to be inspected
            - **block\_number** – Is set to the number of the block

        Returns:
        :   Integer value of the block size in case of success or negative in case of error.

    int coap\_update\_from\_block(const struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Retrieves BLOCK{1,2} and SIZE{1,2} from *cpkt* and updates *ctx* accordingly.

        Parameters:
        :   - **cpkt** – Packet in which to look for block-wise transfers options
            - **ctx** – Block context to be updated

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_next\_block\_for\_option(const struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx, enum [coap\_option\_num](#c.coap_option_num) option)
    :   Updates *ctx* according to *option* set in *cpkt* so after this is called the current entry indicates the correct offset in the body of data being transferred.

        Parameters:
        :   - **cpkt** – Packet in which to look for block-wise transfers options
            - **ctx** – Block context to be updated
            - **option** – Either COAP\_OPTION\_BLOCK1 or COAP\_OPTION\_BLOCK2

        Returns:
        :   The offset in the block-wise transfer, 0 if the transfer has finished or a negative value in case of an error.

    size\_t coap\_next\_block(const struct [coap\_packet](#c.coap_packet) \*cpkt, struct [coap\_block\_context](#c.coap_block_context) \*ctx)
    :   Updates *ctx* so after this is called the current entry indicates the correct offset in the body of data being transferred.

        Parameters:
        :   - **cpkt** – Packet in which to look for block-wise transfers options
            - **ctx** – Block context to be updated

        Returns:
        :   The offset in the block-wise transfer, 0 if the transfer has finished.

    void coap\_observer\_init(struct [coap\_observer](#c.coap_observer) \*observer, const struct [coap\_packet](#c.coap_packet) \*request, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr)
    :   Indicates that the remote device referenced by *addr*, with *request*, wants to observe a resource.

        Parameters:
        :   - **observer** – Observer to be initialized
            - **request** – Request on which the observer will be based
            - **addr** – Address of the remote device

    bool coap\_register\_observer(struct [coap\_resource](#c.coap_resource) \*resource, struct [coap\_observer](#c.coap_observer) \*observer)
    :   After the observer is initialized, associate the observer with an resource.

        Parameters:
        :   - **resource** – Resource to add an observer
            - **observer** – Observer to be added

        Returns:
        :   true if this is the first observer added to this resource.

    bool coap\_remove\_observer(struct [coap\_resource](#c.coap_resource) \*resource, struct [coap\_observer](#c.coap_observer) \*observer)
    :   Remove this observer from the list of registered observers of that resource.

        Parameters:
        :   - **resource** – Resource in which to remove the observer
            - **observer** – Observer to be removed

        Returns:
        :   true if the observer was found and removed.

    struct [coap\_observer](#c.coap_observer) \*coap\_find\_observer(struct [coap\_observer](#c.coap_observer) \*observers, size\_t len, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, const uint8\_t \*token, uint8\_t token\_len)
    :   Returns the observer that matches address *addr* and has token *token*.

        Parameters:
        :   - **observers** – Pointer to the array of observers
            - **len** – Size of the array of observers
            - **addr** – Address of the endpoint observing a resource
            - **token** – Pointer to the token
            - **token\_len** – Length of valid bytes in the token

        Returns:
        :   A pointer to a observer if a match is found, NULL otherwise.

    struct [coap\_observer](#c.coap_observer) \*coap\_find\_observer\_by\_addr(struct [coap\_observer](#c.coap_observer) \*observers, size\_t len, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr)
    :   Returns the observer that matches address *addr*.

        Note

        The function [coap\_find\_observer()](#group__coap_1gaf9c1a55aee52588df2694ea947db5db4) should be preferred if both the observer’s address and token are known.

        Parameters:
        :   - **observers** – Pointer to the array of observers
            - **len** – Size of the array of observers
            - **addr** – Address of the endpoint observing a resource

        Returns:
        :   A pointer to a observer if a match is found, NULL otherwise.

    struct [coap\_observer](#c.coap_observer) \*coap\_find\_observer\_by\_token(struct [coap\_observer](#c.coap_observer) \*observers, size\_t len, const uint8\_t \*token, uint8\_t token\_len)
    :   Returns the observer that has token *token*.

        Note

        The function [coap\_find\_observer()](#group__coap_1gaf9c1a55aee52588df2694ea947db5db4) should be preferred if both the observer’s address and token are known.

        Parameters:
        :   - **observers** – Pointer to the array of observers
            - **len** – Size of the array of observers
            - **token** – Pointer to the token
            - **token\_len** – Length of valid bytes in the token

        Returns:
        :   A pointer to a observer if a match is found, NULL otherwise.

    struct [coap\_observer](#c.coap_observer) \*coap\_observer\_next\_unused(struct [coap\_observer](#c.coap_observer) \*observers, size\_t len)
    :   Returns the next available observer representation.

        Parameters:
        :   - **observers** – Pointer to the array of observers
            - **len** – Size of the array of observers

        Returns:
        :   A pointer to a observer if there’s an available observer, NULL otherwise.

    void coap\_reply\_init(struct [coap\_reply](#c.coap_reply) \*reply, const struct [coap\_packet](#c.coap_packet) \*request)
    :   Indicates that a reply is expected for *request*.

        Parameters:
        :   - **reply** – Reply structure to be initialized
            - **request** – Request from which *reply* will be based

    int coap\_pending\_init(struct [coap\_pending](#c.coap_pending) \*pending, const struct [coap\_packet](#c.coap_packet) \*request, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, const struct [coap\_transmission\_parameters](#c.coap_transmission_parameters) \*params)
    :   Initialize a pending request with a request.

        The request’s fields are copied into the pending struct, so *request* doesn’t have to live for as long as the pending struct lives, but “data” that needs to live for at least that long.

        Parameters:
        :   - **pending** – Structure representing the waiting for a confirmation message, initialized with data from *request*
            - **request** – Message waiting for confirmation
            - **addr** – Address to send the retransmission
            - **params** – Pointer to the CoAP transmission parameters struct, or NULL to use default values

        Returns:
        :   0 in case of success or negative in case of error.

    struct [coap\_pending](#c.coap_pending) \*coap\_pending\_next\_unused(struct [coap\_pending](#c.coap_pending) \*pendings, size\_t len)
    :   Returns the next available pending struct, that can be used to track the retransmission status of a request.

        Parameters:
        :   - **pendings** – Pointer to the array of [coap\_pending](#structcoap__pending) structures
            - **len** – Size of the array of [coap\_pending](#structcoap__pending) structures

        Returns:
        :   pointer to a free [coap\_pending](#structcoap__pending) structure, NULL in case none could be found.

    struct [coap\_reply](#c.coap_reply) \*coap\_reply\_next\_unused(struct [coap\_reply](#c.coap_reply) \*replies, size\_t len)
    :   Returns the next available reply struct, so it can be used to track replies and notifications received.

        Parameters:
        :   - **replies** – Pointer to the array of [coap\_reply](#structcoap__reply) structures
            - **len** – Size of the array of [coap\_reply](#structcoap__reply) structures

        Returns:
        :   pointer to a free [coap\_reply](#structcoap__reply) structure, NULL in case none could be found.

    struct [coap\_pending](#c.coap_pending) \*coap\_pending\_received(const struct [coap\_packet](#c.coap_packet) \*response, struct [coap\_pending](#c.coap_pending) \*pendings, size\_t len)
    :   After a response is received, returns if there is any matching pending request exits.

        User has to clear all pending retransmissions related to that response by calling [coap\_pending\_clear()](#group__coap_1ga03287eb3187aa28e0e83e0e0c72e2631).

        Parameters:
        :   - **response** – The received response
            - **pendings** – Pointer to the array of [coap\_reply](#structcoap__reply) structures
            - **len** – Size of the array of [coap\_reply](#structcoap__reply) structures

        Returns:
        :   pointer to the associated [coap\_pending](#structcoap__pending) structure, NULL in case none could be found.

    struct [coap\_reply](#c.coap_reply) \*coap\_response\_received(const struct [coap\_packet](#c.coap_packet) \*response, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*from, struct [coap\_reply](#c.coap_reply) \*replies, size\_t len)
    :   After a response is received, call [coap\_reply\_t](#group__coap_1ga556deaf757f3047eefc2f032d0d7e0bc) handler registered in [coap\_reply](#structcoap__reply) structure.

        Parameters:
        :   - **response** – A response received
            - **from** – Address from which the response was received
            - **replies** – Pointer to the array of [coap\_reply](#structcoap__reply) structures
            - **len** – Size of the array of [coap\_reply](#structcoap__reply) structures

        Returns:
        :   Pointer to the reply matching the packet received, NULL if none could be found.

    struct [coap\_pending](#c.coap_pending) \*coap\_pending\_next\_to\_expire(struct [coap\_pending](#c.coap_pending) \*pendings, size\_t len)
    :   Returns the next pending about to expire, pending->timeout informs how many ms to next expiration.

        Parameters:
        :   - **pendings** – Pointer to the array of [coap\_pending](#structcoap__pending) structures
            - **len** – Size of the array of [coap\_pending](#structcoap__pending) structures

        Returns:
        :   The next [coap\_pending](#structcoap__pending) to expire, NULL if none is about to expire.

    bool coap\_pending\_cycle(struct [coap\_pending](#c.coap_pending) \*pending)
    :   After a request is sent, user may want to cycle the pending retransmission so the timeout is updated.

        Parameters:
        :   - **pending** – Pending representation to have its timeout updated

        Returns:
        :   false if this is the last retransmission.

    void coap\_pending\_clear(struct [coap\_pending](#c.coap_pending) \*pending)
    :   Cancels the pending retransmission, so it again becomes available.

        Parameters:
        :   - **pending** – Pending representation to be canceled

    void coap\_pendings\_clear(struct [coap\_pending](#c.coap_pending) \*pendings, size\_t len)
    :   Cancels all pending retransmissions, so they become available again.

        Parameters:
        :   - **pendings** – Pointer to the array of [coap\_pending](#structcoap__pending) structures
            - **len** – Size of the array of [coap\_pending](#structcoap__pending) structures

    size\_t coap\_pendings\_count(struct [coap\_pending](#c.coap_pending) \*pendings, size\_t len)
    :   Count number of pending requests.

        Parameters:
        :   - **len** – Number of elements in array.
            - **pendings** – Array of pending requests.

        Returns:
        :   count of elements where timeout is not zero.

    void coap\_reply\_clear(struct [coap\_reply](#c.coap_reply) \*reply)
    :   Cancels awaiting for this reply, so it becomes available again.

        User responsibility to free the memory associated with data.

        Parameters:
        :   - **reply** – The reply to be canceled

    void coap\_replies\_clear(struct [coap\_reply](#c.coap_reply) \*replies, size\_t len)
    :   Cancels all replies, so they become available again.

        Parameters:
        :   - **replies** – Pointer to the array of [coap\_reply](#structcoap__reply) structures
            - **len** – Size of the array of [coap\_reply](#structcoap__reply) structures

    int coap\_resource\_notify(struct [coap\_resource](#c.coap_resource) \*resource)
    :   Indicates that this resource was updated and that the *notify* callback should be called for every registered observer.

        Parameters:
        :   - **resource** – Resource that was updated

        Returns:
        :   0 in case of success or negative in case of error.

    bool coap\_request\_is\_observe(const struct [coap\_packet](#c.coap_packet) \*request)
    :   Returns if this request is enabling observing a resource.

        Parameters:
        :   - **request** – Request to be checked

        Returns:
        :   True if the request is enabling observing a resource, False otherwise

    struct [coap\_transmission\_parameters](#c.coap_transmission_parameters) coap\_get\_transmission\_parameters(void)
    :   Get currently active CoAP transmission parameters.

        Returns:
        :   CoAP transmission parameters structure.

    void coap\_set\_transmission\_parameters(const struct [coap\_transmission\_parameters](#c.coap_transmission_parameters) \*params)
    :   Set CoAP transmission parameters.

        Parameters:
        :   - **params** – Pointer to the transmission parameters structure.

    int coap\_well\_known\_core\_get(struct [coap\_resource](#c.coap_resource) \*resource, const struct [coap\_packet](#c.coap_packet) \*request, struct [coap\_packet](#c.coap_packet) \*response, uint8\_t \*data, uint16\_t data\_len)
    :   Build a CoAP response for a .well-known/core CoAP request.

        Parameters:
        :   - **resource** – Array of known resources, terminated with an empty resource
            - **request** – A pointer to the .well-known/core CoAP request
            - **response** – A pointer to a CoAP response, will be initialized
            - **data** – A data pointer to be used to build the CoAP response
            - **data\_len** – The maximum length of the data buffer

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_well\_known\_core\_get\_len(struct [coap\_resource](#c.coap_resource) \*resources, size\_t resources\_len, const struct [coap\_packet](#c.coap_packet) \*request, struct [coap\_packet](#c.coap_packet) \*response, uint8\_t \*data, uint16\_t data\_len)
    :   Build a CoAP response for a .well-known/core CoAP request.

        Parameters:
        :   - **resources** – Array of known resources
            - **resources\_len** – Number of resources in the array
            - **request** – A pointer to the .well-known/core CoAP request
            - **response** – A pointer to a CoAP response, will be initialized
            - **data** – A data pointer to be used to build the CoAP response
            - **data\_len** – The maximum length of the data buffer

        Returns:
        :   0 in case of success or negative in case of error.

    struct coap\_resource
    :   *#include <coap.h>*

        Description of CoAP resource.

        CoAP servers often want to register resources, so that clients can act on them, by fetching their state or requesting updates to them.

        Public Members

        [coap\_method\_t](#c.coap_method_t) get
        :   Which function to be called for each CoAP method.

        [coap\_notify\_t](#c.coap_notify_t) notify
        :   Notify function to call.

        const char \*const \*path
        :   Resource path.

        void \*user\_data
        :   User specific opaque data.

        [sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") observers
        :   List of resource observers.

        int age
        :   Resource age.

    struct coap\_observer
    :   *#include <coap.h>*

        Represents a remote device that is observing a local resource.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") list
        :   Observer list node.

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") addr
        :   Observer connection end point information.

        uint8\_t token[8]
        :   Observer token.

        uint8\_t tkl
        :   Extended token length.

    struct coap\_packet
    :   *#include <coap.h>*

        Representation of a CoAP Packet.

        Public Members

        uint8\_t \*data
        :   User allocated buffer.

        uint16\_t offset
        :   CoAP lib maintains offset while adding data.

        uint16\_t max\_len
        :   Max CoAP packet data length.

        uint8\_t hdr\_len
        :   CoAP header length.

        uint16\_t opt\_len
        :   Total options length (delta + len + value).

        uint16\_t delta
        :   Used for delta calculation in CoAP packet.

    struct coap\_option
    :   *#include <coap.h>*

        Representation of a CoAP option.

        Public Members

        uint16\_t delta
        :   Option delta.

        uint8\_t len
        :   Option length.

        uint8\_t value[12]
        :   Option value.

    struct coap\_transmission\_parameters
    :   *#include <coap.h>*

        CoAP transmission parameters.

        Public Members

        uint32\_t ack\_timeout
        :   Initial ACK timeout.

            Value is used as a base value to retry pending CoAP packets.

        uint16\_t coap\_backoff\_percent
        :   Set CoAP retry backoff factor.

            A value of 200 means a factor of 2.0.

        uint8\_t max\_retransmission
        :   Maximum number of retransmissions.

    struct coap\_pending
    :   *#include <coap.h>*

        Represents a request awaiting for an acknowledgment (ACK).

        Public Members

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") addr
        :   Remote address.

        int64\_t t0
        :   Time when the request was sent.

        uint32\_t timeout
        :   Timeout in ms.

        uint16\_t id
        :   Message id.

        uint8\_t \*data
        :   User allocated buffer.

        uint16\_t len
        :   Length of the CoAP packet.

        uint8\_t retries
        :   Number of times the request has been sent.

        struct [coap\_transmission\_parameters](#c.coap_transmission_parameters) params
        :   Transmission parameters.

    struct coap\_reply
    :   *#include <coap.h>*

        Represents the handler for the reply of a request, it is also used when observing resources.

        Public Members

        [coap\_reply\_t](#c.coap_reply_t) reply
        :   CoAP reply callback.

        void \*user\_data
        :   User specific opaque data.

        int age
        :   Reply age.

        uint16\_t id
        :   Reply id.

        uint8\_t token[8]
        :   Reply token.

        uint8\_t tkl
        :   Extended token length.

    struct coap\_block\_context
    :   *#include <coap.h>*

        Represents the current state of a block-wise transaction.

        Public Members

        size\_t total\_size
        :   Total size of the block-wise transaction.

        size\_t current
        :   Current size of the block-wise transaction.

        enum [coap\_block\_size](#c.coap_block_size) block\_size
        :   Block size.

    struct coap\_core\_metadata
    :   *#include <coap\_link\_format.h>*

        In case you want to add attributes to the resources included in the ‘well-known/core’ “virtual” resource, the ‘user\_data’ field should point to a valid [coap\_core\_metadata](#structcoap__core__metadata) structure.

        Public Members

        const char \*const \*attributes
        :   List of attributes to add.

        void \*user\_data
        :   User specific data.
