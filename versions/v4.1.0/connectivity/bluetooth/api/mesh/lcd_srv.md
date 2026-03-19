---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/lcd_srv.html
original_path: connectivity/bluetooth/api/mesh/lcd_srv.html
---

# Large Composition Data Server

The Large Composition Data Server model is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled through the
[`CONFIG_BT_MESH_LARGE_COMP_DATA_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV "CONFIG_BT_MESH_LARGE_COMP_DATA_SRV") option.

The Large Composition Data Server model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and is used to support the functionality of exposing pages of Composition Data that do
not fit in a Config Composition Data Status message and to expose metadata of the model instances.

The Large Composition Data Server does not have an API of its own and relies on a
[Large Composition Data Client](lcd_cli.md#bluetooth-mesh-lcd-cli) to control it. The model only accepts messages encrypted with the
node’s device key.

If present, the Large Composition Data Server model must only be instantiated on the primary
element.

## Models metadata

The Large Composition Data Server model allows each model to have a list of model’s specific
metadata that can be read by the Large Composition Data Client model. The metadata list can be
associated with the [`bt_mesh_model`](../../../../doxygen/html/structbt__mesh__model.md) through the [`bt_mesh_model.metadata`](../../../../doxygen/html/structbt__mesh__model.md#af5b948709773e5388c30d457ec2a9559) field.
The metadata list consists of one or more entries defined by the
[`bt_mesh_models_metadata_entry`](../../../../doxygen/html/structbt__mesh__models__metadata__entry.md) structure. Each entry contains the length and ID of the
metadata, and a pointer to the raw data. Entries can be created using the
[`BT_MESH_MODELS_METADATA_ENTRY`](../../../../doxygen/html/group__bt__mesh__access.md#gaa2587adac719c50c311ae41c548b853c) macro. The [`BT_MESH_MODELS_METADATA_END`](../../../../doxygen/html/group__bt__mesh__access.md#gaab5fe51071f6e54debd9136ac6a70a49) macro
marks the end of the metadata list and must always be present. If the model has no metadata, the
helper macro [`BT_MESH_MODELS_METADATA_NONE`](../../../../doxygen/html/group__bt__mesh__access.md#ga56b518123ab47cb3ae4a249f471ae556) can be used instead.

### API reference

[Large Composition Data Server model](../../../../doxygen/html/group__bt__mesh__large__comp__data__srv.md)
