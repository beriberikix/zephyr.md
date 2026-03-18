---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/debugging/mipi_stp_decoder.html
original_path: services/debugging/mipi_stp_decoder.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MIPI STP Decoder

The MIPI System Trace Protocol (MIPI STP) was developed as a generic base protocol that can
be shared by multiple application-specific trace protocols. It serves as a wrapper protocol
that merges disparate streams that typically contain different trace protocols from different
trace sources. Stream consists of opcode (shortest is 4 bit long) followed by optional data and
optional timestamp. There are opcodes for data (8, 16, 32, 64 bit data marked/not marked, with or
without timestamp), stream recognition (master and channel), synchronization (ASYNC opcode) and
others.

One example where protocol is used is ARM Coresight STM (System Trace Macrocell) where data
written to Stimulus Port registers maps directly to STP stream.

This module can be used to perform on-chip decoding of the data stream. STP v2 is used.

## Usage

Decoder is initialized with a callback. A callback is called on each decoded opcode.
Decoder has internal state since there are dependency between opcodes (e.g. timestamp can be
relative). Decoder can be in synchronization or not. Initial state is configurable.
If decoder is not synchronized to the stream then it decodes each nibble in search for ASYNC opcode.
Loss of synchronization can be indicated to the decoder by calling
[`mipi_stp_decoder_sync_loss()`](#c.mipi_stp_decoder_sync_loss). [`mipi_stp_decoder_decode()`](#c.mipi_stp_decoder_decode) is used to decode the data.

## Limitations

There are following limitations:

- Decoder supports only little endian architectures.
- When decoding nibbles, it is more efficient when core supports unaligned memory access.
  Implementation supports optimized version with unaligned memory access and generic one.
  Optimized version is used for ARM Cortex-M (expect for M0).
- Limited set of the most common opcodes is implemented.

## API documentation

*group* STP Decoder API
:   Defines

    STP\_DECODER\_TYPE2STR(\_type)
    :   Convert type to a string literal.

        Parameters:
        :   - **\_type** – type

        Returns:
        :   String literal.

    Typedefs

    typedef void (\*mipi\_stp\_decoder\_cb)(enum [mipi\_stp\_decoder\_ctrl\_type](#c.mipi_stp_decoder_ctrl_type) type, union [mipi\_stp\_decoder\_data](#c.mipi_stp_decoder_data) data, uint64\_t \*ts, bool marked)
    :   Callback signature.

        Callback is called whenever an element from STPv2 stream is decoded.

        Note

        Callback is called with interrupts locked.

        Param type:
        :   Type. See [mipi\_stp\_decoder\_ctrl\_type](#group__mipi__stp__decoder__apis_1ga6e1f4b66b14ab44e549292f97046a50d).

        Param data:
        :   Data. Data associated with a given `type`.

        Param ts:
        :   Timestamp. Present if not NULL.

        Param marked:
        :   Set to true if opcode was marked.

    Enums

    enum mipi\_stp\_decoder\_ctrl\_type
    :   STPv2 opcodes.

        *Values:*

        enumerator STP\_DATA4 = 1

        enumerator STP\_DATA8 = 2

        enumerator STP\_DATA16 = 4

        enumerator STP\_DATA32 = 8

        enumerator STP\_DATA64 = 16

        enumerator STP\_DECODER\_NULL = 128

        enumerator STP\_DECODER\_MASTER

        enumerator STP\_DECODER\_MERROR

        enumerator STP\_DECODER\_CHANNEL

        enumerator STP\_DECODER\_VERSION

        enumerator STP\_DECODER\_FREQ

        enumerator STP\_DECODER\_GERROR

        enumerator STP\_DECODER\_FLAG

        enumerator STP\_DECODER\_ASYNC

        enumerator STP\_DECODER\_NOT\_SUPPORTED

    Functions

    int mipi\_stp\_decoder\_init(const struct [mipi\_stp\_decoder\_config](#c.mipi_stp_decoder_config) \*config)
    :   Initialize the decoder.

        Parameters:
        :   - **config** – Configuration.

        Return values:
        :   - **0** – On successful initialization.
            - **negative** – On failure.

    int mipi\_stp\_decoder\_decode(const uint8\_t \*data, size\_t len)
    :   Decode STPv2 stream.

        Function decodes the stream and calls the callback for every decoded element.

        Parameters:
        :   - **data** – Data.
            - **len** – Data length.

        Return values:
        :   - **0** – On successful decoding.
            - **negative** – On failure.

    void mipi\_stp\_decoder\_sync\_loss(void)
    :   Indicate synchronization loss.

        If detected, then decoder starts to look for ASYNC marker and drops all data until ASYNC is found. Synchronization can be lost when there is data loss (e.g. due to overflow).

    union mipi\_stp\_decoder\_data
    :   *#include <mipi\_stp\_decoder.h>*

        Union with data associated with a given STP opcode.

        Public Members

        uint16\_t id
        :   ID - used for master and channel.

        uint64\_t freq
        :   Frequency.

        uint32\_t ver
        :   Version.

        uint32\_t err
        :   Error code.

        uint32\_t dummy
        :   Dummy.

        uint64\_t data
        :   Data.

    struct mipi\_stp\_decoder\_config
    :   *#include <mipi\_stp\_decoder.h>*

        Decoder configuration.

        Public Members

        bool start\_out\_of\_sync
        :   Indicates that decoder start in out of sync state.

        [mipi\_stp\_decoder\_cb](#c.mipi_stp_decoder_cb) cb
        :   Callback.
