---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/brg_cfg_cli.html
original_path: connectivity/bluetooth/api/mesh/brg_cfg_cli.html
---

# Bridge Configuration Client

The Bridge Configuration Client is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled through
the [`CONFIG_BT_MESH_BRG_CFG_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_BRG_CFG_CLI "CONFIG_BT_MESH_BRG_CFG_CLI") option.

The Bridge Configuration Client model provides functionality for configuring the
subnet bridge functionality of another Mesh node containing the
[Bridge Configuration Server](brg_cfg_srv.md#bluetooth-mesh-models-brg-cfg-srv). The device key of the node containing
the target Bridge Configuration Server is used for access layer security.

If present, the Bridge Configuration Client model must only be instantiated on the primary
element.

## API reference

[Bridge Configuration Client Model](../../../../doxygen/html/group__bt__mesh__brg__cfg__cli.md)
