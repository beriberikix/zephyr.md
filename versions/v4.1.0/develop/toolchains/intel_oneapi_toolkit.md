---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/toolchains/intel_oneapi_toolkit.html
original_path: develop/toolchains/intel_oneapi_toolkit.html
---

# Intel oneAPI Toolkit

1. Download [Intel oneAPI Base Toolkit](https://software.intel.com/content/www/us/en/develop/tools/oneapi/all-toolkits.html)
2. Assuming the toolkit is installed in `/opt/intel/oneApi`, set environment
   using:

   ```text
   # Linux, macOS:
   export ONEAPI_TOOLCHAIN_PATH=/opt/intel/oneapi
   source $ONEAPI_TOOLCHAIN_PATH/compiler/latest/env/vars.sh

   # Windows:
   > set ONEAPI_TOOLCHAIN_PATH=C:\Users\Intel\oneapi
   ```

   To setup the complete oneApi environment, use:

   ```text
   source  /opt/intel/oneapi/setvars.sh
   ```

   The above will also change the python environment to the one used by the
   toolchain and might conflict with what Zephyr uses.
3. Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `oneApi`.
