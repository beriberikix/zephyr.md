---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/peci/README.html
original_path: samples/drivers/peci/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PECI interface

## Overview

This sample demonstrates how to use the [PECI API](../../../hardware/peripherals/peci.md#peci-api).
Callbacks are registered that will write to the console indicating PECI events.
These events indicate PECI host interaction.

## Building and Running

The sample can be built and executed on boards supporting PECI.
Please connect ensure the microcontroller used is connected to a PECI Host
in order to execute.

### Sample output

```shell
PECI test
Note: You are expected to see several interactions including ID and
temperature retrieval.
```
