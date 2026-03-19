---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__rfcomm__dlc__ops.html
original_path: doxygen/html/structbt__rfcomm__dlc__ops.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_rfcomm\_dlc\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [RFCOMM](group__bt__rfcomm.md)

RFCOMM DLC operations structure.
[More...](#details)

`#include <[rfcomm.h](rfcomm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#aba1719c36e7a1dc9705994bcdf134e28) )(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
|  | DLC connected callback. |
| void(\* | [disconnected](#a4eeaf7b5db6c93e846a72797e6612d30) )(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
|  | DLC disconnected callback. |
| void(\* | [recv](#a4a4e29065b267f0370df5ea602223d0a) )(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf) |
|  | DLC recv callback. |
| void(\* | [sent](#a3ba98c41e03c88f330cba0e3539a1cec) )(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, int err) |
|  | DLC sent callback. |

## Detailed Description

RFCOMM DLC operations structure.

## Field Documentation

## [◆ ](#aba1719c36e7a1dc9705994bcdf134e28)connected

| void(\* bt\_rfcomm\_dlc\_ops::connected) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
| --- |

DLC connected callback.

If this callback is provided it will be called whenever the connection completes.

Parameters
:   | dlc | The dlc that has been connected |
    | --- | --- |

## [◆ ](#a4eeaf7b5db6c93e846a72797e6612d30)disconnected

| void(\* bt\_rfcomm\_dlc\_ops::disconnected) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
| --- |

DLC disconnected callback.

If this callback is provided it will be called whenever the dlc is disconnected, including when a connection gets rejected or cancelled (both incoming and outgoing)

Parameters
:   | dlc | The dlc that has been Disconnected |
    | --- | --- |

## [◆ ](#a4a4e29065b267f0370df5ea602223d0a)recv

| void(\* bt\_rfcomm\_dlc\_ops::recv) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

DLC recv callback.

Parameters
:   | dlc | The dlc receiving data. |
    | --- | --- |
    | buf | Buffer containing incoming data. |

## [◆ ](#a3ba98c41e03c88f330cba0e3539a1cec)sent

| void(\* bt\_rfcomm\_dlc\_ops::sent) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, int err) |
| --- |

DLC sent callback.

Parameters
:   | dlc | The dlc which has sent data. |
    | --- | --- |
    | err | Sent result. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[rfcomm.h](rfcomm_8h_source.md)

- [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
