---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__model__cb.html
original_path: doxygen/html/structbt__mesh__model__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_model\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Model callback functions.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\*const | [settings\_set](#a21fc24829c6933a035b0f0be1a1f58e5) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, const char \*name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len\_rd, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
|  | Set value handler of user data tied to the model. |
| int(\*const | [start](#a8333420fb9d1d98799ae03ba3b23bfe4) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Callback called when the mesh is started. |
| int(\*const | [init](#a1688a2c6d7b3b17ba49a0975b6f4f68e) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Model init callback. |
| void(\*const | [reset](#a3a7ad466120085c55bcffacb15c78518) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Model reset callback. |
| void(\*const | [pending\_store](#ae28f875dffc7f5f2ce99abe590369f43) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Callback used to store pending model's user data. |

## Detailed Description

Model callback functions.

## Field Documentation

## [◆ ](#a1688a2c6d7b3b17ba49a0975b6f4f68e)init

| int(\*const bt\_mesh\_model\_cb::init) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Model init callback.

Called on every model instance during mesh initialization.

If any of the model init callbacks return an error, the Mesh subsystem initialization will be aborted, and the error will be returned to the caller of [bt\_mesh\_init](group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405 "bt_mesh_init").

Parameters
:   | model | Model to be initialized. |
    | --- | --- |

Returns
:   0 on success, error otherwise.

## [◆ ](#ae28f875dffc7f5f2ce99abe590369f43)pending\_store

| void(\*const bt\_mesh\_model\_cb::pending\_store) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Callback used to store pending model's user data.

Triggered by [bt\_mesh\_model\_data\_store\_schedule](group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db "bt_mesh_model_data_store_schedule").

To store the user data, call [bt\_mesh\_model\_data\_store](group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85 "bt_mesh_model_data_store").

Parameters
:   | model | Model this callback belongs to. |
    | --- | --- |

## [◆ ](#a3a7ad466120085c55bcffacb15c78518)reset

| void(\*const bt\_mesh\_model\_cb::reset) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Model reset callback.

Called when the mesh node is reset. All model data is deleted on reset, and the model should clear its state.

Note
:   If the model stores any persistent data, this needs to be erased manually.

Parameters
:   | model | Model this callback belongs to. |
    | --- | --- |

## [◆ ](#a21fc24829c6933a035b0f0be1a1f58e5)settings\_set

| int(\*const bt\_mesh\_model\_cb::settings\_set) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, const char \*name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len\_rd, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
| --- |

Set value handler of user data tied to the model.

See also
:   [settings\_handler::h\_set](structsettings__handler.md#a70aa25bf3b53898ab22906e9949963a4 "Set value handler of settings items identified by keyword names.")

Parameters
:   | model | Model to set the persistent data of. |
    | --- | --- |
    | name | Name/key of the settings item. |
    | len\_rd | The size of the data found in the backend. |
    | read\_cb | Function provided to read the data from the backend. |
    | cb\_arg | Arguments for the read function provided by the backend. |

Returns
:   0 on success, error otherwise.

## [◆ ](#a8333420fb9d1d98799ae03ba3b23bfe4)start

| int(\*const bt\_mesh\_model\_cb::start) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Callback called when the mesh is started.

This handler gets called after the node has been provisioned, or after all mesh data has been loaded from persistent storage.

When this callback fires, the mesh model may start its behavior, and all Access APIs are ready for use.

Parameters
:   | model | Model this callback belongs to. |
    | --- | --- |

Returns
:   0 on success, error otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
