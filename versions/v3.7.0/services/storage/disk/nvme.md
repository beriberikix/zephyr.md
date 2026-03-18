---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/storage/disk/nvme.html
original_path: services/storage/disk/nvme.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NVMe

NVMe is a standardized logical device interface on PCIe bus exposing storage devices.

NVMe controllers and disks are supported. Disks can be accessed via the [Disk Access API](access.md#disk-access-api) they expose
and thus be used through the [File System API](../../file_system/index.md#file-system-api).

## Driver design

The driver is sliced up in 3 main parts:

- NVMe controller: [drivers/disk/nvme/nvme\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_controller.c)
- NVMe commands: [drivers/disk/nvme/nvme\_cmd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_cmd.c)
- NVMe namespace: [drivers/disk/nvme/nvme\_namespace.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_namespace.c)

Where the NVMe controller is the root of the device driver. This is the one that will get device driver instances.
Note that this is only what DTS describes: the NVMe controller, and none of its namespaces (disks).
The NVMe command is the generic logic used to communicate with the controller and the namespaces it exposes.
Finally the NVMe namespace is the dedicated part to deal with an actual namespace which, in turn, enables applications
accessing each ones through the Disk Access API [drivers/disk/nvme/nvme\_disk.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_disk.c).

If a controller exposes more than 1 namespace (disk), it will be possible to raise the amount of built-in namespace support
by tweaking the configuration option CONFIG\_NVME\_MAX\_NAMESPACES (see below).

Each exposed disk, via it’s related disk\_info structure, will be distinguished by its name which is inherited from
it’s related namespace. As such, the disk name follows NVMe naming which is nvme<k>n<n> where k is the controller number
and n the namespame number. Most of the time, if only one NVMe disk is plugged into the system, one will see ‘nvme0n0’ as
an exposed disk.

## NVMe configuration

### DTS

Any board exposing an NVMe disk should provide a DTS overlay to enable its use within Zephyr

```devicetree
#include <zephyr/dt-bindings/pcie/pcie.h>
/ {
    pcie0 {
        nvme0: nvme0 {
            compatible = "nvme-controller";
            vendor-id = <VENDOR_ID>;
            device-id = <DEVICE_ID>;
            status = "okay";
        };
    };
};
```

Where VENDOR\_ID and DEVICE\_ID are the ones from the exposed NVMe controller.

### Options

- [`CONFIG_NVME`](../../../kconfig.md#CONFIG_NVME "CONFIG_NVME")

Note that NVME requires the target to support PCIe multi-vector MSI-X in order to function.

- [`CONFIG_NVME_MAX_NAMESPACES`](../../../kconfig.md#CONFIG_NVME_MAX_NAMESPACES "CONFIG_NVME_MAX_NAMESPACES")

## Important note for users

NVMe specifications mandate the data buffer to be placed in a dword (4 bytes) aligned address.
While this is not a problem for advanced OS managing virtual memory and dynamic allocations
below the user processes, this can become an issue in Zephyr as soon as buffer addresses
map directly to physical memory.

At this stage then, it is up to the user to make sure the buffer address being provided to
[`disk_access_read()`](access.md#c.disk_access_read "disk_access_read") and [`disk_access_write()`](access.md#c.disk_access_write "disk_access_write") are dword aligned.
