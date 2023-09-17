## To run my file, you can ignore 3,4,5 steps, which is only to change the sample model to our model

## In Terminal
## Step 1: Installation and Setup
First, you'll need to install Rasa. You can do this using pip:
#### pip install rasa

## Step 2: Create a New Rasa Project
Create a new directory for your chatbot project and navigate to it in your terminal:
#### mkdir my_chatbot
#### cd my_chatbot

Initialize a new Rasa project:
#### rasa init --no-prompt
This command will create the basic project structure with some sample data.

## In VSC
## Step 3: Define Your Chatbot's Domain
Edit the domain.yml file in your project directory to define the actions and responses your chatbot can handle. Here's a basic example:
#### version: 3.1"
#### intents:
####   - greet
####   - goodbye
#### responses:
####   utter_greet:
####     - text: "Hello! How can I assist you today?"
####   utter_goodbye:
####     - text: "Goodbye! Have a great day!"
#### actions:
####   - utter_greet
####   - utter_goodbye

## Step 4: Define Your NLU Data
Create a file called nlu.yml and define the intents and training examples for your chatbot. For example:
#### version: "3.1"
#### nlu:
#### - intent: greet
####   examples: |
####     - Hello
####     - Hi
####     - Hey there
#### - intent: goodbye
####   examples: |
####     - Goodbye
####     - Bye

## Step 5: Define Your Stories
Create a file called stories.yml to define the conversation flows your chatbot should follow. Here's a simple example:
#### version: "3.1"
#### stories:
#### - story: User greets and says goodbye
####   steps:
####     - intent: greet
####     - action: utter_greet
####     - intent: goodbye
####     - action: utter_goodbye

## Back to Terminal
## Step 6: Train Your Chatbot
Train your chatbot using the following command:
#### rasa train

## Step 7: Start the Chatbot's Server
Once training is complete, start the Rasa server:
#### rasa run -m models --enable-api --cors "*"
This will start a local server where you can interact with your chatbot via API.

## Open another Terminal window, when the previous one print (Rasa server is up and running)
## Step 8: Interact with Your Chatbot
You can interact with your chatbot through a REST API or a chat interface. Here's an example using the command line:
#### rasa shell
You can now type messages like "Hello" or "Goodbye," and your chatbot should respond based on the defined intents and responses.

## Step 9: Extend and Customize
You can extend and customize your chatbot by adding more intents, entities, actions, and responses to your domain and NLU data. You can also integrate external APIs or databases to make your chatbot more functional and interactive.

This is a basic example of creating a chatbot with Rasa. Rasa offers many advanced features for handling complex conversations, entity recognition, and more. You can refer to the Rasa documentation for more in-depth guidance and advanced features: Rasa Documentation.
