# AI-Agents
# LangChain with Google Generative AI and Tavily Search in Colab

This notebook demonstrates how to use LangChain with Google Generative AI and Tavily Search in Google Colab.

## Description

This code utilizes the `langchain_google_genai` and `tavily-python` libraries to interact with Google Generative AI and Tavily Search, respectively. It showcases how to:

1. **Install necessary libraries:** Installs `langchain-community`, `langchain-core`, `langchain_google_genai`, and `tavily-python` using `pip`.
2. **Initialize Google Generative AI:** Sets up the `ChatGoogleGenerativeAI` class with the Gemini API key.
3. **Invoke Google Generative AI:** Sends a query to Google Generative AI and prints the response.
4. **Use LangChain Messages:** Demonstrates the use of `HumanMessage` and `AIMessage` to create a conversation with Google Generative AI.
5. **Initialize Tavily Search:** Sets up the `TavilySearchResults` class with the Tavily API key.
6. **Invoke Tavily Search:** Sends a search query to Tavily Search and prints the result.

## Requirements

- Google Colab environment
- Python 3
- `langchain-community`, `langchain-core`, `langchain_google_genai`, and `tavily-python` libraries (installed via `pip`)
- Gemini API key (stored in Colab userdata)
- Tavily API key (stored in Colab userdata)

## Usage

1. Open the notebook in Google Colab.
2. Store your Gemini API key and Tavily API key in Colab userdata using `userdata.set('GEMINI_API_KEY', 'your_gemini_api_key')` and `userdata.set('TAVILY_API_KEY', 'your_tavily_api_key')`, respectively.
3. Run the code cells in the notebook.
4. Observe the responses from Google Generative AI and Tavily Search.

## Contributing

Contributions are welcome! Please open an issue or pull request if you have any suggestions or improvements.

## License

This code is licensed under the MIT License.
