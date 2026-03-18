---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/gptp.html
original_path: connectivity/networking/api/gptp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# generic Precision Time Protocol (gPTP)

## [Overview](#id1)

This gPTP stack supports the protocol and procedures as defined in
the [IEEE 802.1AS-2011 standard](https://standards.ieee.org/findstds/standard/802.1AS-2011.html) (Timing and Synchronization for
Time-Sensitive Applications in Bridged Local Area Networks).

## [Supported features](#id2)

The stack handles communications and state machines defined in the
[IEEE 802.1AS-2011 standard](https://standards.ieee.org/findstds/standard/802.1AS-2011.html). Mandatory requirements for a full-duplex
point-to-point link endpoint, as defined in Annex A of the standard,
are supported.

The stack is in principle capable of handling communications on multiple network
interfaces (also defined as “ports” in the standard) and thus act as
a 802.1AS bridge. However, this mode of operation has not been validated on
the Zephyr OS.

## [Supported hardware](#id3)

Although the stack itself is hardware independent, Ethernet frame timestamping
support must be enabled in ethernet drivers.

Boards supported:

- [NXP FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm-k64f)
- [ST Nucleo H743ZI](../../../boards/st/nucleo_h743zi/doc/index.md#nucleo-h743zi-board)
- [ST Nucleo H745ZI-Q](../../../boards/st/nucleo_h745zi_q/doc/index.md#nucleo-h745zi-q-board)
- [ST Nucleo F767ZI](../../../boards/st/nucleo_f767zi/doc/index.md#nucleo-f767zi-board)
- [SAM E70(B) Xplained](../../../boards/atmel/sam/sam_e70_xplained/doc/index.md#sam-e70-xplained)
- [Native simulator - native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) (only usable for simple testing, limited capabilities
  due to lack of hardware clock)
- [X86 Emulation (QEMU)](../../../boards/qemu/x86/doc/index.md#qemu-x86) (emulated, limited capabilities due to lack of hardware clock)

## [Enabling the stack](#id4)

The following configuration option must me enabled in `prj.conf` file.

- [`CONFIG_NET_GPTP`](../../../kconfig.md#CONFIG_NET_GPTP "CONFIG_NET_GPTP")

## [Application interfaces](#id5)

Only two Application Interfaces as defined in section 9 of the standard
are available:

- `ClockTargetPhaseDiscontinuity` interface ([`gptp_register_phase_dis_cb()`](#c.gptp_register_phase_dis_cb))
- `ClockTargetEventCapture` interface ([`gptp_event_capture()`](#c.gptp_event_capture))

## [Testing](#id6)

The stack has been informally tested using the
[OpenAVnu gPTP](https://github.com/AVnu/gptp) and
[Linux ptp4l](http://linuxptp.sourceforge.net/) daemons.
The [gPTP sample application](../../../samples/net/gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.") from the Zephyr
source distribution can be used for testing.

## [API Reference](#id7)

Related code samples

[gPTP](../../../samples/net/gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.")
:   Enable gPTP support and monitor functionality using net-shell.

*group* gPTP support
:   generic Precision Time Protocol (gPTP) support

    Typedefs

    typedef void (\*gptp\_phase\_dis\_callback\_t)(uint8\_t \*gm\_identity, uint16\_t \*time\_base, struct [gptp\_scaled\_ns](#c.gptp_scaled_ns) \*last\_gm\_ph\_change, double \*last\_gm\_freq\_change)
    :   Define callback that is called after a phase discontinuity has been sent by the grandmaster.

        Param gm\_identity:
        :   A pointer to first element of a ClockIdentity array. The size of the array is GPTP\_CLOCK\_ID\_LEN.

        Param time\_base:
        :   A pointer to the value of timeBaseIndicator of the current grandmaster.

        Param last\_gm\_ph\_change:
        :   A pointer to the value of lastGmPhaseChange received from grandmaster.

        Param last\_gm\_freq\_change:
        :   A pointer to the value of lastGmFreqChange received from the grandmaster.

    typedef void (\*gptp\_port\_cb\_t)(int port, struct [net\_if](net_if.md#c.net_if "net_if") \*iface, void \*user\_data)
    :   Callback used while iterating over gPTP ports.

        Param port:
        :   Port number

        Param iface:
        :   Pointer to network interface

        Param user\_data:
        :   A valid pointer to user data or NULL

    Functions

    void gptp\_register\_phase\_dis\_cb(struct [gptp\_phase\_dis\_cb](#c.gptp_phase_dis_cb) \*phase\_dis, [gptp\_phase\_dis\_callback\_t](#c.gptp_phase_dis_callback_t) cb)
    :   Register a phase discontinuity callback.

        Parameters:
        :   - **phase\_dis** – Caller specified handler for the callback.
            - **cb** – Callback to register.

    void gptp\_unregister\_phase\_dis\_cb(struct [gptp\_phase\_dis\_cb](#c.gptp_phase_dis_cb) \*phase\_dis)
    :   Unregister a phase discontinuity callback.

        Parameters:
        :   - **phase\_dis** – Caller specified handler for the callback.

    void gptp\_call\_phase\_dis\_cb(void)
    :   Call a phase discontinuity callback function.

    int gptp\_event\_capture(struct [net\_ptp\_time](ptp_time.md#c.net_ptp_time "net_ptp_time") \*slave\_time, bool \*gm\_present)
    :   Get gPTP time.

        Parameters:
        :   - **slave\_time** – A pointer to structure where timestamp will be saved.
            - **gm\_present** – A pointer to a boolean where status of the presence of a grand master will be saved.

        Returns:
        :   Error code. 0 if no error.

    char \*gptp\_sprint\_clock\_id(const uint8\_t \*clk\_id, char \*output, size\_t output\_len)
    :   Utility function to print clock id to a user supplied buffer.

        Parameters:
        :   - **clk\_id** – Clock id
            - **output** – Output buffer
            - **output\_len** – Output buffer len

        Returns:
        :   Pointer to output buffer

    void gptp\_foreach\_port([gptp\_port\_cb\_t](#c.gptp_port_cb_t) cb, void \*user\_data)
    :   Go through all the gPTP ports and call callback for each of them.

        Parameters:
        :   - **cb** – User-supplied callback function to call
            - **user\_data** – User specified data

    struct gptp\_domain \*gptp\_get\_domain(void)
    :   Get gPTP domain.

        This contains all the configuration / status of the gPTP domain.

        Returns:
        :   Pointer to domain or NULL if not found.

    void gptp\_clk\_src\_time\_invoke(struct [gptp\_clk\_src\_time\_invoke\_params](#c.gptp_clk_src_time_invoke_params) \*arg)
    :   This interface is used by the ClockSource entity to provide time to the ClockMaster entity of a time-aware system.

        Parameters:
        :   - **arg** – Current state and parameters of the ClockSource entity.

    struct [gptp\_hdr](#c.gptp_hdr) \*gptp\_get\_hdr(struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Return pointer to gPTP packet header in network packet.

        Parameters:
        :   - **pkt** – Network packet (received or sent)

        Returns:
        :   Pointer to gPTP header.

    struct gptp\_scaled\_ns
    :   *#include <gptp.h>*

        Scaled Nanoseconds.

        Public Members

        int32\_t high
        :   High half.

        int64\_t low
        :   Low half.

    struct gptp\_uscaled\_ns
    :   *#include <gptp.h>*

        UScaled Nanoseconds.

        Public Members

        uint32\_t high
        :   High half.

        uint64\_t low
        :   Low half.

    struct gptp\_port\_identity
    :   *#include <gptp.h>*

        Port Identity.

        Public Members

        uint8\_t clk\_id[GPTP\_CLOCK\_ID\_LEN]
        :   Clock identity of the port.

        uint16\_t port\_number
        :   Number of the port.

    struct gptp\_flags
    :   *#include <gptp.h>*

        gPTP message flags

        Public Members

        uint8\_t octets[2]
        :   Byte access.

        uint16\_t all
        :   Whole field access.

    struct gptp\_hdr
    :   *#include <gptp.h>*

        gPTP message header

        Public Members

        uint8\_t message\_type
        :   Type of the message.

        uint8\_t transport\_specific
        :   Transport specific, always 1.

        uint8\_t ptp\_version
        :   Version of the PTP, always 2.

        uint8\_t reserved0
        :   Reserved field.

        uint16\_t message\_length
        :   Total length of the message from the header to the last TLV.

        uint8\_t domain\_number
        :   Domain number, always 0.

        uint8\_t reserved1
        :   Reserved field.

        struct [gptp\_flags](#c.gptp_flags) flags
        :   Message flags.

        int64\_t correction\_field
        :   Correction Field.

            The content depends of the message type.

        uint32\_t reserved2
        :   Reserved field.

        struct [gptp\_port\_identity](#c.gptp_port_identity) port\_id
        :   Port Identity of the sender.

        uint16\_t sequence\_id
        :   Sequence Id.

        uint8\_t control
        :   Control value.

            Sync: 0, Follow-up: 2, Others: 5.

        int8\_t log\_msg\_interval
        :   Message Interval in Log2 for Sync and Announce messages.

    struct gptp\_phase\_dis\_cb
    :   *#include <gptp.h>*

        Phase discontinuity callback structure.

        Stores the phase discontinuity callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node information for the slist.

        [gptp\_phase\_dis\_callback\_t](#c.gptp_phase_dis_callback_t) cb
        :   Phase discontinuity callback.

    struct gptp\_clk\_src\_time\_invoke\_params
    :   *#include <gptp.h>*

        ClockSourceTime.invoke function parameters.

        Parameters passed by ClockSourceTime.invoke function.

        Public Members

        double last\_gm\_freq\_change
        :   Frequency change on the last Time Base Indicator Change.

        struct [net\_ptp\_extended\_time](ptp_time.md#c.net_ptp_extended_time "net_ptp_extended_time") src\_time
        :   The time this function is invoked.

        struct [gptp\_scaled\_ns](#c.gptp_scaled_ns) last\_gm\_phase\_change
        :   Phase change on the last Time Base Indicator Change.

        uint16\_t time\_base\_indicator
        :   Time Base - changed only if Phase or Frequency changes.
