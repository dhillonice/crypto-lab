# Drone Control System

A console-based **Drone Control System** developed in C for Lab Assignment 3. The project simulates basic drone mission management, including user login, waypoint upload, mission execution, telemetry monitoring, and mission-log storage.

The project also demonstrates common software security vulnerabilities and their detection using **Flawfinder Static Application Security Testing (SAST)**.

---

## 📌 Project Overview

The Drone Control System provides a simple command-line interface for controlling and monitoring a simulated drone.

The system allows a user to:

* Login to the drone control system
* Upload mission waypoints
* Execute a drone mission
* View simulated telemetry data
* Store mission information in log files

Along with implementing the basic functionality, the project intentionally demonstrates security vulnerabilities for educational analysis.

---

## ⚙️ Features

### 1. User Login

The system provides a basic login mechanism that allows an authorized user to access the drone control functions.

### 2. Waypoint Upload

Users can provide a set of waypoints that define the route to be followed by the drone.

Example:

```text
Waypoint 1: (10, 20)
Waypoint 2: (20, 30)
Waypoint 3: (30, 40)
```

### 3. Mission Execution

The drone can execute the uploaded mission by sequentially processing the configured waypoints.

### 4. Telemetry

The system displays simulated telemetry information during mission execution.

Telemetry may include information such as:

* Current position
* Current waypoint
* Mission status
* Drone state

### 5. Mission Logging

Mission-related information is stored in a log file for later analysis.

---

## 🔐 Security Analysis

A major part of this project is identifying security weaknesses in the Drone Control System.

The project demonstrates the following vulnerabilities:

### 1. Missing Authentication

Insufficient authentication can allow unauthorized users to access drone control functionality.

**Risk:**
An attacker may gain access to sensitive drone operations without proper authorization.

---

### 2. Buffer Overflow

Unsafe handling of user input can cause data to be written outside the allocated memory buffer.

**Risk:**

* Program crashes
* Memory corruption
* Unexpected behavior
* Potential code execution

---

### 3. Insecure File Handling

The application stores mission information in files.

Improper file handling can allow unauthorized modification or access to mission logs.

**Risk:**

* Sensitive information disclosure
* Log manipulation
* Unauthorized file access

---

## 🧪 Security Testing

**Flawfinder** is used to perform Static Application Security Testing (SAST).

Flawfinder analyzes C/C++ source code and identifies potentially dangerous functions and coding practices.

The generated report is stored in:

```text
sast/flawfinder_report.txt
```

---

## 📁 Project Structure

```text
Drone-Control-System/
│
├── src/
│   └── source code files
│
├── reports/
│   └── security analysis reports
│
├── screenshots/
│   └── project execution screenshots
│
├── sast/
│   └── flawfinder_report.txt
│
├── outputs/
│   └── mission_log.txt
│
├── testcases/
│   └── test_cases.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

* **Programming Language:** C
* **Interface:** Command Line / Console
* **Security Testing:** Flawfinder
* **Operating System:** Linux/Ubuntu
* **Version Control:** Git/GitHub

---

## 🧪 Testing

The project contains test cases covering:

* Valid login
* Invalid login
* Waypoint input
* Mission execution
* Telemetry
* Mission logging
* Invalid input
* Security vulnerability testing

Detailed test cases are available in:

```text
testcases/test_cases.txt
```

---

## 📊 Security Vulnerabilities Summary

| Vulnerability          | Description                  | Potential Impact             |
| ---------------------- | ---------------------------- | ---------------------------- |
| Missing Authentication | Insufficient access control  | Unauthorized drone control   |
| Buffer Overflow        | Unsafe memory/input handling | Crash or memory corruption   |
| Insecure File Handling | Unsafe file operations       | Data manipulation/disclosure |

---

## 📄 Output

Mission execution generates a mission log stored at:

```text
outputs/mission_log.txt
```

The log can be used to review the execution of the simulated drone mission.

---

## 👥 Group Members

| Name            | Roll Number |
| Nice Dhillon    | 2024ucp1367 |
| Siddhi Aggarwal | 2024ucp1385 |

---
