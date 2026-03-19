---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/mesh/health_srv.html
original_path: connectivity/bluetooth/api/mesh/health_srv.html
---

# Health Server

The Health Server model provides attention callbacks and node diagnostics for
[Health Client](health_cli.md#bluetooth-mesh-models-health-cli) models. It is primarily used to report
faults in the mesh node and map the mesh nodes to their physical location.

If present, the Health Server model must be instantiated on the primary element.

## Faults

The Health Server model may report a list of faults that have occurred in the
device’s lifetime. Typically, the faults are events or conditions that may
alter the behavior of the node, like power outages or faulty peripherals.
Faults are split into warnings and errors. Warnings indicate conditions that
are close to the limits of what the node is designed to withstand, but not
necessarily damaging to the device. Errors indicate conditions that are
outside of the node’s design limits, and may have caused invalid behavior or
permanent damage to the device.

Fault values `0x01` to `0x7f` are reserved for the Bluetooth Mesh
specification, and the full list of specification defined faults are available
in [Health faults](#bluetooth-mesh-health-faults). Fault values `0x80` to `0xff` are
vendor specific. The list of faults are always reported with a company ID to
help interpreting the vendor specific faults.

## Attention state

The attention state is used to make the device call attention to itself
through some physical behavior like blinking, playing a sound or vibrating.
The attention state may be used during provisioning to let the user know which
device they’re provisioning, as well as through the Health models at runtime.

The attention state is always assigned a timeout in the range of one to 255
seconds when enabled. The Health Server API provides two callbacks for the
application to run their attention calling behavior:
[`bt_mesh_health_srv_cb.attn_on`](../../../../doxygen/html/structbt__mesh__health__srv__cb.md#ad9e8a392943d4848190c4513327bc52c) is called at the beginning of the
attention period, [`bt_mesh_health_srv_cb.attn_off`](../../../../doxygen/html/structbt__mesh__health__srv__cb.md#abd881db6cf849433808bc6464e109b60) is called at
the end.

The remaining time for the attention period may be queried through
[`bt_mesh_health_srv.attn_timer`](../../../../doxygen/html/structbt__mesh__health__srv.md#a8df7f6c7e434cb717b9b51a3167b5e86).

## API reference

[Health Server Model](../../../../doxygen/html/group__bt__mesh__health__srv.md)

### Health faults

Fault values defined by the Bluetooth Mesh specification.

[Health faults](../../../../doxygen/html/group__bt__mesh__health__faults.md)
