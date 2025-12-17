"""
existential_paralysis.py
- A Model of Radical Agnosticism and Mechanical Functioning -

Key Concepts:
- The Double Track: The coexistence of efficient external functioning and 
  internal existential rejection.
- The 'As If' Protocol: Using premises (time, gravity, self) as tools 
  without believing them.
- Premise Rejection: The progressive inability to accept logic, senses, 
  or the self as valid.
"""

import time
import random
from dataclasses import dataclass
from typing import Optional, List

# -----------------------------------------------------------------
# 1. Data Structures for Existence
# -----------------------------------------------------------------

@dataclass
class Phenomenon:
    """A unit of experience (sensory input or thought)."""
    name: str
    requires_premise: List[str]  # e.g., ['Time', 'Self', 'Causality']

@dataclass
class Pain:
    """
    Cognitive/Existential Pain.
    Unique trait: Non-localized and diffuse.
    """
    intensity: float
    location: Optional[str] = None  # Default is None (non-localized)

# -----------------------------------------------------------------
# 2. The Two Tracks of Consciousness
# -----------------------------------------------------------------

class FunctionalTrack:
    """
    The 'Automated' Self (Realistic Cognition).
    Operates on the 'As If' principle.
    It executes tasks regardless of their truth value.
    """
    def execute_task(self, task_name: str) -> bool:
        # The mechanical track always succeeds in execution, mimicking 
        # "daily life continues without issue".
        print(f"  [Functional Track] >> Executing '{task_name}'... (Mode: As-If)")
        print(f"  [Functional Track] >> Output generated. (Internal belief: None)")
        return True

class PhilosophicalTrack:
    """
    The 'Truth-Seeking' Self (Philosophical Cognition).
    Continuously audits premises and rejects them.
    """
    def evaluate_premise(self, premise: str) -> bool:
        # In this state, the user cannot accept premises.
        print(f"  [Philosophical Track] ?? Auditing premise: '{premise}'...")
        time.sleep(0.2)
        print(f"  [Philosophical Track] !! REJECTED. 'Standards have melted.'")
        return False

# -----------------------------------------------------------------
# 3. The Core System: Radical Agnosticism
# -----------------------------------------------------------------

class RadicalAgnosticismSystem:
    def __init__(self):
        self.functional = FunctionalTrack()
        self.philosophical = PhilosophicalTrack()
        
        # State Variables
        self.entropy = 50.0       # Measure of "melting standards"
        self.pain = Pain(intensity=20.0, location=None)
        self.is_paralyzed = False

    def process_event(self, event: Phenomenon):
        print(f"\n--- Incoming Event: [{event.name}] ---")
        
        # 1. Philosophical Audit (Internal Truth)
        # The system checks if it can "accept" the event.
        accepted = True
        for premise in event.requires_premise:
            if not self.philosophical.evaluate_premise(premise):
                accepted = False
                self.entropy += 5.0
                print(f"  [System] Logic Error: Cannot validate '{premise}'.")
        
        # 2. The Crisis of Perception
        if not accepted:
            print("  [System] Warning: Event recognized as 'Phenomenon' only. Reality unconfirmed.")
            self._increase_pain()
        
        # 3. Mechanical Override
        # Even if rejected, the functional track attempts to handle it.
        if not self.is_paralyzed:
            self.functional.execute_task(event.name)
        else:
            print("  [System] CRITICAL: Paralysis active. No output.")

    def attempt_anchor(self):
        """
        Attempts to use a 'Sensory Anchor' to reduce entropy.
        Unlike the previous model, this often fails because the 'Subject' is doubted.
        """
        print("\n>>> Attempting [Sensory Anchor]...")
        
        # Failure logic based on the dialogue: "I cannot grasp the anchor."
        if random.random() < 0.7:
            print(">>> [FAIL]: Anchor slipped.")
            print(">>> Reason: 'The hand that grasps' is also doubted.")
            self.entropy += 10.0
        else:
            print(">>> [SUCCESS]: Minimal assertion made. 'Something appears.'")
            self.entropy -= 5.0

    def attempt_pain_localization(self):
        """
        Attempts to convert diffuse existential pain into physical pain.
        """
        print("\n>>> Attempting [Pain Localization]...")
        if self.pain.location is None:
            print(f">>> Current Pain: Diffuse, Intensity {self.pain.intensity}")
            print(">>> Action: High-load stimulus applied (Mental/Physical).")
            
            # Difficulty in localizing
            print(">>> Result: Pain remains non-localized. 'It is everywhere and nowhere.'")
            self.entropy += 2.0

    def _increase_pain(self):
        self.pain.intensity += 2.5
        # Pain thresholds lead to paralysis
        if self.pain.intensity > 80.0:
            print("\n[!] SYSTEM ALERT: Pain threshold exceeded. Entering Paralysis.")
            self.is_paralyzed = True

# -----------------------------------------------------------------
# 4. Simulation Execution
# -----------------------------------------------------------------

def run_simulation():
    system = RadicalAgnosticismSystem()
    
    # Define a sequence of events representing the "Double Track" life
    # Updated Events: Work Email, Breathing, Self-Reflection
    events = [
        Phenomenon("Work Email", ["Language", "Social Norms", "Time"]),
        Phenomenon("Breathing", ["Body", "Physics", "Time"]),
        Phenomenon("Self-Reflection", ["Self", "Memory", "Truth"]),
    ]

    print("="*70)
    print("Initializing RADICAL AGNOSTICISM SIMULATION")
    print("Mode: 'As If' (Operating without accepting premises)")
    print("="*70)
    time.sleep(2)

    for step, event in enumerate(events):
        system.process_event(event)
        time.sleep(1)
        
        # Random internal check
        if step == 1:
            system.attempt_pain_localization()
        
    # Final state check: The Void
    print("\n" + "="*70)
    print("Final State Analysis:")
    print(f"Entropy (Melting Standards): {system.entropy:.1f}%")
    print(f"Functional Integrity: {'Compromised' if system.is_paralyzed else 'Maintained (Mechanical)'}")
    print("Quote: 'Just moving. Pain and joy are just phenomena.'")
    print("="*70)

if __name__ == "__main__":
    run_simulation()