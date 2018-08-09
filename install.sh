# Auto-installs the Golden Logo plugin for Krita

# Create directories
path=~/.local/share/krita
rm -rf $path/pykrita/golden
mkdir -p $path/pykrita/golden
mkdir -p $path/actions

# Install files
cp "plugin.desktop" $path/pykrita/golden.desktop
cp "actions.xml" $path/actions/golden.action
cp "plugin/__init__.py" $path/pykrita/golden
cp "plugin/golden.py" $path/pykrita/golden

# Say goodbye (the hardest part)
echo "Finished installation"
echo "You may delete this folder now"
