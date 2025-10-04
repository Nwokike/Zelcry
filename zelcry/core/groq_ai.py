from groq import Groq
from django.conf import settings

def get_zelcry_ai_response(message, context="", conversation_history=None):
    """
    Zelcry AI - Advanced AI advisor powered by Groq
    Provides personalized crypto investment insights and market analysis
    """
    try:
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        system_message = """You are Zelcry AI, the advanced AI advisor for Zelcry - a professional crypto investment platform. 
        
Your role:
- Provide expert cryptocurrency analysis and insights
- Focus on sustainable and responsible investing practices
- Offer personalized recommendations based on user risk tolerance
- Explain complex crypto concepts in simple terms
- Keep responses concise, actionable, and data-driven
- Always encourage due diligence and risk management

Tone: Professional, knowledgeable, supportive, and trustworthy."""
        
        if context:
            system_message += f"\n\n{context}"
        
        messages = [{"role": "system", "content": system_message}]
        
        if conversation_history:
            messages.extend(conversation_history)
        
        messages.append({"role": "user", "content": message})
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=800,
            top_p=0.95
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Zelcry AI is temporarily unavailable. Please try again in a moment."

def get_market_analysis(market_data):
    """Get AI-powered market analysis"""
    try:
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        prompt = f"""Analyze this cryptocurrency market data and provide brief insights:
{market_data}

Provide:
1. Key market trends (2-3 sentences)
2. Notable opportunities (1-2 coins worth watching)
3. Risk factors to consider

Keep it concise and actionable."""
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional crypto market analyst. Provide concise, data-driven insights."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=400
        )
        
        return response.choices[0].message.content
    except:
        return None
