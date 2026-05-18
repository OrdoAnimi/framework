#!/bin/sh
set -e

# Start nginx in background
nginx -g "daemon off;" &
NGINX_PID=$!

# Start Node application
node dist/index.js &
NODE_PID=$!

# Forward signals to both processes
trap "kill $NGINX_PID $NODE_PID 2>/dev/null; exit 0" TERM INT

# Wait — if either process exits, bring down the container
wait -n $NGINX_PID $NODE_PID
EXIT_CODE=$?

kill $NGINX_PID $NODE_PID 2>/dev/null
exit $EXIT_CODE
