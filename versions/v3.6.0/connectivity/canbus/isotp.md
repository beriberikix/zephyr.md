---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/canbus/isotp.html
original_path: connectivity/canbus/isotp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ISO-TP Transport Protocol

## [Overview](#id1)

ISO-TP is a transport protocol defined in the ISO-Standard ISO15765-2 Road
vehicles - Diagnostic communication over Controller Area Network (DoCAN).
Part2: Transport protocol and network layer services. As its name already
implies, it is originally designed, and still used in road vehicle diagnostic
over Controller Area Networks. Nevertheless, it’s not limited to applications in
road vehicles or the automotive domain.

This transport protocol extends the limited payload data size for classical
CAN (8 bytes) and CAN FD (64 bytes) to theoretically four gigabytes.
Additionally, it adds a flow control mechanism to influence the sender’s
behavior. ISO-TP segments packets into small fragments depending on the payload
size of the CAN frame. The header of those segments is called Protocol Control
Information (PCI).

Packets smaller or equal to seven bytes on Classical CAN are called
single-frames (SF). They don’t need to fragment and do not have any flow-control.

Packets larger than that are segmented into a first-frame (FF) and as many
consecutive-frames (CF) as required. The FF contains information about the length of
the entire payload data and additionally, the first few bytes of payload data.
The receiving peer sends back a flow-control-frame (FC) to either deny,
postpone, or accept the following consecutive frames.
The FC also defines the conditions of sending, namely the block-size (BS) and
the minimum separation time between frames (STmin). The block size defines how
many CF the sender is allowed to send, before he has to wait for another FC.

[![ISO-TP Sequence](../../_images/isotp_sequence.svg)](../../_images/isotp_sequence.svg)

## [API Reference](#id2)

Related code samples

