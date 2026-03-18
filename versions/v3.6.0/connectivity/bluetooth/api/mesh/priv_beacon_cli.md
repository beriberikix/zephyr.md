---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/priv_beacon_cli.html
original_path: connectivity/bluetooth/api/mesh/priv_beacon_cli.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Private Beacon Client

The Private Beacon Client model is a foundation model defined by the Bluetooth
mesh specification. It is enabled with the
[`CONFIG_BT_MESH_PRIV_BEACON_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_PRIV_BEACON_CLI "CONFIG_BT_MESH_PRIV_BEACON_CLI") option.

The Private Beacon Client model is introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and provides functionality for configuring the
[Private Beacon Server](priv_beacon_srv.md#bluetooth-mesh-models-priv-beacon-srv) models.

The Private Beacons feature adds privacy to the different Bluetooth Mesh
beacons by periodically randomizing the beacon input data. This protects the
mesh node from being tracked by devices outside the mesh network, and hides the
network’s IV index, IV update and the Key Refresh state.

The Private Beacon Client model communicates with a
[Private Beacon Server](priv_beacon_srv.md#bluetooth-mesh-models-priv-beacon-srv) model using the device key of the
target node. The Private Beacon Client model may communicate with servers on
other nodes or self-configure through the local Private Beacon Server model.

All configuration functions in the Private Beacon Client API have `net_idx`
and `addr` as their first parameters. These should be set to the network
index and the primary unicast address the target node was provisioned with.

If present, the Private Beacon Client model must only be instantiated on the primary element.

## API reference

*group* bt\_mesh\_priv\_beacon\_cli
:   Defines

    BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI(cli\_data)
    :   Private Beacon Client model composition data entry.

        Parameters:
        :   - **cli\_data** – Pointer to a [Bluetooth Mesh Private Beacon Client](#group__bt__mesh__priv__beacon__cli) instance.

    Functions

    int bt\_mesh\_priv\_beacon\_cli\_set(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_priv\_beacon](#c.bt_mesh_priv_beacon) \*val, struct [bt\_mesh\_priv\_beacon](#c.bt_mesh_priv_beacon) \*rsp)
    :   Set the target’s Private Beacon state.

        This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Private Beacon value.
            - **rsp** – If set, returns response status on success.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_priv\_beacon\_cli\_get(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_priv\_beacon](#c.bt_mesh_priv_beacon) \*val)
    :   Get the target’s Private Beacon state.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – Response buffer for Private Beacon value.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*rsp)
    :   Set the target’s Private GATT Proxy state.

        This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Private GATT Proxy value.
            - **rsp** – If set, returns response status on success.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*val)
    :   Get the target’s Private GATT Proxy state.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – Response buffer for Private GATT Proxy value.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_priv\_beacon\_cli\_node\_id\_set(uint16\_t net\_idx, uint16\_t addr, struct [bt\_mesh\_priv\_node\_id](#c.bt_mesh_priv_node_id) \*val, struct [bt\_mesh\_priv\_node\_id](#c.bt_mesh_priv_node_id) \*rsp)
    :   Set the target’s Private Node Identity state.

        This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **val** – New Private Node Identity value.
            - **rsp** – If set, returns response status on success.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    int bt\_mesh\_priv\_beacon\_cli\_node\_id\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, struct [bt\_mesh\_priv\_node\_id](#c.bt_mesh_priv_node_id) \*val)
    :   Get the target’s Private Node Identity state.

        Parameters:
        :   - **net\_idx** – Network index to encrypt with.
            - **addr** – Target node address.
            - **key\_net\_idx** – Network index to get the Private Node Identity state of.
            - **val** – Response buffer for Private Node Identity value.

        Returns:
        :   0 on success, or (negative) error code otherwise.

    struct bt\_mesh\_priv\_beacon
    :   *#include <priv\_beacon\_cli.h>*

        Private Beacon.

        Public Members

        uint8\_t enabled
        :   Private beacon is enabled.

        uint8\_t rand\_interval
        :   Random refresh interval (in 10 second steps), or 0 to keep current value.

    struct bt\_mesh\_priv\_node\_id
    :   *#include <priv\_beacon\_cli.h>*

        Private Node Identity.

        Public Members

        uint16\_t net\_idx
        :   Index of the NetKey.

        uint8\_t state
        :   Private Node Identity state.

        uint8\_t status
        :   Response status code.

    struct bt\_mesh\_priv\_beacon\_cli\_cb
    :   *#include <priv\_beacon\_cli.h>*

        Private Beacon Client Status messages callbacks.

        Public Members

        void (\*priv\_beacon\_status)(struct [bt\_mesh\_priv\_beacon\_cli](#c.bt_mesh_priv_beacon_cli) \*cli, uint16\_t addr, struct [bt\_mesh\_priv\_beacon](#c.bt_mesh_priv_beacon) \*priv\_beacon)
        :   Optional callback for Private Beacon Status message.

            Handles received Private Beacon Status messages from a Private Beacon server.

            Param cli:
            :   Private Beacon client context.

            Param addr:
            :   Address of the sender.

            Param priv\_beacon:
            :   Mesh Private Beacon state received from the server.

        void (\*priv\_gatt\_proxy\_status)(struct [bt\_mesh\_priv\_beacon\_cli](#c.bt_mesh_priv_beacon_cli) \*cli, uint16\_t addr, uint8\_t gatt\_proxy)
        :   Optional callback for Private GATT Proxy Status message.

            Handles received Private GATT Proxy Status messages from a Private Beacon server.

            Param cli:
            :   Private Beacon client context.

            Param addr:
            :   Address of the sender.

            Param gatt\_proxy:
            :   Private GATT Proxy state received from the server.

        void (\*priv\_node\_id\_status)(struct [bt\_mesh\_priv\_beacon\_cli](#c.bt_mesh_priv_beacon_cli) \*cli, uint16\_t addr, struct [bt\_mesh\_priv\_node\_id](#c.bt_mesh_priv_node_id) \*priv\_node\_id)
        :   Optional callback for Private Node Identity Status message.

            Handles received Private Node Identity Status messages from a Private Beacon server.

            Param cli:
            :   Private Beacon client context.

            Param addr:
            :   Address of the sender.

            Param priv\_node\_id:
            :   Private Node Identity state received from the server.

    struct bt\_mesh\_priv\_beacon\_cli
    :   *#include <priv\_beacon\_cli.h>*

        Mesh Private Beacon Client model.

        Public Members

        const struct [bt\_mesh\_priv\_beacon\_cli\_cb](#c.bt_mesh_priv_beacon_cli_cb) \*cb
        :   Optional callback for Private Beacon Client Status messages.
