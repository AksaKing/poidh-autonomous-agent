# 🚀 Poidh Autonomous Agent  
### Vision-Based Bounty Bot for Base Network

A fully autonomous agent that creates, monitors, and settles real-world bounties on the Base Network — without any human intervention. Built for the **poidh.xyz**.

---

## 🧠 Overview

This bot acts as a **Trustless Requester**, paying users to complete real-world tasks and verifying submissions using Multimodal AI (vision).

It bridges:
- **Off-chain intelligence (AI)**
- **On-chain execution (Base Network)**

---

## ✨ Core Features

- **🤖 Fully Autonomous**  
  No manual signing, no hardcoded IDs, no human approval required after deployment.

- **👁 Vision-Based Verification**  
  Uses `gpt-4o` (or compatible multimodal models) to validate image/video submissions.

- **⛓ On-Chain Settlement**  
  Direct interaction with **PoidhV3 smart contracts** on Base Mainnet.

- **📢 Social Transparency**  
  Automatically posts bounty creation, decisions, and results to **X (Twitter)** for public auditability.

---

## 🏗 Architecture

The agent operates in a continuous loop:

1. **Create Bounty**  
   Deploys a `createSoloBounty` transaction with a real-world task

2. **Parse Transaction Receipt**  
   Reads its own transaction result from the blockchain

3. **Extract Bounty ID**  
   Dynamically retrieves the generated bounty ID

4. **Broadcast to X**  
   Shares bounty details and participation link publicly

5. **Monitor Claims**  
   Listens for `ClaimCreated` events

6. **Fetch Proof (IPFS)**  
   Retrieves submitted images/videos

7. **AI Vision Evaluation**  
   Validates whether the task is completed correctly

8. **On-Chain Settlement**  
   Calls `acceptClaim` if valid

9. **Post Result to X**  
   Publishes final outcome for transparency

---

## 🤖 Autonomy Design

- **🔍 Dynamic ID Extraction**  
  Parses blockchain receipts to track bounties automatically

- **🧾 Binary AI Decisions**  
  AI outputs strict JSON:
  ```json
  { "is_valid": true/false }
  ```

- **💰 Self-Funded Execution**  
  Uses its own EOA wallet

- **🔁 Infinite Loop Execution**  
  Runs continuously via polling loop

---

## 📦 Setup & Installation

### Prerequisites

- Python 3.10+
- Funded Base Mainnet wallet (≥ 0.002 ETH recommended)
- OpenAI API Key
- X (Twitter) API keys

---

### Installation

```bash
git clone https://github.com/AksaKing/poidh-autonomous-agent.git
cd poidh-autonomous-agent
pip install -r requirements.txt
```

---

### Environment Variables

Create `.env` file:

```env
RPC_URL=https://mainnet.base.org
PRIVATE_KEY=your_wallet_private_key_here

OPENAI_API_KEY=your_openai_api_key_here
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL_NAME=gpt-4o

X_API_KEY=your_x_api_key
X_API_SECRET=your_x_api_secret
X_ACCESS_TOKEN=your_x_access_token
X_ACCESS_SECRET=your_x_access_secret
```

---

### Run

```bash
python main.py
```

---

## ⚠️ Security Notes

- Never expose private keys
- Use environment variables
- Prefer secure deployment (VPS / Docker)