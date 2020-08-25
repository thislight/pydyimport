# Changelog

## v0.0.1-alpha.1
* (`DynamicImport`) new `env_injector` option to set up a environment injector in `DynamicImport`'s constructor, which accept a callable that recvice path as `str` and code as `str`, return a dict which contains fields set to global.
* (`DynamicImport`) new `inject_require` option in `DynamicImport`'s constructor, set True to inject `require*` functions to imported modules.
* (`RequireEnvInjector`) a new environment injector to inject `require*` functions to modules.
* (`DynamicImport`) global cache now set `False` as default (`global_cache=False`).
* (`DynamicImport`) new `cache` option which can set up a instance-scoped cache, default is `True`.
* (`DynamicImport.load_module_content_from`) remove decorator `staticmethod`
* (`DynamicImport.load_module_content_from`) fix: variables decalred in document-level could not be access by deeper variable scope. (commit `798f9671c8784639097ca1b127f3b7fc2412524d`)

## V0.0.1-alpha.0
* initial version
