---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/led.html
original_path: hardware/peripherals/led.html
---

# Light-Emitting Diode (LED)

## Overview

The LED API provides access to Light Emitting Diodes, both in individual and
strip form.

## Configuration Options

Related configuration options:

- [`CONFIG_LED`](../../kconfig.md#CONFIG_LED "CONFIG_LED")
- [`CONFIG_LED_STRIP`](../../kconfig.md#CONFIG_LED_STRIP "CONFIG_LED_STRIP")

## API Reference

### LED

[LED Interface](../../doxygen/html/group__led__interface.md)

Related code samples

- [Breathing-blinking LED (BBLED)](../../samples/drivers/led/xec/README.md#led-xec "Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.")Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.
- [HT16K33 LED driver with keyscan](../../samples/drivers/ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.
- [IS31FL3194 RGB LED](../../samples/drivers/led/is31fl3194/README.md#is31fl3194 "Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.")Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.
- [IS31FL3216A LED](../../samples/drivers/led/is31fl3216a/README.md#is31fl3216a "Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.")Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.
- [IS31FL3733 LED Matrix](../../samples/drivers/led/is31fl3733/README.md#is31fl3733 "Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.")Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.
- [LED PWM](../../samples/drivers/led/pwm/README.md#led-pwm "Control PWM LEDs using the LED API.")Control PWM LEDs using the LED API.
- [LP3943 RGBW LED](../../samples/drivers/led/lp3943/README.md#lp3943 "Control up to 16 RGBW LEDs connected to an LP3943 driver chip.")Control up to 16 RGBW LEDs connected to an LP3943 driver chip.
- [LP50XX RGB LED](../../samples/drivers/led/lp50xx/README.md#lp50xx "Control up to 12 RGB LEDs connected to an LP50xx driver chip.")Control up to 12 RGB LEDs connected to an LP50xx driver chip.
- [LP5562 RGB LED](../../samples/drivers/led/lp5562/README.md#lp5562 "Control 4 RGB LEDs connected to an LP5562 driver chip.")Control 4 RGB LEDs connected to an LP5562 driver chip.
- [LP5569 9-channel LED controller](../../samples/drivers/led/lp5569/README.md#lp5569 "Control 9 LEDs connected to an LP5569 driver chip.")Control 9 LEDs connected to an LP5569 driver chip.
- [PCA9633 LED](../../samples/drivers/led/pca9633/README.md#pca9633 "Control 4 LEDs connected to a PCA9633 driver chip.")Control 4 LEDs connected to a PCA9633 driver chip.
- [SX1509B RGB LED](../../samples/drivers/led/sx1509b_intensity/README.md#sx1509b "Control an RGB LED connected to an SX1509B driver chip.")Control an RGB LED connected to an SX1509B driver chip.

### LED Strip

[LED Strip Interface](../../doxygen/html/group__led__strip__interface.md)

Related code samples

- [LED strip](../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.")Control an LED strip.
