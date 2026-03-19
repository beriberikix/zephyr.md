---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__aics__cb.html
original_path: doxygen/html/structbt__aics__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_aics\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Audio Input Control Service (AICS)](group__bt__aics.md)

Struct to hold callbacks for the Audio Input Control Service.
[More...](#details)

`#include <[aics.h](aics_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_aics\_state\_cb](group__bt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f) | [state](#a70d099bec6407e5c92f6a4e8d6c44929) |
|  | The audio input state has changed. |
| [bt\_aics\_gain\_setting\_cb](group__bt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb) | [gain\_setting](#a6b2f2a43d0a91abcecfe8372b6a1be4b) |
|  | The gain setting has changed. |
| [bt\_aics\_type\_cb](group__bt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5) | [type](#a41bc7a97e28c53772573d99a38e8ac55) |
|  | The audio input type has changed. |
| [bt\_aics\_status\_cb](group__bt__aics.md#ga044d92a4273c6537a9cdf20922352ed6) | [status](#ac89882943c293e533bec55dd285d7aa0) |
|  | The audio input status has changed. |
| [bt\_aics\_description\_cb](group__bt__aics.md#ga98b142ea7a66de5577c44aa90d507930) | [description](#ad37ae465600fa2e3c1868f0da07fd31a) |
|  | The audio input decscription has changed. |
| [bt\_aics\_discover\_cb](group__bt__aics.md#ga9fda39f8410308e05eb928eeb7267e83) | [discover](#ae946f4b434b485774a3c8ddca5d86898) |
|  | The discovery has completed. |
| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) | [set\_gain](#a1f13bdcfbfac65800f9e66dad48c3b78) |
|  | The set gain operation has completed. |
| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) | [unmute](#a80c8abd842706d2588e6a075cba61ba8) |
|  | The unmute operation has completed. |
| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) | [mute](#a41b6cac6ccc0195921d2e5a127d9091d) |
|  | The mut operation has completed. |
| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) | [set\_manual\_mode](#a1b54464a8c6df54993914da97da2f93d) |
|  | The set manual mode operation has completed. |
| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) | [set\_auto\_mode](#aac9dccf825f5aa423212af4af3d4ca38) |
|  | The set automatic mode has completed. |

## Detailed Description

Struct to hold callbacks for the Audio Input Control Service.

Used by both clients and servers

## Field Documentation

## [◆ ](#ad37ae465600fa2e3c1868f0da07fd31a)description

| [bt\_aics\_description\_cb](group__bt__aics.md#ga98b142ea7a66de5577c44aa90d507930) bt\_aics\_cb::description |
| --- |

The audio input decscription has changed.

## [◆ ](#ae946f4b434b485774a3c8ddca5d86898)discover

| [bt\_aics\_discover\_cb](group__bt__aics.md#ga9fda39f8410308e05eb928eeb7267e83) bt\_aics\_cb::discover |
| --- |

The discovery has completed.

## [◆ ](#a6b2f2a43d0a91abcecfe8372b6a1be4b)gain\_setting

| [bt\_aics\_gain\_setting\_cb](group__bt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb) bt\_aics\_cb::gain\_setting |
| --- |

The gain setting has changed.

## [◆ ](#a41b6cac6ccc0195921d2e5a127d9091d)mute

| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) bt\_aics\_cb::mute |
| --- |

The mut operation has completed.

## [◆ ](#aac9dccf825f5aa423212af4af3d4ca38)set\_auto\_mode

| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) bt\_aics\_cb::set\_auto\_mode |
| --- |

The set automatic mode has completed.

## [◆ ](#a1f13bdcfbfac65800f9e66dad48c3b78)set\_gain

| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) bt\_aics\_cb::set\_gain |
| --- |

The set gain operation has completed.

## [◆ ](#a1b54464a8c6df54993914da97da2f93d)set\_manual\_mode

| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) bt\_aics\_cb::set\_manual\_mode |
| --- |

The set manual mode operation has completed.

## [◆ ](#a70d099bec6407e5c92f6a4e8d6c44929)state

| [bt\_aics\_state\_cb](group__bt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f) bt\_aics\_cb::state |
| --- |

The audio input state has changed.

## [◆ ](#ac89882943c293e533bec55dd285d7aa0)status

| [bt\_aics\_status\_cb](group__bt__aics.md#ga044d92a4273c6537a9cdf20922352ed6) bt\_aics\_cb::status |
| --- |

The audio input status has changed.

## [◆ ](#a41bc7a97e28c53772573d99a38e8ac55)type

| [bt\_aics\_type\_cb](group__bt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5) bt\_aics\_cb::type |
| --- |

The audio input type has changed.

## [◆ ](#a80c8abd842706d2588e6a075cba61ba8)unmute

| [bt\_aics\_write\_cb](group__bt__aics.md#ga36991fe1dee5168db618518d094d80ef) bt\_aics\_cb::unmute |
| --- |

The unmute operation has completed.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[aics.h](aics_8h_source.md)

- [bt\_aics\_cb](structbt__aics__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
