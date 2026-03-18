---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/can/transceiver.html
original_path: hardware/peripherals/can/transceiver.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# CAN Transceiver

## [Overview](#id1)

A CAN transceiver is an external device that converts the logic level signals
from the CAN controller to the bus-levels. The bus lines are called
CAN High (CAN H) and CAN Low (CAN L).
The transmit wire from the controller to the transceiver is called CAN TX,
and the receive wire is called CAN RX.
These wires use the logic levels whereas the bus-level is interpreted
differentially between CAN H and CAN L.
The bus can be either in the recessive (logical one) or dominant (logical zero)
state. The recessive state is when both lines, CAN H and CAN L, are roughly at
the same voltage level. This state is also the idle state.
To write a dominant bit to the bus, open-drain transistors tie CAN H to Vdd
and CAN L to ground.
The first and last node use a 120-ohm resistor between CAN H and CAN L to
terminate the bus. The dominant state always overrides the recessive state.
This structure is called a wired-AND.

[![CAN Transceiver](../../../_images/transceiver.svg)](../../../_images/transceiver.svg)

## [CAN Transceiver API Reference](#id2)

*group* can\_transceiver
:   CAN Transceiver Driver APIs.

    Functions

    static inline int can\_transceiver\_enable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [can\_mode\_t](controller.md#c.can_mode_t "can_mode_t") mode)
    :   Enable CAN transceiver.

        Enable the CAN transceiver.

        See also

        [can\_start()](controller.md#group__can__interface_1gae48dfa8bc5b52f233b9b1a08aac2675a)

        Note

        The CAN transceiver is controlled by the CAN controller driver and should not normally be controlled by the application.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **mode** – Operation mode.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input/output error, failed to enable device.

    static inline int can\_transceiver\_disable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable CAN transceiver.

        Disable the CAN transceiver.

        See also

        [can\_stop()](controller.md#group__can__interface_1ga1b0ac9185341cb0bde85ec64e4c490a5)

        Note

        The CAN transceiver is controlled by the CAN controller driver and should not normally be controlled by the application.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input/output error, failed to disable device.
