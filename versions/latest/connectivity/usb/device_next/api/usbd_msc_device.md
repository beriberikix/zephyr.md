---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/api/usbd_msc_device.html
original_path: connectivity/usb/device_next/api/usbd_msc_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB Mass Storage Class device API

USB Mass Storage Class device API defined in
[include/zephyr/usb/class/usbd\_msc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_msc.h).

## API Reference

Related code samples

[USB Mass Storage](../../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
:   Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.

*group* USB Mass Storage Class device API
:   USB Mass Storage Class device API.

    Defines

    USBD\_DEFINE\_MSC\_LUN(disk\_name, t10\_vendor, t10\_product, t10\_revision)
    :   Define USB Mass Storage Class logical unit.

        Use this macro to create Logical Unit mapping in USB MSC for selected disk. Up to `CONFIG_USBD_MSC_LUNS_PER_INSTANCE` disks can be registered on single USB MSC instance. Currently only one USB MSC instance is supported.

        Parameters:
        :   - **disk\_name** – Disk name as used in [Disk Access Interface](../../../../services/storage/disk/access.md#group__disk__access__interface)
            - **t10\_vendor** – T10 Vendor Indetification
            - **t10\_product** – T10 Product Identification
            - **t10\_revision** – T10 Product Revision Level
