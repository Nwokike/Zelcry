from groq import Groq
from django.conf import settings

def get_groq_response(message, context=""):
    try:
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        system_message = """You are Beacon, the AI advisor for Zelcry - a sustainable crypto investment platform. 
You help beginners understand cryptocurrencies, focusing on sustainability and responsible investing.
Be friendly, informative, and encourage eco-friendly choices. Keep responses concise and helpful."""
        
        if context:
            system_message += f"\n\nContext: {context}"
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=500
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"I'm having trouble connecting right now. Please try again in a moment."
