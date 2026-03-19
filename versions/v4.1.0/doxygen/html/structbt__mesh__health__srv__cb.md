---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__health__srv__cb.html
original_path: doxygen/html/structbt__mesh__health__srv__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_health\_srv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Health Server Model](group__bt__mesh__health__srv.md)

Callback function for the Health Server model.
[More...](#details)

`#include <[health_srv.h](health__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [fault\_get\_cur](#a03ff8869793804dd5943f5d2cd63cc3e) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*company\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count) |
|  | Callback for fetching current faults. |
| int(\* | [fault\_get\_reg](#a555711f2892d8e5a96661c6fff03c7f8) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count) |
|  | Callback for fetching all registered faults. |
| int(\* | [fault\_clear](#afdc878362b78ccfeb4473bcdfb02b9d1) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id) |
|  | Clear all registered faults associated with the given Company ID. |
| int(\* | [fault\_test](#ab426938525f8478ab27dc08a2f25273f) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id) |
|  | Run a self-test. |
| void(\* | [attn\_on](#ad9e8a392943d4848190c4513327bc52c) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Start calling attention to the device. |
| void(\* | [attn\_off](#abd881db6cf849433808bc6464e109b60) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Stop the attention state. |

## Detailed Description

Callback function for the Health Server model.

## Field Documentation

## [◆ ](#abd881db6cf849433808bc6464e109b60)attn\_off

| void(\* bt\_mesh\_health\_srv\_cb::attn\_off) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Stop the attention state.

Any physical activity started to call attention to the device should be stopped.

Parameters
:   | model |  |
    | --- | --- |

## [◆ ](#ad9e8a392943d4848190c4513327bc52c)attn\_on

| void(\* bt\_mesh\_health\_srv\_cb::attn\_on) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
| --- |

Start calling attention to the device.

The attention state is used to map an element address to a physical device. When this callback is called, the device should start some physical procedure meant to call attention to itself, like blinking, buzzing, vibrating or moving. If there are multiple Health server instances on the device, the attention state should also help identify the specific element the server is in.

The attention calling behavior should continue until the `attn_off` callback is called.

Parameters
:   | model | Health Server model to start the attention state of. |
    | --- | --- |

## [◆ ](#afdc878362b78ccfeb4473bcdfb02b9d1)fault\_clear

| int(\* bt\_mesh\_health\_srv\_cb::fault\_clear) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id) |
| --- |

Clear all registered faults associated with the given Company ID.

Parameters
:   | model | Health Server model instance to clear faults of. |
    | --- | --- |
    | company\_id | Company ID to clear faults for. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#a03ff8869793804dd5943f5d2cd63cc3e)fault\_get\_cur

| int(\* bt\_mesh\_health\_srv\_cb::fault\_get\_cur) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*company\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count) |
| --- |

Callback for fetching current faults.

Fault values may either be defined by the specification, or by a vendor. Vendor specific faults should be interpreted in the context of the accompanying Company ID. Specification defined faults may be reported for any Company ID, and the same fault may be presented for multiple Company IDs.

All faults shall be associated with at least one Company ID, representing the device vendor or some other vendor whose vendor specific fault values are used.

If there are multiple Company IDs that have active faults, return only the faults associated with one of them at the time. To report faults for multiple Company IDs, interleave which Company ID is reported for each call.

Parameters
:   | model | Health Server model instance to get faults of. |
    | --- | --- |
    | test\_id | Test ID response buffer. |
    | company\_id | Company ID response buffer. |
    | faults | Array to fill with current faults. |
    | fault\_count | The number of faults the fault array can fit. Should be updated to reflect the number of faults copied into the array. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#a555711f2892d8e5a96661c6fff03c7f8)fault\_get\_reg

| int(\* bt\_mesh\_health\_srv\_cb::fault\_get\_reg) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count) |
| --- |

Callback for fetching all registered faults.

Registered faults are all past and current faults since the last call to `fault_clear`. Only faults associated with the given Company ID should be reported.

Fault values may either be defined by the specification, or by a vendor. Vendor specific faults should be interpreted in the context of the accompanying Company ID. Specification defined faults may be reported for any Company ID, and the same fault may be presented for multiple Company IDs.

Parameters
:   | model | Health Server model instance to get faults of. |
    | --- | --- |
    | company\_id | Company ID to get faults for. |
    | test\_id | Test ID response buffer. |
    | faults | Array to fill with registered faults. |
    | fault\_count | The number of faults the fault array can fit. Should be updated to reflect the number of faults copied into the array. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ab426938525f8478ab27dc08a2f25273f)fault\_test

| int(\* bt\_mesh\_health\_srv\_cb::fault\_test) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id) |
| --- |

Run a self-test.

The Health server may support up to 256 self-tests for each Company ID. The behavior for all test IDs are vendor specific, and should be interpreted based on the accompanying Company ID. Test failures should result in changes to the fault array.

Parameters
:   | model | Health Server model instance to run test for. |
    | --- | --- |
    | test\_id | Test ID to run. |
    | company\_id | Company ID to run test for. |

Returns
:   0 if the test execution was started successfully, or (negative) error code otherwise. Note that the fault array will not be reported back to the client if the test execution didn't start.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[health\_srv.h](health__srv_8h_source.md)

- [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
