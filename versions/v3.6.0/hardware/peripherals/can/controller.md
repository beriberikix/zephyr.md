---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/can/controller.html
original_path: hardware/peripherals/can/controller.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# CAN Controller

## [Overview](#id1)

Controller Area Network is a two-wire serial bus specified by the
Bosch CAN Specification, Bosch CAN with Flexible Data-Rate specification and the
ISO 11898-1:2003 standard.
CAN is mostly known for its application in the automotive domain. However, it
is also used in home and industrial automation and other products.

Warning

CAN controllers can only initialize when the bus is in the idle (recessive)
state for at least 11 recessive bits. Therefore you have to make sure that
CAN RX is high, at least for a short time. This is also necessary for
loopback mode.

The bit-timing as defined in ISO 11898-1:2003 looks as following:

[![CAN Timing](../../../_images/timing.svg)](../../../_images/timing.svg)

A single bit is split into four segments.

- Sync\_Seg: The nodes synchronize at the edge of the Sync\_Seg. It is always one time quantum in length.
- Prop\_Seg: The signal propagation delay of the bus and other delays of the transceiver and node.
- Phase\_Seg1 and Phase\_Seg2 :Define the sampling point. The bit is sampled at the end of Phase\_Seg1.

The bit-rate is calculated from the time of a time quantum and the values
defined above.
A bit has the length of Sync\_Seg plus Prop\_Seg plus Phase\_Seg1 plus Phase\_Seg2
multiplied by the time of single time quantum.
The bit-rate is the inverse of the length of a single bit.

A bit is sampled at the sampling point.
The sample point is between Phase\_Seg1 and PhaseSeg2 and therefore is a
parameter that the user needs to choose.
The CiA recommends setting the sample point to 87.5% of the bit.

The resynchronization jump width (SJW) defines the amount of time quantum the
sample point can be moved.
The sample point is moved when resynchronization is needed.

The timing parameters (SJW, bitrate and sampling point, or bitrate, Prop\_Seg,
Phase\_Seg1and Phase\_Seg2) are initially set from the device-tree and can be
changed at run-time from the timing-API.

CAN uses so-called identifiers to identify the frame instead of addresses to
identify a node.
This identifier can either have 11-bit width (Standard or Basic Frame) or
29-bit in case of an Extended Frame. The Zephyr CAN API supports both Standard
and Extended identifiers concurrently. A CAN frame starts with a dominant
Start Of Frame bit. After that, the identifiers follow. This phase is called the
arbitration phase. During the arbitration phase, write collisions are allowed.
They resolve by the fact that dominant bits override recessive bits.
Nodes monitor the bus and notice when their transmission is being overridden and
in case, abort their transmission.
This effectively gives lower number identifiers priority over higher number
identifiers.

Filters are used to whitelist identifiers that are of interest for the specific
node. An identifier that doesn’t match any filter is ignored.
Filters can either match exactly or a specified part of the identifier.
This method is called masking.
As an example, a mask with 11 bits set for standard or 29 bits set for extended
identifiers must match perfectly.
Bits that are set to zero in the mask are ignored when matching an identifier.
Most CAN controllers implement a limited number of filters in hardware.
The number of filters is also limited in Kconfig to save memory.

Errors may occur during transmission. In case a node detects an erroneous frame,
it partially overrides the current frame with an error-frame.
Error-frames can either be error passive or error active, depending on the state
of the controller.
In case the controller is in error active state, it sends six consecutive
dominant bits, which is a violation of the stuffing rule that all nodes can
detect. The sender may resend the frame right after.

An initialized node can be in one of the following states:

- Error-active
- Error-passive
- Bus-off

After initialization, the node is in the error-active state. In this state, the
node is allowed to send active error frames, ACK, and overload frames.
Every node has a receive- and transmit-error counter.
If either the receive- or the transmit-error counter exceeds 127,
the node changes to error-passive state.
In this state, the node is not allowed to send error-active frames anymore.
If the transmit-error counter increases further to 255, the node changes to the
bus-off state. In this state, the node is not allowed to send any dominant bits
to the bus. Nodes in the bus-off state may recover after receiving 128
occurrences of 11 concurrent recessive bits.

