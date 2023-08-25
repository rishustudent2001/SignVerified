[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for Android/iOS packaging)
package.domain = org.test

# (str) Source code directory (where the main.py lives)
source.dir = .

# (list) Source files to include (leave empty to include all files)
source.include_exts = py,png,jpg,kv

# (str) Application version (use a meaningful version number)
version = 1.0

# (list) Application requirements (dependencies)
requirements = python3,kivy==2.0.0,kivymd,pillow

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash background color for Android (optional)
android.presplash_color = #FFFFFF

# (str) Application icon (replace with the path to your icon)
icon.filename = path/to/your/icon.png

# (list) Supported orientations (landscape, portrait, etc.)
orientation = portrait

# (list) Permissions (e.g., internet access)
android.permissions = INTERNET

#
# Android specific settings
#

# (str) Android API level to use (minimum API version)
android.api = 28

# (int) Android NDK API level (should match the API level above)
android.ndk_api = 21

# (str) Android NDK directory (leave empty to download automatically)
android.ndk_path =

# (str) Android SDK directory (leave empty to download automatically)
android.sdk_path =

# (str) Android Gradle dependencies (leave empty for default)
#android.gradle_dependencies =

# (str) Android build tools version (leave empty for default)
#android.gradle_build_tools = <version>

# (bool) Skip building with the setup.py script
android.skip_pymodules = False

# (bool) Use a precompiled distribution
#android.prebuild_dist_name = kivy

# (list) Additional Java .jar files to add to the libs directory
#android.add_jars = foo.jar,bar.jar

# (list) Python modules to include in the APK (optional)
#android.pymodules = mymodule

# (list) Android AAR archives to add (e.g., for AdMob)
#android.add_aars = /path/to/library.aar

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Use --private storage (True) or --dir public storage (False)
android.private_storage = True

# (int) Target Android API version (should be as high as possible)
android.minapi = 21

# (int) Maximum API version to support (optional)
android.maxapi = 28

# (bool) Full screen mode (True) or not (False)
android.fullscreen = False

# (list) Archs to build for (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = armeabi-v7a, arm64-v8a

# (str) Icon for the application store (512x512 px)
#android.icon.source = path/to/store/icon.png

# (list) Presplash for the application store (leave empty to use default)
#android.presplash.background = path/to/store/background.png
#android.presplash.reduced_opacity = path/to/store/background_reduced_opacity.png

#
# iOS specific settings (not used in this example)
#

[ios]

# iOS settings go here
