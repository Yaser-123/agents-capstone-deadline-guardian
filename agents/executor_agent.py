# executor_agent.py
# Skeleton for the Executor Agent in Deadline Guardian

import time

class ExecutorAgent:
	def __init__(self):
		pass

	def execute_tasks(self, tasks):
		"""
		Executes tasks sequentially.
		Acts as a loop agent — required for the Kaggle features list.
		"""

		print("[ExecutorAgent] Starting task execution...")

		for task in tasks:
			print(f"[ExecutorAgent] Working on: {task}")
			time.sleep(0.5)  # Simulate some work loop

		print("[ExecutorAgent] All tasks completed.")
