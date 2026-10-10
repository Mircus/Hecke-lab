.PHONY: test examples lint

test:
	pytest

examples:
	python examples/agent_move_composition.py
	python examples/document_workflow.py
	python examples/theorem_workflow.py

lint:
	ruff check src tests examples
