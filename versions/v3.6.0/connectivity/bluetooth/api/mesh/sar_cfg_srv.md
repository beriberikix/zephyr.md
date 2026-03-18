---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/sar_cfg_srv.html
original_path: connectivity/bluetooth/api/mesh/sar_cfg_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SAR Configuration Server

The SAR Configuration Server model is a foundation model defined by the Bluetooth Mesh
specification. It is an optional model, enabled with the
[`CONFIG_BT_MESH_SAR_CFG_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_CFG_SRV "CONFIG_BT_MESH_SAR_CFG_SRV") configuration option.

The SAR Configuration Server model is introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and it supports the configuration of the
[segmentation and reassembly (SAR)](sar_cfg.md#bluetooth-mesh-sar-cfg) behavior of a Bluetooth Mesh node.
The model defines a set of states and messages for the SAR configuration.

The SAR Configuration Server model defines two states, SAR Transmitter state and SAR Receiver state.
For more information about the two states, see [SAR states](sar_cfg.md#bt-mesh-sar-cfg-states).

The model also supports the SAR Transmitter and SAR Receiver get and set messages.

The SAR Configuration Server model does not have an API of its own, but relies on a
[SAR Configuration Client](sar_cfg_cli.md#bluetooth-mesh-sar-cfg-cli) to control it. The SAR Configuration Server model only accepts
messages encrypted with the node’s device key.

If present, the SAR Configuration Server model must only be instantiated on the primary element.

## API reference

*group* bt\_mesh\_sar\_cfg\_srv
:   Bluetooth Mesh.

    Defines

    BT\_MESH\_MODEL\_SAR\_CFG\_SRV
    :   Transport SAR Configuration Server model composition data entry.
