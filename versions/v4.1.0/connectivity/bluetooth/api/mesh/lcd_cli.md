---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/lcd_cli.html
original_path: connectivity/bluetooth/api/mesh/lcd_cli.html
---

# Large Composition Data Client

The Large Composition Data Client model is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled through the
[`CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_LARGE_COMP_DATA_CLI "CONFIG_BT_MESH_LARGE_COMP_DATA_CLI") option.

The Large Composition Data Client model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and supports the functionality of reading pages of Composition Data that do not fit in
a Config Composition Data Status message and reading the metadata of the model instances on a node
that supports the [Large Composition Data Server](lcd_srv.md#bluetooth-mesh-lcd-srv) model.

The Large Composition Data Client model communicates with a Large Composition Data Server model
using the device key of the node containing the target Large Composition Data Server model instance.

If present, the Large Composition Data Client model must only be instantiated on the primary
element.

## API reference

[Large Composition Data Client model](../../../../doxygen/html/group__bt__mesh__large__comp__data__cli.md)
