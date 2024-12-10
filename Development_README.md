### Development(Changing source code and rebuilding packages)
If you make change to the source code and want to rebuild the package. In the folder containing the LevSeq repo, build the package again.

```
python setup.py sdist bdist_wheel
pip install dist/levseq-0.1.0.tar.gz
```

### Steps to rebuild the C++ executables on Wynton
Be sure to run these steps on a Wynton dev node! I don't think the login nodes have the correct versions of `make` or `cmake` installed.

1. Clone the `LevSeq` GitHub repository. Create a `levseq` conda environment and install dependencies as outlined in the README.
3. In your `levseq` conda environment, install `zlib` as well as `g++` and `gcc` compilers using `conda install -c conda-forge gcc=13 gxx=13 zlib`.
4. Navigate to `executables`. Delete all files within `build` and the entire `_deps` directory. Within the source directory, delete all files with the execption of `CMakeLists.txt`, all `.cpp` files, and all `.hpp` files.
5. Enter the `build` directory. Build the project using `cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ ../source/`.
    - Your version of `cmake` should be greater than 3.14
6. Run `make -j` within the `build` directory. This should create a new subdirectory, `bin`, where you will find the compiled binaries for the demultiplexing code!
