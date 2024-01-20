# Run pre-commit to all files
.PHONY: check
check:
	@pre-commit run --all-files