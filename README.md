# ONU Diagnostics & Automation Tool

A streamlined automation tool designed for Network Engineers to quickly diagnose fiber client status directly from the OLT (Optical Line Terminal) via an integrated web-scraping dashboard.

## Features
* **Automated Discovery**: Scrapes SmartOLT to extract ONU IDs, ports, and OLT mapping.
* **Direct Diagnostics**: Connects via Telnet to perform real-time checks on:
    * ONU Connection State (Online/Offline).
    * Optical Rx Power levels (dBm).
* **Actionable Insights**: Automatically calculates port health (online percentage) and suggests appropriate actions for NOC teams.
* **Secure Config**: Decouples sensitive credentials and IP addresses from the source code.

## Setup Instructions

### Prerequisites
* Python 3.9+
* Google Chrome installed
* ChromeDriver (matching your Chrome version)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/mazak3r/onu-checker.git](https://github.com/mazak3r/onu-checker.git)
   cd onu-checker

   ---

### 2. Project Description (for GitHub "About" section)

**Project Name:** ONU-Diagnostic-Toolkit

**Short Description:**
An automated network utility that bridges SmartOLT management with direct OLT hardware diagnostics. It utilizes Selenium for web-based discovery and asynchronous Telnet protocols to perform real-time signal strength analysis and ONU status verification. Built for ISP NOC teams to reduce ticket resolution time.

---

### Pro-Tips for your GitHub Repository:

1.  **The `.example` File:** Since you want to share this, create a file named `config.json.example`. This is a copy of your `config.json` but with placeholder data (e.g., `user: "admin"`). This allows people to see the *structure* of the file without you exposing your own passwords.
2.  **License:** If you plan to make this public, add an **MIT License** file. This is the industry standard for open-source projects.
3.  **Branching:** If you are actively working on features (like adding SSH support), create a `dev` branch so you don't break the main deployment.

**Would you like me to create the `LICENSE` file text or help you draft a shell script to automate the installation of dependencies?**
