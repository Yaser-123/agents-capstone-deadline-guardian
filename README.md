# Deadline Guardian – Multi-Agent Productivity Assistant

![Profile Image](https://avatars.githubusercontent.com/u/140265777?v=4)

**Author:** T Mohamed Yaser

- LinkedIn: https://www.linkedin.com/in/mohamedyaser08/
- X: https://x.com/tmohamedyaser
- Demo video: https://youtu.be/UsJGCvIqCKA

## 1. Overview
Deadline Guardian is a multi-agent system that helps users plan tasks, break work into steps, and track progress using memory, tools, and agent loops.

This project is built for the **Kaggle Agents Intensive – Capstone Project**.

## 2. Features (Required by Kaggle)
- Multi-Agent System: main agent, planner agent, executor agent  
- Tools: custom save_task tool  
- Memory: simple memory storage  
- Observability: basic logging  

## 3. Folder Structure


agents/
main_agent.py
planner_agent.py
executor_agent.py
tools/
save_task_tool.py
README.md
submission.md
architecture.png


## 4. How to Run

### 1. Clone the repository


git clone <your-repo-url>
cd <your-folder>


### 2. Run the demo script


python run.py


### 3. Expected Output
- The system will:
	- Read user input inside `run.py`
	- PlannerAgent creates tasks
	- Tasks stored in memory
	- ExecutorAgent executes tasks in a loop
	- SaveTaskTool saves tasks to `saved_tasks.json`

You will see logs printed in the console showing the multi-agent workflow.


This section is required for Documentation (20 points).

## 5. Architecture Diagram
See `architecture.png` (will be added soon).

## 6. Deployment (For Kaggle Bonus Points)

You can deploy Deadline Guardian to Cloud Run by following these steps:

### 1. Build the Docker image
```bash
docker build -t deadline-guardian .
```

### 2. Run locally (optional)
```bash
docker run deadline-guardian
```

### 3. Deploy to Cloud Run
```bash
gcloud run deploy deadline-guardian \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

The service will run the agent pipeline automatically.
No API keys are stored in the image. Gemini API key must be supplied at runtime using:
```bash
--set-env-vars GEMINI_API_KEY=<your-key>
```

