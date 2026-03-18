---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__zperf.html
original_path: doxygen/html/group__zperf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Zperf API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Data Structures | |
| --- | --- |
| struct | [zperf\_upload\_params](structzperf__upload__params.md) |
| struct | [zperf\_download\_params](structzperf__download__params.md) |
| struct | [zperf\_results](structzperf__results.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b)) (enum [zperf\_status](#ga073cc81d6fd201d09e7d1e712927f7cb) status, struct [zperf\_results](structzperf__results.md) \*result, void \*user\_data) |
|  | Zperf callback function used for asynchronous operations. |

| Enumerations | |
| --- | --- |
| enum | [zperf\_status](#ga073cc81d6fd201d09e7d1e712927f7cb) { [ZPERF\_SESSION\_STARTED](#gga073cc81d6fd201d09e7d1e712927f7cba837674d9cb7309c80bf4dac2446667d8) , [ZPERF\_SESSION\_FINISHED](#gga073cc81d6fd201d09e7d1e712927f7cba230ffe541f46d28b19ce4ed66b5f9607) , [ZPERF\_SESSION\_ERROR](#gga073cc81d6fd201d09e7d1e712927f7cba6e2f47cdc1e2b67eede67a378ee5ed95) } |

| Functions | |
| --- | --- |
| int | [zperf\_udp\_upload](#ga6f2704914a9a577dac119a11f98c0e8e) (const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param, struct [zperf\_results](structzperf__results.md) \*result) |
|  | Synchronous UDP upload operation. |
| int | [zperf\_tcp\_upload](#ga24c061ea0dcd44b94c2ad79dfa264e44) (const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param, struct [zperf\_results](structzperf__results.md) \*result) |
|  | Synchronous TCP upload operation. |
| int | [zperf\_udp\_upload\_async](#gacf57dcebd09cae8ecf61b553baf6b2cd) (const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param, [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Asynchronous UDP upload operation. |
| int | [zperf\_tcp\_upload\_async](#ga07704e0bd701c0f2da2b74b9a83d6b35) (const struct [zperf\_upload\_params](structzperf__upload__params.md) \*param, [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Asynchronous TCP upload operation. |
| int | [zperf\_udp\_download](#gaae9e5669a76da0cde7454bbd7b491a4a) (const struct [zperf\_download\_params](structzperf__download__params.md) \*param, [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Start UDP server. |
| int | [zperf\_tcp\_download](#ga9ac136e27fc87f85ddb66cbd2f78256d) (const struct [zperf\_download\_params](structzperf__download__params.md) \*param, [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) callback, void \*user\_data) |
|  | Start TCP server. |
| int | [zperf\_udp\_download\_stop](#ga394e3a10550cf9d0a435f5d217dfbbdf) (void) |
|  | Stop UDP server. |
| int | [zperf\_tcp\_download\_stop](#gac29193fb02ccb159b7adc3c8de64895a) (void) |
|  | Stop TCP server. |

## Detailed Description

## Typedef Documentation

## [◆ ](#gaffeb2d7cbca61021984e784f7ba4595b)zperf\_callback

| typedef void(\* zperf\_callback) (enum [zperf\_status](#ga073cc81d6fd201d09e7d1e712927f7cb) status, struct [zperf\_results](structzperf__results.md) \*result, void \*user\_data) |
| --- |

`#include <[zperf.h](zperf_8h.md)>`

Zperf callback function used for asynchronous operations.

Parameters
:   | status | Session status. |
    | --- | --- |
    | result | Session results. May be NULL for certain events. |
    | user\_data | A pointer to the user provided data. |

## Enumeration Type Documentation

## [◆ ](#ga073cc81d6fd201d09e7d1e712927f7cb)zperf\_status

| enum [zperf\_status](#ga073cc81d6fd201d09e7d1e712927f7cb) |
| --- |

`#include <[zperf.h](zperf_8h.md)>`

| Enumerator | |
| --- | --- |
| ZPERF\_SESSION\_STARTED |  |
| ZPERF\_SESSION\_FINISHED |  |
| ZPERF\_SESSION\_ERROR |  |

## Function Documentation

## [◆ ](#ga9ac136e27fc87f85ddb66cbd2f78256d)zperf\_tcp\_download()

| int zperf\_tcp\_download | ( | const struct [zperf\_download\_params](structzperf__download__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[zperf.h](zperf_8h.md)>`

Start TCP server.

Note
:   Only one TCP server instance can run at a time.

Parameters
:   | param | Download parameters. |
    | --- | --- |
    | callback | Session results callback. |
    | user\_data | A pointer to the user data to be provided with the callback. |

Returns
:   0 if server was started, a negative error code otherwise.

## [◆ ](#gac29193fb02ccb159b7adc3c8de64895a)zperf\_tcp\_download\_stop()

| int zperf\_tcp\_download\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zperf.h](zperf_8h.md)>`

Stop TCP server.

Returns
:   0 if server was stopped successfully, a negative error code otherwise.

## [◆ ](#ga24c061ea0dcd44b94c2ad79dfa264e44)zperf\_tcp\_upload()

| int zperf\_tcp\_upload | ( | const struct [zperf\_upload\_params](structzperf__upload__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct [zperf\_results](structzperf__results.md) \* | *result* ) |

`#include <[zperf.h](zperf_8h.md)>`

Synchronous TCP upload operation.

The function blocks until the upload is complete.

Parameters
:   | param | Upload parameters. |
    | --- | --- |
    | result | Session results. |

Returns
:   0 if session completed successfully, a negative error code otherwise.

## [◆ ](#ga07704e0bd701c0f2da2b74b9a83d6b35)zperf\_tcp\_upload\_async()

| int zperf\_tcp\_upload\_async | ( | const struct [zperf\_upload\_params](structzperf__upload__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[zperf.h](zperf_8h.md)>`

Asynchronous TCP upload operation.

Note
:   Only one asynchronous upload can be performed at a time.

Parameters
:   | param | Upload parameters. |
    | --- | --- |
    | callback | Session results callback. |
    | user\_data | A pointer to the user data to be provided with the callback. |

Returns
:   0 if session was scheduled successfully, a negative error code otherwise.

## [◆ ](#gaae9e5669a76da0cde7454bbd7b491a4a)zperf\_udp\_download()

| int zperf\_udp\_download | ( | const struct [zperf\_download\_params](structzperf__download__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[zperf.h](zperf_8h.md)>`

Start UDP server.

Note
:   Only one UDP server instance can run at a time.

Parameters
:   | param | Download parameters. |
    | --- | --- |
    | callback | Session results callback. |
    | user\_data | A pointer to the user data to be provided with the callback. |

Returns
:   0 if server was started, a negative error code otherwise.

## [◆ ](#ga394e3a10550cf9d0a435f5d217dfbbdf)zperf\_udp\_download\_stop()

| int zperf\_udp\_download\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zperf.h](zperf_8h.md)>`

Stop UDP server.

Returns
:   0 if server was stopped successfully, a negative error code otherwise.

## [◆ ](#ga6f2704914a9a577dac119a11f98c0e8e)zperf\_udp\_upload()

| int zperf\_udp\_upload | ( | const struct [zperf\_upload\_params](structzperf__upload__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct [zperf\_results](structzperf__results.md) \* | *result* ) |

`#include <[zperf.h](zperf_8h.md)>`

Synchronous UDP upload operation.

The function blocks until the upload is complete.

Parameters
:   | param | Upload parameters. |
    | --- | --- |
    | result | Session results. |

Returns
:   0 if session completed successfully, a negative error code otherwise.

## [◆ ](#gacf57dcebd09cae8ecf61b553baf6b2cd)zperf\_udp\_upload\_async()

| int zperf\_udp\_upload\_async | ( | const struct [zperf\_upload\_params](structzperf__upload__params.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [zperf\_callback](#gaffeb2d7cbca61021984e784f7ba4595b) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[zperf.h](zperf_8h.md)>`

Asynchronous UDP upload operation.

Note
:   Only one asynchronous upload can be performed at a time.

Parameters
:   | param | Upload parameters. |
    | --- | --- |
    | callback | Session results callback. |
    | user\_data | A pointer to the user data to be provided with the callback. |

Returns
:   0 if session was scheduled successfully, a negative error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
