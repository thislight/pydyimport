# PyDyImport
Dynamically import python file to aviod mess when you are using a different structure from python suggested.

## Usage
````python
from pydyimport import DynamicImport
require = DynamicImport(__file__).require

mod = require("path/to/file.py")
````

## License
GNU GENERAL PUBLIC LICENSE, version 3 or later.
````
    PyDyImport - dynamically importing and avoid mess in python
    Copyright (C) 2020 thisLight

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
````
