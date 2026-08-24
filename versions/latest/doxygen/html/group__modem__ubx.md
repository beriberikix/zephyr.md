---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__modem__ubx.html
original_path: doxygen/html/group__modem__ubx.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem Ubx

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem Ubx.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [modem\_ubx\_match](structmodem__ubx__match.md) |
| struct | [modem\_ubx\_script](structmodem__ubx__script.md) |
| struct | [modem\_ubx](structmodem__ubx.md) |
| struct | [modem\_ubx\_config](structmodem__ubx__config.md) |

| Macros | |
| --- | --- |
| #define | [MODEM\_UBX\_MATCH\_ARRAY\_DEFINE](#ga8a37614e3a9cf6d4773b9e74de79d340)(\_name, ...) |
| #define | [MODEM\_UBX\_MATCH\_DEFINE](#ga4c04f643a1ea9f0fc940d286713be30e)(\_class\_id, \_msg\_id, \_handler) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_ubx\_match\_callback](#gae0bfe22e7e8d7d38ae9f41648f7fcfda)) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [ubx\_frame](structubx__frame.md) \*frame, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*user\_data) |

| Functions | |
| --- | --- |
| int | [modem\_ubx\_attach](#ga4e459f955e34c9059702c3d7f9794948) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe) |
|  | Attach pipe to Modem Ubx. |
| void | [modem\_ubx\_release](#ga68210f4afd5880c532d82fd0bac1d933) (struct [modem\_ubx](structmodem__ubx.md) \*ubx) |
|  | Release pipe from Modem Ubx instance. |
| int | [modem\_ubx\_init](#gaf49363fb4decb4656566b508a061212f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config) |
|  | Initialize Modem Ubx instance. |
| int | [modem\_ubx\_run\_script](#ga770650b055fd597f000a1d4f9daaf712) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script) |
|  | Writes the ubx frame in script.request and reads back its response (if available). |
| int | [modem\_ubx\_run\_script\_for\_each](#ga0fd0def90f6304e679c4123e3c8d0c3f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script, struct [ubx\_frame](structubx__frame.md) \*array, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) array\_size) |

## Detailed Description

Modem Ubx.

## Macro Definition Documentation

## [◆ ](#ga8a37614e3a9cf6d4773b9e74de79d340)MODEM\_UBX\_MATCH\_ARRAY\_DEFINE

| #define MODEM\_UBX\_MATCH\_ARRAY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

**Value:**

struct [modem\_ubx\_match](structmodem__ubx__match.md) \_name[] = {\_\_VA\_ARGS\_\_};

[modem\_ubx\_match](structmodem__ubx__match.md)

**Definition** ubx.h:37

## [◆ ](#ga4c04f643a1ea9f0fc940d286713be30e)MODEM\_UBX\_MATCH\_DEFINE

| #define MODEM\_UBX\_MATCH\_DEFINE | ( |  | *\_class\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_msg\_id*, |
|  |  |  | *\_handler* ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

**Value:**

{ \

.filter = { \

.class = \_class\_id, \

.id = \_msg\_id, \

}, \

.handler = \_handler, \

}

## Typedef Documentation

## [◆ ](#gae0bfe22e7e8d7d38ae9f41648f7fcfda)modem\_ubx\_match\_callback

| typedef void(\* modem\_ubx\_match\_callback) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [ubx\_frame](structubx__frame.md) \*frame, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*user\_data) |
| --- |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

## Function Documentation

## [◆ ](#ga4e459f955e34c9059702c3d7f9794948)modem\_ubx\_attach()

| int modem\_ubx\_attach | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | struct modem\_pipe \* | *pipe* ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

Attach pipe to Modem Ubx.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |
    | pipe | Pipe instance to attach Modem Ubx instance to |

Returns
:   0 if successful
:   negative errno code if failure

Note
:   Modem Ubx instance is enabled if successful

## [◆ ](#gaf49363fb4decb4656566b508a061212f)modem\_ubx\_init()

| int modem\_ubx\_init | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_ubx\_config](structmodem__ubx__config.md) \* | *config* ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

Initialize Modem Ubx instance.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |
    | config | Configuration which shall be applied to the Modem Ubx instance |

Note
:   Modem Ubx instance must be attached to a pipe instance

## [◆ ](#ga68210f4afd5880c532d82fd0bac1d933)modem\_ubx\_release()

| void modem\_ubx\_release | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

Release pipe from Modem Ubx instance.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |

## [◆ ](#ga770650b055fd597f000a1d4f9daaf712)modem\_ubx\_run\_script()

| int modem\_ubx\_run\_script | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | struct [modem\_ubx\_script](structmodem__ubx__script.md) \* | *script* ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

Writes the ubx frame in script.request and reads back its response (if available).

For each ubx frame sent, the device responds in 0, 1 or both of the following ways:

1. The device sends back a UBX-ACK frame to denote 'acknowledge' and 'not-acknowledge'. Note: the message id of UBX-ACK frame determines whether the device acknowledged. Ex: when we send a UBX-CFG frame, the device responds with a UBX-ACK frame.
2. The device sends back the same frame that we sent to it, with it's payload populated. It's used to get the current configuration corresponding to the frame that we sent. Ex: frame types such as "get" or "poll" ubx frames respond this way. This response (if received) is written to script.response.

This function writes the ubx frame in script.request then reads back it's response. If script.match is not NULL, then every ubx frame received from the device is compared with script.match to check if a match occurred. This could be used to match UBX-ACK frame sent from the device by populating script.match with UBX-ACK that the script expects to receive.

The script terminates when either of the following happens:

1. script.match is successfully received and matched.
2. timeout (denoted by script.timeout) occurs.

   Parameters
   :   | ubx | Modem Ubx instance |
       | --- | --- |
       | script | Script to be executed |

   Note
   :   The length of ubx frame in the script.request should not exceed UBX\_FRAME\_SZ\_MAX
   :   Modem Ubx instance must be attached to a pipe instance

   Returns
   :   0 if successful
   :   negative errno code if failure

## [◆ ](#ga0fd0def90f6304e679c4123e3c8d0c3f)modem\_ubx\_run\_script\_for\_each()

| int modem\_ubx\_run\_script\_for\_each | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | struct [modem\_ubx\_script](structmodem__ubx__script.md) \* | *script*, |
|  |  | struct [ubx\_frame](structubx__frame.md) \* | *array*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *array\_size* ) |

`#include <[zephyr/modem/ubx.h](ubx_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
