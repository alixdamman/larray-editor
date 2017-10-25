#!/bin/bash

"$PYTHON" setup.py install || exit 1

mkdir -p "$PREFIX/Menu"
cp "$RECIPE_DIR/larray-editor.json" "$PREFIX/Menu"
cp "$SRC_DIR/larray_editor/images/larray.ico" "$PREFIX/Menu"
cp "$SRC_DIR/larray_editor/images/larray-help.ico" "$PREFIX/Menu"

# See
# http://docs.continuum.io/conda/build.html
# for a list of environment variables that are set during the build process.