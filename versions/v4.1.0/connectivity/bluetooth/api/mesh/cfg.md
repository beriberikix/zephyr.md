---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/cfg.html
original_path: connectivity/bluetooth/api/mesh/cfg.html
---

# Runtime Configuration

The runtime configuration API allows applications to change their runtime
configuration directly, without going through the Configuration models.

Bluetooth Mesh nodes should generally be configured by a central network
configurator device with a [Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli) model. Each
mesh node instantiates a [Configuration Server](cfg_srv.md#bluetooth-mesh-models-cfg-srv) model that the
Configuration Client can communicate with to change the node configuration. In some
cases, the mesh node can’t rely on the Configuration Client to detect or determine
local constraints, such as low battery power or changes in topology. For these
scenarios, this API can be used to change the configuration locally.

Note

Runtime configuration changes before the node is provisioned will not be stored
in the [persistent storage](core.md#bluetooth-mesh-persistent-storage).

## API reference

[Runtime Configuration](../../../../doxygen/html/group__bt__mesh__cfg.md)
