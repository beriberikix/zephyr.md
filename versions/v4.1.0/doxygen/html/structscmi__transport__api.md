---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structscmi__transport__api.html
original_path: doxygen/html/structscmi__transport__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_transport\_api Struct Reference

`#include <[transport.h](transport_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#a2d90efd745ef78a07482c51a5748fef4) )(const struct [device](structdevice.md) \*transport) |
| int(\* | [send\_message](#a7946a4f860d706d7e0f132aaf532662e) )(const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
| int(\* | [setup\_chan](#a452deceb4eb343b19adf720eae7fb602) )(const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |
| int(\* | [read\_message](#a8cc80f631a74b7cf253140fa1a7707d9) )(const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [channel\_is\_free](#a52c33e80eda1ac892d2e04e3692ced58) )(const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan) |
| struct [scmi\_channel](structscmi__channel.md) \*(\* | [request\_channel](#a517cb99fc369eec024d4a4acf66865e3) )(const struct [device](structdevice.md) \*transport, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) proto, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |

## Field Documentation

## [◆ ](#a52c33e80eda1ac892d2e04e3692ced58)channel\_is\_free

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* scmi\_transport\_api::channel\_is\_free) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan) |
| --- |

## [◆ ](#a2d90efd745ef78a07482c51a5748fef4)init

| int(\* scmi\_transport\_api::init) (const struct [device](structdevice.md) \*transport) |
| --- |

## [◆ ](#a8cc80f631a74b7cf253140fa1a7707d9)read\_message

| int(\* scmi\_transport\_api::read\_message) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
| --- |

## [◆ ](#a517cb99fc369eec024d4a4acf66865e3)request\_channel

| struct [scmi\_channel](structscmi__channel.md) \*(\* scmi\_transport\_api::request\_channel) (const struct [device](structdevice.md) \*transport, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) proto, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |
| --- |

## [◆ ](#a7946a4f860d706d7e0f132aaf532662e)send\_message

| int(\* scmi\_transport\_api::send\_message) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
| --- |

## [◆ ](#a452deceb4eb343b19adf720eae7fb602)setup\_chan

| int(\* scmi\_transport\_api::setup\_chan) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/[transport.h](transport_8h_source.md)

- [scmi\_transport\_api](structscmi__transport__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
