---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/srpl_cli.html
original_path: connectivity/bluetooth/api/mesh/srpl_cli.html
---

# Solicitation PDU RPL Configuration Client

The Solicitation PDU RPL Configuration Client model is a foundation model defined by the Bluetooth
mesh specification. The model is optional, and is enabled through the
[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI "CONFIG_BT_MESH_SOL_PDU_RPL_CLI") option.

The Solicitation PDU RPL Configuration Client model was introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and supports the functionality of removing addresses from the
solicitation replay protection list (SRPL) of a node that supports the
[Solicitation PDU RPL Configuration Server](srpl_srv.md#bluetooth-mesh-srpl-srv) model.

The Solicitation PDU RPL Configuration Client model communicates with a Solicitation PDU RPL
Configuration Server model using the application keys configured by the Configuration Client.

If present, the Solicitation PDU RPL Configuration Client model must only be instantiated on the
primary element.

## Configurations

The Solicitation PDU RPL Configuration Client model behavior can be configured with the transmission
timeout option [`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT "CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT"). The
[`CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT "CONFIG_BT_MESH_SOL_PDU_RPL_CLI_TIMEOUT") controls how long the Solicitation PDU RPL
Configuration Client waits for a response message to arrive in milliseconds. This value can be
changed at runtime using [`bt_mesh_sol_pdu_rpl_cli_timeout_set()`](../../../../doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.md#gadabdbd95f39a498307e3ca9e50acfeb9).

## API reference

[Bluetooth Mesh Solicitation PDU RPL Client](../../../../doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.md)
