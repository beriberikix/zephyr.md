---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/dfd_srv.html
original_path: connectivity/bluetooth/api/mesh/dfd_srv.html
---

# Firmware Distribution Server

The Firmware Distribution Server model implements the Distributor role for the
[Device Firmware Update (DFU)](dfu.md#bluetooth-mesh-dfu) subsystem. It extends the [BLOB Transfer Server](blob_srv.md#bluetooth-mesh-blob-srv), which it uses to
receive the firmware image binary from the Initiator node. It also instantiates a
[Firmware Update Client](dfu_cli.md#bluetooth-mesh-dfu-cli), which it uses to distribute firmware updates throughout the mesh
network.

Note

Currently, the Firmware Distribution Server supports out-of-band (OOB) retrieval of firmware
images over SMP service only.

The Firmware Distribution Server does not have an API of its own, but relies on a Firmware
Distribution Client model on a different device to give it information and trigger image
distribution and upload.

## Firmware slots

The Firmware Distribution Server is capable of storing multiple firmware images for distribution.
Each slot contains a separate firmware image with metadata, and can be distributed to other mesh
nodes in the network in any order. The contents, format and size of the firmware images are vendor
specific, and may contain data from other vendors. The application should never attempt to execute
or modify them.

The slots are managed remotely by a Firmware Distribution Client, which can both upload new slots
and delete old ones. The application is notified of changes to the slots through the Firmware
Distribution Server’s callbacks (`bt_mesh_fd_srv_cb`). While the metadata for each
firmware slot is stored internally, the application must provide a [BLOB streams](blob.md#bluetooth-mesh-blob-stream)
for reading and writing the firmware image.

## API reference

[Firmware Distribution Server model](../../../../doxygen/html/group__bt__mesh__dfd__srv.md)
