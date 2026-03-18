---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/tcpc.html
original_path: hardware/peripherals/tcpc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB Type-C Port Controller (TCPC)

## Overview

[TCPC](https://www.usb.org/document-library/usb-type-cr-port-controller-interface-specification) (USB Type-C Port Controller)
The TCPC is a device used to simplify the implementation of a USB-C system
by providing the following three function:

- VBUS and VCONN control [USB Type-C](https://www.usb.org/document-library/usb-type-cr-cable-and-connector-specification-revision-21):
  The TCPC may provide a Source device, the mechanism to control VBUS sourcing,
  and a Sink device, the mechanism to control VBUS sinking. A similar mechanism
  is provided for the control of VCONN.
- CC control and sensing:
  The TCPC implements logic for controlling the CC pin pull-up and pull-down
  resistors. It also provides a way to sense and report what resistors are
  present on the CC pin.
- Power Delivery message reception and transmission [USB Power Delivery](https://www.usb.org/document-library/usb-power-delivery):
  The TCPC sends and receives messages constructed in the TCPM and places them
  on the CC lines.

### TCPC API

The TCPC device driver functions as the liaison between the TCPC device and the
application software; this is accomplished by the Zephyr’s API provided by the
device driver that’s used to communicate with and control the TCPC device.

## Configuration Options

Related configuration options:

- [`CONFIG_USBC_TCPC_DRIVER`](../../kconfig.md#CONFIG_USBC_TCPC_DRIVER "CONFIG_USBC_TCPC_DRIVER")

## API Reference

*group* USB Type-C
:   USB Type-C.

    Defines

    TC\_V\_SINK\_DISCONNECT\_MIN\_MV
    :   VBUS minimum for a sink disconnect detection.

        See Table 4-3 VBUS Sink Characteristics

    TC\_V\_SINK\_DISCONNECT\_MAX\_MV
    :   VBUS maximum for a sink disconnect detection.

        See Table 4-3 VBUS Sink Characteristics

    TC\_T\_VBUS\_ON\_MAX\_MS
    :   From entry to Attached.SRC until VBUS reaches the minimum vSafe5V threshold as measured at the source’s receptacle See Table 4-29 VBUS and VCONN Timing Parameters.

    TC\_T\_VBUS\_OFF\_MAX\_MS
    :   From the time the Sink is detached until the Source removes VBUS and reaches vSafe0V (See USB PD).

        See Table 4-29 VBUS and VCONN Timing Parameters

    TC\_T\_VCONN\_ON\_MAX\_MS
    :   From the time the Source supplied VBUS in the Attached.SRC state.

        See Table 4-29 VBUS and VCONN Timing Parameters

    TC\_T\_VCONN\_ON\_PA\_MAX\_MS
    :   From the time a Sink with accessory support enters the PoweredAccessory state until the Sink sources minimum VCONN voltage (see Table 4-5) See Table 4-29 VBUS and VCONN Timing Parameters.

    TC\_T\_VCONN\_OFF\_MAX\_MS
    :   From the time that a Sink is detached or as directed until the VCONN supply is disconnected.

        See Table 4-29 VBUS and VCONN Timing Parameters

    TC\_T\_SINK\_ADJ\_MAX\_MS
    :   Response time for a Sink to adjust its current consumption to be in the specified range due to a change in USB Type-C Current advertisement See Table 4-29 VBUS and VCONN Timing Parameters.

    TC\_T\_DRP\_MIN\_MS
    :   The minimum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters.

    TC\_T\_DRP\_MAX\_MS
    :   The maximum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters.

    TC\_T\_DRP\_TRANSITION\_MIN\_MS
    :   The minimum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters.

    TC\_T\_DRP\_TRANSITION\_MAX\_MS
    :   The maximum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters.

    TC\_T\_DRP\_TRY\_MIN\_MS
    :   Minimum wait time associated with the Try.SRC state.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_DRP\_TRY\_MAX\_MS
    :   Maximum wait time associated with the Try.SRC state.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS
    :   Minimum wait time associated with the Try.SNK state.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS
    :   Maximum wait time associated with the Try.SNK state.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_TRY\_TIMEOUT\_MIN\_MS
    :   Minimum timeout for transition from Try.SRC to TryWait.SNK.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_TRY\_TIMEOUT\_MAX\_MS
    :   Maximum timeout for transition from Try.SRC to TryWait.SNK.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_VPD\_DETACH\_MIN\_MS
    :   Minimum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_VPD\_DETACH\_MAX\_MS
    :   Maximum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed.

        See Table 4-30 DRP Timing Parameters

    TC\_T\_CC\_DEBOUNCE\_MIN\_MS
    :   Minimum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing.

    TC\_T\_CC\_DEBOUNCE\_MAX\_MS
    :   Maximum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing.

    TC\_T\_PD\_DEBOUNCE\_MIN\_MS
    :   Minimum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions.

        See Table 4-31 CC Timing

    TC\_T\_PD\_DEBOUNCE\_MAX\_MS
    :   Maximum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions.

        See Table 4-31 CC Timing

    TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS
    :   Minimum Time a port shall wait before it can determine it is re-attached during the try-wait process.

        See Table 4-31 CC Timing

    TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS
    :   Maximum Time a port shall wait before it can determine it is re-attached during the try-wait process.

        See Table 4-31 CC Timing

    TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS
    :   Minimum time a self-powered port shall remain in the ErrorRecovery state.

        See Table 4-31 CC Timing

    TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS
    :   Minimum time a source shall remain in the ErrorRecovery state if it was sourcing VCONN in the previous state.

        See Table 4-31 CC Timing

    TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS
    :   Minimum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle.

        See Table 4-31 CC Timing

    TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS
    :   Maximum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle.

        See Table 4-31 CC Timing

    TC\_T\_SRC\_DISCONNECT\_MIN\_MS
    :   Minimum time a Source shall detect the SRC.Open state.

        The Source should detect the SRC.Open state as quickly as practical. See Table 4-31 CC Timing

    TC\_T\_SRC\_DISCONNECT\_MAX\_MS
    :   Maximum time a Source shall detect the SRC.Open state.

        The Source should detect the SRC.Open state as quickly as practical. See Table 4-31 CC Timing

    TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS
    :   Minimum time to detect connection when neither Port Partner is toggling.

        See Table 4-31 CC Timing

    TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS
    :   Maximum time to detect connection when neither Port Partner is toggling.

        See Table 4-31 CC Timing

    TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS
    :   Minimum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect).

        See Table 4-31 CC Timing

    TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS
    :   Maximum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect).

        See Table 4-31 CC Timing

    TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS
    :   Minimum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect).

        See Table 4-31 CC Timing

    TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS
    :   Maximum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect).

        See Table 4-31 CC Timing

    TC\_T\_VPDCTDD\_MIN\_US
    :   Minimum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC.

        See Table 4-31 CC Timing

    TC\_T\_VPDCTDD\_MAX\_MS
    :   Maximum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC.

        See Table 4-31 CC Timing

    TC\_T\_VPDDISABLE\_MIN\_MS
    :   Minimum time for a Charge-Through VCONN-Powered USB Device shall remain in CTDisabled.VPD state.

        See Table 4-31 CC Timing

    Enums

    enum tc\_cc\_voltage\_state
    :   CC Voltage status.

        *Values:*

        enumerator TC\_CC\_VOLT\_OPEN = 0
        :   No port partner connection.

        enumerator TC\_CC\_VOLT\_RA = 1
        :   Port partner is applying Ra.

        enumerator TC\_CC\_VOLT\_RD = 2
        :   Port partner is applying Rd.

        enumerator TC\_CC\_VOLT\_RP\_DEF = 5
        :   Port partner is applying Rp (0.5A).

        enumerator TC\_CC\_VOLT\_RP\_1A5 = 6

        enumerator TC\_CC\_VOLT\_RP\_3A0 = 7
        :   Port partner is applying Rp (3.0A).

    enum tc\_vbus\_level
    :   VBUS level voltages.

        *Values:*

        enumerator TC\_VBUS\_SAFE0V = 0
        :   VBUS is less than vSafe0V max.

        enumerator TC\_VBUS\_PRESENT = 1
        :   VBUS is at least vSafe5V min.

        enumerator TC\_VBUS\_REMOVED = 2
        :   VBUS is less than vSinkDisconnect max.

    enum tc\_rp\_value
    :   Pull-Up resistor values.

        *Values:*

        enumerator TC\_RP\_USB = 0
        :   Pull-Up resistor for a current of 900mA.

        enumerator TC\_RP\_1A5 = 1
        :   Pull-Up resistor for a current of 1.5A.

        enumerator TC\_RP\_3A0 = 2
        :   Pull-Up resistor for a current of 3.0A.

        enumerator TC\_RP\_RESERVED = 3
        :   No Pull-Up resistor is applied.

    enum tc\_cc\_pull
    :   CC pull resistors.

        *Values:*

        enumerator TC\_CC\_RA = 0
        :   Ra Pull-Down resistor.

        enumerator TC\_CC\_RP = 1
        :   Rp Pull-Up resistor.

        enumerator TC\_CC\_RD = 2
        :   Rd Pull-Down resistor.

        enumerator TC\_CC\_OPEN = 3
        :   No CC resistor.

        enumerator TC\_RA\_RD = 4
        :   Ra and Rd Pull-Down resistor.

    enum tc\_cable\_plug
    :   Cable plug.

        See 6.2.1.1.7 Cable Plug. Only applies to SOP’ and SOP”. Replaced by pd\_power\_role for SOP packets.

        *Values:*

        enumerator PD\_PLUG\_FROM\_DFP\_UFP = 0

        enumerator PD\_PLUG\_FROM\_CABLE\_VPD = 1

    enum tc\_power\_role
    :   Power Delivery Power Role.

        *Values:*

        enumerator TC\_ROLE\_SINK = 0
        :   Power role is a sink.

        enumerator TC\_ROLE\_SOURCE = 1
        :   Power role is a source.

    enum tc\_data\_role
    :   Power Delivery Data Role.

        *Values:*

        enumerator TC\_ROLE\_UFP = 0
        :   Data role is an Upstream Facing Port.

        enumerator TC\_ROLE\_DFP = 1
        :   Data role is a Downstream Facing Port.

        enumerator TC\_ROLE\_DISCONNECTED = 2
        :   Port is disconnected.

    enum tc\_cc\_polarity
    :   Polarity of the CC lines.

        *Values:*

        enumerator TC\_POLARITY\_CC1 = 0
        :   Use CC1 IO for Power Delivery communication.

        enumerator TC\_POLARITY\_CC2 = 1
        :   Use CC2 IO for Power Delivery communication.

    enum tc\_cc\_states
    :   Possible port partner connections based on CC line states.

        *Values:*

        enumerator TC\_CC\_NONE = 0
        :   No port partner attached.

        enumerator TC\_CC\_UFP\_NONE = 1
        :   From DFP perspective.

            No UFP accessory connected

        enumerator TC\_CC\_UFP\_AUDIO\_ACC = 2
        :   UFP Audio accessory connected.

        enumerator TC\_CC\_UFP\_DEBUG\_ACC = 3
        :   UFP Debug accessory connected.

        enumerator TC\_CC\_UFP\_ATTACHED = 4
        :   Plain UFP attached.

        enumerator TC\_CC\_DFP\_ATTACHED = 5
        :   From UFP perspective.

            Plain DFP attached

        enumerator TC\_CC\_DFP\_DEBUG\_ACC = 6
        :   DFP debug accessory connected.

