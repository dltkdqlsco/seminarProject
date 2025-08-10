
CFLAGS  += -ggdb -Og -Wall -DDEBUG=1 -DUNUSEDRESULT_DEBUG= -I/opt/homebrew/Cellar/openssl@3/3.5.1/include
LDFLAGS += -L/opt/homebrew/Cellar/openssl@3/3.5.1/lib
LDLIBS  += -lssl -lcrypto

C_FILES := $(wildcard *.c)
EXECUTABLES := $(C_FILES:.c=)

default: $(EXECUTABLES)

clean:
	rm -f $(EXECUTABLES)
