---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/hci_raw.html
original_path: connectivity/bluetooth/api/hci_raw.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# HCI RAW channel

## Overview

HCI RAW channel API is intended to expose HCI interface to the remote entity.
The local Bluetooth controller gets owned by the remote entity and host
Bluetooth stack is not used. RAW API provides direct access to packets which
are sent and received by the Bluetooth HCI driver.

## API Reference

*group* hci\_raw
:   HCI RAW channel.

    Defines

    BT\_HCI\_ERR\_EXT\_HANDLED

    BT\_HCI\_RAW\_CMD\_EXT(\_op, \_min\_len, \_func)
    :   Helper macro to define a command extension.

        Parameters:
        :   - **\_op** – Opcode of the command.
            - **\_min\_len** – Minimal length of the command.
            - **\_func** – Handler function to be called.

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator BT\_HCI\_RAW\_MODE\_PASSTHROUGH = 0x00
        :   Passthrough mode.

            While in this mode the buffers are passed as is between the stack and the driver.

        enumerator BT\_HCI\_RAW\_MODE\_H4 = 0x01
        :   H:4 mode.

            While in this mode H:4 headers will added into the buffers according to the buffer type when coming from the stack and will be removed and used to set the buffer type.

    Functions

    int bt\_send(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Send packet to the Bluetooth controller.

        Send packet to the Bluetooth controller. Caller needs to implement netbuf pool.

        Parameters:
        :   - **buf** – netbuf packet to be send

        Returns:
        :   Zero on success or (negative) error code otherwise.

    int bt\_hci\_raw\_set\_mode(uint8\_t mode)
    :   Set Bluetooth RAW channel mode.

        Set access mode of Bluetooth RAW channel.

        Parameters:
        :   - **mode** – Access mode.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    uint8\_t bt\_hci\_raw\_get\_mode(void)
    :   Get Bluetooth RAW channel mode.

        Get access mode of Bluetooth RAW channel.

        Returns:
        :   Access mode.

    void bt\_hci\_raw\_cmd\_ext\_register(struct [bt\_hci\_raw\_cmd\_ext](#c.bt_hci_raw_cmd_ext) \*cmds, size\_t size)
    :   Register Bluetooth RAW command extension table.

        Register Bluetooth RAW channel command extension table, opcodes in this table are intercepted to sent to the handler function.

        Parameters:
        :   - **cmds** – Pointer to the command extension table.
            - **size** – Size of the command extension table.

    int bt\_enable\_raw(struct k\_fifo \*rx\_queue)
    :   Enable Bluetooth RAW channel:

        Enable Bluetooth RAW HCI channel.

        Parameters:
        :   - **rx\_queue** – netbuf queue where HCI packets received from the Bluetooth controller are to be queued. The queue is defined in the caller while the available buffers pools are handled in the stack.

        Returns:
        :   Zero on success or (negative) error code otherwise.

    struct bt\_hci\_raw\_cmd\_ext
    :   *#include <hci\_raw.h>*

        Public Members

        uint16\_t op
        :   Opcode of the command.

        size\_t min\_len
        :   Minimal length of the command.

        uint8\_t (\*func)(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
        :   Handler function.

            Handler function to be called when a command is intercepted.

            Param buf:
            :   Buffer containing the command.

            Return:
            :   HCI Status code or BT\_HCI\_ERR\_EXT\_HANDLED if command has been handled already and a response has been sent as oppose to BT\_HCI\_ERR\_SUCCESS which just indicates that the command can be sent to the controller to be processed.