*group* USB Type-C Port Controller API
:   USB Type-C Port Controller API.

    **Since**
    :   3.1

    **Version**
    :   0.1.0

    Typedefs

    typedef int (\*tcpc\_vconn\_control\_cb\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_cc\_polarity](#c.tc_cc_polarity) pol, bool enable)

    typedef int (\*tcpc\_vconn\_discharge\_cb\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_cc\_polarity](#c.tc_cc_polarity) pol, bool enable)

    typedef void (\*tcpc\_alert\_handler\_cb\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*data, enum [tcpc\_alert](#c.tcpc_alert) alert)

    Enums

    enum tcpc\_alert
    :   TCPC Alert bits.

        *Values:*

        enumerator TCPC\_ALERT\_CC\_STATUS
        :   CC status changed.

        enumerator TCPC\_ALERT\_POWER\_STATUS
        :   Power status changed.

        enumerator TCPC\_ALERT\_MSG\_STATUS
        :   Receive Buffer register changed.

        enumerator TCPC\_ALERT\_HARD\_RESET\_RECEIVED
        :   Received Hard Reset message.

        enumerator TCPC\_ALERT\_TRANSMIT\_MSG\_FAILED
        :   SOP\* message transmission not successful.

        enumerator TCPC\_ALERT\_TRANSMIT\_MSG\_DISCARDED
        :   Reset or SOP\* message transmission not sent due to an incoming receive message.

        enumerator TCPC\_ALERT\_TRANSMIT\_MSG\_SUCCESS
        :   Reset or SOP\* message transmission successful.

        enumerator TCPC\_ALERT\_VBUS\_ALARM\_HI
        :   A high-voltage alarm has occurred.

        enumerator TCPC\_ALERT\_VBUS\_ALARM\_LO
        :   A low-voltage alarm has occurred.

        enumerator TCPC\_ALERT\_FAULT\_STATUS
        :   A fault has occurred.

            Read the FAULT\_STATUS register

        enumerator TCPC\_ALERT\_RX\_BUFFER\_OVERFLOW
        :   TCPC RX buffer has overflowed.

        enumerator TCPC\_ALERT\_VBUS\_SNK\_DISCONNECT
        :   The TCPC in Attached.SNK state has detected a sink disconnect.

        enumerator TCPC\_ALERT\_BEGINNING\_MSG\_STATUS
        :   Receive buffer register changed.

        enumerator TCPC\_ALERT\_EXTENDED\_STATUS
        :   Extended status changed.

        enumerator TCPC\_ALERT\_EXTENDED
        :   An extended interrupt event has occurred.

            Read the alert\_extended register

        enumerator TCPC\_ALERT\_VENDOR\_DEFINED
        :   A vendor defined alert has been detected.

    enum tcpc\_status\_reg
    :   TCPC Status register.

        *Values:*

        enumerator TCPC\_CC\_STATUS
        :   The CC Status register.

        enumerator TCPC\_POWER\_STATUS
        :   The Power Status register.

        enumerator TCPC\_FAULT\_STATUS
        :   The Fault Status register.

        enumerator TCPC\_EXTENDED\_STATUS
        :   The Extended Status register.

        enumerator TCPC\_EXTENDED\_ALERT\_STATUS
        :   The Extended Alert Status register.

        enumerator TCPC\_VENDOR\_DEFINED\_STATUS
        :   The Vendor Defined Status register.

    Functions

    static inline int tcpc\_is\_cc\_rp(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc)
    :   Returns whether the sink has detected a Rp resistor on the other side.

    static inline int tcpc\_is\_cc\_open(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if both CC lines are completely open.

    static inline int tcpc\_is\_cc\_snk\_dbg\_acc(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if we detect the port partner is a snk debug accessory.

    static inline int tcpc\_is\_cc\_src\_dbg\_acc(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if we detect the port partner is a src debug accessory.

    static inline int tcpc\_is\_cc\_audio\_acc(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if the port partner is an audio accessory.

    static inline int tcpc\_is\_cc\_at\_least\_one\_rd(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if the port partner is presenting at least one Rd.

    static inline int tcpc\_is\_cc\_only\_one\_rd(enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) cc2)
    :   Returns true if the port partner is presenting Rd on only one CC line.

    static inline int tcpc\_init(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initializes the TCPC.

        Parameters:
        :   - **dev** – Runtime device structure

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-EAGAIN** – if initialization should be postponed

    static inline int tcpc\_get\_cc(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) \*cc1, enum [tc\_cc\_voltage\_state](#c.tc_cc_voltage_state) \*cc2)
    :   Reads the status of the CC lines.

        Parameters:
        :   - **dev** – Runtime device structure
            - **cc1** – A pointer where the CC1 status is written
            - **cc2** – A pointer where the CC2 status is written

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_select\_rp\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_rp\_value](#c.tc_rp_value) rp)
    :   Sets the value of CC pull up resistor used when operating as a Source.

        Parameters:
        :   - **dev** – Runtime device structure
            - **rp** – Value of the Pull-Up Resistor.

        Return values:
        :   - **0** – on success
            - **-ENOSYS** –
            - **-EIO** – on failure

    static inline int tcpc\_get\_rp\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_rp\_value](#c.tc_rp_value) \*rp)
    :   Gets the value of the CC pull up resistor used when operating as a Source.

        Parameters:
        :   - **dev** – Runtime device structure
            - **rp** – pointer where the value of the Pull-Up Resistor is stored

        Return values:
        :   - **0** – on success
            - **-ENOSYS** –
            - **-EIO** – on failure

    static inline int tcpc\_set\_cc(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_cc\_pull](#c.tc_cc_pull) pull)
    :   Sets the CC pull resistor and sets the role as either Source or Sink.

        Parameters:
        :   - **dev** – Runtime device structure
            - **pull** – The pull resistor to set

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure

    static inline void tcpc\_set\_vconn\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [tcpc\_vconn\_control\_cb\_t](#c.tcpc_vconn_control_cb_t) vconn\_cb)
    :   Sets a callback that can enable or disable VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC.

        The callback is called in the tcpc\_set\_vconn function if vconn\_cb isn’t NULL

        Parameters:
        :   - **dev** – Runtime device structure
            - **vconn\_cb** – pointer to the callback function that controls vconn

    static inline void tcpc\_set\_vconn\_discharge\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [tcpc\_vconn\_discharge\_cb\_t](#c.tcpc_vconn_discharge_cb_t) cb)
    :   Sets a callback that can enable or discharge VCONN if the TCPC is unable to or the system is configured in a way that does not use the VCONN control capabilities of the TCPC.

        The callback is called in the tcpc\_vconn\_discharge function if cb isn’t NULL

        Parameters:
        :   - **dev** – Runtime device structure
            - **cb** – pointer to the callback function that discharges vconn

    static inline int tcpc\_vconn\_discharge(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Discharges VCONN.

        This function uses the TCPC to discharge VCONN if possible or calls the callback function set by tcpc\_set\_vconn\_cb

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – VCONN discharge is enabled when true, it’s disabled

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_vconn(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Enables or disables VCONN.

        This function uses the TCPC to measure VCONN if possible or calls the callback function set by tcpc\_set\_vconn\_cb

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – VCONN is enabled when true, it’s disabled

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_roles(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_power\_role](#c.tc_power_role) power\_role, enum [tc\_data\_role](#c.tc_data_role) data\_role)
    :   Sets the Power and Data Role of the PD message header.

        This function only needs to be called once per data / power role change

        Parameters:
        :   - **dev** – Runtime device structure
            - **power\_role** – current power role
            - **data\_role** – current data role

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_get\_rx\_pending\_msg(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [pd\_msg](#c.pd_msg) \*buf)
    :   Retrieves the Power Delivery message from the TCPC.

        If buf is NULL, then only the status is returned, where 0 means there is a message pending and -ENODATA means there is no pending message.

        Parameters:
        :   - **dev** – Runtime device structure
            - **buf** – pointer where the pd\_buf pointer is written, NULL if only checking the status

        Return values:
        :   - **Greater** – or equal to 0 is the number of bytes received if buf parameter is provided
            - **0** – if there is a message pending and buf parameter is NULL
            - **-EIO** – on failure
            - **-ENODATA** – if no message is pending

    static inline int tcpc\_set\_rx\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Enables the reception of SOP\* message types.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – Enable Power Delivery when true, else it’s disabled

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_cc\_polarity(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_cc\_polarity](#c.tc_cc_polarity) polarity)
    :   Sets the polarity of the CC lines.

        Parameters:
        :   - **dev** – Runtime device structure
            - **polarity** – Polarity of the cc line

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure

    static inline int tcpc\_transmit\_data(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [pd\_msg](#c.pd_msg) \*msg)
    :   Transmits a Power Delivery message.

        Parameters:
        :   - **dev** – Runtime device structure
            - **msg** – Power Delivery message to transmit

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_dump\_std\_reg(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Dump a set of TCPC registers.

        Parameters:
        :   - **dev** – Runtime device structure

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_alert\_handler\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [tcpc\_alert\_handler\_cb\_t](#c.tcpc_alert_handler_cb_t) handler, void \*data)
    :   Sets the alert function that’s called when an interrupt is triggered due to an alert bit.

        Calling this function enables the particular alert bit

        Parameters:
        :   - **dev** – Runtime device structure
            - **handler** – The callback function called when the bit is set
            - **data** – user data passed to the callback

        Return values:
        :   - **0** – on success
            - **-EINVAL** – on failure

    static inline int tcpc\_get\_status\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tcpc\_status\_reg](#c.tcpc_status_reg) reg, int32\_t \*status)
    :   Gets a status register.

        Parameters:
        :   - **dev** – Runtime device structure
            - **reg** – The status register to read
            - **status** – Pointer where the status is stored

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_clear\_status\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tcpc\_status\_reg](#c.tcpc_status_reg) reg, uint32\_t mask)
    :   Clears a TCPC status register.

        Parameters:
        :   - **dev** – Runtime device structure
            - **reg** – The status register to read
            - **mask** – A bit mask of the status register to clear. A status bit is cleared when it’s set to 1.

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_mask\_status\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tcpc\_status\_reg](#c.tcpc_status_reg) reg, uint32\_t mask)
    :   Sets the mask of a TCPC status register.

        Parameters:
        :   - **dev** – Runtime device structure
            - **reg** – The status register to read
            - **mask** – A bit mask of the status register to mask. The status bit is masked if it’s 0, else it’s unmasked.

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_debug\_accessory(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Manual control of TCPC DebugAccessory control.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – Enable Debug Accessory when true, else it’s disabled

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_debug\_detach(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Detach from a debug connection.

        Parameters:
        :   - **dev** – Runtime device structure

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_drp\_toggle(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Enable TCPC auto dual role toggle.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – Auto dual role toggle is active when true, else it’s disabled

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_get\_snk\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Queries the current sinking state of the TCPC.

        Parameters:
        :   - **dev** – Runtime device structure

        Return values:
        :   - **true** – if sinking power
            - **false** – if not sinking power
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_snk\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Set the VBUS sinking state of the TCPC.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – True if sinking should be enabled, false if disabled

        Return values:
        :   - **0** – on success
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_get\_src\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Queries the current sourcing state of the TCPC.

        Parameters:
        :   - **dev** – Runtime device structure

        Return values:
        :   - **true** – if sourcing power
            - **false** – if not sourcing power
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_src\_ctrl(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Set the VBUS sourcing state of the TCPC.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – True if sourcing should be enabled, false if disabled

        Return values:
        :   - **0** – on success
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_bist\_test\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Controls the BIST Mode of the TCPC.

        It disables RX alerts while the mode is active.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – The TCPC enters BIST TEST Mode when true

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_get\_chip\_info(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [tcpc\_chip\_info](#c.tcpc_chip_info) \*chip\_info)
    :   Gets the TCPC firmware version.

        Parameters:
        :   - **dev** – Runtime device structure
            - **chip\_info** – Pointer to TCPC chip info where the version is stored

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_set\_low\_power\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Instructs the TCPC to enter or exit low power mode.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – The TCPC enters low power mode when true, else it exits it

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    static inline int tcpc\_sop\_prime\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Enables the reception of SOP Prime messages.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – Can receive SOP Prime messages when true, else it can not

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOSYS** – if not implemented

    struct tcpc\_chip\_info
    :   *#include <usbc\_tcpc.h>*

        TCPC Chip Information.

        Public Members

        uint16\_t vendor\_id
        :   Vendor Id.

        uint16\_t product\_id
        :   Product Id.

        uint16\_t device\_id
        :   Device Id.

        uint64\_t fw\_version\_number
        :   Firmware version number.

        uint8\_t min\_req\_fw\_version\_string[8]
        :   Minimum Required firmware version string.

        uint64\_t min\_req\_fw\_version\_number
        :   Minimum Required firmware version number.

    struct tcpc\_driver\_api
    :   *#include <usbc\_tcpc.h>*

*group* USB Power Delivery
:   USB Power Delivery.

    USB PD 3.1 Rev 1.6, Table 6-70 Counter Parameters

    PD\_N\_CAPS\_COUNT
    :   The CapsCounter is used to count the number of Source\_Capabilities Messages which have been sent by a Source at power up or after a Hard Reset.

        Parameter Name: nCapsCounter

    PD\_N\_HARD\_RESET\_COUNT
    :   The HardResetCounter is used to retry the Hard Reset whenever there is no response from the remote device (see Section 6.6.6) Parameter Name: nHardResetCounter.

    USB PD 3.1 Rev 1.6, Table 6-68 Time Values

    PD\_T\_NO\_RESPONSE\_MIN\_MS
    :   The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset.

        Parameter Name: tNoResponseTimer

    PD\_T\_NO\_RESPONSE\_MAX\_MS
    :   The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset.

        Parameter Name: tNoResponseTimer

    PD\_T\_PS\_HARD\_RESET\_MIN\_MS
    :   Min time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset.

    PD\_T\_PS\_HARD\_RESET\_MAX\_MS
    :   Max time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset.

    PD\_T\_SINK\_TX\_MIN\_MS
    :   Minimum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message.

        Parameter Name: tSinkTx

    PD\_T\_SINK\_TX\_MAX\_MS
    :   Maximum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message.

        Parameter Name: tSinkTx

    PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS
    :   Minimum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached.

        2) The Source is not in an active connection with a PD Sink Port. Parameter Name: tTypeCSendSourceCap

    PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS
    :   Maximum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached.

        2) The Source is not in an active connection with a PD Sink Port. Parameter Name: tTypeCSendSourceCap

    Defines

    PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN
    :   Maximum length of a non-Extended Message in bytes.

        See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgLegacyLen

    PD\_MAX\_EXTENDED\_MSG\_LEN
    :   Maximum length of an Extended Message in bytes.

        See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgLen

    PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN
    :   Maximum length of a Chunked Message in bytes.

        When one of both Port Partners do not support Extended Messages of Data Size greater than PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN then the Protocol Layer supports a Chunking mechanism to break larger Messages into smaller Chunks of size PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN. See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgChunkLen

    PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS
    :   Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap.

    PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS
    :   Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap.

    PD\_V\_SAFE\_0V\_MAX\_MV
    :   VBUS maximum safe operating voltage at “zero volts”.

        See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: vSafe0V

    PD\_V\_SAFE\_5V\_MIN\_MV
    :   VBUS minimum safe operating voltage at 5V.

        See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: vSafe5V

    PD\_T\_SAFE\_0V\_MAX\_MS
    :   Time to reach PD\_V\_SAFE\_0V\_MV max in milliseconds.

        See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: tSafe0V

    PD\_T\_SAFE\_5V\_MAX\_MS
    :   Time to reach PD\_V\_SAFE\_5V\_MV max in milliseconds.

        See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: tSafe5V

    PD\_T\_TX\_TIMEOUT\_MS
    :   Time to wait for TCPC to complete transmit.

    PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS
    :   Minimum time a Hard Reset must complete.

        See Table 6-68 Time Values

    PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS
    :   Maximum time a Hard Reset must complete.

        See Table 6-68 Time Values

    PD\_T\_SENDER\_RESPONSE\_MIN\_MS
    :   Minimum time a response must be sent from a Port Partner See Table 6-68 Time Values.

    PD\_T\_SENDER\_RESPONSE\_NOM\_MS
    :   Nomiminal time a response must be sent from a Port Partner See Table 6-68 Time Values.

    PD\_T\_SENDER\_RESPONSE\_MAX\_MS
    :   Maximum time a response must be sent from a Port Partner See Table 6-68 Time Values.

    PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS
    :   Minimum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS
    :   Nominal SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS
    :   Maximum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS
    :   Minimum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS
    :   Nominal EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS
    :   Maximum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

    PD\_T\_SINK\_REQUEST\_MIN\_MS
    :   Minimum time to wait before sending another request after receiving a Wait message See Table 6-68 Time Values.

    PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS
    :   Minimum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

    PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS
    :   Nominal time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

    PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS
    :   Maximum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

    PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT(c)
    :   Convert bytes to PD Header data object count, where a data object is 4-bytes.

        Parameters:
        :   - **c** – number of bytes to convert

    PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES(c)
    :   Convert PD Header data object count to bytes.

        Parameters:
        :   - **c** – number of PD Header data objects

    SINK\_TX\_OK
    :   Collision avoidance Rp values in REV 3.0 Sink Transmit “OK”.

    SINK\_TX\_NG
    :   Collision avoidance Rp values in REV 3.0 Sink Transmit “NO GO”.

    PD\_GET\_EXT\_HEADER(c)
    :   Used to get extended header from the first 32-bit word of the message.

        Parameters:
        :   - **c** – first 32-bit word of the message

    PDO\_MAX\_DATA\_OBJECTS
    :   PDO - Power Data Object RDO - Request Data Object.

        Maximum number of 32-bit data objects sent in a single request

    PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT(c)
    :   Convert milliamps to Fixed PDO Current in 10mA units.

        Parameters:
        :   - **c** – Current in milliamps

    PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE(v)
    :   Convert millivolts to Fixed PDO Voltage in 50mV units.

        Parameters:
        :   - **v** – Voltage in millivolts

    PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA(c)
    :   Convert a Fixed PDO Current from 10mA units to milliamps.

        Parameters:
        :   - **c** – Fixed PDO current in 10mA units.

    PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV(v)
    :   Convert a Fixed PDO Voltage from 50mV units to millivolts.

        Used for converting [pd\_fixed\_supply\_pdo\_source.voltage](#unionpd__fixed__supply__pdo__source_1a66f55e177b6f2bc76b392707e39fa4fe) and [pd\_fixed\_supply\_pdo\_sink.voltage](#unionpd__fixed__supply__pdo__sink_1ac47dcf98dfca90eb0e6013a3e1c5eb18)

        Parameters:
        :   - **v** – Fixed PDO voltage in 50mV units.

    PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT(c)
    :   Convert milliamps to Variable PDO Current in 10ma units.

        Parameters:
        :   - **c** – Current in milliamps

    PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE(v)
    :   Convert millivolts to Variable PDO Voltage in 50mV units.

        Parameters:
        :   - **v** – Voltage in millivolts

    PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA(c)
    :   Convert a Variable PDO Current from 10mA units to milliamps.

        Parameters:
        :   - **c** – Variable PDO current in 10mA units.

    PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV(v)
    :   Convert a Variable PDO Voltage from 50mV units to millivolts.

        Parameters:
        :   - **v** – Variable PDO voltage in 50mV units.

    PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER(c)
    :   Convert milliwatts to Battery PDO Power in 250mW units.

        Parameters:
        :   - **c** – Power in milliwatts

    PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE(v)
    :   Convert milliwatts to Battery PDO Voltage in 50mV units.

        Parameters:
        :   - **v** – Voltage in millivolts

    PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW(c)
    :   Convert a Battery PDO Power from 250mW units to milliwatts.

        Parameters:
        :   - **c** – Power in 250mW units.

    PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV(v)
    :   Convert a Battery PDO Voltage from 50mV units to millivolts.

        Parameters:
        :   - **v** – Voltage in 50mV units.

    PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT(c)
    :   Convert milliamps to Augmented PDO Current in 50mA units.

        Parameters:
        :   - **c** – Current in milliamps

    PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE(v)
    :   Convert millivolts to Augmented PDO Voltage in 100mV units.

        Parameters:
        :   - **v** – Voltage in millivolts

    PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA(c)
    :   Convert an Augmented PDO Current from 50mA units to milliamps.

        Parameters:
        :   - **c** – Augmented PDO current in 50mA units.

    PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV(v)
    :   Convert an Augmented PDO Voltage from 100mV units to millivolts.

        Parameters:
        :   - **v** – Augmented PDO voltage in 100mV units.

    NUM\_SOP\_STAR\_TYPES
    :   Number of valid Transmit Types.

    Enums

    enum pdo\_type
    :   Power Data Object Type Table 6-7 Power Data Object.

        *Values:*

        enumerator PDO\_FIXED = 0
        :   Fixed supply (Vmin = Vmax).

        enumerator PDO\_BATTERY = 1
        :   Battery.

        enumerator PDO\_VARIABLE = 2
        :   Variable Supply (non-Battery).

        enumerator PDO\_AUGMENTED = 3
        :   Augmented Power Data Object (APDO).

    enum pd\_frs\_type
    :   Fast Role Swap Required for USB Type-C current.

        *Values:*

        enumerator FRS\_NOT\_SUPPORTED
        :   Fast Swap not supported.

        enumerator FRS\_DEFAULT\_USB\_POWER
        :   Default USB Power.

        enumerator FRS\_1P5A\_5V
        :   1.5A @ 5V

        enumerator FRS\_3P0A\_5V
        :   3.0A @ 5V

    enum pd\_rev\_type
    :   Protocol revision.

        *Values:*

        enumerator PD\_REV10 = 0
        :   PD revision 1.0.

        enumerator PD\_REV20 = 1
        :   PD revision 2.0.

        enumerator PD\_REV30 = 2
        :   PD revision 3.0.

    enum pd\_packet\_type
    :   Power Delivery packet type See USB Type-C Port Controller Interface Specification, Revision 2.0, Version 1.2, Table 4-38 TRANSMIT Register Definition.

        *Values:*

        enumerator PD\_PACKET\_SOP = 0
        :   Port Partner message.

        enumerator PD\_PACKET\_SOP\_PRIME = 1
        :   Cable Plug message.

        enumerator PD\_PACKET\_PRIME\_PRIME = 2
        :   Cable Plug message far end.

        enumerator PD\_PACKET\_DEBUG\_PRIME = 3
        :   Currently undefined in the PD specification.

        enumerator PD\_PACKET\_DEBUG\_PRIME\_PRIME = 4
        :   Currently undefined in the PD specification.

        enumerator PD\_PACKET\_TX\_HARD\_RESET = 5
        :   Hard Reset message to the Port Partner.

        enumerator PD\_PACKET\_CABLE\_RESET = 6
        :   Cable Reset message to the Cable.

        enumerator PD\_PACKET\_TX\_BIST\_MODE\_2 = 7
        :   BIST\_MODE\_2 message to the Port Partner.

        enumerator PD\_PACKET\_MSG\_INVALID = 0xf
        :   USED ONLY FOR RECEPTION OF UNKNOWN MSG TYPES.

    enum pd\_ctrl\_msg\_type
    :   Control Message type See Table 6-5 Control Message Types.

        *Values:*

        enumerator PD\_CTRL\_GOOD\_CRC = 1
        :   0 Reserved

            GoodCRC Message

        enumerator PD\_CTRL\_GOTO\_MIN = 2
        :   GotoMin Message.

        enumerator PD\_CTRL\_ACCEPT = 3
        :   Accept Message.

        enumerator PD\_CTRL\_REJECT = 4
        :   Reject Message.

        enumerator PD\_CTRL\_PING = 5
        :   Ping Message.

        enumerator PD\_CTRL\_PS\_RDY = 6
        :   PS\_RDY Message.

        enumerator PD\_CTRL\_GET\_SOURCE\_CAP = 7
        :   Get\_Source\_Cap Message.

        enumerator PD\_CTRL\_GET\_SINK\_CAP = 8
        :   Get\_Sink\_Cap Message.

        enumerator PD\_CTRL\_DR\_SWAP = 9
        :   DR\_Swap Message.

        enumerator PD\_CTRL\_PR\_SWAP = 10
        :   PR\_Swap Message.

        enumerator PD\_CTRL\_VCONN\_SWAP = 11
        :   VCONN\_Swap Message.

        enumerator PD\_CTRL\_WAIT = 12
        :   Wait Message.

        enumerator PD\_CTRL\_SOFT\_RESET = 13
        :   Soft Reset Message.

        enumerator PD\_CTRL\_DATA\_RESET = 14
        :   Used for REV 3.0.

            Data\_Reset Message

        enumerator PD\_CTRL\_DATA\_RESET\_COMPLETE = 15
        :   Data\_Reset\_Complete Message.

        enumerator PD\_CTRL\_NOT\_SUPPORTED = 16
        :   Not\_Supported Message.

        enumerator PD\_CTRL\_GET\_SOURCE\_CAP\_EXT = 17
        :   Get\_Source\_Cap\_Extended Message.

        enumerator PD\_CTRL\_GET\_STATUS = 18
        :   Get\_Status Message.

        enumerator PD\_CTRL\_FR\_SWAP = 19
        :   FR\_Swap Message.

        enumerator PD\_CTRL\_GET\_PPS\_STATUS = 20
        :   Get\_PPS\_Status Message.

        enumerator PD\_CTRL\_GET\_COUNTRY\_CODES = 21
        :   Get\_Country\_Codes Message.

        enumerator PD\_CTRL\_GET\_SINK\_CAP\_EXT = 22
        :   Get\_Sink\_Cap\_Extended Message.

    enum pd\_data\_msg\_type
    :   Data message type See Table 6-6 Data Message Types.

        *Values:*

        enumerator PD\_DATA\_SOURCE\_CAP = 1
        :   0 Reserved

            Source\_Capabilities Message

        enumerator PD\_DATA\_REQUEST = 2
        :   Request Message.

        enumerator PD\_DATA\_BIST = 3
        :   BIST Message.

        enumerator PD\_DATA\_SINK\_CAP = 4
        :   Sink Capabilities Message.

        enumerator PD\_DATA\_BATTERY\_STATUS = 5
        :   5-14 Reserved for REV 2.0

        enumerator PD\_DATA\_ALERT = 6
        :   Alert Message.

        enumerator PD\_DATA\_GET\_COUNTRY\_INFO = 7
        :   Get Country Info Message.

        enumerator PD\_DATA\_ENTER\_USB = 8
        :   8-14 Reserved for REV 3.0

            Enter USB message

        enumerator PD\_DATA\_VENDOR\_DEF = 15
        :   Vendor Defined Message.

    enum pd\_ext\_msg\_type
    :   Extended message type for REV 3.0 See Table 6-48 Extended Message Types.

        *Values:*

        enumerator PD\_EXT\_SOURCE\_CAP = 1
        :   0 Reserved

            Source\_Capabilities\_Extended Message

        enumerator PD\_EXT\_STATUS = 2
        :   Status Message.

        enumerator PD\_EXT\_GET\_BATTERY\_CAP = 3
        :   Get\_Battery\_Cap Message.

        enumerator PD\_EXT\_GET\_BATTERY\_STATUS = 4
        :   Get\_Battery\_Status Message.

        enumerator PD\_EXT\_BATTERY\_CAP = 5
        :   Battery\_Capabilities Message.

        enumerator PD\_EXT\_GET\_MANUFACTURER\_INFO = 6
        :   Get\_Manufacturer\_Info Message.

        enumerator PD\_EXT\_MANUFACTURER\_INFO = 7
        :   Manufacturer\_Info Message.

        enumerator PD\_EXT\_SECURITY\_REQUEST = 8
        :   Security\_Request Message.

        enumerator PD\_EXT\_SECURITY\_RESPONSE = 9
        :   Security\_Response Message.

        enumerator PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST = 10
        :   Firmware\_Update\_Request Message.

        enumerator PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE = 11
        :   Firmware\_Update\_Response Message.

        enumerator PD\_EXT\_PPS\_STATUS = 12
        :   PPS\_Status Message.

        enumerator PD\_EXT\_COUNTRY\_INFO = 13
        :   Country\_Codes Message.

        enumerator PD\_EXT\_COUNTRY\_CODES = 14
        :   Country\_Info Message.

    enum usbpd\_cc\_pin
    :   Active PD CC pin.

        *Values:*

        enumerator USBPD\_CC\_PIN\_1 = 0
        :   PD is active on CC1.

        enumerator USBPD\_CC\_PIN\_2 = 1
        :   PD is active on CC2.

    union pd\_header
    :   *#include <usbc\_pd.h>*

        Build a PD message header See Table 6-1 Message Header.

        Public Members

        uint16\_t message\_type
        :   Type of message.

        uint16\_t port\_data\_role
        :   Port Data role.

        uint16\_t specification\_revision
        :   Specification Revision.

        uint16\_t port\_power\_role
        :   Port Power Role.

        uint16\_t message\_id
        :   Message ID.

        uint16\_t number\_of\_data\_objects
        :   Number of Data Objects.

        uint16\_t extended
        :   Extended Message.

        struct [pd\_header](#c.pd_header).[anonymous] [anonymous]

        uint16\_t raw\_value

    union pd\_ext\_header
    :   *#include <usbc\_pd.h>*

        Build an extended message header See Table 6-3 Extended Message Header.

        Public Members

        uint16\_t data\_size
        :   Number of total bytes in data block.

        uint16\_t reserved0
        :   Reserved.

        uint16\_t request\_chunk
        :   1 for a chunked message, else 0

        uint16\_t chunk\_number
        :   Chunk number when chkd = 1, else 0.

        uint16\_t chunked
        :   1 for chunked messages

        struct [pd\_ext\_header](#c.pd_ext_header).[anonymous] [anonymous]

        uint16\_t raw\_value
        :   Raw PD Ext Header value.

    union pd\_fixed\_supply\_pdo\_source
    :   *#include <usbc\_pd.h>*

        Create a Fixed Supply PDO Source value See Table 6-9 Fixed Supply PDO - Source.

        Public Members

        uint32\_t max\_current
        :   Maximum Current in 10mA units.

        uint32\_t voltage
        :   Voltage in 50mV units.

        uint32\_t peak\_current
        :   Peak Current.

        uint32\_t reserved0
        :   Reserved – Shall be set to zero.

        uint32\_t unchunked\_ext\_msg\_supported
        :   Unchunked Extended Messages Supported.

        uint32\_t dual\_role\_data
        :   Dual-Role Data.

        uint32\_t usb\_comms\_capable
        :   USB Communications Capable.

        uint32\_t unconstrained\_power
        :   Unconstrained Power.

        uint32\_t usb\_suspend\_supported
        :   USB Suspend Supported.

        uint32\_t dual\_role\_power
        :   Dual-Role Power.

        enum [pdo\_type](#c.pdo_type) type
        :   Fixed supply.

            SET TO PDO\_FIXED

        struct [pd\_fixed\_supply\_pdo\_source](#c.pd_fixed_supply_pdo_source).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_fixed\_supply\_pdo\_sink
    :   *#include <usbc\_pd.h>*

        Create a Fixed Supply PDO Sink value See Table 6-14 Fixed Supply PDO - Sink.

        Public Members

        uint32\_t operational\_current
        :   Operational Current in 10mA units.

        uint32\_t voltage
        :   Voltage in 50mV units.

        uint32\_t reserved0
        :   Reserved – Shall be set to zero.

        enum [pd\_frs\_type](#c.pd_frs_type) frs\_required
        :   Fast Role Swap required USB Type-C Current.

        uint32\_t dual\_role\_data
        :   Dual-Role Data.

        uint32\_t usb\_comms\_capable
        :   USB Communications Capable.

        uint32\_t unconstrained\_power
        :   Unconstrained Power.

        uint32\_t higher\_capability
        :   Higher Capability.

        uint32\_t dual\_role\_power
        :   Dual-Role Power.

        enum [pdo\_type](#c.pdo_type) type
        :   Fixed supply.

            SET TO PDO\_FIXED

        struct [pd\_fixed\_supply\_pdo\_sink](#c.pd_fixed_supply_pdo_sink).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_variable\_supply\_pdo\_source
    :   *#include <usbc\_pd.h>*

        Create a Variable Supply PDO Source value See Table 6-11 Variable Supply (non-Battery) PDO - Source.

        Public Members

        uint32\_t max\_current
        :   Maximum Current in 10mA units.

        uint32\_t min\_voltage
        :   Minimum Voltage in 50mV units.

        uint32\_t max\_voltage
        :   Maximum Voltage in 50mV units.

        enum [pdo\_type](#c.pdo_type) type
        :   Variable supply.

            SET TO PDO\_VARIABLE

        struct [pd\_variable\_supply\_pdo\_source](#c.pd_variable_supply_pdo_source).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_variable\_supply\_pdo\_sink
    :   *#include <usbc\_pd.h>*

        Create a Variable Supply PDO Sink value See Table 6-15 Variable Supply (non-Battery) PDO - Sink.

        Public Members

        uint32\_t operational\_current
        :   operational Current in 10mA units

        uint32\_t min\_voltage
        :   Minimum Voltage in 50mV units.

        uint32\_t max\_voltage
        :   Maximum Voltage in 50mV units.

        enum [pdo\_type](#c.pdo_type) type
        :   Variable supply.

            SET TO PDO\_VARIABLE

        struct [pd\_variable\_supply\_pdo\_sink](#c.pd_variable_supply_pdo_sink).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_battery\_supply\_pdo\_source
    :   *#include <usbc\_pd.h>*

        Create a Battery Supply PDO Source value See Table 6-12 Battery Supply PDO - Source.

        Public Members

        uint32\_t max\_power
        :   Maximum Allowable Power in 250mW units.

        uint32\_t min\_voltage
        :   Minimum Voltage in 50mV units.

        uint32\_t max\_voltage
        :   Maximum Voltage in 50mV units.

        enum [pdo\_type](#c.pdo_type) type
        :   Battery supply.

            SET TO PDO\_BATTERY

        struct [pd\_battery\_supply\_pdo\_source](#c.pd_battery_supply_pdo_source).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_battery\_supply\_pdo\_sink
    :   *#include <usbc\_pd.h>*

        Create a Battery Supply PDO Sink value See Table 6-16 Battery Supply PDO - Sink.

        Public Members

        uint32\_t operational\_power
        :   Operational Power in 250mW units.

        uint32\_t min\_voltage
        :   Minimum Voltage in 50mV units.

        uint32\_t max\_voltage
        :   Maximum Voltage in 50mV units.

        enum [pdo\_type](#c.pdo_type) type
        :   Battery supply.

            SET TO PDO\_BATTERY

        struct [pd\_battery\_supply\_pdo\_sink](#c.pd_battery_supply_pdo_sink).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_augmented\_supply\_pdo\_source
    :   *#include <usbc\_pd.h>*

        Create Augmented Supply PDO Source value See Table 6-13 Programmable Power Supply APDO - Source.

        Public Members

        uint32\_t max\_current
        :   Maximum Current in 50mA increments.

        uint32\_t reserved0
        :   Reserved – Shall be set to zero.

        uint32\_t min\_voltage
        :   Minimum Voltage in 100mV increments.

        uint32\_t reserved1
        :   Reserved – Shall be set to zero.

        uint32\_t max\_voltage
        :   Maximum Voltage in 100mV increments.

        uint32\_t reserved2
        :   Reserved – Shall be set to zero.

        uint32\_t pps\_power\_limited
        :   PPS Power Limited.

        uint32\_t reserved3
        :   00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set.

        enum [pdo\_type](#c.pdo_type) type
        :   Augmented Power Data Object (APDO).

            SET TO PDO\_AUGMENTED

        struct [pd\_augmented\_supply\_pdo\_source](#c.pd_augmented_supply_pdo_source).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_augmented\_supply\_pdo\_sink
    :   *#include <usbc\_pd.h>*

        Create Augmented Supply PDO Sink value See Table 6-17 Programmable Power Supply APDO - Sink.

        Public Members

        uint32\_t max\_current
        :   Maximum Current in 50mA increments.

        uint32\_t reserved0
        :   Reserved – Shall be set to zero.

        uint32\_t min\_voltage
        :   Minimum Voltage in 100mV increments.

        uint32\_t reserved1
        :   Reserved – Shall be set to zero.

        uint32\_t max\_voltage
        :   Maximum Voltage in 100mV increments.

        uint32\_t reserved2
        :   Reserved – Shall be set to zero.

        uint32\_t reserved3
        :   00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set.

        enum [pdo\_type](#c.pdo_type) type
        :   Augmented Power Data Object (APDO).

            SET TO PDO\_AUGMENTED

        struct [pd\_augmented\_supply\_pdo\_sink](#c.pd_augmented_supply_pdo_sink).[anonymous] [anonymous]

        uint32\_t raw\_value
        :   Raw PDO value.

    union pd\_rdo
    :   *#include <usbc\_pd.h>*

        The Request Data Object (RDO) Shall be returned by the Sink making a request for power.

        See Section 6.4.2 Request Message

        Public Members

        uint32\_t min\_or\_max\_operating\_current
        :   Operating Current 10mA units NOTE: If Give Back Flag is zero, this field is the Maximum Operating Current.

            If Give Back Flag is one, this field is the Minimum Operating Current.

        uint32\_t operating\_current
        :   Operating current in 10mA units.

            Operating Current 50mA units.

        uint32\_t reserved0
        :   Reserved - Shall be set to zero.

        uint32\_t unchunked\_ext\_msg\_supported
        :   Unchunked Extended Messages Supported.

        uint32\_t no\_usb\_suspend
        :   No USB Suspend.

        uint32\_t usb\_comm\_capable
        :   USB Communications Capable.

        uint32\_t cap\_mismatch
        :   Capability Mismatch.

        uint32\_t giveback
        :   Give Back Flag.

        uint32\_t object\_pos
        :   Object Position (000b is Reserved and Shall Not be used).

        uint32\_t reserved1
        :   Reserved - Shall be set to zero.

        struct [pd\_rdo](#c.pd_rdo).[anonymous] fixed
        :   Create a Fixed RDO value See Table 6-19 Fixed and Variable Request Data Object.

        struct [pd\_rdo](#c.pd_rdo).[anonymous] variable
        :   Create a Variable RDO value See Table 6-19 Fixed and Variable Request Data Object.

        uint32\_t min\_operating\_power
        :   Minimum Operating Power in 250mW units.

        uint32\_t operating\_power
        :   Operating power in 250mW units.

        struct [pd\_rdo](#c.pd_rdo).[anonymous] battery
        :   Create a Battery RDO value See Table 6-20 Battery Request Data Object.

        uint32\_t output\_voltage
        :   Output Voltage in 20mV units.

        uint32\_t reserved2
        :   Reserved - Shall be set to zero.

        uint32\_t reserved3
        :   Reserved - Shall be set to zero.

        struct [pd\_rdo](#c.pd_rdo).[anonymous] augmented
        :   Create an Augmented RDO value See Table 6-22 Programmable Request Data Object.

        uint32\_t raw\_value
        :   Raw RDO value.

    struct pd\_msg
    :   *#include <usbc\_pd.h>*

        Power Delivery message.

        Public Members

        enum [pd\_packet\_type](#c.pd_packet_type) type
        :   Type of this packet.

        union [pd\_header](#c.pd_header) header
        :   Header of this message.

        uint32\_t len
        :   Length of bytes in data.

        uint8\_t data[260]
        :   Message data.
