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
CMAKE_SOURCE_DIR = /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild

# Utility rule file for seqan3_fetch_content-populate.

# Include any custom commands dependencies for this target.
include CMakeFiles/seqan3_fetch_content-populate.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/seqan3_fetch_content-populate.dir/progress.make

CMakeFiles/seqan3_fetch_content-populate: CMakeFiles/seqan3_fetch_content-populate-complete

CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-mkdir
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-build
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install
CMakeFiles/seqan3_fetch_content-populate-complete: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-test
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'seqan3_fetch_content-populate'"
	/home/emre/bin/cmake/bin/cmake -E make_directory /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles
	/home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles/seqan3_fetch_content-populate-complete
	/home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-done

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update:
.PHONY : seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-build: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "No build step for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E echo_append
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-build

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure: seqan3_fetch_content-populate-prefix/tmp/seqan3_fetch_content-populate-cfgcmd.txt
seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "No configure step for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E echo_append
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-gitinfo.txt
seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Performing download step (git clone) for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps && /home/emre/bin/cmake/bin/cmake -P /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/tmp/seqan3_fetch_content-populate-gitclone.cmake
	cd /home/emre/tutorials/sequence_tut/source/_deps && /home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-build
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "No install step for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E echo_append
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Creating directories for 'seqan3_fetch_content-populate'"
	/home/emre/bin/cmake/bin/cmake -Dcfgdir= -P /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/tmp/seqan3_fetch_content-populate-mkdirs.cmake
	/home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-mkdir

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch-info.txt
seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "No patch step for 'seqan3_fetch_content-populate'"
	/home/emre/bin/cmake/bin/cmake -E echo_append
	/home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update:
.PHONY : seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-test: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "No test step for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E echo_append
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-build && /home/emre/bin/cmake/bin/cmake -E touch /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-test

seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update: seqan3_fetch_content-populate-prefix/tmp/seqan3_fetch_content-populate-gitupdate.cmake
seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update-info.txt
seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Performing update step for 'seqan3_fetch_content-populate'"
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-src && /home/emre/bin/cmake/bin/cmake -Dcan_fetch=YES -P /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/seqan3_fetch_content-populate-prefix/tmp/seqan3_fetch_content-populate-gitupdate.cmake

seqan3_fetch_content-populate: CMakeFiles/seqan3_fetch_content-populate
seqan3_fetch_content-populate: CMakeFiles/seqan3_fetch_content-populate-complete
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-build
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-configure
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-download
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-install
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-mkdir
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-patch
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-test
seqan3_fetch_content-populate: seqan3_fetch_content-populate-prefix/src/seqan3_fetch_content-populate-stamp/seqan3_fetch_content-populate-update
seqan3_fetch_content-populate: CMakeFiles/seqan3_fetch_content-populate.dir/build.make
.PHONY : seqan3_fetch_content-populate

# Rule to build all files generated by this target.
CMakeFiles/seqan3_fetch_content-populate.dir/build: seqan3_fetch_content-populate
.PHONY : CMakeFiles/seqan3_fetch_content-populate.dir/build

CMakeFiles/seqan3_fetch_content-populate.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/seqan3_fetch_content-populate.dir/cmake_clean.cmake
.PHONY : CMakeFiles/seqan3_fetch_content-populate.dir/clean

CMakeFiles/seqan3_fetch_content-populate.dir/depend:
	cd /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild /home/emre/tutorials/sequence_tut/source/_deps/seqan3_fetch_content-subbuild/CMakeFiles/seqan3_fetch_content-populate.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/seqan3_fetch_content-populate.dir/depend

