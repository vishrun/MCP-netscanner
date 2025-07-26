# 🛡️ MCP-netscanner

**MCP-netscanner** is a lightweight, agent-ready network and security diagnostics toolkit built using [FastMCP](https://github.com/machine-cognition/fastmcp).  
It exposes essential scanning, inspection, and recon tools via MCP interfaces — perfect for LLM agents, internal security bots, or CLI automations.

---

## ✅ Features

### 🛰️ Network Reachability

- **`ping(domain)`**  
  Perform an ICMP ping to verify if a host is reachable.

---

### 🔎 Port & Service Scanning

- **`nmap_version(ip)`**  
  Run Nmap service/version detection (`-sV -p80` by default).

- **`nmap_os_detection(ip)`**  
  Detect operating system via Nmap OS fingerprinting (`-O`).

- **`nmap_quick_scan(ip)`**  
  Run a fast Nmap scan on common ports (`-T4 -F`).

---

### 🔐 SSL Certificate Inspection

- **`get_ssl_cert_info(domain, port=443)`**  
  Fetch and decode the SSL certificate of a target domain.  
  Returns:
  - Subject and issuer details  
  - Validity period (`valid_from`, `valid_to`)  
  - Serial number

---

### 💬 Utility

- **`greeting(name)`**  
  Returns a friendly greeting — useful to verify MCP setup.

---

## 🧑‍💻 Designed For

- Security engineers & analysts  
- Penetration testers  
- DevSecOps teams  
- LLM agents (Claude, GPT, Cursor, etc.) needing structured recon tools  
- Internal security bots (e.g., Slack, VS Code)

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/vishrun/MCP-netscanner.git
cd MCP-netscanner
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### Step 3: Install Required Python Packages
```bash
pip install -r requirements.txt
```

### Step 4: (Optional) Launch MCP Inspector
```bash
mcp dev main.py
```

### Step 5: Integrate with Claude / Cursor Agents
Edit the conf file
```
{
  "mcpServers": {
    "Security": {
      "command": "your/path/to/python",
      "args": [
        "your/path/to/server.py"
      ]
    }
  }
}

```
### Step 6: Restart Claude Desktop/ Cursor and start searching!
