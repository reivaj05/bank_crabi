default: setup deps linter test

setup:
	chmod +x ./scripts/*.sh; sync
deps:
	./scripts/deps.sh
linter:
	./scripts/linter.sh
test: deps
	./scripts/tests.sh
