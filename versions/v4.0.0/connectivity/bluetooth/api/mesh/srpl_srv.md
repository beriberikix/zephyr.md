---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/srpl_srv.html
original_path: connectivity/bluetooth/api/mesh/srpl_srv.html
---

# Solicitation PDU RPL Configuration Server

The Solicitation PDU RPL Configuration Server model is a foundation model defined by the Bluetooth
mesh specification. The model is enabled if the node has the [On-Demand Private Proxy Server](od_srv.md#bluetooth-mesh-od-srv) enabled.

The Solicitation PDU RPL Configuration Server model was introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and manages the Solicitation Replay Protection List (SRPL) saved on the
device. The SRPL is used to reject Solicitation PDUs that are already processed by a node. When a
valid Solicitation PDU message is successfully processed by a node, the SSRC field and SSEQ field
of the message are stored in the node’s SRPL.

The Solicitation PDU RPL Configuration Server does not have an API of its own, and relies on a
[Solicitation PDU RPL Configuration Client](srpl_cli.md#bluetooth-mesh-srpl-cli) to control it. The model only accepts messages encrypted with an
application key as configured by the Configuration Client.

If present, the Solicitation PDU RPL Configuration Server model must only be instantiated on the
primary element.

## Configurations

For the Solicitation PDU RPL Configuration Server model, the
[`CONFIG_BT_MESH_PROXY_SRPL_SIZE`](../../../../kconfig.md#CONFIG_BT_MESH_PROXY_SRPL_SIZE "CONFIG_BT_MESH_PROXY_SRPL_SIZE") option can be configured to set the size of the
SRPL.

## API reference

[Bluetooth Mesh Solicitation PDU RPL Server](../../../../doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.md)
