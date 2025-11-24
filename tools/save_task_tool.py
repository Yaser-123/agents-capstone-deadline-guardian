# save_task_tool.py
# Custom tool for saving tasks - required by Kaggle

import json

class SaveTaskTool:
	def __init__(self, file_path="saved_tasks.json"):
		self.file_path = file_path

	def save(self, tasks):
		"""
		Saves tasks into a JSON file.
		This simulates a custom tool that interacts with external resources.
		"""

		print("[SaveTaskTool] Saving tasks to", self.file_path)

		with open(self.file_path, "w") as f:
			json.dump({"tasks": tasks}, f, indent=4)

		print("[SaveTaskTool] Save complete!")
