---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/http_server.html
original_path: connectivity/networking/api/http_server.html
---

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
  ([`HTTP_RESOURCE_TYPE_STATIC`](../../../doxygen/html/group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)).
- Dynamic resources - content provided at runtime by respective application
  callback ([`HTTP_RESOURCE_TYPE_DYNAMIC`](../../../doxygen/html/group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)).
- Websocket resources - allowing to establish Websocket connections with the
  server ([`HTTP_RESOURCE_TYPE_WEBSOCKET`](../../../doxygen/html/group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)).

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
                      SUBALIGN ${CONFIG_LINKER_ITERABLE_SUBALIGN})
```

Note

You need to define a separate linker section for each HTTP service
registered in the system.

## [Sample Usage](#id7)

### [Services](#id8)

The application needs to define an HTTP service (or multiple services), with
the same name as used for the linker section with [`HTTP_SERVICE_DEFINE`](../../../doxygen/html/group__http__service.md#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)
macro:

```c
#include <zephyr/net/http/service.h>

static uint16_t http_service_port = 80;

HTTP_SERVICE_DEFINE(my_service, "0.0.0.0", &http_service_port, 1, 10, NULL);
```

Alternatively, an HTTPS service can be defined with
[`HTTPS_SERVICE_DEFINE`](../../../doxygen/html/group__http__service.md#ga3bfac63b6f6e0224157f82da90bc7e50):

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
[`HTTP_RESOURCE_DEFINE`](../../../doxygen/html/group__http__service.md#gab177436ac7a8d6589dcfbd416ffd9200) macro.

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

### [Static filesystem resources](#id10)

Static filesystem resource content is defined build-time and is immutable. The following
example shows how the path can be defined as a static resource in the application:

```c
struct http_resource_detail_static_fs static_fs_resource_detail = {
    .common = {
        .type                              = HTTP_RESOURCE_TYPE_STATIC_FS,
        .bitmask_of_supported_http_methods = BIT(HTTP_GET),
    },
    .fs_path = "/lfs1/www",
};

HTTP_RESOURCE_DEFINE(static_fs_resource, my_service, "*", &static_fs_resource_detail);
```

All files located in /lfs1/www are made available to the client. If a file is
gzipped, .gz must be appended to the file name (e.g. index.html.gz), then the
server delivers index.html.gz when the client requests index.html and adds gzip
content-encoding to the HTTP header.

The content type is evaluated based on the file extension. The server supports
.html, .js, .css, .jpg, .png and .svg. More content types can be provided with the
[`HTTP_SERVER_CONTENT_TYPE`](../../../doxygen/html/group__http__server.md#ga709ddfe3f5ae5605b3399687f8be8c47) macro. All other files are provided with the
content type text/html.

```c
HTTP_SERVER_CONTENT_TYPE(json, "application/json")
```

### [Dynamic resources](#id11)

For dynamic resource, a resource callback is registered to exchange data between
the server and the application.

The following example code shows how to register a dynamic resource with a simple
resource handler, which echoes received data back to the client:

```c
static int dyn_handler(struct http_client_ctx *client, enum http_data_status status,
                                   uint8_t *buffer, size_t len, struct http_response_ctx *response_ctx,
                                   void *user_data)
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

    /* Echo data back to client */
    response_ctx->body = buffer;
    response_ctx->body_len = len;
    response_ctx->final_chunk = (status == HTTP_SERVER_DATA_FINAL);

    return 0;
}

struct http_resource_detail_dynamic dyn_resource_detail = {
    .common = {
        .type = HTTP_RESOURCE_TYPE_DYNAMIC,
        .bitmask_of_supported_http_methods =
            BIT(HTTP_GET) | BIT(HTTP_POST),
    },
    .cb = dyn_handler,
    .user_data = NULL,
};

HTTP_RESOURCE_DEFINE(dyn_resource, my_service, "/dynamic",
                     &dyn_resource_detail);
```

The resource callback may be called multiple times for a single request, hence
the application should be able to keep track of the received data progress.

The `status` field informs the application about the progress in passing
request payload from the server to the application. As long as the status
reports [`HTTP_SERVER_DATA_MORE`](../../../doxygen/html/group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231), the application should expect
more data to be provided in a consecutive callback calls.
Once all request payload has been passed to the application, the server reports
[`HTTP_SERVER_DATA_FINAL`](../../../doxygen/html/group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) status. In case of communication errors
during request processing (for example client closed the connection before
complete payload has been received), the server reports
[`HTTP_SERVER_DATA_ABORTED`](../../../doxygen/html/group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc). Either of the two events indicate that
the application shall reset any progress recorded for the resource, and await
a new request to come. The server guarantees that the resource can only be
accessed by single client at a time.

The `response_ctx` field is used by the application to pass response data to
the HTTP server:

- The `status` field allows the application to send an HTTP response code. If
  not populated, the response code will be 200 by default.
- The `headers` and `header_count` fields can be used for the application to
  send any arbitrary HTTP headers. If not populated, only Transfer-Encoding and
  Content-Type are sent by default. The callback may override the Content-Type
  if desired.
- The `body` and `body_len` fields are used to send body data.
- The `final_chunk` field is used to indicate that the application has no more
  response data to send.

Headers and/or response codes may only be sent in the first populated
`response_ctx`, after which only further body data is allowed in subsequent
callbacks.

The server will call the resource callback until it provided all request data
to the application, and the application reports there is no more data to include
in the reply.

### [Websocket resources](#id12)

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

### [Accessing request headers](#id13)

The application can register an interest in any specific HTTP request headers.
These headers are then stored for each incoming request, and can be accessed
from within a dynamic resource callback.

This feature must first be enabled with
[`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](../../../kconfig.md#CONFIG_HTTP_SERVER_CAPTURE_HEADERS "CONFIG_HTTP_SERVER_CAPTURE_HEADERS") Kconfig option.

Then the application can register headers to be captured, and read the values
from within the dynamic resource callback:

```c
HTTP_SERVER_REGISTER_HEADER_CAPTURE(capture_user_agent, "User-Agent");

static int dyn_handler(struct http_client_ctx *client, enum http_data_status status,
                       uint8_t *buffer, size_t len, void *user_data)
{
    size_t header_count = client->header_capture_ctx.count;
    const struct http_header *headers = client->header_capture_ctx.headers;

    LOG_INF("Captured %d headers with request", header_count);

    for (uint32_t i = 0; i < header_count; i++) {
        LOG_INF("Header: '%s: %s'", headers[i].name, headers[i].value);
    }

    return 0;
}
```

## [API Reference](#id14)

[HTTP service API](../../../doxygen/html/group__http__service.md)

Related code samples

- [HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")Implement an HTTP(s) Server demonstrating various resource types.
- [Prometheus Sample](../../../samples/net/prometheus/README.md#prometheus "Implement a Prometheus Metric Server demonstrating various metric types.")Implement a Prometheus Metric Server demonstrating various metric types.

[HTTP server API](../../../doxygen/html/group__http__server.md)

Related code samples

- [HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")Implement an HTTP(s) Server demonstrating various resource types.
- [Prometheus Sample](../../../samples/net/prometheus/README.md#prometheus "Implement a Prometheus Metric Server demonstrating various metric types.")Implement a Prometheus Metric Server demonstrating various metric types.
