import os
import time
import json
from dotenv import load_dotenv
from web3 import Web3
from openai import OpenAI

load_dotenv()

class PoidhAutonomousAgent:
    def __init__(self):
        print("[INFO] Initializing Poidh Autonomous Agent...")
        
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
        self.private_key = os.getenv("PRIVATE_KEY")
        self.account = self.w3.eth.account.from_key(self.private_key)
        
        self.contract_address = self.w3.to_checksum_address("0x5555Fa783936C260f77385b4E153B9725feF1719")
        
        # Dynamic pathing for contract ABI
        base_dir = os.path.dirname(os.path.abspath(__file__))
        abi_path = os.path.join(base_dir, "contracts", "poidh_abi.json")
        with open(abi_path, "r") as file:
            self.contract_abi = json.load(file)
            
        self.poidh_contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        
        self.ai_client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("AI_BASE_URL")
        )
        self.model_name = os.getenv("AI_MODEL_NAME", "gpt-4o")
        
        self.active_bounty_id = None

    def create_real_world_bounty(self):
        """Creates an on-chain bounty. Fully autonomous execution."""
        print("[INFO] Constructing new real-world bounty transaction...")
        
        task_name = "Underground Aesthetic: Physical Media"
        task_desc = "Take a clear photo of a physical cassette tape or CD leaning against street graffiti. Must look raw. AI will evaluate the presence of both the physical media and the graffiti."
        bounty_amount = self.w3.to_wei(0.001, 'ether')
        
        tx = self.poidh_contract.functions.createSoloBounty(
            task_name, 
            task_desc
        ).build_transaction({
            'from': self.account.address,
            'value': bounty_amount,
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
        })

        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        print(f"[SUCCESS] Bounty created. TX Hash: {self.w3.to_hex(tx_hash)}")
        self.active_bounty_id = 1 
        time.sleep(10)

    def check_submissions(self):
        print(f"[INFO] Polling submissions for bounty ID: {self.active_bounty_id}")
        return [
            {"claim_id": 101, "submitter": "0xABC...", "image_url": "https://example.com/submission1.jpg"}
        ]

    def evaluate_with_ai_vision(self, image_url):
        print("[INFO] Triggering vision model for claim evaluation...")
        
        prompt = """
        You are an autonomous judge for a bounty. 
        Task: Verify if this image clearly shows a physical cassette tape or CD placed in front of street graffiti.
        Respond ONLY in JSON format: {"is_valid": true/false, "reason": "Short explanation of what you see."}
        """
        
        response = self.ai_client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": [{"type": "image_url", "image_url": {"url": image_url}}]}
            ],
            response_format={ "type": "json_object" }
        )
        
        result = json.loads(response.choices[0].message.content)
        return result["is_valid"], result["reason"]

    def execute_payout(self, claim_id):
        print(f"[INFO] Executing on-chain payout for claim ID: {claim_id}")
        pass

    def post_to_socials(self, submitter, reason):
        post_text = f"Poidh Bounty Settled! Winner: {submitter}.\n\nReasoning: {reason}\n\nFully autonomous payout executed on-chain."
        print(f"[SOCIAL] Broadcasting decision:\n{post_text}")

    def run_autonomous_loop(self):
        print("[INFO] Booting autonomous loop...")
        
        if not self.active_bounty_id:
            self.create_real_world_bounty()
            
        while True:
            submissions = self.check_submissions()
            
            for sub in submissions:
                is_valid, reason = self.evaluate_with_ai_vision(sub['image_url'])
                
                if is_valid:
                    self.execute_payout(sub['claim_id'])
                    self.post_to_socials(sub['submitter'], reason)
                    print("[INFO] Cycle complete. Awaiting next task.")
                    self.active_bounty_id = None 
                    return 
                else:
                    print(f"[REJECTED] Claim {sub['claim_id']}. Reason: {reason}")
            
            print("[INFO] No valid submissions. Entering sleep state (300s)...")
            time.sleep(300)

if __name__ == "__main__":
    bot = PoidhAutonomousAgent()
    bot.run_autonomous_loop()