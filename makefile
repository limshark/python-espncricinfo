all:  tests ut 
	@echo "Running every thing"



.PHONY:     clean  tests ut all

tests:
	@echo "running tests...."
	poetry run python3 -m tests

ut:
	@echo "running additional Unit tests ...."
	poetry run python3 -m ut.ut1

clean:
	@echo "cleaning ...."
	@rm -rf ./__pycache__
	@rm -rf ut/__pycache__
    
