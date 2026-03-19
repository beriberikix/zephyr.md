---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/tcpc.html
original_path: hardware/peripherals/tcpc.html
---

# USB Type-C Port Controller (TCPC)

## Overview

[TCPC](https://www.usb.org/document-library/usb-type-cr-port-controller-interface-specification) (USB Type-C Port Controller)
The TCPC is a device used to simplify the implementation of a USB-C system
by providing the following three function:

- VBUS and VCONN control [USB Type-C](https://www.usb.org/document-library/usb-type-cr-cable-and-connector-specification-revision-21):
  The TCPC may provide a Source device, the mechanism to control VBUS sourcing,
  and a Sink device, the mechanism to control VBUS sinking. A similar mechanism
  is provided for the control of VCONN.
- CC control and sensing:
  The TCPC implements logic for controlling the CC pin pull-up and pull-down
  resistors. It also provides a way to sense and report what resistors are
  present on the CC pin.
- Power Delivery message reception and transmission [USB Power Delivery](https://www.usb.org/document-library/usb-power-delivery):
  The TCPC sends and receives messages constructed in the TCPM and places them
  on the CC lines.

### TCPC API

The TCPC device driver functions as the liaison between the TCPC device and the
application software; this is accomplished by the Zephyr’s API provided by the
device driver that’s used to communicate with and control the TCPC device.

## Configuration Options

Related configuration options:

- [`CONFIG_USBC_TCPC_DRIVER`](../../kconfig.md#CONFIG_USBC_TCPC_DRIVER "CONFIG_USBC_TCPC_DRIVER")

## API Reference

[USB Type-C](../../doxygen/html/group__usb__type__c.md)

[USB Type-C Port Controller API](../../doxygen/html/group__usb__type__c__port__controller__api.md)

[USB Power Delivery](../../doxygen/html/group__usb__power__delivery.md)
