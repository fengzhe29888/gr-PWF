INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PWF PWF)

FIND_PATH(
    PWF_INCLUDE_DIRS
    NAMES PWF/api.h
    HINTS $ENV{PWF_DIR}/include
        ${PC_PWF_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PWF_LIBRARIES
    NAMES gnuradio-PWF
    HINTS $ENV{PWF_DIR}/lib
        ${PC_PWF_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PWF DEFAULT_MSG PWF_LIBRARIES PWF_INCLUDE_DIRS)
MARK_AS_ADVANCED(PWF_LIBRARIES PWF_INCLUDE_DIRS)

