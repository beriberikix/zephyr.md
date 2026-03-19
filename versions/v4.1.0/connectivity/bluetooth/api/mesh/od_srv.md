---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/od_srv.html
original_path: connectivity/bluetooth/api/mesh/od_srv.html
---

# On-Demand Private Proxy Server

The On-Demand Private Proxy Server model is a foundation model defined by the Bluetooth Mesh
specification. It is enabled with the [`CONFIG_BT_MESH_OD_PRIV_PROXY_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_SRV "CONFIG_BT_MESH_OD_PRIV_PROXY_SRV") option.

The On-Demand Private Proxy Server model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and supports the configuration of advertising with Private Network Identity type of a
node that is a recipient of Solicitation PDUs by managing its On-Demand Private GATT Proxy state.

When enabled, the [Solicitation PDU RPL Configuration Server](srpl_srv.md#bluetooth-mesh-srpl-srv) is also enabled. The On-Demand Private Proxy Server
is dependent on the [Private Beacon Server](priv_beacon_srv.md#bluetooth-mesh-models-priv-beacon-srv) to be present on the node.

The On-Demand Private Proxy Server does not have an API of its own, and relies on a
[On-Demand Private Proxy Client](od_cli.md#bluetooth-mesh-od-cli) to control it. The On-Demand Private Proxy Server model only accepts
messages encrypted with the node’s device key.

If present, the On-Demand Private Proxy Server model must only be instantiated on the primary
element.

## API reference

[Bluetooth Mesh On-Demand Private GATT Proxy Server](../../../../doxygen/html/group__bt__mesh__od__priv__proxy__srv.md)
