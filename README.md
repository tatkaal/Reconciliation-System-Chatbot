# Rasa Chatbot API Backend

This repository contains the backend implementation for a chatbot using **Rasa**, an open-source conversational AI framework. The chatbot is designed to interact with users via a conversational interface and has an API endpoint for seamless integration.

## Project Overview

The project is structured to facilitate the training and deployment of a Rasa-based chatbot. It includes essential configurations, models, and database files necessary for conversational AI interactions. The chatbot is intended for **RBB Chatbot** and supports various functionalities through stories and API endpoints.

## Features
- **Conversational AI**: Built using Rasa for intent recognition and dialogue management.
- **API Integration**: Provides API endpoints for external systems to interact with the chatbot.
- **Database Storage**: Uses `rasa.db` for tracking conversation events and interactions.
- **Pre-trained Model**: A trained Rasa model included for quick deployment.
- **Custom Stories and Intents**: Predefined stories and responses for chatbot interaction.

## Project Structure

```
├── actions/           # Custom actions for chatbot responses
├── data/              # Training data for NLU and dialogue management
├── images/            # Project-related assets
├── models/            # Trained Rasa models
├── tests/             # Test files for chatbot validation
├── config.yml         # Configuration file for Rasa pipeline and policies
├── credentials.yml    # Authentication details for Rasa integrations
├── domain.yml         # Defines intents, entities, slots, and responses
├── endpoints.yml      # API endpoints for external communication
├── events.db          # Database file storing conversation history
├── requirements.txt   # Dependencies needed to run the project
├── story_graph.dot    # Visual representation of conversation flows
└── README.md          # Documentation for the project
```

## Installation & Setup

1. **Clone the repository**
```bash
git clone <repo-url>
cd rasa_chatbot
```

2. **Create a virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Train the chatbot model (if needed)**
```bash
rasa train
```

4. **Run the chatbot in interactive mode**
```bash
rasa shell
```

5. **Start the action server (for custom actions)**
```bash
rasa run actions
```

6. **Deploy the chatbot API**
```bash
rasa run --enable-api
```

## API Usage

Once the chatbot API is running, it provides endpoints to communicate with the chatbot:

- **POST `/webhooks/rest/webhook`** - Send user messages and receive chatbot responses.
  
  **Example request:**
  ```json
  {
    "sender": "user1",
    "message": "Hello"
  }
  ```

  **Example response:**
  ```json
  [
    {
      "recipient_id": "user1",
      "text": "Hi! How can I help you?"
    }
  ]
  ```

## Configuration Files

- **`config.yml`** - Defines the NLU pipeline and training policies.
- **`domain.yml`** - Contains intents, entities, slots, and responses.
- **`stories.yml`** - Defines conversation flows for training.
- **`endpoints.yml`** - Configures API endpoints for external communication.
- **`credentials.yml`** - Manages authentication for integrations.

## Database & Persistence

The project uses SQLite (`rasa.db` and `events.db`) to store conversation history and track interactions.

## Testing

To validate the chatbot’s responses and interactions:
```bash
rasa test
```

## Conclusion

This project provides a solid foundation for building a **Rasa-based chatbot API**. With trained models, predefined stories, and API integration, the chatbot can be deployed in production environments for real-time user interactions.

For further enhancements, consider:
- Adding more training data to improve intent recognition.
- Integrating with external services for enhanced responses.
- Deploying on cloud platforms for scalability.

Feel free to contribute and improve the chatbot! 🚀

