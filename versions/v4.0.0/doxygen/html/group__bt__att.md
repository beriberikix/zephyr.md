---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__att.html
original_path: doxygen/html/group__bt__att.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Attribute Protocol (ATT)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Attribute Protocol (ATT).
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_ATT\_ERR\_SUCCESS](#ga0032756d54c08d37c101769be8ef2070)   0x00 |
|  | The ATT operation was successful. |
| #define | [BT\_ATT\_ERR\_INVALID\_HANDLE](#gab8d9a6870360f0e5dd7290895202879f)   0x01 |
|  | The attribute handle given was not valid on the server. |
| #define | [BT\_ATT\_ERR\_READ\_NOT\_PERMITTED](#gac26ed224b7f8fb7717b40fe3a545be7e)   0x02 |
|  | The attribute cannot be read. |
| #define | [BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED](#ga2378ff92f5afaff1e4392b1dc2e7326c)   0x03 |
|  | The attribute cannot be written. |
| #define | [BT\_ATT\_ERR\_INVALID\_PDU](#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)   0x04 |
|  | The attribute PDU was invalid. |
| #define | [BT\_ATT\_ERR\_AUTHENTICATION](#ga269e711af78a7a30a770b3d7db210c8a)   0x05 |
|  | The attribute requires authentication before it can be read or written. |
| #define | [BT\_ATT\_ERR\_NOT\_SUPPORTED](#gafcfa214f6f5b600647886f27cebecb49)   0x06 |
|  | The ATT Server does not support the request received from the client. |
| #define | [BT\_ATT\_ERR\_INVALID\_OFFSET](#ga997d113b71af6b4019c26ca3893f3dbb)   0x07 |
|  | Offset specified was past the end of the attribute. |
| #define | [BT\_ATT\_ERR\_AUTHORIZATION](#ga30b28071d7057c2c68b10da34ba32faf)   0x08 |
|  | The attribute requires authorization before it can be read or written. |
| #define | [BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL](#gaa135b2315173e7852afe4e1624169ce2)   0x09 |
|  | Too many prepare writes have been queued. |
| #define | [BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND](#ga5dfcd07918dc665bf600a25608b0736d)   0x0a |
|  | No attribute found within the given attribute handle range. |
| #define | [BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG](#ga240561711499f11b267d2e5ed8fc99f5)   0x0b |
|  | The attribute cannot be read using the ATT\_READ\_BLOB\_REQ PDU. |
| #define | [BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE](#ga2ed58d79dfbd701a97377b171f1b0793)   0x0c |
|  | The Encryption Key Size used for encrypting this link is too short. |
| #define | [BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN](#ga21207d5beb27fe50856f001bd18e1efa)   0x0d |
|  | The attribute value length is invalid for the operation. |
| #define | [BT\_ATT\_ERR\_UNLIKELY](#ga992baa1f0d763a00f314bdcf59965bdd)   0x0e |
|  | The attribute request that was requested has encountered an error that was unlikely. |
| #define | [BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION](#ga8a5235e39b05fa85b5b4f4bfb449683b)   0x0f |
|  | The attribute requires encryption before it can be read or written. |
| #define | [BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE](#ga0611fc39d9d09ea4f0e556b4910f09ed)   0x10 |
|  | The attribute type is not a supported grouping attribute. |
| #define | [BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES](#gaf4a81bc81cad14bf91463d4376a3a868)   0x11 |
|  | Insufficient Resources to complete the request. |
| #define | [BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC](#ga2b9a58bf48f1b76e743cb7fef3aed3a8)   0x12 |
|  | The server requests the client to rediscover the database. |
| #define | [BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED](#ga52ffe5ff2eb092bcdc2ebb05684030d7)   0x13 |
|  | The attribute parameter value was not allowed. |
| #define | [BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED](#ga8363770d0832f3df8fb1d0a22bc3551e)   0xfc |
|  | Write Request Rejected. |
| #define | [BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF](#ga8f623146d7fda4b71514277cfbcd4b21)   0xfd |
|  | Client Characteristic Configuration Descriptor Improperly Configured. |
| #define | [BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS](#gaf9e46c363487c61dbff50790993107f7)   0xfe |
|  | Procedure Already in Progress. |
| #define | [BT\_ATT\_ERR\_OUT\_OF\_RANGE](#gad49773d5e7a39f49c5a06bbaa4f8c365)   0xff |
|  | Out of Range. |
| #define | [BT\_ATT\_MAX\_ATTRIBUTE\_LEN](#ga3c4df4336916e082115d43f9716acb36)   512 |
| #define | [BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE](#gad0aa088f621b8965013c3ced27480df7)   0x0001 |
| #define | [BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE](#ga1b3dc5fedec8d8632d3650405d1ff988)   0xffff |

| Enumerations | |
| --- | --- |
| enum | [bt\_att\_chan\_opt](#gac593a27ecf029f33f50f990b2947562c) { [BT\_ATT\_CHAN\_OPT\_NONE](#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739) = 0x0 , [BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) = BIT(0) , [BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) = BIT(1) } |
|  | ATT channel option bit field values. [More...](#gac593a27ecf029f33f50f990b2947562c) |

| Functions | |
| --- | --- |
| static const char \* | [bt\_att\_err\_to\_str](#gad2305f28744276d97aefd26bdb79023c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) att\_err) |
|  | Converts a ATT error to string. |
| int | [bt\_eatt\_connect](#ga748194cbbd54a3336d3c788f08e3de99) (struct bt\_conn \*conn, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Connect Enhanced ATT channels. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_eatt\_count](#ga3cabc05e8f5c0418ff02dd7122b7565e) (struct bt\_conn \*conn) |
|  | Get number of EATT channels connected. |

## Detailed Description

Attribute Protocol (ATT).

## Macro Definition Documentation

## [◆ ](#ga5dfcd07918dc665bf600a25608b0736d)BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND

| #define BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND   0x0a |
| --- |

`#include <[att.h](att_8h.md)>`

No attribute found within the given attribute handle range.

## [◆ ](#ga240561711499f11b267d2e5ed8fc99f5)BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG

| #define BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG   0x0b |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute cannot be read using the ATT\_READ\_BLOB\_REQ PDU.

## [◆ ](#ga269e711af78a7a30a770b3d7db210c8a)BT\_ATT\_ERR\_AUTHENTICATION

| #define BT\_ATT\_ERR\_AUTHENTICATION   0x05 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute requires authentication before it can be read or written.

## [◆ ](#ga30b28071d7057c2c68b10da34ba32faf)BT\_ATT\_ERR\_AUTHORIZATION

| #define BT\_ATT\_ERR\_AUTHORIZATION   0x08 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute requires authorization before it can be read or written.

## [◆ ](#ga8f623146d7fda4b71514277cfbcd4b21)BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF

| #define BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF   0xfd |
| --- |

`#include <[att.h](att_8h.md)>`

Client Characteristic Configuration Descriptor Improperly Configured.

## [◆ ](#ga2b9a58bf48f1b76e743cb7fef3aed3a8)BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC

| #define BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC   0x12 |
| --- |

`#include <[att.h](att_8h.md)>`

The server requests the client to rediscover the database.

## [◆ ](#ga2ed58d79dfbd701a97377b171f1b0793)BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE

| #define BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE   0x0c |
| --- |

`#include <[att.h](att_8h.md)>`

The Encryption Key Size used for encrypting this link is too short.

## [◆ ](#ga8a5235e39b05fa85b5b4f4bfb449683b)BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION

| #define BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION   0x0f |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute requires encryption before it can be read or written.

## [◆ ](#gaf4a81bc81cad14bf91463d4376a3a868)BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES

| #define BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES   0x11 |
| --- |

`#include <[att.h](att_8h.md)>`

Insufficient Resources to complete the request.

## [◆ ](#ga21207d5beb27fe50856f001bd18e1efa)BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN

| #define BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN   0x0d |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute value length is invalid for the operation.

## [◆ ](#gab8d9a6870360f0e5dd7290895202879f)BT\_ATT\_ERR\_INVALID\_HANDLE

| #define BT\_ATT\_ERR\_INVALID\_HANDLE   0x01 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute handle given was not valid on the server.

## [◆ ](#ga997d113b71af6b4019c26ca3893f3dbb)BT\_ATT\_ERR\_INVALID\_OFFSET

| #define BT\_ATT\_ERR\_INVALID\_OFFSET   0x07 |
| --- |

`#include <[att.h](att_8h.md)>`

Offset specified was past the end of the attribute.

## [◆ ](#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)BT\_ATT\_ERR\_INVALID\_PDU

| #define BT\_ATT\_ERR\_INVALID\_PDU   0x04 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute PDU was invalid.

## [◆ ](#gafcfa214f6f5b600647886f27cebecb49)BT\_ATT\_ERR\_NOT\_SUPPORTED

| #define BT\_ATT\_ERR\_NOT\_SUPPORTED   0x06 |
| --- |

`#include <[att.h](att_8h.md)>`

The ATT Server does not support the request received from the client.

## [◆ ](#gad49773d5e7a39f49c5a06bbaa4f8c365)BT\_ATT\_ERR\_OUT\_OF\_RANGE

| #define BT\_ATT\_ERR\_OUT\_OF\_RANGE   0xff |
| --- |

`#include <[att.h](att_8h.md)>`

Out of Range.

## [◆ ](#gaa135b2315173e7852afe4e1624169ce2)BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL

| #define BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL   0x09 |
| --- |

`#include <[att.h](att_8h.md)>`

Too many prepare writes have been queued.

## [◆ ](#gaf9e46c363487c61dbff50790993107f7)BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS

| #define BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS   0xfe |
| --- |

`#include <[att.h](att_8h.md)>`

Procedure Already in Progress.

## [◆ ](#gac26ed224b7f8fb7717b40fe3a545be7e)BT\_ATT\_ERR\_READ\_NOT\_PERMITTED

| #define BT\_ATT\_ERR\_READ\_NOT\_PERMITTED   0x02 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute cannot be read.

## [◆ ](#ga0032756d54c08d37c101769be8ef2070)BT\_ATT\_ERR\_SUCCESS

| #define BT\_ATT\_ERR\_SUCCESS   0x00 |
| --- |

`#include <[att.h](att_8h.md)>`

The ATT operation was successful.

## [◆ ](#ga992baa1f0d763a00f314bdcf59965bdd)BT\_ATT\_ERR\_UNLIKELY

| #define BT\_ATT\_ERR\_UNLIKELY   0x0e |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute request that was requested has encountered an error that was unlikely.

The attribute request could therefore not be completed as requested

## [◆ ](#ga0611fc39d9d09ea4f0e556b4910f09ed)BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE

| #define BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE   0x10 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute type is not a supported grouping attribute.

The attribute type is not a supported grouping attribute as defined by a higher layer specification.

## [◆ ](#ga52ffe5ff2eb092bcdc2ebb05684030d7)BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED

| #define BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED   0x13 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute parameter value was not allowed.

## [◆ ](#ga2378ff92f5afaff1e4392b1dc2e7326c)BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED

| #define BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED   0x03 |
| --- |

`#include <[att.h](att_8h.md)>`

The attribute cannot be written.

## [◆ ](#ga8363770d0832f3df8fb1d0a22bc3551e)BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED

| #define BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED   0xfc |
| --- |

`#include <[att.h](att_8h.md)>`

Write Request Rejected.

## [◆ ](#gad0aa088f621b8965013c3ced27480df7)BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE

| #define BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE   0x0001 |
| --- |

`#include <[att.h](att_8h.md)>`

## [◆ ](#ga1b3dc5fedec8d8632d3650405d1ff988)BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE

| #define BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE   0xffff |
| --- |

`#include <[att.h](att_8h.md)>`

## [◆ ](#ga3c4df4336916e082115d43f9716acb36)BT\_ATT\_MAX\_ATTRIBUTE\_LEN

| #define BT\_ATT\_MAX\_ATTRIBUTE\_LEN   512 |
| --- |

`#include <[att.h](att_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gac593a27ecf029f33f50f990b2947562c)bt\_att\_chan\_opt

| enum [bt\_att\_chan\_opt](#gac593a27ecf029f33f50f990b2947562c) |
| --- |

`#include <[att.h](att_8h.md)>`

ATT channel option bit field values.

Note
:   [BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) and [BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) are mutually exclusive and both bits may not be set.

| Enumerator | |
| --- | --- |
| BT\_ATT\_CHAN\_OPT\_NONE | Both Enhanced and Unenhanced channels can be used. |
| BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY | Only Unenhanced channels will be used. |
| BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY | Only Enhanced channels will be used. |

## Function Documentation

## [◆ ](#gad2305f28744276d97aefd26bdb79023c)bt\_att\_err\_to\_str()

| | const char \* bt\_att\_err\_to\_str | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *att\_err* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[att.h](att_8h.md)>`

Converts a ATT error to string.

The error codes are described in the Bluetooth Core specification, Vol 3, Part F, Section 3.4.1.1 and in The Supplement to the Bluetooth Core Specification (CSS), v11, Part B, Section 1.2.

The ATT and GATT documentation found in Vol 4, Part F and Part G describe when the different error codes are used.

See also the defined BT\_ATT\_ERR\_\* macros.

Returns
:   The string representation of the ATT error code. If

    ```
    CONFIG_BT_ATT_ERR_TO_STR
    ```

    is not enabled, this just returns the empty string

## [◆ ](#ga748194cbbd54a3336d3c788f08e3de99)bt\_eatt\_connect()

| int bt\_eatt\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_channels* ) |

`#include <[att.h](att_8h.md)>`

Connect Enhanced ATT channels.

Sends a series of Credit Based Connection Requests to connect `num_channels` Enhanced ATT channels. The peer may have limited resources and fewer channels may be created.

Parameters
:   | conn | The connection to send the request on |
    | --- | --- |
    | num\_channels | The number of Enhanced ATT beares to request. Must be in the range 1 -  ``` CONFIG_BT_EATT_MAX ```  , inclusive. |

Returns
:   0 in case of success or negative value in case of error.

Return values
:   | -EINVAL | if `num_channels` is not in the allowed range or `conn` is NULL. |
    | --- | --- |
    | -ENOMEM | if less than `num_channels` are allocated. |
    | 0 | in case of success |

## [◆ ](#ga3cabc05e8f5c0418ff02dd7122b7565e)bt\_eatt\_count()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_eatt\_count | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[att.h](att_8h.md)>`

Get number of EATT channels connected.

Parameters
:   | conn | The connection to get the number of EATT channels for. |
    | --- | --- |

Returns
:   The number of EATT channels connected. Returns 0 if `conn` is NULL or not connected.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
