#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl restart slot_timer
sudo systemctl restart timer_frontend
