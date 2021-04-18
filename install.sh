#get nice-pferd location
SCRIPT=$(readlink -f "$0")
NICE_PFERD_PATH=$(dirname "$SCRIPT")
#install python dependencies
pip install -r "$NICE_PFERD_PATH/requirements.txt"
#add aliases
echo "alias nice-pferd='cd "$NICE_PFERD_PATH" && flask run'" >> ~/.bashrc
echo "alias nice-pferd-upgrade='cd "$NICE_PFERD_PATH"/.. && rm -rf "$NICE_PFERD_PATH" && git clone https://github.com/augustin64/nice-pferd'" >> ~/.bashrc
#make ~/.bashrc executable and execute it to get all the brand new aliases
chmod +x ~/.bashrc && ~/.bashrc
#Display a help message
echo -e '\nUse nice-pferd to start the local server and then use a browser and go to http://localhost:5000 to have a GUI\nUse nice-pferd-upgrade to upgrade to the latest version available'