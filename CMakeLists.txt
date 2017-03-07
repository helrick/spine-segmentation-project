cmake_minimum_required(VERSION 2.8.9)

project(SpineSeg)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/SpineSeg")
set(EXTENSION_CATEGORY "Spine")
set(EXTENSION_CONTRIBUTORS ", Hannah Greer, Hillary Elrick")
set(EXTENSION_DESCRIPTION "For CISC 472, Final Project")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SpineSeg.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SpineSeg/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SpineSeg)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
