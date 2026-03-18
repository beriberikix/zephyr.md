---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/dfu_srv.html
original_path: connectivity/bluetooth/api/mesh/dfu_srv.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Firmware Update Server

The Firmware Update Server model implements the Target node functionality of the
[Device Firmware Update (DFU)](dfu.md#bluetooth-mesh-dfu) subsystem. It extends the [BLOB Transfer Server](blob_srv.md#bluetooth-mesh-blob-srv), which it uses to
receive the firmware image binary from the Distributor node.

Together with the extended BLOB Transfer Server model, the Firmware Update Server model implements
all the required functionality for receiving firmware updates over the mesh network, but does not
provide any functionality for storing, applying or verifying the images.

## Firmware images

The Firmware Update Server holds a list of all the updatable firmware images on the device. The full
list shall be passed to the server through the `_imgs` parameter in
[`BT_MESH_DFU_SRV_INIT`](#c.BT_MESH_DFU_SRV_INIT), and must be populated before the Bluetooth Mesh subsystem is
started. Each firmware image in the image list must be independently updatable, and should have its
own firmware ID.

For instance, a device with an upgradable bootloader, an application and a peripheral chip with
firmware update capabilities could have three entries in the firmware image list, each with their
own separate firmware ID.

## Receiving transfers

The Firmware Update Server model uses a BLOB Transfer Server model on the same element to transfer
the binary image. The interaction between the Firmware Update Server, BLOB Transfer Server and
application is described below:

![Bluetooth Mesh Firmware Update Server transfer](../../../../_images/dfu_srv.svg)

Bluetooth Mesh Firmware Update Server transfer

### Transfer check

The transfer check is an optional pre-transfer check the application can perform on incoming
firmware image metadata. The Firmware Update Server performs the transfer check by calling the
[`check`](#c.bt_mesh_dfu_srv_cb.check) callback.

The result of the transfer check is a pass/fail status return and the expected
[`bt_mesh_dfu_effect`](dfu.md#c.bt_mesh_dfu_effect "bt_mesh_dfu_effect"). The DFU effect return parameter will be communicated back to the
Distributor, and should indicate what effect the firmware update will have on the mesh state of the
device.

#### Composition Data and Models Metadata

If the transfer will cause the device to change its Composition Data or become
unprovisioned, this should be communicated through the effect parameter of the metadata check.

When the transfer will cause the Composition Data to change, and the
[Remote Provisioning Server](rpr_srv.md#bluetooth-mesh-models-rpr-srv) is supported, the Composition Data of the new firmware image
will be represented by Composition Data Pages 128, 129, and 130. The Models Metadata of the new
firmware image will be represented by Models Metadata Page 128. Composition Data Pages 0, 1 and 2,
and Models Metadata Page 0, will represent the Composition Data and the Models Metadata of the old
firmware image until the device is reprovisioned with Node Provisioning Protocol Interface (NPPI)
procedures using the [Remote Provisioning Client](rpr_cli.md#bluetooth-mesh-models-rpr-cli).

The application must call functions [`bt_mesh_comp_change_prepare()`](access.md#c.bt_mesh_comp_change_prepare "bt_mesh_comp_change_prepare") and
[`bt_mesh_models_metadata_change_prepare()`](access.md#c.bt_mesh_models_metadata_change_prepare "bt_mesh_models_metadata_change_prepare") to store the existing Composition Data and Models
Metadata pages before booting into the firmware with the updated Composition Data and Models
Metadata. The old Composition Data will then be loaded into Composition Data Pages 0, 1 and 2,
while the Composition Data in the new firmware will be loaded into Composition Data Pages 128, 129
and 130. The Models Metadata for the old image will be loaded into Models Metadata Page 0, and the
Models Metadata for the new image will be loaded into Models Metadata Page 128.

Limitation:

- It is not possible to change the Composition Data of the device and keep the device provisioned
  and working with the old firmware after the new firmware image is applied.

### Start

The Start procedure prepares the application for the incoming transfer. It’ll contain information
about which image is being updated, as well as the update metadata.

The Firmware Update Server [`start`](#c.bt_mesh_dfu_srv_cb.start) callback must return a
pointer to the BLOB Writer the BLOB Transfer Server will send the BLOB to.

### BLOB transfer

After the setup stage, the Firmware Update Server prepares the BLOB Transfer Server for the incoming
transfer. The entire firmware image is transferred to the BLOB Transfer Server, which passes the
image to its assigned BLOB Writer.

At the end of the BLOB transfer, the Firmware Update Server calls its
[`end`](#c.bt_mesh_dfu_srv_cb.end) callback.

### Image verification

After the BLOB transfer has finished, the application should verify the image in any way it can to
ensure that it is ready for being applied. Once the image has been verified, the application calls
[`bt_mesh_dfu_srv_verified()`](#c.bt_mesh_dfu_srv_verified).

If the image can’t be verified, the application calls [`bt_mesh_dfu_srv_rejected()`](#c.bt_mesh_dfu_srv_rejected).

### Applying the image

Finally, if the image was verified, the Distributor may instruct the Firmware Update Server to apply
the transfer. This is communicated to the application through the [`apply`](#c.bt_mesh_dfu_srv_cb.apply) callback. The application should swap the image and start running with
the new firmware. The firmware image table should be updated to reflect the new firmware ID of the
updated image.

When the transfer applies to the mesh application itself, the device might have to reboot as part of
the swap. This restart can be performed from inside the apply callback, or done asynchronously.
After booting up with the new firmware, the firmware image table should be updated before the
Bluetooth Mesh subsystem is started.

The Distributor will read out the firmware image table to confirm that the transfer was successfully
applied. If the metadata check indicated that the device would become unprovisioned, the Target node
is not required to respond to this check.

## API reference

*group* bt\_mesh\_dfu\_srv
:   API for the Bluetooth Mesh Firmware Update Server model.

    Defines

    BT\_MESH\_DFU\_SRV\_INIT(\_handlers, \_imgs, \_img\_count)
    :   Initialization parameters for [Firmware Update Server model](#group__bt__mesh__dfu__srv).

        Parameters:
        :   - **\_handlers** – DFU handler function structure.
            - **\_imgs** – List of [bt\_mesh\_dfu\_img](dfu.md#structbt__mesh__dfu__img) managed by this Server.
            - **\_img\_count** – Number of DFU images managed by this Server.

    BT\_MESH\_MODEL\_DFU\_SRV(\_srv)
    :   Firmware Update Server model entry.

        Parameters:
        :   - **\_srv** – Pointer to a [Firmware Update Server model](#group__bt__mesh__dfu__srv) instance.

    Functions

    void bt\_mesh\_dfu\_srv\_verified(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Accept the received DFU transfer.

        Should be called at the end of a successful DFU transfer.

        If the DFU transfer completes successfully, the application should verify the image validity (including any image authentication or integrity checks), and call this function if the image is ready to be applied.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

    void bt\_mesh\_dfu\_srv\_rejected(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Reject the received DFU transfer.

        Should be called at the end of a successful DFU transfer.

        If the DFU transfer completes successfully, the application should verify the image validity (including any image authentication or integrity checks), and call this function if one of the checks fail.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

    void bt\_mesh\_dfu\_srv\_cancel(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Cancel the ongoing DFU transfer.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

    void bt\_mesh\_dfu\_srv\_applied(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Confirm that the received DFU transfer was applied.

        Should be called as a result of the [bt\_mesh\_dfu\_srv\_cb::apply](#structbt__mesh__dfu__srv__cb_1afe4b6ca9f56938695addba6ecc18bb4b) callback.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

    bool bt\_mesh\_dfu\_srv\_is\_busy(const struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Check if the Firmware Update Server is busy processing a transfer.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

        Returns:
        :   true if a DFU procedure is in progress, false otherwise.

    uint8\_t bt\_mesh\_dfu\_srv\_progress(const struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv)
    :   Get the progress of the current DFU procedure, in percent.

        Parameters:
        :   - **srv** – Firmware Update Server instance.

        Returns:
        :   The current transfer progress in percent.

    struct bt\_mesh\_dfu\_srv\_cb
    :   *#include <dfu\_srv.h>*

        Firmware Update Server event callbacks.

        Public Members

        int (\*check)(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*metadata, enum [bt\_mesh\_dfu\_effect](dfu.md#c.bt_mesh_dfu_effect "bt_mesh_dfu_effect") \*effect)
        :   Transfer check callback.

            The transfer check can be used to validate the incoming transfer before it starts. The contents of the metadata is implementation specific, and should contain all the information the application needs to determine whether this image should be accepted, and what the effect of the transfer would be.

            If applying the image will have an effect on the provisioning state of the mesh stack, this can be communicated through the `effect` return parameter.

            The metadata check can be performed both as part of starting a new transfer and as a separate procedure.

            This handler is optional.

            Param srv:
            :   Firmware Update Server instance.

            Param img:
            :   DFU image the metadata check is performed on.

            Param metadata:
            :   Image metadata.

            Param effect:
            :   Return parameter for the image effect on the provisioning state of the mesh stack.

            Return:
            :   0 on success, or (negative) error code otherwise.

        int (\*start)(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img, struct [net\_buf\_simple](../../../networking/api/net_buf.md#c.net_buf_simple "net_buf_simple") \*metadata, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*\*io)
        :   Transfer start callback.

            Called when the Firmware Update Server is ready to start a new DFU transfer. The application must provide an initialized BLOB stream to be used during the DFU transfer.

            The following error codes are treated specially, and should be used to communicate these issues:

            - `-ENOMEM:` The device cannot fit this image.
            - `-EBUSY:` The application is temporarily unable to accept the transfer.
            - `-EALREADY:` The device has already received and verified this image, and there’s no need to transfer it again. The Firmware Update model will skip the transfer phase, and mark the image as verified.

            This handler is mandatory.

            Param srv:
            :   Firmware Update Server instance.

            Param img:
            :   DFU image being updated.

            Param metadata:
            :   Image metadata.

            Param io:
            :   BLOB stream return parameter. Must be set to a valid BLOB stream by the callback.

            Return:
            :   0 on success, or (negative) error code otherwise. Return codes `-ENOMEM`, `-EBUSY` `-EALREADY` will be passed to the updater, other error codes are reported as internal errors.

        void (\*end)(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img, bool success)
        :   Transfer end callback.

            This handler is optional.

            If the transfer is successful, the application should verify the firmware image, and call either [bt\_mesh\_dfu\_srv\_verified](#group__bt__mesh__dfu__srv_1ga64eeb5bfe9bac8c1120c5e0aa9ce02ac) or [bt\_mesh\_dfu\_srv\_rejected](#group__bt__mesh__dfu__srv_1ga77142a1f3cfe2ff1d53332114f977b38) depending on the outcome.

            If the transfer fails, the Firmware Update Server will be available for new transfers immediately after this function returns.

            Param srv:
            :   Firmware Update Server instance.

            Param img:
            :   DFU image that failed the update.

            Param success:
            :   Whether the DFU transfer was successful.

        int (\*recover)(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img, const struct [bt\_mesh\_blob\_io](blob.md#c.bt_mesh_blob_io "bt_mesh_blob_io") \*\*io)
        :   Transfer recovery callback.

            If the device reboots in the middle of a transfer, the Firmware Update Server calls this function when the Bluetooth Mesh subsystem is started.

            This callback is optional, but transfers will not be recovered after a reboot without it.

            Param srv:
            :   Firmware Update Server instance.

            Param img:
            :   DFU image being updated.

            Param io:
            :   BLOB stream return parameter. Must be set to a valid BLOB stream by the callback.

            Return:
            :   0 on success, or (negative) error code to abandon the transfer.

        int (\*apply)(struct [bt\_mesh\_dfu\_srv](#c.bt_mesh_dfu_srv) \*srv, const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*img)
        :   Transfer apply callback.

            Called after a transfer has been validated, and the updater sends an apply message to the Target nodes.

            This handler is optional.

            Param srv:
            :   Firmware Update Server instance.

            Param img:
            :   DFU image that should be applied.

            Return:
            :   0 on success, or (negative) error code otherwise.

    struct bt\_mesh\_dfu\_srv
    :   *#include <dfu\_srv.h>*

        Firmware Update Server instance.

        Should be initialized with [BT\_MESH\_DFU\_SRV\_INIT](#group__bt__mesh__dfu__srv_1ga8467cd5241dfdcd7add718bbaae6fa60).

        Public Members

        struct [bt\_mesh\_blob\_srv](blob_srv.md#c.bt_mesh_blob_srv "bt_mesh_blob_srv") blob
        :   Underlying BLOB Transfer Server.

        const struct [bt\_mesh\_dfu\_srv\_cb](#c.bt_mesh_dfu_srv_cb) \*cb
        :   Callback structure.

        const struct [bt\_mesh\_dfu\_img](dfu.md#c.bt_mesh_dfu_img "bt_mesh_dfu_img") \*imgs
        :   List of updatable images.

        size\_t img\_count
        :   Number of updatable images.
