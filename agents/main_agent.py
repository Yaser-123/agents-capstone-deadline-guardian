# main_agent.py
# Skeleton for the Main Agent of Deadline Guardian

class MainAgent:
	def __init__(self, planner, executor, memory):
		self.planner = planner
		self.executor = executor
		self.memory = memory

	def run(self, user_input):
		"""
		Main entry point for the agent.
		1. Receive user request
		2. Send to planner agent
		3. Save planned tasks to memory
		4. Run executor agent loop
		"""

		print("[MainAgent] Received user input:", user_input)

		# Step 1: Plan tasks
		tasks = self.planner.plan_tasks(user_input)
		print("[MainAgent] Tasks generated:", tasks)

		# Step 2: Save tasks to memory
		self.memory["tasks"] = tasks

		# Step 3: Execute tasks
		self.executor.execute_tasks(tasks)

		return "Execution complete"
