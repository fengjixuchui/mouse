include ~/theos/makefiles/common.mk
export SYSROOT =  ~/theos/sdks/iPhoneOS9.3.sdk
export TARGET_CODESIGN_FLAGS="-Ssign.plist"
TOOL_NAME = ios


ios_FILES = main.mm m.m
ios_OBJ_FILES = libcrypto.a libssl.a
ios_FRAMEWORKS = Foundation Security AudioToolbox CoreFoundation AVFoundation MediaPlayer UIKit
ios_PRIVATE_FRAMEWORKS = AppSupport SpringBoardServices IOSurface

include ~/theos/makefiles/tool.mk

export ARCHS = armv7 arm64

CFLAGS = -Wall -g

