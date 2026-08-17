# Athena Tool Ecosystem

## Vision

Athena Tool Ecosystem provides independent tools that prepare, transform,
and enrich external data for Athena.

Core principle:

> Keep Athena Core stable. Put preparation complexity into external tools.

---

# Architecture Principle

External Software

        ↓

Athena Tool

        ↓

Athena Tool SDK

        ↓

Athena Knowledge Package (AKP)

        ↓

Athena Core


---

# Design Rules

## 1. Athena Core Protection

External tools must not:

- modify Athena architecture unnecessarily
- duplicate Athena intelligence
- bypass validation boundaries


## 2. Offline First

Tools should support:

- local processing
- user-owned data
- privacy by default


## 3. Provenance

Every generated knowledge package must record:

- source
- tool
- version
- creation information


## 4. Confidence Preservation

Imported information must preserve uncertainty.

AI-generated content is not treated as verified knowledge.

---

# Current Status

## Frozen Checkpoints

### T0.3-SDK-Freeze

Athena Tool SDK foundation.

Includes:

- AKP model
- validator
- serializer
- manifest
- provenance
- logging


### T0.4-DeepSeek-Importer-Freeze

First official ecosystem tool.

Features:

- DeepSeek export parsing
- conversation normalization
- AKP generation
- batch import
- CLI
- import reports

---

# Tool Inventory

| Tool | Status |
|---|---|
| athena-deepseek-importer | Frozen v0.1 |

---

# Roadmap

## T1 AI Memory Import Suite

Planned:

- ChatGPT importer
- Claude importer
- Gemini importer
- Social media importers


## T2 Personal Archive Tools

Planned:

- Email importer
- Notes importer
- Facebook importer
- Archive processors


## T3 Document Preparation Tools

Planned:

- PDF preparation
- OCR helpers
- Book processors


## T4 Research Intelligence Tools

Planned:

- Repository analyzer
- Code intelligence
- Research collectors


## A21 Tool Registry

Future:

Manage installed Athena tools.


## A22 Assistant Engine

Future:

Controlled assistant capabilities using:

- Athena Core
- Knowledge Workspace
- Tool Ecosystem

---

# Development Environment

Python:

3.14+

Virtual environment:

.venv

---

# Frozen Rule

Future tools must extend Athena without weakening
existing frozen capabilities.
