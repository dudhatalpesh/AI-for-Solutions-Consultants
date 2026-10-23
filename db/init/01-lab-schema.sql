-- Runs once, the first time the Postgres volume is created.
-- Lab-only tables used by the n8n workflows for logging, review queues and audit.
-- In production, give n8n a separate least-privilege role per schema instead of the admin user.

CREATE SCHEMA IF NOT EXISTS lab;

-- Lab 05: document extraction results and the human review queue
CREATE TABLE IF NOT EXISTS lab.extracted_documents (
  id            BIGSERIAL PRIMARY KEY,
  received_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  doc_id        TEXT NOT NULL,
  doc_type      TEXT,
  fields        JSONB NOT NULL,
  confidence    NUMERIC(4,3),
  status        TEXT NOT NULL CHECK (status IN ('auto_approved','needs_review','approved','rejected'))
);

-- Lab 07: agent tool-call log
CREATE TABLE IF NOT EXISTS lab.tool_call_log (
  id            BIGSERIAL PRIMARY KEY,
  logged_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  execution_id  TEXT,
  session_id    TEXT,
  tool_name     TEXT,
  tool_input    JSONB,
  tool_output   TEXT
);

-- Lab 09: approval audit trail
CREATE TABLE IF NOT EXISTS lab.approval_audit (
  id            BIGSERIAL PRIMARY KEY,
  logged_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  request_id    TEXT NOT NULL,
  action        TEXT NOT NULL,
  requested_by  TEXT,
  decision      TEXT NOT NULL CHECK (decision IN ('auto_approved','approved','rejected','timed_out')),
  decided_by    TEXT,
  notes         TEXT
);

-- Lab 12: LLM call telemetry and workflow errors
CREATE TABLE IF NOT EXISTS lab.llm_calls (
  id                BIGSERIAL PRIMARY KEY,
  logged_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  workflow          TEXT,
  execution_id      TEXT,
  model             TEXT,
  prompt_tokens     INTEGER,
  completion_tokens INTEGER,
  latency_ms        INTEGER,
  est_cost_usd      NUMERIC(12,6),
  status            TEXT,
  user_feedback     SMALLINT
);

CREATE TABLE IF NOT EXISTS lab.workflow_errors (
  id            BIGSERIAL PRIMARY KEY,
  logged_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  workflow      TEXT,
  execution_id  TEXT,
  node          TEXT,
  message       TEXT
);
