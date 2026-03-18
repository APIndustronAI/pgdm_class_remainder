# PGDM Class Reminder Automation

## Overview

This project automatically sends class reminder emails to students before the class start time.

The system runs as a cloud scheduler using GitHub Actions and sends reminder emails via Outlook SMTP.

## Features

* 45 minute reminder
* 10 minute reminder
* Cloud execution (serverless)
* No duplicate email logic
* Configurable via .env
* CSV based schedule input

## Project Structure

* reminder/ → automation logic
* data/ → schedule file
* .env → configuration
* GitHub Actions → scheduler

## How It Works

1. GitHub scheduler runs every 5 minutes
2. Python script reads schedule.csv
3. Checks reminder window
4. Sends email using Outlook SMTP

## Future Improvements

* Auto email parser using AI
* Google Sheet integration
* Telegram notification
* Web dashboard
* Student self subscription system
