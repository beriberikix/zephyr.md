---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/device_mgmt/dfu.html
original_path: services/device_mgmt/dfu.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Device Firmware Upgrade

## Overview

The Device Firmware Upgrade subsystem provides the necessary frameworks to
upgrade the image of a Zephyr-based application at run time. It currently
consists of two different modules:

- [subsys/dfu/boot/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/boot/): Interface code to bootloaders
- [subsys/dfu/img\_util/](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/img_util/): Image management code

The DFU subsystem deals with image management, but not with the transport
or management protocols themselves required to send the image to the target
device. For information on these protocols and frameworks please refer to the
[Device Management](index.md#device-mgmt) section.

### Flash Image

The flash image API as part of the Device Firmware Upgrade (DFU) subsystem
provides an abstraction on top of Flash Stream to simplify writing firmware
image chunks to flash.

#### API Reference

*group* flash\_img\_api
:   Abstraction layer to write firmware images to flash.

    Functions

    int flash\_img\_init\_id(struct [flash\_img\_context](#c.flash_img_context) \*ctx, uint8\_t area\_id)
    :   Initialize context needed for writing the image to the flash.

        Parameters:
        :   - **ctx** – context to be initialized
            - **area\_id** – flash area id of partition where the image should be written

        Returns:
        :   0 on success, negative errno code on fail

    int flash\_img\_init(struct [flash\_img\_context](#c.flash_img_context) \*ctx)
    :   Initialize context needed for writing the image to the flash.

        Parameters:
        :   - **ctx** – context to be initialized

        Returns:
        :   0 on success, negative errno code on fail

    size\_t flash\_img\_bytes\_written(struct [flash\_img\_context](#c.flash_img_context) \*ctx)
    :   Read number of bytes of the image written to the flash.

        Parameters:
        :   - **ctx** – context

        Returns:
        :   Number of bytes written to the image flash.

    int flash\_img\_buffered\_write(struct [flash\_img\_context](#c.flash_img_context) \*ctx, const uint8\_t \*data, size\_t len, bool flush)
    :   Process input buffers to be written to the image slot 1.

        flash memory in single blocks. Will store remainder between calls.

        A final call to this function with flush set to true will write out the remaining block buffer to flash. Since flash is written to in blocks, the contents of flash from the last byte written up to the next multiple of CONFIG\_IMG\_BLOCK\_BUF\_SIZE is padded with 0xff.

        Parameters:
        :   - **ctx** – context
            - **data** – data to write
            - **len** – Number of bytes to write
            - **flush** – when true this forces any buffered data to be written to flash

        Returns:
        :   0 on success, negative errno code on fail

    int flash\_img\_check(struct [flash\_img\_context](#c.flash_img_context) \*ctx, const struct [flash\_img\_check](#c.flash_img_check) \*fic, uint8\_t area\_id)
    :   Verify flash memory length bytes integrity from a flash area.

        The start point is indicated by an offset value.

        The function is enabled via CONFIG\_IMG\_ENABLE\_IMAGE\_CHECK Kconfig options.

        Parameters:
        :   - **ctx** – **[in]** context.
            - **fic** – **[in]** flash img check data.
            - **area\_id** – **[in]** flash area id of partition where the image should be verified.

        Returns:
        :   0 on success, negative errno code on fail

    struct flash\_img\_context
    :   *#include <flash\_img.h>*

    struct flash\_img\_check
    :   *#include <flash\_img.h>*

        Structure for verify flash region integrity.

        Match vector length is fixed and depends on size from hash algorithm used to verify flash integrity. The current available algorithm is SHA-256.

        Public Members

        size\_t clen
        :   Match vector data.

### MCUBoot API

The MCUboot API is provided to get version information and boot status of
application images. It allows to select application image and boot type
for the next boot.

#### API Reference

*group* mcuboot\_api
:   MCUboot public API for MCUboot control of image boot process.

    Defines

    BOOT\_SWAP\_TYPE\_NONE
    :   Attempt to boot the contents of slot 0.

    BOOT\_SWAP\_TYPE\_TEST
    :   Swap to slot 1.

        Absent a confirm command, revert back on next boot.

    BOOT\_SWAP\_TYPE\_PERM
    :   Swap to slot 1, and permanently switch to booting its contents.

    BOOT\_SWAP\_TYPE\_REVERT
    :   Swap back to alternate slot.

        A confirm changes this state to NONE.

    BOOT\_SWAP\_TYPE\_FAIL
    :   Swap failed because image to be run is not valid.

    BOOT\_IMG\_VER\_STRLEN\_MAX

    BOOT\_UPGRADE\_TEST
    :   Boot upgrade request modes.

    BOOT\_UPGRADE\_PERMANENT

    Functions

    int boot\_read\_bank\_header(uint8\_t area\_id, struct [mcuboot\_img\_header](#c.mcuboot_img_header) \*header, size\_t header\_size)
    :   Read the MCUboot image header information from an image bank.

        This attempts to parse the image header, From the start of the *area\_id* image.

        Parameters:
        :   - **area\_id** – [flash\_area](../storage/flash_map/flash_map.md#structflash__area) ID of image bank which stores the image.
            - **header** – On success, the returned header information is available in this structure.
            - **header\_size** – Size of the header structure passed by the caller. If this is not large enough to contain all of the necessary information, an error is returned.

        Returns:
        :   Zero on success, a negative value on error.

    bool boot\_is\_img\_confirmed(void)
    :   Check if the currently running image is confirmed as OK.

        MCUboot can perform “test” upgrades. When these occur, a new firmware image is installed and booted, but the old version will be reverted at the next reset unless the new image explicitly marks itself OK.

        This routine can be used to check if the currently running image has been marked as OK.

        See also

        [boot\_write\_img\_confirmed()](#group__mcuboot__api_1ga95ccc9e1c7460fec16b9ce9ac8ad7a72)

        Returns:
        :   True if the image is confirmed as OK, false otherwise.

    int boot\_write\_img\_confirmed(void)
    :   Marks the currently running image as confirmed.

        This routine attempts to mark the currently running firmware image as OK, which will install it permanently, preventing MCUboot from reverting it for an older image at the next reset.

        This routine is safe to call if the current image has already been confirmed. It will return a successful result in this case.

        Returns:
        :   0 on success, negative errno code on fail.

    int boot\_write\_img\_confirmed\_multi(int image\_index)
    :   Marks the image with the given index in the primary slot as confirmed.

        This routine attempts to mark the firmware image in the primary slot as OK, which will install it permanently, preventing MCUboot from reverting it for an older image at the next reset.

        This routine is safe to call if the current image has already been confirmed. It will return a successful result in this case.

        Parameters:
        :   - **image\_index** – Image pair index.

        Returns:
        :   0 on success, negative errno code on fail.

    int mcuboot\_swap\_type(void)
    :   Determines the action, if any, that mcuboot will take on the next reboot.

        Returns:
        :   a BOOT\_SWAP\_TYPE\_[…] constant on success, negative errno code on fail.

    int mcuboot\_swap\_type\_multi(int image\_index)
    :   Determines the action, if any, that mcuboot will take on the next reboot.

        Parameters:
        :   - **image\_index** – Image pair index.

        Returns:
        :   a BOOT\_SWAP\_TYPE\_[…] constant on success, negative errno code on fail.

    int boot\_request\_upgrade(int permanent)
    :   Marks the image in slot 1 as pending.

        On the next reboot, the system will perform a boot of the slot 1 image.

        Parameters:
        :   - **permanent** – Whether the image should be used permanently or only tested once: BOOT\_UPGRADE\_TEST=run image once, then confirm or revert. BOOT\_UPGRADE\_PERMANENT=run image forever.

        Returns:
        :   0 on success, negative errno code on fail.

    int boot\_request\_upgrade\_multi(int image\_index, int permanent)
    :   Marks the image with the given index in the secondary slot as pending.

        On the next reboot, the system will perform a boot of the secondary slot image.

        Parameters:
        :   - **image\_index** – Image pair index.
            - **permanent** – Whether the image should be used permanently or only tested once: BOOT\_UPGRADE\_TEST=run image once, then confirm or revert. BOOT\_UPGRADE\_PERMANENT=run image forever.

        Returns:
        :   0 on success, negative errno code on fail.

    int boot\_erase\_img\_bank(uint8\_t area\_id)
    :   Erase the image Bank.

        Parameters:
        :   - **area\_id** – [flash\_area](../storage/flash_map/flash_map.md#structflash__area) ID of image bank to be erased.

        Returns:
        :   0 on success, negative errno code on fail.

    ssize\_t boot\_get\_area\_trailer\_status\_offset(uint8\_t area\_id)
    :   Get the offset of the status in the image bank.

        Parameters:
        :   - **area\_id** – [flash\_area](../storage/flash_map/flash_map.md#structflash__area) ID of image bank to get the status offset

        Returns:
        :   a positive offset on success, negative errno code on fail

    ssize\_t boot\_get\_trailer\_status\_offset(size\_t area\_size)
    :   Get the offset of the status from an image bank size.

        Parameters:
        :   - **area\_size** – size of image bank

        Returns:
        :   offset of the status. When negative the status will not fit the given size

    struct mcuboot\_img\_sem\_ver
    :   *#include <mcuboot.h>*

        MCUboot image header representation for image version.

        The header for an MCUboot firmware image contains an embedded version number, in semantic versioning format. This structure represents the information it contains.

    struct mcuboot\_img\_header\_v1
    :   *#include <mcuboot.h>*

        Model for the MCUboot image header as of version 1.

        This represents the data present in the image header, in version 1 of the header format.

        Some information present in the header but not currently relevant to applications is omitted.

        Public Members

        uint32\_t image\_size
        :   The size of the image, in bytes.

        struct [mcuboot\_img\_sem\_ver](#c.mcuboot_img_sem_ver) sem\_ver
        :   The image version.

    struct mcuboot\_img\_header
    :   *#include <mcuboot.h>*

        Model for the MCUBoot image header.

        This contains the decoded image header, along with the major version of MCUboot that the header was built for.

        (The MCUboot project guarantees that incompatible changes to the image header will result in major version changes to the bootloader itself, and will be detectable in the persistent representation of the header.)

        Public Members

        uint32\_t mcuboot\_version
        :   The version of MCUboot the header is built for.

            The value 1 corresponds to MCUboot versions 1.x.y.

        struct [mcuboot\_img\_header\_v1](#c.mcuboot_img_header_v1) v1
        :   Header information for MCUboot version 1.

        union [mcuboot\_img\_header](#c.mcuboot_img_header).[anonymous] h
        :   The header information.

            It is only valid to access fields in the union member corresponding to the mcuboot\_version field above.

## Bootloaders

### MCUboot

Zephyr is directly compatible with the open source, cross-RTOS
[MCUboot boot loader](https://mcuboot.com/). It interfaces with MCUboot and is aware of the image
format required by it, so that Device Firmware Upgrade is available when MCUboot
is the boot loader used with Zephyr. The source code itself is hosted in the
[MCUboot GitHub Project](https://github.com/runtimeco/mcuboot) page.

In order to use MCUboot with Zephyr you need to take the following into account:

1. You will need to define the flash partitions required by MCUboot; see
   [Flash map](../storage/flash_map/flash_map.md#flash-map-api) for details.
2. You will have to specify your flash partition as the chosen code partition

```devicetree
/ {
   chosen {
      zephyr,code-partition = &slot0_partition;
   };
};
```

3. Your application’s `.conf` file needs to enable the
   [`CONFIG_BOOTLOADER_MCUBOOT`](../../kconfig.md#CONFIG_BOOTLOADER_MCUBOOT "CONFIG_BOOTLOADER_MCUBOOT") Kconfig option in order for Zephyr to
   be built in an MCUboot-compatible manner
4. You need to build and flash MCUboot itself on your device
5. You might need to take precautions to avoid mass erasing the flash and also
   to flash the Zephyr application image at the correct offset (right after the
   bootloader)

More detailed information regarding the use of MCUboot with Zephyr can be found
in the [MCUboot with Zephyr](https://docs.mcuboot.com/readme-zephyr) documentation page on the MCUboot website.
