---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/tftp.html
original_path: connectivity/networking/api/tftp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# TFTP

Zephyr provides a simple TFTP client library that can enabled with
[`CONFIG_MQTT_SN_LIB`](../../../kconfig.md#CONFIG_MQTT_SN_LIB "CONFIG_MQTT_SN_LIB") Kconfig option.

See [TFTP client sample application](../../../samples/net/tftp_client/README.md#tftp-client "Use the TFTP client library to get/put files from/to a TFTP server.") for
more information about the library usage.

## API Reference

Related code samples

[TFTP client](../../../samples/net/tftp_client/README.md#tftp-client "Use the TFTP client library to get/put files from/to a TFTP server.")
:   Use the TFTP client library to get/put files from/to a TFTP server.

*group* tftp\_client
:   TFTP Client Implementation.

    TFTP client error codes.

    TFTPC\_SUCCESS
    :   Success.

    TFTPC\_DUPLICATE\_DATA
    :   Duplicate data received.

    TFTPC\_BUFFER\_OVERFLOW
    :   User buffer is too small.

    TFTPC\_UNKNOWN\_FAILURE
    :   Unknown failure.

    TFTPC\_REMOTE\_ERROR
    :   Remote server error.

    TFTPC\_RETRIES\_EXHAUSTED
    :   Retries exhausted.

    Defines

    TFTP\_BLOCK\_SIZE
    :   RFC1350: the file is sent in fixed length blocks of 512 bytes.

        Each data packet contains one block of data, and must be acknowledged by an acknowledgment packet before the next packet can be sent. A data packet of less than 512 bytes signals termination of a transfer.

    TFTP\_HEADER\_SIZE
    :   RFC1350: For non-request TFTP message, the header contains 2-byte operation code plus 2-byte block number or error code.

    TFTPC\_MAX\_BUF\_SIZE
    :   Maximum amount of data that can be sent or received.

    Typedefs

    typedef void (\*tftp\_callback\_t)(const struct [tftp\_evt](#c.tftp_evt) \*evt)
    :   TFTP event notification callback registered by the application.

        Param evt:
        :   **[in]** Event description along with result and associated parameters (if any).

    Enums

    enum tftp\_evt\_type
    :   TFTP Asynchronous Events notified to the application from the module through the callback registered by the application.

        *Values:*

        enumerator TFTP\_EVT\_DATA
        :   DATA event when data is received from remote server.

            Note

            DATA event structure contains payload data and size.

        enumerator TFTP\_EVT\_ERROR
        :   ERROR event when error is received from remote server.

            Note

            ERROR event structure contains error code and message.

    Functions

    int tftp\_get(struct [tftpc](#c.tftpc) \*client, const char \*remote\_file, const char \*mode)
    :   This function gets data from a “file” on the remote server.

        Note

        This function blocks until the transfer is completed or network error happens. The integrity of the `client` structure must be ensured until the function returns.

        Parameters:
        :   - **client** – Client information of type [tftpc](#structtftpc).
            - **remote\_file** – Name of the remote file to get.
            - **mode** – TFTP Client “mode” setting.

        Return values:
        :   - **The** – size of data being received if the operation completed successfully.
            - **TFTPC\_BUFFER\_OVERFLOW** – if the file is larger than the user buffer.
            - **TFTPC\_REMOTE\_ERROR** – if the server failed to process our request.
            - **TFTPC\_RETRIES\_EXHAUSTED** – if the client timed out waiting for server.
            - **-EINVAL** – if `client` is NULL.

    int tftp\_put(struct [tftpc](#c.tftpc) \*client, const char \*remote\_file, const char \*mode, const uint8\_t \*user\_buf, uint32\_t user\_buf\_size)
    :   This function puts data to a “file” on the remote server.

        Note

        This function blocks until the transfer is completed or network error happens. The integrity of the `client` structure must be ensured until the function returns.

        Parameters:
        :   - **client** – Client information of type [tftpc](#structtftpc).
            - **remote\_file** – Name of the remote file to put.
            - **mode** – TFTP Client “mode” setting.
            - **user\_buf** – Data buffer containing the data to put.
            - **user\_buf\_size** – Length of the data to put.

        Return values:
        :   - **The** – size of data being sent if the operation completed successfully.
            - **TFTPC\_REMOTE\_ERROR** – if the server failed to process our request.
            - **TFTPC\_RETRIES\_EXHAUSTED** – if the client timed out waiting for server.
            - **-EINVAL** – if `client` or `user_buf` is NULL or if `user_buf_size` is zero.

    struct tftp\_data\_param
    :   *#include <tftp.h>*

        Parameters for data event.

        Public Members

        uint8\_t \*data\_ptr
        :   Pointer to binary data.

        uint32\_t len
        :   Length of binary data.

    struct tftp\_error\_param
    :   *#include <tftp.h>*

        Parameters for error event.

        Public Members

        char \*msg
        :   Error message.

        int code
        :   Error code.

    union tftp\_evt\_param
    :   *#include <tftp.h>*

        Defines event parameters notified along with asynchronous events to the application.

        Public Members

        struct [tftp\_data\_param](#c.tftp_data_param) data
        :   Parameters accompanying TFTP\_EVT\_DATA event.

        struct [tftp\_error\_param](#c.tftp_error_param) error
        :   Parameters accompanying TFTP\_EVT\_ERROR event.

    struct tftp\_evt
    :   *#include <tftp.h>*

        Defines TFTP asynchronous event notified to the application.

        Public Members

        enum [tftp\_evt\_type](#c.tftp_evt_type) type
        :   Identifies the event.

        union [tftp\_evt\_param](#c.tftp_evt_param) param
        :   Contains parameters (if any) accompanying the event.

    struct tftpc
    :   *#include <tftp.h>*

        TFTP client definition to maintain information relevant to the client.

        Note

        Application must initialize `[server](#structtftpc_1a8ff9317a6bbdfac895cb1e408ae72cd9)` and `[callback](#structtftpc_1a39a04978a6cf3826ef19993989400b60)` before calling GET or PUT API with the `[tftpc](#structtftpc)` structure.

        Public Members

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") server
        :   Socket address pointing to the remote TFTP server.

        [tftp\_callback\_t](#c.tftp_callback_t) callback
        :   Event notification callback.

            No notification if NULL

        uint8\_t tftp\_buf[(512 + 4)]
        :   Buffer for internal usage.
