#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Open Org
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Org Alias" }
# @raycast.packageName SF Utils

# Documentation:
# @raycast.description Open Salesforce Org

import sys
import os

os.system("sfdx force:org:open -u " + sys.argv[1])
