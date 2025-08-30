#!/bin/bash

# Set the package name and version
PACKAGE_NAME="tictactoe"
VERSION=$(cat VERSION.md)

# Create temporary directory
TMP_DIR=$(mktemp -d)

# Create directory structure in temporary directory
mkdir -p ${TMP_DIR}/DEBIAN ${TMP_DIR}/usr/bin ${TMP_DIR}/usr/share/applications ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps ${TMP_DIR}/usr/share/tictactoe

# Create control file
cat > ${TMP_DIR}/DEBIAN/control << EOF
Package: tictactoe
Version: ${VERSION}
Section: games
Priority: optional
Architecture: amd64
Depends: python3
Pre-Depends: python3-pygame
Maintainer: Matt Phillips <mathewrphillips@gmail.com> 
Description: Tic Tac Toe Game
 A simple 2-player Tic Tac Toe game built with Pygame.
EOF

# Copy files to temporary directory
cp main.py ${TMP_DIR}/usr/share/tictactoe/
cp tictactoe-icon.png ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps/tictactoe.png

# Create launcher script
cat > ${TMP_DIR}/usr/bin/tictactoe << EOF
#!/bin/bash
python3 /usr/share/tictactoe/main.py
EOF

# Create desktop entry
cat > ${TMP_DIR}/usr/share/applications/tictactoe.desktop << EOF
[Desktop Entry]
Name=Tic Tac Toe
Comment=A simple 2-player Tic Tac Toe game
Exec=/usr/bin/tictactoe
Icon=tictactoe
Terminal=false
Type=Application
Categories=Game;
EOF

# Set permissions for package files
chmod 644 ${TMP_DIR}/DEBIAN/control
chmod 644 ${TMP_DIR}/usr/share/applications/tictactoe.desktop
chmod 644 ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps/tictactoe.png
chmod 644 ${TMP_DIR}/usr/share/tictactoe/main.py
chmod 755 ${TMP_DIR}/usr/bin/tictactoe

# Build the package
dpkg-deb --build --root-owner-group ${TMP_DIR}

# Move the package to the current directory
mv ${TMP_DIR}.deb ${PACKAGE_NAME}_${VERSION}_amd64.deb

# Clean up temporary directory
rm -rf ${TMP_DIR}

echo "Package built successfully: ${PACKAGE_NAME}_${VERSION}_amd64.deb"
