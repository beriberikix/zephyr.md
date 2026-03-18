---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/cfg_srv.html
original_path: connectivity/bluetooth/api/mesh/cfg_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Configuration Server

The Configuration Server model is a foundation model defined by the Bluetooth Mesh
specification. The Configuration Server model controls most parameters of the
mesh node. It does not have an API of its own, but relies on a
[Configuration Client](cfg_cli.md#bluetooth-mesh-models-cfg-cli) to control it.

The Configuration Server model is mandatory on all Bluetooth Mesh nodes, and
must only be instantiated on the primary element.

## API reference

*group* Configuration Server Model
:   Configuration Server Model.

    Defines

    BT\_MESH\_MODEL\_CFG\_SRV
    :   Generic Configuration Server model composition data entry.
