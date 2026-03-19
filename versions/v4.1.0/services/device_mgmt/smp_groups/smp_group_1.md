---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/device_mgmt/smp_groups/smp_group_1.html
original_path: services/device_mgmt/smp_groups/smp_group_1.html
---

# Application/software image management group

Application/software image management group defines following commands:

| `Command ID` | Command description |
| --- | --- |
| `0` | State of images |
| `1` | Image upload |
| `2` | File (reserved but not supported by Zephyr) |
| `3` | Corelist (reserved but not supported by Zephyr) |
| `4` | Coreload (reserved but not supported by Zephyr) |
| `5` | Image erase |
| `6` | Slot info |

## Notion of “slots” and “images” in Zephyr

The “slot” and “image” definition comes from mcuboot where “image” would
consist of two “slots”, further named “primary” and “secondary”; the application
is supposed to run from the “primary slot” and update is supposed to be
uploaded to the “secondary slot”; the mcuboot is responsible in swapping
slots on boot.
This means that pair of slots is dedicated to single upgradable application.
In case of Zephyr this gets a little bit confusing because DTS will use
“slot0\_partition” and “slot1\_partition”, as label of `fixed-partition` dedicated
to single application, but will name them as “image-0” and “image-1” respectively.

Currently Zephyr supports at most two images, in which case mapping is as follows:

| Image | Slot labels | Slot Names |
| --- | --- | --- |
| 1 | “slot0\_partition” “slot1\_partition” | “image-0” “image-1” |
| 2 | “slot2\_partition” “slot3\_partition” | “image-2” “image-3” |

## State of images

The command is used to set state of images and obtain list of images
with their current state.

### Get state of images request

Get state of images request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `1` | `0` |

The command sends an empty CBOR map as data.

### Get state of images response

Get state of images response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `1` | `0` |

Note

Below definition of the response contains “image” field that has been marked
as optional(opt): the field may not appear in response when target application
does not support more than one image. The field is mandatory when application
supports more than one application image to allow identifying which image
information is listed.

A response will only contain information for valid images, if an image can not
be identified as valid it is simply skipped.

CBOR data of successful response:

```text
{
    (str)"images" : [
        {
            (str,opt)"image"        : (uint)
            (str)"slot"             : (uint)
            (str)"version"          : (str)
            (str,opt*)"hash"        : (byte str)
            (str,opt)"bootable"     : (bool)
            (str,opt)"pending"      : (bool)
            (str,opt)"confirmed"    : (bool)
            (str,opt)"active"       : (bool)
            (str,opt)"permanent"    : (bool)
        }
        ...
    ]
    (str,opt)"splitStatus" : (int)
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
    (str,opt)"rsn"  : (str)
}
```

where:

| “image” | semi-optional image number; the field is not required when only one image is supported by the running application. |
| --- | --- |
| “slot” | slot number within “image”; each image has two slots : primary (running one) = 0 and secondary (for DFU dual-bank purposes) = 1. |
| “version” | string representing image version, as set with `imgtool`. |
| “hash” | SHA256 hash of the image header and body. Note that this will not be the same as the SHA256 of the whole file, it is the field in the MCUboot TLV section that contains a hash of the data which is used for signature verification purposes. This field is optional but only optional when using MCUboot’s serial recovery feature with one pair of image slots, Kconfig `CONFIG_BOOT_SERIAL_IMG_GRP_HASH` can be disabled to remove support for hashes in this configuration. MCUmgr in applications must support sending hashes.  Note  See `IMAGE_TLV_SHA256` in the MCUboot image format documentation link below. |
| “bootable” | true if image has bootable flag set; this field does not have to be present if false. |
| “pending” | true if image is set for next swap; this field does not have to be present if false. |
| “confirmed” | true if image has been confirmed; this field does not have to be present if false. |
| “active” | true if image is currently active application; this field does not have to be present if false. |
| “permanent” | true if image is to stay in primary slot after the next boot; this does not have to be present if false. |
| “splitStatus” | states whether loader of split image is compatible with application part; this is unused by Zephyr. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
| “rsn” | optional string that clarifies reason for an error; specifically useful when `rc` is [`MGMT_ERR_EUNKNOWN`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be). |

