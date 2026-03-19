---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/sar_cfg_cli.html
original_path: connectivity/bluetooth/api/mesh/sar_cfg_cli.html
---

# SAR Configuration Client

The SAR Configuration Client model is a foundation model defined by the Bluetooth Mesh
specification. It is an optional model, enabled with the
[`CONFIG_BT_MESH_SAR_CFG_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_SAR_CFG_CLI "CONFIG_BT_MESH_SAR_CFG_CLI") configuration option.

The SAR Configuration Client model is introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and it supports the configuration of the lower transport layer behavior of a node that
supports the [SAR Configuration Server](sar_cfg_srv.md#bluetooth-mesh-sar-cfg-srv) model.

The model can send messages to query or change the states supported by the SAR Configuration Server
(SAR Transmitter and SAR Receiver) using SAR Configuration messages.

The SAR Transmitter procedure is used to determine and configure the SAR Transmitter state of a SAR
Configuration Server. Function calls [`bt_mesh_sar_cfg_cli_transmitter_get()`](../../../../doxygen/html/group__bt__mesh__sar__cfg__cli.md#ga893ef5861708bec12f87b9f9cc64b9fc) and
[`bt_mesh_sar_cfg_cli_transmitter_set()`](../../../../doxygen/html/group__bt__mesh__sar__cfg__cli.md#ga32e2a580b24a41761911e88413e9664e) are used to get and set the SAR Transmitter state
of the Target node respectively.

The SAR Receiver procedure is used to determine and configure the SAR Receiver state of a SAR
Configuration Server. Function calls [`bt_mesh_sar_cfg_cli_receiver_get()`](../../../../doxygen/html/group__bt__mesh__sar__cfg__cli.md#ga444c99254ef2ccdd10dac08a94219d79) and
[`bt_mesh_sar_cfg_cli_receiver_set()`](../../../../doxygen/html/group__bt__mesh__sar__cfg__cli.md#ga884025b2baf8559950ba6dc83e9ef486) are used to get and set the SAR Receiver state of the
Target node respectively.

For more information about the two states, see [SAR states](sar_cfg.md#bt-mesh-sar-cfg-states).

An element can send any SAR Configuration Client message at any time to query or change the states
supported by the SAR Configuration Server model of a peer node. The SAR Configuration Client model
only accepts messages encrypted with the device key of the node supporting the SAR Configuration
Server model.

If present, the SAR Configuration Client model must only be instantiated on the primary element.

## API reference

[Bluetooth Mesh SAR Configuration Client Model](../../../../doxygen/html/group__bt__mesh__sar__cfg__cli.md)
