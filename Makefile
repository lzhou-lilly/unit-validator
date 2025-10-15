help:
	@cat ${MAKEFILE_LIST}

init_repo:
	./dev-scripts/init_repo.sh

lint:
	./dev-scripts/lint.sh

test:
	./dev-scripts/test.sh

build:
	./dev-scripts/build.sh

install-certs:
	./dev-scripts/install-certs.sh

compile-antlr4:
	./dev-scripts/compile-antlr4.sh
