---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hfp__hf__cb.html
original_path: doxygen/html/structbt__hfp__hf__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hfp\_hf\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hands Free Profile (HFP)](group__bt__hfp.md)

HFP profile application callback.
[More...](#details)

`#include <[hfp_hf.h](hfp__hf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#a989373632ab9c5e9f5ee6a8b15d2818d) )(struct bt\_conn \*conn) |
|  | HF connected callback to application. |
| void(\* | [disconnected](#a064e7e6471d537aebc36f3273443cf45) )(struct bt\_conn \*conn) |
|  | HF disconnected callback to application. |
| void(\* | [sco\_connected](#ab99c8d781f4d2f298bd87ab7c6a1cfab) )(struct bt\_conn \*conn, struct bt\_conn \*sco\_conn) |
|  | HF SCO/eSCO connected Callback. |
| void(\* | [sco\_disconnected](#a4586240506c876c9f58cf60a091b4044) )(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | HF SCO/eSCO disconnected Callback. |
| void(\* | [service](#a8e9062e76d30dc9db0b4be9f6ec3e26f) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [call](#a216dcba1621369bc8c8ace22a8b707e8) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [call\_setup](#a0b120f6fd8e20432bab8d9f4f695482f) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [call\_held](#aa9e2671fee627a0767c3f6cb269a39d0) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [signal](#a485cdbf03ef3bce0a156c13c33eed3e1) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [roam](#addc8b3aef445ba67df5d340a5a3e9989) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [battery](#a8deff765f7aa622d495e768b3137871f) )(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [ring\_indication](#a580dd17c688c0e6375ef7c84a3751213) )(struct bt\_conn \*conn) |
|  | HF incoming call Ring indication callback to application. |
| void(\* | [cmd\_complete\_cb](#aa86799138890884ef18e7e0fe4774945) )(struct bt\_conn \*conn, struct [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | HF notify command completed callback to application. |

## Detailed Description

HFP profile application callback.

## Field Documentation

## [◆ ](#a8deff765f7aa622d495e768b3137871f)battery

| void(\* bt\_hfp\_hf\_cb::battery) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback battery service indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | battery indicator value received from the AG. |

## [◆ ](#a216dcba1621369bc8c8ace22a8b707e8)call

| void(\* bt\_hfp\_hf\_cb::call) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides call indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | call indicator value received from the AG. |

## [◆ ](#aa9e2671fee627a0767c3f6cb269a39d0)call\_held

| void(\* bt\_hfp\_hf\_cb::call\_held) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides call held indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | call held indicator value received from the AG. |

## [◆ ](#a0b120f6fd8e20432bab8d9f4f695482f)call\_setup

| void(\* bt\_hfp\_hf\_cb::call\_setup) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides call setup indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | call setup indicator value received from the AG. |

## [◆ ](#aa86799138890884ef18e7e0fe4774945)cmd\_complete\_cb

| void(\* bt\_hfp\_hf\_cb::cmd\_complete\_cb) (struct bt\_conn \*conn, struct [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| --- |

HF notify command completed callback to application.

The command sent from the application is notified about its status

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | structure contains status of the command including cme. |

## [◆ ](#a989373632ab9c5e9f5ee6a8b15d2818d)connected

| void(\* bt\_hfp\_hf\_cb::connected) (struct bt\_conn \*conn) |
| --- |

HF connected callback to application.

If this callback is provided it will be called whenever the connection completes.

Parameters
:   | conn | Connection object. |
    | --- | --- |

## [◆ ](#a064e7e6471d537aebc36f3273443cf45)disconnected

| void(\* bt\_hfp\_hf\_cb::disconnected) (struct bt\_conn \*conn) |
| --- |

HF disconnected callback to application.

If this callback is provided it will be called whenever the connection gets disconnected, including when a connection gets rejected or cancelled or any error in SLC establishment.

Parameters
:   | conn | Connection object. |
    | --- | --- |

## [◆ ](#a580dd17c688c0e6375ef7c84a3751213)ring\_indication

| void(\* bt\_hfp\_hf\_cb::ring\_indication) (struct bt\_conn \*conn) |
| --- |

HF incoming call Ring indication callback to application.

If this callback is provided it will be called whenever there is an incoming call.

Parameters
:   | conn | Connection object. |
    | --- | --- |

## [◆ ](#addc8b3aef445ba67df5d340a5a3e9989)roam

| void(\* bt\_hfp\_hf\_cb::roam) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides roaming indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | roaming indicator value received from the AG. |

## [◆ ](#ab99c8d781f4d2f298bd87ab7c6a1cfab)sco\_connected

| void(\* bt\_hfp\_hf\_cb::sco\_connected) (struct bt\_conn \*conn, struct bt\_conn \*sco\_conn) |
| --- |

HF SCO/eSCO connected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection completes.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | sco\_conn | SCO/eSCO Connection object. |

## [◆ ](#a4586240506c876c9f58cf60a091b4044)sco\_disconnected

| void(\* bt\_hfp\_hf\_cb::sco\_disconnected) (struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

HF SCO/eSCO disconnected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection gets disconnected.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#a8e9062e76d30dc9db0b4be9f6ec3e26f)service

| void(\* bt\_hfp\_hf\_cb::service) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides service indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | service indicator value received from the AG. |

## [◆ ](#a485cdbf03ef3bce0a156c13c33eed3e1)signal

| void(\* bt\_hfp\_hf\_cb::signal) (struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides signal indicator value to the application

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | value | signal indicator value received from the AG. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[hfp\_hf.h](hfp__hf_8h_source.md)

- [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
