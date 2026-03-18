---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/coap_client.html
original_path: connectivity/networking/api/coap_client.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# CoAP client

## [Overview](#id1)

The CoAP client library allows application to send CoAP requests and parse CoAP responses.
The library can be enabled with [`CONFIG_COAP_CLIENT`](../../../kconfig.md#CONFIG_COAP_CLIENT "CONFIG_COAP_CLIENT") Kconfig option.
The application is notified about the response via a callback that is provided to the API
in the request. The CoAP client handles the communication over sockets.
As the CoAP client doesn’t create socket it is using, the application is responsible for creating
the socket. Plain UDP or DTLS sockets are supported.

## [Sample Usage](#id2)

The following is an example of a CoAP client initialization and request sending:

```c
static struct coap_client;
struct coap_client_request req = { 0 };

coap_client_init(&client, NULL);

req.method = COAP_METHOD_GET;
req.confirmable = true;
req.path = "test";
req.fmt = COAP_CONTENT_FORMAT_TEXT_PLAIN;
req.cb = response_cb;
req.payload = NULL;
req.len = 0;

/* Sock is a file descriptor referencing a socket, address is the sockaddr struct for the
 * destination address of the request or NULL if the socket is already connected.
 */
ret = coap_client_req(&client, sock, &address, &req, -1);
```

Before any requests can be sent, the CoAP client needs to be initialized.
After initialization, the application can send a CoAP request and wait for the response.
Currently only one request can be sent for a single CoAP client at a time. There can be multiple
CoAP clients.

The callback provided in the callback will be called in following cases:

- There is a response for the request
- The request failed for some reason

The callback contains a flag last\_block, which indicates if there is more data to come in the
response and means that the current response is part of a blockwise transfer. When the last\_block
is set to true, the response is finished and the client is ready for the next request after
returning from the callback.

If the server responds to the request, the library provides the response to the
application through the response callback registered in the request structure.
As the response can be a blockwise transfer and the client calls the callback once per each
block, the application should be to process all of the blocks to be able to process the response.

The following is an example of a very simple response handling function:

```c
void response_cb(int16_t code, size_t offset, const uint8_t *payload, size_t len,
                 bool last_block, void *user_data)
{
    if (code >= 0) {
            LOG_INF("CoAP response from server %d", code);
            if (last_block) {
                    LOG_INF("Last packet received");
            }
    } else {
            LOG_ERR("Error in sending request %d", code);
    }
}
```

## [API Reference](#id3)

*group* CoAP client API
:   CoAP client API.

    Defines

    MAX\_COAP\_MSG\_LEN
    :   Maximum size of a CoAP message.

    Typedefs

    typedef void (\*coap\_client\_response\_cb\_t)(int16\_t result\_code, size\_t offset, const uint8\_t \*payload, size\_t len, bool last\_block, void \*user\_data)
    :   Callback for CoAP request.

        This callback is called for responses to CoAP client requests. It is used to indicate errors, response codes from server or to deliver payload. Blockwise transfers cause this callback to be called sequentially with increasing payload offset and only partial content in buffer pointed by payload parameter.

        Param result\_code:
        :   Result code of the response. Negative if there was a failure in send. [coap\_response\_code](coap.md#group__coap_1ga1ea81a365834e96f43ab7be573069d26) for positive.

        Param offset:
        :   Payload offset from the beginning of a blockwise transfer.

        Param payload:
        :   Buffer containing the payload from the response. NULL for empty payload.

        Param len:
        :   Size of the payload.

        Param last\_block:
        :   Indicates the last block of the response.

        Param user\_data:
        :   User provided context.

    Functions

    int coap\_client\_init(struct coap\_client \*client, const char \*info)
    :   Initialize the CoAP client.

        Parameters:
        :   - **client** – **[in]** Client instance.
            - **info** – **[in]** Name for the receiving thread of the client. Setting this NULL will result as default name of “coap\_client”.

        Returns:
        :   int Zero on success, otherwise a negative error code.

    int coap\_client\_req(struct coap\_client \*client, int sock, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, struct [coap\_client\_request](#c.coap_client_request) \*req, struct [coap\_transmission\_parameters](coap.md#c.coap_transmission_parameters "coap_transmission_parameters") \*params)
    :   Send CoAP request.

        Operation is handled asynchronously using a background thread. If the socket isn’t connected to a destination address, user must provide a destination address, otherwise the address should be set as NULL. Once the callback is called with last block set as true, socket can be closed or used for another query.

        Parameters:
        :   - **client** – Client instance.
            - **sock** – Open socket file descriptor.
            - **addr** – the destination address of the request, NULL if socket is already connected.
            - **req** – CoAP request structure
            - **params** – Pointer to transmission parameters structure or NULL to use default values.

        Returns:
        :   zero when operation started successfully or negative error code otherwise.

    void coap\_client\_cancel\_requests(struct coap\_client \*client)
    :   Cancel all current requests.

        This is intended for canceling long-running requests (e.g. GETs with the OBSERVE option set) which has gone stale for some reason.

        Parameters:
        :   - **client** – Client instance.

    struct coap\_client\_request
    :   *#include <coap\_client.h>*

        Representation of a CoAP client request.

        Public Members

        enum [coap\_method](coap.md#c.coap_method "coap_method") method
        :   Method of the request.

        bool confirmable
        :   CoAP Confirmable/Non-confirmable message.

        const char \*path
        :   Path of the requested resource.

        enum [coap\_content\_format](coap.md#c.coap_content_format "coap_content_format") fmt
        :   Content format to be used.

        uint8\_t \*payload
        :   User allocated buffer for send request.

        size\_t len
        :   Length of the payload.

        [coap\_client\_response\_cb\_t](#c.coap_client_response_cb_t) cb
        :   Callback when response received.

        struct [coap\_client\_option](#c.coap_client_option) \*options
        :   Extra options to be added to request.

        uint8\_t num\_options
        :   Number of extra options.

        void \*user\_data
        :   User provided context.

    struct coap\_client\_option
    :   *#include <coap\_client.h>*

        Representation of extra options for the CoAP client request.

        Public Members

        uint16\_t code
        :   Option code.

        uint8\_t len
        :   Option len.

        uint8\_t value[12]
        :   Buffer for the length.
