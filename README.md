# basic-go-backdoor
Educational****

# 🐀 Simple Go-based Remote Access Tool (RAT)

> ⚠️ This project is intended **strictly for educational and ethical penetration testing purposes only.** Do not use it without authorization.

## 📚 Description

This is a lightweight Remote Access Tool (RAT) written in Go. It establishes a reverse TCP connection from the victim machine back to a Command-and-Control (C2) server. The tool allows the operator to run shell commands, navigate the filesystem, download/upload files, capture screenshots, and maintain persistence via crontab.

---

## ⚙️ Features

- Remote shell execution
- Directory navigation (`cd`)
- File upload and download via base64 encoding
- Screenshot capture (via `kbinani/screenshot`)
- Basic persistence (crontab on Linux)
- Auto-reconnect mechanism to the C2 server

---

## 🚀 Setup

### ✅ Prerequisites

- Go (v1.18 or higher recommended)
- Git
- Linux/macOS/Windows (GUI required for screenshot capture)

### 📦 Installation

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
go mod tidy  # Ensure all dependencies are installed
go build -o client main.go

