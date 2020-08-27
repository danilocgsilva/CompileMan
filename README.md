# CompileMan

Works with PHP and node for frontend compilations. Are you working with a PHP project with modern frontend (e.g Laravel, Symphony with node)?

Type "`cman`" to compile assets and run project. Type "`cman`" again to clean up the things, so you can commit to the repository.

Type "`cman compile`" or "`cman clean`" if eventually the script miss in detecting your project state.

In a near future **dotnet projects also will be embraced**.

## Installing

Go to the root project folder and type in the command line:
```
pip install .
```

## Usage

Go to the command line
```
cman compile|clean
```

This projects actually works only to the following projects:

* php
* node (only for frontend assets compilation in web application)
