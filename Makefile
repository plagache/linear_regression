
all:
	python3 -m pip install -r requirement.txt

# clean data
clean:
	rm -rf theta.csv
	cp base_theta.csv theta.csv

# clean also Binary
fclean: clean

visual:
	python3 graph.py

train: clean
	python3 training.py

predict:
	python3 predict.py

re:
	$(MAKE) fclean
	$(MAKE) all

FORCE:

.PHONY:
	all clean fclean re FORCE training visual
.SILENT:
