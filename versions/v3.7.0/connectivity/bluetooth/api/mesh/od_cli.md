---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/od_cli.html
original_path: connectivity/bluetooth/api/mesh/od_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# On-Demand Private Proxy Client

The On-Demand Private Proxy Client model is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled with the
[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI") option.

The On-Demand Private Proxy Client model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and is used to set and retrieve the On-Demand Private GATT Proxy state. The state
defines how long a node will advertise Mesh Proxy Service with Private Network Identity type after
it receives a Solicitation PDU.

The On-Demand Private Proxy Client model communicates with an On-Demand Private Proxy Server model
using the device key of the node containing the target On-Demand Private Proxy Server model
instance.

If present, the On-Demand Private Proxy Client model must only be instantiated on the primary
element.

## Configurations

The On-Demand Private Proxy Client model behavior can be configured with the transmission timeout
option [`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT"). The
[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT") controls how long the Client waits for a
state response message to arrive in milliseconds. This value can be changed at runtime using
[`bt_mesh_od_priv_proxy_cli_timeout_set()`](#c.bt_mesh_od_priv_proxy_cli_timeout_set).

## API reference

*group* Bluetooth Mesh On-Demand Private GATT Proxy Client
:   Defines

    BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI(cli\_data)
    :   On-Demand Private Proxy Client model composition data entry.

    Functions

    int bt\_mesh\_od\_priv\_proxy\_cli\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*val\_rsp)
    :   Get the target’s On-Demand Private GATT Proxy state.

        This method can be used asynchronously by setting `val_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `od_status` callback in `[bt_mesh_od_priv_proxy_cli](#structbt__mesh__od__priv__proxy__cli)` struct.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val\_rsp** – Response buffer for On-Demand Private GATT Proxy value.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_od\_priv\_proxy\_cli\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*val\_rsp)
    :   Set the target’s On-Demand Private GATT Proxy state.

        This method can be used asynchronously by setting `val_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        To process the response arguments of an async method, register the `od_status` callback in `[bt_mesh_od_priv_proxy_cli](#structbt__mesh__od__priv__proxy__cli)` struct.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – On-Demand Private GATT Proxy state to be set
            - **val\_rsp** – Response buffer for On-Demand Private GATT Proxy value.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    void bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout in milliseconds.

    struct bt\_mesh\_od\_priv\_proxy\_cli
    :   *#include <od\_priv\_proxy\_cli.h>*

        On-Demand Private Proxy Client Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Solicitation PDU RPL model entry pointer.

        void (\*od\_status)(struct [bt\_mesh\_od\_priv\_proxy\_cli](#c.bt_mesh_od_priv_proxy_cli) \*cli, uint16\_t addr, uint8\_t state)
        :   Optional callback for On-Demand Private Proxy Status messages.

            Handles received On-Demand Private Proxy Status messages from a On-Demand Private Proxy server.The `state` param represents state of On-Demand Private Proxy server.

            Param cli:
            :   On-Demand Private Proxy client that received the status message.

            Param addr:
            :   Address of the sender.

            Param state:
            :   State value.
