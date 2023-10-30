#!/usr/bin/env bash

set -eou pipefail

function start_weaviate() {
  docker compose up -d

  while ! curl --fail -o /dev/null -s http://localhost:8080/v1/.well-known/ready; do
    echo "Waiting for Weaviate to be ready..."
    sleep 1;
  done
}

function import_with_curl() {
  ./import/curl/create_schema.sh
  ./import/curl/import.sh
}

function import_with_go() {
  function cmd_go() {
    if ! hash "go" 2>/dev/null; then
      docker run --rm -v "$PWD":/app -w /app golang:1.19-alpine $@
    else
      $@
    fi
  }
  cd ./import/go && cmd_go go mod vendor; go run cmd/main.go && cd -
}

run_go=true
run_curl=false

while [[ "$#" -gt 0 ]]; do
  case $1 in
    --go) run_curl=false; run_go=true ;;
    --curl) run_curl=true ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

start_weaviate

if $run_curl
then
  echo "Running import using curl"
  import_with_curl
fi

if $run_go
then
  echo "Running import using Go client"
  import_with_go
fi



##Create and activate virtual env
# check the OS 
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows
  python -m venv venv
  source venv/Scripts/activate
else
  # macOS or Linux
  python -m venv venv
  source venv/bin/activate
fi

echo "VENV: created and activated"

##Change to python/ 
cd python

#Install requirements
pip install -r requirements.txt
echo "COMPLETE: requirements.txt install"

#Run python client
## PYTHONUNBUFFERED=1 python app.py

python "app.py"

