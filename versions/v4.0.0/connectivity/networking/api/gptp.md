---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/gptp.html
original_path: connectivity/networking/api/gptp.html
---

# generic Precision Time Protocol (gPTP)

## [Overview](#id1)

This gPTP stack supports the protocol and procedures as defined in
the [IEEE 802.1AS-2011 standard](https://standards.ieee.org/findstds/standard/802.1AS-2011.html) (Timing and Synchronization for
Time-Sensitive Applications in Bridged Local Area Networks).

## [Supported features](#id2)

The stack handles communications and state machines defined in the
[IEEE 802.1AS-2011 standard](https://standards.ieee.org/findstds/standard/802.1AS-2011.html). Mandatory requirements for a full-duplex
point-to-point link endpoint, as defined in Annex A of the standard,
are supported.

The stack is in principle capable of handling communications on multiple network
interfaces (also defined as “ports” in the standard) and thus act as
a 802.1AS bridge. However, this mode of operation has not been validated on
the Zephyr OS.

## [Supported hardware](#id3)

Although the stack itself is hardware independent, Ethernet frame timestamping
support must be enabled in ethernet drivers.

Boards supported:

- [FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f)
- [Nucleo H743ZI](../../../boards/st/nucleo_h743zi/doc/index.md#nucleo_h743zi)
- [Nucleo H745ZI-Q](../../../boards/st/nucleo_h745zi_q/doc/index.md#nucleo_h745zi_q)
- [Nucleo F767ZI](../../../boards/st/nucleo_f767zi/doc/index.md#nucleo_f767zi)
- [SAM E70(B) Xplained](../../../boards/atmel/sam/sam_e70_xplained/doc/index.md#sam_e70_xplained)
- [Native simulator - native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) (only usable for simple testing, limited capabilities
  due to lack of hardware clock)
- [QEMU Emulation for X86](../../../boards/qemu/x86/doc/index.md#qemu_x86) (emulated, limited capabilities due to lack of hardware clock)

## [Enabling the stack](#id4)

The following configuration option must me enabled in `prj.conf` file.

- [`CONFIG_NET_GPTP`](../../../kconfig.md#CONFIG_NET_GPTP "CONFIG_NET_GPTP")

## [Application interfaces](#id5)

The following Application Interfaces as defined in section 9 of the standard
are available:

- `ClockSourceTime` interface ([`gptp_clk_src_time_invoke()`](../../../doxygen/html/group__gptp.md#ga9b27c9a741fb0ca72eff78e334e629fe))
- `ClockTargetPhaseDiscontinuity` interface ([`gptp_register_phase_dis_cb()`](../../../doxygen/html/group__gptp.md#gaad2282df9cbf7f05f557285323af8f07))
- `ClockTargetEventCapture` interface ([`gptp_event_capture()`](../../../doxygen/html/group__gptp.md#ga9a8e2ccf20d0430b4e62f3302462c6eb))

## [Testing](#id6)

The stack has been informally tested using the
[OpenAVnu gPTP](https://github.com/AVnu/gptp) and
[Linux ptp4l](http://linuxptp.sourceforge.net/) daemons.
The [gPTP sample application](../../../samples/net/gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.") from the Zephyr
source distribution can be used for testing.

## [API Reference](#id7)

[gPTP support](../../../doxygen/html/group__gptp.md)

Related code samples

- [gPTP](../../../samples/net/gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.")Enable gPTP support and monitor functionality using net-shell.
