---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__ots__client__cb.html
original_path: doxygen/html/structbt__ots__client__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

OTS client callback structure.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [obj\_selected](#ace98d27220e394b0990a8274bbd43026) )(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err) |
|  | Callback function when a new object is selected. |
| int(\* | [obj\_data\_read](#ae95f3b85758c04279ada801c001086bc) )(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_p, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_complete) |
|  | Callback function for the data of the selected object. |
| void(\* | [obj\_metadata\_read](#ab6c03b98fc5c68aa8c76ada23b7dff1c) )(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata\_read) |
|  | Callback function for metadata of the selected object. |
| void(\* | [obj\_data\_written](#a2baaf13c8de4ade034f2b58896225e0d) )(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Callback function for the data of the write object. |
| void(\* | [obj\_checksum\_calculated](#ad5537da9ced98a15620a7fb1e77b0218) )(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) checksum) |
|  | Callback function when checksum indication is received. |

## Detailed Description

OTS client callback structure.

## Field Documentation

## [◆ ](#ad5537da9ced98a15620a7fb1e77b0218)obj\_checksum\_calculated

| void(\* bt\_ots\_client\_cb::obj\_checksum\_calculated) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) checksum) |
| --- |

Callback function when checksum indication is received.

Called when the oacp\_ind\_handler received response of OP BT\_GATT\_OTS\_OACP\_PROC\_CHECKSUM\_CALC.

Parameters
:   | ots\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | The connection to the peer device. |
    | err | Error code (bt\_gatt\_ots\_oacp\_res\_code). |
    | [Checksum](group__checksum.md) | Checksum if error code is BT\_GATT\_OTS\_OACP\_RES\_SUCCESS, otherwise 0. |

## [◆ ](#ae95f3b85758c04279ada801c001086bc)obj\_data\_read

| int(\* bt\_ots\_client\_cb::obj\_data\_read) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_p, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_complete) |
| --- |

Callback function for the data of the selected object.

Called when the data of the selected object are read using [bt\_ots\_client\_read\_object\_data()](group__bt__ots.md#ga8ad1c53325c1b77271307507317a5965 "Read the data of the current selected object.").

Parameters
:   | ots\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | The connection to the peer device. |
    | offset | Offset of the received data. |
    | len | Length of the received data. |
    | data\_p | Pointer to the received data. |
    | is\_complete | Indicate if the whole object has been received. |

Returns
:   int BT\_OTS\_STOP or BT\_OTS\_CONTINUE. BT\_OTS\_STOP can be used to stop reading.

## [◆ ](#a2baaf13c8de4ade034f2b58896225e0d)obj\_data\_written

| void(\* bt\_ots\_client\_cb::obj\_data\_written) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Callback function for the data of the write object.

Called when the data of the selected object is written using [bt\_ots\_client\_write\_object\_data()](group__bt__ots.md#ga9444b064c616718dae1577b21540fb9a "Write the data of the current selected object.").

Parameters
:   | ots\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | The connection to the peer device. |
    | len | Length of the written data. |

## [◆ ](#ab6c03b98fc5c68aa8c76ada23b7dff1c)obj\_metadata\_read

| void(\* bt\_ots\_client\_cb::obj\_metadata\_read) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata\_read) |
| --- |

Callback function for metadata of the selected object.

Called when metadata of the selected object are read using [bt\_ots\_client\_read\_object\_metadata()](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0 "Read the metadata of the current object."). Not all of the metadata may have been initialized.

Parameters
:   | ots\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | The connection to the peer device. |
    | err | Error value. 0 on success, GATT error or ERRNO on fail. |
    | metadata\_read | Bitfield of the metadata that was successfully read. |

## [◆ ](#ace98d27220e394b0990a8274bbd43026)obj\_selected

| void(\* bt\_ots\_client\_cb::obj\_selected) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn, int err) |
| --- |

Callback function when a new object is selected.

Called when the a new object is selected and the current object has changed. The cur\_object in ots\_inst will have been reset, and metadata should be read again with [bt\_ots\_client\_read\_object\_metadata()](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0 "Read the metadata of the current object.").

Parameters
:   | ots\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | The connection to the peer device. |
    | err | Error code (bt\_ots\_olcp\_res\_code). |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_client\_cb](structbt__ots__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
