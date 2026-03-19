---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smp__bt_8h.html
original_path: doxygen/html/smp__bt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_bt.h File Reference

Bluetooth transport for the mcumgr SMP protocol.
[More...](#details)

`#include <[zephyr/bluetooth/uuid.h](uuid_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](smp__bt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SMP\_BT\_SVC\_UUID\_VAL](#a35a151d8a3e9fb6f5e2e355c0c23f17c)   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84) |
|  | SMP service UUID value. |
| #define | [SMP\_BT\_SVC\_UUID](#afa04c341a4ed3b5a10c07d268266acc3)   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([SMP\_BT\_SVC\_UUID\_VAL](#a35a151d8a3e9fb6f5e2e355c0c23f17c)) |
|  | SMP service UUID. |
| #define | [SMP\_BT\_CHR\_UUID\_VAL](#a3f75f06a2f437008ecbe87474971a4ec)   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48) |
|  | SMP characteristic UUID value. |
| #define | [SMP\_BT\_CHR\_UUID](#aa42455942e31ddafc6174c5eca6f85ac)   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([SMP\_BT\_CHR\_UUID\_VAL](#a3f75f06a2f437008ecbe87474971a4ec)) |
|  | SMP characteristic UUID Used for both requests and responses. |

| Functions | |
| --- | --- |
| int | [smp\_bt\_register](#a9ceedfe6c84f194ff103356a4c30331f) (void) |
|  | Registers the SMP Bluetooth service. |
| int | [smp\_bt\_unregister](#ad19e1e1ba3ed59f13b5953bfda53ac15) (void) |
|  | Unregisters the SMP Bluetooth service. |
| int | [smp\_bt\_notify](#a8f52f0fda08b308dd7f1272b5ce5ba84) (struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Transmits an SMP command/response over the specified Bluetooth connection as a notification. |

## Detailed Description

Bluetooth transport for the mcumgr SMP protocol.

## Macro Definition Documentation

## [◆ ](#aa42455942e31ddafc6174c5eca6f85ac)SMP\_BT\_CHR\_UUID

| #define SMP\_BT\_CHR\_UUID   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([SMP\_BT\_CHR\_UUID\_VAL](#a3f75f06a2f437008ecbe87474971a4ec)) |
| --- |

SMP characteristic UUID Used for both requests and responses.

## [◆ ](#a3f75f06a2f437008ecbe87474971a4ec)SMP\_BT\_CHR\_UUID\_VAL

| #define SMP\_BT\_CHR\_UUID\_VAL   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48) |
| --- |

SMP characteristic UUID value.

## [◆ ](#afa04c341a4ed3b5a10c07d268266acc3)SMP\_BT\_SVC\_UUID

| #define SMP\_BT\_SVC\_UUID   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([SMP\_BT\_SVC\_UUID\_VAL](#a35a151d8a3e9fb6f5e2e355c0c23f17c)) |
| --- |

SMP service UUID.

## [◆ ](#a35a151d8a3e9fb6f5e2e355c0c23f17c)SMP\_BT\_SVC\_UUID\_VAL

| #define SMP\_BT\_SVC\_UUID\_VAL   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84) |
| --- |

SMP service UUID value.

## Function Documentation

## [◆ ](#a8f52f0fda08b308dd7f1272b5ce5ba84)smp\_bt\_notify()

| int smp\_bt\_notify | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

Transmits an SMP command/response over the specified Bluetooth connection as a notification.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | data | Pointer to SMP message. |
    | len | data length. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a9ceedfe6c84f194ff103356a4c30331f)smp\_bt\_register()

| int smp\_bt\_register | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Registers the SMP Bluetooth service.

Should only be called if the Bluetooth transport has been unregistered by calling [smp\_bt\_unregister()](#ad19e1e1ba3ed59f13b5953bfda53ac15).

Returns
:   0 on success; negative error code on failure.

## [◆ ](#ad19e1e1ba3ed59f13b5953bfda53ac15)smp\_bt\_unregister()

| int smp\_bt\_unregister | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Unregisters the SMP Bluetooth service.

Returns
:   0 on success; negative error code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_bt.h](smp__bt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
