---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/sar_cfg_cli.html
original_path: connectivity/bluetooth/api/mesh/sar_cfg_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SAR Configuration Client

The SAR Configuration Client model is a foundation model defined by the Bluetooth Mesh
specification. It is an optional model, enabled with the
[`CONFIG_BT_MESH_SAR_CFG_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_CFG_CLI "CONFIG_BT_MESH_SAR_CFG_CLI") configuration option.

The SAR Configuration Client model is introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and it supports the configuration of the lower transport layer behavior of a node that
supports the [SAR Configuration Server](sar_cfg_srv.md#bluetooth-mesh-sar-cfg-srv) model.

The model can send messages to query or change the states supported by the SAR Configuration Server
(SAR Transmitter and SAR Receiver) using SAR Configuration messages.

The SAR Transmitter procedure is used to determine and configure the SAR Transmitter state of a SAR
Configuration Server. Function calls [`bt_mesh_sar_cfg_cli_transmitter_get()`](#c.bt_mesh_sar_cfg_cli_transmitter_get) and
[`bt_mesh_sar_cfg_cli_transmitter_set()`](#c.bt_mesh_sar_cfg_cli_transmitter_set) are used to get and set the SAR Transmitter state
of the Target node respectively.

The SAR Receiver procedure is used to determine and configure the SAR Receiver state of a SAR
Configuration Server. Function calls [`bt_mesh_sar_cfg_cli_receiver_get()`](#c.bt_mesh_sar_cfg_cli_receiver_get) and
[`bt_mesh_sar_cfg_cli_receiver_set()`](#c.bt_mesh_sar_cfg_cli_receiver_set) are used to get and set the SAR Receiver state of the
Target node respectively.

For more information about the two states, see [SAR states](sar_cfg.md#bt-mesh-sar-cfg-states).

An element can send any SAR Configuration Client message at any time to query or change the states
supported by the SAR Configuration Server model of a peer node. The SAR Configuration Client model
only accepts messages encrypted with the device key of the node supporting the SAR Configuration
Server model.

If present, the SAR Configuration Client model must only be instantiated on the primary element.

## API reference

*group* Bluetooth Mesh SAR Configuration Client Model
:   Bluetooth Mesh.

    Defines

    BT\_MESH\_MODEL\_SAR\_CFG\_CLI(\_cli)
    :   SAR Configuration Client model composition data entry.

        Parameters:
        :   - **\_cli** – **[in]** Pointer to a [Bluetooth Mesh SAR Configuration Client Model](#group__bt__mesh__sar__cfg__cli) instance.

    Functions

    int bt\_mesh\_sar\_cfg\_cli\_transmitter\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_sar\_tx \*rsp)
    :   Get the SAR Transmitter state of the target node.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **rsp** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_sar\_cfg\_cli\_transmitter\_set(uint16\_t net\_idx, uint16\_t addr, const struct bt\_mesh\_sar\_tx \*set, struct bt\_mesh\_sar\_tx \*rsp)
    :   Set the SAR Transmitter state of the target node.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **set** – New SAR Transmitter state to set on the target node.
            - **rsp** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_sar\_cfg\_cli\_receiver\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_sar\_rx \*rsp)
    :   Get the SAR Receiver state of the target node.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **rsp** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_sar\_cfg\_cli\_receiver\_set(uint16\_t net\_idx, uint16\_t addr, const struct bt\_mesh\_sar\_rx \*set, struct bt\_mesh\_sar\_rx \*rsp)
    :   Set the SAR Receiver state of the target node.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **set** – New SAR Receiver state to set on the target node.
            - **rsp** – Status response parameter.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int32\_t bt\_mesh\_sar\_cfg\_cli\_timeout\_get(void)
    :   Get the current transmission timeout value.

        Returns:
        :   The configured transmission timeout in milliseconds.

    void bt\_mesh\_sar\_cfg\_cli\_timeout\_set(int32\_t timeout)
    :   Set the transmission timeout value.

        Parameters:
        :   - **timeout** – The new transmission timeout.

    struct bt\_mesh\_sar\_cfg\_cli
    :   *#include <sar\_cfg\_cli.h>*

        Mesh SAR Configuration Client Model Context.

        Public Members

        const struct [bt\_mesh\_model](access.md#c.bt_mesh_model "bt_mesh_model") \*model
        :   Access model pointer.
