# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/emre/bin/cmake/bin/cmake

# The command to remove a file.
RM = /home/emre/bin/cmake/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/emre/tutorials/sequence_tut/source

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/emre/tutorials/sequence_tut/source

# Include any dependencies generated for this target.
include CMakeFiles/hw.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/hw.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/hw.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/hw.dir/flags.make

CMakeFiles/hw.dir/hw.cpp.o: CMakeFiles/hw.dir/flags.make
CMakeFiles/hw.dir/hw.cpp.o: hw.cpp
CMakeFiles/hw.dir/hw.cpp.o: CMakeFiles/hw.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/emre/tutorials/sequence_tut/source/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/hw.dir/hw.cpp.o"
	/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/hw.dir/hw.cpp.o -MF CMakeFiles/hw.dir/hw.cpp.o.d -o CMakeFiles/hw.dir/hw.cpp.o -c /home/emre/tutorials/sequence_tut/source/hw.cpp

CMakeFiles/hw.dir/hw.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/hw.dir/hw.cpp.i"
	/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/emre/tutorials/sequence_tut/source/hw.cpp > CMakeFiles/hw.dir/hw.cpp.i

CMakeFiles/hw.dir/hw.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/hw.dir/hw.cpp.s"
	/home/emre/miniconda3/envs/conda_gcc_env/bin/x86_64-conda-linux-gnu-c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/emre/tutorials/sequence_tut/source/hw.cpp -o CMakeFiles/hw.dir/hw.cpp.s

# Object files for target hw
hw_OBJECTS = \
"CMakeFiles/hw.dir/hw.cpp.o"

# External object files for target hw
hw_EXTERNAL_OBJECTS =

hw: CMakeFiles/hw.dir/hw.cpp.o
hw: CMakeFiles/hw.dir/build.make
hw: /home/emre/miniconda3/lib/libyaml-cpp.so.0.7.0
hw: CMakeFiles/hw.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable hw"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hw.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/hw.dir/build: hw
.PHONY : CMakeFiles/hw.dir/build

CMakeFiles/hw.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/hw.dir/cmake_clean.cmake
.PHONY : CMakeFiles/hw.dir/clean

CMakeFiles/hw.dir/depend:
	cd /home/emre/tutorials/sequence_tut/source && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/emre/tutorials/sequence_tut/source /home/emre/tutorials/sequence_tut/source /home/emre/tutorials/sequence_tut/source /home/emre/tutorials/sequence_tut/source /home/emre/tutorials/sequence_tut/source/CMakeFiles/hw.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/hw.dir/depend

