
all:
	python3 -m pip install -r requirement.txt

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
