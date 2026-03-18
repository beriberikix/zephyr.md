---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/retention/blinfo.html
original_path: services/retention/blinfo.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bootloader Information

The bootloader information (abbreviated to blinfo) subsystem is an extension of
the [Retention System](index.md#retention-api) which allows for reading shared data from a bootloader
and allowing applications to query it. It has an optional feature of organising
the information retrieved from the bootloader and storing it in the
[Settings](../settings/index.md#settings-api) with the `blinfo/` prefix.

## Devicetree setup

To use the bootloader information subsystem, a retention area needs to be
created which has a retained data section as its parent, generally non-init RAM
is used for this purpose. See the following example (examples in this guide are
based on the [nRF52840 DK](../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board and memory layout):

```devicetree
/ {
        sram@2003F000 {
                compatible = "zephyr,memory-region", "mmio-sram";
                reg = <0x2003F000 DT_SIZE_K(1)>;
                zephyr,memory-region = "RetainedMem";
                status = "okay";

                retainedmem {
                        compatible = "zephyr,retained-ram";
                        status = "okay";
                        #address-cells = <1>;
                        #size-cells = <1>;

                        boot_info0: boot_info@0 {
                                compatible = "zephyr,retention";
                                status = "okay";
                                reg = <0x0 0x100>;
                        };
                };
        };

        chosen {
                zephyr,bootloader-info = &boot_info0;
        };
};

/* Reduce SRAM0 usage by 1KB to account for non-init area */
&sram0 {
        reg = <0x20000000 DT_SIZE_K(255)>;
};
```

Note that this configuration needs to be applied on both the bootloader
(MCUboot) and application to be usable. It can be combined with other retention
system APIs such as the [Boot mode](index.md#boot-mode-api)

## MCUboot setup

Once the above devicetree configuration is applied, MCUboot needs to be
configured to store the shared data in this area, the following Kconfigs need
to be set for this:

- [`CONFIG_RETAINED_MEM`](../../kconfig.md#CONFIG_RETAINED_MEM "CONFIG_RETAINED_MEM") - Enables retained memory driver
- [`CONFIG_RETENTION`](../../kconfig.md#CONFIG_RETENTION "CONFIG_RETENTION") - Enables retention system
- `CONFIG_BOOT_SHARE_DATA` - Enables shared data
- `CONFIG_BOOT_SHARE_DATA_BOOTINFO` - Enables boot information
  shared data type
- `CONFIG_BOOT_SHARE_BACKEND_RETENTION` - Stores shared data
  using retention/blinfo subsystem

## Application setup

The application must enable the following base Kconfig options for the
bootloader information subsystem to function:

- [`CONFIG_RETAINED_MEM`](../../kconfig.md#CONFIG_RETAINED_MEM "CONFIG_RETAINED_MEM")
- [`CONFIG_RETENTION`](../../kconfig.md#CONFIG_RETENTION "CONFIG_RETENTION")
- [`CONFIG_RETENTION_BOOTLOADER_INFO`](../../kconfig.md#CONFIG_RETENTION_BOOTLOADER_INFO "CONFIG_RETENTION_BOOTLOADER_INFO")
- [`CONFIG_RETENTION_BOOTLOADER_INFO_TYPE_MCUBOOT`](../../kconfig.md#CONFIG_RETENTION_BOOTLOADER_INFO_TYPE_MCUBOOT "CONFIG_RETENTION_BOOTLOADER_INFO_TYPE_MCUBOOT")

The following include is needed to use the bootloader information subsystem:

```c
#include <zephyr/retention/blinfo.h>
```

By default, only the lookup function is provided: [`blinfo_lookup()`](#c.blinfo_lookup), the
application can call this to query the information from the bootloader. This
function is enabled by default with
[`CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION`](../../kconfig.md#CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION "CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION"), however,
applications can optionally choose to use the settings storage feature instead.
In this mode, the bootloader information can be queries by using settings keys,
the following Kconfig options need to be enabled for this mode:

- [`CONFIG_SETTINGS`](../../kconfig.md#CONFIG_SETTINGS "CONFIG_SETTINGS")
- [`CONFIG_SETTINGS_RUNTIME`](../../kconfig.md#CONFIG_SETTINGS_RUNTIME "CONFIG_SETTINGS_RUNTIME")
- [`CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_SETTINGS`](../../kconfig.md#CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_SETTINGS "CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_SETTINGS")

This allows the information to be queried via the
[`settings_runtime_get()`](../settings/index.md#c.settings_runtime_get "settings_runtime_get") function with the following keys:

- `blinfo/mode` The mode that MCUboot is configured for
  (`enum mcuboot_mode` value)
- `blinfo/signature_type` The signature type MCUboot is configured for
  (`enum mcuboot_signature_type` value)
- `blinfo/recovery` The recovery type enabled in MCUboot
  (`enum mcuboot_recovery_mode` value)
- `blinfo/running_slot` The running slot, useful for direct-XIP mode to know
  which slot to use for an update
- `blinfo/bootloader_version` Version of the bootloader
  (`struct image_version` object)
- `blinfo/max_application_size` Maximum size of an application (in bytes)
  that can be loaded

In addition to the previous include, the following includes are required for
this mode:

```c
#include <bootutil/boot_status.h>
#include <bootutil/image.h>
#include <zephyr/mcuboot_version.h>
#include <zephyr/settings/settings.h>
```

## API Reference

### Bootloader information API

*group* Bootloader info interface
:   Bootloader info interface.

    **Since**
    :   3.5

    **Version**
    :   0.1.0

    Functions

    int blinfo\_lookup(uint16\_t key, char \*val, int val\_len\_max)
    :   Returns bootinfo information.

        Parameters:
        :   - **key** – The information to return (for MCUboot: minor TLV).
            - **val** – Where the return information will be placed.
            - **val\_len\_max** – The maximum size of the provided buffer.

        Return values:
        :   - **>=** – 0 If successful (contains length of read value)
            - **-EOVERFLOW** – If the data is too large to fit the supplied buffer.
            - **-EIO** – If the requested key was not found.
            - **-errno** – Error code.
