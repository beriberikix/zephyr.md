---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__ots__cb.html
original_path: doxygen/html/structbt__ots__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

OTS callback structure.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [obj\_created](#a0c95b2bc382474be3c1ae849936a8206) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*add\_param, struct [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md) \*created\_desc) |
|  | Object created callback. |
| int(\* | [obj\_deleted](#a2fd78b43691e83c1faa86c1748ab2359) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Object deleted callback. |
| void(\* | [obj\_selected](#ae8602aef0fd001d6768dc20c8873742d) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Object selected callback. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [obj\_read](#ab67ca0032b8b2fd9b8fbe6c117c186dd) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, void \*\*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset) |
|  | Object read callback. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [obj\_write](#ae31da190c9c6bee086e4d7f8fcd6fbb5) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rem) |
|  | Object write callback. |
| void(\* | [obj\_name\_written](#a600fa13a97f39e3bd53c524039e2733c) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const char \*cur\_name, const char \*new\_name) |
|  | Object name written callback. |
| int(\* | [obj\_cal\_checksum](#a2ef2245c017015b81c0f276f00fd6f79) )(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*\*data) |
|  | Object Calculate checksum callback. |

## Detailed Description

OTS callback structure.

## Field Documentation

## [◆ ](#a2ef2245c017015b81c0f276f00fd6f79)obj\_cal\_checksum

| int(\* bt\_ots\_cb::obj\_cal\_checksum) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*\*data) |
| --- |

Object Calculate checksum callback.

This callback is called when the OACP Calculate Checksum procedure is performed. Because object data is opaque to OTS, the application is the only one who knows where data is and should return pointer of actual object data.

Parameters
:   | [in] | ots | OTS instance. |
    | --- | --- | --- |
    | [in] | conn | The connection that wrote object. |
    | [in] | id | Object ID. |
    | [in] | offset | The first octet of the object contents need to be calculated. |
    | [in] | len | The length number of octets object name. |
    | [out] | data | Pointer of actual object data. |

Returns
:   0 to accept, or any negative value to reject.

## [◆ ](#a0c95b2bc382474be3c1ae849936a8206)obj\_created

| int(\* bt\_ots\_cb::obj\_created) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*add\_param, struct [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md) \*created\_desc) |
| --- |

Object created callback.

This callback is called whenever a new object is created. Application can reject this request by returning an error when it does not have necessary resources to hold this new object. This callback is also triggered when the server creates a new object with [bt\_ots\_obj\_add()](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c "Add an object to the OTS instance.") API.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that is requesting object creation or NULL if object is created by [bt\_ots\_obj\_add()](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c "Add an object to the OTS instance."). |
    | id | Object ID. |
    | add\_param | Object creation requested parameters. |
    | created\_desc | Created object descriptor that shall be filled by the receiver of this callback. |

Returns
:   0 in case of success or negative value in case of error.
:   -ENOTSUP if object type is not supported
:   -ENOMEM if no available space for new object.
:   -EINVAL if an invalid parameter is provided
:   other negative values are treated as a generic operation failure

## [◆ ](#a2fd78b43691e83c1faa86c1748ab2359)obj\_deleted

| int(\* bt\_ots\_cb::obj\_deleted) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Object deleted callback.

This callback is called whenever an object is deleted. It is also triggered when the server deletes an object with [bt\_ots\_obj\_delete()](group__bt__ots.md#ga872ba5a73fa4e617b9d48e7361af74c7 "Delete an object from the OTS instance.") API.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that deleted the object or NULL if this request came from the server. |
    | id | Object ID. |

Return values
:   | When | an error is indicated by using a negative value, the object delete procedure is aborted and a corresponding failed status is returned to the client. |
    | --- | --- |

Returns
:   0 in case of success.
:   -EBUSY if the object is locked. This is generally not expected to be returned by the application as the OTS layer tracks object accesses. An object locked status is returned to the client.
:   Other negative values in case of error. A generic operation failed status is returned to the client.

## [◆ ](#a600fa13a97f39e3bd53c524039e2733c)obj\_name\_written

| void(\* bt\_ots\_cb::obj\_name\_written) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const char \*cur\_name, const char \*new\_name) |
| --- |

Object name written callback.

This callback is called when the object name is written. This is a notification to the application that the object name will be updated by the OTS service implementation.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that wrote object name. |
    | id | Object ID. |
    | cur\_name | Current object name. |
    | new\_name | New object name. |

## [◆ ](#ab67ca0032b8b2fd9b8fbe6c117c186dd)obj\_read

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* bt\_ots\_cb::obj\_read) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, void \*\*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset) |
| --- |

Object read callback.

This callback is called multiple times during the Object read operation. OTS module will keep requesting successive Object fragments from the application until the read operation is completed. The end of read operation is indicated by NULL data parameter.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that read object. |
    | id | Object ID. |
    | data | In: NULL once the read operations is completed. Out: Next chunk of data to be sent. |
    | len | Remaining length requested by the client. |
    | offset | Object data offset. |

Returns
:   Data length to be sent via data parameter. This value shall be smaller or equal to the len parameter.
:   Negative value in case of an error.

## [◆ ](#ae8602aef0fd001d6768dc20c8873742d)obj\_selected

| void(\* bt\_ots\_cb::obj\_selected) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Object selected callback.

This callback is called on successful object selection.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that selected new object. |
    | id | Object ID. |

## [◆ ](#ae31da190c9c6bee086e4d7f8fcd6fbb5)obj\_write

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* bt\_ots\_cb::obj\_write) (struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rem) |
| --- |

Object write callback.

This callback is called multiple times during the Object write operation. OTS module will keep providing successive Object fragments to the application until the write operation is completed. The offset and length of each write fragment is validated by the OTS module to be within the allocated size of the object. The remaining length indicates data length remaining to be written and will decrease each write iteration until it reaches 0 in the last write fragment.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | conn | The connection that wrote object. |
    | id | Object ID. |
    | data | Next chunk of data to be written. |
    | len | Length of the current chunk of data in the buffer. |
    | offset | Object data offset. |
    | rem | Remaining length in the write operation. |

Returns
:   Number of bytes written in case of success, if the number of bytes written does not match len, -EIO is returned to the L2CAP layer.
:   A negative value in case of an error.
:   -EINPROGRESS has a special meaning and is unsupported at the moment. It should not be returned.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_cb](structbt__ots__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
