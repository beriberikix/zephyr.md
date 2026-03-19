---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/common/opensda-debug.html
original_path: boards/nxp/common/opensda-debug.html
---

A debug probe is used for both flashing and debugging the board. This board has
an [OpenSDA Onboard Debug Probe](../../../develop/flash_debug/probes.md#opensda-onboard-debug-probe). The default firmware present on this
probe is the [OpenSDA DAPLink Onboard Debug Probe](../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe).

Based on the host tool installed, please use the following instructions
to setup your debug probe:

- [J-Link Debug Host Tools](../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools): [Using J-Link on NXP OpenSDA Boards](#using-j-link-on-nxp-opensda-boards)
- [LinkServer Debug Host Tools](../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools): [Using DAPLink on NXP OpenSDA Boards](#using-daplink-on-nxp-opensda-boards)
- [pyOCD Debug Host Tools](../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools): [Using DAPLink on NXP OpenSDA Boards](#using-daplink-on-nxp-opensda-boards)

# Using DAPLink on NXP OpenSDA Boards

1. If the debug firmware has been modified, follow the instructions provided at
   [OpenSDA DAPLink Onboard Debug Probe](../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are populated

# Using J-Link on NXP OpenSDA Boards

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or a [J-Link External Debug Probe](../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
board.

To update the onboard debug circuit, please do the following:

1. If the debug firmware has been modified, follow the instructions provided at
   [OpenSDA J-Link Onboard Debug Probe](../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are removed.

To attach an external J-Link probe, ensure the SWD isolation jumpers are
removed, and connect the external probe to the JTAG/SWD header.
