---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__decoder__api.html
original_path: doxygen/html/structsensor__decoder__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_decoder\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

Decodes a single raw data buffer.
[More...](#details)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [get\_frame\_count](#a16c0b0f1a3a13d037b9ffcbf348da1f5) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count) |
|  | Get the number of frames in the current buffer. |
| int(\* | [get\_size\_info](#a026be8086386e9eea0a1cb25c1cd602e) )(struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
|  | Get the size required to decode a given channel. |
| int(\* | [decode](#a1d24e69b5c2f0c41ce175de2aa2618db) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out) |
|  | Decode up to `max_count` samples from the buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [has\_trigger](#a78706bae0f1314615b5804736ef43493) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger) |
|  | Check if the given trigger type is present. |

## Detailed Description

Decodes a single raw data buffer.

Data buffers are provided on the [RTIO](group__rtio.md "RTIO") context that's supplied to [sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976 "sensor_read").

## Field Documentation

## [◆ ](#a1d24e69b5c2f0c41ce175de2aa2618db)decode

| int(\* sensor\_decoder\_api::decode) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out) |
| --- |

Decode up to `max_count` samples from the buffer.

Decode samples of channel [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934 "sensor_channel") across multiple frames. If there exist multiple instances of the same channel, `channel_index` is used to differentiate them. As an example, assume a sensor provides 2 distance measurements:

// Decode the first channel instance of 'distance'

decoder->decode(buffer, [SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08), 0, &fit, 5, out);

...

// Decode the second channel instance of 'distance'

decoder->decode(buffer, [SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08), 1, &fit, 5, out);

[SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)

@ SENSOR\_CHAN\_DISTANCE

Distance.

**Definition** sensor.h:119

Parameters
:   | [in] | buffer | The buffer provided on the [RTIO](group__rtio.md "RTIO") context |
    | --- | --- | --- |
    | [in] | channel | The channel to decode |
    | [in,out] | fit | The current frame iterator |
    | [in] | max\_count | The maximum number of channels to decode. |
    | [out] | data\_out | The decoded data |

Returns
:   0 no more samples to decode
:   >0 the number of decoded frames
:   <0 on error

## [◆ ](#a16c0b0f1a3a13d037b9ffcbf348da1f5)get\_frame\_count

| int(\* sensor\_decoder\_api::get\_frame\_count) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count) |
| --- |

Get the number of frames in the current buffer.

Parameters
:   | [in] | buffer | The buffer provided on the [RTIO](group__rtio.md "RTIO") context. |
    | --- | --- | --- |
    | [in] | channel | The channel to get the count for |
    | [out] | frame\_count | The number of frames on the buffer (at least 1) |

Returns
:   0 on success
:   -ENOTSUP if the channel/channel\_idx aren't found

## [◆ ](#a026be8086386e9eea0a1cb25c1cd602e)get\_size\_info

| int(\* sensor\_decoder\_api::get\_size\_info) (struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
| --- |

Get the size required to decode a given channel.

When decoding a single frame, use `base_size`. For every additional frame, add another `frame_size`. As an example, to decode 3 frames use: 'base\_size + 2 \* frame\_size'.

Parameters
:   | [in] | channel | The channel to query |
    | --- | --- | --- |
    | [out] | base\_size | The size of decoding the first frame |
    | [out] | frame\_size | The additional size of every additional frame |

Returns
:   0 on success
:   -ENOTSUP if the channel is not supported

## [◆ ](#a78706bae0f1314615b5804736ef43493)has\_trigger

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* sensor\_decoder\_api::has\_trigger) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger) |
| --- |

Check if the given trigger type is present.

Parameters
:   | [in] | buffer | The buffer provided on the [RTIO](group__rtio.md "RTIO") context |
    | --- | --- | --- |
    | [in] | trigger | The trigger type in question |

Returns
:   Whether the trigger is present in the buffer

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_decoder\_api](structsensor__decoder__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
