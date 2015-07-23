#!/bin/bash
tmux new-window -a
tmux send-keys "ssh $3" C-m
