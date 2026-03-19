---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/att_8h.html
original_path: doxygen/html/att_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

att.h File Reference

Attribute Protocol handling.
[More...](#details)

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`

[Go to the source code of this file.](att_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_ATT\_ERR\_SUCCESS](group__bt__att.md#ga0032756d54c08d37c101769be8ef2070)   0x00 |
|  | The ATT operation was successful. |
| #define | [BT\_ATT\_ERR\_INVALID\_HANDLE](group__bt__att.md#gab8d9a6870360f0e5dd7290895202879f)   0x01 |
|  | The attribute handle given was not valid on the server. |
| #define | [BT\_ATT\_ERR\_READ\_NOT\_PERMITTED](group__bt__att.md#gac26ed224b7f8fb7717b40fe3a545be7e)   0x02 |
|  | The attribute cannot be read. |
| #define | [BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED](group__bt__att.md#ga2378ff92f5afaff1e4392b1dc2e7326c)   0x03 |
|  | The attribute cannot be written. |
| #define | [BT\_ATT\_ERR\_INVALID\_PDU](group__bt__att.md#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)   0x04 |
|  | The attribute PDU was invalid. |
| #define | [BT\_ATT\_ERR\_AUTHENTICATION](group__bt__att.md#ga269e711af78a7a30a770b3d7db210c8a)   0x05 |
|  | The attribute requires authentication before it can be read or written. |
| #define | [BT\_ATT\_ERR\_NOT\_SUPPORTED](group__bt__att.md#gafcfa214f6f5b600647886f27cebecb49)   0x06 |
|  | The ATT Server does not support the request received from the client. |
| #define | [BT\_ATT\_ERR\_INVALID\_OFFSET](group__bt__att.md#ga997d113b71af6b4019c26ca3893f3dbb)   0x07 |
|  | Offset specified was past the end of the attribute. |
| #define | [BT\_ATT\_ERR\_AUTHORIZATION](group__bt__att.md#ga30b28071d7057c2c68b10da34ba32faf)   0x08 |
|  | The attribute requires authorization before it can be read or written. |
| #define | [BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL](group__bt__att.md#gaa135b2315173e7852afe4e1624169ce2)   0x09 |
|  | Too many prepare writes have been queued. |
| #define | [BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND](group__bt__att.md#ga5dfcd07918dc665bf600a25608b0736d)   0x0a |
|  | No attribute found within the given attribute handle range. |
| #define | [BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG](group__bt__att.md#ga240561711499f11b267d2e5ed8fc99f5)   0x0b |
|  | The attribute cannot be read using the ATT\_READ\_BLOB\_REQ PDU. |
| #define | [BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE](group__bt__att.md#ga2ed58d79dfbd701a97377b171f1b0793)   0x0c |
|  | The Encryption Key Size used for encrypting this link is too short. |
| #define | [BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN](group__bt__att.md#ga21207d5beb27fe50856f001bd18e1efa)   0x0d |
|  | The attribute value length is invalid for the operation. |
| #define | [BT\_ATT\_ERR\_UNLIKELY](group__bt__att.md#ga992baa1f0d763a00f314bdcf59965bdd)   0x0e |
|  | The attribute request that was requested has encountered an error that was unlikely. |
| #define | [BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION](group__bt__att.md#ga8a5235e39b05fa85b5b4f4bfb449683b)   0x0f |
|  | The attribute requires encryption before it can be read or written. |
| #define | [BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE](group__bt__att.md#ga0611fc39d9d09ea4f0e556b4910f09ed)   0x10 |
|  | The attribute type is not a supported grouping attribute. |
| #define | [BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES](group__bt__att.md#gaf4a81bc81cad14bf91463d4376a3a868)   0x11 |
|  | Insufficient Resources to complete the request. |
| #define | [BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC](group__bt__att.md#ga2b9a58bf48f1b76e743cb7fef3aed3a8)   0x12 |
|  | The server requests the client to rediscover the database. |
| #define | [BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED](group__bt__att.md#ga52ffe5ff2eb092bcdc2ebb05684030d7)   0x13 |
|  | The attribute parameter value was not allowed. |
| #define | [BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED](group__bt__att.md#ga8363770d0832f3df8fb1d0a22bc3551e)   0xfc |
|  | Write Request Rejected. |
| #define | [BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF](group__bt__att.md#ga8f623146d7fda4b71514277cfbcd4b21)   0xfd |
|  | Client Characteristic Configuration Descriptor Improperly Configured. |
| #define | [BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS](group__bt__att.md#gaf9e46c363487c61dbff50790993107f7)   0xfe |
|  | Procedure Already in Progress. |
| #define | [BT\_ATT\_ERR\_OUT\_OF\_RANGE](group__bt__att.md#gad49773d5e7a39f49c5a06bbaa4f8c365)   0xff |
|  | Out of Range. |
| #define | [BT\_ATT\_MAX\_ATTRIBUTE\_LEN](group__bt__att.md#ga3c4df4336916e082115d43f9716acb36)   512 |
| #define | [BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE](group__bt__att.md#gad0aa088f621b8965013c3ced27480df7)   0x0001 |
| #define | [BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE](group__bt__att.md#ga1b3dc5fedec8d8632d3650405d1ff988)   0xffff |

| Enumerations | |
| --- | --- |
| enum | [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) { [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739) = 0x0 , [BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) = BIT(0) , [BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) = BIT(1) } |
|  | ATT channel option bit field values. [More...](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) |

| Functions | |
| --- | --- |
| static const char \* | [bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) att\_err) |
|  | Converts a ATT error to string. |
| int | [bt\_eatt\_connect](group__bt__att.md#ga748194cbbd54a3336d3c788f08e3de99) (struct bt\_conn \*conn, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Connect Enhanced ATT channels. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_eatt\_count](group__bt__att.md#ga3cabc05e8f5c0418ff02dd7122b7565e) (struct bt\_conn \*conn) |
|  | Get number of EATT channels connected. |

## Detailed Description

Attribute Protocol handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [att.h](att_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
