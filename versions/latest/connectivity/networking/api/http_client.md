---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/http_client.html
original_path: connectivity/networking/api/http_client.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

Related code samples

[HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")
:   Implement an HTTP(S) client that issues a variety of HTTP requests.

[TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")
:   Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

*group* HTTP client API
:   HTTP client API.

    **Since**
    :   2.1

    **Version**
    :   0.2.0

    Typedefs

    typedef int (\*http\_payload\_cb\_t)(int sock, struct [http\_request](#c.http_request) \*req, void \*user\_data)
    :   Callback used when data needs to be sent to the server.

        Param sock:
        :   Socket id of the connection

        Param req:
        :   HTTP request information

        Param user\_data:
        :   User specified data specified in [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81)

        Return:
        :   >=0 amount of data sent, in this case [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81) should continue sending data, <0 if [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81) should return the error code to the caller.

    typedef int (\*http\_header\_cb\_t)(int sock, struct [http\_request](#c.http_request) \*req, void \*user\_data)
    :   Callback can be used if application wants to construct additional HTTP headers when the HTTP request is sent.

        Usage of this is optional.

        Param sock:
        :   Socket id of the connection

        Param req:
        :   HTTP request information

        Param user\_data:
        :   User specified data specified in [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81)

        Return:
        :   >=0 amount of data sent, in this case [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81) should continue sending data, <0 if [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81) should return the error code to the caller.

    typedef void (\*http\_response\_cb\_t)(struct [http\_response](#c.http_response) \*rsp, enum [http\_final\_call](#c.http_final_call) final\_data, void \*user\_data)
    :   Callback used when data is received from the server.

        Param rsp:
        :   HTTP response information

        Param final\_data:
        :   Does this data buffer contain all the data or is there still more data to come.

        Param user\_data:
        :   User specified data specified in [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81)

    Enums

    enum http\_final\_call
    :   Is there more data to come.

        *Values:*

        enumerator HTTP\_DATA\_MORE = 0
        :   More data will come.

        enumerator HTTP\_DATA\_FINAL = 1
        :   End of data.

    Functions

    int http\_client\_req(int sock, struct [http\_request](#c.http_request) \*req, int32\_t timeout, void \*user\_data)
    :   Do a HTTP request.

        The callback is called when data is received from the HTTP server. The caller must have created a connection to the server before calling this function so [connect()](sockets.md#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386) call must have be done successfully for the socket.

        Parameters:
        :   - **sock** – Socket id of the connection.
            - **req** – HTTP request information
            - **timeout** – Max timeout to wait for the data. The timeout value cannot be 0 as there would be no time to receive the data. The timeout value is in milliseconds.
            - **user\_data** – User specified data that is passed to the callback.

        Returns:
        :   <0 if error, >=0 amount of data sent to the server

    struct http\_response
    :   *#include <client.h>*

        HTTP response from the server.

        Public Members

        const struct http\_parser\_settings \*http\_cb
        :   HTTP parser settings for the application usage.

        [http\_response\_cb\_t](#c.http_response_cb_t) cb
        :   User provided HTTP response callback which is called when a response is received to a sent HTTP request.

        uint8\_t \*body\_frag\_start
        :   Start address of the body fragment contained in the recv\_buf.

            ```text
                              recv_buffer that contains header + body
                              _______________________________________

                                          |←-------- body_frag_len ---------→|
                       |←--------------------- data len --------------------→|
                   ---------------------------------------------------------------
             ..header  |      header      |               body               |  body..
                   ---------------------------------------------------------------
                       ↑                  ↑
                    recv_buf          body_frag_start

                                 recv_buffer that contains body only
                                 ___________________________________

                        |←------------------ body_frag_len ------------------→|
                        |←--------------------- data len --------------------→|
                   ---------------------------------------------------------------
            ```

            ### 

            #### ..header/body | body | body..

            ↑ recv\_buf body\_frag\_start

            body\_frag\_start >= recv\_buf body\_frag\_len = data\_len - (body\_frag\_start - recv\_buf)

        size\_t body\_frag\_len
        :   Length of the body fragment contained in the recv\_buf.

        uint8\_t \*recv\_buf
        :   Where the response is stored, this is to be provided by the user.

        size\_t recv\_buf\_len
        :   Response buffer maximum length.

        size\_t data\_len
        :   Length of the data in the result buf.

            If the value is larger than recv\_buf\_len, then it means that the data is truncated and could not be fully copied into recv\_buf. This can only happen if the user did not set the response callback. If the callback is set, then the HTTP client API will call response callback many times so that all the data is delivered to the user. Will be zero in the event of a null response.

        size\_t content\_length
        :   HTTP Content-Length field value.

            Will be set to zero in the event of a null response.

        size\_t processed
        :   Amount of data given to the response callback so far, including the current data given to the callback.

            This should be equal to the content\_length field once the entire body has been received. Will be zero if a null response is given.

        char http\_status[HTTP\_STATUS\_STR\_SIZE]
        :   See [https://tools.ietf.org/html/rfc7230#section-3.1.2](https://tools.ietf.org/html/rfc7230#section-3.1.2) for more information.

            The status-code element is a 3-digit integer code

            The reason-phrase element exists for the sole purpose of providing a textual description associated with the numeric status code. A client SHOULD ignore the reason-phrase content.

            Will be blank if a null HTTP response is given.

        uint16\_t http\_status\_code
        :   Numeric HTTP status code which corresponds to the textual description.

            Set to zero if null response is given. Otherwise, will be a 3-digit integer code if valid HTTP response is given.

        uint8\_t cl\_present
        :   Is Content-Length field present.

        uint8\_t body\_found
        :   Is message body found.

        uint8\_t message\_complete
        :   Is HTTP message parsing complete.

    struct http\_client\_internal\_data
    :   *#include <client.h>*

        HTTP client internal data that the application should not touch.

        Public Members

        struct http\_parser parser
        :   HTTP parser context.

        struct http\_parser\_settings parser\_settings
        :   HTTP parser settings.

        struct [http\_response](#c.http_response) response
        :   HTTP response specific data (filled by [http\_client\_req()](#group__http__client_1gaa38b6efb03f88d6959273a41b6acac81) when data is received).

        void \*user\_data
        :   User data.

        int sock
        :   HTTP socket.

    struct http\_request
    :   *#include <client.h>*

        HTTP client request.

        This contains all the data that is needed when doing a HTTP request.

        Public Members

        struct [http\_client\_internal\_data](#c.http_client_internal_data) internal
        :   HTTP client request internal data.

        enum http\_method method
        :   The HTTP method: GET, HEAD, OPTIONS, POST, …

        [http\_response\_cb\_t](#c.http_response_cb_t) response
        :   User supplied callback function to call when response is received.

        const struct http\_parser\_settings \*http\_cb
        :   User supplied list of HTTP callback functions if the calling application wants to know the parsing status or the HTTP fields.

            This is optional and normally not needed.

        uint8\_t \*recv\_buf
        :   User supplied buffer where received data is stored.

        size\_t recv\_buf\_len
        :   Length of the user supplied receive buffer.

        const char \*url
        :   The URL for this request, for example: /index.html.

        const char \*protocol
        :   The HTTP protocol, for example “HTTP/1.1”.

        const char \*\*header\_fields
        :   The HTTP header fields (application specific) The Content-Type may be specified here or in the next field.

            Depending on your application, the Content-Type may vary, however some header fields may remain constant through the application’s life cycle. This is a NULL terminated list of header fields.

        const char \*content\_type\_value
        :   The value of the Content-Type header field, may be NULL.

        const char \*host
        :   Hostname to be used in the request.

        const char \*port
        :   Port number to be used in the request.

        [http\_payload\_cb\_t](#c.http_payload_cb_t) payload\_cb
        :   User supplied callback function to call when payload needs to be sent.

            This can be NULL in which case the payload field in [http\_request](#structhttp__request) is used. The idea of this payload callback is to allow user to send more data that is practical to store in allocated memory.

        const char \*payload
        :   Payload, may be NULL.

        size\_t payload\_len
        :   Payload length is used to calculate Content-Length.

            Set to 0 for chunked transfers.

        [http\_header\_cb\_t](#c.http_header_cb_t) optional\_headers\_cb
        :   User supplied callback function to call when optional headers need to be sent.

            This can be NULL, in which case the optional\_headers field in [http\_request](#structhttp__request) is used. The idea of this optional\_headers callback is to allow user to send more HTTP header data that is practical to store in allocated memory.

        const char \*\*optional\_headers
        :   A NULL terminated list of any optional headers that should be added to the HTTP request.

            May be NULL. If the optional\_headers\_cb is specified, then this field is ignored. Note that there are two similar fields that contain headers, the header\_fields above and this optional\_headers. This is done like this to support Websocket use case where Websocket will use header\_fields variable and any optional application specific headers will be placed into this field.
