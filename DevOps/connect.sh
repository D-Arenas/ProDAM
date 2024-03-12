#!/bin/bash

# Usage: Execute these commands to connect to the server
chmod 600 dashboard_keys.pem
ssh -i dashboard_keys.pem ec2-user@ec2-54-211-196-48.compute-1.amazonaws.com
