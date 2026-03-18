---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/http_server.html
original_path: connectivity/networking/api/http_server.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# HTTP Server

## [Overview](#id5)

Zephyr provides an HTTP server library, which allows to register HTTP services
and HTTP resources associated with those services. The server creates a listening
socket for every registered service, and handles incoming client connections.
It’s possible to communicate over a plain TCP socket (HTTP) or a TLS socket (HTTPS).
Both, HTTP/1.1 (RFC 2616) and HTTP/2 (RFC 9113) protocol versions are supported.

The server operation is generally transparent for the application, running in a
background thread. The application can control the server activity with
respective API functions.

Certain resource types (for example dynamic resource) provide resource-specific
application callbacks, allowing the server to interact with the application (for
instance provide resource content, or process request payload).

Currently, the following resource types are supported:

- Static resources - content defined compile-time, cannot be modified at runtime
  ([`HTTP_RESOURCE_TYPE_STATIC`](#c.http_resource_type.HTTP_RESOURCE_TYPE_STATIC)).
- Dynamic resources - content provided at runtime by respective application
  callback ([`HTTP_RESOURCE_TYPE_DYNAMIC`](#c.http_resource_type.HTTP_RESOURCE_TYPE_DYNAMIC)).
- Websocket resources - allowing to establish Websocket connections with the
  server ([`HTTP_RESOURCE_TYPE_WEBSOCKET`](#c.http_resource_type.HTTP_RESOURCE_TYPE_WEBSOCKET)).

Zephyr provides a sample demonstrating HTTP(s) server operation and various
resource types usage. See [HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.") for more
information.

## [Server Setup](#id6)

A few prerequisites are needed in order to enable HTTP server functionality in
the application.

First of all, the HTTP server has to be enabled in applications configuration file
with [`CONFIG_HTTP_SERVER`](../../../kconfig.md#CONFIG_HTTP_SERVER "CONFIG_HTTP_SERVER") Kconfig option:

`prj.conf`

```cfg
CONFIG_HTTP_SERVER=y
```

All HTTP services and HTTP resources are placed in a dedicated linker section.
The linker section for services is predefined locally, however the application
is responsible for defining linker sections for resources associated with
respective services. Linker section names for resources should be prefixed with
`http_resource_desc_`, appended with the service name.

Linker sections for resources should be defined in a linker file. For example,
for a service named `my_service`, the linker section shall be defined as follows:

`sections-rom.ld`

```c
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_ROM(http_resource_desc_my_service, Z_LINK_ITERABLE_SUBALIGN)
```

Finally, the linker file and linker section have to be added to your application
using CMake:

`CMakeLists.txt`

```cmake
zephyr_linker_sources(SECTIONS sections-rom.ld)
zephyr_linker_section(NAME http_resource_desc_my_service
                      KVMA RAM_REGION GROUP RODATA_REGION
                      SUBALIGN Z_LINK_ITERABLE_SUBALIGN)
```

Note

You need to define a separate linker section for each HTTP service
registered in the system.

## [Sample Usage](#id7)

### [Services](#id8)

The application needs to define an HTTP service (or multiple services), with
the same name as used for the linker section with [`HTTP_SERVICE_DEFINE`](#c.HTTP_SERVICE_DEFINE)
macro:

```c
#include <zephyr/net/http/service.h>

static uint16_t http_service_port = 80;

HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10, NULL);
```

Alternatively, an HTTPS service can be defined with
[`HTTPS_SERVICE_DEFINE`](#c.HTTPS_SERVICE_DEFINE):

```c
#include <zephyr/net/http/service.h>
#include <zephyr/net/tls_credentials.h>

#define HTTP_SERVER_CERTIFICATE_TAG 1

static uint16_t https_service_port = 443;
static const sec_tag_t sec_tag_list[] = {
    HTTP_SERVER_CERTIFICATE_TAG,
};

HTTPS_SERVICE_DEFINE(my_service, "0.0.0.0", &https_service_port, 1, 10,
                     NULL, sec_tag_list, sizeof(sec_tag_list));
```

Note

HTTPS services rely on TLS credentials being registered in the system.
See [TLS credentials subsystem](sockets.md#sockets-tls-credentials-subsys) for information on how to
configure TLS credentials in the system.

Once HTTP(s) service is defined, resources can be registered for it with
[`HTTP_RESOURCE_DEFINE`](#c.HTTP_RESOURCE_DEFINE) macro.

Application can enable resource wildcard support by enabling
[`CONFIG_HTTP_SERVER_RESOURCE_WILDCARD`](../../../kconfig.md#CONFIG_HTTP_SERVER_RESOURCE_WILDCARD "CONFIG_HTTP_SERVER_RESOURCE_WILDCARD") option. When this
option is set, then it is possible to match several incoming HTTP requests
with just one resource handler. The [fnmatch()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fnmatch.html)
POSIX API function is used to match the pattern in the URL paths.

Example:

```c
HTTP_RESOURCE_DEFINE(my_resource, my_service, "/foo*", &resource_detail);
```

This would match all URLs that start with a string `foo`. See
[POSIX.2 chapter 2.13](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_13)
for pattern matching syntax description.

### [Static resources](#id9)

Static resource content is defined build-time and is immutable. The following
example shows how gzip compressed webpage can be defined as a static resource
in the application:

```c
static const uint8_t index_html_gz[] = {
    #include "index.html.gz.inc"
};

struct http_resource_detail_static index_html_gz_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_STATIC,
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
        .content_encoding = "gzip",
    },
    .static_data = index_html_gz,
    .static_data_len = sizeof(index_html_gz),
};

HTTP_RESOURCE_DEFINE(index_html_gz_resource, my_service, "/",
                     &index_html_gz_resource_detail);
```

The resource content and content encoding is application specific. For the above
example, a gzip compressed webpage can be generated during build, by adding the
following code to the application’s `CMakeLists.txt` file:

`CMakeLists.txt`

```cmake
set(gen_dir ${ZEPHYR_BINARY_DIR}/include/generated/)
set(source_file_index src/index.html)
generate_inc_file_for_target(app ${source_file_index} ${gen_dir}/index.html.gz.inc --gzip)
```

where `src/index.html` is the location of the webpage to be compressed.

### [Dynamic resources](#id10)

For dynamic resource, a resource callback is registered to exchange data between
the server and the application. The application defines a resource buffer used
to pass the request payload data from the server, and to provide response payload
to the server. The following example code shows how to register a dynamic resource
with a simple resource handler, which echoes received data back to the client:

```c
static uint8_t recv_buffer[1024];

static int dyn_handler(struct http_client_ctx *client,
                       enum http_data_status status, uint8_t *buffer,
                       size_t len, void *user_data)
{
#define MAX_TEMP_PRINT_LEN 32
    static char print_str[MAX_TEMP_PRINT_LEN];
    enum http_method method = client->method;
    static size_t processed;

    __ASSERT_NO_MSG(buffer != NULL);

    if (status == HTTP_SERVER_DATA_ABORTED) {
        LOG_DBG("Transaction aborted after %zd bytes.", processed);
        processed = 0;
        return 0;
    }

    processed += len;

    snprintf(print_str, sizeof(print_str), "%s received (%zd bytes)",
             http_method_str(method), len);
    LOG_HEXDUMP_DBG(buffer, len, print_str);

    if (status == HTTP_SERVER_DATA_FINAL) {
        LOG_DBG("All data received (%zd bytes).", processed);
        processed = 0;
    }

    /* This will echo data back to client as the buffer and recv_buffer
     * point to same area.
     */
    return len;
}

struct http_resource_detail_dynamic dyn_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_DYNAMIC,
        .bitmask_of_supported_http_methods =
            BIT(HTTP_GET) | BIT(HTTP_POST),
    },
    .cb = dyn_handler,
    .data_buffer = recv_buffer,
    .data_buffer_len = sizeof(recv_buffer),
    .user_data = NULL,
};

HTTP_RESOURCE_DEFINE(dyn_resource, my_service, "/dynamic",
                     &dyn_resource_detail);
```

The resource callback may be called multiple times for a single request, hence
the application should be able to keep track of the received data progress.

The `status` field informs the application about the progress in passing
request payload from the server to the application. As long as the status
reports [`HTTP_SERVER_DATA_MORE`](#c.http_data_status.HTTP_SERVER_DATA_MORE), the application should expect
more data to be provided in a consecutive callback calls.
Once all request payload has been passed to the application, the server reports
[`HTTP_SERVER_DATA_FINAL`](#c.http_data_status.HTTP_SERVER_DATA_FINAL) status. In case of communication errors
during request processing (for example client closed the connection before
complete payload has been received), the server reports
[`HTTP_SERVER_DATA_ABORTED`](#c.http_data_status.HTTP_SERVER_DATA_ABORTED). Either of the two events indicate that
the application shall reset any progress recorded for the resource, and await
a new request to come. The server guarantees that the resource can only be
accessed by single client at a time.

The resource callback returns the number of bytes to be replied in the response
payload to the server (provided in the resource data buffer). In case there is
no more data to be included in the response, the callback should return 0.

The server will call the resource callback until it provided all request data
to the application, and the application reports there is no more data to include
in the reply.

### [Websocket resources](#id11)

Websocket resources register an application callback, which is called when a
Websocket connection upgrade takes place. The callback is provided with a socket
descriptor corresponding to the underlying TCP/TLS connection. Once called,
the application takes full control over the socket, i. e. is responsible to
release it when done.

```c
static int ws_socket;
static uint8_t ws_recv_buffer[1024];

int ws_setup(int sock, void *user_data)
{
    ws_socket = sock;
    return 0;
}

struct http_resource_detail_websocket ws_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_WEBSOCKET,
        /* We need HTTP/1.1 Get method for upgrading */
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
    },
    .cb = ws_setup,
    .data_buffer = ws_recv_buffer,
    .data_buffer_len = sizeof(ws_recv_buffer),
    .user_data = NULL, /* Fill this for any user specific data */
};

HTTP_RESOURCE_DEFINE(ws_resource, my_service, "/", &ws_resource_detail);
```

The above minimalistic example shows how to register a Websocket resource with
a simple callback, used only to store the socket descriptor provided. Further
processing of the Websocket connection is application-specific, hence outside
of scope of this guide. See [HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.") for an
example Websocket-based echo service implementation.

## [API Reference](#id12)

Related code samples

[HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")
:   Implement an HTTP(s) Server demonstrating various resource types.

*group* HTTP service API
:   Defines

    HTTP\_RESOURCE\_DEFINE(\_name, \_service, \_resource, \_detail)
    :   Define a static HTTP resource.

        A static HTTP resource is one that is known prior to system initialization. In contrast, dynamic resources may be discovered upon system initialization. Dynamic resources may also be inserted, or removed by events originating internally or externally to the system at runtime.

        Note

        The `_resource` is the URL without the associated protocol, host, or URL parameters. E.g. the resource for `#param1=value1` would be `/bar/baz.html`. It is often referred to as the “path” of the URL. Every `(service, resource)` pair should be unique. The `_resource` must be non-NULL.

        Parameters:
        :   - **\_name** – Name of the resource.
            - **\_service** – Name of the associated service.
            - **\_resource** – Pathname-like string identifying the resource.
            - **\_detail** – Implementation-specific detail associated with the resource.

    HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail)
    :   Define an HTTP service without static resources.

        Note

        The `_host` parameter must be non-`NULL`. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.

        Note

        The `_port` parameter must be non-`NULL`. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

        Parameters:
        :   - **\_name** – Name of the service.
            - **\_host** – IP address or hostname associated with the service.
            - **\_port** – **[inout]** Pointer to port associated with the service.
            - **\_concurrent** – Maximum number of concurrent clients.
            - **\_backlog** – Maximum number queued connections.
            - **\_detail** – Implementation-specific detail associated with the service.

    HTTPS\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size)
    :   Define an HTTPS service without static resources.

        Note

        The `_host` parameter must be non-`NULL`. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.

        Note

        The `_port` parameter must be non-`NULL`. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

        Parameters:
        :   - **\_name** – Name of the service.
            - **\_host** – IP address or hostname associated with the service.
            - **\_port** – **[inout]** Pointer to port associated with the service.
            - **\_concurrent** – Maximum number of concurrent clients.
            - **\_backlog** – Maximum number queued connections.
            - **\_detail** – Implementation-specific detail associated with the service.
            - **\_sec\_tag\_list** – TLS security tag list used to setup a HTTPS socket.
            - **\_sec\_tag\_list\_size** – TLS security tag list size used to setup a HTTPS socket.

    HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail)
    :   Define an HTTP service with static resources.

        Note

        The `_host` parameter must be non-`NULL`. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.

        Note

        The `_port` parameter must be non-`NULL`. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

        Parameters:
        :   - **\_name** – Name of the service.
            - **\_host** – IP address or hostname associated with the service.
            - **\_port** – **[inout]** Pointer to port associated with the service.
            - **\_concurrent** – Maximum number of concurrent clients.
            - **\_backlog** – Maximum number queued connections.
            - **\_detail** – Implementation-specific detail associated with the service.

    HTTPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size)
    :   Define an HTTPS service with static resources.

        Note

        The `_host` parameter must be non-`NULL`. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.

        Note

        The `_port` parameter must be non-`NULL`. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

        Parameters:
        :   - **\_name** – Name of the service.
            - **\_host** – IP address or hostname associated with the service.
            - **\_port** – **[inout]** Pointer to port associated with the service.
            - **\_concurrent** – Maximum number of concurrent clients.
            - **\_backlog** – Maximum number queued connections.
            - **\_detail** – Implementation-specific detail associated with the service.
            - **\_sec\_tag\_list** – TLS security tag list used to setup a HTTPS socket.
            - **\_sec\_tag\_list\_size** – TLS security tag list size used to setup a HTTPS socket.

    HTTP\_SERVICE\_COUNT(\_dst)
    :   Count the number of HTTP services.

        Parameters:
        :   - **\_dst** – **[out]** Pointer to location where result is written.

    HTTP\_SERVICE\_RESOURCE\_COUNT(\_service)
    :   Count HTTP service static resources.

        Parameters:
        :   - **\_service** – Pointer to a service.

    HTTP\_SERVICE\_FOREACH(\_it)
    :   Iterate over all HTTP services.

        Parameters:
        :   - **\_it** – Name of http\_service\_desc iterator

    HTTP\_RESOURCE\_FOREACH(\_service, \_it)
    :   Iterate over static HTTP resources associated with a given `_service`.

        Note

        This macro requires that `_service` is defined with [HTTP\_SERVICE\_DEFINE](#group__http__service_1ga38d08c32ea0e082cb39ed2a8d1a3dcc3).

        Parameters:
        :   - **\_service** – Name of HTTP service
            - **\_it** – Name of iterator (of type [http\_resource\_desc](#structhttp__resource__desc))

    HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it)
    :   Iterate over all static resources associated with `_service` .

        Note

        This macro is suitable for a `_service` defined with either [HTTP\_SERVICE\_DEFINE](#group__http__service_1ga38d08c32ea0e082cb39ed2a8d1a3dcc3) or [HTTP\_SERVICE\_DEFINE\_EMPTY](#group__http__service_1gaa146bcb3349e5f476b520113f74969ab).

        Parameters:
        :   - **\_service** – Pointer to HTTP service
            - **\_it** – Name of iterator (of type [http\_resource\_desc](#structhttp__resource__desc))

    struct http\_resource\_desc
    :   *#include <service.h>*

        HTTP resource description.

        Public Members

        const char \*resource
        :   Resource name.

        void \*detail
        :   Detail associated with this resource.

Related code samples

[HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")
:   Implement an HTTP(s) Server demonstrating various resource types.

*group* HTTP server API
:   Typedefs

    typedef int (\*http\_resource\_dynamic\_cb\_t)(struct [http\_client\_ctx](#c.http_client_ctx) \*client, enum [http\_data\_status](#c.http_data_status) status, uint8\_t \*data\_buffer, size\_t data\_len, void \*user\_data)
    :   Callback used when data is received.

        Data to be sent to client can be specified.

        Param client:
        :   HTTP context information for this client connection.

        Param status:
        :   HTTP data status, indicate whether more data is expected or not.

        Param data\_buffer:
        :   Data received.

        Param data\_len:
        :   Amount of data received.

        Param user\_data:
        :   User specified data.

        Return:
        :   >0 amount of data to be sent to client, let server to call this function again when new data is received. 0 nothing to sent to client, close the connection <0 error, close the connection.

    typedef int (\*http\_resource\_websocket\_cb\_t)(int ws\_socket, void \*user\_data)
    :   Callback used when a Websocket connection is setup.

        The application will need to handle all functionality related to the connection like reading and writing websocket data, and closing the connection.

        Param ws\_socket:
        :   A socket for the Websocket data.

        Param user\_data:
        :   User specified data.

        Return:
        :   0 Accepting the connection, HTTP server library will no longer handle data to/from the socket and it is application responsibility to send and receive data to/from the supplied socket. <0 error, close the connection.

    Enums

    enum http\_resource\_type
    :   HTTP server resource type.

        *Values:*

        enumerator HTTP\_RESOURCE\_TYPE\_STATIC
        :   Static resource, cannot be modified on runtime.

        enumerator HTTP\_RESOURCE\_TYPE\_DYNAMIC
        :   Dynamic resource, server interacts with the application via registered [http\_resource\_dynamic\_cb\_t](#group__http__server_1gace7ba97c942714d81f47c7ba860a0de2).

        enumerator HTTP\_RESOURCE\_TYPE\_WEBSOCKET
        :   Websocket resource, application takes control over Websocket connection after and upgrade.

    enum http\_data\_status
    :   Indicates the status of the currently processed piece of data.

        *Values:*

        enumerator HTTP\_SERVER\_DATA\_ABORTED = -1
        :   Transaction aborted, data incomplete.

        enumerator HTTP\_SERVER\_DATA\_MORE = 0
        :   Transaction incomplete, more data expected.

        enumerator HTTP\_SERVER\_DATA\_FINAL = 1
        :   Final data fragment in current transaction.

    Functions

    int http\_server\_start(void)
    :   Start the HTTP2 server.

        The server runs in a background thread. Once started, the server will create a server socket for all HTTP services registered in the system and accept connections from clients (see [HTTP\_SERVICE\_DEFINE](#group__http__service_1ga38d08c32ea0e082cb39ed2a8d1a3dcc3)).

    int http\_server\_stop(void)
    :   Stop the HTTP2 server.

        All server sockets are closed and the server thread is suspended.

    struct http\_resource\_detail
    :   *#include <server.h>*

        Representation of a server resource, common for all resource types.

        Public Members

        uint32\_t bitmask\_of\_supported\_http\_methods
        :   Bitmask of supported HTTP methods (http\_method).

        enum [http\_resource\_type](#c.http_resource_type) type
        :   Resource type.

        int path\_len
        :   Length of the URL path.

        const char \*content\_encoding
        :   Content encoding of the resource.

        const char \*content\_type
        :   Content type of the resource.

    struct http\_resource\_detail\_static
    :   *#include <server.h>*

        Representation of a static server resource.

        Public Members

        struct [http\_resource\_detail](#c.http_resource_detail) common
        :   Common resource details.

        const void \*static\_data
        :   Content of the static resource.

        size\_t static\_data\_len
        :   Size of the static resource.

    struct http\_resource\_detail\_dynamic
    :   *#include <server.h>*

        Representation of a dynamic server resource.

        Public Members

        struct [http\_resource\_detail](#c.http_resource_detail) common
        :   Common resource details.

        [http\_resource\_dynamic\_cb\_t](#c.http_resource_dynamic_cb_t) cb
        :   Resource callback used by the server to interact with the application.

        uint8\_t \*data\_buffer
        :   Data buffer used to exchanged data between server and the, application.

        size\_t data\_buffer\_len
        :   Length of the data in the data buffer.

        struct [http\_client\_ctx](#c.http_client_ctx) \*holder
        :   A pointer to the client currently processing resource, used to prevent concurrent access to the resource from multiple clients.

        void \*user\_data
        :   A pointer to the user data registered by the application.

    struct http\_resource\_detail\_websocket
    :   *#include <server.h>*

        Representation of a websocket server resource.

        Public Members

        struct [http\_resource\_detail](#c.http_resource_detail) common
        :   Common resource details.

        int ws\_sock
        :   Websocket socket value.

        [http\_resource\_websocket\_cb\_t](#c.http_resource_websocket_cb_t) cb
        :   Resource callback used by the server to interact with the application.

        uint8\_t \*data\_buffer
        :   Data buffer used to exchanged data between server and the, application.

        size\_t data\_buffer\_len
        :   Length of the data in the data buffer.

        void \*user\_data
        :   A pointer to the user data registered by the application.

    struct http2\_stream\_ctx
    :   *#include <server.h>*

        HTTP/2 stream representation.

        Public Members

        int stream\_id
        :   Stream identifier.

        enum http2\_stream\_state stream\_state
        :   Stream state.

        int window\_size
        :   Stream-level window size.

        bool headers\_sent
        :   Flag indicating that headers were sent in the reply.

        bool end\_stream\_sent
        :   Flag indicating that END\_STREAM flag was sent.

    struct http2\_frame
    :   *#include <server.h>*

        HTTP/2 frame representation.

        Public Members

        uint32\_t length
        :   Frame payload length.

        uint32\_t stream\_identifier
        :   Stream ID the frame belongs to.

        uint8\_t type
        :   Frame type.

        uint8\_t flags
        :   Frame flags.

        uint8\_t padding\_len
        :   Frame padding length.

    struct http\_client\_ctx
    :   *#include <server.h>*

        Representation of an HTTP client connected to the server.

        Public Members

        int fd
        :   Socket descriptor associated with the server.

        unsigned char buffer[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE]
        :   Client data buffer.

        unsigned char \*cursor
        :   Cursor indicating currently processed byte.

        size\_t data\_len
        :   Data left to process in the buffer.

        int window\_size
        :   Connection-level window size.

        enum http\_server\_state server\_state
        :   Server state for the associated client.

        struct [http2\_frame](#c.http2_frame) current\_frame
        :   Currently processed HTTP/2 frame.

        struct [http\_resource\_detail](#c.http_resource_detail) \*current\_detail
        :   Currently processed resource detail.

        struct [http2\_stream\_ctx](#c.http2_stream_ctx) \*current\_stream
        :   Currently processed stream.

        struct http\_hpack\_header\_buf header\_field
        :   HTTP/2 header parser context.

        struct [http2\_stream\_ctx](#c.http2_stream_ctx) streams[HTTP\_SERVER\_MAX\_STREAMS]
        :   HTTP/2 streams context.

        struct http\_parser\_settings parser\_settings
        :   HTTP/1 parser configuration.

        struct http\_parser parser
        :   HTTP/1 parser context.

        unsigned char url\_buffer[HTTP\_SERVER\_MAX\_URL\_LENGTH]
        :   Request URL.

        unsigned char content\_type[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN]
        :   Request content type.

        unsigned char header\_buffer[HTTP\_SERVER\_MAX\_HEADER\_LEN]
        :   Temp buffer for currently processed header (HTTP/1 only).

        size\_t content\_len
        :   Request content length.

        enum http\_method method
        :   Request method.

        enum http1\_parser\_state parser\_state
        :   HTTP/1 parser state.

        int http1\_frag\_data\_len
        :   Length of the payload length in the currently processed request fragment (HTTP/1 only).

        struct [k\_work\_delayable](../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") inactivity\_timer
        :   Client inactivity timer.

            The client connection is closed by the server when it expires.

        bool preface\_sent
        :   Flag indicating that HTTP2 preface was sent.

        bool http1\_headers\_sent
        :   Flag indicating that HTTP1 headers were sent.

        bool has\_upgrade\_header
        :   Flag indicating that upgrade header was present in the request.

        bool http2\_upgrade
        :   Flag indicating HTTP/2 upgrade takes place.

        bool websocket\_upgrade
        :   Flag indicating Websocket upgrade takes place.

        bool websocket\_sec\_key\_next
        :   Flag indicating Websocket key is being processed.

        bool expect\_continuation
        :   The next frame on the stream is expectd to be a continuation frame.
