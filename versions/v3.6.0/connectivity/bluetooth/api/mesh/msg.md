---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/msg.html
original_path: connectivity/bluetooth/api/mesh/msg.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Message

The Bluetooth Mesh message provides set of structures, macros and functions used
for preparing message buffers, managing message and acknowledged message
contexts.

## API reference

*group* bt\_mesh\_msg
:   Message.

    Defines

    BT\_MESH\_MIC\_SHORT
    :   Length of a short Mesh MIC.

    BT\_MESH\_MIC\_LONG
    :   Length of a long Mesh MIC.

    BT\_MESH\_MODEL\_OP\_LEN(\_op)
    :   Helper to determine the length of an opcode.

        Parameters:
        :   - **\_op** – Opcode.

    BT\_MESH\_MODEL\_BUF\_LEN(\_op, \_payload\_len)
    :   Helper for model message buffer length.

        Returns the length of a Mesh model message buffer, including the opcode length and a short MIC.

        Parameters:
        :   - **\_op** – Opcode of the message.
            - **\_payload\_len** – Length of the model payload.

    BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC(\_op, \_payload\_len)
    :   Helper for model message buffer length.

        Returns the length of a Mesh model message buffer, including the opcode length and a long MIC.

        Parameters:
        :   - **\_op** – Opcode of the message.
            - **\_payload\_len** – Length of the model payload.

    BT\_MESH\_MODEL\_BUF\_DEFINE(\_buf, \_op, \_payload\_len)
    :   Define a Mesh model message buffer using [NET\_BUF\_SIMPLE\_DEFINE](../../../networking/api/net_buf.md#group__net__buf_1gaf85aa0b705bb4fbe2630191fde802501).

        Parameters:
        :   - **\_buf** – Buffer name.
            - **\_op** – Opcode of the message.
            - **\_payload\_len** – Length of the model message payload.

    BT\_MESH\_MSG\_CTX\_INIT(net\_key\_idx, app\_key\_idx, dst, ttl)
    :   Helper for [bt\_mesh\_msg\_ctx](#structbt__mesh__msg__ctx) structure initialization.

        Note

        If `dst` is a Virtual Address, Label UUID shall be initialized separately.

        Parameters:
        :   - **net\_key\_idx** – NetKey Index of the subnet to send the message on. Only used if `app_key_idx` points to devkey.
            - **app\_key\_idx** – AppKey Index to encrypt the message with.
            - **dst** – Remote addr.
            - **ttl** – Time To Live.

    BT\_MESH\_MSG\_CTX\_INIT\_APP(app\_key\_idx, dst)
    :   Helper for [bt\_mesh\_msg\_ctx](#structbt__mesh__msg__ctx) structure initialization secured with Application Key.

        Parameters:
        :   - **app\_key\_idx** – AppKey Index to encrypt the message with.
            - **dst** – Remote addr.

    BT\_MESH\_MSG\_CTX\_INIT\_DEV(net\_key\_idx, dst)
    :   Helper for [bt\_mesh\_msg\_ctx](#structbt__mesh__msg__ctx) structure initialization secured with Device Key of a remote device.

        Parameters:
        :   - **net\_key\_idx** – NetKey Index of the subnet to send the message on.
            - **dst** – Remote addr.

    BT\_MESH\_MSG\_CTX\_INIT\_PUB(pub)
    :   Helper for [bt\_mesh\_msg\_ctx](#structbt__mesh__msg__ctx) structure initialization using Model Publication context.

        Parameters:
        :   - **pub** – Pointer to a model publication context.

    Functions

    void bt\_mesh\_model\_msg\_init(struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*msg, uint32\_t opcode)
    :   Initialize a model message.

        Clears the message buffer contents, and encodes the given opcode. The message buffer will be ready for filling in payload data.

        Parameters:
        :   - **msg** – Message buffer.
            - **opcode** – Opcode to encode.

    static inline void bt\_mesh\_msg\_ack\_ctx\_init(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack)
    :   Initialize an acknowledged message context.

        Initializes semaphore used for synchronization between [bt\_mesh\_msg\_ack\_ctx\_wait](#group__bt__mesh__msg_1ga83561f4d003c6c3c2b91a6afd180d1fd) and [bt\_mesh\_msg\_ack\_ctx\_rx](#group__bt__mesh__msg_1ga2b054f7dc01daeef067cd3d819a7c42c) calls. Call this function before using [bt\_mesh\_msg\_ack\_ctx](#structbt__mesh__msg__ack__ctx).

        Parameters:
        :   - **ack** – Acknowledged message context to initialize.

    static inline void bt\_mesh\_msg\_ack\_ctx\_reset(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack)
    :   Reset the synchronization semaphore in an acknowledged message context.

        This function aborts call to [bt\_mesh\_msg\_ack\_ctx\_wait](#group__bt__mesh__msg_1ga83561f4d003c6c3c2b91a6afd180d1fd).

        Parameters:
        :   - **ack** – Acknowledged message context to be reset.

    void bt\_mesh\_msg\_ack\_ctx\_clear(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack)
    :   Clear parameters of an acknowledged message context.

        This function clears the opcode, remote address and user data set by [bt\_mesh\_msg\_ack\_ctx\_prepare](#group__bt__mesh__msg_1ga1bb34a904103933140e2159cb53d49f5).

        Parameters:
        :   - **ack** – Acknowledged message context to be cleared.

    int bt\_mesh\_msg\_ack\_ctx\_prepare(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack, uint32\_t op, uint16\_t dst, void \*user\_data)
    :   Prepare an acknowledged message context for the incoming message to wait.

        This function sets the opcode, remote address of the incoming message and stores the user data. Use this function before calling [bt\_mesh\_msg\_ack\_ctx\_wait](#group__bt__mesh__msg_1ga83561f4d003c6c3c2b91a6afd180d1fd).

        Parameters:
        :   - **ack** – Acknowledged message context to prepare.
            - **op** – The message OpCode.
            - **dst** – Destination address of the message.
            - **user\_data** – User data for the acknowledged message context.

        Returns:
        :   0 on success, or (negative) error code on failure.

    static inline bool bt\_mesh\_msg\_ack\_ctx\_busy(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack)
    :   Check if the acknowledged message context is initialized with an opcode.

        Parameters:
        :   - **ack** – Acknowledged message context.

        Returns:
        :   true if the acknowledged message context is initialized with an opcode, false otherwise.

    int bt\_mesh\_msg\_ack\_ctx\_wait(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack, [k\_timeout\_t](../../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Wait for a message acknowledge.

        This function blocks execution until [bt\_mesh\_msg\_ack\_ctx\_rx](#group__bt__mesh__msg_1ga2b054f7dc01daeef067cd3d819a7c42c) is called or by timeout.

        Parameters:
        :   - **ack** – Acknowledged message context of the message to wait for.
            - **timeout** – Wait timeout.

        Returns:
        :   0 on success, or (negative) error code on failure.

    static inline void bt\_mesh\_msg\_ack\_ctx\_rx(struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack)
    :   Mark a message as acknowledged.

        This function unblocks call to [bt\_mesh\_msg\_ack\_ctx\_wait](#group__bt__mesh__msg_1ga83561f4d003c6c3c2b91a6afd180d1fd).

        Parameters:
        :   - **ack** – Context of a message to be acknowledged.

    bool bt\_mesh\_msg\_ack\_ctx\_match(const struct [bt\_mesh\_msg\_ack\_ctx](#c.bt_mesh_msg_ack_ctx) \*ack, uint32\_t op, uint16\_t addr, void \*\*user\_data)
    :   Check if an opcode and address of a message matches the expected one.

        Parameters:
        :   - **ack** – Acknowledged message context to be checked.
            - **op** – OpCode of the incoming message.
            - **addr** – Source address of the incoming message.
            - **user\_data** – If not NULL, returns a user data stored in the acknowledged message context by [bt\_mesh\_msg\_ack\_ctx\_prepare](#group__bt__mesh__msg_1ga1bb34a904103933140e2159cb53d49f5).

        Returns:
        :   true if the incoming message matches the expected one, false otherwise.

    struct bt\_mesh\_msg\_ctx
    :   *#include <msg.h>*

        Message sending context.

        Public Members

        uint16\_t net\_idx
        :   NetKey Index of the subnet to send the message on.

        uint16\_t app\_idx
        :   AppKey Index to encrypt the message with.

        uint16\_t addr
        :   Remote address.

        uint16\_t recv\_dst
        :   Destination address of a received message.

            Not used for sending.

        const uint8\_t \*uuid
        :   Label UUID if Remote address is Virtual address, or NULL otherwise.

        int8\_t recv\_rssi
        :   RSSI of received packet.

            Not used for sending.

        uint8\_t recv\_ttl
        :   Received TTL value.

            Not used for sending.

        bool send\_rel
        :   Force sending reliably by using segment acknowledgment.

        bool rnd\_delay
        :   Send message with a random delay according to the Access layer transmitting rules.

        uint8\_t send\_ttl
        :   TTL, or BT\_MESH\_TTL\_DEFAULT for default TTL.

    struct bt\_mesh\_msg\_ack\_ctx
    :   *#include <msg.h>*

        Acknowledged message context for tracking the status of model messages pending a response.

        Public Members

        struct k\_sem sem
        :   Sync semaphore.

        uint32\_t op
        :   Opcode we’re waiting for.

        uint16\_t dst
        :   Address of the node that should respond.

        void \*user\_data
        :   User specific parameter.
