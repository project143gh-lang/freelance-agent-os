import os
import sys

sys.path.append("C:/Users/ADMIN/FreelanceOS")
from kernel.kernel import FreelanceKernel

def main():
    print("==================================================")
    print("      FREELANCE-OS (v0.3) - LOCAL BRAIN CORE      ")
    print("   Brain: Ollama (Local) | RAG Monitoring ON    ")
    print("==================================================")
    print("Commands:")
    print("  /persona <name>    - Switch role (closer, accountant, scout, researcher)")
    print("  /monitor <query>    - Query OS logs (RAG)")
    print("  /brain-status      - Check Local Model Health")
    print("  /set-model <name>   - Change the Brain model")
    print("  exit               - Shutdown OS")
    
    kernel = FreelanceKernel()
    
    while True:
        try:
            user_input = input("\nFreelanceOS >> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            if user_input.startswith("/monitor"):
                query = user_input.replace("/monitor ", "").strip()
                result = kernel.run(f"Query the monitor_service for: {query}")
                print(f"\n[MONITOR]: {result}")
                continue

            result = kernel.run(user_input)
            print(f"\nBrain: {result}")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
