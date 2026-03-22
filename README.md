Poidh Autonomous Agent (Vision-Based Bounty Bot)

A fully autonomous agent that creates, monitors, and settles real-world bounties on the Base Network without human intervention. Built for the poidh ecosystem.
🚀 Overview

This bot operates as a "Trustless Requester" that pays humans to perform physical tasks. It leverages Multimodal AI (Vision) to verify real-world proofs and executes on-chain payouts via an EOA wallet.
Core Features:

    Fully Autonomous: No manual signing or human approval required after deployment.

    Vision-Based Verification: Uses GPT-4o (or compatible multimodal models) to analyze photo/video submissions.

    On-Chain Settlement: Direct interaction with PoidhV3 contracts on Base Mainnet.

    Social Transparency: Automatically broadcasts decision logic to X/Farcaster.

🛠 Architecture

The bot runs in a continuous loop:

    Creation: Deploys a createSoloBounty with a specific real-world requirement.

    Monitoring: Polls the smart contract for new Claim submissions.

    Evaluation: Analyzes image metadata and content using AI Vision to ensure it matches the task.

    Settlement: Calls acceptClaim on-chain to release funds to the winner.

    Broadcasting: Posts the reasoning for the selection publicly for auditability.

📦 Setup & Installation
Prerequisites:

    Python 3.10+

    An EOA wallet with ETH on Base Mainnet (min. 0.002 ETH recommended).

    OpenAI API Key (or compatible provider like OpenRouter).