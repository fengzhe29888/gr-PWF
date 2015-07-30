# Install script for directory: /home/haili/gr-PWF/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/PWF" TYPE FILE FILES
    "/home/haili/gr-PWF/python/__init__.py"
    "/home/haili/gr-PWF/python/sigmagen.py"
    "/home/haili/gr-PWF/python/pilot_gen.py"
    "/home/haili/gr-PWF/python/channel.py"
    "/home/haili/gr-PWF/python/pilot_receive.py"
    "/home/haili/gr-PWF/python/power_adjust.py"
    "/home/haili/gr-PWF/python/weighted_sum_rate.py"
    "/home/haili/gr-PWF/python/debug_printmsg.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/PWF" TYPE FILE FILES
    "/home/haili/gr-PWF/build/python/__init__.pyc"
    "/home/haili/gr-PWF/build/python/sigmagen.pyc"
    "/home/haili/gr-PWF/build/python/pilot_gen.pyc"
    "/home/haili/gr-PWF/build/python/channel.pyc"
    "/home/haili/gr-PWF/build/python/pilot_receive.pyc"
    "/home/haili/gr-PWF/build/python/power_adjust.pyc"
    "/home/haili/gr-PWF/build/python/weighted_sum_rate.pyc"
    "/home/haili/gr-PWF/build/python/debug_printmsg.pyc"
    "/home/haili/gr-PWF/build/python/__init__.pyo"
    "/home/haili/gr-PWF/build/python/sigmagen.pyo"
    "/home/haili/gr-PWF/build/python/pilot_gen.pyo"
    "/home/haili/gr-PWF/build/python/channel.pyo"
    "/home/haili/gr-PWF/build/python/pilot_receive.pyo"
    "/home/haili/gr-PWF/build/python/power_adjust.pyo"
    "/home/haili/gr-PWF/build/python/weighted_sum_rate.pyo"
    "/home/haili/gr-PWF/build/python/debug_printmsg.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

