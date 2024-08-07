# Template Marlin Processor

A template Marlin package with a skeleton processor. It contains the following:

* A template structure for organizing your code.
* A CMakeLists.txt for compilation.
* A skeleton processor that you can modify.

Note that official Marlin packages follow a slightly different template. This is because they are based on old CMake conventions. The template documented here has been updated for modern CMake.

## Compiling
Start by making a fork or directly cloning the template repository.

```bash
git clone https://github.com/MuonColliderSoft/TemplatePackage.git
```

The package can be compiled by loading the Muon Collider software environment and compiling as any CMake package.

```
# cmake -S TemplatePackage -B build
cmake -S TemplatePackage -B build
cmake --build build
```

## Running
The software environment needs to be informed of the location of the library containing your processor. It loads all libraries specified by the MARLIN_DLL environmental variable.

The following command will update the variable and call Marlin with the provided example steering file.

```bash
export MARLIN_DLL=$(realpath build/libTemplatePackage.so):${MARLIN_DLL}
k4run TemplatePackage/share/example.py --LcioEvent.Files output_reco.slcio
```

## Modifying
The processor is implemented inside the src/TemplateProcessor.cxx, with the header located in TemplatePackage/TemplateProcessor.hxx.

The class implements the following functions:

* `init()`: Called at the start of Marlin execution.
* `processRunHeader()`: Called at start of a file.
* `processEvent()`: Called for each event.
* `end()`: Called at the end.
```

Parameters are declared inside the class constructor using the following template:

```c++
registerProcessorParameter("MinPt", // Name of the parameter
                           "Minimum particle pT.", // Description
                           _minPt, // Variable that will contain the parameter
                           _minPt); // Default value
```
Parameters that correspond to input and output collections are defined slightly differently.

To define a parameter containing an input collection name:

```c++
registerInputCollection( LCIO::MCPARTICLE,
                         "InputCollectionName" ,
                         "Name of an input collection.",
                         _inputCollectionName,
                         _inputCollectionName
                         );
```			 
To define a parameter containing an output collection name:

```c++
registerOutputCollection( LCIO::MCPARTICLE,
                          "OutputCollectionName" ,
                          "Name of the output collection" ,
                          _outputCollectionName,
                          _outputCollectionName
                          );
```

## Advanced topics

If you need to manage multiple packages, a simple workspace template is available at [TemplateWorkspace](https://github.com/MuonColliderSoft/TemplateWorkspace). More information is contained in the `README.md` file of the repository, but in a nutshell allows to automatically recognize packages clones (preferably as git submodule) inside the packages folder, providws a simple top `CMakeLists.txt` file to compile them all and a `setup.sh` script to modify automatically the `MARLIN_DLL` environmental variable correctly.
