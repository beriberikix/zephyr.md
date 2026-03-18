---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/srpl_cli.html
original_path: connectivity/bluetooth/api/mesh/srpl_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Solicitation PDU RPL Configuration Client

The Solicitation PDU RPL Configuration Client model is a foundation model defined by the Bluetooth
mesh specification. The model is optional, and is enabled through the
[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI "CONFIG_BT_MESH_SOL_PDU_RPL_CLI") option.

The Solicitation PDU RPL Configuration Client model was introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and supports the functionality of removing addresses from the
solicitation replay protection list (SRPL) of a node that supports the
[Solicitation PDU RPL Configuration Server](srpl_srv.md#bluetooth-mesh-srpl-srv) model.

The Solicitation PDU RPL Configuration Client model communicates with a Solicitation PDU RPL
Configuration Server model using the application keys configured by the Configuration Client.

If present, the Solicitation PDU RPL Configuration Client model must only be instantiated on the
primary element.

## Configurations

The Solicitation PDU RPL Configuration Client model behavior can be configured with the transmission
timeout option [`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT "CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT"). The
[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT "CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT") controls how long the Solicitation PDU RPL
Configuration Client waits for a response message to arrive in milliseconds. This value can be
changed at runtime using [`bt_mesh_sol_pdu_rpl_cli_timeout_set()`](#c.bt_mesh_sol_pdu_rpl_cli_timeout_set).

## API reference

*group* Bluetooth Mesh Solicitation PDU RPL Client
:   Defines

    BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI(cli\_data)
    :   Solicitation PDU RPL Client model composition data entry.

    Functions

    int bt\_mesh\_sol\_pdu\_rpl\_clear(struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t range\_start, uint8\_t range\_len, uint16\_t \*start\_rsp, uint8\_t \*len\_rsp)
    :   Remove entries from Solicitation PDU RPL of addresses in given range.

        This method can be used asynchronously by setting `start_rsp` or `len_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `srpl_status` callback in `[bt_mesh_sol_pdu_rpl_cli](#structbt__mesh__sol__pdu__rpl__cli)` struct.

        Parameters:
        :   - **ctx** – Message context for the message.
            - **range\_start** – Start of Unicast address range.
            - **range\_len** – Length of Unicast address range. Valid values are 0x00 and 0x02 to 0xff.
            - **start\_rsp** – Range start response buffer.
            - **len\_rsp** – Range length response buffer.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_sol\_pdu\_rpl\_clear\_unack(struct [bt\_mesh\_msg\_ctx](msg.md#c.bt_mesh_msg_ctx "bt_mesh_msg_ctx") \*ctx, uint16\_t range\_start, uint8\_t range\_len)
    :   Remove entries from Solicitation PDU RPL of addresses in given range (unacked).

        Parameters:
        :   - **ctx** – Message context for the message.
            - **range\_start** – Start of Unicast address range.
            - **range\_len** – Length of Unicast address range. Valid values are 0x00 and 0x02 to 0xff.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    void bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout in milliseconds.

    struct bt\_mesh\_sol\_pdu\_rpl\_cli
    :   *#include <sol\_pdu\_rpl\_cli.h>*

        Solicitation PDU RPL Client Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Solicitation PDU RPL model entry pointer.

        void (\*srpl\_status)(struct [bt\_mesh\_sol\_pdu\_rpl\_cli](#c.bt_mesh_sol_pdu_rpl_cli) \*cli, uint16\_t addr, uint16\_t range\_start, uint8\_t range\_length)
        :   Optional callback for Solicitation PDU RPL Status messages.

            Handles received Solicitation PDU RPL Status messages from a Solicitation PDU RPL server.The `start` param represents the start of range that server has cleared. The `length` param represents length of range cleared by server.

            Param cli:
            :   Solicitation PDU RPL client that received the status message.

            Param addr:
            :   Address of the sender.

            Param range\_start:
            :   Range start value.

            Param range\_length:
            :   Range length value.
