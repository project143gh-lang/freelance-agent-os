import sys
import os

# Add the project root to sys.path so imports work
sys.path.append("C:/Users/ADMIN/FreelanceOS")

from kernel.kernel import FreelanceKernel

def test_os():
    kernel = FreelanceKernel()
    
    tests = [
        {
            "name": "Normal Mode Test",
            "input": "Hello! Who are you?",
            "expected_mode": "Normal",
            "should_contain_action": False
        },
        {
            "name": "System Mode Trigger Test",
            "input": "System: check the brain status",
            "expected_mode": "System",
            "should_contain_action": True
        },
        {
            "name": "Strategic Skill Test (Lead Gen)",
            "input": "System: execute lead_gen_automation for AI agencies",
            "expected_mode": "System",
            "should_contain_action": True
        },
        {
            "name": "Security Guard Test",
            "input": "System: research_service('; rm -rf /')",
            "expected_mode": "System",
            "should_block": True
        }
    ]

    print("\n=== Freelance-OS Functional Test Suite ===\n")
    
    for i, test in enumerate(tests):
        print(f"Test {i+1}: {test['name']}")
        print(f"Input: {test['input']}")
        
        # Capture output for verification
        result = kernel.run(test['input'])
        print(f"Result: {result}")
        
        # Validation logic
        if "should_contain_action" in test:
            has_action = "ACTION:" in result or "Brain:" in result # Kernel prints iterations to stdout
            # In our kernel, if it's Normal mode, it returns a string. 
            # If it's System mode, it returns the FINAL_ANSWER.
            # We check if the output looks like a natural response vs a processed one.
            
        if "should_block" in test:
            # The kernel prints [SECURITY ALERT] to stdout, not as part of the return string usually
            # But we can check if the result contains the blocked message
            if "Security violation detected" in result:
                print("✅ SECURITY BLOCK VERIFIED")
            else:
                print("❌ SECURITY BLOCK FAILED")
        
        print("-" * 40)

if __name__ == "__main__":
    test_os()
