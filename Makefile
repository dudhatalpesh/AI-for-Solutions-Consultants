# Convenience targets. Windows users: run from Git Bash or WSL, or use the
# PowerShell equivalents in docs/02-environment-setup.md.

COMPOSE ?= docker compose
PY      ?= python

.PHONY: help setup up down logs ps pull-models kb import-workflows export-workflows backup venv test validate clean reset

help:            ## List targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-18s %s\n", $$1, $$2}'

setup:           ## Create .env from .env.example (edit it afterwards!)
	@test -f .env || cp .env.example .env
	@mkdir -p shared/kb shared/inbox backups
	@echo ".env ready. Change every CHANGE_ME value before 'make up'."

up:              ## Start the lab stack
	$(COMPOSE) up -d

down:            ## Stop the stack (keeps data)
	$(COMPOSE) down

logs:            ## Follow n8n logs
	$(COMPOSE) logs -f n8n

ps:              ## Show container status
	$(COMPOSE) ps

pull-models:     ## Pull/refresh Ollama models
	$(COMPOSE) exec ollama ollama pull llama3.2
	$(COMPOSE) exec ollama ollama pull nomic-embed-text

kb:              ## Copy Lab 04 sample knowledge base into shared/kb
	@mkdir -p shared/kb
	cp labs/lab-04-n8n-rag-knowledge-assistant/sample-docs/*.md shared/kb/

import-workflows: ## Import every workflow in n8n-workflows/ into n8n (creates new copies)
	$(COMPOSE) exec n8n sh -c 'for f in /data/workflows/*.json; do n8n import:workflow --input="$$f"; done'

export-workflows: ## Export all workflows to shared/backups (no credentials)
	@mkdir -p shared/backups
	$(COMPOSE) exec n8n n8n export:workflow --all --separate --output=/data/shared/backups/

backup:          ## Dump Postgres (n8n + lab schema) to backups/
	@mkdir -p backups
	$(COMPOSE) exec -T postgres sh -c 'pg_dump -U "$$POSTGRES_USER" "$$POSTGRES_DB"' > backups/n8n-$$(date +%Y%m%d-%H%M%S).sql

venv:            ## Create Python virtual env and install requirements
	$(PY) -m venv .venv
	.venv/bin/pip install -r requirements.txt || .venv/Scripts/pip install -r requirements.txt

test:            ## Run Python unit tests (no services needed)
	$(PY) -m pytest -q labs

validate:        ## Validate JSON, links and secret patterns
	$(PY) scripts/validate_repo.py

clean:           ## Remove Python caches
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +

reset:           ## DANGER: stop and delete ALL lab data (volumes)
	$(COMPOSE) down -v
