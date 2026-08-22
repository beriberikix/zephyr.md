---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nrf__clock__control_8h.html
original_path: doxygen/html/nrf__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/onoff.h](onoff_8h_source.md)>`  
`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](nrf__clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nrf\_clock\_spec](structnrf__clock__spec.md) |
| struct | [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX](#a23770353a9de4e4bec02bca693c6709e)   [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) |
| #define | [NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX](#af6cb7f3b8b7bb9540751639e1e48f229)   1 |
| #define | [NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM](#a4a7fdc5110eef82b86b642d40d9dc02e)(ppm) |
| #define | [NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH](#a0c870f2b78d538f7a33cf47110ed6ea7)   1 |
| #define | [NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT](#a15b112b62c60a7b9ca0b7fd2fccd5cca)   0 |

| Functions | |
| --- | --- |
| static int | [nrf\_clock\_control\_request](#a2da9657c008b903a9131238bde6ed1ac) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Request a reservation to use a given clock with specified attributes. |
| int | [nrf\_clock\_control\_request\_sync](#af334bc4e8b5ca0eb63b2bc4b1d963ac8) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Synchronously request a reservation to use a given clock with specified attributes. |
| static int | [nrf\_clock\_control\_release](#aa46e3e407fb02b206772c438a0108634) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec) |
|  | Release a reserved use of a clock. |
| static int | [nrf\_clock\_control\_cancel\_or\_release](#a3ecff5c6b37ced253c030fd032c61a70) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, struct [onoff\_client](structonoff__client.md) \*cli) |
|  | Safely cancel a reservation request. |
| static int | [nrf\_clock\_control\_resolve](#add7ed9d76f521cc2894ba21abc8e4d94) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*req\_spec, struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*res\_spec) |
|  | Resolve a requested clock spec to resulting spec. |
| static int | [nrf\_clock\_control\_get\_startup\_time](#a0ac2c96482c7551b16f1cc4eadd01560) (const struct [device](structdevice.md) \*dev, const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*startup\_time\_us) |
|  | Get the startup time of a clock. |
| void | [nrf\_clock\_control\_hfxo\_request](#a259dfa1a679d21c4b92ecbf9fdfd3d13) (void) |
|  | Request the HFXO from Zero Latency Interrupt context. |
| void | [nrf\_clock\_control\_hfxo\_release](#a502110bf4c35eca120f883ba766705b7) (void) |
|  | Release the HFXO from Zero Latency Interrupt context. |

## Macro Definition Documentation

## [◆ ](#af6cb7f3b8b7bb9540751639e1e48f229)NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX

| #define NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX   1 |
| --- |

## [◆ ](#a4a7fdc5110eef82b86b642d40d9dc02e)NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM

| #define NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM | ( |  | *ppm* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(ppm)

## [◆ ](#a23770353a9de4e4bec02bca693c6709e)NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX

| #define NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX   [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) |
| --- |

## [◆ ](#a15b112b62c60a7b9ca0b7fd2fccd5cca)NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT

| #define NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT   0 |
| --- |

## [◆ ](#a0c870f2b78d538f7a33cf47110ed6ea7)NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH

| #define NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH   1 |
| --- |

## Function Documentation

## [◆ ](#a3ecff5c6b37ced253c030fd032c61a70)nrf\_clock\_control\_cancel\_or\_release()

| | int nrf\_clock\_control\_cancel\_or\_release | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *spec*, | |  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Safely cancel a reservation request.

It may be that a client has issued a reservation request but needs to shut down before the request has completed. This function attempts to cancel the request and issues a release if cancellation fails because the request was completed. This synchronously ensures that ownership data reverts to the client so is available for a future request.

Parameters
:   | dev | pointer to the clock device structure. |
    | --- | --- |
    | spec | the same specification of the clock attributes that was used in the reservation request. |
    | cli | a pointer to the same client state that was provided when the operation to be cancelled was issued. |

Return values
:   | [ONOFF\_STATE\_TO\_ON](group__resource__mgmt__onoff__apis.md#gac4a0d8a7b501adb011aa1c4c4da3f2a3 "Value exposed by ONOFF_STATE_MASK when service is transitioning to on.") | if the cancellation occurred before the transition completed. |
    | --- | --- |
    | [ONOFF\_STATE\_ON](group__resource__mgmt__onoff__apis.md#ga7cd0fba52afba2e337ab7c830d3058d7 "Value exposed by ONOFF_STATE_MASK when service is on.") | if the cancellation occurred after the transition completed. |
    | -EINVAL | if the parameters are invalid. |
    | negative | other errors produced by [onoff\_release()](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6 "Release a reserved use of an on-off service."). |

## [◆ ](#a0ac2c96482c7551b16f1cc4eadd01560)nrf\_clock\_control\_get\_startup\_time()

| | int nrf\_clock\_control\_get\_startup\_time | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *spec*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *startup\_time\_us* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Get the startup time of a clock.

Parameters
:   | dev | Device structure. |
    | --- | --- |
    | spec | Clock specification to get startup time for. |
    | startup\_time\_us | Destination for startup time in microseconds. |

Return values
:   | Successful | if successful. |
    | --- | --- |
    | -errno | code if failure. |

## [◆ ](#a502110bf4c35eca120f883ba766705b7)nrf\_clock\_control\_hfxo\_release()

| void nrf\_clock\_control\_hfxo\_release | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Release the HFXO from Zero Latency Interrupt context.

Function is optimized for use in Zero Latency Interrupt context.

Calls to this function must be coupled with prior calls to [nrf\_clock\_control\_hfxo\_request()](#a259dfa1a679d21c4b92ecbf9fdfd3d13), because it uses basic reference counting to make sure the HFXO is released when there are no more pending requests.

## [◆ ](#a259dfa1a679d21c4b92ecbf9fdfd3d13)nrf\_clock\_control\_hfxo\_request()

| void nrf\_clock\_control\_hfxo\_request | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Request the HFXO from Zero Latency Interrupt context.

Function is optimized for use in Zero Latency Interrupt context. It does not give notification when the HFXO is ready, so each user must put the request early enough to make sure the HFXO ramp-up has finished on time.

This function uses reference counting so the caller must ensure that every [nrf\_clock\_control\_hfxo\_request()](#a259dfa1a679d21c4b92ecbf9fdfd3d13) call has a matching [nrf\_clock\_control\_hfxo\_release()](#a502110bf4c35eca120f883ba766705b7) call.

## [◆ ](#aa46e3e407fb02b206772c438a0108634)nrf\_clock\_control\_release()

| | int nrf\_clock\_control\_release | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *spec* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Release a reserved use of a clock.

Parameters
:   | dev | pointer to the clock device structure. |
    | --- | --- |
    | spec | the same specification of the clock attributes that was used in the reservation request (so that the clock control module can keep track of what attributes are still requested). |

Return values
:   | non-negative | the observed state of the on-off service associated with the clock machine at the time the request was processed (see [onoff\_release()](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6 "Release a reserved use of an on-off service.")), if successful. |
    | --- | --- |
    | -EIO | if service has recorded an error. |
    | -ENOTSUP | if the service is not in a state that permits release. |

## [◆ ](#a2da9657c008b903a9131238bde6ed1ac)nrf\_clock\_control\_request()

| | int nrf\_clock\_control\_request | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *spec*, | |  |  | struct [onoff\_client](structonoff__client.md) \* | *cli* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Request a reservation to use a given clock with specified attributes.

The return value indicates the success or failure of an attempt to initiate an operation to request the clock be made available. If initiation of the operation succeeds, the result of the request operation is provided through the configured client notification method, possibly before this call returns.

Note that the call to this function may succeed in a case where the actual request fails. Always check the operation completion result.

Parameters
:   | dev | pointer to the clock device structure. |
    | --- | --- |
    | spec | specification of minimal acceptable attributes, like frequency, accuracy, and precision, required for the clock. Value of 0 has the meaning of "default" and can be passed instead of a given attribute if there is no strict requirement in this regard. If there is no specific requirement for any of the attributes, this parameter can be NULL. |
    | cli | pointer to client state providing instructions on synchronous expectations and how to notify the client when the request completes. Behavior is undefined if client passes a pointer object associated with an incomplete service operation. |

Return values
:   | non-negative | the observed state of the on-off service associated with the clock machine at the time the request was processed (see [onoff\_request()](group__resource__mgmt__onoff__apis.md#ga20dcb358e405deb87b7fbb7846ef9d68 "Request a reservation to use an on-off service.")), if successful. |
    | --- | --- |
    | -EIO | if service has recorded an error. |
    | -EINVAL | if the function parameters are invalid or the clock attributes cannot be provided (e.g. the requested accuracy is unavailable). |
    | -EAGAIN | if the reference count would overflow. |

## [◆ ](#af334bc4e8b5ca0eb63b2bc4b1d963ac8)nrf\_clock\_control\_request\_sync()

| int nrf\_clock\_control\_request\_sync | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *spec*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

Synchronously request a reservation to use a given clock with specified attributes.

Function can only be called from thread context as it blocks until request is completed.

See also
:   [nrf\_clock\_control\_request()](#a2da9657c008b903a9131238bde6ed1ac).

Parameters
:   | dev | pointer to the clock device structure. |
    | --- | --- |
    | spec | See [nrf\_clock\_control\_request()](#a2da9657c008b903a9131238bde6ed1ac). |
    | timeout | Request timeout. |

Return values
:   | 0 | if request is fulfilled. |
    | --- | --- |
    | -EWOULDBLOCK | if request is called from the interrupt context. |
    | negative | See error codes returned by [nrf\_clock\_control\_request()](#a2da9657c008b903a9131238bde6ed1ac). |

## [◆ ](#add7ed9d76f521cc2894ba21abc8e4d94)nrf\_clock\_control\_resolve()

| | int nrf\_clock\_control\_resolve | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *req\_spec*, | |  |  | struct [nrf\_clock\_spec](structnrf__clock__spec.md) \* | *res\_spec* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Resolve a requested clock spec to resulting spec.

Parameters
:   | dev | Device structure. |
    | --- | --- |
    | req\_spec | The requested clock specification. |
    | res\_spec | Destination for the resulting clock specification. |

Return values
:   | Successful | if successful. |
    | --- | --- |
    | -errno | code if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [nrf\_clock\_control.h](nrf__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
