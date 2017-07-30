# use import to import modules
import hello

hello.say_hello("Sponge Bob")

#to import specific functions only
from hello import say_hello

#giving a function an alias
from hello import say_hello as sh

#giving an alias to a module
import hello as h

#import all functions in a module
from pizza import *
