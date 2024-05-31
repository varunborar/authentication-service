
PYTHON := venv/Scripts/python.exe

UVICORN := uvicorn

APP_MODULE := app.api.app:app

PORT := 8000

setup:
	python -m venv venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

tools:
	docker-compose -f docker-compose.dev.yml up -d

run:
	$(UVICORN) $(APP_MODULE) --reload --port $(PORT)

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	docker-compose -f docker-compose.dev.yml down
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

help:
	@echo "Makefile commands:"
	@echo "  setup     - Create a virtual environment and install dependencies"
	@echo "  run       - Start the FastAPI server with Uvicorn"
	@echo "  install   - Install Python dependencies"
	@echo "  clean     - Remove Python cache files"
	@echo "  help      - Show this help message"
