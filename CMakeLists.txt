########################################################
# cmake file for building a Marlin Package
# @author Karol Krizka
CMAKE_MINIMUM_REQUIRED(VERSION 3.15 FATAL_ERROR)
########################################################

# project name
PROJECT( TemplatePackage )

# project version
SET( ${PROJECT_NAME}_VERSION_MAJOR 0 )
SET( ${PROJECT_NAME}_VERSION_MINOR 0 )
SET( ${PROJECT_NAME}_VERSION_PATCH 1 )

### DEPENDENCIES ############################################################

FIND_PACKAGE( ILCUTIL REQUIRED COMPONENTS ILCSOFT_CMAKE_MODULES )

FIND_PACKAGE( Marlin 1.0 REQUIRED ) # minimum required Marlin version

FIND_PACKAGE( ROOT REQUIRED) ## COMPONENTS Hist)

FIND_PACKAGE( RAIDA REQUIRED )

### DOCUMENTATION ###########################################################

OPTION( INSTALL_DOC "Set to OFF to skip build/install Documentation" OFF )

IF( INSTALL_DOC AND EXISTS "${PROJECT_SOURCE_DIR}/doc/CMakeLists.txt" )
    ADD_SUBDIRECTORY( ./doc )
ENDIF()

### DATA ###########################################################

### LIBRARY #################################################################

# Main library with Processors
ADD_LIBRARY(TemplatePackage SHARED
  ./src/TemplateProcessor.cxx
  )
TARGET_INCLUDE_DIRECTORIES(TemplatePackage
  PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}
  PRIVATE
  ${Marlin_INCLUDE_DIRS}
  ${RAIDA_INCLUDE_DIRS}
  ${ROOT_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES(TemplatePackage
  PRIVATE
  ${RAIDA_LIBRARIES}
  ROOT::Hist
  ${ROOT_LIBRARIES} 
  )
TARGET_COMPILE_DEFINITIONS(TemplatePackage
  PRIVATE
  ${RAIDA_DEFINITIONS})
