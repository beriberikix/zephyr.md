---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh.html
original_path: doxygen/html/group__bt__mesh.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Mesh.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Access layer](group__bt__mesh__access.md) |
|  | Access layer. |
|  | [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md) |
|  | [Bluetooth Mesh BLOB Transfer Server model API](group__bt__mesh__blob__srv.md) |
|  | [Bluetooth Mesh BLOB flash stream](group__bt__mesh__blob__io__flash.md) |
|  | [Bluetooth Mesh BLOB model API](group__bt__mesh__blob.md) |
|  | [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) |
|  | [Bluetooth Mesh On-Demand Private GATT Proxy Client](group__bt__mesh__od__priv__proxy__cli.md) |
|  | [Bluetooth Mesh On-Demand Private GATT Proxy Server](group__bt__mesh__od__priv__proxy__srv.md) |
|  | [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md) |
|  | [Bluetooth Mesh Private Beacon Server](group__bt__mesh__priv__beacon__srv.md) |
|  | [Bluetooth Mesh SAR Configuration Client Model](group__bt__mesh__sar__cfg__cli.md) |
|  | Bluetooth Mesh. |
|  | [Bluetooth Mesh SAR Configuration Server Model](group__bt__mesh__sar__cfg__srv.md) |
|  | Bluetooth Mesh. |
|  | [Bluetooth Mesh Solicitation PDU RPL Client](group__bt__mesh__sol__pdu__rpl__cli.md) |
|  | [Bluetooth Mesh Solicitation PDU RPL Server](group__bt__mesh__sol__pdu__rpl__srv.md) |
|  | [Configuration Client Model](group__bt__mesh__cfg__cli.md) |
|  | Configuration Client Model. |
|  | [Configuration Server Model](group__bt__mesh__cfg__srv.md) |
|  | Configuration Server Model. |
|  | [Firmware Distribution models](group__bt__mesh__dfd.md) |
|  | [Health Client Model](group__bt__mesh__health__cli.md) |
|  | Health Client Model. |
|  | [Health Server Model](group__bt__mesh__health__srv.md) |
|  | Health Server Model. |
|  | [Health faults](group__bt__mesh__health__faults.md) |
|  | List of specification defined Health fault values. |
|  | [Heartbeat](group__bt__mesh__heartbeat.md) |
|  | Heartbeat. |
|  | [Large Composition Data Client model](group__bt__mesh__large__comp__data__cli.md) |
|  | [Large Composition Data Server model](group__bt__mesh__large__comp__data__srv.md) |
|  | [Message](group__bt__mesh__msg.md) |
|  | Message. |
|  | [Opcodes Aggregator Client model](group__bt__mesh__op__agg__cli.md) |
|  | [Opcodes Aggregator Server model](group__bt__mesh__op__agg__srv.md) |
|  | [Provisioning](group__bt__mesh__prov.md) |
|  | Provisioning. |
|  | [Proxy](group__bt__mesh__proxy.md) |
|  | Proxy. |
|  | [Remote Provisioning Client model](group__bt__mesh__rpr__cli.md) |
|  | [Remote Provisioning models](group__bt__mesh__rpr.md) |
|  | [Remote provisioning server](group__bt__mesh__rpr__srv.md) |
|  | [Runtime Configuration](group__bt__mesh__cfg.md) |
|  | Runtime Configuration. |
|  | [SAR Configuration common header](group__bt__mesh__sar__cfg.md) |
|  | [Statistic](group__bt__mesh__stat.md) |
|  | Statistic. |

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md) |
|  | Low Power Node callback functions. [More...](structbt__mesh__lpn__cb.md#details) |
| struct | [bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md) |
|  | Friend Node callback functions. [More...](structbt__mesh__friend__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_NET\_PRIMARY](#ga0d6985da3c7be76732ee103458b77121)   0x000 |
|  | Primary Network Key index. |
| #define | [BT\_MESH\_FEAT\_RELAY](#gac588eefe83db94784a420ce063f02b55)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Relay feature. |
| #define | [BT\_MESH\_FEAT\_PROXY](#gaee648ce202316c56d4d588cb0ad5aeb4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | GATT Proxy feature. |
| #define | [BT\_MESH\_FEAT\_FRIEND](#ga8f27086b3bc3c4a6e14621836f9f8e80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Friend feature. |
| #define | [BT\_MESH\_FEAT\_LOW\_POWER](#gaad71a36c82b4e4d3fa334ecff5cc0171)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Low Power Node feature. |
| #define | [BT\_MESH\_FEAT\_SUPPORTED](#gac337fd8688d70e862974e010ad42a11b) |
|  | Supported heartbeat publication features. |
| #define | [BT\_MESH\_LPN\_CB\_DEFINE](#gac18d4ce09495a8ade098a6320bb26ec2)(\_name) |
|  | Register a callback structure for Friendship events. |
| #define | [BT\_MESH\_FRIEND\_CB\_DEFINE](#ga4f00fa03af86b39e24140eb09c51ca4c)(\_name) |
|  | Register a callback structure for Friendship events. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_init](#ga521def6f74467a9bd3f2757c6aabd405) (const struct [bt\_mesh\_prov](structbt__mesh__prov.md) \*prov, const struct [bt\_mesh\_comp](structbt__mesh__comp.md) \*comp) |
|  | Initialize Mesh support. |
| void | [bt\_mesh\_reset](#ga69fc65f4e07e6007388473f139e5d8d8) (void) |
|  | Reset the state of the local Mesh node. |
| int | [bt\_mesh\_suspend](#ga6c209dbad6881f1e9634d9b7d42f2c34) (void) |
|  | Suspend the Mesh network temporarily. |
| int | [bt\_mesh\_resume](#gaa9114ce8941e641dbb23828d7c0451fd) (void) |
|  | Resume a suspended Mesh network. |
| void | [bt\_mesh\_iv\_update\_test](#ga3fdc601bd036477f6bdf212667c6b0c9) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Toggle the IV Update test mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_iv\_update](#gacdf00423b03057fdf3a4207ee579eb74) (void) |
|  | Toggle the IV Update state. |
| int | [bt\_mesh\_lpn\_set](#ga7964f5b1abb7b12728e4ec224c95c849) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Toggle the Low Power feature of the local device. |
| int | [bt\_mesh\_lpn\_poll](#ga3fd66605950a55e299ca3a7cc697d453) (void) |
|  | Send out a Friend Poll message. |
| int | [bt\_mesh\_friend\_terminate](#ga28b9b1d7d732e300be8d4bbffdbad391) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
|  | Terminate Friendship. |
| void | [bt\_mesh\_rpl\_pending\_store](#ga62f9a72c4e9dc5e4f3f42bd4df4fe452) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Store pending RPL entry(ies) in the persistent storage. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [bt\_mesh\_va\_uuid\_get](#ga20fe74e33e6a35c452cd076c78aa4f05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*uuid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*retaddr) |
|  | Iterate stored Label UUIDs. |

## Detailed Description

Bluetooth Mesh.

## Macro Definition Documentation

## [◆ ](#ga8f27086b3bc3c4a6e14621836f9f8e80)BT\_MESH\_FEAT\_FRIEND

| #define BT\_MESH\_FEAT\_FRIEND   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[main.h](main_8h.md)>`

Friend feature.

## [◆ ](#gaad71a36c82b4e4d3fa334ecff5cc0171)BT\_MESH\_FEAT\_LOW\_POWER

| #define BT\_MESH\_FEAT\_LOW\_POWER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[main.h](main_8h.md)>`

Low Power Node feature.

## [◆ ](#gaee648ce202316c56d4d588cb0ad5aeb4)BT\_MESH\_FEAT\_PROXY

| #define BT\_MESH\_FEAT\_PROXY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[main.h](main_8h.md)>`

GATT Proxy feature.

## [◆ ](#gac588eefe83db94784a420ce063f02b55)BT\_MESH\_FEAT\_RELAY

| #define BT\_MESH\_FEAT\_RELAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[main.h](main_8h.md)>`

Relay feature.

## [◆ ](#gac337fd8688d70e862974e010ad42a11b)BT\_MESH\_FEAT\_SUPPORTED

| #define BT\_MESH\_FEAT\_SUPPORTED |
| --- |

`#include <[main.h](main_8h.md)>`

**Value:**

([BT\_MESH\_FEAT\_RELAY](#gac588eefe83db94784a420ce063f02b55) | \

[BT\_MESH\_FEAT\_PROXY](#gaee648ce202316c56d4d588cb0ad5aeb4) | \

[BT\_MESH\_FEAT\_FRIEND](#ga8f27086b3bc3c4a6e14621836f9f8e80) | \

[BT\_MESH\_FEAT\_LOW\_POWER](#gaad71a36c82b4e4d3fa334ecff5cc0171))

[BT\_MESH\_FEAT\_FRIEND](#ga8f27086b3bc3c4a6e14621836f9f8e80)

#define BT\_MESH\_FEAT\_FRIEND

Friend feature.

**Definition** main.h:567

[BT\_MESH\_FEAT\_LOW\_POWER](#gaad71a36c82b4e4d3fa334ecff5cc0171)

#define BT\_MESH\_FEAT\_LOW\_POWER

Low Power Node feature.

**Definition** main.h:569

[BT\_MESH\_FEAT\_RELAY](#gac588eefe83db94784a420ce063f02b55)

#define BT\_MESH\_FEAT\_RELAY

Relay feature.

**Definition** main.h:563

[BT\_MESH\_FEAT\_PROXY](#gaee648ce202316c56d4d588cb0ad5aeb4)

#define BT\_MESH\_FEAT\_PROXY

GATT Proxy feature.

**Definition** main.h:565

Supported heartbeat publication features.

## [◆ ](#ga4f00fa03af86b39e24140eb09c51ca4c)BT\_MESH\_FRIEND\_CB\_DEFINE

| #define BT\_MESH\_FRIEND\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md), \

\_CONCAT(bt\_mesh\_friend\_cb\_, \

\_name))

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md)

Friend Node callback functions.

**Definition** main.h:721

Register a callback structure for Friendship events.

Registers a callback structure that will be called whenever Friendship gets established or terminated.

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## [◆ ](#gac18d4ce09495a8ade098a6320bb26ec2)BT\_MESH\_LPN\_CB\_DEFINE

| #define BT\_MESH\_LPN\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md), \

\_CONCAT(bt\_mesh\_lpn\_cb\_, \

\_name))

[bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md)

Low Power Node callback functions.

**Definition** main.h:670

Register a callback structure for Friendship events.

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## [◆ ](#ga0d6985da3c7be76732ee103458b77121)BT\_MESH\_NET\_PRIMARY

| #define BT\_MESH\_NET\_PRIMARY   0x000 |
| --- |

`#include <[main.h](main_8h.md)>`

Primary Network Key index.

## Function Documentation

## [◆ ](#ga28b9b1d7d732e300be8d4bbffdbad391)bt\_mesh\_friend\_terminate()

| int bt\_mesh\_friend\_terminate | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *lpn\_addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Terminate Friendship.

Terminated Friendship for given LPN.

Parameters
:   | lpn\_addr | Low Power Node address. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga521def6f74467a9bd3f2757c6aabd405)bt\_mesh\_init()

| int bt\_mesh\_init | ( | const struct [bt\_mesh\_prov](structbt__mesh__prov.md) \* | *prov*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_comp](structbt__mesh__comp.md) \* | *comp* ) |

`#include <[main.h](main_8h.md)>`

Initialize Mesh support.

After calling this API, the node will not automatically advertise as unprovisioned, rather the [bt\_mesh\_prov\_enable()](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9 "Enable specific provisioning bearers.") API needs to be called to enable unprovisioned advertising on one or more provisioning bearers.

Parameters
:   | prov | Node provisioning information. |
    | --- | --- |
    | comp | Node Composition. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gacdf00423b03057fdf3a4207ee579eb74)bt\_mesh\_iv\_update()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_iv\_update | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Toggle the IV Update state.

This API is only available if the IV Update test mode has been enabled in Kconfig. It is needed for passing most of the IV Update qualification test cases.

Returns
:   true if IV Update In Progress state was entered, false otherwise.

## [◆ ](#ga3fdc601bd036477f6bdf212667c6b0c9)bt\_mesh\_iv\_update\_test()

| void bt\_mesh\_iv\_update\_test | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Toggle the IV Update test mode.

This API is only available if the IV Update test mode has been enabled in Kconfig. It is needed for passing most of the IV Update qualification test cases.

Parameters
:   | enable | true to enable IV Update test mode, false to disable it. |
    | --- | --- |

## [◆ ](#ga3fd66605950a55e299ca3a7cc697d453)bt\_mesh\_lpn\_poll()

| int bt\_mesh\_lpn\_poll | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Send out a Friend Poll message.

Send a Friend Poll message to the Friend of this node. If there is no established Friendship the function will return an error.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga7964f5b1abb7b12728e4ec224c95c849)bt\_mesh\_lpn\_set()

| int bt\_mesh\_lpn\_set | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Toggle the Low Power feature of the local device.

Enables or disables the Low Power feature of the local device. This is exposed as a run-time feature, since the device might want to change this e.g. based on being plugged into a stable power source or running from a battery power source.

Parameters
:   | enable | true to enable LPN functionality, false to disable it. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga69fc65f4e07e6007388473f139e5d8d8)bt\_mesh\_reset()

| void bt\_mesh\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Reset the state of the local Mesh node.

Resets the state of the node, which means that it needs to be reprovisioned to become an active node in a Mesh network again.

After calling this API, the node will not automatically advertise as unprovisioned, rather the [bt\_mesh\_prov\_enable()](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9 "Enable specific provisioning bearers.") API needs to be called to enable unprovisioned advertising on one or more provisioning bearers.

## [◆ ](#gaa9114ce8941e641dbb23828d7c0451fd)bt\_mesh\_resume()

| int bt\_mesh\_resume | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Resume a suspended Mesh network.

This API resumes the local node, after it has been suspended using the [bt\_mesh\_suspend()](#ga6c209dbad6881f1e9634d9b7d42f2c34) API.

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga62f9a72c4e9dc5e4f3f42bd4df4fe452)bt\_mesh\_rpl\_pending\_store()

| void bt\_mesh\_rpl\_pending\_store | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Store pending RPL entry(ies) in the persistent storage.

This API allows the user to store pending RPL entry(ies) in the persistent storage without waiting for the timeout.

Note
:   When flash is used as the persistent storage, calling this API too frequently may wear it out.

Parameters
:   | addr | Address of the node which RPL entry needs to be stored or [BT\_MESH\_ADDR\_ALL\_NODES](group__bt__mesh__access.md#ga27aafd100b6ccc1de060a75370184620 "BT_MESH_ADDR_ALL_NODES") to store all pending RPL entries. |
    | --- | --- |

## [◆ ](#ga6c209dbad6881f1e9634d9b7d42f2c34)bt\_mesh\_suspend()

| int bt\_mesh\_suspend | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Suspend the Mesh network temporarily.

This API can be used for power saving purposes, but the user should be aware that leaving the local node suspended for a long period of time may cause it to become permanently disconnected from the Mesh network. If at all possible, the Friendship feature should be used instead, to make the node into a Low Power Node.

Note
:   Should not be called from work queue due to undefined behavior. This is due to [k\_work\_flush\_delayable()](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f "Flush delayable work.") being used in disabling of the extended advertising.

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga20fe74e33e6a35c452cd076c78aa4f05)bt\_mesh\_va\_uuid\_get()

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* bt\_mesh\_va\_uuid\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *uuid*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *retaddr* ) |

`#include <[main.h](main_8h.md)>`

Iterate stored Label UUIDs.

When `addr` is [BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c "BT_MESH_ADDR_UNASSIGNED"), this function iterates over all available addresses starting with `uuid`. In this case, use `retaddr` to get virtual address representation of the returned Label UUID. When `addr` is a virtual address, this function returns next Label UUID corresponding to the `addr`. When `uuid` is NULL, this function returns the first available UUID. If `uuid` is previously returned uuid, this function returns following uuid.

Parameters
:   | addr | Virtual address to search for, or [BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c "BT_MESH_ADDR_UNASSIGNED"). |
    | --- | --- |
    | uuid | Pointer to the previously returned Label UUID or NULL. |
    | retaddr | Pointer to a memory where virtual address representation of the returning UUID is to be stored to. |

Returns
:   Pointer to Label UUID, or NULL if no more entries found.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
