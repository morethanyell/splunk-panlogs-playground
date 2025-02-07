# Palo Alto Networks Fake Log Generator

This is a Python-based fake log generator that simulates Palo Alto Networks (PAN) firewall traffic logs. It continuously prints randomly generated PAN logs in the correct comma-separated format (CSV), making it useful for testing, Splunk ingestion, and SIEM training.

## Features
- ✅ Simulates random source and destination IPs (public & private)
- ✅ Includes realistic timestamps, ports, zones, and actions (allow, deny, drop)
- ✅ Prepends log entries with timestamp, hostname, and a static 1 for authenticity
- ✅ Runs continuously, printing new logs every 2 to 30 seconds
- ✅ Supports manual stopping via CTRL + C

## Installation

1. In your Splunk development instance, install the official Splunk-built ["Splunk Add-on for Palo Alto Networks"](https://splunkbase.splunk.com/app/7523)
2. Download the file `<this_github_repo>/src/Splunk_TA_paloalto_networks/bin/pan_log_generator.py`
3. Copy that file into your Splunk instance: e.g.: `cp /tmp/pan_log_generator.py $SPLUNK_HOME/etc/apps/Splunk_TA_paloalto_networks/bin/`
4. Download the file `<this_github_repo>/src/Splunk_TA_paloalto_networks/local/inputs.conf`
4. Copy that file into your Splunk instance. But if your Splunk intance (this: `$SPLUNK_HOME/etc/apps/Splunk_TA_paloalto_networks/local/`) already has an inputs.conf in it, make sure you don't overwrite it. Instead, just append the new input stanza contained in the this repository:

```
[script://$SPLUNK_HOME/etc/apps/Splunk_TA_paloalto_networks/bin/pan_log_generator.py]
disabled = 0
host = <your host here>
index = <your index here>
interval = -1
sourcetype = pan_log
```

## Usage 
1. Change the value for your `host = <your host here>` and `index = <your index here>`
2. Notice that this input stanza is set to disabled (`disabled = 1`), this is to ensure it doesn't start right away. Enable the script whenever you're ready.
3. Once enabled, the script will run forever by virtue of `interval = -1`. This will make the script print fake PAN logs until forcefully stopped by a multitude of methods (e.g.: Disabling the scripted input, CLI-method, etc.)


## How It Works

The script continuously generates logs in real-time:

- Generates a new log entry with random fields (IP, ports, zones, actions, etc.).
- Formats the log entry with a timestamp, local hostname, and a fixed 1.
- Prints to STDIO (console) at random intervals that is 1-3 seconds.
- With this party trick running alongside `Splunk_TA_paloalto_networks`, all its configurations like `props.conf` and `transforms.conf` should work, e.g.: Field Extractions, Source Type renaming from `sourcetype = pan_log` into `sourcetype = pan:traffic` if the log matches "TRAFFIC", and etc.


## Author
- daniel.l.astillero@gmail.com (accepts beer donations via Paypal)
- Watch my 35mm film vlogs on youtube.com/@grainfrizz