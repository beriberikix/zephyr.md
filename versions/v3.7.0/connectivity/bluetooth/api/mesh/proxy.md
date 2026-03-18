---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/proxy.html
original_path: connectivity/bluetooth/api/mesh/proxy.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Proxy

The Proxy feature allows legacy devices like phones to access the Bluetooth Mesh network through
GATT. The Proxy feature is only compiled in if the [`CONFIG_BT_MESH_GATT_PROXY`](../../../../kconfig.md#CONFIG_BT_MESH_GATT_PROXY "CONFIG_BT_MESH_GATT_PROXY")
option is set. The Proxy feature state is controlled by the [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv),
and the initial value can be set with `bt_mesh_cfg_srv.gatt_proxy`.

Nodes with the Proxy feature enabled can advertise with Network Identity and Node Identity,
which is controlled by the [Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli).

The GATT Proxy state indicates if the Proxy feature is supported.

## Private Proxy

A node supporting the Proxy feature and the [Private Beacon Server](priv_beacon_srv.md#bluetooth-mesh-models-priv-beacon-srv) model can
advertise with Private Network Identity and Private Node Identity types, which is controlled by the
[Private Beacon Client](priv_beacon_cli.md#bluetooth-mesh-models-priv-beacon-cli). By advertising with this set of identification types,
the node allows the legacy device to connect to the network over GATT while maintaining the
privacy of the network.

The Private GATT Proxy state indicates whether the Private Proxy functionality is supported.

## Proxy Solicitation

In the case where both GATT Proxy and Private GATT Proxy states are disabled on a node, a legacy
device cannot connect to it. A node supporting the [On-Demand Private Proxy Server](od_srv.md#bluetooth-mesh-od-srv) may however be
solicited to advertise connectable advertising events without enabling the Private GATT Proxy state.
To solicit the node, the legacy device can send a Solicitation PDU by calling the
`bt_mesh_proxy_solicit()` function. To enable this feature, the device must to be compiled with
the [`CONFIG_BT_MESH_PROXY_SOLICITATION`](../../../../kconfig.md#CONFIG_BT_MESH_PROXY_SOLICITATION "CONFIG_BT_MESH_PROXY_SOLICITATION") option set.

Solicitation PDUs are non-mesh, non-connectable, undirected advertising messages containing Proxy
Solicitation UUID, encrypted with the network key of the subnet that the legacy device wants to
connect to. The PDU contains the source address of the legacy device and a sequence number. The
sequence number is maintained by the legacy device and is incremented for every new Solicitation PDU
sent.

Each node supporting the Solicitation PDU reception holds its own Solicitation Replay Protection
List (SRPL). The SRPL protects the solicitation mechanism from replay attacks by storing
solicitation sequence number (SSEQ) and solicitation source (SSRC) pairs of valid Solicitation PDUs
processed by the node. The delay between updating the SRPL and storing the change to the persistent
storage is defined by [`CONFIG_BT_MESH_RPL_STORE_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_RPL_STORE_TIMEOUT "CONFIG_BT_MESH_RPL_STORE_TIMEOUT").

The Solicitation PDU RPL Configuration models, [Solicitation PDU RPL Configuration Client](srpl_cli.md#bluetooth-mesh-srpl-cli) and
[Solicitation PDU RPL Configuration Server](srpl_srv.md#bluetooth-mesh-srpl-srv), provide the functionality of saving and clearing SRPL entries. A
node that supports the Solicitation PDU RPL Configuration Client model can clear a section of the
SRPL on the target by calling the `bt_mesh_sol_pdu_rpl_clear()` function. Communication between
the Solicitation PDU RPL Configuration Client and Server is encrypted using the application key,
therefore, the Solicitation PDU RPL Configuration Client can be instantiated on any device in the
network.

When the node receives the Solicitation PDU and successfully authenticates it, it will start
advertising connectable advertisements with the Private Network Identity type. The duration of the
advertisement can be configured by the On-Demand Private Proxy Client model.

## API reference

*group* Proxy
:   Proxy.

    Defines

    BT\_MESH\_PROXY\_CB\_DEFINE(\_name)
    :   Register a callback structure for Proxy events.

        Registers a structure with callback functions that gets called on various Proxy events.

        Parameters:
        :   - **\_name** – Name of callback structure.

    Functions

    int bt\_mesh\_proxy\_identity\_enable(void)
    :   Enable advertising with Node Identity.

        This API requires that GATT Proxy support has been enabled. Once called each subnet will start advertising using Node Identity for the next 60 seconds.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_proxy\_private\_identity\_enable(void)
    :   Enable advertising with Private Node Identity.

        This API requires that GATT Proxy support has been enabled. Once called each subnet will start advertising using Private Node Identity for the next 60 seconds.

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_proxy\_connect(uint16\_t net\_idx)
    :   Allow Proxy Client to auto connect to a network.

        This API allows a proxy client to auto-connect a given network.

        Parameters:
        :   - **net\_idx** – Network Key Index

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_proxy\_disconnect(uint16\_t net\_idx)
    :   Disallow Proxy Client to auto connect to a network.

        This API disallows a proxy client to connect a given network.

        Parameters:
        :   - **net\_idx** – Network Key Index

        Returns:
        :   0 on success, or (negative) error code on failure.

    int bt\_mesh\_proxy\_solicit(uint16\_t net\_idx)
    :   Schedule advertising of Solicitation PDUs.

        Once called, the device will schedule advertising Solicitation PDUs for the amount of time defined by `adv_int` \* (`CONFIG_BT_MESH_SOL_ADV_XMIT` + 1), where `adv_int` is 20ms for Bluetooth v5.0 or higher, or 100ms otherwise.

        If the number of advertised Solicitation PDUs reached 0xFFFFFF, the advertisements will no longer be started until the node is reprovisioned.

        Parameters:
        :   - **net\_idx** – Network Key Index

        Returns:
        :   0 on success, or (negative) error code on failure.

    struct bt\_mesh\_proxy\_cb
    :   *#include <proxy.h>*

        Callbacks for the Proxy feature.

        Should be instantiated with [BT\_MESH\_PROXY\_CB\_DEFINE](#group__bt__mesh__proxy_1ga325b71c3d7ed69952bf760c0288b28ef).

        Public Members

        void (\*identity\_enabled)(uint16\_t net\_idx)
        :   Started sending Node Identity beacons on the given subnet.

            Param net\_idx:
            :   Network index the Node Identity beacons are running on.

        void (\*identity\_disabled)(uint16\_t net\_idx)
        :   Stopped sending Node Identity beacons on the given subnet.

            Param net\_idx:
            :   Network index the Node Identity beacons were running on.
