---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/brg_cfg_srv.html
original_path: connectivity/bluetooth/api/mesh/brg_cfg_srv.html
---

# Bridge Configuration Server

The Bridge Configuration Server model is a foundation model defined by the Bluetooth Mesh
specification. It is an optional model, enabled with the
[`CONFIG_BT_MESH_BRG_CFG_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_BRG_CFG_SRV "CONFIG_BT_MESH_BRG_CFG_SRV") configuration option. This model extends
the [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model.

The Bridge Configuration Server model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and is used for supporting and configuring the Subnet Bridge feature.

The Bridge Configuration Server model relies on a [Bridge Configuration Client](brg_cfg_cli.md#bluetooth-mesh-models-brg-cfg-cli) to
configure it. The Bridge Configuration Server model only accepts messages encrypted with the node’s
device key.

If present, the Bridge Configuration Server model must be instantiated on the primary element.

The Bridge Configuration Server model provides access to the following three states:

- Subnet Bridge
- Bridging Table
- Bridging Table Size

For more information about the states, see [Subnet Bridge states](brg_cfg.md#bluetooth-mesh-brg-cfg-states).

## API reference

[Bridge Configuration Server Model](../../../../doxygen/html/group__bt__mesh__brg__cfg__srv.md)
