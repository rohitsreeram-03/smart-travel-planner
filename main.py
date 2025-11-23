import os
from dotenv import load_dotenv
from gemini_client import generate_text

def build_prompt(destination, days, style, interests):
    return (
        f"You are an expert travel planner. Create a {days}-day itinerary for {destination}. "
        f"Travel style: {style}. Interests: {interests}. Include schedule, attractions, foods, packing tips, budget."
    )

def main():
    load_dotenv()
    print("=== Simple Travel Planner — Gemini ===")
    destination = input("Destination: ").strip()
    days = int(input("Days: ").strip() or 3)
    style = input("Travel style: ").strip() or "relaxed"
    interests = input("Interests: ").strip() or "sightseeing"

    prompt = build_prompt(destination, days, style, interests)
    print("Generating plan...")
    plan = generate_text(prompt)

    print("\n--- Travel Plan ---\n")
    print(plan)

    with open("plan.txt", "w", encoding="utf-8") as f:
        f.write(plan)

    print("\nSaved to plan.txt")

if __name__ == "__main__":
    main()
