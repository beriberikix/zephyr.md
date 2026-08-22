---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/sca/coverity.html
original_path: develop/sca/coverity.html
---

# Coverity

Coverity Scan is a service by which Black Duck provides the results of analysis
on open source coding projects to open source code developers that have
registered their products with Coverity Scan.

This integration was only tested with scan.coverity.com and the tool
distribution available through this service.

## Generating Build Data Files

To use this integration, coverity tool distribution must be found in your [`PATH`](../env_vars.md#envvar-PATH) environment and
[west build](../west/build-flash-debug.md#west-building) should be called with a `-DZEPHYR_SCA_VARIANT=coverity`
parameter, e.g.

```shell
west build -b qemu_cortex_m3 samples/hello_world -- -DZEPHYR_SCA_VARIANT=coverity
```

Results of the scan will be generated as `build/sca/coverity`.

You can also set `COVERITY_OUTPUT_DIR` as the destination for multiple
and incremental scan results.

## Result Analysis

Follow the instructions on [http://scan.coverity.com](http://scan.coverity.com) for uploading results.
