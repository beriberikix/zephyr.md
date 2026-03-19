---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/stepper/tmc50xx/README.html
original_path: samples/drivers/stepper/tmc50xx/README.html
---

# TMC50XX stepper

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/stepper/tmc50xx/README.rst/..)

## Description

This sample application periodically spins the stepper clockwise and counterclockwise depending on
the `CONFIG_PING_PONG_N_REV` configuration.

## References

> - TMC5041: [https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5041\_datasheet\_rev1.16.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5041_datasheet_rev1.16.pdf)
> - TMC5072: [https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5072\_datasheet\_rev1.26.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5072_datasheet_rev1.26.pdf)

## Wiring

This sample uses the TMC5072 BOB controlled using the SPI interface. The board’s Devicetree must define
a `stepper` alias for the stepper motor node.

## Building and Running

This project spins the stepper and outputs the events to the console. It requires an TMC50XX stepper
driver. It should work with any platform featuring a SPI peripheral interface.
It does not work on QEMU.

```shell
# From the root of the zephyr repository
west build -b nucleo_g071rb samples/drivers/stepper/tmc50xx
west flash
```

### Sample Output

```shell
Starting tmc50xx stepper sample
stepper is 0x8007240, name is tmc_stepper@0
stepper_callback steps completed changing direction
stepper_callback steps completed changing direction
stepper_callback steps completed changing direction
```

<repeats endlessly>

## See also

[Stepper Driver Interface](../../../../doxygen/html/group__stepper__interface.md)
