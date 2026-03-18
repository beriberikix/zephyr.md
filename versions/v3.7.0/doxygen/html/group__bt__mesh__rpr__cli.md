---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__rpr__cli.html
original_path: doxygen/html/group__bt__mesh__rpr__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Remote Provisioning Client model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) |
|  | Scan status response. [More...](structbt__mesh__rpr__scan__status.md#details) |
| struct | [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) |
|  | Remote Provisioning Server scanning capabilities. [More...](structbt__mesh__rpr__caps.md#details) |
| struct | [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) |
|  | Remote Provisioning Client model instance. [More...](structbt__mesh__rpr__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY](#gafa00eb1bff764a4ab723bb978b459297)   0 |
|  | Special value for the `max_devs` parameter of [bt\_mesh\_rpr\_scan\_start](#gaf404922f2340442490f1ab29191f43e3). |
| #define | [BT\_MESH\_MODEL\_RPR\_CLI](#ga83d18bb8d1108db9f7e54cd2cad32a99)(\_cli) |
|  | Remote Provisioning Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_rpr\_scan\_caps\_get](#ga1cfef51b2d6389fb4b125cba4d21d739) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) \*caps) |
|  | Get scanning capabilities of Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_scan\_get](#ga03602b651a5bf1c88dac810e272ea142) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Get current scanning state of Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_scan\_start](#gaf404922f2340442490f1ab29191f43e3) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_devs, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Start scanning for unprovisioned devices. |
| int | [bt\_mesh\_rpr\_scan\_start\_ext](#ga934104e6ee33ba8c228fde4c68e752e1) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ad\_types, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_count) |
|  | Start extended scanning for unprovisioned devices. |
| int | [bt\_mesh\_rpr\_scan\_stop](#ga007aa9b409d1370ed04c45efccdf0408) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Stop any ongoing scanning on the Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_link\_get](#ga36de5bfca8ba9b03a99625fbc1734839) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp) |
|  | Get the current link status of the Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_link\_close](#gaa240b465a1ed5796b190d241e484d467) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp) |
|  | Close any open link on the Remote Provisioning Server. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_rpr\_cli\_timeout\_get](#ga93aca19586795801eefa04ffc4635533) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_rpr\_cli\_timeout\_set](#ga5ad2a2f6f0b9a3f27ef8174cd15b8818) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga83d18bb8d1108db9f7e54cd2cad32a99)BT\_MESH\_MODEL\_RPR\_CLI

| #define BT\_MESH\_MODEL\_RPR\_CLI | ( |  | *\_cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI](group__bt__mesh__access.md#gaf373eb4d8af5d6bee76a821bd4d5e48c), \

\_bt\_mesh\_rpr\_cli\_op, NULL, \_cli, &\_bt\_mesh\_rpr\_cli\_cb)

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI](group__bt__mesh__access.md#gaf373eb4d8af5d6bee76a821bd4d5e48c)

#define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI

Remote Provisioning Client.

**Definition** access.h:189

Remote Provisioning Client model composition data entry.

Parameters
:   | \_cli | Pointer to a [Remote Provisioning Client model](group__bt__mesh__rpr__cli.md "Remote Provisioning Client model") instance. |
    | --- | --- |

## [◆ ](#gafa00eb1bff764a4ab723bb978b459297)BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY

| #define BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY   0 |
| --- |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Special value for the `max_devs` parameter of [bt\_mesh\_rpr\_scan\_start](#gaf404922f2340442490f1ab29191f43e3).

Tells the Remote Provisioning Server not to put restrictions on the max number of devices reported to the Client.

## Function Documentation

## [◆ ](#ga93aca19586795801eefa04ffc4635533)bt\_mesh\_rpr\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_rpr\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)bt\_mesh\_rpr\_cli\_timeout\_set()

| void bt\_mesh\_rpr\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Set the transmission timeout value.

The transmission timeout controls the amount of time the Remote Provisioning Client models will wait for a response from the Server.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

## [◆ ](#gaa240b465a1ed5796b190d241e484d467)bt\_mesh\_rpr\_link\_close()

| int bt\_mesh\_rpr\_link\_close | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \* | *rsp* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Close any open link on the Remote Provisioning Server.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | rsp | Link status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga36de5bfca8ba9b03a99625fbc1734839)bt\_mesh\_rpr\_link\_get()

| int bt\_mesh\_rpr\_link\_get | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \* | *rsp* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Get the current link status of the Remote Provisioning Server.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | rsp | Link status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga1cfef51b2d6389fb4b125cba4d21d739)bt\_mesh\_rpr\_scan\_caps\_get()

| int bt\_mesh\_rpr\_scan\_caps\_get | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | struct [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) \* | *caps* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Get scanning capabilities of Remote Provisioning Server.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | caps | Capabilities response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga03602b651a5bf1c88dac810e272ea142)bt\_mesh\_rpr\_scan\_get()

| int bt\_mesh\_rpr\_scan\_get | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \* | *status* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Get current scanning state of Remote Provisioning Server.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | status | Scan status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gaf404922f2340442490f1ab29191f43e3)bt\_mesh\_rpr\_scan\_start()

| int bt\_mesh\_rpr\_scan\_start | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *timeout*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *max\_devs*, |
|  |  | struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \* | *status* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Start scanning for unprovisioned devices.

Tells the Remote Provisioning Server to start scanning for unprovisioned devices. The Server will report back the results through the [bt\_mesh\_rpr\_cli::scan\_report](structbt__mesh__rpr__cli.md#a32b3c63218b506d1bc5759640cb3fb81 "bt_mesh_rpr_cli::scan_report") callback.

Use the `uuid` parameter to scan for a specific device, or leave it as NULL to report all unprovisioned devices.

The Server will ignore duplicates, and report up to `max_devs` number of devices. Requesting a `max_devs` number that's higher than the Server's capability will result in an error.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | uuid | Device UUID to scan for, or NULL to report all devices. |
    | timeout | Scan timeout in seconds. Must be at least 1 second. |
    | max\_devs | Max number of devices to report, or 0 to report as many as possible. |
    | status | Scan status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga934104e6ee33ba8c228fde4c68e752e1)bt\_mesh\_rpr\_scan\_start\_ext()

| int bt\_mesh\_rpr\_scan\_start\_ext | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *timeout*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ad\_types*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ad\_count* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Start extended scanning for unprovisioned devices.

Extended scanning supplements regular unprovisioned scanning, by allowing the Server to report additional data for a specific device. The Remote Provisioning Server will use active scanning to request a scan response from the unprovisioned device, if supported. If no UUID is provided, the Server will report a scan on its own OOB information and advertising data.

Use the ad\_types array to specify which AD types to include in the scan report. Some AD types invoke special behavior:

- [BT\_DATA\_NAME\_COMPLETE](group__bt__gap__defines.md#gab94a7c5689d296acf47f976538056ab5 "BT_DATA_NAME_COMPLETE") Will report both the complete and the shortened name.
- [BT\_DATA\_URI](group__bt__gap__defines.md#ga3c6a5903cc4a46aaf0b30a0de0179403 "BT_DATA_URI") If the unprovisioned beacon contains a URI hash, the Server will extend the scanning to include packets other than the scan response, to look for URIs matching the URI hash. Only matching URIs will be reported.

The following AD types should not be used:

- [BT\_DATA\_NAME\_SHORTENED](group__bt__gap__defines.md#gafc509b33a8d2dd9124f6893eadbe1662 "BT_DATA_NAME_SHORTENED")
- [BT\_DATA\_UUID16\_SOME](group__bt__gap__defines.md#ga6c725bd3d31c159a4d046561dbca38ba "BT_DATA_UUID16_SOME")
- [BT\_DATA\_UUID32\_SOME](group__bt__gap__defines.md#ga2486a6748490ba57e442ca15223482ef "BT_DATA_UUID32_SOME")
- [BT\_DATA\_UUID128\_SOME](group__bt__gap__defines.md#ga5c4f7fc1b93c611e95f735330fba243b "BT_DATA_UUID128_SOME")

Additionally, each AD type should only occur once.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | uuid | Device UUID to start extended scanning for, or NULL to scan the remote server. |
    | timeout | Scan timeout in seconds. Valid values from [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN](group__bt__mesh__rpr.md#ga2b7e2636da150f5c5cb4e3bdee13c745 "BT_MESH_RPR_EXT_SCAN_TIME_MIN") to [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX](group__bt__mesh__rpr.md#ga2a5241b2e87fec227740dd4f2de3a68a "BT_MESH_RPR_EXT_SCAN_TIME_MAX"). Ignored if UUID is NULL. |
    | ad\_types | List of AD types to include in the scan report. Must contain 1 to CONFIG\_BT\_MESH\_RPR\_AD\_TYPES\_MAX entries. |
    | ad\_count | Number of AD types in `ad_types`. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga007aa9b409d1370ed04c45efccdf0408)bt\_mesh\_rpr\_scan\_stop()

| int bt\_mesh\_rpr\_scan\_stop | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \* | *status* ) |

`#include <[rpr_cli.h](rpr__cli_8h.md)>`

Stop any ongoing scanning on the Remote Provisioning Server.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | srv | Remote Provisioning Server. |
    | status | Scan status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
