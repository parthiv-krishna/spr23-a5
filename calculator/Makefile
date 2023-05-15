OBJS = addition.o division.o main.o multiplication.o subtraction.o
TARGET = calculator
CC = gcc

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $^ -I. -o $@ 

$(OBJS): %.o:%.c
	cc -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJS)

.PHONY: clean