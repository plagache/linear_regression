
all:
	python3 -m pip install -r requirement.txt

train:
	git restore theta.csv
	./linear_regression.py

predict:
	./predict.py

# clean only source
clean:

# clean also Binary
fclean:

re:
	$(MAKE) fclean
	$(MAKE) all

FORCE:

.PHONY:
	all clean fclean re FORCE
.SILENT:
