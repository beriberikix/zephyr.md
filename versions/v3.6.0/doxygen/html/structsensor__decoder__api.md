---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensor__decoder__api.html
original_path: doxygen/html/structsensor__decoder__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| int(\* | [get\_frame\_count](#ac8344c7849c9a7084788192fb4f691fc) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channel\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count) |
|  | Get the number of frames in the current buffer. |
| int(\* | [get\_size\_info](#a67db53773d768b160fb74ab72affee14) )(enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
|  | Get the size required to decode a given channel. |
| int(\* | [decode](#a6c910d525374987ae68da10d75f9766e) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channel\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out) |
|  | Decode up to `max_count` samples from the buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [has\_trigger](#a78706bae0f1314615b5804736ef43493) )(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger) |
|  | Check if the given trigger type is present. |

## Detailed Description

Decodes a single raw data buffer.

Data buffers are provided on the [RTIO](group__rtio.md "RTIO") context that's supplied to [sensor\_read](group__sensor__interface.md#ga385feca2a8b65cb6a24443a5d903ca8b "sensor_read").

## Field Documentation

## [◆ ](#a6c910d525374987ae68da10d75f9766e)decode

| int(\* sensor\_decoder\_api::decode) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channel\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out) |
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

**Definition** sensor.h:117

Parameters
:   | [in] | buffer | The buffer provided on the [RTIO](group__rtio.md "RTIO") context |
    | --- | --- | --- |
    | [in] | channel | The channel to decode |
    | [in] | channel\_idx | The index of the channel |
    | [in,out] | fit | The current frame iterator |
    | [in] | max\_count | The maximum number of channels to decode. |
    | [out] | data\_out | The decoded data |

Returns
:   0 no more samples to decode
:   >0 the number of decoded frames
:   <0 on error

## [◆ ](#ac8344c7849c9a7084788192fb4f691fc)get\_frame\_count

| int(\* sensor\_decoder\_api::get\_frame\_count) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channel\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count) |
| --- |

Get the number of frames in the current buffer.

Parameters
:   | [in] | buffer | The buffer provided on the [RTIO](group__rtio.md "RTIO") context. |
    | --- | --- | --- |
    | [in] | channel | The channel to get the count for |
    | [in] | channel\_idx | The index of the channel |
    | [out] | frame\_count | The number of frames on the buffer (at least 1) |

Returns
:   0 on success
:   -ENOTSUP if the channel/channel\_idx aren't found

## [◆ ](#a67db53773d768b160fb74ab72affee14)get\_size\_info

| int(\* sensor\_decoder\_api::get\_size\_info) (enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*frame\_size) |
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
