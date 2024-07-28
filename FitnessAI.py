import google.generativeai as genai
import gradio as gr

# Configure the API
api_key = '###'  # Replace with your actual API key
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel('gemini-pro')

messages = [{"author": "system", "content": "You are a personal fitness and training expert that specializes in various types of fitness activities that focus on a persons health and wellness"}]

def CustomChatGPT(user_input):
    try:
        messages.append({"author": "user", "content": user_input})

        # Prepare the complete conversation history for context
        conversation = "\n".join([f"{msg['author']}: {msg['content']}" for msg in messages])
        
        # Generate response using Google's Generative AI
        response = model.generate_content(conversation)
        ChatGPT_reply = response.text  # Assuming 'text' contains the generated content

        # Post-process the response to handle formatting issues
        ChatGPT_reply = ChatGPT_reply.replace("**", "")  # Remove bold formatting
        ChatGPT_reply = ChatGPT_reply.replace("* ", "• ")  # Replace asterisks with bullet points

        messages.append({"author": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        return str(e)

# Custom CSS for better aesthetics
custom_css = """
body {
    background-color: #f7f9fc;
    font-family: 'Arial', sans-serif;
}

.gradio-container {
    background-color: #313678;
    border: 1px solid #000000;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 20px;
    max-width: 800px;
    margin: auto;
}

.gradio-title {
    color: #333333;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 10px;
    text-align: center;
}

.gradio-interface {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.gradio-text-input, .gradio-output-text {
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
    border: 1px solid #cccccc;
    border-radius: 6px;
    padding: 10px;
    font-size: 16px;
    background-color: #f7f9fc;
    color: #333333;
}

.gradio-submit-button {
    background-color: #ab5d03;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
}

.gradio-submit-button:hover {
    background-color: #ab5d03;
}

.gradio-clear-button, .gradio-flag-button {
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
}

.gradio-clear-button:hover, .gradio-flag-button:hover {
    background-color: #5a6268;
}
"""

# Create a Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Personal Fitness Assistant",
    css=custom_css
)

# Launch the interface
demo.launch(share=True)
