Langflow + Chainlit Demo
==========================================================


### Overview
This is a simple demo of a chat application that integrates **Langflow** as a low-code backend and **Chainlit** as an interactive UI. The system enables users to retrieve information from specified documents using a vector database. 
It also includes authentication, persistence mechanisms, and user feedback integration.

The demo features:
- **Langflow** as the low-code backend for designing AI workflows.
- **Ollama** as the model provider (using `nomic-embed-text` for embeddings and `llama3.2-1b` for completion/generation).
- **ChromaDB** as a simple vector store.
- **Chainlit** as the frontend UI, supporting both **light and dark modes**.
- **Custom logo** stored in the `public` folder.
- **Chat history, persistence, and user feedback mechanisms** integrated via **Literal AI**.
- **User authentication** using an SQLite database.

---

### Sample Screenshots
#### Landing Page
![image](https://github.com/user-attachments/assets/efb6f501-d9ad-4b72-9fc1-428a14aff82d)

#### Sample Query (Dark Mode)
![image](https://github.com/user-attachments/assets/7f5a13f1-e00c-4aff-afdf-fc2c087b4dcd)

#### Sample Query (Light Mode)
![image](https://github.com/user-attachments/assets/a7080c4f-1b23-4042-964a-1c3722e51c80)

#### Langflow Workspace
![image](https://github.com/user-attachments/assets/d25fb267-45d8-4917-9065-7bc48d5cb9a2)

---

### Features
- **Low-Code Backend**: Langflow enables intuitive design and modification of AI workflows without writing extensive code.
- **Ollama LLMs**: Supports `nomic-embed-text` for vector search and `llama3.2-1b` for text generation.
- **ChromaDB Vector Store**: Simple and lightweight retrieval system for semantic search.
- **Chainlit UI**: Chatbot interface with real-time updates, supporting both light and dark themes.
- **Custom Branding**: Includes a personalized logo stored in the `public` folder.
- **Persistence & Feedback**: Stores chat history and integrates user feedback via **Literal AI**.
- **Authentication**: Uses SQLite to manage user credentials securely.

---

### Project Structure
```plaintext
📂 langflow-chainlit-sample
├── 📂 .chainlit/           # Chainlit configurations
├── 📂 public/              # Stores custom branding assets (e.g., logo)
├── .gitignore              # Git ignore rules
├── app.py                  # Chainlit main script
├── lf_python_api.py        # Langflow exported API script
├── init_db.py              # Script to initialize SQLite database
├── requirements.txt        # List of dependencies
├── start_backend.ps1       # Starts Langflow as backend
├── start_frontend.ps1      # Starts Chainlit as frontend
```

---

### Explanation of Scripts
- **`app.py`**: Runs the Chainlit UI, handling user interactions and responses from the backend.
- **`lf_python_api.py`**: Python code exported from Langflow, defining the AI processing flow.
- **`init_db.py`**: Example script to initialize the SQLite database and create a user table.
- **`start_backend.ps1`**: Starts Langflow as the backend service.
- **`start_frontend.ps1`**: Launches Chainlit as the frontend UI.

---

### How to Run

1. **Create a virtual environment and install dependencies**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   pip install -r requirements.txt
   ```

2. **Start Langflow to design your AI flow**:
   ```sh
   uv run langflow run
   ```
   - Modify your Langflow workspace as needed.
   - You can swap **ChromaDB** for another vector store or use different models.
   - Upload your docs via the Upload data flow.
   - Once satisfied, export the Python API code and replace `lf_python_api.py`.

3. **Set up environment variables**:
   Create a `.env` file with the following content:
   ```env
   LITERAL_API_KEY=your-literal-ai-key #Can get from your provisioned project @ cloud.getliteral.ai
   CHAINLIT_AUTH_SECRET=your-auth-secret
   FLOW_ID=your-langflow-flow-id
   ```

4. **Run the backend service (Langflow)**:
   ```sh
   ./start_backend.ps1
   ```

5. **Run the frontend (Chainlit UI)**:
   ```sh
   ./start_frontend.ps1
   ```

6. **Access the chatbot UI**:
   Open your browser and go to `http://localhost:8000` (or the configured Chainlit port).

---

### Credits
- **Langflow** for the low-code AI backend.
- **Ollama** for LLM inference models (`nomic-embed-text`, `llama3.2-1b`).
- **Chainlit** & **Literal AI**  for the conversational UI.












