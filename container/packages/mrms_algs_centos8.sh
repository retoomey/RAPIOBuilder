# Toomey Sept 2020
# Centos:8 image requirements for building
# If using docker/etc, having a single install script drops the storage for layers quite a bit

# Add base libraries/packages/utils
./rapio_centos8.sh

# Add packages for algs
./mrms_add_algs_centos8.sh
