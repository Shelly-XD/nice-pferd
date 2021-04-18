SCRIPT=$(readlink -f "$0")
NICE_PFERD_PATH=$(dirname "$SCRIPT")

pip install -r "$NICE_PFERD_PATH/requirements.txt"

echo "alias nice-pferd='cd "$NICE_PFERD_PATH" && flask run'" >> ~/.bashrc
echo "alias nice-pferd-upgrade='cd "$NICE_PFERD_PATH"/.. && rm -rf "$NICE_PFERD_PATH" && git clone https://github.com/augustin64/nice-pferd'" >> ~/.bashrc