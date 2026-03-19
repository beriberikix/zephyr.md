---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/od_cli.html
original_path: connectivity/bluetooth/api/mesh/od_cli.html
---

# On-Demand Private Proxy Client

The On-Demand Private Proxy Client model is a foundation model defined by the Bluetooth Mesh
specification. The model is optional, and is enabled with the
[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI") option.

The On-Demand Private Proxy Client model was introduced in the Bluetooth Mesh Protocol Specification
version 1.1, and is used to set and retrieve the On-Demand Private GATT Proxy state. The state
defines how long a node will advertise Mesh Proxy Service with Private Network Identity type after
it receives a Solicitation PDU.

The On-Demand Private Proxy Client model communicates with an On-Demand Private Proxy Server model
using the device key of the node containing the target On-Demand Private Proxy Server model
instance.

If present, the On-Demand Private Proxy Client model must only be instantiated on the primary
element.

## Configurations

The On-Demand Private Proxy Client model behavior can be configured with the transmission timeout
option [`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT"). The
[`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT`](../../../../kconfig.md#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT "CONFIG_BT_MESH_OD_PRIV_PROXY_CLI_TIMEOUT") controls how long the Client waits for a
state response message to arrive in milliseconds. This value can be changed at runtime using
[`bt_mesh_od_priv_proxy_cli_timeout_set()`](../../../../doxygen/html/group__bt__mesh__od__priv__proxy__cli.md#gad613c78e708f0df5aabda9e16fae6a2c).

## API reference

[Bluetooth Mesh On-Demand Private GATT Proxy Client](../../../../doxygen/html/group__bt__mesh__od__priv__proxy__cli.md)
