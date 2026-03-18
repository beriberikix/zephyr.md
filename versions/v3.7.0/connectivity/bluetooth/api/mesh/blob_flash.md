---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/mesh/blob_flash.html
original_path: connectivity/bluetooth/api/mesh/blob_flash.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BLOB Flash

The BLOB Flash Readers and Writers implement BLOB reading to and writing from flash partitions
defined in the [flash map](../../../../services/storage/flash_map/flash_map.md#flash-map-api).

## BLOB Flash Reader

The BLOB Flash Reader interacts with the BLOB Transfer Client to read BLOB data directly from flash.
It must be initialized by calling `bt_mesh_blob_flash_rd_init()` before being passed to the
BLOB Transfer Client. Each BLOB Flash Reader only supports one transfer at the time.

## BLOB Flash Writer

The BLOB Flash Writer interacts with the BLOB Transfer Server to write BLOB data directly to flash.
It must be initialized by calling `bt_mesh_blob_flash_rd_init()` before being passed to the
BLOB Transfer Server. Each BLOB Flash Writer only supports one transfer at the time, and requires a
block size that is a multiple of the flash page size. If a transfer is started with a block size
lower than the flash page size, the transfer will be rejected.

The BLOB Flash Writer copies chunk data into a buffer to accommodate chunks that are unaligned with
the flash write block size. The buffer data is padded with `0xff` if either the start or length of
the chunk is unaligned.

## API Reference

*group* Bluetooth Mesh BLOB flash stream
:   Functions

    int bt\_mesh\_blob\_io\_flash\_init(struct [bt\_mesh\_blob\_io\_flash](#c.bt_mesh_blob_io_flash) \*flash, uint8\_t area\_id, off\_t offset)
    :   Initialize a flash stream.

        Parameters:
        :   - **flash** – Flash stream.
            - **area\_id** – Flash partition identifier. See [flash\_area\_open](../../../../services/storage/flash_map/flash_map.md#group__flash__area__api_1ga6fe2593210688eb85e03bea5f96ea2f7).
            - **offset** – Offset into the flash area, in bytes.

        Returns:
        :   0 on success or (negative) error code otherwise.

    struct bt\_mesh\_blob\_io\_flash
    :   *#include <blob\_io\_flash.h>*

        BLOB flash stream.

        Public Members

        uint8\_t area\_id
        :   Flash area ID to write the BLOB to.

        enum [bt\_mesh\_blob\_io\_mode](blob.md#c.bt_mesh_blob_io_mode "bt_mesh_blob_io_mode") mode
        :   Active stream mode.

        off\_t offset
        :   Offset into the flash area to place the BLOB at (in bytes).
