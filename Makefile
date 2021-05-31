#SOCKETLIBS= -lnsl

#PTHREADLIBS= -lpthread

#PCAPLIBS= -lpcap

#CP=@CP@



CC=gcc

CFLAGS +=

LDFLAGS +=

SOCKETLIBS=

PTHREADLIBS=



all: hello hello2 hello3



hello: hello.c

        $(CC) $(CFLAGS) $(LDFLAGS) $(INCLUDEDIRS) -o $@ $(SOCKETLIBS)$(PTHREADLIBS) hello.c

hello2: hello2.c

        $(CC) $(CFLAGS) $(LDFLAGS) $(INCLUDEDIRS) -o $@ $(SOCKETLIBS)$(PTHREADLIBS) hello.c

hello3: hello3.c

        $(CC) $(CFLAGS) $(LDFLAGS) $(INCLUDEDIRS) -o $@ $(SOCKETLIBS)$(PTHREADLIBS) hello.c


clean:

        rm -f core hello

        rm -f *~ */*~