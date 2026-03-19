---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/device_mgmt/ota.html
original_path: services/device_mgmt/ota.html
---

# Over-the-Air Update

## Overview

Over-the-Air (OTA) Update is a method for delivering firmware updates to remote
devices using a network connection. Although the name implies a wireless
connection, updates received over a wired connection (such as Ethernet)
are still commonly referred to as OTA updates. This approach requires server
infrastructure to host the firmware binary and implement a method of signaling
when an update is available. Security is a concern with OTA updates; firmware
binaries should be cryptographically signed and verified before upgrading.

The [Device Firmware Upgrade](dfu.md#dfu) section discusses upgrading Zephyr firmware using MCUboot. The
same method can be used as part of OTA. The binary is first downloaded
into an unoccupied code partition, usually named `slot1_partition`, then
upgraded using the [MCUboot](dfu.md#mcuboot) process.

## Examples of OTA

### Golioth

[Golioth](https://golioth.io/) is an IoT management platform that includes OTA updates. Devices are
configured to observe your available firmware revisions on the Golioth Cloud.
When a new version is available, the device downloads and flashes the binary. In
this implementation, the connection between cloud and device is secured using
TLS/DTLS, and the signed firmware binary is confirmed by MCUboot before the
upgrade occurs.

1. A working sample can be found on the [Golioth Firmware SDK repository](https://github.com/golioth/golioth-firmware-sdk/tree/main/examples/zephyr/fw_update)
2. The [Golioth OTA documentation](https://docs.golioth.io/device-management/ota) includes complete information about the
   versioning process

### Eclipse hawkBit™

[Eclipse hawkBit](https://www.eclipse.org/hawkbit/)™ is an update server framework that uses polling on a
REST api to detect firmware updates. When a new update is detected, the binary
is downloaded and installed. MCUboot can be used to verify the signature before
upgrading the firmware.

There is a [Eclipse hawkBit Direct Device Integration API](../../samples/subsys/mgmt/hawkbit/README.md#hawkbit-api "Update a device using Eclipse hawkBit DDI API.") sample included in the
Zephyr [Management](../../samples/subsys/mgmt/mgmt.md#mgmt) section.

### UpdateHub

[UpdateHub](https://updatehub.io/) is a platform for remotely updating embedded devices. Updates can
be manually triggered or monitored via polling. When a new update is detected,
the binary is downloaded and installed. MCUboot can be used to verify the
signature before upgrading the firmware.

There is an [UpdateHub embedded Firmware Over-The-Air (FOTA) update](../../samples/subsys/mgmt/updatehub/README.md#updatehub-fota "Perform Firmware Over-The-Air (FOTA) updates using UpdateHub.") sample included in the Zephyr
[Management](../../samples/subsys/mgmt/mgmt.md#mgmt) section.

### SMP Server

A Simple Management Protocol (SMP) server can be used to update firmware via
Bluetooth Low Energy (BLE) or UDP. [MCUmgr](mcumgr.md#mcu-mgr) is used to send a signed
firmware binary to the remote device where it is verified by MCUboot before the
upgrade occurs.

There is an [SMP server](../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") sample included in the Zephyr
[Management](../../samples/subsys/mgmt/mgmt.md#mgmt) section.

### Lightweight M2M (LWM2M)

The [Lightweight M2M (LWM2M)](../../connectivity/networking/api/lwm2m.md#lwm2m-interface) protocol includes support for firmware update via
[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](../../kconfig.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT "CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT"). Devices securely
connect to an LwM2M server using DTLS. A [LwM2M client](../../samples/net/lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server.") sample is
available but it does not demonstrate the firmware update feature.
