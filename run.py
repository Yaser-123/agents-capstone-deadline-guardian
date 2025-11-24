# run.py
# Connects all agents + tool and runs a full pipeline

from agents.main_agent import MainAgent
from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from tools.save_task_tool import SaveTaskTool

def main():
    # Initialize agents
    planner = PlannerAgent()
    executor = ExecutorAgent()
    
    # Simple in-memory dictionary as required for memory feature
    memory = {}

    # Initialize main agent
    main_agent = MainAgent(planner, executor, memory)

    # User test input
    user_input = "Plan my study schedule for this week"

    # Run the system
    result = main_agent.run(user_input)

    # Use custom tool to save tasks
    save_tool = SaveTaskTool()
    save_tool.save(memory["tasks"])

    print("\nFinal Output:", result)

if __name__ == "__main__":
    main()
