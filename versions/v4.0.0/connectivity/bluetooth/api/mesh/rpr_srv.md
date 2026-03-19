---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/rpr_srv.html
original_path: connectivity/bluetooth/api/mesh/rpr_srv.html
---

# Remote Provisioning Server

The Remote Provisioning Server model is a foundation model defined by the Bluetooth
mesh specification. It is enabled with the
[`CONFIG_BT_MESH_RPR_SRV`](../../../../kconfig.md#CONFIG_BT_MESH_RPR_SRV "CONFIG_BT_MESH_RPR_SRV") option.

The Remote Provisioning Server model is introduced in the Bluetooth Mesh Protocol
Specification version 1.1, and is used to support the functionality of remotely
provisioning devices into a mesh network.

The Remote Provisioning Server does not have an API of its own, but relies on a
[Remote Provisioning Client](rpr_cli.md#bluetooth-mesh-models-rpr-cli) to control it. The Remote Provisioning Server
model only accepts messages encrypted with the node’s device key.

If present, the Remote Provisioning Server model must be instantiated on the primary element.

Note that after refreshing the device key, node address or Composition Data through a Node
Provisioning Protocol Interface (NPPI) procedure, the [`bt_mesh_prov.reprovisioned`](../../../../doxygen/html/structbt__mesh__prov.md#ac131476cdeb002f0027407b4cf80c2b5)
callback is triggered. See section [Remote Provisioning Client](rpr_cli.md#bluetooth-mesh-models-rpr-cli) for further details.

## Limitations

The following limitations apply to Remote Provisioning Server model:

- Provisioning of unprovisioned device using PB-GATT is not supported.
- All Node Provisioning Protocol Interface (NPPI) procedures are supported. However, if the composition data of a device gets changed after device firmware update (see [firmware effect](dfu.md#bluetooth-mesh-dfu-firmware-effect)), it is not possible for the device to remain provisioned. The device should be unprovisioned if its composition data is expected to change.

### API reference

[Remote provisioning server](../../../../doxygen/html/group__bt__mesh__rpr__srv.md)
