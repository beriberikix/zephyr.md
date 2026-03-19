---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/design.html
original_path: build/dts/design.html
---

# Design goals

Zephyr’s use of devicetree has evolved significantly over time, and further
changes are expected. The following are the general design goals, along with
specific examples about how they impact Zephyr’s source code, and areas where
more work remains to be done.

## Single source for hardware information

Zephyr’s built-in device drivers and sample applications shall obtain
configurable hardware descriptions from devicetree.

### Examples

- New device drivers shall use devicetree APIs to determine which [devices
  to create](howtos.md#dt-create-devices).
- In-tree sample applications shall use [aliases](intro-syntax-structure.md#dt-alias-chosen) to
  determine which of multiple possible generic devices of a given type will be
  used in the current build. For example, the [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample uses this to
  determine the LED to blink.
- Boot-time pin muxing and pin control for new SoCs shall be accomplished via a
  devicetree-based pinctrl driver

### Example remaining work

- Zephyr’s [Test Runner (Twister)](../../develop/test/twister.md#twister-script) currently use `board.yaml` files to
  determine the hardware supported by a board. This should be obtained from
  devicetree instead.
- Legacy device drivers currently use Kconfig to determine which instances of a
  particular compatible are enabled. This can and should be done with devicetree
  overlays instead.
- Board-level documentation still contains tables of hardware support which are
  generated and maintained by hand. This can and should be obtained from the
  board level devicetree instead.
- Runtime determination of `struct device` relationships should be done using
  information obtained from devicetree, e.g. for device power management.

## Source compatibility with other operating systems

Zephyr’s devicetree tooling is based on a generic layer which is interoperable
with other devicetree users, such as the Linux kernel.

Zephyr’s binding language *semantics* can support Zephyr-specific attributes,
but shall not express Zephyr-specific relationships.

### Examples

- Zephyr’s devicetree source parser, [dtlib.py](intro-input-output.md#dt-scripts), is
  source-compatible with other tools like [dtc](https://git.kernel.org/pub/scm/utils/dtc/dtc.git/about/) in both directions:
  `dtlib.py` can parse `dtc` output, and `dtc` can parse
  `dtlib.py` output.
- Zephyr’s “extended dtlib” library, `edtlib.py`, shall not include
  Zephyr-specific features. Its purpose is to provide a higher-level view of the
  devicetree for common elements like interrupts and buses.

  Only the high-level `gen_defines.py` script, which is built on top of
  `edtlib.py`, contains Zephyr-specific knowledge and features.

### Example remaining work

- Zephyr has a custom [Devicetree bindings](bindings.md#dt-bindings) language *syntax*. While Linux’s
  dtschema does not yet meet Zephyr’s needs, we should try to follow what it is
  capable of representing in Zephyr’s own bindings.
- Due to inflexibility in the bindings language, Zephyr cannot support the full
  set of bindings supported by Linux.
- Devicetree source sharing between Zephyr and Linux is not done.
