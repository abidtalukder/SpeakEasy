import dotenv from 'dotenv';
import openai from 'openai';

// Activate the dotenv configuration
dotenv.config();

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

// Initialize the OpenAI API client
const client = new openai.OpenAIAPI({ apiKey: OPENAI_API_KEY });

// Function to make a request to the OpenAI GPT-3 API
async function callChatGPT(prompt) {
  try {
    const completion = await client.complete({
      engine: 'davinci',
      prompt: prompt,
      maxTokens: 150,
    });
    return completion.choices[0].text.trim();
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}

// Example prompt to test the function
const examplePrompt = "Once upon a time";

callChatGPT(examplePrompt)
  .then((response) => {
    console.log('Generated response:', response);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
