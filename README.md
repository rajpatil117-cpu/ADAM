# ADAM 🤖

A fully local AI assistant for Android, powered by Qwen3 and llama.cpp.

## Current Status

🚧 Under active development

ADAM is being built as a privacy-focused, zero-cost personal AI assistant that runs locally on an Android device.

### Milestone 1 — Local LLM ✅

- Android development environment using Termux
- Local LLM inference using llama.cpp
- Qwen3 0.6B Q4_0 GGUF model
- Successful inference entirely on-device
- No paid API or cloud LLM required

## Planned Features

- 💬 Conversational assistant
- 🧠 Persistent memory
- 🎤 Voice input
- 🔊 Voice responses
- 📱 Android device integration
- 🛠️ Tool execution
- 🔐 Permission and safety controls

## Architecture

```text
User
 │
 ▼
ADAM
 │
 ├── Local LLM
 │     └── Qwen3
 │
 ├── Memory
 │     └── SQLite
 │
 ├── Tools
 │     └── Android / Termux APIs
 │
 └── Voice
       ├── Speech-to-Text
       └── Text-to-Speech



