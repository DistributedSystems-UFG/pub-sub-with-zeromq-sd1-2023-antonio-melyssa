[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/09MEmU6P)
# Pub-Sub-Basics-with-ZeroMQ

This is a very simple pub-sub app implemented with ZeroMQ. Use it as an example for the pub-sub assignment (topic-based chat system).

# Group Messaging Application

This is a group messaging application implemented using RPyC (Remote Python Calls) and ZeroMQ. The application allows users to send direct messages to each other or send messages to a group.

## Features

- Direct Messaging: Users can send direct messages to other users.
- Group Messaging: Users can send messages to a group, and all members of the group will receive the message.
- Real-time Updates: Users receive messages in real-time without needing to refresh or manually check for new messages.
- Message History: Users can view the message history of the group.
- Automatic Filtering: The application filters out messages sent by the user from being displayed in the received messages.

## Prerequisites

- Python 3.7 or above
- RPyC library
- ZeroMQ library

## Installation

1. Clone the repository:

git clone https://github.com/your-username/group-messaging-app.git

2. Install the required dependencies:

pip install rpyc zmq

## Usage

1. Start the RPyC server:

python server.py

2. Start the messaging client:

python client.py

3. Choose the messaging option:

- To send a direct message, select "direct" and follow the prompts to enter your name, the recipient's name, and the message content.
- To send a group message, select "group" and enter your name. Then, enter the message content. All members of the group will receive the message.

4. Interact with the application:

- To exit the application, type "exit" when prompted for input.
- In a group messaging session, you will see messages from other users in real-time. Your own messages will be filtered out to avoid displaying them to you.

## Architecture

The group messaging application consists of two main components:

1. RPyC Server (`server.py`):
- The RPyC server implements the server-side functionality of the application.
- It exposes several methods that handle message sending, user registration, and message retrieval.
- The server runs on a specified port and listens for incoming connections from clients.

2. Messaging Client (`client.py`):
- The messaging client allows users to interact with the group messaging application.
- It provides an interactive command-line interface for sending messages.
- The client connects to the RPyC server using the specified host and port.
- It utilizes the ZeroMQ library to publish and subscribe to group messages.
