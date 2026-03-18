---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/l2cap.html
original_path: connectivity/bluetooth/api/l2cap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Logical Link Control and Adaptation Protocol (L2CAP)

L2CAP layer enables connection-oriented channels which can be enable with the
configuration option: [`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](../../../kconfig.md#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL "CONFIG_BT_L2CAP_DYNAMIC_CHANNEL"). This channels
support segmentation and reassembly transparently, they also support credit
based flow control making it suitable for data streams.

Channels instances are represented by the [`bt_l2cap_chan`](#c.bt_l2cap_chan) struct which
contains the callbacks in the [`bt_l2cap_chan_ops`](#c.bt_l2cap_chan_ops) struct to inform
when the channel has been connected, disconnected or when the encryption has
changed.
In addition to that it also contains the `recv` callback which is called
whenever an incoming data has been received. Data received this way can be
marked as processed by returning 0 or using
[`bt_l2cap_chan_recv_complete()`](#c.bt_l2cap_chan_recv_complete) API if processing is asynchronous.

Note

The `recv` callback is called directly from RX Thread thus it is not
recommended to block for long periods of time.

For sending data the [`bt_l2cap_chan_send()`](#c.bt_l2cap_chan_send) API can be used noting that
it may block if no credits are available, and resuming as soon as more credits
are available.

Servers can be registered using [`bt_l2cap_server_register()`](#c.bt_l2cap_server_register) API passing
the [`bt_l2cap_server`](#c.bt_l2cap_server) struct which informs what `psm` it should
listen to, the required security level `sec_level`, and the callback
`accept` which is called to authorize incoming connection requests and
allocate channel instances.

Client channels can be initiated with use of [`bt_l2cap_chan_connect()`](#c.bt_l2cap_chan_connect)
API and can be disconnected with the [`bt_l2cap_chan_disconnect()`](#c.bt_l2cap_chan_disconnect) API.
Note that the later can also disconnect channel instances created by servers.

## API Reference

*group* L2CAP
:   L2CAP.

    Defines

    BT\_L2CAP\_HDR\_SIZE
    :   L2CAP PDU header size, used for buffer size calculations.

    BT\_L2CAP\_TX\_MTU
    :   Maximum Transmission Unit (MTU) for an outgoing L2CAP PDU.

    BT\_L2CAP\_RX\_MTU
    :   Maximum Transmission Unit (MTU) for an incoming L2CAP PDU.

    BT\_L2CAP\_BUF\_SIZE(mtu)
    :   Helper to calculate needed buffer size for L2CAP PDUs.

        Useful for creating buffer pools.

        Parameters:
        :   - **mtu** – Needed L2CAP PDU MTU.

        Returns:
        :   Needed buffer size to match the requested L2CAP PDU MTU.

    BT\_L2CAP\_SDU\_HDR\_SIZE
    :   L2CAP SDU header size, used for buffer size calculations.

    BT\_L2CAP\_SDU\_TX\_MTU
    :   Maximum Transmission Unit for an unsegmented outgoing L2CAP SDU.

        The Maximum Transmission Unit for an outgoing L2CAP SDU when sent without segmentation, i.e. a single L2CAP SDU will fit inside a single L2CAP PDU.

        The MTU for outgoing L2CAP SDUs with segmentation is defined by the size of the application buffer pool.

    BT\_L2CAP\_SDU\_RX\_MTU
    :   Maximum Transmission Unit for an unsegmented incoming L2CAP SDU.

        The Maximum Transmission Unit for an incoming L2CAP SDU when sent without segmentation, i.e. a single L2CAP SDU will fit inside a single L2CAP PDU.

        The MTU for incoming L2CAP SDUs with segmentation is defined by the size of the application buffer pool. The application will have to define an alloc\_buf callback for the channel in order to support receiving segmented L2CAP SDUs.

    BT\_L2CAP\_SDU\_BUF\_SIZE(mtu)
    :   Helper to calculate needed buffer size for L2CAP SDUs.

        Useful for creating buffer pools.

        Parameters:
        :   - **mtu** – Required BT\_L2CAP\_\*\_SDU.

        Returns:
        :   Needed buffer size to match the requested L2CAP SDU MTU.

    BT\_L2CAP\_LE\_CHAN(\_ch)
    :   Helper macro getting container object of type [bt\_l2cap\_le\_chan](#structbt__l2cap__le__chan) address having the same container chan member address as object in question.

        Parameters:
        :   - **\_ch** – Address of object of [bt\_l2cap\_chan](#structbt__l2cap__chan) type

        Returns:
        :   Address of in memory [bt\_l2cap\_le\_chan](#structbt__l2cap__le__chan) object type containing the address of in question object.

    BT\_L2CAP\_CHAN\_SEND\_RESERVE
    :   Headroom needed for outgoing L2CAP PDUs.

    BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE
    :   Headroom needed for outgoing L2CAP SDUs.

    Typedefs

    typedef void (\*bt\_l2cap\_chan\_destroy\_t)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
    :   Channel destroy callback.

        Param chan:
        :   Channel object.

    typedef enum [bt\_l2cap\_chan\_state](#c.bt_l2cap_chan_state) bt\_l2cap\_chan\_state\_t
    :   Life-span states of L2CAP CoC channel.

        Used only by internal APIs dealing with setting channel to proper state depending on operational context.

        A channel enters the [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state upon [bt\_l2cap\_chan\_connect](#group__bt__l2cap_1ga3c3cfb4b151c808c0a3d2562a5c26a20), [bt\_l2cap\_ecred\_chan\_connect](#group__bt__l2cap_1gaebc2d157fb5f013722e9c332b3d81804) or upon returning from [bt\_l2cap\_server::accept](#structbt__l2cap__server_1ad31a1908f7dc733f9497164ccabba2af).

        When a channel leaves the [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state, [bt\_l2cap\_chan\_ops::connected](#structbt__l2cap__chan__ops_1a3a4dd75a11c9867adcade6d288dec2de) is called.

    typedef enum [bt\_l2cap\_chan\_status](#c.bt_l2cap_chan_status) bt\_l2cap\_chan\_status\_t
    :   Status of L2CAP channel.

    Enums

    enum bt\_l2cap\_chan\_state
    :   Life-span states of L2CAP CoC channel.

        Used only by internal APIs dealing with setting channel to proper state depending on operational context.

        A channel enters the [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state upon [bt\_l2cap\_chan\_connect](#group__bt__l2cap_1ga3c3cfb4b151c808c0a3d2562a5c26a20), [bt\_l2cap\_ecred\_chan\_connect](#group__bt__l2cap_1gaebc2d157fb5f013722e9c332b3d81804) or upon returning from [bt\_l2cap\_server::accept](#structbt__l2cap__server_1ad31a1908f7dc733f9497164ccabba2af).

        When a channel leaves the [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state, [bt\_l2cap\_chan\_ops::connected](#structbt__l2cap__chan__ops_1a3a4dd75a11c9867adcade6d288dec2de) is called.

        *Values:*

        enumerator BT\_L2CAP\_DISCONNECTED
        :   Channel disconnected.

        enumerator BT\_L2CAP\_CONNECTING
        :   Channel in connecting state.

        enumerator BT\_L2CAP\_CONFIG
        :   Channel in config state, BR/EDR specific.

        enumerator BT\_L2CAP\_CONNECTED
        :   Channel ready for upper layer traffic on it.

        enumerator BT\_L2CAP\_DISCONNECTING
        :   Channel in disconnecting state.

    enum bt\_l2cap\_chan\_status
    :   Status of L2CAP channel.

        *Values:*

        enumerator BT\_L2CAP\_STATUS\_OUT
        :   Channel can send at least one PDU.

        enumerator BT\_L2CAP\_STATUS\_SHUTDOWN
        :   Channel shutdown status.

            Once this status is notified it means the channel will no longer be able to transmit or receive data.

        enumerator BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING
        :   Channel encryption pending status.

        enumerator BT\_L2CAP\_NUM\_STATUS

    Functions

    int bt\_l2cap\_server\_register(struct [bt\_l2cap\_server](#c.bt_l2cap_server) \*server)
    :   Register L2CAP server.

        Register L2CAP server for a PSM, each new connection is authorized using the [accept()](../../networking/api/sockets.md#group__bsd__sockets_1ga33e6ea428ff537ed7a4763ce91b7d9bb) callback which in case of success shall allocate the channel structure to be used by the new connection.

        For fixed, SIG-assigned PSMs (in the range 0x0001-0x007f) the PSM should be assigned to server->psm before calling this API. For dynamic PSMs (in the range 0x0080-0x00ff) server->psm may be pre-set to a given value (this is however not recommended) or be left as 0, in which case upon return a newly allocated value will have been assigned to it. For dynamically allocated values the expectation is that it’s exposed through a GATT service, and that’s how L2CAP clients discover how to connect to the server.

        Parameters:
        :   - **server** – Server structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_br\_server\_register(struct [bt\_l2cap\_server](#c.bt_l2cap_server) \*server)
    :   Register L2CAP server on BR/EDR oriented connection.

        Register L2CAP server for a PSM, each new connection is authorized using the [accept()](../../networking/api/sockets.md#group__bsd__sockets_1ga33e6ea428ff537ed7a4763ce91b7d9bb) callback which in case of success shall allocate the channel structure to be used by the new connection.

        Parameters:
        :   - **server** – Server structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_ecred\_chan\_connect(struct bt\_conn \*conn, struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*\*chans, uint16\_t psm)
    :   Connect Enhanced Credit Based L2CAP channels.

        Connect up to 5 L2CAP channels by PSM, once the connection is completed each channel connected() callback will be called. If the connection is rejected disconnected() callback is called instead.

        Parameters:
        :   - **conn** – Connection object.
            - **chans** – Array of channel objects.
            - **psm** – Channel PSM to connect to.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_ecred\_chan\_reconfigure(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*\*chans, uint16\_t mtu)
    :   Reconfigure Enhanced Credit Based L2CAP channels.

        Reconfigure up to 5 L2CAP channels. Channels must be from the same bt\_conn. Once reconfiguration is completed each channel reconfigured() callback will be called. MTU cannot be decreased on any of provided channels.

        Parameters:
        :   - **chans** – Array of channel objects. Null-terminated. Elements after the first 5 are silently ignored.
            - **mtu** – Channel MTU to reconfigure to.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_chan\_connect(struct bt\_conn \*conn, struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, uint16\_t psm)
    :   Connect L2CAP channel.

        Connect L2CAP channel by PSM, once the connection is completed channel connected() callback will be called. If the connection is rejected disconnected() callback is called instead. Channel object passed (over an address of it) as second parameter shouldn’t be instantiated in application as standalone. Instead of, application should create transport dedicated L2CAP objects, i.e. type of [bt\_l2cap\_le\_chan](#structbt__l2cap__le__chan) for LE and/or type of [bt\_l2cap\_br\_chan](#structbt__l2cap__br__chan) for BR/EDR. Then pass to this API the location (address) of [bt\_l2cap\_chan](#structbt__l2cap__chan) type object which is a member of both transport dedicated objects.

        Parameters:
        :   - **conn** – Connection object.
            - **chan** – Channel object.
            - **psm** – Channel PSM to connect to.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_chan\_disconnect(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
    :   Disconnect L2CAP channel.

        Disconnect L2CAP channel, if the connection is pending it will be canceled and as a result the channel disconnected() callback is called. Regarding to input parameter, to get details see reference description to [bt\_l2cap\_chan\_connect()](#group__bt__l2cap_1ga3c3cfb4b151c808c0a3d2562a5c26a20) API above.

        Parameters:
        :   - **chan** – Channel object.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_chan\_send(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Send data to L2CAP channel.

        Send data from buffer to the channel. If credits are not available, buf will be queued and sent as and when credits are received from peer. Regarding to first input parameter, to get details see reference description to [bt\_l2cap\_chan\_connect()](#group__bt__l2cap_1ga3c3cfb4b151c808c0a3d2562a5c26a20) API above.

        Network buffer fragments (ie `buf->frags`) are not supported.

        When sending L2CAP data over an BR/EDR connection the application is sending L2CAP PDUs. The application is required to have reserved [BT\_L2CAP\_CHAN\_SEND\_RESERVE](#group__bt__l2cap_1ga281232ec622c626c0be2be23bae18d8d) bytes in the buffer before sending. The application should use the [BT\_L2CAP\_BUF\_SIZE()](#group__bt__l2cap_1gab95b119de4757588074e367a90a7136a) helper to correctly size the buffers for the for the outgoing buffer pool.

        When sending L2CAP data over an LE connection the application is sending L2CAP SDUs. The application shall reserve [BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE](#group__bt__l2cap_1gabdb3983d3862f6654a1653dd45c4157d) bytes in the buffer before sending.

        The application can use the [BT\_L2CAP\_SDU\_BUF\_SIZE()](#group__bt__l2cap_1ga1c76618c32bbe86b18fd8663760fb220) helper to correctly size the buffer to account for the reserved headroom.

        When segmenting an L2CAP SDU into L2CAP PDUs the stack will first attempt to allocate buffers from the channel’s `alloc_seg` callback and will fallback on the stack’s global buffer pool (sized  [`CONFIG_BT_L2CAP_TX_BUF_COUNT`](../../../kconfig.md#CONFIG_BT_L2CAP_TX_BUF_COUNT "CONFIG_BT_L2CAP_TX_BUF_COUNT") ).

        Note

        Buffer ownership is transferred to the stack in case of success, in case of an error the caller retains the ownership of the buffer.

        Returns:
        :   0 in case of success or negative value in case of error.

        Returns:
        :   -EINVAL if `buf` or `chan` is NULL.

        Returns:
        :   -EINVAL if `chan` is not either BR/EDR or LE credit-based.

        Returns:
        :   -EINVAL if buffer doesn’t have enough bytes reserved to fit header.

        Returns:
        :   -EINVAL if buffer’s reference counter != 1

        Returns:
        :   -EMSGSIZE if `buf` is larger than `chan`’s MTU.

        Returns:
        :   -ENOTCONN if underlying conn is disconnected.

        Returns:
        :   -ESHUTDOWN if L2CAP channel is disconnected.

        Returns:
        :   -other (from lower layers) if chan is BR/EDR.

    int bt\_l2cap\_chan\_give\_credits(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, uint16\_t additional\_credits)
    :   Give credits to the remote.

        Only available for channels using [bt\_l2cap\_chan\_ops::seg\_recv](#structbt__l2cap__chan__ops_1a7759a713038d74748952d5f2eb712429).  [`CONFIG_BT_L2CAP_SEG_RECV`](../../../kconfig.md#CONFIG_BT_L2CAP_SEG_RECV "CONFIG_BT_L2CAP_SEG_RECV") must be enabled to make this function available.

        Each credit given allows the peer to send one segment.

        This function depends on a valid `chan` object. Make sure to default-initialize or memset `chan` when allocating or reusing it for new connections.

        Adding zero credits is not allowed.

        Credits can be given before entering the [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state. Doing so will adjust the ‘initial credits’ sent in the connection PDU.

        Must not be called while the channel is in [BT\_L2CAP\_CONNECTING](#group__bt__l2cap_1gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_l2cap\_chan\_recv\_complete(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Complete receiving L2CAP channel data.

        Complete the reception of incoming data. This shall only be called if the channel recv callback has returned -EINPROGRESS to process some incoming data. The buffer shall contain the original user\_data as that is used for storing the credits/segments used by the packet.

        Parameters:
        :   - **chan** – Channel object.
            - **buf** – Buffer containing the data.

        Returns:
        :   0 in case of success or negative value in case of error.

    struct bt\_l2cap\_chan
    :   *#include <l2cap.h>*

        L2CAP Channel structure.

        Public Members

        struct bt\_conn \*conn
        :   Channel connection reference.

        const struct [bt\_l2cap\_chan\_ops](#c.bt_l2cap_chan_ops) \*ops
        :   Channel operations reference.

    struct bt\_l2cap\_le\_endpoint
    :   *#include <l2cap.h>*

        LE L2CAP Endpoint structure.

        Public Members

        uint16\_t cid
        :   Endpoint Channel Identifier (CID).

        uint16\_t mtu
        :   Endpoint Maximum Transmission Unit.

        uint16\_t mps
        :   Endpoint Maximum PDU payload Size.

        atomic\_t credits
        :   Endpoint credits.

    struct bt\_l2cap\_le\_chan
    :   *#include <l2cap.h>*

        LE L2CAP Channel structure.

        Public Members

        struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) chan
        :   Common L2CAP channel reference object.

        struct [bt\_l2cap\_le\_endpoint](#c.bt_l2cap_le_endpoint) rx
        :   Channel Receiving Endpoint.

            If the application has set an alloc\_buf channel callback for the channel to support receiving segmented L2CAP SDUs the application should initialize the MTU of the Receiving Endpoint. Otherwise the MTU of the receiving endpoint will be initialized to [BT\_L2CAP\_SDU\_RX\_MTU](#group__bt__l2cap_1ga13b93a8f09157fbcf739fa4949840efe) by the stack.

            This is the source of the MTU, MPS and credit values when sending L2CAP\_LE\_CREDIT\_BASED\_CONNECTION\_REQ/RSP and L2CAP\_CONFIGURATION\_REQ.

        uint16\_t pending\_rx\_mtu
        :   Pending RX MTU on ECFC reconfigure, used internally by stack.

        struct [bt\_l2cap\_le\_endpoint](#c.bt_l2cap_le_endpoint) tx
        :   Channel Transmission Endpoint.

            This is an image of the remote’s rx.

            The MTU and MPS is controlled by the remote by L2CAP\_LE\_CREDIT\_BASED\_CONNECTION\_REQ/RSP or L2CAP\_CONFIGURATION\_REQ.

        struct k\_fifo tx\_queue
        :   Channel Transmission queue (for SDUs).

    struct bt\_l2cap\_br\_endpoint
    :   *#include <l2cap.h>*

        BREDR L2CAP Endpoint structure.

        Public Members

        uint16\_t cid
        :   Endpoint Channel Identifier (CID).

        uint16\_t mtu
        :   Endpoint Maximum Transmission Unit.

    struct bt\_l2cap\_br\_chan
    :   *#include <l2cap.h>*

        BREDR L2CAP Channel structure.

        Public Members

        struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) chan
        :   Common L2CAP channel reference object.

        struct [bt\_l2cap\_br\_endpoint](#c.bt_l2cap_br_endpoint) rx
        :   Channel Receiving Endpoint.

        struct [bt\_l2cap\_br\_endpoint](#c.bt_l2cap_br_endpoint) tx
        :   Channel Transmission Endpoint.

        uint16\_t psm
        :   Remote PSM to be connected.

        uint8\_t ident
        :   Helps match request context during CoC.

    struct bt\_l2cap\_chan\_ops
    :   *#include <l2cap.h>*

        L2CAP Channel operations structure.

        Public Members

        void (\*connected)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel connected callback.

            If this callback is provided it will be called whenever the connection completes.

            Param chan:
            :   The channel that has been connected

        void (\*disconnected)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel disconnected callback.

            If this callback is provided it will be called whenever the channel is disconnected, including when a connection gets rejected.

            Param chan:
            :   The channel that has been Disconnected

        void (\*encrypt\_change)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, uint8\_t hci\_status)
        :   Channel encrypt\_change callback.

            If this callback is provided it will be called whenever the security level changed (indirectly link encryption done) or authentication procedure fails. In both cases security initiator and responder got the final status (HCI status) passed by related to encryption and authentication events from local host’s controller.

            Param chan:
            :   The channel which has made encryption status changed.

            Param status:
            :   HCI status of performed security procedure caused by channel security requirements. The value is populated by HCI layer and set to 0 when success and to non-zero (reference to HCI Error Codes) when security/authentication failed.

        struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*(\*alloc\_seg)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel alloc\_seg callback.

            If this callback is provided the channel will use it to allocate buffers to store segments. This avoids wasting big SDU buffers with potentially much smaller PDUs. If this callback is supplied, it must return a valid buffer.

            Param chan:
            :   The channel requesting a buffer.

            Return:
            :   Allocated buffer.

        struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*(\*alloc\_buf)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel alloc\_buf callback.

            If this callback is provided the channel will use it to allocate buffers to store incoming data. Channels that requires segmentation must set this callback. If the application has not set a callback the L2CAP SDU MTU will be truncated to [BT\_L2CAP\_SDU\_RX\_MTU](#group__bt__l2cap_1ga13b93a8f09157fbcf739fa4949840efe).

            Param chan:
            :   The channel requesting a buffer.

            Return:
            :   Allocated buffer.

        int (\*recv)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
        :   Channel recv callback.

            Param chan:
            :   The channel receiving data.

            Param buf:
            :   Buffer containing incoming data.

            Return:
            :   0 in case of success or negative value in case of error.

            Return:
            :   -EINPROGRESS in case where user has to confirm once the data has been processed by calling [bt\_l2cap\_chan\_recv\_complete](#group__bt__l2cap_1gad53f5fc31314121ff84e740879eae3cf) passing back the buffer received with its original user\_data which contains the number of segments/credits used by the packet.

        void (\*sent)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel sent callback.

            This callback will be called once the controller marks the SDU as completed. When the controller does so is implementation dependent. It could be after the SDU is enqueued for transmission, or after it is sent on air.

            Param chan:
            :   The channel which has sent data.

        void (\*status)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, atomic\_t \*status)
        :   Channel status callback.

            If this callback is provided it will be called whenever the channel status changes.

            Param chan:
            :   The channel which status changed

            Param status:
            :   The channel status

        void (\*reconfigured)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan)
        :   Channel reconfigured callback.

            If this callback is provided it will be called whenever peer or local device requested reconfiguration. Application may check updated MTU and MPS values by inspecting chan->le endpoints.

            Param chan:
            :   The channel which was reconfigured

        void (\*seg\_recv)(struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*chan, size\_t sdu\_len, off\_t seg\_offset, struct [net\_buf\_simple](../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*seg)
        :   Handle L2CAP segments directly.

            This is an alternative to [bt\_l2cap\_chan\_ops::recv](#structbt__l2cap__chan__ops_1a0ab419d3c52c08e0dfda236466d7cadd). They cannot be used together.

            This is called immediately for each received segment.

            Unlike with [bt\_l2cap\_chan\_ops::recv](#structbt__l2cap__chan__ops_1a0ab419d3c52c08e0dfda236466d7cadd), flow control is explicit. Each time this handler is invoked, the remote has permanently used up one credit. Use [bt\_l2cap\_chan\_give\_credits](#group__bt__l2cap_1ga9bc950a929fc2bdb1463c268cea478b6) to give credits.

            The start of an SDU is marked by `seg_offset == 0`. The end of an SDU is marked by `seg_offset + seg->len == sdu_len`.

            The stack guarantees that:

            - The sender had the credit.
            - The SDU length does not exceed MTU.
            - The segment length does not exceed MPS.

            Additionally, the L2CAP protocol is such that:

            - Segments come in order.
            - SDUs cannot be interleaved or aborted halfway.

            Note

            With this alternative API, the application is responsible for setting the RX MTU and MPS. The MPS must not exceed [BT\_L2CAP\_RX\_MTU](#group__bt__l2cap_1ga6e458a1758e5012755f3b97f8348c966).

            Param chan:
            :   The receiving channel.

            Param sdu\_len:
            :   Byte length of the SDU this segment is part of.

            Param seg\_offset:
            :   The byte offset of this segment in the SDU.

            Param seg:
            :   The segment payload.

    struct bt\_l2cap\_server
    :   *#include <l2cap.h>*

        L2CAP Server structure.

        Public Members

        uint16\_t psm
        :   Server PSM.

            Possible values: 0 A dynamic value will be auto-allocated when [bt\_l2cap\_server\_register()](#group__bt__l2cap_1ga1a5e8c81c086872d7fb8da5329f982c6) is called.

            0x0001-0x007f Standard, Bluetooth SIG-assigned fixed values.

            0x0080-0x00ff Dynamically allocated. May be pre-set by the application before server registration (not recommended however), or auto-allocated by the stack if the app gave 0 as the value.

        [bt\_security\_t](connection_mgmt.md#c.bt_security_t "bt_security_t") sec\_level
        :   Required minimum security level.

        int (\*accept)(struct bt\_conn \*conn, struct [bt\_l2cap\_server](#c.bt_l2cap_server) \*server, struct [bt\_l2cap\_chan](#c.bt_l2cap_chan) \*\*chan)
        :   Server accept callback.

            This callback is called whenever a new incoming connection requires authorization.

            Param conn:
            :   The connection that is requesting authorization

            Param server:
            :   Pointer to the server structure this callback relates to

            Param chan:
            :   Pointer to received the allocated channel

            Return:
            :   0 in case of success or negative value in case of error.

            Return:
            :   -ENOMEM if no available space for new channel.

            Return:
            :   -EACCES if application did not authorize the connection.

            Return:
            :   -EPERM if encryption key size is too short.
