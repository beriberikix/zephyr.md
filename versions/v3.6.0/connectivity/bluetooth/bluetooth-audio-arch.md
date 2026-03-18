---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/bluetooth-audio-arch.html
original_path: connectivity/bluetooth/bluetooth-audio-arch.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Audio Architecture

![Bluetooth Audio Architecture](../../_images/ble_audio_arch.svg)

Bluetooth Audio Architecture

## Generic Audio Framework (GAF)

The Generic Audio Framework (GAF) is considered the middleware of the Bluetooth
LE Audio architecture. The GAF contains the profiles and services that allows
higher layer applications and profiles to set up streams, change volume, control
media and telephony and more. The GAF builds on GATT, GAP and isochronous
channels (ISO).

GAF uses GAP to connect, advertise and synchronize to other devices.
GAF uses GATT to configure streams, associate streams with content
(e.g. media or telephony), control volume and more.
GAF uses ISO for the audio streams themselves, both as unicast (connected)
audio streams or broadcast (unconnected) audio streams.

GAF mandates the use of the LC3 codec, but also supports other codecs.

![Generic Audio Framework](../../_images/gaf.svg)

Generic Audio Framework

The top-level profiles TMAP and HAP are not part of the GAF, but rather provide
top-level requirements for how to use the GAF.

GAF has been implemented in Zephyr with the following structure.

![Generic Audio Framework](../../_images/zephyr_gaf.svg)

Zephyr Generic Audio Framework

### Bluetooth Audio Stack Status

The following table shows the current status and support of the profiles in the
Bluetooth Audio Stack.

Bluetooth Audio Profile status

| Module | Role | Version | Added in Release | Status | Remaining |
| --- | --- | --- | --- | --- | --- |
| VCP | Volume Renderer | 1.0 | 2.6 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Volume Controller | 1.0 | 2.6 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| MICP | Microphone Device | 1.0 | 2.7 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Microphone Controller | 1.0 | 2.7 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| CSIP | Set Member | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Set Coordinator | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| CCP | Call Control Server | 1.0 | 3.0 | - Feature complete - Shell Module - BSIM test | - API refactor - Sample Application |
| Call Control Client | 1.0 | 3.0 | - Feature complete - Shell Module - BSIM test | - API refactor - Sample Application |
| MCP | Media Control Server | 1.0 | 3.0 | - Feature complete - Shell Module - BSIM test | - API refactor - Support for multiple instances and connections - Sample Application |
| Media Control Client | 1.0 | 3.0 | - Feature complete - Shell Module - BSIM test | - API refactor - Sample Application |
| BAP | Unicast Server | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Unicast Client | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Broadcast Source | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Broadcast Sink | 1.0.1 | 3.0 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Scan Delegator | 1.0.1 | 3.3 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Broadcast Assistant | 1.0.1 | 3.3 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| CAP | Acceptor | 1.0 | 3.2 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Initiator | 1.0 | 3.3 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Commander |  |  | - WIP | - Feature complete - Shell Module - BSIM test - Sample Application |
| HAP | Hearing Aid | 1.0 | 3.1 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Hearing Aid Unicast Client | 1.0 | 3.1 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Hearing Aid Remote Controller |  |  | - WIP | - Feature complete - Shell Module - BSIM test - Sample Application |
| TMAP | Call Gateway | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Call Terminal | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Unicast Media Sender | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Unicast Media Receiver | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Broadcast Media Sender | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Broadcast Media Receiver | 1.0 | 3.4 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| PBP | Public Broadcast Source |  | 3.5 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Public Broadcast Sink |  | 3.5 | - Feature complete - Shell Module - BSIM test - Sample Application |  |
| Public Broadcast Assistant |  |  |  | - Feature complete - Shell Module - BSIM test - Sample Application |
| GMAP | Unicast Game Gateway |  | 3.5 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Unicast Game Terminal |  | 3.5 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Broadcast Game Sender |  | 3.5 | - Feature complete - Shell Module - BSIM test | - Sample Application |
| Broadcast Game Receiver |  | 3.5 | - Feature complete - Shell Module - BSIM test | - Sample Application |

### Using the Bluetooth Audio Stack

To use any of the profiles in the Bluetooth Audio Stack, including the top-level
profiles outside of GAF, [`CONFIG_BT_AUDIO`](../../kconfig.md#CONFIG_BT_AUDIO "CONFIG_BT_AUDIO") shall be enabled.
This Kconfig option allows the enabling of the individual profiles inside of the
Bluetooth Audio Stack. Each profile can generally be enabled on its own, but
enabling higher-layer profiles (such as CAP, TMAP and HAP) will typically
require enabling some of the lower layer profiles.

It is, however, possible to create a device that uses e.g. only Stream Control
(with just the BAP), without using any of the content control or
rendering/capture control profiles, or vice versa. Using the higher layer
profiles will however typically provide a better user experience and better
interoperability with other devices.

#### Common Audio Profile (CAP)

The Common Audio Profile introduces restrictions and requirements on the lower layer profiles.
The procedures in CAP works on one or more streams for one or more devices. Is it thus possible via
CAP to do a single function call to setup multiple streams across multiple devices.

The figure below shows a complete structure of the procedures in CAP and
how they correspond to procedures from the other profiles. The circles with I, A and C show whether
the procedure has active involvement or requirements from the CAP Initiator, CAP Accept and CAP
Commander roles respectively.

![Common Audio Profile Procedures](../../_images/cap_proc.svg)

Common Audio Profile Procedures

The API reference for CAP can be found in [Common Audio Profile](api/cap.md#bluetooth-cap).

#### Stream Control (BAP)

Stream control is implemented by the Basic Audio Profile. This profile
defines multiple roles:

- Unicast Client
- Unicast Server
- Broadcast Source
- Broadcast Sink
- Scan Delegator (not yet implemented)
- Broadcast assistant (not yet implemented)

Each role can be enabled individually, and it is possible to support more than
one role.

The API reference for stream control can be found in
[Bluetooth Audio](api/audio.md#bluetooth-audio).

#### Rendering and Capture Control

Rendering and capture control is implemented by the Volume Control Profile
(VCP) and Microphone Control Profile (MICP).

The VCP implementation supports the following roles

- Volume Control Service (VCS) Server
- Volume Control Service (VCS) Client

The MICP implementation supports the following roles

- Microphone Control Profile (MICP) Microphone Device (server)
- Microphone Control Profile (MICP) Microphone Controller (client)

The API reference for volume control can be found in
[Bluetooth Volume Control](api/volume.md#bluetooth-volume).

The API reference for Microphone Control can be found in
[Bluetooth Microphone Control](api/microphone.md#bluetooth-microphone).

#### Content Control

Content control is implemented by the Call Control Profile (CCP) and
Media Control Profile (MCP).

The CCP implementation is not yet implemented in Zephyr.

The MCP implementation supports the following roles

- Media Control Service (MCS) Server via the Media Proxy module
- Media Control Client (MCC)

The API reference for media control can be found in
[Bluetooth Media Control](api/media.md#bluetooth-media).

#### Coordinated Sets

Coordinated Sets is implemented by the Coordinated Sets Identification Profile
(CSIP).

The CSIP implementation supports the following roles

- Coordinated Set Identification Service (CSIP) Set Member
- Coordinated Set Identification Service (CSIP) Set Coordinator

The API reference for media control can be found in
[Bluetooth Coordinated Sets](api/coordinated_sets.md#bluetooth-coordinated-sets).
