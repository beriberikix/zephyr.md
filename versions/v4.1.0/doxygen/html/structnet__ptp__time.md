---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__ptp__time.html
original_path: doxygen/html/structnet__ptp__time.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_ptp\_time Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PTP time](group__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.
[More...](#details)

`#include <[ptp_time.h](ptp__time_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [second](#a8d61359ca53147d2da761edeb9e1ab04) |  |
|  | Second value. [More...](#a8d61359ca53147d2da761edeb9e1ab04) |
| }; |  |
|  | Seconds encoded on 48 bits. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nanosecond](#a31af3f0b8f924336c17585ee1b15ee0e) |
|  | Nanoseconds. |

## Detailed Description

(Generalized) Precision Time Protocol Timestamp format.

This structure represents a timestamp according to the Precision Time Protocol standard ("PTP", IEEE 1588, section 5.3.3), the Generalized Precision Time Protocol standard ("gPTP", IEEE 802.1AS, section 6.4.3.4), or any other well-defined context in which precision structured timestamps are required on network messages in Zephyr.

Seconds are encoded as a 48 bits unsigned integer. Nanoseconds are encoded as a 32 bits unsigned integer.

In the context of (g)PTP, *timestamps* designate the time, relative to a local clock ("LocalClock") at which the message timestamp point passes a reference plane marking the boundary between the PTP Instance and the network medium (IEEE 1855, section 7.3.4.2; IEEE 802.1AS, section 8.4.3).

The exact definitions of the *message timestamp point* and *reference plane* depends on the network medium and use case.

For (g)PTP the media-specific message timestamp points and reference planes are defined in the standard. In non-PTP contexts specific to Zephyr, timestamps are measured relative to the same local clock but with a context-specific message timestamp point and reference plane, defined below per use case.

A *"LocalClock"* is a freerunning clock, embedded into a well-defined entity (e.g. a PTP Instance) and provides a common time to that entity relative to an arbitrary epoch (IEEE 1855, section 3.1.26, IEEE 802.1AS, section 3.16).

In Zephyr, the local clock is usually any instance of a kernel system clock driver, counter driver, RTC API driver or low-level counter/timer peripheral (e.g. an ethernet peripheral with hardware timestamp support or a radio timer) with sufficient precision for the context in which it is used.

See IEEE 802.1AS, Annex B for specific performance requirements regarding conformance of local clocks in the gPTP context. See IEEE 1588, Annex A, section A5.4 for general performance requirements regarding PTP local clocks. See IEEE 802.15.4-2020, section 15.7 for requirements in the context of ranging applications and ibid., section 6.7.6 for the relation between guard times and clock accuracy which again influence the precision required for subprotocols like CSL, TSCH, RIT, etc.

Applications that use timestamps across different subsystems or media must ensure that they understand the definition of the respective reference planes and interpret timestamps accordingly. Applications must further ensure that timestamps are either all referenced to the same local clock or convert between clocks based on sufficiently precise conversion algorithms.

Timestamps may be measured on ingress (RX timestamps) or egress (TX timestamps) of network messages. Timestamps can also be used to schedule a network message to a well-defined point in time in the future at which it is to be sent over the medium (timed TX). A future timestamp and a duration, both referenced to the local clock, may be given to specify a time window at which a network device should expect incoming messages (RX window).

In Zephyr this timestamp structure is currently used in the following contexts:

- gPTP for Full Duplex Point-to-Point IEEE 802.3 links (IEEE 802.1AS, section 11): the reference plane and message timestamp points are as defined in the standard.
- IEEE 802.15.4 timed TX and RX: Timestamps designate the point in time at which the end of the last symbol of the start-of-frame delimiter (SFD) (or equivalently, the start of the first symbol of the PHY header) is at the local antenna. The standard also refers to this as the "RMARKER" (IEEE 802.15.4-2020, section 6.9.1) or "symbol boundary" (ibid., section 6.5.2), depending on the context. In the context of beacon timestamps, the difference between the timestamp measurement plane and the reference plane is defined by the MAC PIB attribute "macSyncSymbolOffset", ibid., section 8.4.3.1, table 8-94.

If further use cases are added to Zephyr using this timestamp structure, their clock performance requirements, message timestamp points and reference plane definition SHALL be added to the above list.

## Field Documentation

## [◆ ](#a9ef6ab971069f9ea8fb55a27d7dacd99)[union]

| union { ... } [net\_ptp\_time](structnet__ptp__time.md) |
| --- |

Seconds encoded on 48 bits.

## [◆ ](#a31af3f0b8f924336c17585ee1b15ee0e)nanosecond

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_ptp\_time::nanosecond |
| --- |

Nanoseconds.

## [◆ ](#a8d61359ca53147d2da761edeb9e1ab04)second

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_ptp\_time::second |
| --- |

Second value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ptp\_time.h](ptp__time_8h_source.md)

- [net\_ptp\_time](structnet__ptp__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
