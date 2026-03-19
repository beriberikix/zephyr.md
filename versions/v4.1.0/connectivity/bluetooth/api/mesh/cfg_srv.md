---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/cfg_srv.html
original_path: connectivity/bluetooth/api/mesh/cfg_srv.html
---

# Configuration Server

The Configuration Server model is a foundation model defined by the Bluetooth Mesh
specification. The Configuration Server model controls most parameters of the
mesh node. It does not have an API of its own, but relies on a
[Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli) to control it.

The Configuration Server model is mandatory on all Bluetooth Mesh nodes, and
must only be instantiated on the primary element.

## API reference

[Configuration Server Model](../../../../doxygen/html/group__bt__mesh__cfg__srv.md)
