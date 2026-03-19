---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__radio__api.html
original_path: doxygen/html/structieee802154__radio__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_radio\_api Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

IEEE 802.15.4 driver interface API.
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#aa955462d8c6950dc4b5935973f4575d8) |
|  | network interface API |
| enum [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4)(\* | [get\_capabilities](#a09a4b5df81822845f718952c6029442c) )(const struct [device](structdevice.md) \*dev) |
|  | Get the device driver capabilities. |
| int(\* | [cca](#a2cbbd0e64fae28f748bb3e4d654a92bf) )(const struct [device](structdevice.md) \*dev) |
|  | Clear Channel Assessment - Check channel's activity. |
| int(\* | [set\_channel](#a9ad27a2ff0a839dc5b9a4e6317cc59b1) )(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) channel) |
|  | Set current channel. |
| int(\* | [filter](#aa9502e0e014a8d05ffe235567e8c98f3) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) set, enum [ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) type, const struct [ieee802154\_filter](structieee802154__filter.md) \*filter) |
|  | Set/Unset PAN ID, extended or short address filters. |
| int(\* | [set\_txpower](#aeeab6dfcde08af23357ea40f8af68f66) )(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) dbm) |
|  | Set TX power level in dbm. |
| int(\* | [tx](#a70139acec22642c1fc09f2323c383fe6) )(const struct [device](structdevice.md) \*dev, enum [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) mode, struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Transmit a packet fragment as a single frame. |
| int(\* | [start](#a0e4d57dc3a53299ddedf2140e172103d) )(const struct [device](structdevice.md) \*dev) |
|  | Start the device. |
| int(\* | [stop](#a75cfcfe2b9e69c2e4af53f00c8294b36) )(const struct [device](structdevice.md) \*dev) |
|  | Stop the device. |
| int(\* | [configure](#a9acaf4810bd5d3b026cc381bff301071) )(const struct [device](structdevice.md) \*dev, enum [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) type, const struct [ieee802154\_config](structieee802154__config.md) \*config) |
|  | Set or update driver configuration. |
| int(\* | [ed\_scan](#a01fc17f85f2be33877a9347f59a84c54) )(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration, [energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5) done\_cb) |
|  | Run an energy detection scan. |
| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)(\* | [get\_time](#a829a0d59fdcda5b6cb029ef1334a6b8b) )(const struct [device](structdevice.md) \*dev) |
|  | Get the current time in nanoseconds relative to the network subsystem's local uptime clock as represented by this network interface. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [get\_sch\_acc](#ae4a3ef40a5b8031c868d72ead163c97d) )(const struct [device](structdevice.md) \*dev) |
|  | Get the current estimated worst case accuracy (maximum ± deviation from the nominal frequency) of the network subsystem's local clock used to calculate tolerances and guard times when scheduling delayed receive or transmit radio operations. |
| int(\* | [attr\_get](#a0b3e0ed1385dd428c861e08c79849ef4) )(const struct [device](structdevice.md) \*dev, enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) attr, struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value) |
|  | Get the value of a driver specific attribute. |

## Detailed Description

IEEE 802.15.4 driver interface API.

Note
:   This structure is called "radio" API for backwards compatibility. A better name would be "IEEE 802.15.4 driver API" as typical drivers will not only implement L1/radio (PHY) features but also L2 (MAC) features if the vendor-specific driver hardware or firmware offers offloading opportunities.

While L1-level driver features are exclusively implemented by drivers and MAY be mandatory to support certain application requirements, L2 features SHOULD be optional by default and only need to be implemented for performance optimization or precise timing as deemed necessary by driver maintainers. Fallback implementations ("Soft MAC") SHOULD be provided in the driver-independent L2 layer for all L2/MAC features especially if these features are not implemented in vendor hardware/firmware by a majority of existing in-tree drivers. If, however, a driver offers offloading opportunities then L2 implementations SHALL delegate performance critical or resource intensive tasks to the driver.

All drivers SHALL support two externally observable interface operational states: "UP" and "DOWN". Drivers MAY additionally support a "TESTING" interface state (see continuous\_carrier()).

The following rules apply:

- An interface is considered "UP" when it is able to transmit and receive packets, "DOWN" otherwise (see precise definitions of the corresponding ifOperStatus values in RFC 2863, section 3.1.14, [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9 "net_if_oper_state") and the continuous\_carrier() exception below). A device that has its receiver temporarily disabled during "UP" state due to an active receive window configuration is still considered "UP".
- Upper layers will assume that the interface managed by the driver is "UP" after a call to [start()](#a0e4d57dc3a53299ddedf2140e172103d) returned zero or -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4 "Operation already in progress."). Upper layers assume that the interface is "DOWN" after calling [stop()](#a75cfcfe2b9e69c2e4af53f00c8294b36) returned zero or -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4 "Operation already in progress.").
- The driver SHALL block [start()](#a0e4d57dc3a53299ddedf2140e172103d)/[stop()](#a75cfcfe2b9e69c2e4af53f00c8294b36) calls until the interface fully transitioned to the new state (e.g. the receiver is operational, ongoing transmissions were finished, etc.). Drivers SHOULD yield the calling thread (i.e. "sleep") if waiting for the new state without CPU interaction is possible.
- Drivers are responsible of guaranteeing atomicity of state changes. Appropriate means of synchronization SHALL be implemented (locking, atomic flags, ...).
- While the interface is "DOWN", the driver SHALL be placed in the lowest possible power state. The driver MAY return from a call to [stop()](#a75cfcfe2b9e69c2e4af53f00c8294b36) before it reaches the lowest possible power state, i.e. manage power asynchronously. While the interface is "UP", the driver SHOULD autonomously and asynchronously transition to lower power states whenever possible. If the driver claims to support timed RX/TX capabilities and the upper layers configure an RX slot, then the driver SHALL immediately transition (asynchronously) to the lowest possible power state until the start of the RX slot or until a scheduled packet needs to be transmitted.
- The driver SHALL NOT change the interface's "UP"/"DOWN" state on its own. Initially, the interface SHALL be in the "DOWN" state.
- Drivers that implement the optional continuous\_carrier() operation will be considered to be in the RFC 2863 "testing" ifOperStatus state if that operation returns zero. This state is active until either [start()](#a0e4d57dc3a53299ddedf2140e172103d) or [stop()](#a75cfcfe2b9e69c2e4af53f00c8294b36) is called. If continuous\_carrier() returns a non-zero value then the previous state is assumed by upper layers.
- If calls to [start()](#a0e4d57dc3a53299ddedf2140e172103d)/[stop()](#a75cfcfe2b9e69c2e4af53f00c8294b36) return any other value than zero or -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4 "Operation already in progress."), upper layers will consider the interface to be in a "lowerLayerDown" state as defined in RFC 2863.
- The RFC 2863 "dormant", "unknown" and "notPresent" ifOperStatus states are currently not supported. The "lowerLevelUp" state.
- The [ed\_scan()](#a01fc17f85f2be33877a9347f59a84c54), [cca()](#a2cbbd0e64fae28f748bb3e4d654a92bf) and [tx()](#a70139acec22642c1fc09f2323c383fe6) operations SHALL only be supported in the "UP" state and return -[ENETDOWN](group__system__errno.md#gaac51995026fa19cdd0ad84a272304af0 "Network is down.") in any other state. See the function-level API documentation below for further details.

Note
:   In case of devices that support timed RX/TX, the "UP" state is not equal to "receiver enabled". If a receive window (i.e. RX slot, see [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6 "IEEE802154_CONFIG_RX_SLOT")) is configured before calling [start()](#a0e4d57dc3a53299ddedf2140e172103d) then the receiver will not be enabled when transitioning to the "UP" state. Configuring a receive window while the interface is "UP" will cause the receiver to be disabled immediately until the configured reception time has arrived.

## Field Documentation

## [◆ ](#a0b3e0ed1385dd428c861e08c79849ef4)attr\_get

| int(\* ieee802154\_radio\_api::attr\_get) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430) attr, struct [ieee802154\_attr\_value](structieee802154__attr__value.md) \*value) |
| --- |

Get the value of a driver specific attribute.

Note
:   This function SHALL NOT return any values configurable by the MAC (L2) layer. It is reserved to non-boolean (i.e. scalar or structured) attributes that originate from the driver implementation and cannot be directly or indirectly derived by L2. Boolean attributes SHALL be implemented as [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4 "ieee802154_hw_caps").
:   Implementations SHALL be **isr-ok** and MUST NOT **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Return values
:   | 0 | The requested attribute is supported by the driver and the value can be retrieved from the corresponding [ieee802154\_attr\_value](structieee802154__attr__value.md "ieee802154_attr_value") member. |
    | --- | --- |
    | -ENOENT | The driver does not provide the requested attribute. The value structure has not been updated with attribute data. The content of the value attribute is undefined. |

## [◆ ](#a2cbbd0e64fae28f748bb3e4d654a92bf)cca

| int(\* ieee802154\_radio\_api::cca) (const struct [device](structdevice.md) \*dev) |
| --- |

Clear Channel Assessment - Check channel's activity.

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. SHALL return -ENETDOWN unless the interface is "UP".

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Return values
:   | 0 | the channel is available |
    | --- | --- |
    | -EBUSY | The channel is busy. |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -ENETDOWN | The interface is not "UP". |
    | -ENOTSUP | CCA is not supported by this driver. |
    | -EIO | The CCA procedure could not be executed. |

## [◆ ](#a9acaf4810bd5d3b026cc381bff301071)configure

| int(\* ieee802154\_radio\_api::configure) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09) type, const struct [ieee802154\_config](structieee802154__config.md) \*config) |
| --- |

Set or update driver configuration.

The method blocks until the interface has been reconfigured atomically with respect to ongoing package reception, transmission or any other ongoing driver operation.

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready"). Some configuration options may not be supported in all interface operational states, see the detailed specifications in [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09 "ieee802154_config_type"). In this case the operation returns -[EACCES](group__system__errno.md#gac2a2e9fa555401f94478f74e01868032 "Permission denied.").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | type | the configuration type to be set |
    | config | the configuration parameters to be set for the given configuration type |

Return values
:   | 0 | configuration successful |
    | --- | --- |
    | -EINVAL | The configuration parameters are invalid for the given configuration type. |
    | -ENOTSUP | The given configuration type is not supported by this driver. |
    | -EACCES | The given configuration type is supported by this driver but cannot be configured in the current interface operational state. |
    | -ENOMEM | The configuration cannot be saved due to missing memory resources. |
    | -ENOENT | The resource referenced in the configuration parameters cannot be found in the configuration. |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -EIO | An internal error occurred while trying to configure the given configuration parameter. |

## [◆ ](#a01fc17f85f2be33877a9347f59a84c54)ed\_scan

| int(\* ieee802154\_radio\_api::ed\_scan) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration, [energy\_scan\_done\_cb\_t](group__ieee802154__driver.md#ga8c9ab3cecefe641a25f003eb6d014fc5) done\_cb) |
| --- |

Run an energy detection scan.

Note
:   requires IEEE802154\_HW\_ENERGY\_SCAN capability
:   The radio channel must be set prior to calling this function.
:   Implementations SHALL be **isr-ok** and MAY **sleep**. SHALL return -[ENETDOWN](group__system__errno.md#gaac51995026fa19cdd0ad84a272304af0 "Network is down.") unless the interface is "UP".

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | duration | duration of energy scan in ms |
    | done\_cb | function called when the energy scan has finished |

Return values
:   | 0 | the energy detection scan was successfully scheduled |
    | --- | --- |
    | -EBUSY | the energy detection scan could not be scheduled at this time |
    | -EALREADY | a previous energy detection scan has not finished yet. |
    | -ENETDOWN | The interface is not "UP". |
    | -ENOTSUP | This driver does not support energy scans. |
    | -EIO | The energy detection procedure could not be executed. |

## [◆ ](#aa9502e0e014a8d05ffe235567e8c98f3)filter

| int(\* ieee802154\_radio\_api::filter) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) set, enum [ieee802154\_filter\_type](group__ieee802154__driver.md#gaa1971591e72866d0f3f0d4db2931e25a) type, const struct [ieee802154\_filter](structieee802154__filter.md) \*filter) |
| --- |

Set/Unset PAN ID, extended or short address filters.

Note
:   requires IEEE802154\_HW\_FILTER capability.
:   Implementations SHALL be **isr-ok** and MAY **sleep**. SHALL return -EIO unless the interface is either "UP" or "DOWN".

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | set | true to set the filter, false to remove it |
    | type | the type of entity to be added/removed from the filter list (a PAN ID or a source/destination address) |
    | [filter](#aa9502e0e014a8d05ffe235567e8c98f3) | the entity to be added/removed from the filter list |

Return values
:   | 0 | The filter was successfully added/removed. |
    | --- | --- |
    | -EINVAL | The given filter entity or filter entity type was not valid. |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -ENOTSUP | Setting/removing this filter or filter type is not supported by this driver. |
    | -EIO | Error while setting/removing the filter. |

## [◆ ](#a09a4b5df81822845f718952c6029442c)get\_capabilities

| enum [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4)(\* ieee802154\_radio\_api::get\_capabilities) (const struct [device](structdevice.md) \*dev) |
| --- |

Get the device driver capabilities.

Note
:   Implementations SHALL be **isr-ok** and MUST NOT **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Returns
:   Bit field with all supported device driver capabilities.

## [◆ ](#ae4a3ef40a5b8031c868d72ead163c97d)get\_sch\_acc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* ieee802154\_radio\_api::get\_sch\_acc) (const struct [device](structdevice.md) \*dev) |
| --- |

Get the current estimated worst case accuracy (maximum ± deviation from the nominal frequency) of the network subsystem's local clock used to calculate tolerances and guard times when scheduling delayed receive or transmit radio operations.

The deviation is given in units of PPM (parts per million).

Note
:   requires IEEE802154\_HW\_TXTIME and/or IEEE802154\_HW\_RXTIME capabilities.
:   Implementations may estimate this value based on current operating conditions (e.g. temperature). Implementations SHALL be **isr-ok** and MUST NOT **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Returns
:   current estimated clock accuracy in PPM

## [◆ ](#a829a0d59fdcda5b6cb029ef1334a6b8b)get\_time

| [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)(\* ieee802154\_radio\_api::get\_time) (const struct [device](structdevice.md) \*dev) |
| --- |

Get the current time in nanoseconds relative to the network subsystem's local uptime clock as represented by this network interface.

See [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "net_time_t") for semantic details.

Note
:   requires IEEE802154\_HW\_TXTIME and/or IEEE802154\_HW\_RXTIME capabilities. Implementations SHALL be **isr-ok** and MUST NOT **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Returns
:   nanoseconds relative to the network subsystem's local clock, -1 if an error occurred or the operation is not supported

## [◆ ](#aa955462d8c6950dc4b5935973f4575d8)iface\_api

| struct net\_if\_api ieee802154\_radio\_api::iface\_api |
| --- |

network interface API

Note
:   Network devices must extend the network interface API. It is therefore mandatory to place it at the top of the driver API struct so that it can be cast to a network interface.

## [◆ ](#a9ad27a2ff0a839dc5b9a4e6317cc59b1)set\_channel

| int(\* ieee802154\_radio\_api::set\_channel) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) channel) |
| --- |

Set current channel.

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. SHALL return -EIO unless the interface is either "UP" or "DOWN".

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | channel | the number of the channel to be set in CPU byte order |

Return values
:   | 0 | channel was successfully set |
    | --- | --- |
    | -EALREADY | The previous channel is the same as the requested channel. |
    | -EINVAL | The given channel is not within the range of valid channels of the driver's current channel page, see the IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES driver attribute. |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -ENOTSUP | The given channel is within the range of valid channels of the driver's current channel page but unsupported by the current driver. |
    | -EIO | The channel could not be set. |

## [◆ ](#aeeab6dfcde08af23357ea40f8af68f66)set\_txpower

| int(\* ieee802154\_radio\_api::set\_txpower) (const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) dbm) |
| --- |

Set TX power level in dbm.

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. SHALL return -EIO unless the interface is either "UP" or "DOWN".

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | dbm | TX power in dbm |

Return values
:   | 0 | The TX power was successfully set. |
    | --- | --- |
    | -EINVAL | The given dbm value is invalid or not supported by the driver. |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -EIO | The TX power could not be set. |

## [◆ ](#a0e4d57dc3a53299ddedf2140e172103d)start

| int(\* ieee802154\_radio\_api::start) (const struct [device](structdevice.md) \*dev) |
| --- |

Start the device.

Upper layers will assume the interface is "UP" if this operation returns with zero or -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4 "Operation already in progress."). The interface is placed in receive mode before returning from this operation unless an RX slot has been configured (even if it lies in the past, see [IEEE802154\_CONFIG\_RX\_SLOT](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6 "IEEE802154_CONFIG_RX_SLOT")).

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Return values
:   | 0 | The driver was successfully started. |
    | --- | --- |
    | -EALREADY | The driver was already "UP". |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -EIO | The driver could not be started. |

## [◆ ](#a75cfcfe2b9e69c2e4af53f00c8294b36)stop

| int(\* ieee802154\_radio\_api::stop) (const struct [device](structdevice.md) \*dev) |
| --- |

Stop the device.

Upper layers will assume the interface is "DOWN" if this operation returns with zero or -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4 "Operation already in progress."). The driver switches off the receiver before returning if it was previously on. The driver enters the lowest possible power mode after this operation is called. This MAY happen asynchronously (i.e. after the operation already returned control).

Note
:   Implementations SHALL be **isr-ok** and MAY **sleep**. MAY be called in any interface state once the driver is fully initialized ("ready").

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |

Return values
:   | 0 | The driver was successfully stopped. |
    | --- | --- |
    | -EWOULDBLOCK | The operation is called from ISR context but temporarily cannot be executed without blocking. |
    | -EALREADY | The driver was already "DOWN". |
    | -EIO | The driver could not be stopped. |

## [◆ ](#a70139acec22642c1fc09f2323c383fe6)tx

| int(\* ieee802154\_radio\_api::tx) (const struct [device](structdevice.md) \*dev, enum [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d) mode, struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag) |
| --- |

Transmit a packet fragment as a single frame.

Depending on the level of offloading features supported by the driver, the frame MAY not be fully encrypted/authenticated or it MAY not contain an FCS. It is the responsibility of L2 implementations to prepare the frame according to the offloading capabilities announced by the driver and to decide whether CCA, CSMA/CA, ACK or retransmission procedures need to be executed outside ("soft MAC") or inside ("hard MAC") the driver .

All frames originating from L2 SHALL have all required IEs pre-allocated and pre-filled such that the driver does not have to parse and manipulate IEs at all. This includes ACK packets if the driver does not have the [IEEE802154\_HW\_RX\_TX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03 "IEEE802154_HW_RX_TX_ACK") capability. Also see [IEEE802154\_CONFIG\_ENH\_ACK\_HEADER\_IE](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907 "IEEE802154_CONFIG_ENH_ACK_HEADER_IE") for drivers that have the [IEEE802154\_HW\_RX\_TX\_ACK](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03 "IEEE802154_HW_RX_TX_ACK") capability.

IEs that cannot be prepared by L2 unless the TX time is known (e.g. CSL IE, Rendezvous Time IE, Time Correction IE, ...) SHALL be sent in any of the timed TX modes with appropriate timing information pre-filled in the IE such that drivers do not have to parse and manipulate IEs at all unless the frame is generated by the driver itself.

In case any of the timed TX modes is supported and used (see [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4 "ieee802154_hw_caps") and [ieee802154\_tx\_mode](group__ieee802154__driver.md#gab2bee8752291e082cb277145cef1225d "ieee802154_tx_mode")), the driver SHALL take responsibility of scheduling and sending the packet at the precise programmed time autonomously without further interaction by upper layers. The call to [tx()](#a70139acec22642c1fc09f2323c383fe6) will block until the package has either been sent successfully (possibly including channel acquisition and packet acknowledgment) or a terminal transmission error occurred. The driver SHALL sleep and keep power consumption to the lowest possible level until the scheduled transmission time arrives or during any other idle waiting time.

Warning
:   The driver SHALL NOT take ownership of the given network packet and frame (fragment) buffer. Any data required by the driver including the actual frame content must be read synchronously and copied internally if needed at a later time (e.g. the contents of IEs required for protocol configuration, states of frame counters, sequence numbers, etc). Both, the packet and the buffer MAY be re-used or released by upper layers immediately after the function returns.

Note
:   Implementations MAY **sleep** and will usually NOT be **isr-ok** - especially when timed TX, CSMA/CA, retransmissions, auto-ACK or any other offloading feature is supported that implies considerable idle waiting time. SHALL return -[ENETDOWN](group__system__errno.md#gaac51995026fa19cdd0ad84a272304af0 "Network is down.") unless the interface is "UP".
:   The transmission occurs on the radio channel set by the call to [set\_channel()](#a9ad27a2ff0a839dc5b9a4e6317cc59b1). However, if the CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL is set and the driver has the capability [IEEE802154\_HW\_SELECTIVE\_TXCHANNEL](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e "Support for timed transmissions on selective channel.") then the transmissions requested with mode IEEE802154\_TX\_MODE\_TXTIME or [IEEE802154\_TX\_MODE\_TXTIME\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e "Transmit packet in the future, perform CCA before transmission.") SHALL use the radio channel returned by net\_pkt\_ieee802154\_txchannel() to transmit the packet and receive an ACK on that channel if the frame requested it. After the operation the driver should return to the channel set previously by [set\_channel()](#a9ad27a2ff0a839dc5b9a4e6317cc59b1) call. It is responsibility of an upper layer to set the required radio channel for the packet by a call to net\_pkt\_set\_ieee802154\_txchannel(). This feature allows CSL transmissions as stated in IEEE 802.15.4-2020 chapter 6.12.2.7 CSL over multiple channels. This feature allows to perform a switch of the radio channel as late as possible before transmission without interrupting possible reception that could occur if separate [set\_channel()](#a9ad27a2ff0a839dc5b9a4e6317cc59b1) was called.

Parameters
:   | dev | pointer to IEEE 802.15.4 driver device |
    | --- | --- |
    | mode | the transmission mode, some of which require specific offloading capabilities. |
    | pkt | pointer to the network packet to be transmitted. |
    | frag | pointer to a network buffer containing a single fragment with the frame data to be transmitted |

Return values
:   | 0 | The frame was successfully sent or scheduled. If the driver supports ACK offloading and the frame requested acknowledgment (AR bit set), this means that the packet was successfully acknowledged by its peer. |
    | --- | --- |
    | -EINVAL | Invalid packet (e.g. an expected IE is missing or the encryption/authentication state is not as expected). |
    | -EBUSY | The frame could not be sent because the medium was busy (CSMA/CA or CCA offloading feature only). |
    | -ENOMSG | The frame was not confirmed by an ACK packet (TX ACK offloading feature only) or the received ACK packet was invalid. |
    | -ENOBUFS | The frame could not be scheduled due to missing internal resources (timed TX offloading feature only). |
    | -ENETDOWN | The interface is not "UP". |
    | -ENOTSUP | The given TX mode is not supported. |
    | -EIO | The frame could not be sent due to some unspecified driver error (e.g. the driver being busy). |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_radio\_api](structieee802154__radio__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