Note

For more information on how does image/slots function, please refer to
the MCUBoot documentation
[https://docs.mcuboot.com/design.html#image-slots](https://docs.mcuboot.com/design.html#image-slots)
For information on MCUboot image format, please reset to the MCUboot
documentation [https://docs.mcuboot.com/design.html#image-format](https://docs.mcuboot.com/design.html#image-format)

### Set state of image request

Set state of image request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `1` | `0` |

CBOR data of request:

```text
{
    (str,opt)"hash"     : (str)
    (str)"confirm"      : (bool)
}
```

If “confirm” is false or not provided, an image with the “hash” will be set for
test, which means that it will not be marked as permanent and upon hard reset
the previous application will be restored to the primary slot.
In case when “confirm” is true, the “hash” is optional as the currently running
application will be assumed as target for confirmation.

### Set state of image response

The response takes the same format as [Get state of images response](#mcumgr-smp-protocol-op-1-grp-1-cmd-0)

## Image upload

The image upload command allows to update application image.

### Image upload request

The image upload request is sent for each chunk of image that is uploaded, until
complete image gets uploaded to a device.

Image upload request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `1` | `1` |

CBOR data of request:

```text
{
    (str,opt)"image"    : (uint)
    (str,opt)"len"      : (uint)
    (str)"off"          : (uint)
    (str,opt)"sha"      : (byte str)
    (str)"data"         : (byte str)
    (str,opt)"upgrade"  : (bool)
}
```

where:

| “image” | optional image number, it does not have to appear in request at all, in which case it is assumed to be 0. Should only be present when “off” is 0. |
| --- | --- |
| “len” | optional length of an image. Must appear when “off” is 0. |
| “off” | offset of image chunk the request carries. |
| “sha” | SHA256 hash of an upload; this is used to identify an upload session (e.g. to allow MCUmgr to continue a broken session), and for image verification purposes. This must be a full SHA256 hash of the whole image being uploaded, or not included if the hash is not available (in which case, upload session continuation and image verification functionality will be unavailable). Should only be present when “off” is 0. |
| “data” | image data to write at provided offset. |
| “upgrade” | optional flag that states that only upgrade should be allowed, so if the version of uploaded software is not higher then already on a device, the image upload will be rejected. Zephyr compares major, minor and revision (x.y.z) by default unless [`CONFIG_MCUMGR_GRP_IMG_VERSION_CMP_USE_BUILD_NUMBER`](../../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_VERSION_CMP_USE_BUILD_NUMBER "CONFIG_MCUMGR_GRP_IMG_VERSION_CMP_USE_BUILD_NUMBER") is set, whereby it will compare build numbers too. Should only be present when “off” is 0. |

Note

There is no field representing size of chunk that is carried as “data” because
that information is embedded within “data” field itself.

Note

It is possible that a server will respond to an upload with “off” of 0, this
may happen if an upload on another transport (or outside of MCUmgr entirely)
is started, if the device has rebooted or if a packet has been lost. If this
happens, a client must re-send all the required and optional fields that it
sent in the original first packet so that the upload state can be re-created
by the server. If the original fields are not included, the upload will be
unable to continue.

The MCUmgr library uses “sha” field to tag ongoing update session, to be able
to continue it in case when it gets broken, and for upload verification
purposes.
If library gets request with “off” equal zero it checks stored “sha” within its
state and if it matches it will respond to update client application with
offset that it should continue with.
If this hash is not available (e.g. because a file is being streamed) then it
must not be provided, image verification and upload session continuation
features will be unavailable in this case.

### Image upload response

Image upload response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `1` | `1` |

CBOR data of successful response:

```text
{
    (str,opt)"off"    : (uint)
    (str,opt)"match"  : (bool)
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
    (str,opt)"rsn"  : (str)
}
```

where:

| “off” | offset of last successfully written byte of update. |
| --- | --- |
| “match” | indicates if the uploaded data successfully matches the provided SHA256 hash or not, only sent in the final packet if [`CONFIG_IMG_ENABLE_IMAGE_CHECK`](../../../kconfig.md#CONFIG_IMG_ENABLE_IMAGE_CHECK "CONFIG_IMG_ENABLE_IMAGE_CHECK") is enabled. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
| “rsn” | optional string that clarifies reason for an error; specifically useful when `rc` is [`MGMT_ERR_EUNKNOWN`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be). |

The “off” field is only included in responses to successfully processed requests;
if “rc” is negative then “off” may not appear.

## Image erase

The command is used for erasing image slot on a target device.

Note

This is synchronous command which means that a sender of request will not
receive response until the command completes, which can take a long time.

### Image erase request

Image erase request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `2` | `1` | `5` |

CBOR data of request:

```text
{
    (str,opt)"slot"     : (uint)
}
```

where:

| “slot” | optional slot number, it does not have to appear in the request at all, in which case it is assumed to be 1. |
| --- | --- |

### Image erase response

Image erase response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `3` | `1` | `5` |

The command sends an empty CBOR map as data if successful. In case of error the
CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
    (str,opt)"rsn"  : (str)
}
```

where:

| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| --- | --- |
| “err” -> “rc” | contains the index of the group-based error code. Only appears if non-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
| “rsn” | optional string that clarifies reason for an error; specifically useful when `rc` is [`MGMT_ERR_EUNKNOWN`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be). |

Note

Response from Zephyr running device may have “rc” value of
[`MGMT_ERR_EBADSTATE`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787), which means that the secondary
image has been marked for next boot already and may not be erased.

## Slot info

The command is used for fetching information on slots that are available. This command can be
enabled with [`CONFIG_MCUMGR_GRP_IMG_SLOT_INFO`](../../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_SLOT_INFO "CONFIG_MCUMGR_GRP_IMG_SLOT_INFO").

### Slot info request

Slot info request header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `0` | `1` | `6` |

The command sends an empty CBOR map as data.

### Slot info response

Slot info response header fields:

| `OP` | `Group ID` | `Command ID` |
| --- | --- | --- |
| `1` | `1` | `6` |

CBOR data of successful response:

```text
{
    (str)"images" : [
        {
            (str)"image"                        : (uint)
            (str)"slots" : [
                {
                    (str)"slot"                 : (uint)
                    (str)"size"                 : (uint)
                    (str,opt)"upload_image_id"  : (uint)
                }
                ...
            ]
            (str,opt)"max_image_size"           : (uint)
        }
        ...
    ]
}
```

In case of error the CBOR data takes the form:

SMP version 2SMP version 1 (and non-group SMP version 2)

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

```text
{
    (str)"rc"       : (int)
}
```

where:

| “image” | the image number being enumerated. |
| --- | --- |
| “slot” | the slot inside the image being enumerated (note: this will be 0 or 1, it is the slot of the image not the physical slot number). |
| “size” | the size of the slot. |
| “upload\_image\_id” | optional field (only present if [`CONFIG_MCUMGR_GRP_IMG_DIRECT_UPLOAD`](../../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_DIRECT_UPLOAD "CONFIG_MCUMGR_GRP_IMG_DIRECT_UPLOAD") is enabled to allow direct image uploads) which specifies the image ID that can be used by external tools to upload an image to that slot. |
| “max\_image\_size” | optional field (only present if [`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD`](../../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD "CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD") or [`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO`](../../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO "CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO") are enabled) which specifies the maximum size of an application that can be uploaded to that image number. |
| “err” -> “group” | [`mcumgr_group_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5) group of the group-based error code. Only appears if an error is returned when using SMP version 2. |
| “err” -> “rc” | contains the index of the group-based error code. Only appears ifnon-zero (error condition) when using SMP version 2. |
| “rc” | [`mcumgr_err_t`](../../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) only appears if non-zero (error condition) when using SMP version 1 or for SMP errors when using SMP version 2. |
