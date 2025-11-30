from scraper import scrape_data, TARGET_URL # Import your scraping function

def run_chatbot():
    print("🤖 Chatbot initialized. Type 'scrape' to get the latest data or 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["quit", "exit"]:
            print("🤖 Goodbye!")
            break

        elif user_input == "scrape":
            print("🤖 Fetching data now...")
            scraped_result = scrape_data(TARGET_URL)
            print(f"🤖 Result: {scraped_result}")

        else:
            # Simple static responses for other inputs
            print("🤖 I only know how to 'scrape' the website right now. Try typing that.")

if name == "main":
    run_chatbot()