from pydyimport import DynamicImport
require = DynamicImport(__file__, inject_require=True).require

require('mod1.py').hello1()