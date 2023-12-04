# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


set(CPACK_BUILD_SOURCE_DIRS "/home/emre/tutorials/sequence_tut/source;/home/emre/tutorials/sequence_tut/source")
set(CPACK_CMAKE_GENERATOR "Unix Makefiles")
set(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_FILE "/home/emre/bin/cmake/share/cmake-3.27/Templates/CPack.GenericDescription.txt")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_SUMMARY "my_app built using CMake")
set(CPACK_DMG_SLA_USE_RESOURCE_FILE_LICENSE "ON")
set(CPACK_GENERATOR "TXZ")
set(CPACK_INNOSETUP_ARCHITECTURE "x64")
set(CPACK_INSTALL_CMAKE_PROJECTS "/home/emre/tutorials/sequence_tut/source;my_app;ALL;/")
set(CPACK_INSTALL_PREFIX "/usr/local")
set(CPACK_MODULE_PATH "/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-src/build_system")
set(CPACK_NSIS_DISPLAY_NAME "my_app 3.4.0-rc.1")
set(CPACK_NSIS_INSTALLER_ICON_CODE "")
set(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
set(CPACK_NSIS_PACKAGE_NAME "my_app 3.4.0-rc.1")
set(CPACK_NSIS_UNINSTALL_NAME "Uninstall")
set(CPACK_OBJCOPY_EXECUTABLE "/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-objcopy")
set(CPACK_OBJDUMP_EXECUTABLE "/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-objdump")
set(CPACK_OUTPUT_CONFIG_FILE "/home/emre/tutorials/sequence_tut/source/CPackConfig.cmake")
set(CPACK_PACKAGE_CHECKSUM "SHA256")
set(CPACK_PACKAGE_DEFAULT_LOCATION "/")
set(CPACK_PACKAGE_DESCRIPTION_FILE "/home/emre/bin/cmake/share/cmake-3.27/Templates/CPack.GenericDescription.txt")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "my_app built using CMake")
set(CPACK_PACKAGE_FILE_NAME "my_app-3.4.0-rc.1-Linux")
set(CPACK_PACKAGE_ICON "/home/emre/tutorials/sequence_tut/seqan3/test/documentation/seqan_logo.svg")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "my_app 3.4.0-rc.1")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "my_app 3.4.0-rc.1")
set(CPACK_PACKAGE_NAME "my_app")
set(CPACK_PACKAGE_RELOCATABLE "true")
set(CPACK_PACKAGE_VENDOR "seqan")
set(CPACK_PACKAGE_VERSION "3.4.0-rc.1")
set(CPACK_PACKAGE_VERSION_MAJOR "1")
set(CPACK_PACKAGE_VERSION_MINOR "0")
set(CPACK_PACKAGE_VERSION_PATCH "0")
set(CPACK_READELF_EXECUTABLE "/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-readelf")
set(CPACK_RESOURCE_FILE_LICENSE "/home/emre/tutorials/sequence_tut/seqan3/LICENSE.md")
set(CPACK_RESOURCE_FILE_README "/home/emre/tutorials/sequence_tut/seqan3/README.md")
set(CPACK_RESOURCE_FILE_WELCOME "/home/emre/bin/cmake/share/cmake-3.27/Templates/CPack.GenericWelcome.txt")
set(CPACK_SET_DESTDIR "OFF")
set(CPACK_SOURCE_GENERATOR "TXZ")
set(CPACK_SOURCE_IGNORE_FILES "\\.git($|/)")
set(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/home/emre/tutorials/sequence_tut/source/CPackSourceConfig.cmake")
set(CPACK_SYSTEM_NAME "Linux")
set(CPACK_THREADS "1")
set(CPACK_TOPLEVEL_TAG "Linux")
set(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "/home/emre/tutorials/sequence_tut/source/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()
