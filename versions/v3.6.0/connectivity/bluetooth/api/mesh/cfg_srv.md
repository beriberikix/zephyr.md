---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/cfg_srv.html
original_path: connectivity/bluetooth/api/mesh/cfg_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Configuration Server

The Configuration Server model is a foundation model defined by the Bluetooth Mesh
specification. The Configuration Server model controls most parameters of the
mesh node. It does not have an API of its own, but relies on a
[Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli) to control it.

Note

The `bt_mesh_cfg_srv` structure has been deprecated. The initial
values of the Relay, Beacon, Friend, Network transmit and Relay retransmit
should be set through Kconfig, and the Heartbeat feature should be
controlled through the [Heartbeat](heartbeat.md#bluetooth-mesh-heartbeat) API.

The Configuration Server model is mandatory on all Bluetooth Mesh nodes, and
must only be instantiated on the primary element.

## API reference

*group* bt\_mesh\_cfg\_srv
:   Configuration Server Model.

    Defines

    BT\_MESH\_MODEL\_CFG\_SRV
    :   Generic Configuration Server model composition data entry.
