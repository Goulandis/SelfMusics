Overview
-----------------------------------------------------------
MyClouds is a plugin for AIMP player that provides ability to play music from cloud storages.


Privacy Policy
-----------------------------------------------------------
The plugin provides a read-only access to your cloud storage device for playback purposes, 
its means that all files and documents except audio files are not displayed in the player.

By default, plugin uses OAuth authorization to get access to cloud storage. Its authorization 
method is more secure than basic user authentication (using login and password), and player 
does not keep any user personal data in this case.


Features
-----------------------------------------------------------
+ Full integration to Music Library
+ Ability to download files via drag-n-drop
+ Smart file-based cache system
+ Support for Lyrics that provided as separate files in the .lrc / .srt file formats
+ Support for CUE sheets
+ Support for Cloud@Mail.ru, OneDrive, DropBox and Google Drive cloud storages
+ Support for WebDAV-based cloud services (including Yandex.Disk, 4shared, OpenDrive, ADrive, Box, pCloud and DriveOnWeb cloud storages)


Limitations
-----------------------------------------------------------
Cloud@Mail.Ru: 
+ Only basic user authentication are supported (Login+Password)
+ File names and content encryption are not supported


History
-----------------------------------------------------------
v1.00.22 (16.07.2018)
+ Included to AIMP v4.60 bundle as default plugin

v1.00.21 (11.06.2018)
+ Alphabetic sorting is now used as default sorting

v1.00.20 Beta (10.05.2018)
+ Support for smart-playlists

v1.00.18 Beta (01.05.2018)
- Fixed: small issues with WebDAV parser

v1.00 Beta (13.04.2018)
* Support for connection settings
- Fixed: an issue with token auto-refreshing for Cloud@Mail.ru Service
- Fixed: small issues with datetime conversions

v0.60 Beta (07.04.2018)
+ Support for Cloud@Mail.ru service (experimental)

v0.50 Beta (05.04.2018)
+ Support for file tags
+ Support for Dropbox service
+ Support for OneDrive service
- Fixed: the Streaming Access does not work with Google Drive

v0.20 Preview (29.03.2018)
+ Added an ability to display album arts
+ Support for 4shared, OpenDrive, DriveOnWeb, ADrive cloud storages
+ Support for Google Drive service 

v0.10 Preview (26.03.2018)
+ Support for OAuth2 authorization mode (built-in support for Yandex.Disk)
+ Support for Box.com and pCloud.com clouds storages
* WebDAV parser has been improved to support custom WebDAV-based storages

v0.01 Preview (31.01.2018)
+ First public preview release