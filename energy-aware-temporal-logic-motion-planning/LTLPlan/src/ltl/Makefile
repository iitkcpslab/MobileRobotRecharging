
CC = g++
CFLAGS = -Wall -c
LFLAGS = -Wall


UTILS_DIR = ../utils
LTLPARSER_DIR = ../ltlparser


OBJS_UTILS = $(UTILS_DIR)/primitive.o $(UTILS_DIR)/readinputs.o $(UTILS_DIR)/writeconstraints.o $(UTILS_DIR)/generatetrajectory.o $(UTILS_DIR)/extractoutput.o
OBJS_LTL = $(LTLPARSER_DIR)/generateloopconstraints.o
OBJS_Z3 = $(OBJS_UTILS) $(OBJS_SAFE) $(OBJS_LTL) definepropositions.o ltlmotionplanning.o


all: util ltlparser tool_z3


tool_z3 : $(OBJS_Z3)
	$(CC) $(LFLAGS) $(OBJS_Z3) -o tool_z3

definepropositions.o : $(UTILS_DIR)/primitive.h $(UTILS_DIR)/readinputs.h definepropositions.h definepropositions.cpp
	$(CC) $(CFLAGS) definepropositions.cpp

ltlmotionplanning.o : $(UTILS_DIR)/primitive.h $(UTILS_DIR)/readinputs.h $(UTILS_DIR)/extractoutput.h $(UTILS_DIR)/writeconstraints.h $(LTLPARSER_DIR)/generateloopconstraints.h definepropositions.h ltlmotionplanning.cpp
	$(CC) $(CFLAGS) ltlmotionplanning.cpp


util : 
	$(MAKE) -C $(UTILS_DIR)

ltlparser:
	$(MAKE) -C $(LTLPARSER_DIR) generateloopconstraints.o


.PHONY: clean
clean : 
	rm -f *.o
	rm -f tool_*
	$(MAKE) -C $(UTILS_DIR) clean
	$(MAKE) -C $(LTLPARSER_DIR) clean 
