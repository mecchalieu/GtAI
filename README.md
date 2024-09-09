# Growtopia AI Companion
```markdown
The Growtopia AI Companion is a user-friendly bot designed to assist players in Growtopia. This guide provides instructions on how to set up and run the AI companion.

## Table of Contents
- [Clone the Repository](#clone-the-repository)
- [Install Python](#install-python)
- [Install Dependencies](#install-dependencies)
- [Run the Setup Wizard (For First-Time Users)](#run-the-setup-wizard-for-first-time-users)
- [Start a Bot](#start-a-bot)
- [Stop a Bot](#stop-a-bot)
- [Switching Between Bots](#switching-between-bots)
- [Check Configurations](#check-configurations)
- [Example Workflow](#example-workflow)
- [Additional Notes](#additional-notes)

## Install Python
Ensure you have Python installed on your system. You can check by running:

```bash
python --version
```

If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

## Install Dependencies
If your script has dependencies (like specific Python packages), create a `requirements.txt` file listing them, and install with:

```bash
pip install -r requirements.txt
```

If your script doesn’t need any external libraries, you can skip this step.

## Run the Setup Wizard (For First-Time Users)
This will help new users configure their bots easily.

```bash
python gtai.py setup
```

Follow the on-screen instructions to configure your bots.

## Start a Bot
To start a specific bot, use the following command. Replace `bot1` with the name of the bot you want to start.

```bash
python gtai.py start --bot bot1
```

## Stop a Bot
To stop a bot, use the following command. Replace `bot1` with the name of the bot you want to stop.

```bash
python gtai.py stop --bot bot1
```

## Switching Between Bots
If you have multiple bots and want to switch between them, use the `--bot` flag with the appropriate bot name when starting or stopping.

## Check Configurations
You can modify bot configurations by editing the JSON files in the `config/` directory. Make sure to restart the bot after making changes.

## Example Workflow
```bash
# Run the setup wizard
python gtai.py setup

# Start a bot
python gtai.py start --bot bot1

# Stop the bot
python gtai.py stop --bot bot1
```

## Additional Notes
- **Configuration Files:** Store your bot configurations in the `config/` directory. Example configuration files can be found in `config/gtai/`.
- **Script Modifications:** The script is designed to be easily modifiable. If you want to add more features or customize it, simply modify the `gtai.py` file or create additional scripts as needed.

## Copyright
© Mecchalieu / kylvj
```

DM (Mecchalieu / kylvj) for more information
