# MRI Quality Assurance 

Software for performing UCLH Medical Physics MRI Quality Assurance (QA) protocols on DICOM images. Protocols are defined in the SOPS MPB 138 (Image Handling) and MPB 139 (Image Analysis).

## Installation
This installation has been tested using python 3.6 in Windows and Linux environments.
```
python setup.py install
```

## Usage

### mriqa
Wrapper script for the MRI QA software modules. Passes command line arguments to the relevant modules. Used by the graphical user interface to run the software.
```
usage: mriqa [-h] module args

optional arguments:
  module          name of MRI quality assurance module to run: [all, rename, uniformity]
  args            command line arguments to be passed to downstream module
      -i indir    directory containing DICOM files 
      -c config   config file with regular expressions for validating DICOM Series Description
  -h, --help  show this help message and exit
  -v          show program's version number and exit
```

### graphical user interface
The GUI is invoked by calling `mriqagui` from the command line.

## Modules

### rename
Rename DICOM images by validating strings in the DICOM Series Description tag.
```
usage: mriqa rename [-h] -i indir -c config [-v]
```

### uniformity
Calculate the fractional uniformity of ROI profiles. Input directory must have been processed by `mriqa rename`. 
```
usage: mriqa uniformity [-h] -i indir -c config [-v]
```

## Development
This package was developed using **setuptools**.  Use `pip install -e .` to track changes in local scripts during development.

### Updating the GUI
The gui is called by the script 'mriqa/gui.py' and launched by the command `mriqagui`. This GUI is a wrapper for the main `mriqa` command line module. 

### Updating the default config file
The config file found in 'data/config.ini' contains configuration settings for different modules. To update the settings, such as filename search strings, edit this file and repeat the installation step.

### Adding new modules
Scripts can be added to the package in a modular fashion. These new modules should be placed in the 'mriqa/' directory and contain a main function that takes the command line arguments (as *args* in `mriqa.py`):
```
def main(args):
    ....
```
The script should then be imported in `mriqa.py` and added to its **MODULES** list. The GUI can then be updated to include tickboxes for the new script options. 

### TODO
* Add more appropriate logging statements and write to output file.
* Create Windows .exe launcher
