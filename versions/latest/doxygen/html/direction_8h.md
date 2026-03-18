---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/direction_8h.html
original_path: doxygen/html/direction_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

direction.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](direction_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md) |
|  | Constant Tone Extension parameters for connectionless transmission. [More...](structbt__df__adv__cte__tx__param.md#details) |
| struct | [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md) |
|  | Constant Tone Extension parameters for connectionless reception. [More...](structbt__df__per__adv__sync__cte__rx__param.md#details) |
| struct | [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) |
| struct | [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md) |
| struct | [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md) |
| struct | [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md) |
|  | Constant Tone Extension parameters for CTE transmission in connected mode. [More...](structbt__df__conn__cte__tx__param.md#details) |
| struct | [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md) |

| Enumerations | |
| --- | --- |
| enum | [bt\_df\_cte\_type](#a64bf01dee8bc4bbc62e0dbc356726a05) {     [BT\_DF\_CTE\_TYPE\_NONE](#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1) = 0 , [BT\_DF\_CTE\_TYPE\_AOA](#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207) = BIT(0) , [BT\_DF\_CTE\_TYPE\_AOD\_1US](#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da) = BIT(1) , [BT\_DF\_CTE\_TYPE\_AOD\_2US](#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8) = BIT(2) ,     [BT\_DF\_CTE\_TYPE\_ALL](#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7) = (BT\_DF\_CTE\_TYPE\_AOA | BT\_DF\_CTE\_TYPE\_AOD\_1US | BT\_DF\_CTE\_TYPE\_AOD\_2US)   } |
|  | Constant Tone Extension (CTE) types. [More...](#a64bf01dee8bc4bbc62e0dbc356726a05) |
| enum | [bt\_df\_antenna\_switching\_slot](#a546598ce9a81161ad1ba098a7b1a8df4) { [BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_1US](#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a) = 0x1 , [BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_2US](#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38) = 0x2 } |
|  | Allowed antenna switching slots: 1 us or 2 us. [More...](#a546598ce9a81161ad1ba098a7b1a8df4) |
| enum | [bt\_df\_packet\_status](#ab9acadbaf03dd976a2ee185574effb4c) { [BT\_DF\_CTE\_CRC\_OK](#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c) = 0x0 , [BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME](#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92) = 0x1 , [BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER](#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9) = 0x2 , [BT\_DF\_CTE\_INSUFFICIENT\_RESOURCES](#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b) = 0xFF } |
|  | Possible statuses of PDU that contained reported CTE. [More...](#ab9acadbaf03dd976a2ee185574effb4c) |
| enum | [bt\_df\_iq\_sample](#a53df7da4b178b4a6e4dd68e9266c0771) { [BT\_DF\_IQ\_SAMPLE\_8\_BITS\_INT](#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4) , [BT\_DF\_IQ\_SAMPLE\_16\_BITS\_INT](#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b) } |
| enum | [bt\_df\_conn\_iq\_report\_err](#a953634e6a88617a8729541d6b5bd0dd6) { [BT\_DF\_IQ\_REPORT\_ERR\_SUCCESS](#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519) , [BT\_DF\_IQ\_REPORT\_ERR\_NO\_CTE](#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e) , [BT\_DF\_IQ\_REPORT\_ERR\_PEER\_REJECTED](#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512) } |

| Functions | |
| --- | --- |
| int | [bt\_df\_set\_adv\_cte\_tx\_param](#ae98248377f111deb6aa0565db1d3f690) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md) \*params) |
|  | Set or update the Constant Tone Extension parameters for periodic advertising set. |
| int | [bt\_df\_adv\_cte\_tx\_enable](#ab03ec552192056eb8ddb9aae49029265) (struct bt\_le\_ext\_adv \*adv) |
|  | Enable transmission of Constant Tone Extension for the given advertising set. |
| int | [bt\_df\_adv\_cte\_tx\_disable](#a248cd22ad9afe050e3d535f7124112d9) (struct bt\_le\_ext\_adv \*adv) |
|  | Disable transmission of Constant Tone Extension for the given advertising set. |
| int | [bt\_df\_per\_adv\_sync\_cte\_rx\_enable](#a26c40ea36de60266f029763551cd9d4e) (struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md) \*params) |
|  | Enable receive and sampling of Constant Tone Extension for the given sync set. |
| int | [bt\_df\_per\_adv\_sync\_cte\_rx\_disable](#ac2064484bb3c4ea6ae5eb684f3ace008) (struct bt\_le\_per\_adv\_sync \*sync) |
|  | Disable receive and sampling of Constant Tone Extension for the given sync set. |
| int | [bt\_df\_conn\_cte\_rx\_enable](#a92d0b485a83a7395b3613b144b6e749f) (struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md) \*params) |
|  | Enable receive and sampling of Constant Tone Extension for the connection object. |
| int | [bt\_df\_conn\_cte\_rx\_disable](#a861696041baa770ef3968789afd4cbac) (struct bt\_conn \*conn) |
|  | Disable receive and sampling of Constant Tone Extension for the connection object. |
| int | [bt\_df\_set\_conn\_cte\_tx\_param](#aa0eba41c1a810c9592e0097ee4fe7329) (struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md) \*params) |
|  | Set Constant Tone Extension transmission parameters for a connection. |
| int | [bt\_df\_conn\_cte\_req\_enable](#a84fee1f1ac25af73bb7a8f91ed912c67) (struct bt\_conn \*conn, const struct [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md) \*params) |
|  | Enable Constant Tone Extension request procedure for a connection. |
| int | [bt\_df\_conn\_cte\_req\_disable](#ade1a048c3fdf11e979fa9a74f33bc375) (struct bt\_conn \*conn) |
|  | Disable Constant Tone Extension request procedure for a connection. |
| int | [bt\_df\_conn\_cte\_rsp\_enable](#a5e4a5168020d488561646beac48916f5) (struct bt\_conn \*conn) |
|  | Enable Constant Tone Extension response procedure for a connection. |
| int | [bt\_df\_conn\_cte\_rsp\_disable](#a856cfbe26fba92c80f4cf6012a0bbafe) (struct bt\_conn \*conn) |
|  | Disable Constant Tone Extension response procedure for a connection. |

## Enumeration Type Documentation

## [◆ ](#a546598ce9a81161ad1ba098a7b1a8df4)bt\_df\_antenna\_switching\_slot

| enum [bt\_df\_antenna\_switching\_slot](#a546598ce9a81161ad1ba098a7b1a8df4) |
| --- |

Allowed antenna switching slots: 1 us or 2 us.

| Enumerator | |
| --- | --- |
| BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_1US |  |
| BT\_DF\_ANTENNA\_SWITCHING\_SLOT\_2US |  |

## [◆ ](#a953634e6a88617a8729541d6b5bd0dd6)bt\_df\_conn\_iq\_report\_err

| enum [bt\_df\_conn\_iq\_report\_err](#a953634e6a88617a8729541d6b5bd0dd6) |
| --- |

| Enumerator | |
| --- | --- |
| BT\_DF\_IQ\_REPORT\_ERR\_SUCCESS | IQ samples report received successfully. |
| BT\_DF\_IQ\_REPORT\_ERR\_NO\_CTE | Received PDU without CTE.  No valid data in report. |
| BT\_DF\_IQ\_REPORT\_ERR\_PEER\_REJECTED | Peer rejected CTE request.  No valid data in report. |

## [◆ ](#a64bf01dee8bc4bbc62e0dbc356726a05)bt\_df\_cte\_type

| enum [bt\_df\_cte\_type](#a64bf01dee8bc4bbc62e0dbc356726a05) |
| --- |

Constant Tone Extension (CTE) types.

| Enumerator | |
| --- | --- |
| BT\_DF\_CTE\_TYPE\_NONE | Convenience value for purposes where non of CTE types is allowed. |
| BT\_DF\_CTE\_TYPE\_AOA | Angle of Arrival mode.  Antenna switching done on receiver site. |
| BT\_DF\_CTE\_TYPE\_AOD\_1US | Angle of Departure mode with 1 us antenna switching slots.  Antenna switching done on transmitter site. |
| BT\_DF\_CTE\_TYPE\_AOD\_2US | Angle of Departure mode with 2 us antenna switching slots.  Antenna switching done on transmitter site. |
| BT\_DF\_CTE\_TYPE\_ALL | Convenience value that collects all possible CTE types in one entry. |

## [◆ ](#a53df7da4b178b4a6e4dd68e9266c0771)bt\_df\_iq\_sample

| enum [bt\_df\_iq\_sample](#a53df7da4b178b4a6e4dd68e9266c0771) |
| --- |

| Enumerator | |
| --- | --- |
| BT\_DF\_IQ\_SAMPLE\_8\_BITS\_INT | Reported IQ samples have 8 bits signed integer format.  Size defined in BT Core 5.3 Vol 4, Part E sections 7.7.65.21 and 7.7.65.22. |
| BT\_DF\_IQ\_SAMPLE\_16\_BITS\_INT | Reported IQ samples have 16 bits signed integer format.  Vendor specific extension. |

## [◆ ](#ab9acadbaf03dd976a2ee185574effb4c)bt\_df\_packet\_status

| enum [bt\_df\_packet\_status](#ab9acadbaf03dd976a2ee185574effb4c) |
| --- |

Possible statuses of PDU that contained reported CTE.

| Enumerator | |
| --- | --- |
| BT\_DF\_CTE\_CRC\_OK | Received PDU had CRC OK. |
| BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_TIME | Received PDU had incorrect CRC, but Radio peripheral was able to parse CTEInfo field of the PDU and process sampling of CTE. |
| BT\_DF\_CTE\_CRC\_ERR\_CTE\_BASED\_OTHER | Received PDU had incorrect CRC, but Radio peripheral was able to process sampling of CTE in some other way. |
| BT\_DF\_CTE\_INSUFFICIENT\_RESOURCES | There were no sufficient resources to sample CTE. |

## Function Documentation

## [◆ ](#a248cd22ad9afe050e3d535f7124112d9)bt\_df\_adv\_cte\_tx\_disable()

| int bt\_df\_adv\_cte\_tx\_disable | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable transmission of Constant Tone Extension for the given advertising set.

Parameters
:   | [in] | adv | Advertising set object. |
    | --- | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ab03ec552192056eb8ddb9aae49029265)bt\_df\_adv\_cte\_tx\_enable()

| int bt\_df\_adv\_cte\_tx\_enable | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable transmission of Constant Tone Extension for the given advertising set.

Transmission of Constant Tone Extension may be enabled only after setting periodic advertising parameters ([bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1 "bt_le_per_adv_set_param")) and Constant Tone Extension parameters ([bt\_df\_set\_adv\_cte\_tx\_param](#ae98248377f111deb6aa0565db1d3f690)).

Parameters
:   | [in] | adv | Advertising set object. |
    | --- | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ade1a048c3fdf11e979fa9a74f33bc375)bt\_df\_conn\_cte\_req\_disable()

| int bt\_df\_conn\_cte\_req\_disable | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable Constant Tone Extension request procedure for a connection.

The function is available if `CONFIG_BT_DF_CONNECTION_CTE_REQ` is enabled.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#a84fee1f1ac25af73bb7a8f91ed912c67)bt\_df\_conn\_cte\_req\_enable()

| int bt\_df\_conn\_cte\_req\_enable | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_df\_conn\_cte\_req\_params](structbt__df__conn__cte__req__params.md) \* | *params* ) |

Enable Constant Tone Extension request procedure for a connection.

The function is available if `CONFIG_BT_DF_CONNECTION_CTE_REQ` is enabled.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | CTE receive and sampling parameters. |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#a856cfbe26fba92c80f4cf6012a0bbafe)bt\_df\_conn\_cte\_rsp\_disable()

| int bt\_df\_conn\_cte\_rsp\_disable | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable Constant Tone Extension response procedure for a connection.

The function is available if `CONFIG_BT_DF_CONNECTION_CTE_RSP` is enabled.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#a5e4a5168020d488561646beac48916f5)bt\_df\_conn\_cte\_rsp\_enable()

| int bt\_df\_conn\_cte\_rsp\_enable | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable Constant Tone Extension response procedure for a connection.

The function is available if `CONFIG_BT_DF_CONNECTION_CTE_RSP` is enabled.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#a861696041baa770ef3968789afd4cbac)bt\_df\_conn\_cte\_rx\_disable()

| int bt\_df\_conn\_cte\_rx\_disable | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable receive and sampling of Constant Tone Extension for the connection object.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#a92d0b485a83a7395b3613b144b6e749f)bt\_df\_conn\_cte\_rx\_enable()

| int bt\_df\_conn\_cte\_rx\_enable | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_df\_conn\_cte\_rx\_param](structbt__df__conn__cte__rx__param.md) \* | *params* ) |

Enable receive and sampling of Constant Tone Extension for the connection object.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | CTE receive and sampling parameters. |

Returns
:   Zero in case of success, other value in case of failure.

## [◆ ](#ac2064484bb3c4ea6ae5eb684f3ace008)bt\_df\_per\_adv\_sync\_cte\_rx\_disable()

| int bt\_df\_per\_adv\_sync\_cte\_rx\_disable | ( | struct bt\_le\_per\_adv\_sync \* | *sync* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable receive and sampling of Constant Tone Extension for the given sync set.

Parameters
:   | sync | Periodic advertising sync object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#a26c40ea36de60266f029763551cd9d4e)bt\_df\_per\_adv\_sync\_cte\_rx\_enable()

| int bt\_df\_per\_adv\_sync\_cte\_rx\_enable | ( | struct bt\_le\_per\_adv\_sync \* | *sync*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_df\_per\_adv\_sync\_cte\_rx\_param](structbt__df__per__adv__sync__cte__rx__param.md) \* | *params* ) |

Enable receive and sampling of Constant Tone Extension for the given sync set.

Receive and sampling of Constant Tone Extension may be enabled only after periodic advertising sync is established.

Parameters
:   | sync | Periodic advertising sync object. |
    | --- | --- |
    | params | CTE receive and sampling parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ae98248377f111deb6aa0565db1d3f690)bt\_df\_set\_adv\_cte\_tx\_param()

| int bt\_df\_set\_adv\_cte\_tx\_param | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_df\_adv\_cte\_tx\_param](structbt__df__adv__cte__tx__param.md) \* | *params* ) |

Set or update the Constant Tone Extension parameters for periodic advertising set.

Parameters
:   | [in] | adv | Advertising set object. |
    | --- | --- | --- |
    | [in] | params | Constant Tone Extension parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#aa0eba41c1a810c9592e0097ee4fe7329)bt\_df\_set\_conn\_cte\_tx\_param()

| int bt\_df\_set\_conn\_cte\_tx\_param | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_df\_conn\_cte\_tx\_param](structbt__df__conn__cte__tx__param.md) \* | *params* ) |

Set Constant Tone Extension transmission parameters for a connection.

The function is available if `CONFIG_BT_DF_CONNECTION_CTE_TX` is enabled.

Note
:   If neither BT\_DF\_CTE\_TYPE\_AOD\_1US or BT\_DF\_CTE\_TYPE\_AOD\_2US are set in the bitfield, then the [bt\_df\_conn\_cte\_tx\_param.num\_ant\_ids](structbt__df__conn__cte__tx__param.md#ad49bc64170e8ee4741aa01393284e7de "Number of antenna switch pattern.") and [bt\_df\_conn\_cte\_tx\_param.ant\_ids](structbt__df__conn__cte__tx__param.md#a9df1dac6180e77a4c7abc80890346c4a "Antenna switch pattern.") parameters will be ignored.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | CTE transmission parameters. |

Returns
:   Zero in case of success, other value in case of failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [direction.h](direction_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
