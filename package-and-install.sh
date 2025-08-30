#!/bin/bash

# Tic Tac Toe Debian Package Builder and Installer

# Set the package name and version
PACKAGE_NAME="tictactoe"
VERSION=$(cat VERSION.md)

echo "Building Tic Tac Toe Debian package..."

# Create temporary directory
TMP_DIR=$(mktemp -d)

# Create directory structure in temporary directory
echo "Creating directory structure..."
mkdir -p ${TMP_DIR}/DEBIAN ${TMP_DIR}/usr/bin ${TMP_DIR}/usr/share/applications ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps ${TMP_DIR}/usr/share/tictactoe

# Create control file
echo "Creating control file..."
cat > ${TMP_DIR}/DEBIAN/control << EOF
Package: tictactoe
Version: ${VERSION}
Section: games
Priority: optional
Architecture: amd64
Depends: python3
Pre-Depends: python3-pygame
Maintainer: Your Name <your.email@example.com>
Description: Tic Tac Toe Game
 A simple 2-player Tic Tac Toe game built with Pygame.
EOF

# Copy game file
echo "Copying game file..."
cp main.py ${TMP_DIR}/usr/share/tictactoe/

# Create launcher script
echo "Creating launcher script..."
cat > ${TMP_DIR}/usr/bin/tictactoe << EOF
#!/bin/bash
python3 /usr/share/tictactoe/main.py
EOF

# Make launcher executable
chmod +x ${TMP_DIR}/usr/bin/tictactoe

# Create desktop entry
echo "Creating desktop entry..."
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

# Create icon if it doesn't exist
if [ ! -f tictactoe-icon.png ]; then
    echo "Creating icon..."
    python3 create_icon.py
fi

# Copy icon
echo "Copying icon..."
cp tictactoe-icon.png ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps/tictactoe.png

# Set permissions
echo "Setting permissions..."
chmod 644 ${TMP_DIR}/DEBIAN/control
chmod 644 ${TMP_DIR}/usr/share/applications/tictactoe.desktop
chmod 644 ${TMP_DIR}/usr/share/icons/hicolor/256x256/apps/tictactoe.png
chmod 644 ${TMP_DIR}/usr/share/tictactoe/main.py

# Build package
echo "Building package..."
dpkg-deb --build --root-owner-group ${TMP_DIR}

# Rename package
mv ${TMP_DIR}.deb ${PACKAGE_NAME}_${VERSION}_amd64.deb

# Clean up temporary directory
rm -rf ${TMP_DIR}

echo "Package built successfully: ${PACKAGE_NAME}_${VERSION}_amd64.deb"

# Ask user if they want to install the package
echo ""
echo "Do you want to install the package now? (y/n)"
read -r response

if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]; then
    echo "Installing package..."
    sudo dpkg -i ${PACKAGE_NAME}_${VERSION}_amd64.deb
    
    # Fix dependencies if needed
    echo "Fixing dependencies if needed..."
    sudo apt-get install -f -y
    
    echo ""
    echo "Installation complete!"
    echo "You can now launch the game by:"
    echo "1. Running 'tictactoe' in the terminal"
    echo "2. Finding 'Tic Tac Toe' in your applications menu under Games"
else
    echo "Package built but not installed. You can install it later with:"
    echo "sudo dpkg -i ${PACKAGE_NAME}_${VERSION}_amd64.deb"
    echo "sudo apt-get install -f"
fi
