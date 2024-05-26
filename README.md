# ai_hackathon_may24
# Code written for the Hackathon in Oxford, May 2024

# Procedure to run it:

sudo apt install python3.11
sudo apt install python3.11-venv

python3.11 -m venv .venv
source .venv/bin/activate
pip install async-timeout
pip install git+https://github.com/asynchronous-flows/asyncflows@main
pip install -U duckduckgo_search
ACTIONS_MODULE=my_actions python main.py