[ISO-TP library](../../samples/subsys/canbus/isotp/README.md#isotp "Use ISO-TP library to exchange messages between two boards.")
:   Use ISO-TP library to exchange messages between two boards.

*group* can\_isotp
:   CAN ISO-TP Protocol.

    ISO-TP message ID flags

    ISOTP\_MSG\_EXT\_ADDR
    :   Message uses ISO-TP extended addressing (first payload byte of CAN frame).

    ISOTP\_MSG\_FIXED\_ADDR
    :   Message uses ISO-TP fixed addressing (according to SAE J1939).

        Only valid in combination with `[ISOTP_MSG_IDE](#group__can__isotp_1ga16935466c1a543c03d11b71b8944d0b8)`.

    ISOTP\_MSG\_IDE
    :   Message uses extended (29-bit) CAN ID.

    ISOTP\_MSG\_FDF
    :   Message uses CAN FD format (FDF).

    ISOTP\_MSG\_BRS
    :   Message uses CAN FD Baud Rate Switch (BRS).

        Only valid in combination with `[ISOTP_MSG_FDF](#group__can__isotp_1ga70b485a2e576b1b0fec2cc8037215bd9)`.

    Defines

    ISOTP\_N\_OK
    :   Completed successfully.

    ISOTP\_N\_TIMEOUT\_A
    :   Ar/As has timed out.

    ISOTP\_N\_TIMEOUT\_BS
    :   Reception of next FC has timed out.

    ISOTP\_N\_TIMEOUT\_CR
    :   Cr has timed out.

    ISOTP\_N\_WRONG\_SN
    :   Unexpected sequence number.

    ISOTP\_N\_INVALID\_FS
    :   Invalid flow status received.

    ISOTP\_N\_UNEXP\_PDU
    :   Unexpected PDU received.

    ISOTP\_N\_WFT\_OVRN
    :   Maximum number of WAIT flowStatus PDUs exceeded.

    ISOTP\_N\_BUFFER\_OVERFLW
    :   FlowStatus OVFLW PDU was received.

    ISOTP\_N\_ERROR
    :   General error.

    ISOTP\_NO\_FREE\_FILTER
    :   Implementation specific errors.

        Can’t bind or send because the CAN device has no filter left

    ISOTP\_NO\_NET\_BUF\_LEFT
    :   No net buffer left to allocate.

    ISOTP\_NO\_BUF\_DATA\_LEFT
    :   Not sufficient space in the buffer left for the data.

    ISOTP\_NO\_CTX\_LEFT
    :   No context buffer left to allocate.

    ISOTP\_RECV\_TIMEOUT
    :   Timeout for recv.

    ISOTP\_FIXED\_ADDR\_SA\_POS
    :   Position of fixed source address (SA).

    ISOTP\_FIXED\_ADDR\_SA\_MASK
    :   Mask to obtain fixed source address (SA).

    ISOTP\_FIXED\_ADDR\_TA\_POS
    :   Position of fixed target address (TA).

    ISOTP\_FIXED\_ADDR\_TA\_MASK
    :   Mask to obtain fixed target address (TA).

    ISOTP\_FIXED\_ADDR\_PRIO\_POS
    :   Position of priority in fixed addressing mode.

    ISOTP\_FIXED\_ADDR\_PRIO\_MASK
    :   Mask for priority in fixed addressing mode.

    ISOTP\_FIXED\_ADDR\_RX\_MASK
    :   CAN filter RX mask to match any priority and source address (SA).

    Typedefs

    typedef void (\*isotp\_tx\_callback\_t)(int error\_nr, void \*arg)
    :   Transmission callback.

        This callback is called when a transmission is completed.

        Param error\_nr:
        :   ISOTP\_N\_OK on success, ISOTP\_N\_\* on error

        Param arg:
        :   Callback argument passed to the send function

    Functions

    int isotp\_bind(struct isotp\_recv\_ctx \*rctx, const struct [device](../../kernel/drivers/index.md#c.device "device") \*can\_dev, const struct [isotp\_msg\_id](#c.isotp_msg_id) \*rx\_addr, const struct [isotp\_msg\_id](#c.isotp_msg_id) \*tx\_addr, const struct [isotp\_fc\_opts](#c.isotp_fc_opts) \*opts, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Bind an address to a receiving context.

        This function binds an RX and TX address combination to an RX context. When data arrives from the specified address, it is buffered and can be read by calling isotp\_recv. When calling this routine, a filter is applied in the CAN device, and the context is initialized. The context must be valid until calling unbind.

        Parameters:
        :   - **rctx** – Context to store the internal states.
            - **can\_dev** – The CAN device to be used for sending and receiving.
            - **rx\_addr** – Identifier for incoming data.
            - **tx\_addr** – Identifier for FC frames.
            - **opts** – Flow control options.
            - **timeout** – Timeout for FF SF buffer allocation.

        Return values:
        :   - **ISOTP\_N\_OK** – on success
            - **ISOTP\_NO\_FREE\_FILTER** – if CAN device has no filters left.

    void isotp\_unbind(struct isotp\_recv\_ctx \*rctx)
    :   Unbind a context from the interface.

        This function removes the binding from isotp\_bind. The filter is detached from the CAN device, and if a transmission is ongoing, buffers are freed. The context can be discarded safely after calling this function.

        Parameters:
        :   - **rctx** – Context that should be unbound.

    int isotp\_recv(struct isotp\_recv\_ctx \*rctx, uint8\_t \*data, size\_t len, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Read out received data from fifo.

        This function reads the data from the receive FIFO of the context. It blocks if the FIFO is empty. If an error occurs, the function returns a negative number and leaves the data buffer unchanged.

        Parameters:
        :   - **rctx** – Context that is already bound.
            - **data** – Pointer to a buffer where the data is copied to.
            - **len** – Size of the buffer.
            - **timeout** – Timeout for incoming data.

        Return values:
        :   - **Number** – of bytes copied on success
            - **ISOTP\_RECV\_TIMEOUT** – when “timeout” timed out
            - **ISOTP\_N\_\*** – on error

    int isotp\_recv\_net(struct isotp\_recv\_ctx \*rctx, struct [net\_buf](../networking/api/net_buf.md#c.net_buf "net_buf") \*\*buffer, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get the net buffer on data reception.

        This function reads incoming data into net-buffers. It blocks until the entire packet is received, BS is reached, or an error occurred. If BS was zero, the data is in a single [net\_buf](../networking/api/net_buf.md#structnet__buf). Otherwise, the data is fragmented in chunks of BS size. The net-buffers are referenced and must be freed with net\_buf\_unref after the data is processed.

        Parameters:
        :   - **rctx** – Context that is already bound.
            - **buffer** – Pointer where the [net\_buf](../networking/api/net_buf.md#structnet__buf) pointer is written to.
            - **timeout** – Timeout for incoming data.

        Return values:
        :   - **Remaining** – data length for this transfer if BS > 0, 0 for BS = 0
            - **ISOTP\_RECV\_TIMEOUT** – when “timeout” timed out
            - **ISOTP\_N\_\*** – on error

    int isotp\_send(struct isotp\_send\_ctx \*sctx, const struct [device](../../kernel/drivers/index.md#c.device "device") \*can\_dev, const uint8\_t \*data, size\_t len, const struct [isotp\_msg\_id](#c.isotp_msg_id) \*tx\_addr, const struct [isotp\_msg\_id](#c.isotp_msg_id) \*rx\_addr, [isotp\_tx\_callback\_t](#c.isotp_tx_callback_t) complete\_cb, void \*cb\_arg)
    :   Send data.

        This function is used to send data to a peer that listens to the tx\_addr. An internal work-queue is used to transfer the segmented data. Data and context must be valid until the transmission has finished. If a complete\_cb is given, this function is non-blocking, and the callback is called on completion with the return value as a parameter.

        Parameters:
        :   - **sctx** – Context to store the internal states.
            - **can\_dev** – The CAN device to be used for sending and receiving.
            - **data** – Data to be sent.
            - **len** – Length of the data to be sent.
            - **rx\_addr** – Identifier for FC frames.
            - **tx\_addr** – Identifier for outgoing frames the receiver listens on.
            - **complete\_cb** – Function called on completion or NULL.
            - **cb\_arg** – Argument passed to the complete callback.

        Return values:
        :   - **ISOTP\_N\_OK** – on success
            - **ISOTP\_N\_\*** – on error

    struct isotp\_msg\_id
    :   *#include <isotp.h>*

        ISO-TP message id struct.

        Used to pass addresses to the bind and send functions.

        Public Members

        union [isotp\_msg\_id](#c.isotp_msg_id).[anonymous] [anonymous]
        :   CAN identifier.

            If ISO-TP fixed addressing is used, isotp\_bind ignores SA and priority sections and modifies TA section in flow control frames.

        uint8\_t ext\_addr
        :   ISO-TP extended address (if used).

        uint8\_t dl
        :   ISO-TP frame data length (TX\_DL for TX address or RX\_DL for RX address).

            Valid values are 8 for classical CAN or 8, 12, 16, 20, 24, 32, 48 and 64 for CAN FD.

            0 will be interpreted as 8 or 64 (if ISOTP\_MSG\_FDF is set).

            The value for incoming transmissions (RX\_DL) is determined automatically based on the received first frame and does not need to be set during initialization.

        uint8\_t flags
        :   Flags.

            See also

            [ISOTP\_MSG\_FLAGS](#group__can__isotp_1ISOTP_MSG_FLAGS).

    struct isotp\_fc\_opts
    :   *#include <isotp.h>*

        ISO-TP frame control options struct.

        Used to pass the options to the bind and send functions.

        Public Members

        uint8\_t bs
        :   Block size.

            Number of CF PDUs before next CF is sent

        uint8\_t stmin
        :   Minimum separation time.

            Min time between frames
