---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/rfcomm.html
original_path: connectivity/bluetooth/api/rfcomm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Serial Port Emulation (RFCOMM)

## API Reference

*group* RFCOMM
:   RFCOMM.

    Typedefs

    typedef enum [bt\_rfcomm\_role](#c.bt_rfcomm_role) bt\_rfcomm\_role\_t
    :   Role of RFCOMM session and dlc.

        Used only by internal APIs

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator BT\_RFCOMM\_CHAN\_HFP\_HF = 1

        enumerator BT\_RFCOMM\_CHAN\_HFP\_AG

        enumerator BT\_RFCOMM\_CHAN\_HSP\_AG

        enumerator BT\_RFCOMM\_CHAN\_HSP\_HS

        enumerator BT\_RFCOMM\_CHAN\_SPP

    enum bt\_rfcomm\_role
    :   Role of RFCOMM session and dlc.

        Used only by internal APIs

        *Values:*

        enumerator BT\_RFCOMM\_ROLE\_ACCEPTOR

        enumerator BT\_RFCOMM\_ROLE\_INITIATOR

    Functions

    int bt\_rfcomm\_server\_register(struct [bt\_rfcomm\_server](#c.bt_rfcomm_server) \*server)
    :   Register RFCOMM server.

        Register RFCOMM server for a channel, each new connection is authorized using the [accept()](../../networking/api/sockets.md#group__bsd__sockets_1ga33e6ea428ff537ed7a4763ce91b7d9bb) callback which in case of success shall allocate the dlc structure to be used by the new connection.

        Parameters:
        :   - **server** – Server structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_rfcomm\_dlc\_connect(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc, uint8\_t channel)
    :   Connect RFCOMM channel.

        Connect RFCOMM dlc by channel, once the connection is completed dlc connected() callback will be called. If the connection is rejected disconnected() callback is called instead.

        Parameters:
        :   - **conn** – Connection object.
            - **dlc** – Dlc object.
            - **channel** – Server channel to connect to.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_rfcomm\_dlc\_send(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc, struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Send data to RFCOMM.

        Send data from buffer to the dlc. Length should be less than or equal to mtu.

        Parameters:
        :   - **dlc** – Dlc object.
            - **buf** – Data buffer.

        Returns:
        :   Bytes sent in case of success or negative value in case of error.

    int bt\_rfcomm\_dlc\_disconnect(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc)
    :   Disconnect RFCOMM dlc.

        Disconnect RFCOMM dlc, if the connection is pending it will be canceled and as a result the dlc disconnected() callback is called.

        Parameters:
        :   - **dlc** – Dlc object.

        Returns:
        :   0 in case of success or negative value in case of error.

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_rfcomm\_create\_pdu(struct [net\_buf\_pool](../../networking/api/net_buf.md#c.net_buf_pool "net_buf_pool") \*pool)
    :   Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers.

        Parameters:
        :   - **pool** – Which pool to take the buffer from.

        Returns:
        :   New buffer.

    struct bt\_rfcomm\_dlc\_ops
    :   *#include <rfcomm.h>*

        RFCOMM DLC operations structure.

        Public Members

        void (\*connected)(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc)
        :   DLC connected callback.

            If this callback is provided it will be called whenever the connection completes.

            Param dlc:
            :   The dlc that has been connected

        void (\*disconnected)(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc)
        :   DLC disconnected callback.

            If this callback is provided it will be called whenever the dlc is disconnected, including when a connection gets rejected or cancelled (both incoming and outgoing)

            Param dlc:
            :   The dlc that has been Disconnected

        void (\*recv)(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc, struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
        :   DLC recv callback.

            Param dlc:
            :   The dlc receiving data.

            Param buf:
            :   Buffer containing incoming data.

        void (\*sent)(struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*dlc, int err)
        :   DLC sent callback.

            Param dlc:
            :   The dlc which has sent data.

            Param err:
            :   Sent result.

    struct bt\_rfcomm\_dlc
    :   *#include <rfcomm.h>*

        RFCOMM DLC structure.

    struct bt\_rfcomm\_server
    :   *#include <rfcomm.h>*

        Public Members

        uint8\_t channel
        :   Server Channel.

        int (\*accept)(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](#c.bt_rfcomm_dlc) \*\*dlc)
        :   Server accept callback.

            This callback is called whenever a new incoming connection requires authorization.

            Param conn:
            :   The connection that is requesting authorization

            Param dlc:
            :   Pointer to received the allocated dlc

            Return:
            :   0 in case of success or negative value in case of error.
