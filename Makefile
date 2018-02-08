help: _help_

_help_:
	@echo make run - run development environment
	@echo make deploy - run production environment. Just debug is false

run:
	ln -sf ./app/configs/dev.py ./config.py

deploy:
	ln -sf ./app/configs/prod.py ./config.py
