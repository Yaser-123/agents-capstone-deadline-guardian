# Deadline Guardian – Multi-Agent Productivity Assistant
**Track:** Concierge Agents  
**Author:** T Mohamed Yaser  

---

## 1. Problem
Most students struggle to organize tasks, manage deadlines, and break down work into small actionable steps. Without structure, tasks appear overwhelming and lead to delays, stress, and missed deadlines. Managing study schedules manually is time-consuming and inefficient.

## 2. Solution
Deadline Guardian is a lightweight multi-agent productivity assistant that automatically breaks tasks into steps, executes them in sequence, stores them in memory, and saves them using a custom tool. It demonstrates agent coordination, memory, tools, loops, and observability in a simple and reproducible way.

## 3. Why Agents?
Agents are ideal because the task naturally splits into planning, executing, and saving progress. A single monolithic script cannot demonstrate agent reasoning, memory, or tool usage. Multi-agent structure improves modularity and mirrors how real world workflows operate — a planner thinks, an executor performs actions, and a tool handles external storage.

## 4. Architecture
See architecture.png.

The system uses:
- MainAgent: orchestrates flow
- PlannerAgent: creates step-by-step tasks
- ExecutorAgent: loops through tasks sequentially
- Memory: in-memory dictionary
- SaveTaskTool: custom tool writing tasks to JSON

## 5. Key Features Implemented
- Multi-agent (main, planner, executor)
- Custom tool: save_task_tool
- Memory usage
- Basic observability (logging)

## 6. How It Works (Short Description)
1. User gives a request (e.g., “Plan my study schedule”).
2. MainAgent sends the request to PlannerAgent.
3. PlannerAgent generates task steps.
4. Tasks are stored in memory.
5. ExecutorAgent loops through tasks and simulates execution.
6. SaveTaskTool saves tasks to saved_tasks.json with logging.

## 7. How to Run
Run the system using:
python run.py
The script initializes all agents, processes a sample request, prints logs, and saves tasks.

## 8. Links
- GitHub Repository: https://github.com/Yaser-123/agents-capstone-deadline-guardian
- Notebook: (Optional)

## 9. Video Link (Optional but +10 points)
(Add later)

