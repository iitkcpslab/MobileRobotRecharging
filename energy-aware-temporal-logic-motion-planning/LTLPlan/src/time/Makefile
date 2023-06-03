
CC = g++
CFLAGS = -Wall -c
LFLAGS = -Wall


UTILS_DIR = ../utils
SAFE_DIR = ../safe
LTLPARSER_DIR = ../ltlparser
LTL_DIR = ../ltl


OBJS_UTILS = $(UTILS_DIR)/primitive.o $(UTILS_DIR)/readinputs.o $(UTILS_DIR)/writeconstraints.o  $(UTILS_DIR)/extractoutput.o
OBJS_SAFE = $(SAFE_DIR)/writespecificationconstraints.o
OBJS_LTLPARSER = $(LTLPARSER_DIR)/generateloopconstraints.o
OBJS_LTL = $(LTL_DIR)/ltlmotionplanning.o
OBJS_Z3 = $(OBJS_UTILS) $(OBJS_SAFE) $(OBJS_LTLPARSER) $(OBJS_LTL) definepropositions.o
#OBJS_Z3 = $(OBJS_UTILS) $(OBJS_SAFE) $(OBJS_LTLPARSER) $(OBJS_LTL) definepropositions.o stlmotionplanning.o


all: util safe ltlparser ltl tool_z3


tool_z3 : $(OBJS_Z3)
	$(CC) $(LFLAGS) $(OBJS_Z3) -o tool_z3

definepropositions.o : $(UTILS_DIR)/primitive.h $(UTILS_DIR)/readinputs.h  $(UTILS_DIR)/extractoutput.o definepropositions.h definepropositionspostoffice.cpp
	$(CC) $(CFLAGS) definepropositionspostoffice.cpp
	mv definepropositionspostoffice.o definepropositions.o

#definepropositions.o : $(UTILS_DIR)/primitive.h $(UTILS_DIR)/readinputs.h definepropositions.h definepropositionschemicals.cpp
#	$(CC) $(CFLAGS) definepropositionschemicals.cpp
#	mv definepropositionschemicals.o definepropositions.o
 
#stlmotionplanning.o : $(UTILS_DIR)/primitive.h $(UTILS_DIR)/readinputs.h $(SAFE_DIR)/writespecificationconstraints.h $(LTLPARSER_DIR)/generateloopconstraints.h definepropositions.h stlmotionplanning.cpp
#	$(CC) $(CFLAGS) stlmotionplanning.cpp


util : 
	$(MAKE) -C $(UTILS_DIR)


safe : 
	$(MAKE) -C $(SAFE_DIR) writespecificationconstraints.o


ltlparser:
	$(MAKE) -C $(LTLPARSER_DIR) generateloopconstraints.o


ltl:
	$(MAKE) -C $(LTL_DIR) ltlmotionplanning.o



.PHONY: clean
clean : 
	rm -f *.o
	rm -f tool_*
	$(MAKE) -C $(UTILS_DIR) clean
	$(MAKE) -C $(SAFE_DIR) clean
	$(MAKE) -C $(LTLPARSER_DIR) clean 
	$(MAKE) -C $(LTL_DIR) clean
