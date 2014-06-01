#!/bin/bash

set -e

# Ensure we're in the right directory
cd "$(dirname "$0")"

CHANGELOG="CHANGELOG.md"

echo "Creating CHANGELOG.md"
echo "Latest Changes" > $CHANGELOG
echo "==============" >> $CHANGELOG
echo "Compiled on: `date`" >> $CHANGELOG
echo "\nThis file is auto-generated upon every new release. To review the latest commits in the master branch, please refer to: https://github.com/skakri/django-unstructured/commits/master"
echo "" >> $CHANGELOG
git log --graph --pretty=format:'%h -%d %s (%ci) <%an>' --abbrev-commit | sed "s/^/    /" >> $CHANGELOG

echo "Building docs..."
cd docs
make html
cd ..

echo "Building Python source distribution..."
rm -Rf *egg-info/
python setup.py sdist

