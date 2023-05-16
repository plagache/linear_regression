
all:
	python3 -m pip install -r requirement.txt

# clean data
clean:
	git restore thetas.csv
	rm -rf png/

# clean also gif
fclean: clean
	rm -rf training.gif

graph:
	# python3 graph.py
	# python3 graph.py -p
	# python3 graph.py -l
	# python3 graph.py -g
	python3 graph.py -pl
	# python3 graph.py -plg

train: clean
	python3 training.py

predict:
	python3 predict.py

re:
	$(MAKE) fclean
	$(MAKE) all

FORCE:

.PHONY:
	all clean fclean re FORCE train graph predict
.SILENT:
