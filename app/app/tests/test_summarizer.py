from app.llms.openai_llm import load_llm
from app.agent.prompts.summarize import summarize_prompt

def test_summarize():
    role = "buyer"
    chat_history = """
    House Buyer (HB): Hello! I'm interested in buying a house, and I saw your listing online. Can you tell me more about the property?

    House Seller (HS): Hi there! Absolutely, I'd be happy to provide more information. It's a beautiful 3-bedroom, 2-bathroom house located in a quiet neighborhood with easy access to schools and parks. The property sits on a 0.25-acre lot and has a spacious backyard.

    HB: That sounds great! I'm particularly interested in the neighborhood. Can you tell me more about the community and the nearby amenities?

    HS: Of course! The neighborhood is known for being family-friendly, with a low crime rate and friendly neighbors. There are several schools nearby, both public and private, which makes it an ideal location for families with children. Additionally, there are parks within walking distance, perfect for outdoor activities and relaxation.

    HB: Excellent. How about the condition of the house? Has it undergone any recent renovations or updates?

    HS: The house is in good condition. We recently renovated the kitchen, adding new cabinets and countertops. The bathrooms have also been updated with modern fixtures. The roof was replaced last year, and we've installed energy-efficient windows throughout the house.

    HB: That's reassuring to hear. What about transportation and commuting options in the area?

    HS: The location is convenient for commuting. There are bus stops nearby, and the main highway is just a few minutes away. It's also easy to reach the train station, which provides access to the city center and other nearby areas.

    HB: Perfect. Now, let's talk about the price and any other expenses I should be aware of, such as property taxes or homeowner association fees.

    HS: The listing price is $350,000. As for property taxes, they amount to approximately $4,500 per year. There's no homeowner association in this neighborhood, so you won't have to worry about those fees.

    HB: That fits well within my budget. I'd like to schedule a visit to see the house in person. Can we arrange a time for that?

    HS: Certainly! I'm available most afternoons and weekends. How about this Saturday at 2:00 PM? That should give us enough time to explore the property and the neighborhood.

    HB: Sounds good to me. I'll see you on Saturday at 2:00 PM. Oh, before I forget, could you provide the address so I can plan my route?

    HS: Of course! I'll send you the address and some additional information via email. Is there anything specific you'd like to see or ask about during the visit?

    HB: I'd like to take a closer look at the backyard and check for any potential repairs or maintenance needed. Also, if you have any information on the average utility costs for the house, that would be helpful.

    HS: Noted! I'll make sure to have all that information ready for you when you visit. If you have any other questions before Saturday, feel free to reach out anytime.

    HB: Will do. Thanks for your assistance. Looking forward to seeing the house!

    HS: You're welcome! See you on Saturday. Have a great day!
    """
    llm = load_llm(max_tokens=300)
    response = llm(summarize_prompt.format_prompt(role=role, chat_history=chat_history).to_messages())
    print(response.content)

if __name__ == "__main__":
    test_summarize()
    