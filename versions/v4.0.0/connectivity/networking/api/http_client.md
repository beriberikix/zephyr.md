---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/http_client.html
original_path: connectivity/networking/api/http_client.html
---

# HTTP Client

## [Overview](#id1)

The HTTP client library allows you to send HTTP requests and
parse HTTP responses. The library communicates over the sockets
API but it does not create sockets on its own.
It can be enabled with [`CONFIG_HTTP_CLIENT`](../../../kconfig.md#CONFIG_HTTP_CLIENT "CONFIG_HTTP_CLIENT") Kconfig option.

The application must be responsible for creating a socket and passing it to the library.
Therefore, depending on the application’s needs, the library can communicate over
either a plain TCP socket (HTTP) or a TLS socket (HTTPS).

## [Sample Usage](#id2)

The API of the HTTP client library has a single function.

The following is an example of a request structure created correctly:

```c
struct http_request req = { 0 };
static uint8_t recv_buf[512];

req.method = HTTP_GET;
req.url = "/";
req.host = "localhost";
req.protocol = "HTTP/1.1";
req.response = response_cb;
req.recv_buf = recv_buf;
req.recv_buf_len = sizeof(recv_buf);

/* sock is a file descriptor referencing a socket that has been connected
 * to the HTTP server.
 */
ret = http_client_req(sock, &req, 5000, NULL);
```

If the server responds to the request, the library provides the response to the
application through the response callback registered in the request structure.
As the library can provide the response in chunks, the application must be able
to process these.

Together with the structure containing the response data, the callback function
also provides information about whether the library expects to receive more data.

The following is an example of a very simple response handling function:

```c
static void response_cb(struct http_response *rsp,
                        enum http_final_call final_data,
                        void *user_data)
{
    if (final_data == HTTP_DATA_MORE) {
        LOG_INF("Partial data received (%zd bytes)", rsp->data_len);
    } else if (final_data == HTTP_DATA_FINAL) {
        LOG_INF("All the data received (%zd bytes)", rsp->data_len);
    }

    LOG_INF("Response status %s", rsp->http_status);
}
```

See [HTTP client sample application](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.") for
more information about the library usage.

## [API Reference](#id3)

[HTTP client API](../../../doxygen/html/group__http__client.md)

Related code samples

- [HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.
