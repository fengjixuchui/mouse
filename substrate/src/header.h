//            ---------------------------------------------------
//                              Mouse Framework                                 
//            ---------------------------------------------------
//                Copyright (C) <2019-2020>  <Entynetproject>
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

#import "rocketbootstrap.h"
@interface SBMediaController : NSObject {
	int _manualVolumeChangeCount;
	float _pendingVolumeChange;
	NSTimer* _volumeCommitTimer;
	BOOL _debounceVolumeRepeat;
	NSDictionary *_nowPlayingInfo;
}
@property (assign,getter=isRingerMuted,nonatomic) BOOL ringerMuted;
+(id)sharedInstance;
-(void)setRingerMuted:(BOOL)arg1;
-(void)cancelLockScreenIdleTimer;
-(void)turnOnScreenFullyWithBacklightSource:(int)arg1;
-(BOOL)play;
-(BOOL)togglePlayPause;
-(BOOL)isPlaying;
-(BOOL)changeTrack:(int)track;
@end


@interface SBIcon : NSObject
- (NSString *)nodeIdentifier;
@end


@interface SBApplicationIcon : SBIcon

@end

@interface SBIconController : NSObject
-(id)lastTouchedIcon;
@end

@interface SBUserAgent : NSObject
+(id)sharedUserAgent;
-(void)lockAndDimDevice;
-(void)handleMenuDoubleTap;
-(void)clickedMenuButton;
-(bool)handleHomeButtonSinglePressUp;
-(bool)handleHomeButtonDoublePressDown;
@end


@interface SBDeviceLockController : NSObject
+(id)sharedController;
-(void)_clearBlockedState;
-(BOOL)isPasscodeLocked;
@end

@interface CLLocationManager : NSObject
+ (void)setLocationServicesEnabled:(BOOL)arg1;
@end

@interface SBLockScreenManager : NSObject
@property (nonatomic, readonly) BOOL isUILocked;
+(id)sharedInstance;
-(BOOL)attemptUnlockWithPasscode:(id)passcode;
@end

@interface SBHUDController : NSObject
+(id)sharedInstance;
-(void)hideHUD;
-(void)showHUD;
@end

@interface VolumeControl : NSObject
+(id)sharedVolumeControl;
-(void)toggleMute;
@end


