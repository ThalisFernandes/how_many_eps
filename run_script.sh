#!/bin/sh

echo "Rodando applicação para achar episodios"


call_service ()
{
    chmod 777 runner.py
        
    python3 runner.py
}

call_service