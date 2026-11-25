
.PHONY: install test lint format clean

# Install project and development dependencies
install:
	pip install -e ".[dev]"

# Run automated tests
test:
	pytest tests/

# Check code quality
lint:
	ruff check .

# Format Python code
format:
	ruff format .

# Remove Python cache files
clean:
	powershell -Command "Get-ChildItem -Path . -Filter __pycache__ -Recurse -Directory | Remove-Item -Recurse -Force"