You can read more about CAN bus in this
[CAN Wikipedia article](https://en.wikipedia.org/wiki/CAN_bus).

Zephyr supports following CAN features:

- Standard and Extended Identifiers
- Filters with Masking
- Loopback and Silent mode
- Remote Request

## [Sending](#id2)

The following code snippets show how to send data.

This basic sample sends a CAN frame with standard identifier 0x123 and eight
bytes of data. When passing NULL as the callback, as shown in this example,
the send function blocks until the frame is sent and acknowledged by at least
one other node or an error occurred. The timeout only takes effect on acquiring
a mailbox. When a transmitting mailbox is assigned, sending cannot be canceled.

```c
struct can_frame frame = {
        .flags = 0,
        .id = 0x123,
        .dlc = 8,
        .data = {1,2,3,4,5,6,7,8}
};
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));
int ret;

ret = can_send(can_dev, &frame, K_MSEC(100), NULL, NULL);
if (ret != 0) {
        LOG_ERR("Sending failed [%d]", ret);
}
```

This example shows how to send a frame with extended identifier 0x1234567 and
two bytes of data. The provided callback is called when the message is sent, or
an error occurred. Passing [`K_FOREVER`](../../../kernel/services/timing/clocks.md#c.K_FOREVER "K_FOREVER") to the timeout causes the
function to block until a transfer mailbox is assigned to the frame or an error
occurred. It does not block until the message is sent like the example above.

```c
void tx_callback(const struct device *dev, int error, void *user_data)
{
        char *sender = (char *)user_data;

        if (error != 0) {
                LOG_ERR("Sending failed [%d]\nSender: %s\n", error, sender);
        }
}

int send_function(const struct device *can_dev)
{
        struct can_frame frame = {
                .flags = CAN_FRAME_IDE,
                .id = 0x1234567,
                .dlc = 2
        };

        frame.data[0] = 1;
        frame.data[1] = 2;

        return can_send(can_dev, &frame, K_FOREVER, tx_callback, "Sender 1");
}
```

## [Receiving](#id3)

Frames are only received when they match a filter.
The following code snippets show how to receive frames by adding filters.

Here we have an example for a receiving callback as used for
[`can_add_rx_filter()`](#c.can_add_rx_filter). The user data argument is passed when the filter is
added.

```c
void rx_callback_function(const struct device *dev, struct can_frame *frame, void *user_data)
{
        ... do something with the frame ...
}
```

The following snippet shows how to add a filter with a callback function.
It is the most efficient but also the most critical way to receive messages.
The callback function is called from an interrupt context, which means that the
callback function should be as short as possible and must not block.
Adding callback functions is not allowed from userspace context.

The filter for this example is configured to match the identifier 0x123 exactly.

```c
const struct can_filter my_filter = {
        .flags = 0U,
        .id = 0x123,
        .mask = CAN_STD_ID_MASK
};
int filter_id;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));

filter_id = can_add_rx_filter(can_dev, rx_callback_function, callback_arg, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to add rx filter [%d]", filter_id);
}
```

Here an example for [`can_add_rx_filter_msgq()`](#c.can_add_rx_filter_msgq) is shown. With this
function, it is possible to receive frames synchronously. This function can be
called from userspace context. The size of the message queue should be as big
as the expected backlog.

The filter for this example is configured to match the extended identifier
0x1234567 exactly.

```c
const struct can_filter my_filter = {
        .flags = CAN_FILTER_IDE,
        .id = 0x1234567,
        .mask = CAN_EXT_ID_MASK
};
CAN_MSGQ_DEFINE(my_can_msgq, 2);
struct can_frame rx_frame;
int filter_id;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));

filter_id = can_add_rx_filter_msgq(can_dev, &my_can_msgq, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to add rx msgq [%d]", filter_id);
  return;
}

while (true) {
  k_msgq_get(&my_can_msgq, &rx_frame, K_FOREVER);
  ... do something with the frame ...
}
```

[`can_remove_rx_filter()`](#c.can_remove_rx_filter) removes the given filter.

```c
can_remove_rx_filter(can_dev, filter_id);
```

## [Setting the bitrate](#id4)

The bitrate and sampling point is initially set at runtime. To change it from
the application, one can use the [`can_set_timing()`](#c.can_set_timing) API. The [`can_calc_timing()`](#c.can_calc_timing)
function can calculate timing from a bitrate and sampling point in permille.
The following example sets the bitrate to 250k baud with the sampling point at
87.5%.

```c
struct can_timing timing;
const struct device *const can_dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_canbus));
int ret;

ret = can_calc_timing(can_dev, &timing, 250000, 875);
if (ret > 0) {
  LOG_INF("Sample-Point error: %d", ret);
}

if (ret < 0) {
  LOG_ERR("Failed to calc a valid timing");
  return;
}

ret = can_stop(can_dev);
if (ret != 0) {
  LOG_ERR("Failed to stop CAN controller");
}

ret = can_set_timing(can_dev, &timing);
if (ret != 0) {
  LOG_ERR("Failed to set timing");
}

ret = can_start(can_dev);
if (ret != 0) {
  LOG_ERR("Failed to start CAN controller");
}
```

A similar API exists for calculating and setting the timing for the data phase for CAN FD capable
controllers. See [`can_set_timing_data()`](#c.can_set_timing_data) and [`can_calc_timing_data()`](#c.can_calc_timing_data).

## [SocketCAN](#id5)

Zephyr additionally supports SocketCAN, a BSD socket implementation of the
Zephyr CAN API.
SocketCAN brings the convenience of the well-known BSD Socket API to
Controller Area Networks. It is compatible with the Linux SocketCAN
implementation, where many other high-level CAN projects build on top.
Note that frames are routed to the network stack instead of passed directly,
which adds some computation and memory overhead.

## [Samples](#id6)

We have two ready-to-build samples demonstrating use of the Zephyr CAN API:
[Zephyr CAN counter sample](../../../samples/drivers/can/counter/README.md#can-counter "Send and receive CAN messages.") and
[SocketCAN sample](../../../samples/net/sockets/can/README.md#socket-can "Send and receive raw CAN frames using BSD sockets API.").

## [CAN Controller API Reference](#id7)

Related code samples

[Controller Area Network (CAN) babbling node](../../../samples/drivers/can/babbling/README.md#can-babbling "Simulate a babbling CAN node.")
:   Simulate a babbling CAN node.

[Controller Area Network (CAN) counter](../../../samples/drivers/can/counter/README.md#can-counter "Send and receive CAN messages.")
:   Send and receive CAN messages.

*group* can\_interface
:   CAN Interface.

    CAN controller configuration

    int can\_get\_core\_clock(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*rate)
    :   Get the CAN core clock rate.

        Returns the CAN core clock rate. One time quantum is 1/(core clock rate).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **rate** – **[out]** CAN core clock rate in Hz.

        Returns:
        :   0 on success, or a negative error code on error

    int can\_get\_max\_bitrate(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*max\_bitrate)
    :   Get maximum supported bitrate.

        Get the maximum supported bitrate for the CAN controller/transceiver combination.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **max\_bitrate** – **[out]** Maximum supported bitrate in bits/s

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input/output error.
            - **-ENOSYS** – If this function is not implemented by the driver.

    const struct [can\_timing](#c.can_timing) \*can\_get\_timing\_min(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the minimum supported timing parameter values.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Pointer to the minimum supported timing parameter values.

    const struct [can\_timing](#c.can_timing) \*can\_get\_timing\_max(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the maximum supported timing parameter values.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Pointer to the maximum supported timing parameter values.

    int can\_calc\_timing(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [can\_timing](#c.can_timing) \*res, uint32\_t bitrate, uint16\_t sample\_pnt)
    :   Calculate timing parameters from bitrate and sample point.

        Calculate the timing parameters from a given bitrate in bits/s and the sampling point in permill (1/1000) of the entire bit time. The bitrate must always match perfectly. If no result can be reached for the given parameters, -EINVAL is returned.

        Note

        The requested `sample_pnt` will not always be matched perfectly. The algorithm calculates the best possible match.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **res** – **[out]** Result is written into the *[can\_timing](#structcan__timing)* struct provided.
            - **bitrate** – Target bitrate in bits/s.
            - **sample\_pnt** – Sampling point in permill of the entire bit time.

        Return values:
        :   - **0** – or positive sample point error on success.
            - **-EINVAL** – if the requested bitrate or sample point is out of range.
            - **-ENOTSUP** – if the requested bitrate is not supported.
            - **-EIO** – if *[can\_get\_core\_clock()](#group__can__interface_1ga4af6d0d9ab72b195909f511ac65cb8fa)* is not available.

    const struct [can\_timing](#c.can_timing) \*can\_get\_timing\_data\_min(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the minimum supported timing parameter values for the data phase.

        Same as *[can\_get\_timing\_min()](#group__can__interface_1ga5a57627de4764f0bd3b4bafe07f56e6f)* but for the minimum values for the data phase.

        Note

        [`CONFIG_CAN_FD_MODE`](../../../kconfig.md#CONFIG_CAN_FD_MODE "CONFIG_CAN_FD_MODE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Pointer to the minimum supported timing parameter values, or NULL if CAN FD support is not implemented by the driver.

    const struct [can\_timing](#c.can_timing) \*can\_get\_timing\_data\_max(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the maximum supported timing parameter values for the data phase.

        Same as *[can\_get\_timing\_max()](#group__can__interface_1gabe385d0f003b1e990c78ef7a2a3f9616)* but for the maximum values for the data phase.

        Note

        [`CONFIG_CAN_FD_MODE`](../../../kconfig.md#CONFIG_CAN_FD_MODE "CONFIG_CAN_FD_MODE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Pointer to the maximum supported timing parameter values, or NULL if CAN FD support is not implemented by the driver.

    int can\_calc\_timing\_data(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [can\_timing](#c.can_timing) \*res, uint32\_t bitrate, uint16\_t sample\_pnt)
    :   Calculate timing parameters for the data phase.

        Same as *[can\_calc\_timing()](#group__can__interface_1gac27fe64142603f0d32d422594356b2d7)* but with the maximum and minimum values from the data phase.

        Note

        [`CONFIG_CAN_FD_MODE`](../../../kconfig.md#CONFIG_CAN_FD_MODE "CONFIG_CAN_FD_MODE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **res** – **[out]** Result is written into the *[can\_timing](#structcan__timing)* struct provided.
            - **bitrate** – Target bitrate for the data phase in bits/s
            - **sample\_pnt** – Sampling point for the data phase in permille of the entire bit time.

        Return values:
        :   - **0** – or positive sample point error on success.
            - **-EINVAL** – if the requested bitrate or sample point is out of range.
            - **-ENOTSUP** – if the requested bitrate is not supported.
            - **-EIO** – if *[can\_get\_core\_clock()](#group__can__interface_1ga4af6d0d9ab72b195909f511ac65cb8fa)* is not available.

    int can\_set\_timing\_data(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [can\_timing](#c.can_timing) \*timing\_data)
    :   Configure the bus timing for the data phase of a CAN FD controller.

        See also

        [can\_set\_timing()](#group__can__interface_1ga1b134af5d6286ea0fee130b6da5217da)

        Note

        [`CONFIG_CAN_FD_MODE`](../../../kconfig.md#CONFIG_CAN_FD_MODE "CONFIG_CAN_FD_MODE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **timing\_data** – Bus timings for data phase

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – if the CAN controller is not in stopped state.
            - **-EIO** – General input/output error, failed to configure device.
            - **-ENOTSUP** – if the timing parameters are not supported by the driver.
            - **-ENOSYS** – if CAN FD support is not implemented by the driver.

    int can\_set\_bitrate\_data(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t bitrate\_data)
    :   Set the bitrate for the data phase of the CAN FD controller.

        CAN in Automation (CiA) 301 v4.2.0 recommends a sample point location of 87.5% percent for all bitrates. However, some CAN controllers have difficulties meeting this for higher bitrates.

        This function defaults to using a sample point of 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. This is in line with the sample point locations used by the Linux kernel.

        See also

        [can\_set\_bitrate()](#group__can__interface_1ga0685ebfacfb79d33131167ac3aaa6f9b)

        Note

        [`CONFIG_CAN_FD_MODE`](../../../kconfig.md#CONFIG_CAN_FD_MODE "CONFIG_CAN_FD_MODE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **bitrate\_data** – Desired data phase bitrate.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – if the CAN controller is not in stopped state.
            - **-EINVAL** – if the requested bitrate is out of range.
            - **-ENOTSUP** – if the requested bitrate not supported by the CAN controller/transceiver combination.
            - **-ERANGE** – if the resulting sample point is off by more than +/- 5%.
            - **-EIO** – General input/output error, failed to set bitrate.

    int can\_calc\_prescaler(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [can\_timing](#c.can_timing) \*timing, uint32\_t bitrate)
    :   Fill in the prescaler value for a given bitrate and timing.

        Fill the prescaler value in the timing struct. The sjw, prop\_seg, phase\_seg1 and phase\_seg2 must be given.

        The returned bitrate error is remainder of the division of the clock rate by the bitrate times the timing segments.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **timing** – Result is written into the [can\_timing](#structcan__timing) struct provided.
            - **bitrate** – Target bitrate.

        Return values:
        :   - **0** – or positive bitrate error.
            - **Negative** – error code on error.

    int can\_set\_timing(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [can\_timing](#c.can_timing) \*timing)
    :   Configure the bus timing of a CAN controller.

        See also

        [can\_set\_timing\_data()](#group__can__interface_1ga606cf9fda4c66a0f4abf74e1d357eac2)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **timing** – Bus timings.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – if the CAN controller is not in stopped state.
            - **-ENOTSUP** – if the timing parameters are not supported by the driver.
            - **-EIO** – General input/output error, failed to configure device.

    int can\_get\_capabilities(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [can\_mode\_t](#c.can_mode_t) \*cap)
    :   Get the supported modes of the CAN controller.

        The returned capabilities may not necessarily be supported at the same time (e.g. some CAN controllers support both `[CAN_MODE_LOOPBACK](#group__can__interface_1ga891031afc77974a041accb3d0ceb21bb)` and `[CAN_MODE_LISTENONLY](#group__can__interface_1ga117d04b9118a1b3f839c557ef6b596cb)`, but not at the same time).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cap** – **[out]** Supported capabilities.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input/output error, failed to get capabilities.

    const struct [device](../../../kernel/drivers/index.md#c.device "device") \*can\_get\_transceiver(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the CAN transceiver associated with the CAN controller.

        Get a pointer to the device structure for the CAN transceiver associated with the CAN controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Pointer to the device structure for the associated CAN transceiver driver instance, or NULL if no transceiver is associated.

    int can\_start(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start the CAN controller.

        Bring the CAN controller out of `[CAN_STATE_STOPPED](#group__can__interface_1ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)`. This will reset the RX/TX error counters, enable the CAN controller to participate in CAN communication, and enable the CAN tranceiver, if supported.

        Starting the CAN controller resets all the CAN controller statistics.

        See also

        [can\_stop()](#group__can__interface_1ga1b0ac9185341cb0bde85ec64e4c490a5)

        See also

        [can\_transceiver\_enable()](transceiver.md#group__can__transceiver_1ga0d0e87150b49198c41e2782a17cfd694)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – if successful.
            - **-EALREADY** – if the device is already started.
            - **-EIO** – General input/output error, failed to start device.

    int can\_stop(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Stop the CAN controller.

        Bring the CAN controller into `[CAN_STATE_STOPPED](#group__can__interface_1ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)`. This will disallow the CAN controller from participating in CAN communication, abort any pending CAN frame transmissions, and disable the CAN transceiver, if supported.

        See also

        [can\_start()](#group__can__interface_1gae48dfa8bc5b52f233b9b1a08aac2675a)

        See also

        [can\_transceiver\_disable()](transceiver.md#group__can__transceiver_1ga7509ca0b6ece81b4038b7d128af961be)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – if successful.
            - **-EALREADY** – if the device is already stopped.
            - **-EIO** – General input/output error, failed to stop device.

    int can\_set\_mode(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [can\_mode\_t](#c.can_mode_t) mode)
    :   Set the CAN controller to the given operation mode.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **mode** – Operation mode.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – if the CAN controller is not in stopped state.
            - **-EIO** – General input/output error, failed to configure device.

    [can\_mode\_t](#c.can_mode_t) can\_get\_mode(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the operation mode of the CAN controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   Current operation mode.

    int can\_set\_bitrate(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t bitrate)
    :   Set the bitrate of the CAN controller.

        CAN in Automation (CiA) 301 v4.2.0 recommends a sample point location of 87.5% percent for all bitrates. However, some CAN controllers have difficulties meeting this for higher bitrates.

        This function defaults to using a sample point of 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. This is in line with the sample point locations used by the Linux kernel.

        See also

        [can\_set\_bitrate\_data()](#group__can__interface_1ga0afd2c446fc5e685370641a1678f87b7)

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **bitrate** – Desired arbitration phase bitrate.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – if the CAN controller is not in stopped state.
            - **-EINVAL** – if the requested bitrate is out of range.
            - **-ENOTSUP** – if the requested bitrate not supported by the CAN controller/transceiver combination.
            - **-ERANGE** – if the resulting sample point is off by more than +/- 5%.
            - **-EIO** – General input/output error, failed to set bitrate.

    Transmitting CAN frames

    int can\_send(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [can\_frame](#c.can_frame) \*frame, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout, [can\_tx\_callback\_t](#c.can_tx_callback_t) callback, void \*user\_data)
    :   Queue a CAN frame for transmission on the CAN bus.

        Queue a CAN frame for transmission on the CAN bus with optional timeout and completion callback function.

        Queued CAN frames are transmitted in order according to the their priority:

        - The lower the CAN-ID, the higher the priority.
        - Data frames have higher priority than Remote Transmission Request (RTR) frames with identical CAN-IDs.
        - Frames with standard (11-bit) identifiers have higher priority than frames with extended (29-bit) identifiers with identical base IDs (the higher 11 bits of the extended identifier).
        - Transmission order for queued frames with the same priority is hardware dependent.

        By default, the CAN controller will automatically retry transmission in case of lost bus arbitration or missing acknowledge. Some CAN controllers support disabling automatic retransmissions via `[CAN_MODE_ONE_SHOT](#group__can__interface_1ga033d7ade1966299c7e6249b945f38202)`.

        Note

        If transmitting segmented messages spanning multiple CAN frames with identical CAN-IDs, the sender must ensure to only queue one frame at a time if FIFO order is required.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **frame** – CAN frame to transmit.
            - **timeout** – Timeout waiting for a empty TX mailbox or `[K_FOREVER](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga0bb4b83f0222193b21a8910311bab0ca)`.
            - **callback** – Optional callback for when the frame was sent or a transmission error occurred. If `NULL`, this function is blocking until frame is sent. The callback must be `NULL` if called from user mode.
            - **user\_data** – User data to pass to callback function.

        Return values:
        :   - **0** – if successful.
            - **-EINVAL** – if an invalid parameter was passed to the function.
            - **-ENOTSUP** – if an unsupported parameter was passed to the function.
            - **-ENETDOWN** – if the CAN controller is in stopped state.
            - **-ENETUNREACH** – if the CAN controller is in bus-off state.
            - **-EBUSY** – if CAN bus arbitration was lost (only applicable if automatic retransmissions are disabled).
            - **-EIO** – if a general transmit error occurred (e.g. missing ACK if automatic retransmissions are disabled).
            - **-EAGAIN** – on timeout.

    Receiving CAN frames

    static inline int can\_add\_rx\_filter(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [can\_rx\_callback\_t](#c.can_rx_callback_t) callback, void \*user\_data, const struct [can\_filter](#c.can_filter) \*filter)
    :   Add a callback function for a given CAN filter.

        Add a callback to CAN identifiers specified by a filter. When a received CAN frame matching the filter is received by the CAN controller, the callback function is called in interrupt context.

        If a received frame matches more than one filter (i.e., the filter IDs/masks or flags overlap), the priority of the match is hardware dependent.

        The same callback function can be used for multiple filters.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – This function is called by the CAN controller driver whenever a frame matching the filter is received.
            - **user\_data** – User data to pass to callback function.
            - **filter** – Pointer to a *[can\_filter](#structcan__filter)* structure defining the filter.

        Return values:
        :   - **filter\_id** – on success.
            - **-ENOSPC** – if there are no free filters.
            - **-EINVAL** – if the requested filter type is invalid.
            - **-ENOTSUP** – if the requested filter type is not supported.

    int can\_add\_rx\_filter\_msgq(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [k\_msgq](../../../kernel/services/data_passing/message_queues.md#c.k_msgq "k_msgq") \*msgq, const struct [can\_filter](#c.can_filter) \*filter)
    :   Simple wrapper function for adding a message queue for a given filter.

        Wrapper function for *[can\_add\_rx\_filter()](#group__can__interface_1ga0cf4baa2c4216d8515554d180ceb774a)* which puts received CAN frames matching the filter in a message queue instead of calling a callback.

        If a received frame matches more than one filter (i.e., the filter IDs/masks or flags overlap), the priority of the match is hardware dependent.

        The same message queue can be used for multiple filters.

        Note

        The message queue must be initialized before calling this function and the caller must have appropriate permissions on it.

        Warning

        Message queue overruns are silently ignored and overrun frames discarded. Custom error handling can be implemented by using *[can\_add\_rx\_filter()](#group__can__interface_1ga0cf4baa2c4216d8515554d180ceb774a)* and *[k\_msgq\_put()](../../../kernel/services/data_passing/message_queues.md#group__msgq__apis_1ga54e96aaaea5462a1f963b7fd5ca82bfe)* directly.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **msgq** – Pointer to the already initialized *[k\_msgq](../../../kernel/services/data_passing/message_queues.md#structk__msgq)* struct.
            - **filter** – Pointer to a *[can\_filter](#structcan__filter)* structure defining the filter.

        Return values:
        :   - **filter\_id** – on success.
            - **-ENOSPC** – if there are no free filters.
            - **-ENOTSUP** – if the requested filter type is not supported.

    void can\_remove\_rx\_filter(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, int filter\_id)
    :   Remove a CAN RX filter.

        This routine removes a CAN RX filter based on the filter ID returned by *[can\_add\_rx\_filter()](#group__can__interface_1ga0cf4baa2c4216d8515554d180ceb774a)* or *[can\_add\_rx\_filter\_msgq()](#group__can__interface_1gaaac20a068b7f32d2f38d1601d588b35c)*.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **filter\_id** – Filter ID

    int can\_get\_max\_filters(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, bool ide)
    :   Get maximum number of RX filters.

        Get the maximum number of concurrent RX filters for the CAN controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ide** – Get the maximum standard (11-bit) CAN ID filters if false, or extended (29-bit) CAN ID filters if true.

        Return values:
        :   - **Positive** – number of maximum concurrent filters.
            - **-EIO** – General input/output error.
            - **-ENOSYS** – If this function is not implemented by the driver.

    CAN\_MSGQ\_DEFINE(name, max\_frames)
    :   Statically define and initialize a CAN RX message queue.

        The message queue’s ring buffer contains space for *max\_frames* CAN frames.

        See also

        [can\_add\_rx\_filter\_msgq()](#group__can__interface_1gaaac20a068b7f32d2f38d1601d588b35c)

        Parameters:
        :   - **name** – Name of the message queue.
            - **max\_frames** – Maximum number of CAN frames that can be queued.

    CAN bus error reporting and handling

    int can\_get\_state(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [can\_state](#c.can_state) \*state, struct [can\_bus\_err\_cnt](#c.can_bus_err_cnt) \*err\_cnt)
    :   Get current CAN controller state.

        Returns the current state and optionally the error counter values of the CAN controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **state** – Pointer to the state destination enum or NULL.
            - **err\_cnt** – **[out]** Pointer to the err\_cnt destination structure or NULL.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input/output error, failed to get state.

    int can\_recover(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Recover from bus-off state.

        Recover the CAN controller from bus-off state to error-active state.

        Note

        [`CONFIG_CAN_AUTO_BUS_OFF_RECOVERY`](../../../kconfig.md#CONFIG_CAN_AUTO_BUS_OFF_RECOVERY "CONFIG_CAN_AUTO_BUS_OFF_RECOVERY") must be deselected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **timeout** – Timeout for waiting for the recovery or `[K_FOREVER](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga0bb4b83f0222193b21a8910311bab0ca)`.

        Return values:
        :   - **0** – on success.
            - **-ENETDOWN** – if the CAN controller is in stopped state.
            - **-EAGAIN** – on timeout.

    static inline void can\_set\_state\_change\_callback(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [can\_state\_change\_callback\_t](#c.can_state_change_callback_t) callback, void \*user\_data)
    :   Set a callback for CAN controller state change events.

        Set the callback for CAN controller state change events. The callback function will be called in interrupt context.

        Only one callback can be registered per controller. Calling this function again overrides any previously registered callback.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – Callback function.
            - **user\_data** – User data to pass to callback function.

    CAN statistics

    uint32\_t can\_stats\_get\_bit\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the bit error counter for a CAN device.

        The bit error counter is incremented when the CAN controller is unable to transmit either a dominant or a recessive bit.

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   bit error counter

    uint32\_t can\_stats\_get\_bit0\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the bit0 error counter for a CAN device.

        The bit0 error counter is incremented when the CAN controller is unable to transmit a dominant bit.

        See also

        [can\_stats\_get\_bit\_errors()](#group__can__interface_1ga27b277f3b5146590f159171f602904db)

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   bit0 error counter

    uint32\_t can\_stats\_get\_bit1\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the bit1 error counter for a CAN device.

        The bit1 error counter is incremented when the CAN controller is unable to transmit a recessive bit.

        See also

        [can\_stats\_get\_bit\_errors()](#group__can__interface_1ga27b277f3b5146590f159171f602904db)

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   bit1 error counter

    uint32\_t can\_stats\_get\_stuff\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the stuffing error counter for a CAN device.

        The stuffing error counter is incremented when the CAN controller detects a bit stuffing error.

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   stuffing error counter

    uint32\_t can\_stats\_get\_crc\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the CRC error counter for a CAN device.

        The CRC error counter is incremented when the CAN controller detects a frame with an invalid CRC.

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   CRC error counter

    uint32\_t can\_stats\_get\_form\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the form error counter for a CAN device.

        The form error counter is incremented when the CAN controller detects a fixed-form bit field containing illegal bits.

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   form error counter

    uint32\_t can\_stats\_get\_ack\_errors(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the acknowledge error counter for a CAN device.

        The acknowledge error counter is incremented when the CAN controller does not monitor a dominant bit in the ACK slot.

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   acknowledge error counter

    uint32\_t can\_stats\_get\_rx\_overruns(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the RX overrun counter for a CAN device.

        The RX overrun counter is incremented when the CAN controller receives a CAN frame matching an installed filter but lacks the capacity to store it (either due to an already full RX mailbox or a full RX FIFO).

        Note

        [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") must be selected for this function to be available.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Returns:
        :   RX overrun counter

    CAN utility functions

    static inline uint8\_t can\_dlc\_to\_bytes(uint8\_t dlc)
    :   Convert from Data Length Code (DLC) to the number of data bytes.

        Parameters:
        :   - **dlc** – Data Length Code (DLC).

        Return values:
        :   **Number** – of bytes.

    static inline uint8\_t can\_bytes\_to\_dlc(uint8\_t num\_bytes)
    :   Convert from number of bytes to Data Length Code (DLC).

        Parameters:
        :   - **num\_bytes** – Number of bytes.

        Return values:
        :   **Data** – Length Code (DLC).

    static inline bool can\_frame\_matches\_filter(const struct [can\_frame](#c.can_frame) \*frame, const struct [can\_filter](#c.can_filter) \*filter)
    :   Check if a CAN frame matches a CAN filter.

        Parameters:
        :   - **frame** – CAN frame.
            - **filter** – CAN filter.

        Returns:
        :   true if the CAN frame matches the CAN filter, false otherwise

    CAN frame definitions

    CAN\_STD\_ID\_MASK
    :   Bit mask for a standard (11-bit) CAN identifier.

    CAN\_MAX\_STD\_ID
    :   Maximum value for a standard (11-bit) CAN identifier.

    CAN\_EXT\_ID\_MASK
    :   Bit mask for an extended (29-bit) CAN identifier.

    CAN\_MAX\_EXT\_ID
    :   Maximum value for an extended (29-bit) CAN identifier.

    CAN\_MAX\_DLC
    :   Maximum data length code for CAN 2.0A/2.0B.

    CANFD\_MAX\_DLC
    :   Maximum data length code for CAN FD.

    CAN controller mode flags

    CAN\_MODE\_NORMAL
    :   Normal mode.

    CAN\_MODE\_LOOPBACK
    :   Controller is in loopback mode (receives own frames).

    CAN\_MODE\_LISTENONLY
    :   Controller is not allowed to send dominant bits.

    CAN\_MODE\_FD
    :   Controller allows transmitting/receiving CAN FD frames.

    CAN\_MODE\_ONE\_SHOT
    :   Controller does not retransmit in case of lost arbitration or missing ACK.

    CAN\_MODE\_3\_SAMPLES
    :   Controller uses triple sampling mode.

    CAN frame flags

    CAN\_FRAME\_IDE
    :   Frame uses extended (29-bit) CAN ID.

    CAN\_FRAME\_RTR
    :   Frame is a Remote Transmission Request (RTR).

    CAN\_FRAME\_FDF
    :   Frame uses CAN FD format (FDF).

    CAN\_FRAME\_BRS
    :   Frame uses CAN FD Baud Rate Switch (BRS).

        Only valid in combination with `[CAN_FRAME_FDF](#group__can__interface_1ga22f85e1d16b93e46200f9673abdbb589)`.

    CAN\_FRAME\_ESI
    :   CAN FD Error State Indicator (ESI).

        Indicates that the transmitting node is in error-passive state. Only valid in combination with `[CAN_FRAME_FDF](#group__can__interface_1ga22f85e1d16b93e46200f9673abdbb589)`.

    CAN filter flags

    CAN\_FILTER\_IDE
    :   Filter matches frames with extended (29-bit) CAN IDs.

    Defines

    CAN\_STATS\_BIT\_ERROR\_INC(dev\_)
    :   Increment the bit error counter for a CAN device.

        The bit error counter is incremented when the CAN controller is unable to transmit either a dominant or a recessive bit.

        See also

        [CAN\_STATS\_BIT0\_ERROR\_INC()](#group__can__interface_1ga120a37d5ae5064dcbf116e488f733764)

        See also

        [CAN\_STATS\_BIT1\_ERROR\_INC()](#group__can__interface_1ga678b74039632302efcb5ef80f0e3a90b)

        Note

        This error counter should only be incremented if the CAN controller is unable to distinquish between failure to transmit a dominant versus failure to transmit a recessive bit. If the CAN controller supports distinguishing between the two, the `bit0` or `bit1` error counter shall be incremented instead.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_BIT0\_ERROR\_INC(dev\_)
    :   Increment the bit0 error counter for a CAN device.

        The bit0 error counter is incremented when the CAN controller is unable to transmit a dominant bit.

        Incrementing this counter will automatically increment the bit error counter.

        See also

        [CAN\_STATS\_BIT\_ERROR\_INC()](#group__can__interface_1gaf6f7efa9d99f44af6f58352f558d7fec)

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_BIT1\_ERROR\_INC(dev\_)
    :   Increment the bit1 (recessive) error counter for a CAN device.

        The bit1 error counter is incremented when the CAN controller is unable to transmit a recessive bit.

        Incrementing this counter will automatically increment the bit error counter.

        See also

        [CAN\_STATS\_BIT\_ERROR\_INC()](#group__can__interface_1gaf6f7efa9d99f44af6f58352f558d7fec)

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_STUFF\_ERROR\_INC(dev\_)
    :   Increment the stuffing error counter for a CAN device.

        The stuffing error counter is incremented when the CAN controller detects a bit stuffing error.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_CRC\_ERROR\_INC(dev\_)
    :   Increment the CRC error counter for a CAN device.

        The CRC error counter is incremented when the CAN controller detects a frame with an invalid CRC.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_FORM\_ERROR\_INC(dev\_)
    :   Increment the form error counter for a CAN device.

        The form error counter is incremented when the CAN controller detects a fixed-form bit field containing illegal bits.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_ACK\_ERROR\_INC(dev\_)
    :   Increment the acknowledge error counter for a CAN device.

        The acknowledge error counter is incremented when the CAN controller does not monitor a dominant bit in the ACK slot.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_RX\_OVERRUN\_INC(dev\_)
    :   Increment the RX overrun counter for a CAN device.

        The RX overrun counter is incremented when the CAN controller receives a CAN frame matching an installed filter but lacks the capacity to store it (either due to an already full RX mailbox or a full RX FIFO).

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_STATS\_RESET(dev\_)
    :   Zero all statistics for a CAN device.

        The driver is reponsible for resetting the statistics before starting the CAN controller.

        Parameters:
        :   - **dev\_** – Pointer to the device structure for the driver instance.

    CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, ...)
    :   Like [DEVICE\_DT\_DEFINE()](../../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) with CAN device specifics.

        Defines a device which implements the CAN API. May generate a custom [device\_state](../../../kernel/drivers/index.md#structdevice__state) container struct and init\_fn wrapper when needed depending on  [`CONFIG_CAN_STATS`](../../../kconfig.md#CONFIG_CAN_STATS "CONFIG_CAN_STATS") .

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Name of the init function of the driver.
            - **pm** – PM device resources reference (NULL if device does not use PM).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **level** – The initialization level. See SYS\_INIT() for details.
            - **prio** – Priority within the selected initialization level. See SYS\_INIT() for details.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.

    CAN\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like [CAN\_DEVICE\_DT\_DEFINE()](#group__can__interface_1ga599d0695abe481411660d7af2893f4a5) for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – Instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to [CAN\_DEVICE\_DT\_DEFINE()](#group__can__interface_1ga599d0695abe481411660d7af2893f4a5).
            - **...** – Other parameters as expected by [CAN\_DEVICE\_DT\_DEFINE()](#group__can__interface_1ga599d0695abe481411660d7af2893f4a5).

    Typedefs

    typedef uint32\_t can\_mode\_t
    :   Provides a type to hold CAN controller configuration flags.

        The lower 24 bits are reserved for common CAN controller mode flags. The upper 8 bits are reserved for CAN controller/driver specific flags.

        See also

        [CAN\_MODE\_FLAGS](#group__can__interface_1CAN_MODE_FLAGS).

    typedef void (\*can\_tx\_callback\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, int error, void \*user\_data)
    :   Defines the application callback handler function signature.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param error:
        :   Status of the performed send operation. See the list of return values for *[can\_send()](#group__can__interface_1ga446ee31913699de3c80be05d837b5fd5)* for value descriptions.

        Param user\_data:
        :   User data provided when the frame was sent.

    typedef void (\*can\_rx\_callback\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [can\_frame](#c.can_frame) \*frame, void \*user\_data)
    :   Defines the application callback handler function signature for receiving.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param frame:
        :   Received frame.

        Param user\_data:
        :   User data provided when the filter was added.

    typedef void (\*can\_state\_change\_callback\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [can\_state](#c.can_state) state, struct [can\_bus\_err\_cnt](#c.can_bus_err_cnt) err\_cnt, void \*user\_data)
    :   Defines the state change callback handler function signature.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param state:
        :   State of the CAN controller.

        Param err\_cnt:
        :   CAN controller error counter values.

        Param user\_data:
        :   User data provided the callback was set.

    Enums

    enum can\_state
    :   Defines the state of the CAN controller.

        *Values:*

        enumerator CAN\_STATE\_ERROR\_ACTIVE
        :   Error-active state (RX/TX error count < 96).

        enumerator CAN\_STATE\_ERROR\_WARNING
        :   Error-warning state (RX/TX error count < 128).

        enumerator CAN\_STATE\_ERROR\_PASSIVE
        :   Error-passive state (RX/TX error count < 256).

        enumerator CAN\_STATE\_BUS\_OFF
        :   Bus-off state (RX/TX error count >= 256).

        enumerator CAN\_STATE\_STOPPED
        :   CAN controller is stopped and does not participate in CAN communication.

    struct can\_frame
    :   *#include <can.h>*

        CAN frame structure.

        Public Members

        uint32\_t id
        :   Standard (11-bit) or extended (29-bit) CAN identifier.

        uint8\_t dlc
        :   Data Length Code (DLC) indicating data length in bytes.

        uint8\_t flags
        :   Flags.

            See also

            [CAN\_FRAME\_FLAGS](#group__can__interface_1CAN_FRAME_FLAGS).

        uint16\_t timestamp
        :   Captured value of the free-running timer in the CAN controller when this frame was received.

            The timer is incremented every bit time and captured at the start of frame bit (SOF).

            Note

            [`CONFIG_CAN_RX_TIMESTAMP`](../../../kconfig.md#CONFIG_CAN_RX_TIMESTAMP "CONFIG_CAN_RX_TIMESTAMP") must be selected for this field to be available.

        uint8\_t data[CAN\_MAX\_DLEN]
        :   Payload data accessed as unsigned 8 bit values.

        uint32\_t data\_32[[DIV\_ROUND\_UP](../../../kernel/util/index.md#c.DIV_ROUND_UP "DIV_ROUND_UP")(CAN\_MAX\_DLEN, sizeof(uint32\_t))]
        :   Payload data accessed as unsigned 32 bit values.

        union [can\_frame](#c.can_frame).[anonymous] [anonymous]
        :   The frame payload data.

    struct can\_filter
    :   *#include <can.h>*

        CAN filter structure.

        Public Members

        uint32\_t id
        :   CAN identifier to match.

        uint32\_t mask
        :   CAN identifier matching mask.

            If a bit in this mask is 0, the value of the corresponding bit in the `[id](#structcan__filter_1adf2b18eab11d360780707478a1f624b9)` field is ignored by the filter.

        uint8\_t flags
        :   Flags.

            See also

            [CAN\_FILTER\_FLAGS](#group__can__interface_1CAN_FILTER_FLAGS).

    struct can\_bus\_err\_cnt
    :   *#include <can.h>*

        CAN controller error counters.

        Public Members

        uint8\_t tx\_err\_cnt
        :   Value of the CAN controller transmit error counter.

        uint8\_t rx\_err\_cnt
        :   Value of the CAN controller receive error counter.

    struct can\_timing
    :   *#include <can.h>*

        CAN bus timing structure.

        This struct is used to pass bus timing values to the configuration and bitrate calculation functions.

        The propagation segment represents the time of the signal propagation. Phase segment 1 and phase segment 2 define the sampling point. The `[prop_seg](#structcan__timing_1ac009d40fee9788b663963978498b2ee9)` and `[phase_seg1](#structcan__timing_1a9941688e79fa4ce01c4b498433319089)` values affect the sampling point in the same way and some controllers only have a register for the sum of those two. The sync segment always has a length of 1 time quantum (see below).

        ```text
        +---------+----------+------------+------------+
        |sync_seg | prop_seg | phase_seg1 | phase_seg2 |
        +---------+----------+------------+------------+
                                          ^
                                    Sampling-Point
        ```

        1 time quantum (tq) has the length of 1/(core\_clock / prescaler). The bitrate is defined by the core clock divided by the prescaler and the sum of the segments:

        br = (core\_clock / prescaler) / (1 + prop\_seg + phase\_seg1 + phase\_seg2)

        The Synchronization Jump Width (SJW) defines the amount of time quanta the sample point can be moved. The sample point is moved when resynchronization is needed.

        Public Members

        uint16\_t sjw
        :   Synchronisation jump width.

        uint16\_t prop\_seg
        :   Propagation segment.

        uint16\_t phase\_seg1
        :   Phase segment 1.

        uint16\_t phase\_seg2
        :   Phase segment 2.

        uint16\_t prescaler
        :   Prescaler value.

    struct can\_device\_state
    :   *#include <can.h>*

        CAN specific device state which allows for CAN device class specific additions.

        Public Members

        struct [device\_state](../../../kernel/drivers/index.md#c.device_state "device_state") devstate
        :   Common device state.

        struct stats\_can stats
        :   CAN device statistics.
